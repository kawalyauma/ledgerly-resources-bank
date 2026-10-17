# Job ltsk_ea210e3812864e158e80303c01d002cb-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 6 lesson(s) below of week 6 of the Science scheme for Primary Four 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P4: one 40-minute lesson: 2–4 sections; about 12–24 points; meanings, examples and uses; 5–7 activities.

lessonId=lles_f788139fc0614f68856cdd805d605817: lesson 31, Monday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: Common accidents — Common accidents.
  Objectives: Identify, explain or describe common accidents using the cited school science scheme.

lessonId=lles_194b6d1e08bc4a528ca73e33ad8c74f2: lesson 32, Tuesday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: Causes of accidents — Causes of accidents.
  Objectives: Identify, explain or describe causes of accidents using the cited school science scheme.

lessonId=lles_239966c8aebb4db2bb33cc83d800a158: lesson 33, Wednesday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: Accidents at home and school — Accidents at home and school.
  Objectives: Identify, explain or describe accidents at home and school using the cited school science scheme.

lessonId=lles_984c5e6bd15f4bfea603d743ddcb428d: lesson 34, Thursday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: Road accidents — Road accidents.
  Objectives: Identify, explain or describe road accidents using the cited school science scheme.

lessonId=lles_ef585285c736442780045ef44d0412ff: lesson 35, Friday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: Road safety and crossings — Road safety and crossings.
  Objectives: Identify, explain or describe road safety and crossings using the cited school science scheme.

lessonId=lles_fb724a61ea26494db8a1d9e162f7c060: lesson 36, Friday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: Meaning of first aid — Meaning of first aid.
  Objectives: Identify, explain or describe meaning of first aid using the cited school science scheme.

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
<passage id="lchk_e08ff84b884a43039cba425cfdde1b98" source="Primary 4 Science Scheme of Work, Term 3" part="4">
Breeding places
Life cycle of a tsetse fly
Disease spread by a tsetse fly
How such diseases spread
Signs and symptoms of sleeping sickness
Ways of controlling tsetse flies
 Guided discussion
 Question and answer technique
 Drawing the life cycle of a tsetse
flue
 Critical thinking
 Effective communication
 Life cycle of a tsetse fly on a
chart
 MK Primary Science book 4 page
151
4 1
Human health
Disease vectors
Common vectors
The learner;
Describes the structure
of a flea
Mentions where fleas
live
Names the disease
spread by fleas
The learner;
Spells and writes
words and
sentences correctly
-plague
-burrow
-boils
Itch mites
Places they live
Disease spread
How scabies spreads
Ways of controlling scabies
Fleas
 Self discovery
 Question and
answer technique
 Discussing the
prevention and
control measures
for bubonic
 Effective
communication
 Chalkboard
illustration
 MK Primary
Science book 4
page 144
8
Mentions the ways of
controlling bubonic
plague
Describes how itch
mites work
Names places where
itch mites live
Explain how scabies
spreads
-swellings Places they live
Ways fleas spread diseased
Ways of controlling bubonic plague
2
Human health
Disease vectors
Common vectors
The learner;
Mentions the habitat /
breeding place for lice
Names the types of lice
Explains how lice
spread diseases
States ways of
controlling lice
The learner;
Spells words like
-typhoid
-relapsing
-lice
-bubonic
-nits
Lice
Breeding places
Types of lice
Disease spread by lice
Explains how lice spread
Controlling ticks and lice
 Question and answer
technique
 Explaining ways of
controlling lice and
ticks
 Effective
communication
 Real ticks
 MK Primary Science
book 4 page 140
3
Human health
Disease vectors
Common vectors
The learner;
Draws the structure of
a fresh waster snail
Names the disease
spread by a fresh
water snail
Mentions the ways of
controlling bilharzias
The learner;
Reads words and
sentences correctly
-schistosoma
-flukes
-bilharzias
Water snails
Habitats
Diagram of a water snail
Diseases spread by a water snail
Signs and symptoms of bilharzia
 Brain storming
 Guided discovery
 Discussing ways
of controlling
bilharzia
 Problem solving
 Real snails
 Comp. Book 3
page
4
Human health
Accident and first aid
Common accidents
The learner;
Defines an accident
Mentions examples of
accidents
States the effects of
accidents on human
health
The learner;
Reads, spells words
correctly
- bleeding
-steam
-vapour
Accidents
Definition of an accident
Causes of accidents
Examples of common accidents
Types of accidents
Dangers of accidents to human life
 Self discovery
 Discussion
 Discussing common
accidents at home
 Problem solving
 Effective
communication
 Chalkboard
illustration
 MK. Primary Science
