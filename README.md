# Ledgerly Resources Bank

This repo is the content desk for the **Ledgerly learning engine**, the part
of Ledgerly that prepares schemes of work, lesson notes and lesson plans for
Ugandan schools.

Ledgerly doesn't write the content itself. It **collects the resources** (the
NCDC curriculum, and every EduShare resource including drafts: notes, schemes,
question papers, workbooks and teacher guides), **publishes them here as jobs**, and lets **any AI agent** do the
writing. When a job is done, Ledgerly pulls the answer back, checks it and
saves it.

> **The golden rule: agents assemble, they never invent.**
> Every fact, note, example, activity, exercise question and answer must come
> from the resources supplied with the job. An agent chooses, orders, cleans
> up and formats material. It doesn't make material up.

---

## Contents

1. [How it works](#1-how-it-works)
2. [The golden rule in detail](#2-the-golden-rule-in-detail)
3. [Repository layout](#3-repository-layout)
4. [Resource packs](#4-resource-packs)
5. [Jobs](#5-jobs)
6. [Answer formats](#6-answer-formats)
7. [Illustrations](#7-illustrations)
8. [Equations and maths](#8-equations-and-maths)
9. [Quality checks](#9-quality-checks)
10. [Instructions for agents](#10-instructions-for-agents)
11. [Who writes where](#11-who-writes-where)
12. [Review and publishing](#12-review-and-publishing)
13. [Privacy and content rules](#13-privacy-and-content-rules)
14. [Status](#14-status)

---

## 1. How it works

```
 Teacher / DOS clicks "Generate scheme"                       (Ledgerly)
        │
        ▼
 1. SOURCING (Ledgerly, no AI)
    finds the NCDC curriculum pages, notes, schemes, question papers and
    other e-library resources for the class, subject and term
        │
        ▼
 2. PUBLISH (Ledgerly → this repo)
    library/<pack>/   the resource pack: guide + every source's text
    jobs/inbox/<job>  a job: "write the term outline for this scheme"
        │
        ▼
 3. AN AGENT (any agent: Claude, Codex, …)
    pulls, reads the job and the pack, writes the answer,
    runs tools/check.py, pushes jobs/outbox/<job>/
        │
        ▼
 4. IMPORT (this repo → Ledgerly)
    Ledgerly pulls, runs the same checks plus its own quality gate
        ├── passed   → saved as "ready for review" in Ledgerly
        └── rejected → jobs/feedback/<job>.md says exactly why,
                        and the job returns to the inbox (max 3 attempts)
        │
        ▼
 5. Teacher clicks "Write notes" for a week → steps 2–4 repeat with a
    week job (notes + lesson plans + activities for every lesson that week)
```

Ledgerly syncs with this repo every few minutes. Agents work at their own pace.
Git is the only link between the two sides, so either side can be offline and
any agent can pick up where another stopped.

---

## 2. The golden rule in detail

Agents **must not invent** notes, examples, activities, exercise questions,
answers, facts, names, dates or figures. They use the **variety** of
resources in the pack instead:

| Needed in the answer | Where it must come from |
|---|---|
| Topics, subtopics, competences, order of teaching | NCDC curriculum / syllabus pages in the pack, with the reference schemes as a guide to order |
| Note content (definitions, explanations, facts, rules, worked examples) | Notes, textbooks and teacher guides in the pack |
| Examples (**Mathematics, English and Reading only**) | Worked examples that appear in the sources |
| Activities (= exercise questions; the two words mean the same thing) | Exercises in notes and workbooks, **and past question papers** (BOT, MID, EOT, mock, PLE) in the pack |
| Answers | The source's marking guide or answer key. For maths and other computed questions, the agent may work the answer out of a *sourced* question and must mark it `"answer_origin": "worked"`. |
| Classroom activities in plans (discussion, story, song, demonstration) | The teacher guides, schemes and methods named in the sources |
| Diagrams | Things the sources describe or show, labelled only with parts the sources name |

What an agent **may** do:

- Choose the best material from several sources, and combine them.
- Put material in teaching order and split it into 40-minute lessons.
- Tidy the wording to suit the class level (simpler sentences, Uganda spelling),
  **without changing facts, numbers or the substance of a question**.
- Format it: headings, tables, numbering, LaTeX maths.

What an agent **must not** do:

- Write a question, example or activity that doesn't appear in a source,
  even an "easy practice one".
- Change the numbers in a question to make a "new" one.
- Fill a gap from memory or general knowledge.

**When the pack isn't enough**, the agent writes the missing item in `gaps`
and leaves it out.

**Small classes (P1–P3) with thin material** get more periods per subtopic
through **Part B lessons** (lesson kind `practice`). A Part B lesson continues the
subtopic of the lesson before it, with *new* activities (and new examples in
Maths, English and Reading) drawn from other sources in the pack, and still never invented. Ledgerly reads the gaps and fetches more resources (a
re-sourcing job). A short lesson with an honest gap is always better than an
invented one.

### Citations (required)

Every note section, example, activity and exercise question carries a
`source` reference:

```json
{ "source": "lsch_9f2c1e…", "quote": "A noun is a naming word." }
```

- `source` is a **passage id**. Pack sources are split into numbered passages,
  marked `<!-- passage <id> part <n> -->` … `<!-- /passage -->`.
- `quote` is a short exact extract (≤ 25 words) from that passage.
- In notes, the citation is a comment: `<!-- source: <id> "<quote>" -->`.

The checker looks up every `quote` in the pack's source text. **If a quote
can't be found, the item is rejected as invented.**

### Variety

A good answer spreads its picks across the pack: notes from more than one
source, and exercise questions drawn from several past papers and workbooks,
not one book copied end to end. `meta.json` lists the sources used, and the
checker warns when one source supplies more than about 70% of a week.

---

## 3. Repository layout

```
README.md                  this file
AGENT.md                   short standing orders for agents (summary of §10)
schema/                    JSON Schemas for every file an agent writes
tools/
  next.py                  list open jobs / claim one
  check.py                 validate an answer exactly as Ledgerly will
library/                   resource packs (written by Ledgerly only)
  <school>/<year>-T<term>/<class>/<subject>/
jobs/
  inbox/                   open jobs (written by Ledgerly only)
  outbox/                  answers (written by agents only)
  feedback/                rejection reasons (written by Ledgerly only)
  done/                    accepted jobs, for history (written by Ledgerly only)
figures/
  library/                 shared picture library, reused by every school
.github/workflows/check.yml   runs tools/check.py on every push to jobs/outbox
```

`<school>` is a short code, never a learner's or staff member's name.

---

## 4. Resource packs

When a scheme is created, Ledgerly publishes everything that scheme will be
built from:

```
library/<school>/2026-T3/P6/mathematics/
  GUIDE.md        class, subject, term, number of weeks, periods per week,
                  lesson length (40 min), review and assessment rules,
                  class level notes, house style
  scheme.json     the accepted term outline (after the outline job is done)
  scheme.md       the same outline as a readable table
  sources/
    INDEX.md      every source: id, title, kind (curriculum / notes / scheme /
                  past paper / workbook / teacher guide), provider (NCDC /
                  e-library), year, pages used, why it was picked
    <source-id>.md  the source's text, split into passages:
                    <!-- passage lsch_… part 3 --> … <!-- /passage -->
                    (past papers include their marking guide when there is one)
  figures/        diagrams already made for this scheme
  lessons/        finished, approved lessons (read-only history), so later
                  weeks stay consistent with earlier ones and never repeat
```

Only the pages relevant to the scheme are included, not whole books.
When a scheme is re-sourced, the pack is updated in place, and git keeps the
old version.

---

## 5. Jobs

Each job is a folder in `jobs/inbox/`:

```
jobs/inbox/<job-id>/
  job.json      what to do, where the pack is, the passages quoted in the prompt, status and attempt
                (any passage in the pack may be cited, not only those: use the variety)
  prompt.md     the full instructions for this job (what to produce; the answer FORMAT is
                always the folder format below, whatever prompt.md says about JSON)
  passages.md   extra passages for this job that aren't in the pack (optional)
  example/      one approved lesson of the same class and subject, if one exists:
                the standard to match
```

`job.json`:

```json
{
  "job": "ltsk_8ce92c-w04",
  "kind": "lesson.write",
  "school": "sch-01",
  "class": "P6",
  "subject": "Mathematics",
  "term": "2026-T3",
  "week": 4,
  "classLevel": 6,
  "lessons": [
    { "id": "lles_3f…", "title": "Adding fractions", "subtopic": "Same denominator",
      "kind": "teach", "week": 4, "periods": 1 }
  ],
  "pack": "library/sch-01/2026-T3/P6/mathematics",
  "passages": ["lsch_9f2c1e…", "lsch_77ab01…"],
  "status": "open",
  "attempt": 1,
  "priority": 40,
  "created": "2026-10-12T15:00:00Z"
}
```

Job kinds:

| kind | What the agent produces |
|---|---|
| `scheme.outline` | The term outline: weeks → lessons, each with kind (teach / practice / review), subtopic, competences and sources |
| `lesson.write` | One week: notes, plan and activities for each lesson |
| `lesson.plan` | The plan only, for a lesson that already has notes (fallback) |
| `figure.generate` | One realistic illustration (only agents that can make images) |

---

## 6. Answer formats

Not TSX and not PDF. Ledgerly makes PDFs itself when something is printed.
Answers are plain text files that are easy for any agent to write, easy to read
on GitHub, and strict enough to check.

### `lesson.write` answer

```
jobs/outbox/<job-id>/
  meta.json                      job, attempt, agent, model, gaps, notes for the reviewer
  <lessonId>.notes.md            chalkboard notes
  <lessonId>.plan.json           lesson plan
  <lessonId>.activities.json     activities (exercise questions) with answers
  figures/<key>.json             a coded-figure spec or an illustration request
  figures/<key>.svg              a simple schematic drawn by the agent
  (one notes/plan/activities set per lesson id in job.json)
```

**Notes (`*.notes.md`)** are what learners copy from the chalkboard, nothing else:

```markdown
# FRACTIONS
## SUB-TOPIC: Adding fractions with the same denominator

### Rule
When the denominators are the same, add the numerators and keep the denominator.
<!-- source: lsch_9f2c1e "add the numerators and keep the denominator" -->

### Example
$\frac{1}{5} + \frac{2}{5} = \frac{3}{5}$
<!-- source: lsch_9f2c1e "1/5 + 2/5 = 3/5" -->

[[diagram:fraction-bars-3-5]]

### Exercise
1. $\frac{2}{7} + \frac{3}{7}$   <!-- source: lsch_77ab01 "Add: (a) 2/7 + 3/7" -->
2. …
```

- Structure: `# TOPIC` / `## SUB-TOPIC` / `### sections` / `### Exercise`.
- Every section, example and question has a `<!-- source: … -->` comment. Teachers
  never see these comments, but the checker reads them.
- Classroom activities (story telling, discussion, songs, Bible reading) belong
  in the **plan**, never in the notes.
- Tables are Markdown tables. A table is never turned into a picture.

**Plan (`*.plan.json`)** has fixed fields (see `schema/plan.schema.json`):
competences, methods (names only), teaching aids, references (the source ids),
a step-by-step teaching guide (introduction / development / conclusion with
minutes), and assessment. Each step that describes a classroom activity cites
its source.

**Activities (`*.activities.json`)**: the question, answer, `answer_origin`
(`"source"` or `"worked"`), options for multiple choice, kind, skill,
cognitive level, difficulty 1–5, and `source` + `page` + `quote`.

### `scheme.outline` answer

`scheme.json` (strict, see `schema/scheme.schema.json`) plus `scheme.md` (readable).

---

## 7. Illustrations

The notes never wait for a picture. There are three kinds:

1. **Coded figures.** The agent writes a small spec and Ledgerly draws it with
   code, so it's exact, free and identical whichever agent wrote it.
   Supported: shapes, fractions, number lines, clocks, the Uganda map, bar charts.
   Also: column addition/subtraction/multiplication, long division, angles,
   Venn diagrams (full list: `tools/coded-figures.md`).
   ```json
   { "key": "fraction-bars-3-5", "method": "coded",
     "coded": { "type": "fraction", "shape": "bar", "numerator": 3, "denominator": 5 },
     "source": { "source": "lsch_77ab01", "quote": "shading three parts out of five" } }
   ```
2. **SVG schematics.** The agent draws simple labelled outlines (water cycle,
   parts of a plant) as `figures/<key>.svg`. They must be black and white,
   printable, and labelled only with parts the source names.
3. **Realistic illustrations** (a hen, a hoe, a hut). The agent writes an
   illustration request (concept, parts to label, source). Ledgerly first looks
   in the shared picture library and reuses a match. If there isn't one, it
   opens a `figure.generate` job for an agent that can make images. All
   illustrations use one style: black-and-white line art on white, suitable
   for printing. Until a picture arrives, the lesson shows a captioned placeholder.

In notes, a picture goes on its own line as `[[diagram:<key>]]`.

---

## 8. Equations and maths

- Write maths in LaTeX: inline `$\frac{3}{4}$`, display `$$ … $$`. This applies in
  every class, P1 to P7.
- Ledgerly renders it with KaTeX in the app, in PDFs and in print.
- Primary vertical working (column addition and subtraction, long division) is
  laid out with **coded figures**, not LaTeX, so it always looks the way
  teachers write it on the board.
- Units and money: `shs 5,000`, `5 kg`, `3 m`. Uganda conventions.

---

## 9. Quality checks

`tools/check.py <job-id>` runs locally, on GitHub CI, and on the Ledgerly
server, with the same rules everywhere:

- **Sourcing:** every item has a `source`, the source id exists in the pack, and
  the `quote` is found in that source's text. A missing quote means the item is rejected as invented.
- **Shape:** every file matches its schema, and every lesson in the job is answered.
- **Notes:** correct heading structure, no classroom activities, no tables
  turned into pictures, every `[[diagram:key]]` has a matching figure.
- **Size:** each lesson is teachable in one 40-minute period.
- **Plan:** every required field is filled, and the minutes add up to the period.
- **Variety:** warns if one source supplies more than about 70% of a week.
- **Maths:** the LaTeX compiles.

After the checker, Ledgerly runs its own quality gate (the chalkboard-notes
rules and lesson quality checks). Anything rejected comes back in
`jobs/feedback/<job-id>.md` with the exact reasons.

---

## 10. Instructions for agents

The loop:

1. `git pull --rebase`
2. `python3 tools/next.py` lists open jobs, most urgent first.
   `python3 tools/next.py claim <job-id>` claims one (it commits and pushes a claim so two agents never take the same job).
3. Read, in order:
   - `jobs/inbox/<job-id>/job.json`
   - `jobs/feedback/<job-id>.md`, if present: fix exactly what it says
   - `<pack>/GUIDE.md`, `<pack>/scheme.md`, `<pack>/sources/INDEX.md`
   - `<pack>/lessons/`: what has already been taught
   - `jobs/inbox/<job-id>/example/`: the standard to match
   - `jobs/inbox/<job-id>/prompt.md`: the exact task
4. Write the answer in `jobs/outbox/<job-id>/`.
5. `python3 tools/check.py <job-id>`, then fix until it passes.
6. `git add jobs/outbox/<job-id> && git commit -m "answer <job-id>: P6 Mathematics w04" && git push`
7. Back to 1.

Remember:

- **Never invent.** If it isn't in the pack, it goes in `gaps`.
- One lesson = one 40-minute period.
- Notes are chalkboard notes, and activities go in the plan.
- Write for the class's level, with Uganda context and spelling.
- Ask yourself: would a head teacher hand these notes to a new teacher
  without changes? If not, the job isn't done.

---

## 11. Who writes where

| Path | Written by |
|---|---|
| `library/`, `jobs/inbox/`, `jobs/feedback/`, `jobs/done/`, `figures/library/` | Ledgerly only |
| `jobs/outbox/`, `jobs/claims/` | Agents only (Ledgerly moves an answer to `jobs/done/` once it is accepted) |
| `README.md`, `AGENT.md`, `schema/`, `tools/`, `.github/` | Maintainers |

Because the two sides never write the same files, syncs never conflict.

---

## 12. Review and publishing

Accepted answers land in Ledgerly as **"ready for review"**. A DOS or head
teacher reads them and approves or sends them back with comments. Approved
lessons are copied into the pack's `lessons/` folder, so later jobs build on
them. Once the agents have proved reliable, approval can switch to automatic.

---

## 13. Privacy and content rules

- **No learner or staff data ever goes in this repo.** Jobs are curriculum work
  only. Student summaries and scanned exercise books stay inside Ledgerly.
- Schools are referred to by a short code.
- Source text is limited to the excerpts a scheme actually uses.
- No passwords, keys or server details in any file.

---

## 14. Status

| Step | | |
|---|---|---|
| 1 | README, AGENT.md, schemas, check.py (+ self-test), next.py, CI | done |
| 2 | Ledgerly "git" provider + exporter (jobs and packs pushed here) | done (deployed 2026-10-13; waiting for the deploy key) |
| 3 | Importer, feedback, attempts, archive to `jobs/done` | done |
| 4 | New coded figures (column sums, long division, angles, Venn) + maths in print/Word/app | done |
| 5 | App panel (Ledgerly Academics 2.5.0): Resources bank writer, jobs waiting / answered, Sync now | done |
