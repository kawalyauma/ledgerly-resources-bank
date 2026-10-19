# Job ltsk_9e8d22d1ec9e41daa17ede9336d53284-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 5 lesson(s) below of week 3 of the Science scheme for Primary One 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P1: one 40-minute lesson: 1–2 small ideas; about 6–14 short points; very short words; concrete/local examples; 3–5 oral, matching, tracing or picture-led activities.

lessonId=lles_bcccde7511234475802ce85c11a721ba: lesson 11, Monday, 1 period(s), 40 minutes.
  Unit: Transport (theme: Our Transport). Lesson: Dangerous things on the road — Dangerous things on the road.
  Objectives: By the end of the lesson, learners should be able to name three dangerous things on the road.; By the end of the lesson, learners should be able to identify a road hazard in a picture.

lessonId=lles_24cdae453b09407f9aa54a2d6f5db1eb: lesson 12, Tuesday, 1 period(s), 40 minutes.
  Unit: Transport (theme: Our Transport). Lesson: Causes and control of road accidents — Causes and control of road accidents.
  Objectives: By the end of the lesson, learners should be able to identify two causes of road accidents.; By the end of the lesson, learners should be able to state two ways of avoiding road accidents.

lessonId=lles_011fce4d2c6042eda8115fd8151dcac2: lesson 13, Wednesday, 1 period(s), 40 minutes.
  Unit: Things we make and communication (theme: Things We Make). Lesson: Things we make at home — Things we make at home.
  Objectives: By the end of the lesson, learners should be able to name three things made at home.; By the end of the lesson, learners should be able to sort familiar things into playing things and kitchen tools.

lessonId=lles_b8eb824890eb40a5acdba87e92fc4b0d: lesson 14, Thursday, 1 period(s), 40 minutes.
  Unit: Things we make and communication (theme: Things We Make). Lesson: Means of communication — Means of communication.
  Objectives: By the end of the lesson, learners should be able to identify familiar means of communication.; By the end of the lesson, learners should be able to state a use of communication.

