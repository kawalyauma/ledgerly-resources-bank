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

What the teacher writes on the board and learners copy, **content only**, in
**point form** like a good pupil's notebook. No paragraphs.

```markdown
# TOPIC: LOCATION OF UGANDA ON THE MAP OF EAST AFRICA
## SUB-TOPIC: Highland districts

### Highland districts
- These are districts which are located in areas of high altitude.
- Such districts usually have many hills and mountains.
- **Altitude** is the height above the sea level.
<!-- source: lsch_51a0 "districts which are located in areas of high altitude" -->

### Examples of highland districts
- Mbale
- Kapchorwa
- Kabale
- Kisoro
- Bundibugyo
- Kasese
<!-- source: lsch_51a0 "Examples of highland districts. Mbale, Kapchorwa, Kabale" -->

### Economic activities carried out in highland districts
- Tourism
- Mining
- Crop growing
<!-- source: lsch_51a0 "Tourism, Mining, Crop growing" -->

### Problems faced by people living in highland districts
- Landslides
- Severe soil erosion
- Poor transport network
- Difficulty in agricultural mechanisation
<!-- source: lsch_51a0 "Landslides, Severe soil erosion, Poor transport network" -->

### Possible solutions to the problems faced by people living in highland districts
- By rearing donkeys to use them as means of transport.
- By constructing winding roads.
- By terracing, contour ploughing and strip cropping to reduce soil erosion.
<!-- source: lsch_51a0 "By constructing winding roads" -->

### Note
- Heavy rainfall is the major cause of landslides in highland areas.
- Landslides can be controlled in highland areas by planting more trees.
<!-- source: lsch_51a0 "Heavy rainfall is the major cause of landslides" -->

### Exercise
1. What are highland districts? <!-- source: lsch_77ab "What are highland districts?" -->
2. Give any two examples of highland districts in Uganda. <!-- source: lsch_77ab "two examples of highland districts" -->
3. Why is it difficult to use tractors in highland areas? <!-- source: lsch_77ab "difficult to use tractors" -->
```

- `# TOPIC:` / `## SUB-TOPIC:` / `###` sections / `### Exercise` last.
- **Every content line is a `- ` point**: one fact, about 3–15 words (the checker rejects
  points over 30 words), in the sources' own wording. A meaning is a point too.
  Lists of names are one name per point, with no explanation.
- **Section headings use the usual notebook wording**: the thing itself (its meaning),
  Examples of…, Reasons why…, Importance of…, Advantages/Disadvantages of…, Causes of…,
  Effects of…, Economic activities…, Problems faced by…, Possible solutions to…, Ways of…,
  Duties/Roles of… Use the ones the sources support.
- **`### Note`** after the content: 2–5 key facts or exam tips from the sources
  (shown to learners as "Note:" with ticks). Leave it out when the sources give none.
- **No padding.** No paragraphs, no linking or summary sentences ("This shows…",
  "These help…", "In the supplied notes…", "according to the passages", "In this lesson…").
  The checker rejects them. Shorten; never stretch.
- Mathematics, English and Reading also have `### Example 1`, `### Example 2`… with
  the worked steps from the sources, one step per line. Other subjects have no examples.
- Each `###` section (except `### New words`) and each exercise line carries a
  `<!-- source: <passage id> "<exact quote>" -->` comment. Teachers never see these comments.
- The `### Exercise` questions are the same as the questions in `<lessonId>.activities.json`.
- No classroom instructions in notes ("discuss", "in groups", "sing", "tell the story"…).
  Those belong in the plan's steps.
- Maths in LaTeX: `$…$` inline, `$$…$$` display. Column sums and long division are
  coded figures, not LaTeX.
- Pictures go on their own line as `[[diagram:<key>]]`.
- Size by class: from about 6–14 points (P1) to 18–36 points (P7). The checker only
  rejects stubs (P1 under 50 words … P7 under 170).

## Quotes

A quote is copied **exactly** from the passage (≤ 25 words, and at least 6 letters/digits:
quote a short sum with its label, e.g. `"Add: (a) 2/7 + 3/7"`, not just `"2/7 + 3/7"`). The checker ignores
case, spacing and punctuation, but not words. A quote that can't be found means the
item is rejected as invented.

## Done means

`python3 tools/check.py <job>` prints PASS, the whole answer folder (notes, plan and
activities for every lesson, figures, and `meta.json`) is pushed, and a head teacher would
hand these notes to a new teacher without changing them.

Anything less is **NOT DONE**: never call it complete. Ledgerly does not import an answer
without `meta.json`, and it writes `jobs/feedback/<job>.md` listing what is missing from an
unfinished answer folder.