book 4 page 154
9
Examples of injuries
5
Human health
Accident and first aid
Common accidents
The learner;
Mentions the common
accidents at home,
school and road
States the causes of
accidents at school,
home and road
Mentions ways of
controlling accidents at
home, school and road
The learner;
Reads, spells and
pronounces key
words correctly;
-mechanical
-motorists
-pedestrians
-cyclists
Accidents at home / school
Examples
Causes
Prevention
Road accidents definition
Causes, definition
Prevention
How to cross the road
 Brain storming
 Question and answer
 Guided discussion
 Naming common accidents
at home
 Effective communication
 Problem solving
 Audio visual learning
 MK Primary science book 4
page 154
5 1
Human health
</passage>

<passage id="lchk_96bb9c91444b4473888ca3f00d68a890" source="Primary 4 Science Scheme of Work, Term 3" part="5">
Accidents and first aid
First aid
The learner;
Defines first aid
Defines a casualty
Mentions the reasons
for giving first aid
States the qualities of a
first aider
Identifies the
responsibilities of a first
aider
The learner;
Reads and writes
words and
sentences about
first aid
-casualty
-bleeding
-anaemic
First aid
Definition
Reasons for giving first aid
Definition of a first aider
Qualities of a first aider
Responsibilities of a first aider
 Discovery
 Question and answer technique
 Stating the qualities of a first aider
 Care, Empathy, creative thinking
 Chalkboard illustration
 Comp. Primary Science book 4 page 161
10
2
Human health
Accidents and first aid
First aid
The learner;
Defines a first aid kit
Mentions the
components of a first
aid box
Defines a first aid box
Mentions the
importance of a first
aid box to a school and
home
The learner;
Reads and writes
words and
sentences correctly
-kit
-components
-constituents
First aid kit
Definition
Components of a first aid box
First aid box
Definition
Diagram
Items which can be kept in a first aid box in a
school and home.
Uses of each element of a first aid box
 Discovery
 Discussion
 Identifying items found in a first aid kit
 Effective communication
 Creative thinking
 Real first aid materials
 Comp. Book 4 Science page 161-162
3
Human health
Accidents and first aid
Injuries
The learner;
Mentions the
examples of injuries
Defines a fracture
Mentions the types of
fractures
Draws the types of
fractures
Describes the first aid
for fractures
The learner;
Spells words like
-fracture
-ligament
-dislocation
-sprain
-strain
-tendon
-musles
Types / examples of injuries
Fractures
Burns and scales
Dislocation
Sprains and strains
Fractures
Definition and causes
Types of fractures
Signs of fractures
First aid for fractures
 Guided discussion
 Questions and answer
 Demonstrating the first aid for fractures
 Sack , stretches and sticks
 Care
 Problem solving
 MK Primary Science book 4 page 161
11
4
Human health
Accidents and first aid
Injuries
The learner;
Defines burns and
scalds
Mentions the causes of
burns and scalds
Describes the first aid
for burns and scalds
Discusses ways of
preventing burns and
scalds
The learner;
Reads and write
words and
sentences like
-scald
-heat
-liquid
-acid
Burns and scalds
Burns
Definition of a burn
Causes of burns
Scalds
Definition of scalds
Causes of scalds
First aid for burns and scalds
Prevention of burns and scalds
 Questions and answer
 Discovery
 Demonstrating the first aid for
burns and scalds
 Water cloth
 Problem solving
 Creative thinking
 MK primary Science book 4 page
5
Human health
Accidents and first aid
Injuries
The learner;
Defines a sprain and a
strain
Mentions the signs of
strains and sprains
Describes the first aid
of sprains and strains
The learner;
Reads, spells and
pronounces words
correctly
-stretched
-torn
-pain
Sprains
Definition
Causes of sprains
Signs of sprains
First aid for sprains
Strains
Definition
Causes of strains
Signs of strains
First aid for strains
 Discovery (Guided)
 Describing the first aid for sprains
and strains
 Care, Problem solving and creative
thinking
 Bandage
 Ice cubes
 MK primary science book 4 page 159
6 1
Human health
Accidents and first
aid
Injuries
The learner;
Defines a dislocation
Mentions the cause of
a dislocation
Describes the first aid
for dislocations
The learner;
Pronounces, spells
and writes words
like
-location
-dislocation
-tourniquet
Dislocation
Definition
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

<passage id="lchk_70d4052bd2d14a1c9da425f429749377" source="Primary 4 Science Scheme of Work for Terms 1–3" part="6">
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
• Sprains and strains (their
first aid).
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
Page 19
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
• How they enter into the
body.
• How they feed.
• Prevention and control.
(c) Round worms (Nematodes)
• Structure.
• How they enter into the
body.
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
Page 20
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