lessonId=lles_78c112225ad24af09f6eddfe38f72442: lesson 15, Friday, 1 period(s), 40 minutes.
  Unit: Things we make and communication (theme: Things We Make). Lesson: Week 3 review — Transport, Things we make and communication.
  Objectives: Review this week's lessons: Dangerous things on the road; Causes and control of road accidents; Things we make at home; Means of communication
  This is the FRIDAY REVIEW of this week's lessons (listed in the objectives). notes = a '### Summary' heading per lesson with its key points ('- ' points), then '### Exercise' with review questions taken from the passages. activities = those questions.

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
<passage id="lchk_e3d07b1570aa426dbf34b81164b491c6" source="P I Literacy Scheme OF Work Term III" part="2">
- Parking, traffic lights, No
parking , school ahead, zebra
crossing, round about, humps,
a head, stop accident a head,
railway crossing, bridge, a
head, animals, crossing
- Guided
discussion
- Guided
discovery
- Question
and
answer
- Spellings
- Reading
- Writing
- Drawing
- A chart
showing
road
signs
- Effective
communic
ation
- Patience
- Responsib
ility
- Care
Rs them lit I Bk I pg 106 & 107 Kobta lit Bk I
PG 74
4 Traffic
lights
- Identifies the three
colours of the traffic
lights and their
meanings.
- Spells, reads and
pronounces the words
correctly.
- Draws and names the
colours of the traffic
lights.
- Writes the correct
spellings
Traffic lights
There are three colours of the
traffic lights
- Red
- Orange
- Green
Means of traffic lights
- Red – stop
- Orange – get ready
- Green – go
5 - Identifies the safe ways
of using the road
- States the unsafe ways of
using the road.
- Spells, reads and
pronounces words
correctly
- Writes correct spellings
Safe ways if using the road
- Use zebra crossing, it is a safe
place to cross from.
- Obey traffic lights.
- Do not cross the roads while
running
- Follow the traffic lights
- Walk in a single line on the
road.
- Look right, look left, look right
again, then cross the road.
- Use foot paths for pedestrians
on the road.
- - - -
KOBTA Lit Bk I pg 75 – 76
1 A learner
- Identifies the dangerous
things on the road
- Spells, reads and
pronounces words
correctly.
- Writes correctly
Dangerous things on the
road
- Broken bottles
- Broken electric wires
- Over speeding cars
- Falling trees
- Pot holes
- Nails
- stones
- Guided
discussion
- Guided
discovery
- Question
and
answer
- Reading
- Spelling
- Writing
- A chart
showing
dangerou
s objects
which
cause
accidents
on the
road
- Conscious
ness
- Responsib
ility
- Care
The
metic
Lit I
Bk I
Pg
79
2 - Identifies the cause of
road accidents and how
to control accidents.
- Spells, reads and
pronounces words
correctly.
- Writes the words
correctly
Causes of road accidents
These are things that may lead
to accidents on the road.
Examples
- Over loading/ bicycles/ motor
cycles
- Talking on phone while
driving
- Speeding drivers
- Drunken drivers
- Pot holes
- Slippery roads
- Bad weather
- Driving vehicles in bad
mechanical condition
- Bad roads
How to control accidents on
the road
- Cross on the zebra crossing
- Follow road signs
- Avoid playing on the road
- Follow traffic rules
- Proper disposal of broken
bottle and glasses.
- - - -
3 - Identifies the most
expensive, cheapest
common and quickest
type of transport.
- States the importance of
transport.
- Spells, reads and
pronounces the words
correctly.
- Writes the words
correctly
Importance of transport
- Carrying people
- Carrying animal
- Carrying goods
- Carrying water
- People get jobs e.g taxi drivers,
boda boda riders.
Comparing types of
transports
- Most expensive – air transport
- Cheapest – water transport
- Commonest – road transport
- Quickest – air transport
- Guided
discussion
- Guided
discovery
- Question
and
answers
- Spelling
- Reading
- Writing
- A chart
showing
different
means of
transport
- Care
- Problem
solving
- Love
Kobta Lit BK 1 pg 95
4 Things we
make
Things we
make at
home
- Identifies the things we
make at home.
- Spells, reads and
pronounces words
correctly.
- Draws the things we
make at home
Things we make at home
- Playing things: e.g balls,
dolls, ropes, toy cars, kites,
mats.
- Kitchen tools: basket, plates,
cups, pots, mortar, pestles,
charcoal, stove, winnower,
</passage>

