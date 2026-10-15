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

## Lesson plans

A plan a head teacher or supervisor would accept (Ugandan format), written from the lesson's notes.
Never one generic line per step ("Explain key terms", "Give questions"): name the terms and quote the questions.

- `competences`: 2–4, each "The learner …" with a concrete verb and the lesson's actual content.
- `languageCompetence`: the key words learners pronounce, spell, read and write.
- `objectives`: 2–4 measurable ("By the end of the lesson, learners should be able to …"), not copies of the competences.
- `priorKnowledge`: what learners already know that the lesson builds on.
- `methods` ≥ 3 names; `materials` ≥ 2 specific aids ("chart of the three arms of government", not only "chalkboard");
  `references`: source titles (with page numbers when the sources give them).
- `steps`: 4–7, minutes adding up exactly to the lesson: Introduction (link to prior knowledge, the starter question),
  one development step per notes section, a Practice / Exercise step, a Conclusion. Every step has
  `content` (the points taught or written on the board in that step, from the notes; required except in the
  introduction and conclusion), `teacherActivity` (2–4 sentences, ≥ 20 words, with the actual questions and
  examples) and `learnerActivity` (1–3 sentences, ≥ 10 words).
- `assessment`: at least 3 actual oral or written questions; `homework`: one specific task; `lifeSkills`: 2–4.

```json
{
  "competences": ["The learner names the three arms of government.", "The learner states the duties of the legislature."],
  "languageCompetence": "Pronounces, spells and writes: legislature, executive, judiciary, Speaker, bill.",
  "objectives": ["By the end of the lesson, learners should be able to name the three arms of government.",
                 "By the end of the lesson, learners should be able to state three duties of the legislature."],
  "priorKnowledge": "Learners know from the previous lesson that Uganda has a government that leads the country.",
  "methods": ["Explanation", "Question and answer", "Guided discussion"],
  "materials": ["Chart of the three arms of government", "Picture of Parliament in session"],
  "references": ["P.5 SST SCHEME TERM III 2019", "Primary Five Social Studies Notes 2020"],
  "steps": [
    {"stage": "Introduction", "minutes": 5,
     "teacherActivity": "The teacher asks: 'Who makes the rules in our school?' and 'Who makes the laws of Uganda?', then links the answers to the arms of government.",
     "learnerActivity": "Learners name people who make rules at school and at home, and guess who makes the laws of Uganda."},
    {"stage": "Development: the arms of government", "minutes": 10,
     "content": "The three arms of government: the legislature (makes laws), the executive (implements laws), the judiciary (interprets laws).",
     "teacherActivity": "The teacher shows the chart, writes the three arms on the board and explains each with an example: Parliament passes a law, ministers carry it out, courts settle cases under it.",
     "learnerActivity": "Learners read the three arms aloud from the chart and copy them with their work into their books."},
    {"stage": "Development: duties of the legislature", "minutes": 10,
     "content": "Duties of the legislature: to make laws, to approve the national budget, to approve ministers, to protect the constitution.",
     "teacherActivity": "The teacher asks: 'Which arm of government makes laws?' and writes the duties of the legislature on the board, explaining what a bill is and how it becomes a law.",
     "learnerActivity": "Learners discuss in pairs one duty of Parliament they have heard about on radio, then share with the class."},
    {"stage": "Practice", "minutes": 10,
     "content": "Exercise: name the three arms of government; state two duties of the legislature; who heads Parliament?",
     "teacherActivity": "The teacher writes the exercise questions on the board, moves around marking, and helps learners who mix up the executive and the legislature.",
     "learnerActivity": "Learners answer the exercise questions in their books and correct their mistakes as the teacher marks."},
    {"stage": "Conclusion", "minutes": 5,
     "teacherActivity": "The teacher summarises the arms of government and asks three learners: 'Which arm interprets the law?', 'Which arm makes laws?', 'Who heads Parliament?'",
     "learnerActivity": "Learners answer the oral questions and read the summary on the board together."}
  ],
  "assessment": "Oral questions in the conclusion (Which arm interprets the law? Which arm makes laws? Who heads Parliament?) and the written exercise, marked in class.",
  "homework": "Write two duties of the legislature and two of the judiciary in your book.",
  "lifeSkills": ["Critical thinking", "Effective communication", "Respect for authority"]
}
```

`tools/check.py` rejects plans that miss any of these (thin activities, missing content, too few steps,
competences, objectives or aids, no prior knowledge, vague assessment, notes sections not taught).

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
