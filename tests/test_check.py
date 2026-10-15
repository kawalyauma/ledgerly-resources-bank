#!/usr/bin/env python3
"""Self-test for tools/check.py: a tiny P4 Mathematics job with one good and several bad answers."""
import json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

PASSAGES = """# Primary Four Mathematics Notes (sample)
<!-- passage lsch_t1 part 1 -->
Adding fractions with the same denominator. When the denominators are the same, add the numerators and keep the denominator.
Example: 1/5 + 2/5 = 3/5. Example: 2/9 + 4/9 = 6/9.
A fraction is part of a whole. The top number is the numerator and the bottom number is the denominator.
When we add fractions with the same denominator, the size of each part does not change, so the denominator stays the same. Only the number of parts changes, so we add the numerators.
<!-- /passage -->
<!-- passage lsch_t2 part 4 -->
Exercise 4B. Add: (a) 2/7 + 3/7 (b) 1/9 + 4/9 (c) 3/11 + 5/11 (d) 1/4 + 2/4. Answers: (a) 5/7 (b) 5/9 (c) 8/11 (d) 3/4.
Use fraction bars to show 3/5 by shading three parts out of five equal parts.
<!-- /passage -->
"""

JOB = {"job": "test-job", "task": "ltsk_test", "call": 0, "kind": "lesson.write", "status": "open", "attempt": 1,
       "school": "sch-test", "class": "P4", "classLevel": 4, "subject": "Mathematics", "term": "2026-T3", "week": 1,
       "pack": "library/sch-test/2026-T3/P4/mathematics", "passages": ["lsch_t1", "lsch_t2"],
       "lessons": [{"id": "lles_t1", "title": "Adding fractions", "subtopic": "Same denominator", "kind": "teach", "week": 1, "periods": 1}]}

S1 = '<!-- source: lsch_t1 "add the numerators and keep the denominator" -->'
NOTES = f"""# TOPIC: FRACTIONS
## SUB-TOPIC: Adding fractions with the same denominator

### Meaning of a fraction
- A **fraction** is part of a whole.
- The top number is the **numerator**.
- The bottom number is the **denominator**.
<!-- source: lsch_t1 "A fraction is part of a whole" -->

### Rule
- When the denominators are the same, add the numerators and keep the denominator.
{S1}
1. Look at the denominators. They must be the same.
2. Add the top numbers, which are the numerators, to get the new numerator.
3. Write the same denominator under the answer and do not add the bottom numbers.

### Why the denominator stays the same
- When we add fractions with the same denominator, the size of each part does not change.
- So the **denominator stays the same**.
- Only the number of parts changes, so we add the **numerators**.
- Fifths added to fifths still give fifths; ninths added to ninths still give ninths.
<!-- source: lsch_t1 "the size of each part does not change, so the denominator stays the same" -->

### Example 1
$\\frac{{1}}{{5}} + \\frac{{2}}{{5}} = \\frac{{3}}{{5}}$ because one fifth and two fifths together make three fifths of the same whole.
<!-- source: lsch_t1 "1/5 + 2/5 = 3/5" -->

[[diagram:fraction-bar-3-5]]

### Example 2
$\\frac{{2}}{{9}} + \\frac{{4}}{{9}} = \\frac{{6}}{{9}}$ because two ninths and four ninths together make six ninths of the same whole.
<!-- source: lsch_t1 "2/9 + 4/9 = 6/9" -->

### Exercise
1. $\\frac{{2}}{{7}} + \\frac{{3}}{{7}}$ <!-- source: lsch_t2 "Add: (a) 2/7 + 3/7" -->
2. $\\frac{{1}}{{9}} + \\frac{{4}}{{9}}$ <!-- source: lsch_t2 "(b) 1/9 + 4/9 (c)" -->
3. $\\frac{{3}}{{11}} + \\frac{{5}}{{11}}$ <!-- source: lsch_t2 "(c) 3/11 + 5/11" -->
4. $\\frac{{1}}{{4}} + \\frac{{2}}{{4}}$ <!-- source: lsch_t2 "(d) 1/4 + 2/4. Answers" -->
"""