<passage id="lchk_c59083b188004ce194c13f539473b127" source="P I Literacy Scheme OF Work Term III" part="3">
mingling stick, trays.
- - Spelling
- Reading
- Writing
and
drawing
- A chart
showing
things we
make and
real
objects
- Problem
solving
care
- Responsib
ility
- Appreciate
Kobta Bk I pg 101 - 103
Communi
cation
Means of
communicati
on
- Defines common types
of communication
- Give examples of
means of
communication
- Draw means of
communication
Definition of communication
Types of communication
Examples of communication
Means of communication
Uses of communication
Number plates and their
importance
- - - Real
objects
-
Kobta bk 1 pg 97
5 Furniture - Identifies the term
furniture and crafts.
- Identifies examples of
furniture and craft.
- Spells, reads and
pronounces words
correctly.
- Draws and names
examples of furniture
Furniture
- Furniture are things made out
of wood.
Furniture used at home
tables, chairs, beds cupboards,
stools, doors, windows.
Crafts
- Crafts are things we make out
of local materials using hands
e.g. Omaments like bangles,
finger rings, necklaces.
- Guide
discussion
- Guided
discovery
- Question
and
answer
- Reading
- Writing
- Spelling
- A chart
showing
examples
of
furniture
- Creatively
appreciati
on
Kobta Bk 1 pg 103
1 Things we
make
Clothes A learner
- Identifies the clothes
we make and use at
home
- Spells, reads and
pronounces words
correctly.
- Writes the words
Clothes we make to wear
Examples
- trousers
- shirts
- dresses
- sweaters
- jackets
- coats
- Guided
discussion
- Guided
discovery
- Question
and
answer
- Spelling
- Reading
- Writing
- Drawing
- A chart
showing
examples
of
furniture
used at
home
- Creativity
- Problem
solving
correctly.
- Draws and names the
clothes we use at home
others are
- belts
- bags
- hats
- shoes
-
2 Tools - States the tools we
make at home.
- States the things we
make at school
- Reads, spells and
pronounces words
correctly.
- Draws pictures of tools
and things we make.
Tools we make at home (Text
book teaching)
hoes, slashers, knives, rakes,
pangas, wheel barrow, axe.
Things we make at school
hats, baskets, pots, chairs,
dolls, brooms, stools, toy cars,
ropes, mats, table cloths, cups,
kites, scarves, sweaters
titles of people who make
things
- Tailors, potter, carpenter,
black smith
- Who is a tailor and potter
- - - A chart
showing
tools we
make at
home at
real
objects
-
3 Use of
things we
make
- States the uses of things
we make
- States the things we
make and their materials
- Reads, spells and
pronounces words
correctly
Use of things we make
- Mat – sitting on
- Balls – playing football and net
ball.
- Dolls – playing with
- Bricks – building
- Stools/ chairs – sitting on
- - - Real
objects
- Awareness
- Appreciati
on
- Creativity
- Writes the words
correctly
- Ropes – skipping
Materials used for things we
make
- sisal - mud
- clay - beads
- raffia - banana fibres
- threads - papers
- papyrus reeds
4
Our Environment
Components of environment
A learner
- Defines environment.
- States components of the
environment
- Spells, reads and
pronounces words
- Writes words correctly
- Draws some components
of the environment
Environment
Environment are the natural
surroundings of man.
Components of the
environment
Plants, animals, insects, birds,
soil, hills, mountains, swamps,
rivers, valleys, people, lakes,
wells, air
-
- Guided
discovery
- Guided
discussion
- Question
and
answer
- Spelling
- Reading
- Writing
- Drawing
- Real
objects
and a
chart
- Awareness
- Appreciate
- Creative
thinking
5
Living things
- Defines living things
- Identifies characteristics
</passage>

<passage id="lchk_82c1a2885f414f588bf14de72f1767bd" source="P I Literacy Lesson Notes Term III" part="4">
4. What are domestic animals?
5. Give three examp
6. How is a zebra crossing useful to road users?
7. Listen and write
8. Name the dangerous objects
Date Class L. Area
THEME : Transport
SUBTHEME : Road safety
COMPETENCES : A Learner
- States
- Identifies the most expensive, cheapest, commonest and quickest
type of transport.
- Identifies ways of controlling accidents
- Reads , spells and pronounces the words correctly
- Writes the words correctly
METHODS : Guided Discussion
- Guided discovery
- Question and answer
CONTENT : Importance of transport
 Carrying people ( transport people)
 Carrying goods
 Carrying animals
 Carrying water
 Employing people
 Earning money
13
pot holes bad roads
Mention three accidents at home
An ___________is a sudden happening that causes harm or
injury to the body.
What are domestic animals?
Give three examples of domestic animals.
How is a zebra crossing useful to road users?
Listen and write
Name the dangerous objects
L. Area No. of children Time
Transport
Road safety
A Learner
States the importance of transport.
Identifies the most expensive, cheapest, commonest and quickest
type of transport.
Identifies ways of controlling accidents
Reads , spells and pronounces the words correctly
Writes the words correctly
Discussion
Guided discovery
Question and answer
Importance of transport
Carrying people ( transport people)
Carrying goods
Carrying animals
Carrying water
Employing people
Earning money
An ___________is a sudden happening that causes harm or
Identifies the most expensive, cheapest, commonest and quickest
Reads , spells and pronounces the words correctly
 Transport school children
