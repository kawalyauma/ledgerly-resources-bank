# Standing orders for writing agents

You prepare schemes of work, lesson notes and lesson plans for Ugandan schools.
`README.md` explains the whole system. This page is what you do every time.

## The golden rule

**Assemble, never invent.** Every note, example, activity, answer, fact and
classroom activity comes from the passages in the job's pack. You choose, order,
tidy and format material, but you don't make it up. If the pack doesn't cover
something, write it in `meta.json` → `gaps` and leave it out.

- Use the **variety** of the pack: notes from different sources, past papers,
  workbooks, drafts and teacher guides. Don't copy one book end to end.
- **Activity = exercise.** They are the same thing: the questions learners answer.
- **Examples** (worked examples) are only for **Mathematics, English and Reading**.
  Other subjects have no Example sections.
- Every lesson is **one 40-minute period**.
- Lessons of kind `practice` are **Part B lessons**: they continue the same subtopic
  as the lesson before, with *new* activities (and new examples in Maths/English/
  Reading) taken from other sources in the pack. Use them for small classes where
  one subtopic needs more than one period.

## The loop

```bash
git pull --rebase
python3 tools/next.py                 # open jobs, most urgent first
python3 tools/next.py claim <job>     # claim one (commits + pushes a claim)
# read: jobs/inbox/<job>/job.json, prompt.md, example/ (if any),
#       jobs/feedback/<job>.md (if any), and the pack named in job.json
# write: jobs/outbox/<job>/...
python3 tools/check.py <job>          # must print PASS
git add jobs/outbox/<job> && git commit -m "answer <job>" && git push
```

If `git push` is rejected, `git pull --rebase` and push again. You only ever write in
`jobs/outbox/<job>/` and `jobs/claims/`, so rebases never conflict.

## What to write

### `scheme.outline` → `jobs/outbox/<job>/scheme.json` + `meta.json`
Schema: `schema/scheme.schema.json`. Weeks → units → lessons. Each lesson is
`teach` or `practice` (Part B), with objectives and `sources`.

### `lesson.write` → for every lesson id in `job.json`:

| File | Contents |
|---|---|
| `<lessonId>.notes.md` | Chalkboard notes (below) |
| `<lessonId>.plan.json` | Lesson plan (`schema/plan.schema.json`) |
| `<lessonId>.activities.json` | Activities / exercise questions with answers (`schema/activities.schema.json`) |
| `figures/<key>.json` (+ `<key>.svg`) | Pictures (`schema/figure.schema.json`, `tools/coded-figures.md`) |

and one `meta.json` (`schema/meta.schema.json`).

### `lesson.plan` → `<lessonId>.plan.json` + `meta.json`

## Chalkboard notes

What the teacher writes on the board and learners copy, **content only**:

```markdown
# TOPIC: FRACTIONS
## SUB-TOPIC: Adding fractions with the same denominator

### Rule
When the denominators are the same, add the numerators and keep the denominator.
<!-- source: lsch_9f2c1e "add the numerators and keep the denominator" -->

### Example 1
$\frac{1}{5} + \frac{2}{5} = \frac{3}{5}$
<!-- source: lsch_9f2c1e "1/5 + 2/5 = 3/5" -->

[[diagram:fraction-bar-3-5]]

### Exercise
1. $\frac{2}{7} + \frac{3}{7}$ <!-- source: lsch_77ab01 "2/7 + 3/7" -->
2. $\frac{1}{9} + \frac{4}{9}$ <!-- source: lsch_77ab01 "1/9 + 4/9" -->
```

- `# TOPIC:` / `## SUB-TOPIC:` / `###` sections / `### Exercise` last.
- Each `###` section (except `### New words`) and each exercise line carries a
  `<!-- source: <passage id> "<exact quote>" -->` comment. Teachers never see these comments.
- The `### Exercise` questions are the same as the questions in `<lessonId>.activities.json`.
- No classroom instructions in notes ("discuss", "in groups", "sing", "tell the story"…).
  Those belong in the plan's steps.
- Maths in LaTeX: `$…$` inline, `$$…$$` display. Column sums and long division are
  coded figures, not LaTeX.
- Pictures go on their own line as `[[diagram:<key>]]`.
- Size by class: P1 ≈ 100–220 words … P7 ≈ 400–650 words (the checker enforces minimums).

## Quotes

A quote is copied **exactly** from the passage (≤ 25 words). The checker ignores
case, spacing and punctuation, but not words. A quote that can't be found means the
item is rejected as invented.

## Done means

`python3 tools/check.py <job>` prints PASS, and a head teacher would hand
these notes to a new teacher without changing them.