def act(q, a, quote):
    return {"question": q, "answer": a, "answerOrigin": "source", "kind": "computation", "difficulty": 2,
            "cognitiveLevel": "apply", "source": {"source": "lsch_t2", "quote": quote}}

ACTS = [act("$\\frac{2}{7} + \\frac{3}{7}$", "$\\frac{5}{7}$", "Add: (a) 2/7 + 3/7"), act("$\\frac{1}{9} + \\frac{4}{9}$", "$\\frac{5}{9}$", "(b) 1/9 + 4/9 (c)"),
        act("$\\frac{3}{11} + \\frac{5}{11}$", "$\\frac{8}{11}$", "(c) 3/11 + 5/11"), act("$\\frac{1}{4} + \\frac{2}{4}$", "$\\frac{3}{4}$", "(d) 1/4 + 2/4. Answers")]

PLAN = {"competences": ["The learner adds fractions with the same denominator.", "The learner explains why the denominator stays the same."],
        "languageCompetence": "Pronounces, spells and writes: fraction, numerator, denominator.",
        "objectives": ["By the end of the lesson, learners should be able to add two fractions with the same denominator.",
                       "By the end of the lesson, learners should be able to explain why the denominator does not change."],
        "priorKnowledge": "Learners already know that a fraction is part of a whole and can name the numerator and denominator.",
        "methods": ["Explanation", "Question and answer", "Guided practice"], "materials": ["Fraction bars", "Chart of fifths and ninths"],
        "references": ["Primary Four Mathematics Notes (sample)"],
        "steps": [{"stage": "Introduction", "minutes": 5, "teacherActivity": "The teacher holds up a fraction bar and asks: 'What is the top number called?' and 'What does the bottom number tell us?' to revise the meaning of a fraction.", "learnerActivity": "Learners name the numerator and the denominator of the fractions the teacher shows."},
                  {"stage": "Development: the rule", "minutes": 10, "content": "Rule: when the denominators are the same, add the numerators and keep the denominator.", "teacherActivity": "The teacher writes the rule on the board and explains, with the fraction bars, why the size of each part does not change so the denominator stays the same.", "learnerActivity": "Learners read the rule aloud together and shade parts of fraction bars to show it."},
                  {"stage": "Development: worked examples", "minutes": 10, "content": "Example 1: 1/5 + 2/5 = 3/5. Example 2: 2/9 + 4/9 = 6/9.", "teacherActivity": "The teacher works Examples 1 and 2 on the board, asking after each step: 'What do we add?' and 'What happens to the denominator?'", "learnerActivity": "Learners answer the questions at each step and copy the worked examples into their books."},
                  {"stage": "Practice", "minutes": 12, "content": "Exercise: add 2/7 + 3/7, 1/9 + 4/9, 3/11 + 5/11 and 1/4 + 2/4.", "teacherActivity": "The teacher writes the exercise on the board, marks learners' work as they finish and helps those who add the denominators by mistake.", "learnerActivity": "Learners add the four pairs of fractions in their books and correct their mistakes."},
                  {"stage": "Conclusion", "minutes": 3, "teacherActivity": "The teacher summarises the rule and asks: 'What is 1/5 + 2/5?' and 'Why does the denominator stay the same?' to check understanding.", "learnerActivity": "Learners answer the oral questions and say the rule together."}],
        "assessment": "Oral questions (What is 1/5 + 2/5? Why does the denominator stay the same?) and the written exercise of four sums, marked in class.",
        "homework": "Add 2/7 + 4/7 and 1/9 + 5/9 in your book.",
        "lifeSkills": ["Critical thinking", "Accuracy"]}

FIG = {"key": "fraction-bar-3-5", "lesson": "lles_t1", "title": "Three fifths", "method": "coded", "parts": [],
       "coded": {"type": "fraction", "shape": "bar", "numerator": 3, "denominator": 5},
       "source": {"source": "lsch_t2", "quote": "shading three parts out of five equal parts"}}