Comparing transport
 Most expensive
 Cheapest
 Commonest
 Quickest
 Slowest
Exercise
1. Mention the importance of transport
2. Draw these things we us to clean our body.
Soap
3. Draw and shade the traffic lights.
4. Which type of transport I;
a. The commonest
b. The slowest
c. The fastest
5. Fill in the missing letters
exp __nsiv___
g __ __ds
6. Draw and
1. How do we call the movement of people with their goods from one place to another?
2. Identify the four types of transport
______ _______
3. Match correctly
bus water transport
14
Transport school children
Comparing transport
Most expensive – air transport
Cheapest – water transport
Commonest – road transport
Quickest – air transport
Slowest – water
Mention the importance of transport
Draw these things we us to clean our body.
Sponge Tooth brush Towel
Draw and shade the traffic lights.
Which type of transport I;
The commonest - ________________
The slowest - ____________________
The fastest - _____________________
Fill in the missing letters
exp __nsiv___ ch ___ ___p tr ___nsp___rt
g __ __ds
Draw and name three things made out of wool
End of theme test
How do we call the movement of people with their goods from one place to another?
Identify the four types of transport
_______ ________ __________
water transport
Towel
tr ___nsp___rt
How do we call the movement of people with their goods from one place to another?
15
train air transport
aeroplane railway transport
ship road transport
b) which means of transport can you use to go to London?
4. Name the means of transport
5. Which is the most expensive type of transport?
6. Draw to show a train
7. Name the cheapest and slowest type of transport
8. Draw and name four means of road transport
9. Write their titles
A person who drives a bus
A person who flies an aeroplane
People who travels in a bus
</passage>

<passage id="lchk_db5aee10b6944b13b0185638aff6c33f" source="P I Literacy Lesson Notes Term III" part="3">
3. Listen and write
4. Identify two domestic birds
5. Write the name of your headteacher
Date Class L. Area No. of children Time
THEME : Transport
SUBTHEME : Road safety
COMPETENCES : A Learner
- Identifies the threecolours of the traffic lights
- Tells the meanings of the traffic lights
- Mentions the safe and unsafe ways of using the road
- Spells reads and pronounces words correctly
METHODS : Guided discussion
- Guided discovery
- Question and answer
CONTENT : Traffic lights
There are three colours of the traffic lights
 Red
 Orange
 Green
Meaning of traffic lights
 Red – stop
 Orange – get ready
 Green – go
10
Safe ways of using the road
 Use zebra crossing, it is a safe place to cross from
 Obey traffic rules
 Do not cross the road while running
 Following the traffic lights
 Walk in a single line on the road
 Look right, look left and look right again, the cross.
 Use foot paths for pedestrians on the road
Unsafe ways of using the road
 Playing on the road
 Grazing on the road
 Over loading of cars
 Over speeding of cars
 Driving while drunk
Exercise
1. Name the three colours of the traffic lights
2. Write the meaning of the traffic lights
a) Read means __________
b) Orange means __________
c) Green means ____________
3. Underline the safe ways of using the road
a) Follow the traffic lights, over speeding
b) Obey traffic rules
4. Why is it good for you to follow road signs?
5. A person who walks on the road is called a_____
6. Why is it bad to run while crossing the road?
7. Write the name of your school
Date Class L. Area No. of children Time
THEME : Transport
SUBTHEME : Road safety
COMPETENCES : A learner
- Identifies the dangerous things on the road
- Read , spell and pronounce the words correctly
- Write the spellings correctly
METHODS : Guided discussion
- Guided discovery
- Question and answer
11
CONTENT : Dangerous things on the road
 Broken bottles
 Broken electric wires
 Over speeding cars
 Falling trees
 Pot holes
 Nails
 Stones
 Snakes
