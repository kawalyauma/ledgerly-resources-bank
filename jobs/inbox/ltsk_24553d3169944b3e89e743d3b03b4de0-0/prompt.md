# Job ltsk_24553d3169944b3e89e743d3b03b4de0-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 6 lesson(s) below of week 8 of the Science scheme for Primary Four 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P4: one 40-minute lesson: 2–4 sections; about 12–24 points; meanings, examples and uses; 5–7 activities.

lessonId=lles_ac9e0d13e31b46469b9f239e350f3acd: lesson 43, Monday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: Poisoning — Poisoning.
  Objectives: Identify, explain or describe poisoning using the cited school science scheme.

lessonId=lles_8ce777f1ea844d369dca7586cdfec070: lesson 44, Tuesday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: Preventing poisoning — Preventing poisoning.
  Objectives: Identify, explain or describe preventing poisoning using the cited school science scheme.

lessonId=lles_7cc6958d75874c0b8fc9ea05a8f99276: lesson 45, Wednesday, 1 period(s), 40 minutes.
  Unit: Rabbit Keeping (theme: The World of Living Things). Lesson: Meaning of rabbit keeping — Meaning of rabbit keeping.
  Objectives: Identify, explain or describe meaning of rabbit keeping using the cited school science scheme.

lessonId=lles_7aff4347189a4b6b8c256ced9028c707: lesson 46, Thursday, 1 period(s), 40 minutes.
  Unit: Rabbit Keeping (theme: The World of Living Things). Lesson: External parts of a rabbit — External parts of a rabbit.
  Objectives: Identify, explain or describe external parts of a rabbit using the cited school science scheme.

lessonId=lles_b36f2195c83c481aa3402bc56a39279f: lesson 47, Friday, 1 period(s), 40 minutes.
  Unit: Rabbit Keeping (theme: The World of Living Things). Lesson: Rabbit products — Rabbit products.
  Objectives: Identify, explain or describe rabbit products using the cited school science scheme.

lessonId=lles_cf5fccfd7da041a4a1ef49e8204e082c: lesson 48, Friday, 1 period(s), 40 minutes.
  Unit: Rabbit Keeping (theme: The World of Living Things). Lesson: Local breeds of rabbits — Local breeds of rabbits.
  Objectives: Identify, explain or describe local breeds of rabbits using the cited school science scheme.

Write, using ONLY the passages below. Passages from "NCDC" documents are the official base for what to teach; NCDC lower-primary thematic curricula put every learning area in columns separated by " | ": use only the Science column.
For EACH lesson:
- notes: the CHALKBOARD NOTES the teacher writes on the board for learners to copy into their exercise books, in Markdown, at exactly this class level.
  Use the detailed notes in the passages as the factual base, not merely the short scheme wording.
  Learner-facing CONTENT ONLY. Never write instructions or activities in the notes: no 'discuss', 'in your groups', 'tell the story', 'sing', 'act out', 'read with your teacher', 'say aloud', 'think of'. Those go in methods.
  Write the content itself: state the facts, meanings, examples and lists. For a Bible or Quran passage, give the reference AND what it says or teaches in one short point (not 'read John 8:12').
  HOUSE STYLE: POINT FORM, like a good Ugandan pupil's notebook. NO PARAGRAPHS. Every content line is a short point starting with '- ': one fact per point, about 3 to 15 words, in the passages' own wording.
    A meaning is a point too ('- Altitude is the height above the sea level.'). Lists of names are one name per point with no explanation ('- Mbale', '- Kapchorwa').
    Never pad or link points: no 'This shows…', 'These help…', 'In the supplied notes…', 'according to the passages', 'In this lesson…', no summary sentence at the end of a section. Shorten; never stretch.
  Structure:
    # TOPIC: <unit title in capitals>
    ## SUB-TOPIC: <lesson title>
    then sections, each under a ### heading in the usual notebook wording: ### <Thing> (its meaning), ### Examples of …, ### Reasons why …, ### Importance of …, ### Advantages of …, ### Disadvantages of …,
    ### Causes of …, ### Effects of …, ### Economic activities carried out in …, ### Problems faced by …, ### Possible solutions to the problems …, ### Ways of …, ### Duties/Roles of … (use whichever the passages support).
    ### Note at the end of the content: 2 to 5 key facts or exam tips from the passages that a learner must remember (e.g. '- Heavy rainfall is the major cause of landslides in highland areas.'). Leave it out when the passages give none.
    Bold only the key word being defined. Use a small Markdown table only for comparisons (e.g. organ of government | its work).
    Examples ('### Example 1', '### Example 2', ...) are ONLY for Mathematics, English and Reading: worked examples taken from the passages, set out step by step (each step on its own line). Other subjects have no Example sections.
    Write mathematics in LaTeX: $\frac{3}{4}$ inline, $$...$$ on its own line. Column sums and long division are coded diagrams, not LaTeX.
    When the curriculum names new words, list them once near the top as '### New words' followed by the words separated by commas (no tables, no pronunciation drills).
    End with '### Exercise': 3–8 numbered questions on this lesson, taken from the activities, for learners to answer in their books.
  Keep it board-sized: as much as a teacher writes in one lesson; no greetings, no 'In this lesson we will', no notes to the teacher.
  Where a matching past-paper question exists, use it as a worked example, an Activity, or a clearly marked 'NB / Exam practice' item; do not let an exam paper determine the curriculum order.