META = {"job": "test-job", "attempt": 1, "agent": "test", "model": "none", "gaps": {}}


def build(root, notes=NOTES, acts=ACTS, plan=PLAN, fig=FIG, meta=META):
    pack = os.path.join(root, JOB["pack"], "sources"); os.makedirs(pack)
    open(os.path.join(pack, "elib-test.md"), "w").write(PASSAGES)
    inbox = os.path.join(root, "jobs/inbox/test-job"); os.makedirs(inbox)
    json.dump(JOB, open(os.path.join(inbox, "job.json"), "w"))
    out = os.path.join(root, "jobs/outbox/test-job"); os.makedirs(os.path.join(out, "figures"))
    open(os.path.join(out, "lles_t1.notes.md"), "w").write(notes)
    json.dump(acts, open(os.path.join(out, "lles_t1.activities.json"), "w"))
    json.dump(plan, open(os.path.join(out, "lles_t1.plan.json"), "w"))
    json.dump(fig, open(os.path.join(out, "figures/fraction-bar-3-5.json"), "w"))
    json.dump(meta, open(os.path.join(out, "meta.json"), "w"))


def run(case, expect_pass, must_mention=None, **overrides):
    root = tempfile.mkdtemp()
    shutil.copytree(os.path.join(REPO, "tools"), os.path.join(root, "tools"))
    shutil.copytree(os.path.join(REPO, "schema"), os.path.join(root, "schema"))
    build(root, **overrides)
    r = subprocess.run([sys.executable, os.path.join(root, "tools/check.py"), "test-job"], capture_output=True, text=True)
    ok = (r.returncode == 0) == expect_pass and (must_mention is None or must_mention in r.stdout)
    print(f"{'ok ' if ok else 'BAD'} {case}")
    if not ok: print(r.stdout, r.stderr)
    shutil.rmtree(root)
    return ok


cases = [
    run("good answer passes", True),
    run("invented quote is rejected", False, "quote not found", notes=NOTES.replace('"1/5 + 2/5 = 3/5"', '"1/6 + 2/6 = 3/6"')),
    run("exercise line without source is rejected", False, "exercise line has no source",
        notes=NOTES.replace(' <!-- source: lsch_t2 "(d) 1/4 + 2/4. Answers" -->', "")),
    run("paragraph notes are rejected", False, "point form",
        notes=NOTES.replace("- A **fraction** is part of a whole.\n- The top number is the **numerator**.\n- The bottom number is the **denominator**.\n",
                            "A **fraction** is part of a whole. The top number is the **numerator** and the bottom number is the **denominator**, as every learner in the class should be able to explain clearly.\n")),
    run("padding is rejected", False, "padding", notes=NOTES.replace("- The top number is the **numerator**.", "- The top number is the **numerator**, according to the notes.")),
    run("classroom instruction in notes is rejected", False, "classroom instructions",
        notes=NOTES.replace("### Exercise", "Discuss in your groups.\n\n### Exercise")),
    run("maths without examples is rejected", False, "need '### Example'",
        notes=NOTES.replace("### Example 1", "### First sum").replace("### Example 2", "### Second sum")),
    run("missing diagram is rejected", False, "has no figures/", notes=NOTES.replace("fraction-bar-3-5", "missing-key")),
    run("plan minutes must add to 40", False, "add up to", plan={**PLAN, "steps": PLAN["steps"][:2]}),
    run("shallow plan is rejected", False, "teacher activity too thin", plan={**PLAN, "steps": [{**st, "teacherActivity": "Explains key terms."} for st in PLAN["steps"]]}),
    run("stale attempt is rejected", False, "attempt", meta={**META, "attempt": 2}),
    run("unbalanced latex is rejected", False, "unbalanced", notes=NOTES.replace("$\\frac{2}{9}", "\\frac{2}{9}")),
]
sys.exit(0 if all(cases) else 1)
