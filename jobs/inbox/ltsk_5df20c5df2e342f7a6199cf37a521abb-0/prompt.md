# Job ltsk_5df20c5df2e342f7a6199cf37a521abb-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 6 lesson(s) below of week 2 of the Science scheme for Primary Four 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P4: one 40-minute lesson: 2–4 sections; about 12–24 points; meanings, examples and uses; 5–7 activities.

lessonId=lles_fd1c8d85ef044232ae8add26207f1432: lesson 7, Monday, 1 period(s), 40 minutes.
  Unit: Communicable Intestinal Diseases and Worm Infestation (theme: Human Health). Lesson: Dehydration — Dehydration.
  Objectives: Identify, explain or describe dehydration using the cited school science scheme.

lessonId=lles_749f9e8b8f6d4bbebadc864a59a1cf53: lesson 8, Tuesday, 1 period(s), 40 minutes.
  Unit: Communicable Intestinal Diseases and Worm Infestation (theme: Human Health). Lesson: Oral rehydration solution — Oral rehydration solution.
  Objectives: Identify, explain or describe oral rehydration solution using the cited school science scheme.

lessonId=lles_5147b3679ea24a95a7ca5c797e8e36c8: lesson 9, Wednesday, 1 period(s), 40 minutes.
  Unit: Communicable Intestinal Diseases and Worm Infestation (theme: Human Health). Lesson: Intestinal worm infestation — Intestinal worm infestation.
  Objectives: Identify, explain or describe intestinal worm infestation using the cited school science scheme.

lessonId=lles_d031f7e874c542e1a3fffff29c4cce3c: lesson 10, Thursday, 1 period(s), 40 minutes.
  Unit: Communicable Intestinal Diseases and Worm Infestation (theme: Human Health). Lesson: Tapeworms — Tapeworms.
  Objectives: Identify, explain or describe tapeworms using the cited school science scheme.

lessonId=lles_261eec1b640647b39dcf8bdf4d894e31: lesson 11, Friday, 1 period(s), 40 minutes.
  Unit: Communicable Intestinal Diseases and Worm Infestation (theme: Human Health). Lesson: Hookworms — Hookworms.
  Objectives: Identify, explain or describe hookworms using the cited school science scheme.

lessonId=lles_02d2aa79bd9f407590fa7e4da1a8f715: lesson 12, Friday, 1 period(s), 40 minutes.
  Unit: Communicable Intestinal Diseases and Worm Infestation (theme: Human Health). Lesson: Threadworms — Threadworms.
  Objectives: Identify, explain or describe threadworms using the cited school science scheme.

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

<passage id="lchk_14d3b12c87444f08bcf54f1bdd08bc10" source="Primary Four Scheme Work SCI" part="1">
Pd mii hs SCHEME OF WORK FOR TERM If 2023
;

1

— ~
Ww Theme | Topic. S/Topic Competences. * Content Methods LiActivities L/Skills L/Aids | Ref Rnks
k : SUBJECT LANGUA j
: 6 _
Human | Common Diarrheal Learner: ~Reads Defining Guided Defining Problem | chart | St.
health intestinal diseases -Defines words and |. communicable discovery communicable | solving Benard
diseases and communicable sentences diseases Explanation | diseases Logical sci 4 pg
worm diseases . -Construgts ||"“Defining diarrhea | Question Mentioning reasoning 123
infestations Mention the sentences | -Mentioning and answer | diarrhea
' diartheal , | diarrhea diseases diseases
diseases -Effects of diarrhea
- 2 (3Ds)
2 | Human | Common Dysentery, Leamer: | Reads Causes of dysentery | Guided Mentioning Probiem chart St.
heaith intestinal cholera and | -Identifies words arid | Signs and symptoms | discovery signs and solying Benard
diseases and | typhoid causes ofeach’ | sentenceg | of dysentery Explanation | symptoms of | Logical sci 4 pg
worn disease." ~Construgts | Causes of cholera Question each disease reasoning 124
infestations -Signsand ‘ | sentences Signs and symptoms | and answer
symptoms of - of cholera
each disease | Causes of typhoid
Signs and symptoms
_. of typhoid im
3 | Human | Common Dysentery, Learner: Reads Causes of Guided Mentioning Problem | chart | St.
health intestinal cholera and | Mentions causes | words and | communicable discovery the causes of | solving Benard
diseases and | typhoid of sentences { diseases Explanation | communicable | Logical Sci4 pg
worm communicable |--Constructs | The 4Fs cycle Question diseases reasoning, 126
infestations diseases sentences and answer L
Describes the
4Fs :
4 | Human | Common Dysentery, Learner: Reads How to prevent Guided Identifying Problem | chart ] St.
health intestinal cholera and | Mentions how to | words and | commutable discovery how to prevent | solving Benard
diseases and | typhoid prevent sentenceq diseases Explanation | communicable | Logical sci 4 pg
worm communicable Constructs | Effects of Question. diseases reasoning 129
infestations diseases sentences | commutable “and answer
: =_| diseases et nf
5 | Human | Common Dehydration | Leaner: ~Reads Defining Guided Defining Problem | chart | St.
health intestinal Defines words and | dehydration discovery _ | dehydration . | solving | Benard
diseases and dehydration sentences | Causes of “| “Explanation «|: Idéntifying: © Logical ” * | sci 4 pg
worm Lidentifies -Constructs | dehydration Question causes of reasoning 130
infestations causes of sentences Signs and symptoms | andanswer | dehydration ns
i dehydration f of dehydration Signs and