- methods: ONLY the names of the teaching methods, comma separated, for the scheme of work's Methods column (e.g. 'Story telling, Discussion, Guided Bible reading, Question and answer'). At most 6 names, no sentences.
- teachingGuide: the CLASS ACTIVITIES, step by step: what the teacher does and what learners do (discussion, group work, story telling, songs, dramatisation, guided Bible/Quran reading, oral work, drawing, games), as given or implied in the passages. Everything taken out of the notes because it is an instruction goes here.
- materials, lifeSkills, assessment: as given or implied in the passages; null when the passages are silent.
- lessonPlan: a COMPLETE lesson plan in the Ugandan format that a head teacher or supervisor would accept, written from this lesson's notes:
  competences: 2-4 subject competences, each 'The learner ...' with a concrete verb (defines, names, explains, draws, calculates, locates) and this lesson's actual content.
  languageCompetence: the key words of the lesson learners pronounce, spell, read and write (name them).
  objectives: 2-4 measurable objectives ('By the end of the lesson, learners should be able to ...'), not copies of the competences.
  priorKnowledge: what learners already know that this lesson builds on (the previous lesson or everyday experience), in one or two sentences.
  methods: at least 3 method names. materials: at least 2 specific teaching aids (e.g. 'chart of the three arms of government', not only 'chalkboard'). references: the source titles, with page numbers when the passages give them.
  steps: 4-7 steps whose minutes add up exactly to the lesson's minutes: Introduction (how the teacher links to prior knowledge, with the starter question asked); one Lesson development step for each notes section (or two small sections together); a Practice / Exercise step; and a Conclusion (summary and evaluation).
  Every step has: stage; minutes; content = the exact points taught or written on the board in that step, taken from the notes; teacherActivity = what the teacher does and says in 2-4 sentences, quoting the actual questions asked and the examples used; learnerActivity = what learners do in 1-3 sentences (answer, copy, discuss in pairs, draw, read aloud, demonstrate, act).
  Never write generic steps such as 'Explain key terms', 'Give questions' or 'Review the lesson': name the terms, quote the questions, say what is reviewed.
  assessment: how learning is checked, listing at least 3 actual oral or written questions (from the notes' Exercise). homework: one specific task. lifeSkills: 2-4 life skills and values shown in the lesson.
  The content of the plan comes from this lesson's notes; plan when the teacher writes each part on the board, and put the class activities from teachingGuide into the steps.
- activities (activities and exercise questions are the same thing): questions for learners copied from the passages, drawn from the variety of notes, workbooks and past papers supplied. Set origin='source'.
  For each one set sourcePassageId and sourceQuote = the question's exact words copied from that passage, so it can be verified.
  Give answer only when the passage gives it or it is plain arithmetic; otherwise null. concept = the subtopic it tests, skill = what the learner does (e.g. 'identify', 'compute', 'explain').
  kind is one of: computation, short_answer, multiple_choice, fill_blank, true_false, matching, structured, essay, drawing. cognitiveLevel is one of: remember, understand, apply, analyse, evaluate, create.
- Never write a question, example or activity that is not in the passages, and never change a sourced question's numbers to make a new one. If the passages have too few, use what there is and list the shortfall in gaps.
- diagrams: up to 3 teaching pictures per lesson of things the passages describe that learners must SEE. Skip them when nothing in the lesson is visual.
  NEVER make a table, list or text box into a diagram; tables belong in the notes as Markdown tables. Choose a method per picture:
  * method "illustration" for real things: animals, plants, body parts and organs, tools, apparatus, objects, scenes (e.g. the external parts of a domestic fowl, a beehive, a flower).
    Give concept = a precise description of what to draw (e.g. 'side view of a domestic hen, full body') and parts = the exact part names from the passages to label. No svg. Ledgerly draws it once and reuses it.
    For a picture comparing two things, name each part with its owner so both get labelled, e.g. 'comb (cock)', 'comb (hen)'.
  * method "coded" for exact maths pictures, with coded = one of:
    {"type":"shape","shape":"circle|square|rectangle|triangle|right-triangle|equilateral-triangle|isosceles-triangle|parallelogram|rhombus|trapezium|kite|pentagon|hexagon|octagon"}
    {"type":"fraction","shape":"circle|bar","numerator":3,"denominator":4}   {"type":"number-line","from":0,"to":10,"step":1,"marks":[3,7]}
    {"type":"map","region":"uganda","layers":["lakes","rivers","mountains","towns","neighbours","regions","equator"],"highlight":["Northern"]} for any map of Uganda (pick the layers needed; parts = the lakes, rivers, mountains, towns, neighbours or regions to label, e.g. 'Lake Kyoga', 'River Victoria Nile', 'Mount Elgon', 'Kenya', 'Northern Region'),
    {"type":"clock","hour":3,"minute":30}   {"type":"bar-chart","title":"...","yLabel":"...","bars":[{"label":"Mon","value":4}]} (only with data given in the passages)
    {"type":"column-sum","operation":"add|subtract|multiply","numbers":[345,278],"showAnswer":true} for vertical working   {"type":"long-division","dividend":756,"divisor":6,"showWorking":true}
    {"type":"angle","degrees":60,"label":"x"}   {"type":"venn","sets":[{"label":"Even","items":["4"]},{"label":"Prime","items":["3"]}],"both":["2"]} (numbers always from the sourced question)
  All pictures are printed in BLACK: black outlines on white, mostly outline, simple grey or hatched shading only where needed, never colour.
  * method "svg" for simple schematics only (cycles, food chains, flow of a process): a self-contained SVG, viewBox="0 0 640 420", white background, black outlined shapes (fills white or light grey #e6e6e6 only),
    labels font-size 16-18 joined by leader lines, arrows via <marker>, a title at the top, nothing outside the viewBox. No scripts, images, links, CSS or external fonts.
  Label only parts the passages name. key is a short slug, unique within the lesson; put [[diagram:key]] on its own line in that lesson's notes where it belongs; sourcePassageId is the passage it depicts.
- sourcePassageIds: every passage id that lesson used.

Reply shape:
{"lessons":[{"lessonId":string,"notes":string,"methods":string|null,"teachingGuide":string|null,"materials":string|null,"lifeSkills":string|null,"assessment":string|null,"sourcePassageIds":[string],"lessonPlan":{"competences":[string],"languageCompetence":string|null,"objectives":[string],"priorKnowledge":string|null,"methods":[string],"materials":[string],"references":[string],"steps":[{"stage":string,"minutes":int,"content":string,"teacherActivity":string,"learnerActivity":string}],"assessment":string|null,"homework":string|null,"lifeSkills":[string]},"diagrams":[{"key":string,"title":string,"caption":string|null,"method":"illustration"|"coded"|"svg","concept":string|null,"parts":[string],"coded":object|null,"svg":string|null,"sourcePassageId":string|null}],"activities":[{"question":string,"answer":string|null,"options":[string]|null,"kind":string,"concept":string,"skill":string,"cognitiveLevel":string,"difficulty":1-5,"origin":"source"|"generated","sourcePassageId":string|null,"sourceQuote":string|null}],"gaps":[string]}]}

<passages>
<passage id="lchk_3e640d10b65a43af89a019881ffafee4" source="Primary 4 Science Scheme of Work, Term 3" part="6">
Causes of dislocations
First aid for a dislocation
First aid for a snake bit
 Discussion
(Guided)
 Discovery
 Demonstrat
ing the first
aid for
dislocation
 Problem
solving
 Bandage
 Compo.
Primary
Science
12
Describes the first aid
for snake bites
2
Human health
Accidents and first aid
Poisoning
The learner;
Defines poison and
poisoning
Mentions the causes of
poisoning
Describes the
appropriate first aid for
poisoning
States the ways of
preventing poisoning
The learner;
Spells, reads and
pronounces words
-poison
-chemical
-substance
-harm
-vomiting
-throad
Poisoning
Definition of poison and poisoning
Examples of poisons
Causes of poisoning
First aid for poisoning
Prevention of poisoning at home, school and
community
 Guided discussion
 Question and answer
technique
 Mentioning the examples of
poisons
 Problem solving
 Chalk board illustration
 MK primary science book 4
page 169
3
The world of living things
Rabbit keeping
Rabbits
The leaner;
Defines the terms used
in rabbit keeping
Mentions the reasons
for rearing rabbits
Draws a rabbit and
labels the parts
(tracing)
The learner;
Reads, spells and
pronounces words
and sentences e.g.
-burrow
-doe
-hutch
-litter
-kitten
-fur
-kindling
-kit
Rabbit keeping
Definition
Terms used in rabbit keeping
Reasons for rearing rabbits
Parts of a rabbit (ear, head, eye, neck, nose,
whiskers, thigh, tail, hind leg)
Rabbit products
 Question and answer
 Self discovery
 Drawing a rabbit and naming the parts
 Care
 Appreciation
 Real rabbits
 MK primary science book 4 page 176
4
The world of
living things
Rabbit keeping
Breeds of rabbits The learner;
Mentions the types of
rabbit breeds
Identifies the
characteristics of each
types of breeds
The learners;
Reads and writes
words and
sentences about
types of rabbits
-local
-exotic
Breeds of rabbits
Local rabbits
Exotic rabbits
Local rabbits
Meaning and habitat
 Guided
discussio
n
 Excursio
n
 Identifyi
ng the
rabbit
breeds
 Care
 Creative
thinking
 Chalkboa
rd
illustrati
 MK
Primary
Science
13
Writes the differences
between exotic and
local rabbits
-indigenous
-breeds
-features
Characteristics
Exotic rabbits
Meaning
Characteristics
Differences between exotic and local rabbits
5
The world of living things
Rabbit keeping
Breeds of rabbits
The learner;
Names the exotic
breeds of rabbits
Describes how each
breed looks
Draws the house for
rabbits
The learner;
Writes sentences
about rabbit breeds
Examples of Exotic rabbit breeds
Chinchilla rabbits
Angora rabbits
Newzealand white
California rabbits
Appearance of each breed
Housing for rabbits
Structure of a hutch
Qualities of a good hutch
How to make a hutch
 Excursion
 Discovery
 Making a hutch for rabbits
 Care
 Effective communication
 Made hutch using boxes
 MK Primary science book 4 page 180
14
7 1
The world of living things
Rabbit keeping
Rabbit management practices
The learner;
Names the food for
rabbits
Mentions the breeding
process for rabbits
The learner;
Reads and writes
words and
sentences correctly
-pellets
-main facture
Feeding of rabbits
Green vegetables
Carrots
Sweet potato leaves
Banana peelings
Pellets (Manufactured foods)
 Questions and answer
 Discussion
 Mentioning the signs of heat in rabbits
 Appreciation
 Care
 Real food stuffs
 Chalkboard illustration
 MK Primary Science book 4 page 184
Breeding in rabbits
Name given to male and female rabbits.
Signs of heat in rabbits
Gestation period of rabbits.
Act of giving birth by a doe (kindling)
</passage>

<passage id="lchk_98670b27a5454f21a36a23dd71e9ad3e" source="Primary 4 Science Scheme of Work – Term III" part="1">
For more schemes of work, visit www.uganda.madpath.com
SCHEME OF WORK FOR P.4 SCIENCE TERM III
WK PD THEME SUB-
THEME
CONTENT COMPETENCES METHODS ACTIVITY LIFE SKILLS
AND
VALUES
INSTRUCTIONAL
MATERIALS
REF
COMMUN
ICABLE
DISEASE
S AND
WORM
INFESTA
TION
Diarrheal
diseases
or faecal
diseases
• Definition of Diarrhoea.
• Examples of diarrhoeal
diseases.
• Causes
• The 4Fs
• Prevention.
• Dehydration (Definition)
• Its causes
• Signs
• (Use of ORS)
• Solutes
• Solvent
• Solution
• Rehydration (Definition)
• Identifies diarrheal
diseases.
• Describes the spread of the
above diseases.
• Demonstrates the
preparation of ORS and
SSS.
• Draw the structure of a tape
worm.
• Tell how tape worms enter
our bodies.
-Demonstration
-Discussion
-Guided
discovery
-Question and
answer
-Note making
-Preparing ORS and
SSS
-Cleaning the toilet
or latrines
-Boiling water
- Making SSS
-Critical
thinking
-Problem
solving
-Decision
making
-Self
awareness
• Water
• Sugar
• Salt
• Spoons
• Chart showing
the 4Fs
Mk
integrated
Pri Sci Bk
4 Pg 124
Functional
intergrated
Pri Sci for
Ug Pg 180
For more schemes of work, visit www.uganda.madpath.com
• Preparation of ORS and
SSS.
2 1 HUMAN
HEALTH
VECTORS
AND
DISEASES
Common Vectors
• Definition of vectors
• Examples of common
vectors
• Cockroaches
• Ticks
• Bedbugs
• House flies
• Mites
• Rats
• Lice
• Mosquitoes
• Tsetse flies
* Life cycle of vectors
* Diseases spread by each
vector
• Body structure
• Their habitat
• Their feeding habits
• Their life cycles
• How they protect them
selves from enemies
How vectors spread diseases.
• Bites
• Dirty body
• Dirty environment
Prevention and control
• Proper hygiene
• Covering food.
• Spraying
• Biological control.
• Sleeping under a treated
mosquito net.
The learners:-
• Defines vectors
• Identifies some common
disease vectors
• Describes characteristics of
some disease vectors.
-Guided
discovery
-Question and
answer
Discussion.
Observation
Field
Study
- Naming
- Drawing
- Answering
questions
Match
- Awareness
- Care
Responsibility
-Self
awareness
-Decision
making
Taking
Decision
Sharing
Appreciation
Effective
communicatio
n
• A chart with
some vectors.
• Real vectors
like
cockroaches
For more schemes of work, visit www.uganda.madpath.com
HUMAN
HEALTH
Accidents
poisoning
and first
Aid
Accidents
• Definition
• Types of accidents
• Causes of accidents
• Prevention of accidents
First Aid
• Definition
• Reasons for giving first aid.
• Responsibilities of a first
aider.
• Qualities of a first aider.
• First aid kit (box)
• How to use a first aid kit.
• Components of the first and
kit and uses.
• Places where we find first aid
box
The learner:-
- Names common accidents
and poisoning at home, on
the way to, from and at
school.
- States causes of accidents
and poisoning.
- Demonstrates how to take
care of one who has taken
poison.
Language
- Talks about common
accidents.
- Reads and writes words,
sentences and stories
about accidents.
-Guided
discussion
-Group work.
Demonstration.
• Collecting first
aid items.
• Making a first
aid box.
• Demonstrating
how to give first
aid.
-Critical
thinking.
-Problem
solving
-Coping with
stress.
-Care
Sympathy
-
Responsibility
-Real first aid
materials.
- Chart showing
common
accidents.
Mk
intergrated
Prim Sci
Bk 4 Pg
154
WORLD
OF
LIVING
THINGS
Animal
life
(Rabbits)
Definition of terms
• Rabbitary
• Rabbit keeping
External parts of a rabbit
Breeds of rabbits
• Local
• - Exotic
• Examples of exotic breeds.
Importance / uses of rabbits.
</passage>

<passage id="lchk_5dafbe1c7a86470881adbcdfdb1b75b2" source="Primary 4 Science Scheme of Work for Terms 1–3" part="5">
-Decision
making
-Self
awareness
• Water
• Sugar
• Salt
• Spoons
• Chart
showing the
4Fs
Mk
integrated
Pri Sci Bk
4 Pg 124
Functional
intergrated
Pri Sci for
Ug Pg 180
2 1 HUMAN
HEALTH
VECTORS
AND
DISEASES
Common Vectors
• Definition of vectors
• Examples of common
vectors
• Cockroaches
• Ticks
• Bedbugs
• House flies
• Mites
• Rats
• Lice
• Mosquitoes
• Tsetse flies
The learners:-
• Defines vectors
• Identifies some common
disease vectors
-Guided
discovery
-Question and
answer
Discussion.
Observation
- Naming
- Drawing
- Answering
questions
Match
- Awareness
- Care
Responsibility
-Self
• A chart with
some vectors.
• Real vectors
like
cockroaches
Page 15
* Life cycle of vectors
* Diseases spread by each
vector
• Body structure
• Their habitat
• Their feeding habits
• Their life cycles
• How they protect them
selves from enemies
How vectors spread diseases.
• Through bites of infected
anmals
• Through contaminated food
• Through contaminated air
• Through open wounds
• Through infected insect
bites
Prevention and control
• Proper hygiene
• Covering food.
• Spraying
• Biological control.
• Sleeping under a treated
mosquito net.
• Describes characteristics
of some disease vectors.
Field
Study
awareness
-Decision
making
Taking
Decision
Sharing
Appreciation
Effective
communicatio
n
Page 16
HUMAN
HEALTH
Accidents
poisoning
and first
Aid
Accidents
• Definition
• Types of accidents
• Causes of accidents
• Prevention of accidents
First Aid
• Definition
• Reasons for giving first aid.
• Responsibilities of a first
aider.
• Qualities of a first aider.
• First aid kit (box)
• How to use a first aid kit.
• Components of the first and
kit and uses.
• Places where we find first
aid box
The learner:-
- Names common accidents
and poisoning at home, on
the way to, from and at
school.
- States causes of accidents
and poisoning.
- Demonstrates how to take
care of one who has taken
poison.
Language
- Talks about common
accidents.
- Reads and writes words,
sentences and stories
about accidents.
-Guided
discussion
-Group work.
Demonstration.
• Collecting first
aid items.
• Making a first
aid box.
• Demonstrating
how to give first
aid.
-Critical
thinking.
-Problem
solving
-Coping with
stress.
-Care
Sympathy
-
Responsibility
-Real first aid
materials.
- Chart showing
common
accidents.
Mk
intergrated
Prim Sci
Bk 4 Pg
154
WORLD
OF
LIVING
THINGS
Animal
life
(Rabbits)
Definition of terms
• Rabbitary
• Rabbit keeping
External parts of a rabbit
Subject
• Defines new terms.
• Names external parts of a
rabbit.
• Names breeds of rabbits.
• Lists examples of exotic
Guided
discovery
Discussion
• Drawing.
• Note taking
• Answering oral
and written
questions.
.
-Effective
communication.
-Critical
thinking.
-Creative
-Prepared chart Mk
Intergrated
Prim Bk 4
Pg 180
Page 17
Breeds of rabbits
• Local
• - Exotic
• Examples of exotic breeds.
Importance / uses of rabbits.
• Advantages of keeping
rabbits over other animals.
• Housing in rabbits.
• Management practices.
• Diseases of rabbits and their
control.
• Keeping farm records.
breeds.
• Explains the uses of
rabbits
• Describes the habitat for
rabbits
• Demonstrates skills in
keeping rabbits.
• Names diseases of rabbits
and their control.
• Signs of a sick rabbit
• Requirements of starting a
rabbitary farm
Demonstration
Question and
answer.
Group work
field trip.
thinking.
-Decision
making
-Problem
solving.
-Appreciation
- Patience
-Care
-Fluency
Page 18
HUMAN
HEALTH
Road
traffic
accident
s,
sprains,
strains,
bruises
wounds
</passage>

<passage id="lchk_73b688b0899f450286c151bf40e4f659" source="P 4 Primary Four SCI Scheme OF Work Teacher AC 1" part="5">
-Decision
making
-Self
awareness
• Water
• Sugar
• Salt
• Spoons
• Chart
showing the
4Fs
Mk
integrated
Pri Sci Bk
4 Pg 124
Functional
intergrated
Pri Sci for
Ug Pg 180
2 1 HUMAN
HEALTH
VECTORS
AND
DISEASES
Common Vectors
• Definition of vectors
• Examples of common
vectors
• Cockroaches
• Ticks
• Bedbugs
• House flies
• Mites
• Rats
• Lice
• Mosquitoes
• Tsetse flies
The learners:-
• Defines vectors
• Identifies some common
disease vectors
-Guided
discovery
-Question and
answer
Discussion.
Observation
- Naming
- Drawing
- Answering
questions
Match
- Awareness
- Care
Responsibility
-Self
• A chart with
some vectors.
• Real vectors
like
cockroaches
Page 15
* Life cycle of vectors
* Diseases spread by each
vector
• Body structure
• Their habitat
• Their feeding habits
• Their life cycles
• How they protect them
selves from enemies
How vectors spread diseases.
• Through bites of infected
anmals
• Through contaminated food
• Through contaminated air
• Through open wounds
• Through infected insect
bites
Prevention and control
• Proper hygiene
• Covering food.
• Spraying
• Biological control.
• Sleeping under a treated
mosquito net.
• Describes characteristics
of some disease vectors.
Field
Study
awareness
-Decision
making
Taking
Decision
Sharing
Appreciation
Effective
communicatio
n
Page 16
HUMAN
HEALTH
Accidents
poisoning
and first
Aid
Accidents
• Definition
• Types of accidents
• Causes of accidents
• Prevention of accidents
First Aid
• Definition
• Reasons for giving first aid.
• Responsibilities of a first
aider.
• Qualities of a first aider.
• First aid kit (box)
• How to use a first aid kit.
• Components of the first and
kit and uses.
• Places where we find first
aid box
The learner:-
- Names common accidents
and poisoning at home, on
the way to, from and at
school.
- States causes of accidents
and poisoning.
- Demonstrates how to take
care of one who has taken
poison.
Language
- Talks about common
accidents.
- Reads and writes words,
sentences and stories
about accidents.
-Guided
discussion
-Group work.
Demonstration.
• Collecting first
aid items.
• Making a first
aid box.
• Demonstrating
how to give first
aid.
-Critical
thinking.
-Problem
solving
-Coping with
stress.
-Care
Sympathy
-
Responsibility
-Real first aid
materials.
- Chart showing
common
accidents.
Mk
intergrated
Prim Sci
Bk 4 Pg
154
WORLD
OF
LIVING
THINGS
Animal
life
(Rabbits)
Definition of terms
• Rabbitary
• Rabbit keeping
External parts of a rabbit
Subject
• Defines new terms.
• Names external parts of a
rabbit.
• Names breeds of rabbits.
• Lists examples of exotic
Guided
discovery
Discussion
• Drawing.
• Note taking
• Answering oral
and written
questions.
.
-Effective
communication.
-Critical
thinking.
-Creative
-Prepared chart Mk
Intergrated
Prim Bk 4
Pg 180
Page 17
Breeds of rabbits
• Local
• - Exotic
• Examples of exotic breeds.
Importance / uses of rabbits.
• Advantages of keeping
rabbits over other animals.
• Housing in rabbits.
• Management practices.
• Diseases of rabbits and their
control.
• Keeping farm records.
breeds.
• Explains the uses of
rabbits
• Describes the habitat for
rabbits
• Demonstrates skills in
keeping rabbits.
• Names diseases of rabbits
and their control.
• Signs of a sick rabbit
• Requirements of starting a
rabbitary farm
Demonstration
Question and
answer.
Group work
field trip.
thinking.
-Decision
making
-Problem
solving.
-Appreciation
- Patience
-Care
-Fluency
Page 18
HUMAN
HEALTH
Road
traffic
accident
s,
sprains,
strains,
bruises
wounds
</passage>

<passage id="lchk_2b4fb78b47bb4beab4c6e31bc4cb4036" source="Primary 4 Science Scheme of Work – Term III" part="2">
• Advantages of keeping
rabbits over other animals.
• Housing in rabbits.
• Management practices.
Subject
• Defines new terms.
• Names external parts of a
rabbit.
• Names breeds of rabbits.
• Lists examples of exotic
breeds.
• Explains the uses of rabbits
• Describes the habitat for
rabbits
• Demonstrates skills in
keeping rabbits.
• Names diseases of rabbits
and their control.
• Signs of a sick rabbit
Guided
discovery
Discussion
Demonstration
Question and
answer.
Group work
field trip.
• Drawing.
• Note taking
• Answering oral
and written
questions.
.
-Effective
communication.
-Critical
thinking.
-Creative
thinking.
-Decision
making
-Problem
solving.
-Appreciation
- Patience
-Care
-Fluency
-Prepared chart Mk
Intergrated
Prim Bk 4
Pg 180
For more schemes of work, visit www.uganda.madpath.com
• Diseases of rabbits and their
control.
• Keeping farm records.
• Requirements of starting a
rabbitary farm
HUMAN
HEALTH
Road
traffic
accident
s,
sprains,
strains,
bruises
wounds
• Definition of road accidents.
• Causes of road traffic
accidents.
• How to cross the road e.g.
from zebra crossing.
• How to prevent road traffic
accidents.
Injuries / Fractures
Types of injuries.
• Fractures (types and their
first aid)
• Sprains and strains (their first
aid).
• Dis location and its first aid.
• Bruises and their first aid.
• Blisters and their first aid.
• Wounds and their first aid.
Subject competences
The learner
- Names causes of road
accidents
- Name road users
- Demonstrates how to cross
a busy road.
Language
- Talks about common
injuries.
- Reads , poems , posters
about accidents
Accident
s,
poisonin
g and
First Aid
• Definition of
• Poison
• Poisoning
- Common poisons in our
homes.
- Causes of poisoning.
- Signs of poisoning
- First aid
- How to prevent poisoning.
For more schemes of work, visit www.uganda.madpath.com
Intestinal
worms
infestatio
n
Definition:
• Intestinal worms
• Parasites
• Examples of intestinal worm
(a) Tape worms
- Structure
- How it spreads
- How it feeds
- What it feeds on
- Effect on body prevention
and control
(b) Hook worms
• Structure
• How they enter into the body.
• How they feed.
• Prevention and control.
(c) Round worms (Nematodes)
• Structure.
• How they enter into the body.
• How they feed.
• Prevention and control.
(d) Pin worms (thread worms)
• Their structure
• Feeding habits
• How they enter the body.
• Prevention and control
• Whip worms
• Structure
• How they enter our bodies.
• Their feeding habits
• Prevention and control
The learner:-
• Describes the habits of pin
worms.
• Describes the habits of
whip worms
</passage>

<passage id="lchk_d13b27bd6a7f4f85a1625d3fd208f53f" source="Primary Four Science Scheme of Work, Terms I–III, 2023" part="26">
Chalkb
oard
illustrati
on
Mk.
Int.
sci.
pbk
4
Int.
sci.
sylla
bus
bk 4
solid poison.
5 5 First aid for snake
bites and nose
bleeding.
First aid for snake
bites.
 Tie a tourniquet
between the
bitten part and
the heart to
prevent venom
(poison from
reading the
heart.)
 A tourniquet is a
piece of cloth used
to tie near the
bitten part.
First aid for nose
bleeding
 Bend the patients
head forward.
 Pinch the nose of
the patient and
advise the patient
to breathe through
the mouth.
The learner;
1. Describe and
illustrates the first
aid for snake
bites and nose
bleeding.
The learner;
1. Pronounces,
spells, reads
writes and
demonstrates
meaning of
words related to
first aid
2. Reads,
internalize and
writes texts and
questions
related to first
aid.
Guided
discovery
Discussion
Observati
on
Illustration
Describing
the first aid
for snake
bites and
nose
bleeding
Appreciati-
on.
Care
Awareness
Fluency
Concern
Chalkb
oard
illustrati
on
Mk.
Int.
sci.
pbk
4
Int.
sci.
sylla
bus
bk 4
5 6 Keepin
g
rabbits
RABBIT
S
RABBITS
- A female rabbit is
called a doe.
- A male rabbit is
The learner;
1. Identifies the
external parts of
a rabbit.
The learner;
1. Pronounces,
spells, reads
writes and
Guided
discovery
Discussion
Describing
the first aid
for snake
bites and
Appreciati-
on.
Care
Chart
showin
g parts
of a
Mk.
Int.
sci.
pbk
called a buck
- The young of a
rabbit is called a kit.
- Many young rabbits
born at the same
time are called a
litter.
The external parts of
a rabbit.
2. Draws and
labels the
external parts of
a rabbit.
demonstrates
meaning of
words related to
rabbits
2. Reads,
internalize and
writes texts and
questions
related to
rabbits
Observati
on
Illustration
nose
bleeding
Awareness
Fluency
Concern
rabbit. 4
Int.
sci.
sylla
bus
bk 4
6 1 Keepin
g
rabbits
Types
of
Rabbit
s
Types of Rabbits
1. local breeds
2. exotic breeds
Local breeds of
rabbits.
 They are also
called indigenous
breeds or native
breeds
 They mainly live in
bushes (burrows)
on their own.
Exotic breeds of
rabbits.
 They are kept in
homes (hutches)
 They live in
The learner;
1. Identifies the
types of rabbits.
2. Describe the
CCCs of local
and exotic
breeds of
rabbits.
The learner;
1. Pronounces,
spells, reads
writes and
demonstrates
meaning of
words related to
rabbits
2. Reads,
internalize and
writes texts and
questions
related to
rabbits
Guided
discovery
Discussion
Observati
on
Illustration
. Identifies
the types of
rabbits.
2. Describe
the CCCs of
local and
exotic
breeds of
rabbits.
Appreciati-
on.
Care
Awareness
Fluency
Concern
Chart
showin
g
differen
t
breeds
exotic
breeds.
Mk.
Int.
sci.
pbk
4
Int.
sci.
sylla
bus
bk 4
hutches
constructed by
the farmers.
Examples of exotic
breeds of rabbits.
1. Angora rabbits
2. Rex rabbit
3. Californian rabbits
6 2 Keepin
g
rabbits
Uses of
rabbits
Uses of rabbits
Reasons why people
keep rabbits
 Rabbits are sold
by farmers to get
money.
 Rabbits are a
source of meat
 Rabbits provide
skins used to
make bags,
jackets, belts,
shoes and host.
Comparing the local
and exotic breeds
The learner;
1. States the uses
of rabbits to
people.
2. Compares local
breeds of rabbits
and exotic
breeds.
The learner;
1. Pronounces,
spells, reads
writes and
demonstrates
meaning of
words related to
rabbits
2. Reads,
internalize and
writes texts and
questions
related to
rabbits
Guided
discovery
Discussion
Observati
on
Illustration
Stating the
uses of
rabbits to
people.
Comparing
local breeds
of rabbits
and exotic
breeds.
Appreciati-
on.
Care
Awareness
Fluency
</passage>

<passage id="lchk_72580cdbd253401da5c354457261d4c4" source="P4 Science Remedial Work 2020 Set 3: Our Food – Classes of Food" part="1">
1
BUDO JUNIOR SCHOOL
REMEDIAL WORK 2020 - SET THREE
PRIMARY FOUR
SCIENCE
THEME: HUMAN HEALTH
TOPIC: OUR FOOD
SUBTOPIC: CLASSES OF FOOD
What is food?
Food is something good to eat or drink.
NEW TERMS USED
Nutrients: these are useful components of food.
Nutrition: This is the supplying of nutrients to the body.
Malnutrition: This is a condition caused by lack of a balanced diet.
This condition results from eating a diet in which one or more nutrients are either not enough or are too
much which causes health problems.
Deficiency diseases: These are diseases caused by lack of some food values or nutrients. They normally
result from malnutrition.
Examples of food
• Rice
• water
• Meat
• Beans
• Peas
• Maize
• Greens
The major sources of food in our environment are:
• Plants
• Animals
Places where food is got:
• Markets
• Shops
• Supermarkets
• Water bodies
• Gardens
• Forests e.t.c
2
IMPORTANCE OF EATING FOOD(5Hs)
We eat food to be healthy
We eat food to show hospitality
We eat food because we are hungry
We eat food because it is a habit
We eat food because we are happy
We eat food to get energy
Classes of food
There are 3 major classes of food:
▪ Proteins
▪ Carbohydrates
▪ Vitamins
Proteins are body building foods.
Carbohydrates are energy giving foods
Vitamins are health giving foods
Other classes of food
• Fats and oils
• Mineral salts
• Roughages
• Water
PROTEINS
Proteins are body building foods
There are two kinds of proteins;
Proteins got from animals are called animal proteins.
Proteins got from plants are called plant proteins.
Animal proteins Plant proteins
Meat Beans
Milk Soya beans
Eggs Cow peas
Fish Groundnuts
3
Importance of proteins in our diet
❖ proteins build new cells in our body.
❖ proteins repair damaged body tissues.
Note: proteins are very important during the pregnancy and growth of a baby to build new cells.
❖ Sick people need proteins to repair the damaged tissues and replace dead cells.
When someone lacks proteins they are most likely to suffer from kwashiorkor.
Kwashiorkor
Kwashiorkor is caused by lack of proteins in one’s body.
- Kwashiorkor can be controlled or prevented by eating food rich in proteins.
- It can be prevented by eating a meal containing a balanced diet.
Signs and symptoms of kwashiorkor
• The hair is little and turns brownish or reddish.
• The person is miserable.
• The stomach swells/gets a pot belly.
• The legs and hands swell.
• The skin cracks and also becomes scaly.
CARBOHYDRATES
Carbohydrates are energy giving foods.
Carbohydrates provide the body with energy.
Sources of carbohydrates
- maize
- millet
- Rice
- matooke
- Irish potatoes
- Cassava
- Milk
- All foods with sugar
Note: excess carbohydrates are changed into fats by the body.
When someone lacks carbohydrates they are likely to get marasmus.
Marasmus is also called starvation.
Signs and symptoms of marasmus
- The person becomes weak.
- The face appears old.
- The person becomes thin and underweight.
4
VITAMINS
Vitamins are health giving foods.
There are many kinds of vitamins but the human body needs:
• Vitamin A
• Vitamin B complex
• Vitamin C
• Vitamin D
• Vitamin E
• Vitamin K
Vitamins Vitamin source Deficiency disease Signs and symptoms
Vitamin A
(Retinal)
Liver
cheese
Carrots eggs
Milk
margarine
Butter red palm
oil
Night blindness
(poor night vision)
Poor night vision
The cornea becomes
dry and opaque
Vitamin B1
(thiamine)
Milk yeast
Beans grain
cereals
Groundnuts
meat
Beriberi Muscles weakness
Fast heart rate
Mental confusion
</passage>

<passage id="lchk_452e3a0642be4f88be951edf12f20652" source="KCCA Primary 4 Integrated Science End-of-Year Examination 2022" part="1">
Read the following instructions carefully.

1. This paper is made up of two sections:
AandB

. Section A has 40 questions (40 marks)
- Section B has 15 questions (60 marks)

- Answer ALL questions in both Sections A and B

a PWN

. ALL answers MUST be written in Blue or Black
Ball - point pen or ink

6. Un-necessary alteration of work may lead to
loss of marks.

7. All diagrams MUST be drawn in pencils,

8. Any handwriting that cannot be easily read may
lead to loss of marks,

9. Do not fill any thing in the boxes shown

“For Examiner’s use only”.

©2022 KCCA PRIMARY SCHOOLS EXAMINA TIONS COMMITT 2.

FOR EXAMINER’s USE

ONLY :
oar}

, | MARKS

:

TURN OVER

Scanned with CamScanner

‘Scanned with CamScanner

26. Write down any one PIASCY message found in

your ‘schoo! compound

28. Why is it advisable to wash hands with clear eae
ate a latrine? “a water wd Soap after

stheeeeeas oe

i BDAnY eran! 6 rust Aine

Scanned with CamScanner

31. What is mulching?

‘Scanned with CamScanner

oe

abapweness-s0°°°°

that may make a seed to fail to germin

‘MINATIONS COMMITTEE

HOOLS EXA.
MA SENCE END OF YEAR EXAMINATIONS 2022

‘Scanned with CamScanner

‘Scanned with CamScanner

a) Which body organ is responsible for following functions;
ps blood to all body organs

KCCA PRIMARY SCHOOLS EXAMINATIONS COMMITTEE 7
= © 4 INTEGRATED SCIENCE END OF YEAR EXAMINA TiANC 2099

‘Scanned with CamScanner

a: B
a) Blackfly Bilharzia

i Cholera
Rabies
River blindness

any two examples of annual crops.

Ss eo res Se es

accidents that can occur at home.
we HH) ccceeesesecsenesnenenenssseeneeneseneeteneneetenees

‘Scanned with CamScanner
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
