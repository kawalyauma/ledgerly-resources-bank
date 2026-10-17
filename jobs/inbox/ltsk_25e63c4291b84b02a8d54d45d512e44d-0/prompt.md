# Job ltsk_25e63c4291b84b02a8d54d45d512e44d-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 6 lesson(s) below of week 10 of the Science scheme for Primary Four 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P4: one 40-minute lesson: 2–4 sections; about 12–24 points; meanings, examples and uses; 5–7 activities.

lessonId=lles_e728a4656de1487e8056f0c9b3fc8423: lesson 55, Monday, 1 period(s), 40 minutes.
  Unit: Rabbit Keeping (theme: The World of Living Things). Lesson: Keeping rabbits healthy — Keeping rabbits healthy.
  Objectives: Identify, explain or describe keeping rabbits healthy using the cited school science scheme.

lessonId=lles_4441b3af29954e7ca1c304659f55f988: lesson 56, Tuesday, 1 period(s), 40 minutes.
  Unit: Rabbit Keeping (theme: The World of Living Things). Lesson: Diseases of rabbits — Diseases of rabbits.
  Objectives: Identify, explain or describe diseases of rabbits using the cited school science scheme.

lessonId=lles_909d4540f9ef4ff3a6a5a30170c6a6c4: lesson 57, Wednesday, 1 period(s), 40 minutes.
  Unit: Rabbit Keeping (theme: The World of Living Things). Lesson: Rabbit parasites — Rabbit parasites.
  Objectives: Identify, explain or describe rabbit parasites using the cited school science scheme.

lessonId=lles_58d00ecfb02c441ba4052b6be4a56bbb: lesson 58, Thursday, 1 period(s), 40 minutes.
  Unit: Rabbit Keeping (theme: The World of Living Things). Lesson: Rabbit farm records and requirements — Rabbit farm records and requirements.
  Objectives: Identify, explain or describe rabbit farm records and requirements using the cited school science scheme.