Mentions signs i symptoms of
and s) dehydration
of de .
Human Common Learner: ~Reads ORS in full Guided Describing Probien Salt St.
health | intestinal Write ORS in words and | Contents ofORs. ; sdiscovery how to prepare solving Water | Benard
: diseases and full sentences « | How to prepare Explanation | ORS Logical Sugar | sci4 pg
worm Prepares ORS Constructs ORS. . Questioa> el pal teasoning 130
infestations Sentences [ and answer *
Human Common -Reads | Examples of Guid Mentioning Problem chart St,
health | intestinal Mentions words and - | intestinal ‘Worms discovery examples of solving Benard
diseases and examples of Sentences Structure and Parts | Explanation worms Logical Sci 4 pg
worm intestinal worms Constructs | of, a tape worm westion Draws and reasoning 133
</passage>

<passage id="lchk_f0819c00bdbe41f2bbcd6f53aa2aa723" source="P 4 Term I, II, III Scie Notes" part="19">
d) Scrubbing etc.
SANITATION AT WATER SOURCES AND ON OUR ROADS
1. Water is a home for many living things.
2. Many germs are found in water.
3. We need to keep our water safe and water sources clean by:
a) Avoid dumping rubbish in water sources.
b) Avoid urinating or defecating near or in water sources
c) Do not share water source with domestic animals
d) Slash bushes around water sources.
e) Put protective covers on open wells
4. Roads are also part of our environment.
5. We need to keep our roads clean
5. Do not dump rubbish, urinate or defecate on the road or path.
62
P.4 Science lesson notes Term III
Theme: Human Health
Topic: Communicable Intestinal Diseases and Worm infestation
A communicable disease is a disease that can be passed on from an infected person to a
healthy one.
Examples of communicable diseases .
a) Diarrhoea
b) Dysentery
c) Typhoid
d) Cholera
Diarrhoea
1. Diarrhoea is the frequent passing out of watery stool.
2. Diarrhoea is caused by bacteria or a virus.
3. The germs can be got from eating contaminated food and water with the diarrhoea germ
How diarrhoea is spread
1. Diarrhoea is spread through the 4FS germ path. The 4Fs are:
Faeces Flies Food Fingers
2. Infected faeces contain germs.
3. Flies pick the faeces with germs and carry them to uncovered food.
4.The food is then contaminated.
6. When a healthy person eats the food, the germs get into the body.
7. Then he suffers from diarrhoea.
Effects of diarrhoea
a) Dehydration
b) Death
The 3D’S
a) Diarrhoea
b) Dehydration
c) Death
Dehydration
1. Dehydration is a condition when the body does not have enough water and mineral salts.
2. A dehydrated person loses water, energy and salts like sodium, potassium, etc.
Causes of dehydration
a) Severe diarrhoea
b) Severe vomiting
c) Severe sweating
Signs and symptoms of a dehydrated person
a) Have sunken eyes
b) Have dry mouth.
63
c) Passes out little or no urine.
d) Have little or no sweat.
e) A dehydrated baby has a sunken fontanel.
f) A pinch on the skin goes slowly to original position.
Treatment of dehydration
a) Giving the patient Oral Rehydration Solution.
b) Giving a patient Sugar Salt Solution.
Note : The solution helps a person to get back the lost water, salts and energy.
Rehydration
1. Rehydration is the replacement of lost body fluids.
2. In rehydration, we use
a) ORS - Oral Rehydration Solution
b) SSS - Salt Sugar Solution
c) Plenty of water, fruit drinks and soup to drink.
3. ORS is made in factories and SSS can be made locally at home.
How to make salt sugar solution
a) Wash your hands clean with safe water and soap.
b) Measure one litre of safe water into a clean container.
c) Measure one leveled teaspoon of salt and 8 leveled tea spoon of sugar.
d) Add the mixture until the salt and sugar disappears/dissolves completely.
How to prevent diarrhoea
a) Scrub the latrines.
b) Wash hands after visiting the latrine.
c) Put all faeces in latrine.
d) Boil drinking water.
e) Cover left over food.
f) Wash hands before and after eating.
Dysentery
1. Dysentery is the passing out of watery stool with blood.
2. Dysentery is caused by bacteria.
3. It can also be caused by a germ called amoeba.
4. The person loses both water and blood.
5. One becomes dehydrated and may die from lack of enough blood.
6. These germs are passed on through infected faeces.
7. Dysentery is spread by a house fly.
8. They both lead to dehydration and death.
Cholera
1. Cholera is caused by bacteria germs.
</passage>