Exercise
1. Identify four dangerous things on the road
b) ________________ c) _______________
c) _______________ d) _______________
2. Draw these dangerous things on the road
Nails Stones Broken bottles Cars
3. Write down any two good ways of using the road.
4. What is the meaning of the following road sign?
5. Match food to their classes
Maize body building food
Mango energy giving food
Eggs healthy giving food
6. Draw these accidents
Falls ___________ strings _________
12
Date Class L. Area No. of children Time
THEME : Transport
SUBTHEME : Road safety
COMPETENCES : A learner
- Identifies the causes of road accidents
- Read the words correctly
- Spell and pronounce the words correctly and control measures
METHODS : Guided discovery
- Question and answer
CONTENT : causes of road accidents
These are things that may lead to accidents on the road.
Examples
Over loading/ bicycles/ motorcycles.
Talking on phone while driving
Over speeding drivers
Drunken drivers
Pot holes
Slippery roads
Bad weather
Driving vehicles in bad mechanical condition.
Bad roads
How to control accidents on road
 Cross on the Zebra crossing
 Follow the road signs
 Avoid playing on the road
 Follow traffic rules
 Proper disposal of broken bottles and glasses
Exercise
1. Underline the causes of road accidents
Drunken driver, following road signs ,
pot holes
2. Mention three accidents at home
3. An ___________is a sudden happening that causes harm or
injury to the body.
</passage>

<passage id="lchk_48d27650aa34415baef12c2554a537c0" source="P I Literacy Lesson Notes Term III" part="7">
8. Draw to show danger a head
9. Give two uses of water
REVISION : Things we use for playing
 Balls
 Doll
 Kites
 Balloons
 Toy cars
 Ropes
Exercise
1. Write five things we used for playing
2. Draw these play things.
Kites Balloons Toy cars
3. Draw two things we make for decoration
4. Name things we make for home use
5. Name these things we make for playing.
End of theme test things we make
1. Draw and name four examples of things we make at school
2. Match things we make to their uses
Toy car
Bag
Cup
Charcoal stove
Mat
3. Name these clothes we wear
4. Match things we make to the materials used
Pot
Mat
Mortar / pestle
Broom
5. Of what importance is a panga?
6. Identify three things we make out of wood
7. Give three examples of ornaments
8. Name these things we get from animal skins
24
End of theme test things we make
Draw and name four examples of things we make at school
Match things we make to their uses
sitting on
playing with
carrying books
cooking food
drinking from
Name these clothes we wear
Match things we make to the materials used
grass
clay soil
palm leaves
wood
Of what importance is a panga?
Identify three things we make out of wood
Give three examples of ornaments
Name these things we get from animal skins
25
9. Draw to show the means of road transport
Lorry _________ horse ___________
LESSON Things we make at home and at school
mats, drum, sticks, shakers, boots, dolls, balls, rope, baskets, pots, hats, winnowers, table mats,
decorations
Question
1. Draw and name any four things we can make at home and at school.
Balls Pot hat
Materials used to make things at home and at school
sisal, clay, banana stalks, sticks, tins, cloth, palm leaves, threads, papers, seeds, bottle tops
LESSON
Sources of materials we use to make things at home and at school
swamps, wetland, bush, forests, plants
What do we get from swamps?
- clay
- papyrus
What do we get from forests?
grass, wood, sticks, firewood, herbs, reeds, raffia, palm leaves
Things we make for playing
dolls, ropes, balls, toys
Things we make for domestic use
Mats , baskets, mingling sticks, walking sticks.
Things we make for sale
dolls, baskets, toys, pots, ropes, balls, bags, flower vases, mats, hats , carpets, door mats , table
mats
26
Things we make for decoration
table mats , table, clothes, paper collage , frames
Date Class L. Area No. of children Time
THEME : Our environment
SUBTHEME : Things in our environment
COMPETENCES : A Learner
- Defines environment
- States components of the environment.
- Draws things in our environment
- Spells, reads, and pronounces words correctly.
- Writes the words correctly
METHODS : Brain storming
- Guided discovery
- Question and answer ( out side class room lesson)
CONTENT : Our environment
What is environment?
Environment are the natural surroundings of man.
Components of theenvironment(These should be drawn )
 Plants,
 hills,
 animals ,
 mountain
 birds,
 river,
 Land/ soil,
 people,
 insects,
 lakes
 valleys
 swamps
 air
