#!/usr/bin/env python3
"""Check an answer exactly as Ledgerly will. Standard library only.

  python3 tools/check.py <job-id>        check jobs/outbox/<job-id>/
  python3 tools/check.py --all           check every answer in jobs/outbox/
  python3 tools/check.py <job-id> --json print the result as JSON (used by Ledgerly)

Exit code 0 = PASS (warnings allowed), 1 = FAIL.
"""
import json, os, re, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA_DIR = os.path.join(ROOT, "schema")

# ---------------------------------------------------------------- helpers

def load_json(path, problems):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        problems.append(f"missing file {os.path.relpath(path, ROOT)}")
    except json.JSONDecodeError as e:
        problems.append(f"{os.path.relpath(path, ROOT)} is not valid JSON: {e}")
    return None


def norm(text):
    """Case, accents, spacing and punctuation don't matter, but words do. LaTeX is flattened, so a quote
    like '1/5 + 2/5' still matches a passage that reads '1/5+2/5'."""
    text = unicodedata.normalize("NFKD", text or "").lower()
    text = re.sub(r"\\frac\{([^}]*)\}\{([^}]*)\}", r"\1/\2", text)
    text = re.sub(r"\\(times|div|cdot)", lambda m: {"times": "x", "div": "/", "cdot": "x"}[m.group(1)], text)
    text = re.sub(r"[^a-z0-9]+", "", text)
    return text


SCHEMAS = {}

def schema(name):
    if name not in SCHEMAS:
        with open(os.path.join(SCHEMA_DIR, f"{name}.schema.json"), encoding="utf-8") as f:
            SCHEMAS[name] = json.load(f)
    return SCHEMAS[name]


TYPES = {"object": dict, "array": list, "string": str, "integer": int, "number": (int, float), "boolean": bool, "null": type(None)}

def validate(value, sch, where, problems):
    """A small JSON Schema subset: type, required, properties, additionalProperties, items, enum,
    minLength/maxLength, minimum/maximum, minItems/maxItems, pattern, $ref."""
    if "$ref" in sch:
        return validate(value, schema(sch["$ref"]), where, problems)
    if "type" in sch:
        kinds = sch["type"] if isinstance(sch["type"], list) else [sch["type"]]
        ok = any(isinstance(value, TYPES[k]) and not (k in ("integer", "number") and isinstance(value, bool)) for k in kinds)
        if not ok:
            problems.append(f"{where}: expected {' or '.join(kinds)}, got {type(value).__name__}")
            return
    if "enum" in sch and value not in sch["enum"]:
        problems.append(f"{where}: {value!r} is not one of {sch['enum']}")
    if isinstance(value, str):
        if len(value) < sch.get("minLength", 0): problems.append(f"{where}: too short")
        if len(value) > sch.get("maxLength", 10**9): problems.append(f"{where}: too long ({len(value)} > {sch['maxLength']})")
        if "pattern" in sch and not re.fullmatch(sch["pattern"], value): problems.append(f"{where}: {value!r} doesn't match {sch['pattern']}")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if value < sch.get("minimum", -10**18): problems.append(f"{where}: {value} < {sch['minimum']}")
        if value > sch.get("maximum", 10**18): problems.append(f"{where}: {value} > {sch['maximum']}")
    if isinstance(value, list):
        if len(value) < sch.get("minItems", 0): problems.append(f"{where}: needs at least {sch['minItems']} items")
        if len(value) > sch.get("maxItems", 10**9): problems.append(f"{where}: at most {sch['maxItems']} items")
        if "items" in sch:
            for i, item in enumerate(value): validate(item, sch["items"], f"{where}[{i}]", problems)
    if isinstance(value, dict):
        for key in sch.get("required", []):
            if key not in value: problems.append(f"{where}: missing '{key}'")
        props = sch.get("properties", {})
        for key, item in value.items():
            if key in props: validate(item, props[key], f"{where}.{key}", problems)
            elif sch.get("additionalProperties") is False: problems.append(f"{where}: unknown field '{key}'")
            elif isinstance(sch.get("additionalProperties"), dict): validate(item, sch["additionalProperties"], f"{where}.{key}", problems)