<passage id="lchk_78129b48452e4cff8e709c0b2e755bbb" source="Primary Four Science Scheme of Work, Terms I–III, 2023" part="19">
internalize and
writes texts and
questions
related to
prevention and
control of
Guided
discovery
Discussion
Observati
on
illustration
Stating the
ways of
preventing
the spread
of
diarrhoeal
diseases.
Stating the
effect of
diarrhoeal
Stating the
causes of
dehydration
.
Mentioning
Appreciati-
on.
Care
Awareness
Fluency
Concern
A
picture
of a
dehydr
ated
child.
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
 Too much
diarrhoea
 Too much
vomiting
Signs and symptoms
of dehydration.
 Sunken eyes.
 Little or no urine or
tears.
Diarrhoeal
diseases
signs and
symptoms of
dehydration
. plant.
2 1 Comm
unicab
le
intestin
al
diseas
es and
worm
infesta
tions
Treatm
ent of
dehydr
ation.
Treatment of
dehydration.
 The patient should
be given Oral
Rehydration
solution (ORS)
 ORS is given in
order to replace
the lost body
fluids.
Preparation of ORS /
SSS – Salt sugar
solution ORS – from a
sachet.
What is needed?
1. One sachet of
ORS (oral
rehydration salts)
2. 1 litre (2
tumpecos) of
drinking water.
3. Spoon
4. Water
5. Clean container
The learner;
1. Mentions the
treatment given
to a dehydrated
person.
2. Illustrate how to
prepare ORS/
SSS
The learner;
1. Pronounces,
spells, reads
writes and
demonstrates
meaning of
words related to
treatment of
dehydration
2. Reads,
internalize and
writes texts and
questions
related to
treatment of
dehydration.
Guided
discovery
Discussion
Observati
on
illustration
Mentioning
the
treatment
given to a
dehydrated
person.
Illustrating
how to
prepare
ORS/ SSS
Appreciati-
on.
Care
Awareness
Fluency
Concern
Salt
Sugar
Water
water
jar
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
Steps taken to
prepare
 Wash your hands
with water and
soap.
2 2 Comm
unicab
le
intestin
al
diseas
es and
worm
infesta
tions
Prepar
ation
of S.S.S
– Salt
Sugar
solutio
n
Requir
ement
s
Preparation of S.S.S –
Salt Sugar solution
Requirements
 water and soap
 clean boiled cool
water
Steps taken
 Wash your hands
with water and
soap.
 Measure one litre
of clean cool
boiled water and
pour it in in a
clean container.
 Measure 8