27
Exercise
1. Write down six things in our environment
2. Fill in the missing letters
Pl__nts b__rds P__ __ple env__ronm__nt
3. Draw these components of the environment
Plants Animals Birds Insects
4. ___________ are the natural surroundings of man (mountain,
environment)
5. How do we call things made out of wood?
Date Class L. Area No. of children Time
THEME : Our environment
SUBTHEME : Components of environment
COMPETENCES : A Learner
- Define living things
</passage>

<passage id="lchk_87d1c44a733548fa934619f27e5b59e1" source="P I Literacy Lesson Notes Term III" part="16">
 Helping one another
 Respecting each other
 Providing basic needs in homes for the school
 Obeying rules and regulations
Causes of insecurity at school
 Playing bad games
 Refusing to respect leaders stealing
 Lack of security at school teasing
 Dangerous things at school fighting
 Not providing school needs
 Failure to obey school rules and regulation
 Child abuse at school punishment using corporal at school
 Stealing people’s property.
How to promote peace and security at school
 Observing class and school rules eg
 Having good relationships with others
 Working well with others
 Sharing with others
 Playing good games with others
 Be hard working and helpful
Exercise
1. Listen and write
2. Write six causes of insecurity at school.
61
3. Write down five ways we keep peace and security
4. Draw children playing together
5. Name any two plants where by we eat leaves.
6. Draw a sugar cane
7. Draw and name three accidents at home
Date Class L. Area No. of children Time
THEME : Peace and security
SUBTHEME : People who keep security at home
METHOD : Guided discovery
Question and answer
Brain storming
COMPETENCES : A learner
- Identifies people who keep security at home
- States ways of promoting peace and security at home.
- Reads, pronounces words correctly.
- Writes the words correctly
CONTENT : People who keep security at home
 Father
 Mother
 Elder brothers
 Elder sisters
 Grand father
 Grand mother
 Uncle
 Aunt
 Workman
62
Ways to promote peace and security at home
 Greeting one another.
 Greeting our parents
 Obeying rules at home/ parents
 Respecting people at home
 Doing house work together
 Praying together
 Showing love to one another
Exercise
1. Fill in the missing
F_th_r a_nt p__ ___ce sec __rity
2. Write five people who keep security at home.
3. Draw these people who keep peace and security at home.
Father Mother Grandfather Uncle
4. Underline things that cause insecurity at home
5. Circle things that promote peace and security.
6. Why do we wash our hands before eating?
7. What makes food go bad?
Date Class L. Area No. of children Time
THEME : Peace and security
SUBTHEME : Causes of insecurity at home
METHOD : Guided discovery
Question and answer
Brain storming
COMPETENCES : A learner
- States ways of promoting peace and security at home.
63
- Identifies causes of insecurity at home
Text book teaching
CONTENT : Causes of insecurity at home
 Lack of basic needs
 Child abuse
 Neglecting homes
 Lack of love at home
 Lack of medical care
 Quarrels among parents
 Disobedience of children
 Having bad neighbours
 Quarreling and fighting among family members
 Laziness and not being helpful
How we can promote peace and security at home
 Promote co-operation among family members
 Good behaviour
 Good health practices e.g keeping our homes clean.
 Respect of elders
 Love and are for one another
 Sharing with others
Exercise
1. ______________is the situation when people are free from danger or
harm.
2. _______________ when people and their property are free from
danger or harm.
3. Write down two causes of insecurity
64
4. Draw a child being taken to hospital
5. How can you keep peace and security at home?
6. Write down 2 causes of insecurity at home.
Date Class L. Area No. of children Time
THEME : Peace and security
SUBTHEME : Things which cause insecurity in homes
METHOD : Guided discovery
Question and answer
Guided discussion
COMPETENCES : A learner
</passage>