# ---------------------------------------------------------------- passages

PASSAGE_RE = re.compile(r"<!--\s*passage\s+(\S+)[^>]*-->(.*?)<!--\s*/passage\s*-->", re.S)

def load_passages(job, job_dir):
    # The job's own passages.md first, then the pack, so a passage is attributed to its source file in the pack.
    files = []
    extra = os.path.join(job_dir, "passages.md")
    if os.path.exists(extra): files.append(extra)
    pack = os.path.join(ROOT, job.get("pack", ""), "sources")
    if os.path.isdir(pack):
        files += [os.path.join(pack, f) for f in sorted(os.listdir(pack)) if f.endswith(".md") and f != "INDEX.md"]
    passages = {}
    for path in files:
        with open(path, encoding="utf-8") as f:
            for pid, text in PASSAGE_RE.findall(f.read()):
                passages[pid] = {"text": text, "norm": norm(text), "file": os.path.basename(path)}
    return passages


class Cites:
    def __init__(self, passages, allowed):
        self.passages, self.allowed, self.used = passages, set(allowed or passages.keys()), []

    def check(self, cite, where, problems):
        if not isinstance(cite, dict): return
        pid, quote = cite.get("source", ""), cite.get("quote", "")
        if pid not in self.passages:
            problems.append(f"{where}: source '{pid}' is not a passage in this job's pack"); return
        q = norm(quote)
        if len(q) < 6 or q not in self.passages[pid]["norm"]:
            problems.append(f"{where}: quote not found in {pid} (invented?): \"{quote[:80]}\"")
        if len(quote.split()) > 25:
            problems.append(f"{where}: quote is longer than 25 words")
        self.used.append(self.passages[pid]["file"])

# ---------------------------------------------------------------- notes

SOURCE_COMMENT = re.compile(r"<!--\s*source:\s*(\S+)\s+\"([^\"]+)\"\s*-->")
INSTRUCTION_PHRASES = re.compile(r"\b(?:discuss(?:ing)?|in (?:your|their|small) groups?|tell (?:the|a|your) (?:story|partner|class)|sing (?:a |the )?songs?|act out|dramati[sz]e|read (?:it |this |these |the passages? )?(?:aloud|with your teacher)|say (?:each|the|these) words?|think (?:of|about) a|with your teacher|your teacher will)\b", re.I)
MIN_WORDS = {1: 80, 2: 120, 3: 160, 4: 200, 5: 240, 6: 280, 7: 320}
EXAMPLE_SUBJECTS = re.compile(r"math|english|reading|literacy|phonics", re.I)


def check_latex(text, where, problems):
    plain = re.sub(r"\\\$", "", text)
    if plain.count("$") % 2: problems.append(f"{where}: unbalanced $ (LaTeX)")
    for m in re.finditer(r"\$\$?(.+?)\$\$?", plain, re.S):
        if m.group(1).count("{") != m.group(1).count("}"): problems.append(f"{where}: unbalanced braces in ${m.group(1)[:40]}$")