levelled tea
spoons of sugar
and one leveled
tea spoon of salt
into the container
The learner;
1. Identifies the
steps involved in
preparing
ORS/SSS.
2. Practically
prepares ORS/
s.s.s
The learner;
1. Pronounces,
spells, reads
writes and
demonstrates
meaning of
words related to
preparation of
ORS/SSS
2. Reads,
internalize and
writes texts and
questions
related to
preparation of
ORS/ SSS
Guided
discovery
Discussion
Observati
on
Illustration
Demonstr
ation.
Identifying
the steps
involved in
preparing
ORS/SSS.
Practically
preparing O
RS / s.s.s
Appreciati-
on.
Care
Awareness
Fluency
Concern
Salt
Sugar
Water
water
jar
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
2 3 Comm
unicab
le
intestin
al
diseas
es and
WORM
INFEST
ATION
WORM INFESTATION
 Worms are long,
slender soft
bodied animals
with no limbs.
 Worms can live in
soil, bodies of
The learner;
1. Describes worm
infestations.
2. Mentions the
examples of
worms.
The learner;
1. Pronounces,
spells, reads
writes and
demonstrates
meaning of
words related to
Guided
discovery
Discussion
Observati
describing
worm
infestations
Mentioning
the
examples of
Appreciati-
on.
Care
A chart
showin
g
differen
t types
of
worms.
Mk.
Int.
sci.
pbk
4
worm
infesta
tions
animals, in fresh
water, in plants,
fruits or
vegetables.
Examples of intestinal
worms
 tape worms
 hook worms
How we can get
worms.
 Eating
contaminated
food with worms
or eggs
 Drinking
contaminated
water-Eating
under cooked
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

<passage id="lchk_1b88b6d5144441fabe043b13479541af" source="P4 Science Remedial Work 2020 Set 3: Our Food – Classes of Food" part="3">
• Boiling
• Frying
• Roasting
• Baking
• Mingling
• Steaming
Food preservation
Food preservation is a way of keeping food from going bad over a period of time.
Ways in which food can be preserved
• Salting
• Sun drying
• Refrigerating/freezing
• Tinning/canning
• Smoking
9
EXERCISE 1.
1. What is food?
2. Mention two groups of people who need proteins most.
3. Name the deficiency disease caused by lack of:
a) Proteins
b) Carbohydrates
c) Vitamin C
d) Vitamin D
e) Iodine
4. Name two examples of food rich in;
i. Vitamin C
ii. Proteins
iii. Carbohydrates
5. Which deficiency disease affects the eyes?
6. What is malnutrition?
7. Which of the 5Hs is provided by vitamin foods?
8. Name the mineral salt that strengthens teeth and bones.
9. What vitamin is got from morning sunshine.
10. Give one reason why an adult is not advised to drink milk only as a source of food.
11. Mary lacks what to eat, what deficiency disease is she most likely to suffer from?
12. What are excess carbohydrates converted into by the body?
13. How can scurvy be prevented?
14. Mention any two sources of water in the body.
15. Of what importance is water in the body?
10
EXERCISE 2 .
1. Name any two sources of food.
2. Apart from proteins, name any one class of food needed by the body.
3. Out line any one source of food rich in carbohydrates.
4. What is a balanced diet?
5. Which food value is one likely to get from eating ground nuts?
6. State any one reason why people eat food.
7. What causes Kwashiorkor?
8. How can the above disease be prevented?
9. Name any one sign on symptoms of Kwashiorkor.
10. Which food value helps to insulate the body against heat loss?
11. Write any one importance of roughages in one diet.
12. Which food value is absent in milk?
13. Identify the vitamin got from eating fresh fruits and vegetables?
14. Give any two ways one can use to prevent / control / rickets.
15. What causes marasmus?
16. How is Vitamin A useful to our body?
17. Which deficiency disease is causes bleeding of the gum.
18. How can the above disease be prevented?
19. Why is it important for one to add roughages to their diet?
20. Match correctly.
A B
i. Vitamin B I night blindness
ii. Vitamin B 3 beri beri
iii. Vitamin D pelbgra
iv. Vitamin A rickets
21. Define the following.
i. Food contamination
ii. Food preservation
22. Mention any two ways through which food gets contaminated.
23. List any 4 methods of food preservation.
11
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