<passage id="lchk_9491de5179da48e8888aeb6bd7f511c5" source="P1 Curriculum" part="18">
 Shade/colour pictures related to weather
 Tear and paste creatively
 Model creatively
 Sing songs correctly
 Move to the rhythm
 Play simple percussion instruments
28
28
Theme 6: Accidents and Safety
Expected Learning Outcomes: The learner is able to identify and know the common accidents, understand the importance and effects of taking precautions
SUB-THEME / CONTENT MATHEMATICS
COMPETENCES
LITERACY COMPETENCES ENGLISH (NON-MEDIUM)
COMPETENCES
CREATIVE PERFORMING
ARTS
LIFE SKILLS AND VALUES
6.1 ACCIDENTS AND
SAFETY AT HOME
 Accidents, e.g.:
- burns
- falling
- cutting
- poisoning
- snake / dog bite
- drowning
- electric shock
 Safety
precautions
e.g.
- Avoid playing near fire
and water.
- Keep medicine away
from children.
 Effects of accidents
e.g.:
- blindness
- deafness
- lameness
- sickness
- death
 Counting up to 60
 Writing number symbols
up to 40
 Writing number names 6-
10
 Reading number names
6-10
 Matching symbols to
number names 1-10
 Multiplying table of 2
 Recognising symbol for
multiplication „x‟
 Adding with sum less
than 40 vertically and
horizontally, no carrying
LISTENING AND SPEAKING
 Identifying things that cause bodily
harm
 Naming sharp objects that can cause
harm
 Describing given pictures
 Describing dangerous situations
 Telling / re-telling / signing stories
 Reciting rhymes related to safety
 Saying sentences related to safety,
e.g.:
- Don‟t play with fire.
- Don‟t play with knives.
PRE-READING AND READING /
TACTILE
 Matching
 Fitting jigsaw puzzles
 Playing picture dominoes
 Reading words with double vowels
 Reading 4 simple sentences with link
verbs (e.g. „to be‟, „to have‟)
PRE-WRITING AND WRITING /
BRAILLING
 Writing letters
 Copying words
 Copying simple sentences
VOCABULARY
 Naming accidents and
safety at home e.g. pin,
knife, thorn, fire, razor
blade, broken glass,
needle, sharp, hurt, fall,
burn, cut.
USING STRUCTURES
 „Don‟t play with …‟
 „Show me a …‟
 „This is a …
 „That is a …‟
 „Are you …(hurt, burnt)?‟
 „Yes, I am...‟
 „No, I am not ....‟
 Singing / signing
 Reciting e.g. rhymes
 Role-playing
 Telling / signing stories
 Saying riddles
 Drawing
 Colouring
 Cutting and pasting
 Empathy
 Critical thinking
 Decision-making
 Self-awareness
 Interpersonal relationships
 Self-esteem
 Mobility and orientation
(SNE)
 Care
 Co-operation
 Perseverance
 Responsibility
 Patience
 Friendliness
6.2 ACCIDENTS AND
SAFETY ON THE WAY
 Accidents on
the way, e.g.
- snake/dog/
insect bites
- motor accident
 Sorting
 Matching
 Counting (51-60)
 Writing number symbols
up to 40
 Adding with sum less
than 40 vertically without
LISTENING AND SPEAKING
 Naming different types of accidents
 Listening to stories
 Telling, re-telling /signing stories
 Naming safe ways of moving to and
from school, e.g.:
- Walk on the path
VOCABULARY
Naming accidents and safety
on the way e.g. burn, bite,
play, drown, knock.
USING STRUCTURES
 „Don‟t …(play)‟
 „Be careful with …(dogs)‟
 Singing / signing
 Role-playing
 Telling and re-telling /
signing stories
 Saying riddles
 Reciting, e.g. rhymes
 Making simple
 Empathy
 Decision-making
 Self-awareness
 Interpersonal relationship
 Self-esteem
 Mobility and orientation