def check_notes(text, lesson, job, cites, figures, activities, problems, warnings):
    where = f"{lesson['id']}.notes.md"
    kind, level, subject = lesson.get("kind", "teach"), job.get("classLevel") or 4, job.get("subject", "")
    body = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    words = len(re.findall(r"[^\W_][\w'’-]*", body))
    minimum = MIN_WORDS.get(level, 200) if kind == "teach" else 120 if kind == "assessment" else 70
    if words < minimum: problems.append(f"{where}: notes too short ({words} words; need {minimum} for P{level})")
    if kind == "teach" and not re.search(r"^##\s+SUB-TOPIC", text, re.M | re.I):
        problems.append(f"{where}: needs '## SUB-TOPIC: …'")
    if kind == "teach" and not re.search(r"^#\s+TOPIC", text, re.M | re.I):
        problems.append(f"{where}: needs '# TOPIC: …'")
    if kind != "assessment" and not re.search(r"^###\s+Exercise", text, re.M | re.I):
        problems.append(f"{where}: must end with '### Exercise'")
    found = sorted({m.lower() for m in INSTRUCTION_PHRASES.findall(body)})
    if found: problems.append(f"{where}: classroom instructions belong in the plan, not the notes ({', '.join(found[:5])})")
    has_example = re.search(r"^###\s+(?:Worked\s+)?Examples?\b", text, re.M | re.I)
    if EXAMPLE_SUBJECTS.search(subject):
        if kind in ("teach", "practice") and not has_example:
            problems.append(f"{where}: {subject} lessons need '### Example' sections taken from the sources")
    elif has_example:
        problems.append(f"{where}: Example sections are only for Mathematics, English and Reading")
    # Every section (except New words) carries at least one source comment; every exercise line carries one.
    sections = re.split(r"^(?=###\s)", text, flags=re.M)
    for sec in sections:
        head = sec.splitlines()[0] if sec.strip() else ""
        if not head.startswith("###") or re.match(r"###\s+New words", head, re.I): continue
        if re.match(r"###\s+Exercise", head, re.I):
            lines = [l for l in sec.splitlines()[1:] if re.match(r"\s*\d+[.)]\s", l)]
            if len(lines) < 3 and kind != "assessment": problems.append(f"{where}: Exercise needs at least 3 numbered questions")
            for l in lines:
                if not SOURCE_COMMENT.search(l): problems.append(f"{where}: exercise line has no source: {l.strip()[:60]}")
            if activities is not None and len(lines) > len(activities):
                problems.append(f"{where}: Exercise has {len(lines)} questions but activities.json has {len(activities)}")
        elif not SOURCE_COMMENT.search(sec):
            problems.append(f"{where}: section '{head[4:60]}' has no <!-- source: … --> comment")
    for pid, quote in SOURCE_COMMENT.findall(text):
        cites.check({"source": pid, "quote": quote}, where, problems)
    for key in re.findall(r"\[\[diagram:([a-z0-9-]+)\]\]", text):
        if key not in figures: problems.append(f"{where}: [[diagram:{key}]] has no figures/{key}.json")
    check_latex(body, where, problems)
    paragraphs = [norm(p) for p in body.split("\n\n") if len(norm(p)) > 60]
    if len(set(paragraphs)) < len(paragraphs): problems.append(f"{where}: repeated paragraphs")


def check_plan(plan, lesson, cites, problems, warnings):
    where = f"{lesson['id']}.plan.json"
    validate(plan, schema("plan"), where, problems)
    if not isinstance(plan, dict): return
    total = sum(s.get("minutes", 0) for s in plan.get("steps", []) if isinstance(s, dict))
    want = 40 * int(lesson.get("periods") or 1)
    if abs(total - want) > 5: problems.append(f"{where}: steps add up to {total} minutes; the lesson is {want}")
    for i, step in enumerate(plan.get("steps", [])):
        if isinstance(step, dict) and "source" in step: cites.check(step["source"], f"{where}.steps[{i}]", problems)
        text = json.dumps(step).lower() if isinstance(step, dict) else ""
        if re.search(r"\b(story|song|sing|poem|rhyme|drama|role play|demonstrat)", text) and not (isinstance(step, dict) and "source" in step):
            problems.append(f"{where}.steps[{i}]: a story/song/demonstration needs a source")


def check_activities(acts, lesson, job, cites, problems, warnings):
    where = f"{lesson['id']}.activities.json"
    validate(acts, schema("activities"), where, problems)
    if not isinstance(acts, list): return
    level, kind = job.get("classLevel") or 4, lesson.get("kind", "teach")
    need = 15 if kind == "assessment" else min(5, max(3, level - 1)) if kind == "teach" else 3
    if len(acts) < need: problems.append(f"{where}: {len(acts)} activities; need at least {need}")
    seen = set()
    for i, a in enumerate(acts):
        if not isinstance(a, dict): continue
        cites.check(a.get("source"), f"{where}[{i}]", problems)
        if a.get("answerOrigin") == "worked" and not EXAMPLE_SUBJECTS.search(job.get("subject", "")) and "math" not in job.get("subject", "").lower():
            warnings.append(f"{where}[{i}]: 'worked' answers are meant for Mathematics")
        if a.get("answer") is None and a.get("answerOrigin") != "none": problems.append(f"{where}[{i}]: answer is null but answerOrigin isn't 'none'")
        if a.get("kind") == "multiple_choice" and len(a.get("options") or []) < 2: problems.append(f"{where}[{i}]: multiple-choice needs options")
        q = norm(a.get("question", ""))
        if q in seen: problems.append(f"{where}[{i}]: duplicate question")
        seen.add(q)
        check_latex(a.get("question", "") + " " + (a.get("answer") or ""), f"{where}[{i}]", problems)