lessonId=lles_043529a1b10649719c4cd661253fd64a: lesson 59, Friday, 1 period(s), 40 minutes.
  Unit: Rabbit Keeping (theme: The World of Living Things). Lesson: End-of-term assessment — End-of-term assessment.
  Objectives: Complete an approved end-of-term Science assessment using sourced examination questions.
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points ('- ' points, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

lessonId=lles_ff65882172e7490997330038be6c17ad: lesson 60, Friday, 1 period(s), 40 minutes.
  Unit: Rabbit Keeping (theme: The World of Living Things). Lesson: End of term assessment — Communicable Intestinal Diseases and Worm Infestation, Disease Vectors, Accidents and First Aid, Rabbit Keeping.
  Objectives: Assess what learners have learnt this term
  This is the END OF TERM ASSESSMENT. notes = an assessment paper of 15–25 questions from the passages covering the term's units, numbered, with a marking guide (answers) at the end where the passages give them. activities = the questions.

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
<passage id="lchk_dc2c047d903447cab4c39d91ced92868" source="Primary 4 Science Scheme of Work, Term 3" part="1">
1
P.4 SCIENCE SCHEME TERM III
WK PD THEME TOPIC SUB
TOPIC
SUBJECT COMPETENCE LANGUAGE
COMPETENCE
CONTENT METHODS ACTIVITY SKILLS T/AID
S
REF
1 1
Human health
Communicable intestinal diseases and worm
infestation
Communicable diseases
The learner;
Defines communicable
intestinal diseases
Mentions the examples
of such diseases
describes how such
diseases are spread
The learner;
Reads and writes
words and
sentences correctly
Spells words like
communicable,
deficiency, intestine
and health
Infestations
Communicable diseases
Definition of communicable diseases.
Examples of communicable diseases
Communicable intestinal diseases
Definition
Examples
How they spread
Difference between communicable and non-
communicable diseases
Non- communicable diseases
-All deficiency diseases
-Suckle cell anaemia
-Cancer
 Guided discovery
 Question and answer
 Naming common communicable diseases
 Care
 Effective communication
 Learners’ experience
 Comp. Primary Science book 4 page 122
2
Note: Communicable intestinal diseases
are also called diarrhoeal diseases
The learner;
Defines diarrhoea
Gives causes
Writes the 4Fs in full
States the effect of
diarrhoea to human
health
The learner;
Spells words like
-diarrhoea
-severe
-dehydration
-excessive
Diarrhoea
Definition
Cause – bacteria or viruses
The 4Fs germ path
Danger of excessive diarrhoea
Prevention and control of diarrhoea
 Guided discussion
 Naming the 4Fs disease germ
path
 Effective communication
 Care
 Chalk board illustration
 MK primary Science book 4 page
122
3
Note:
Communicable
intestinal diseases The learner;
Defines dysentery
Explains how dysentery
spreads
Mentions at least three
The learner;
Pronounces words
like
-Dysentery
-Stains
-Stool
Dysentery
Definition
How it spreads
Cause of dysentery
 Self
discover
y
 Question
and
 Explainin
g how
dysenter
y
 Problem
solving
 Care
 Chalk
board
illustrati
 MK
primary
Science
2
signs and symptoms of
dysentery
-Watery Signs and symptoms of dysentery
4
Human health
Communicable intestinal diseases and worms
communicable diseases
The learner
Describes the cause
and spread of cholera
Mentions the signs of
cholera
Explains the way of
controlling cholera
The learner;
Reads and spells
words and
sentences
Pronounces words
correctly
Cholera
What causes Cholera?
How is cholera spread?
Signs of cholera
Prevention of cholera
Effects of cholera on human health
 Guided discussion
 Question and answer technique
 Stating the preventive and control measures for cholera
 Problem solving
 Self esteem
 Drawn chart showing a cholera patient
 Primary 4 syllabus page 17
 Comp. Scine page 102
5
Human health
Communicable
intestinal diseases
and worms
communicable
diseases
The leaner;
Mentions the cause of
typhoid
Explains how typhoid
spreads
Mentions the signs and
The learner;
Reads and writes
words and
sentences correctly
Tells stories about
typhoid outbreak
Typhoid
Causes of typhoid
How typhoid is spread
Signs and symptoms of typhoid
Prevention and control of typhoid
 Guided
discovery
 Brain
storming
 Stating the
signs and
symptoms
of typhoid
 Critical
thinking
 Empathy
 Chalkboard
illustration
 Primary 4
syllabus
page 17
3
symptoms of typhoid
Explains how to
prevent typhoid
Diarrhoeal
Faecal
Faeces
Effect of typhoid on human health
2 1
Human Health
Communicable intestinal diseases and worms
Communicable diseases
The learner;
Defines dehydration
Mentions the cause of
dehydration
Describes the signs of
dehydration
Explains the treatment
</passage>

<passage id="lchk_b27e946bc5fb41328c393e4048eabc7c" source="Primary 4 Science Scheme of Work, Term 3" part="2">
for dehydration
Describes how to make
ORS in four sentences
The learner;
Describes the steps
of making ORS.
Reads and spells
words like
-dehydration
-rehydration
-solute
-solvent
-dissolves
Dehydration
Definition
Causes of dehydration
Salts lost during dehydration
The signs of dehydration
Treatment and prevention of dehydration
Oral rehydration solution
In full and short
Importance to the victim
Materials used for preparing ORS – sugar, salt, safe
drinking water
Uses of each
Steps involved in making ORS.
 Self discovery
 Question and answer technique
 Experimentation
 Describing the steps involved in preparing ORS
 Problem solving
 Critical thinking
 Chalkboard illustration
 Comp. Science page 80
 MK Science page 125
2
Human Health
Communicable
intestinal diseases and
worms
Communicable diseases The learner;
Defines a parasite
Mentions the examples
of intestinal worms
Describes tape worms,
feeding and habitat
The learner;
Reads, spells,
pronounces key
words correctly;
-host
-ecto
-endo
Worms infestation
Why they are parasites
Definitions of a parasite
Examples of common discussion worms
Tape worms
What they feed on
 Guided
discussion
 Brain storming
 Discussing the
dangers of
tape worms
 Effective
communicatio
n
 Chalkboard
illustration
 MK Science
page 128
4
Draws the structure of
a tape worm -malnutrition Where they live
Structure of a tape worm
Signs and symptoms of tape worm infestation
Prevention of tape worms
Dangers of tape worms
-They lead to frequent hunger / malnutrition
-They lead to wounds in the intestines
-They can lead to intestinal obstruction
3
Human health
Communicable intestinal diseases and worm
infestation
Worm infestation
The learner;
Describes the life cycle
of a hook worm
Explains how hook
worms enter our
bodies
Mentions the signs and
symptoms of hook
worm infestation
States the dangers of
hook worms on human
health
States the preventive
measures for hook
worms
The learner;
Reads and spells
words correctly
Reads and tells
poems about hook
worms
Hook worms
How they look like (structure)
How they enter our bodies
Signs and symptoms of hook worm infestation
Dangers of hook worms to human health
Explains the preventive and control measures for
hook worms
Prevention and control of hook worms
 Question and answer technique
 Brain storming
 Discussing the preventive and control
measures for hook worms
 Problem solving
 Effective communication
 Illustration of hook worms on the chalk
board
 Science syllabus page
 MK science book 4 page 129
4
Human health
Communicable
intestinal diseases and
worm infestation
Worm infestation The learner;
Explains how thread
worms look like.
Mentions the signs and
symptoms of thread
worms and ascaris
States the effects of
The learner;
Pronounces words
correctly
Writes sentences
correctly
-attachment
Thread worms
Structure
How they enter our bodies
Signs and symptoms of thread worms infestation
Effects of thread worms on human health
 Guided
discussion
 Stating the
effects of
thread worms
 Problem
solving
 Chalkboard
illustration
 MK Science
book 4 page
131
5
thread worms and
ascaries
Describes the
prevention
-hooks
-suckers
-sucking
Prevention and control of thread worms
5
Human health
Communicable intestinal diseases and worm infestation
Worm infestation
The learner;
Mentions where ascaris
live
Explains how ascaris
enter our bodies
States the danger of
ascaris to man
Mentions the general
control measures for
worms
The learner;
Spells, reads and
</passage>

<passage id="lchk_687fb75c4339419d940590d699cef987" source="Primary 4 Science Scheme of Work, Term 3" part="3">
writes words like
- Ascaris
- Bowels
- Burrow
Ascaris
How they enter our bodies
Where they live in the human body
Danger of ascaris
General control measures for worms
 Guided discovery
 Question and answer technique
 Discussing the general control measures for worms
 Effective communication
 Problem solving
 Chalkboard illustration
 Compo. Primary Science
3 1
Human health
Disease vectors
Common vectors
The learner;
Defines a vector and a
germ
Mentions the examples
of common vectors
Draws common vectors
Mentions the habitat
The learner;
Reads, spells and
pronounces key
words correctly
-cause
-transmit
Vectors
Definition
Examples of common vectors
Diagrams of common vectors
Cockroaches
Habitat
 Discussion
 Group work
discussion
 Naming common
vectors
 Empathy
 Problem solving
 Drawing of
common vectors
 Comp. Primary
Science book 4
page 117
6
for a cockroach.
Draws the life cycle of a
cockroach and names
the stages
Names the diseases
spread by a cockroach.
Explains how
cockroaches spread
diseases
Why they move at night
Lifecycle of a cockroach
Diseases spread by cockroaches
How cockroaches spread diseases
Prevention of diseases spread by cockroaches
2
Human health
Disease vectors
Common vectors
The learner;
Mentions the breeding
places for houseflies
Explains how houseflies
spread germs
Draws the life cycle of a
house fly
Mentions the diseases
spread by a house fly
States the 4Fs disease
path
Discusses ways of
controlling the diseases
spread by houseflies
The learner;
Reads and writes
words and
sentences correctly
-hairy
-carry
-carrier
House flies
Breeding places
Life cycle of a house fly
How houseflies are able to spread germs
Diseases spread by houseflies
The 4FS disease path
Ways of controlling the diseases spread through
houseflies
 Guided discovery
 Question and answer
 Drawing the life cycle of a house fly
 Effective communication
 Problem solving
 Life cycle of a house fly on a chart
 MK primary science book 4 page 143
3
Human health
Disease vectors
Common vectors
The learner;
Describes the structure
of a mosquito
Names the habitat for
mosquitoes
Draws the life cycle of a
mosquito
The learner;
Reads, spells and
pronounces key
words correctly
-wringler
-wringling
-Proboscis
Mosquitoes
Breeding place and habitat
Types of mosquitoes
Life cycles of mosquitoes
Diseases spread by each mosquito
 Guided discussion
 Question and
answer technique
 Drawing the
mosquito life
cycles
 Creative thinking
 Self awareness
and Empathy
 Life cycle of
mosquitoes and
on a chart
 Comp. Primary
science book 4
page 109
7
Names the diseases
spread by mosquitoes
4
Human health
Disease vectors
Common vectors
The learner;
Explains how malaria
spreads
Mentions the signs and
symptoms of malaria
States the control
measures for malaria
Ways elephantiasis and
yellow fever are spread
The learner;
Reads a poem about
mosquitoes
How malaria spreads
Signs and symptoms of malaria
Ways of controlling malaria, yellow fever and
elephantiasis
 Discussion
 Brain storming
 Discussing ways of
controlling malaria
 Effective communication
 Chalkboard illustration
 Comp. Primary Science
book 4 page 109
5
Human health
Disease vectors
Common vectors
The learner;
Describes the life cycle
of a tsetse fly.
Names the diseases
spread by a tsetse fly
Mentions the signs and
symptoms of sleeping
sickness.
States the control
measures for tsetse
flies
The learner;
Reads and writes
words and
sentences correctly
-trap
-warmth
-trypanosoma
Tsetse flies
</passage>

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

<passage id="lchk_4de44e5115ce4459905a5f4fb53d384d" source="Primary 4 Science Scheme of Work, Term 3" part="7">
Litter of rabbits
Care for young rabbits
2
The world of living things
Rabbit keeping
Rabbit management
practices
The learner;
Explains how to keep
the rabbits healthy
Names the common
disease of rabbits
Identifies the signs and
symptoms of each
disease
The learner;
Spells and reads
words like
-coccidiosis
-snuffles
-canker
-colds ....
-pneumonia
Hygiene / ways of keeping rabbits health
Proper feeding
Cleaning the hutch regularly
Proper ventilation of the hutch
Diseases of rabbits
Signs and symptoms of each disease
 Role play
 Brain storming
 Naming common
rabbit diseases
 Care
 Problem solving
 Chalk board
 MK book 4 page
185
3
The world of living things
Rabbit keeping
Rabbit management practices The learner;
Mentions the ways of
controlling rabbit
diseases
Names the parasites in
rabbits
States ways of
controlling rabbit
parasites
The learner;
Reads, spells and
pronounces words
-parasite
-feed
-tick
-mite
Ways of controlling rabbit diseases
Keeping hutches clean
Proper feeding....
Parasites of rabbits
Definition of a parasite
Examples of parasites
Types of parasites
 Discussion
 Question and answer
 Naming common
rabbit parasites
 Care
 Problem solving
 Real parasites
 MK science book 4
page 186
15
Ways of controlling parasites
4
The world of living things
Rabbit keeping
Rabbit management practices
The leaner;
Defines records
Mentions the examples
of records kept in a
farm
Mentions the reasons
why farmers keep
records
Names the
requirements for
starting a rabbit farm
The learner;
Writes records kept
in rabbit keeping
Record keeping
Records are written statements about all activities
carried out in a farm.
Examples of rabbit records
Record table
Reasons why farmers keep records (importance)
Requirements for starting a rabbit farm
 Discovery
 Brain storming
 Drawing record tables for rabbit
farms
 Critical thinking
 Problem solving
 Sample record on a chart
 MK Primary Science book 4 page
187
END
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
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