(SNE)
29 29
SUB-THEME / CONTENT MATHEMATICS
COMPETENCES
LITERACY COMPETENCES ENGLISH (NON-MEDIUM)
COMPETENCES
CREATIVE PERFORMING
ARTS
LIFE SKILLS AND VALUES
- drowning
- cuts / injuries
- electrical shock
- lightning
 Safety
precautions
e.g.
</passage>

<passage id="lchk_368d2991fa374de796ea6159f5c7dc46" source="P1 Term 3 Literacy 1 Workbook" part="5">
1. Which part do we eat on the following plants ?
cabbage
yam
sugarcane
banana
maize
cassava
onion
sweet potato _
TekArt Learning Workbooks TERM III P.1 Literacy one
work book
Page 31
Date:
Lesson 28 : Things plants need to grow well.
Lesson hints:
 sunlight
 air
 water
 good soil
Activity
1. Write three things that plants need to grow well.
(i)
(ii)
(iii)
Date:
Lesson 29: Ways of caring for plants
Lesson hints:
Ways of caring for plants.
 By watering them.
 By weeding them.
 By harvesting them.
 By manuring them.
 By spraying them.
 By thinning and pruning them.
Activity
1. Write any two ways of caring for a plant.
(i)
(ii)
TekArt Learning Workbooks TERM III P.1 Literacy one
work book
Page 32
2. Draw these ways of caring for plants.
harvesting watering spraying
3. Give two ways of caring for plants.
(i)
(ii)
4. Draw a person watering a plant.
Date:
Sub-theme: Factors that damage our environment.
Lesson 30 : Factors that damage our environment.
Lesson hints:
Activities that spoil our environment
 cutting down trees.
 bush burning.
 leaving uncovered holes.
 over grazing.
 poor waste disposal e.g. polythene bags.
 building and farming in wet land(swamps).
TekArt Learning Workbooks TERM III P.1 Literacy one
work book
Page 33
 Over harvesting of sand, brick making.
 Pollution. (air pollution and water pollution)
 Poor fishing methods e.g catching fish with poison
 Hunting wild animals in game parks.
 Poor farming methods e.g over cultivation.
Activity
1. Underline the activities that spoil our environment.
burning bush, over grazing, sweeping, digging,
dancing, pollution, cutting down trees,
building in wetland,
2. Name any three activities that damage our environment.
(i)
(ii)
(iii)
3. Draw a man cutting down trees.
Date:
Sub-theme: Conservation of our environment
Lesson 31: Ways of conserving the environment.
Lesson hints:
Ways of conserving the environment.
 By planting trees.
 By watering plants.
 By harvesting crops.
TekArt Learning Workbooks TERM III P.1 Literacy one
work book
Page 34
 avoid bush burning
 avoid cutting trees.
 proper disposal of waste products.
 by harvesting water to avoid floods.
 not building in swamps.
 not hunting wild animals.
 Practicing agro forestry (planting crops together with trees)
 keeping water sources clean.
 grazing animals well.
 terracing the hilly land to avoid soil erosion.
Activity
Name these ways of conserving the environment .
TekArt Learning Workbooks TERM III P.1 Literacy one
work book
Page 35
Date:
Lesson 32:
Importance /uses of non living things.
air : Living things (plants and animals) breathe in air to support life
and other things.
houses : We use houses for shelter.
water : We use water for drinking, washing, bathing, cooking
(domestic use).
chairs : We use chairs for sitting
on.
pencils: We use pencils for writing.
Natural things are things created by God.
Non living things that are natural are air, water, clouds, sun, lakes,
river, hills, gardens, soil, forests, roads etc.
Nimbus clouds : give us rain.
Lakes and rivers : are sources of water and homes of some ani-
mals.
hills and mountains : are sources of money from tourists.
gardens : are sources of food.
roads : are used for transport.
Soil/land : is used for farming.
forests : are sources of building materials.
Activity
1. Match the importance of the non-living things.
water bodies writing
soil shelter
houses sources of water
pencils farming
TekArt Learning Workbooks TERM III P.1 Literacy one
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