CODED = {
    "shape": {"shape"}, "fraction": {"shape", "numerator", "denominator"}, "number-line": {"from", "to", "step"},
    "clock": {"hour", "minute"}, "map": {"layers"}, "bar-chart": {"bars"}, "column-sum": {"operation", "numbers"},
    "long-division": {"dividend", "divisor"}, "angle": {"degrees"}, "venn": {"sets"},
}

def check_figures(answer_dir, lesson_ids, cites, problems):
    figures = {}
    fig_dir = os.path.join(answer_dir, "figures")
    if not os.path.isdir(fig_dir): return figures
    for name in sorted(os.listdir(fig_dir)):
        if not name.endswith(".json"): continue
        where = f"figures/{name}"
        fig = load_json(os.path.join(fig_dir, name), problems)
        if not isinstance(fig, dict): continue
        validate(fig, schema("figure"), where, problems)
        key = fig.get("key", "")
        if name != f"{key}.json": problems.append(f"{where}: file name must be <key>.json")
        if fig.get("lesson") not in lesson_ids: problems.append(f"{where}: lesson '{fig.get('lesson')}' is not in this job")
        cites.check(fig.get("source"), where, problems)
        method = fig.get("method")
        if method == "coded":
            spec = fig.get("coded") or {}
            t = spec.get("type")
            if t not in CODED: problems.append(f"{where}: coded type must be one of {sorted(CODED)}")
            elif not CODED[t] <= set(spec): problems.append(f"{where}: coded {t} needs {sorted(CODED[t])}")
        elif method == "svg":
            svg_path = os.path.join(fig_dir, f"{key}.svg")
            if not os.path.exists(svg_path): problems.append(f"{where}: method svg needs figures/{key}.svg")
            else:
                svg = open(svg_path, encoding="utf-8").read()
                if "<svg" not in svg: problems.append(f"figures/{key}.svg is not an SVG")
                if re.search(r"<script|<image|href=\"http", svg, re.I): problems.append(f"figures/{key}.svg: no scripts, embedded images or links")
                colours = set(re.findall(r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b", svg)) - {"#000", "#000000", "#fff", "#ffffff", "#FFF", "#FFFFFF"}
                if colours: problems.append(f"figures/{key}.svg: black and white only (found {', '.join(sorted(colours)[:3])})")
        elif method == "illustration" and not fig.get("concept"):
            problems.append(f"{where}: an illustration needs 'concept' (what to draw)")
        figures[key] = fig
    return figures

# ---------------------------------------------------------------- job

def check_job(job_id):
    problems, warnings = [], []
    job_dir = os.path.join(ROOT, "jobs", "inbox", job_id)
    answer_dir = os.path.join(ROOT, "jobs", "outbox", job_id)
    job = load_json(os.path.join(job_dir, "job.json"), problems)
    if not isinstance(job, dict):
        return problems or [f"job {job_id} not found in jobs/inbox"], warnings
    if not os.path.isdir(answer_dir):
        return [f"no answer yet: jobs/outbox/{job_id}/"], warnings
    passages = load_passages(job, job_dir)
    if not passages: problems.append("no passages found for this job (pack missing?)")
    cites = Cites(passages, job.get("passages"))
    meta = load_json(os.path.join(answer_dir, "meta.json"), problems)
    if meta is not None:
        validate(meta, schema("meta"), "meta.json", problems)
        if isinstance(meta, dict) and meta.get("attempt") != job.get("attempt", 1):
            problems.append(f"meta.json: attempt is {meta.get('attempt')} but the job is on attempt {job.get('attempt', 1)}")
    kind = job.get("kind")
    lessons = job.get("lessons", [])
    lesson_ids = {l["id"] for l in lessons}

    if kind == "scheme.outline":
        scheme = load_json(os.path.join(answer_dir, "scheme.json"), problems)
        if isinstance(scheme, dict):
            validate(scheme, schema("scheme"), "scheme.json", problems)
            weeks = int(job.get("weeks") or 0)
            per_week = {}
            for u, unit in enumerate(scheme.get("units", [])):
                if not isinstance(unit, dict): continue
                for c, cite in enumerate(unit.get("sources", [])): cites.check(cite, f"scheme.json units[{u}].sources[{c}]", problems)
                for l, lesson in enumerate(unit.get("lessons", [])):
                    if not isinstance(lesson, dict): continue
                    for c, cite in enumerate(lesson.get("sources", [])): cites.check(cite, f"scheme.json units[{u}].lessons[{l}].sources[{c}]", problems)
                    w = lesson.get("week")
                    if isinstance(w, int):
                        per_week[w] = per_week.get(w, 0) + 1
                        if weeks and w > weeks: problems.append(f"scheme.json units[{u}].lessons[{l}]: week {w} is after the last week ({weeks})")
            ppw = job.get("periodsPerWeek")
            if ppw:
                for w, n in sorted(per_week.items()):
                    if n > ppw: problems.append(f"scheme.json: week {w} has {n} lessons but the subject has {ppw} periods a week")
    elif kind in ("lesson.write", "lesson.plan"):
        figures = check_figures(answer_dir, lesson_ids, cites, problems) if kind == "lesson.write" else {}
        for lesson in lessons:
            base = os.path.join(answer_dir, lesson["id"])
            plan = load_json(base + ".plan.json", problems)
            if plan is not None: check_plan(plan, lesson, cites, problems, warnings)
            if kind == "lesson.plan": continue
            acts = load_json(base + ".activities.json", problems)
            if acts is not None: check_activities(acts, lesson, job, cites, problems, warnings)
            try:
                notes = open(base + ".notes.md", encoding="utf-8").read()
                check_notes(notes, lesson, job, cites, figures, acts if isinstance(acts, list) else None, problems, warnings)
            except FileNotFoundError:
                problems.append(f"missing file {lesson['id']}.notes.md")
        extra = {f.split(".")[0] for f in os.listdir(answer_dir) if f.endswith((".notes.md", ".plan.json", ".activities.json"))} - lesson_ids
        if extra: problems.append(f"files for lessons not in this job: {', '.join(sorted(extra))}")
    elif kind == "figure.generate":
        key = job.get("figureKey", "")
        png = os.path.join(answer_dir, f"{key}.png")
        if not os.path.exists(png): problems.append(f"missing {key}.png")
        elif open(png, "rb").read(8) != b"\x89PNG\r\n\x1a\n": problems.append(f"{key}.png is not a PNG")
    else:
        problems.append(f"unknown job kind {kind!r}")

    if cites.used and kind == "lesson.write":
        top = max(set(cites.used), key=cites.used.count)
        share = cites.used.count(top) / len(cites.used)
        if share > 0.7 and len(set(f for f in cites.used)) < len({p["file"] for p in passages.values()}):
            warnings.append(f"variety: {share:.0%} of citations come from {top}; use more of the pack")
    return problems, warnings


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    as_json = "--json" in sys.argv
    if "--all" in sys.argv:
        out = os.path.join(ROOT, "jobs", "outbox")
        args = sorted(d for d in os.listdir(out) if os.path.isdir(os.path.join(out, d)))
    if not args:
        print(__doc__); sys.exit(2)
    failed = False
    results = {}
    for job_id in args:
        problems, warnings = check_job(job_id)
        results[job_id] = {"pass": not problems, "problems": problems, "warnings": warnings}
        failed |= bool(problems)
        if not as_json:
            print(f"{'PASS' if not problems else 'FAIL'}  {job_id}")
            for p in problems: print(f"  ✗ {p}")
            for w in warnings: print(f"  ! {w}")
    if as_json: print(json.dumps(results, indent=1))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
