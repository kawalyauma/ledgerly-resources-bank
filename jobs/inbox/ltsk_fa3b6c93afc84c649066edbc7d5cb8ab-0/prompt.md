# Job ltsk_fa3b6c93afc84c649066edbc7d5cb8ab-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 6 lesson(s) below of week 1 of the Mathematics scheme for Primary Six 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P6: one 40-minute lesson: 3–6 sections; about 16–32 points; worked examples and exam-style points; 6–8 activities.

lessonId=lles_d6800929a40a4259a592cd787486eaec: lesson 1, Monday, 1 period(s), 40 minutes.
  Unit: Length, Mass and Capacity (theme: Length, Mass and Capacity). Lesson: Metric units of length — Metric units of length.
  Objectives: By the end of the lesson, learners should be able to identify metric length units and convert kilometres to metres.

lessonId=lles_a08795a53ec04c749fa12d6af88d1caa: lesson 2, Tuesday, 1 period(s), 40 minutes.
  Unit: Length, Mass and Capacity (theme: Length, Mass and Capacity). Lesson: Converting metric length units — Converting metric length units.
  Objectives: By the end of the lesson, learners should be able to convert metres, decimetres, centimetres and millimetres.

lessonId=lles_95ac4e982f48438f9c315d6b7f62c0fb: lesson 3, Wednesday, 1 period(s), 40 minutes.
  Unit: Length, Mass and Capacity (theme: Length, Mass and Capacity). Lesson: Converting square units — Converting square units.
  Objectives: By the end of the lesson, learners should be able to convert square metres to square centimetres.

lessonId=lles_07e7dda1dff24388b780cd355bc7b3aa: lesson 4, Thursday, 1 period(s), 40 minutes.
  Unit: Length, Mass and Capacity (theme: Length, Mass and Capacity). Lesson: Area and perimeter of a square — Area and perimeter of a square.
  Objectives: By the end of the lesson, learners should be able to find the side and perimeter from the area of a square.

lessonId=lles_fa0ed1447ec64f65a880844618c18068: lesson 5, Friday, 1 period(s), 40 minutes.
  Unit: Length, Mass and Capacity (theme: Length, Mass and Capacity). Lesson: Area and perimeter of a rectangle — Area and perimeter of a rectangle.
  Objectives: By the end of the lesson, learners should be able to find a rectangle’s missing side and perimeter from its area.

lessonId=lles_df846ed449664d83a952543ebad64e97: lesson 6, Friday, 1 period(s), 40 minutes.
  Unit: Length, Mass and Capacity (theme: Length, Mass and Capacity). Lesson: Unknown sides, area and perimeter — Unknown sides, area and perimeter.
  Objectives: By the end of the lesson, learners should be able to find unknown sides, area and perimeter of a rectangle.

Write, using ONLY the passages below. Passages from "NCDC" documents are the official base for what to teach; NCDC lower-primary thematic curricula put every learning area in columns separated by " | ": use only the Mathematics column.
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
<passage id="lchk_036f6f4092db424eb71c43d3de3aaace" source="P.6 MATHEMATICS SCHEME TERM 3" part="1">
1
Tel:0775787978/0742845900 osebEdu@gmail.com ##2023 PLE 🎯
PRIMARY SIX MATHEMATICS SCHEME OF WORK—TERM III,2023 (OSEB Educational consult-Kampala )
W
K
P
D
UNIT TOPIC SUBTOPIC COMPETENCES CONTENT METHOD LIFE
SKILLS
ACTIVITIE
S
L/T
AIDS
REF R
E
M
SUBJECT LANGUAGE
1
1
&
2
&
3
M
E
A
S
U
R
E
M
E
N
T
LENGT
H,
MASS
AND
CAPACI
TY
Conversion
of metric
units
The learner:
1.Identifies
the different
metric units
2. Changes
from one
unit to
another.
3. Changes
from square
unit to
another.
The learner:
reads and
uses the
words such
as metric,
conversion,
units
Example
1. Change
5dm to
centimeters.
2. Convert
8.5m to
millimeters.
3. Express
25Km to
metres.
4.Convert
4m² to cm²
Brainstor
ming
Guided
discovery
Problems
olving
Appreciati
on of
oneself
and
others,
Problem
solving
and
assertiven
ess
Drawing
the table
showing
the
different
metric
units.
Doing the
class
exercise.
A chart
showin
g the
conver
sion of
the
metric
units
Unde
rstan
ding
mtcs
bk 6
page
Mk
mtcs
bk 6
page
313
Foun
tain
mtcs
bk 6
pg
4
&
5
Finding
area when
given the
perimeter
The learner
1.
Calculates
the
perimeter of
the
rectangle
and square.
The learner
explains the
meaning of
words such
as length,
width,
perimeter and
Example
1. The area of
a square is
81cm.
Calculate its
perimeter.
2. The area of
Guided
discovery
Class
discussio
n
Brain
Expressin
g one’s
point of
view,
Effective
decision
making
Answering
the oral
questions
Attemptin
g the
given
evaluation
Chalkb
oard
illustra
tion
Func
tional
mtcs
bk 6
page
Mk
2
Tel:0775787978/0742845900 osebEdu@gmail.com ##2023 PLE 🎯
2. Finds the
missing
side.
3. Calculate
the area
when given
the
perimeter.
area. a rectangle is
45dm and the
width is
5dm.Find the
perimeter of
the same
rectangle.
storming
guided
discussio
n
think and
pair
and
respecting
others.
exercise. mtcs
bk 6
page
333
6
$
1
M
E
A
S
U
R
E
M
E
N
T
LENGT
H,
MASS
AND
CAPACI
TY
Finding the
sides, area
and
perimeter
The learner
1. Finds the
value of the
unknowns.
2.
Calculates
the area of
the
rectangle.
3. Finds its
perimeter.
The learner
explains the
meaning of
words such
as length,
width,
perimeter and
area.
Example
1. ABCD is a
rectangle.
Use it to
answer the
questions
that follow
1)Find the
value of x
2) Find the
actual length
and width of
the rectangle.
3) Find its
area and
perimeter.
Guided
discovery
Problem
solving
Class
discussio
n
Assertiven
ess,
Problem
solving
and
audibility
Attemptin
g the trial
numbers
given by
the
teacher.
Doing the
evaluation
exercise
Chalkb
oard
illustra
tion
Mk
mtcs
book
6
page
334
2
2
LENGT
H,
Area of
shaded
parts of
rectangles
The learner
1.Finds the
length and
width of the
rectangles
The learner
explains the
meaning of
words such
as length,
Example
1.Use the
figure below
to answer the
questions
Brainstor
ming
Class
discussio
Appreciati
on of
oneself
and
others, Answering
3
Tel:0775787978/0742845900 osebEdu@gmail.com ##2023 PLE 🎯
10cm
&
3
MASS
AND
CAPACI
TY
2.
Calculates
the area of
the shaded
rectangles.
width,
perimeter and
area.
that follow
a) Find the
length and
width of the
outer
rectangle.
b) Calculate
the area of
the shaded
part.
n
Problem
solving
Problem
solving
and
assertiven
ess
the oral
questions
Doing the
evaluation
exercise
Chalkb
oard
illustra
tion
Mk
mtcs
bk 6
page
336
Func
tional
mtcs
book
6
page
4
$
5
M
E
A
S
U
R
E
M
E
N
T
Finding the
unknowns
by
comparing
areas of
triangles.
The learner
1. Finds the
base of the
triangle.
2. Finds the
height of
the triangle.
The learner
explains the
meaning of
words such
as bases,
height and
</passage>

<passage id="lchk_03f8b377dc464cf8a3543c4f833ea50d" source="MATH P.6 TERM III" part="1">
For more lesson notes, visit www.freshteacheruganda.com
PRIMARY SIX MATHEMATICS
TERM THREE
LENGTH, MASS AND CAPACITY
Conversion of units
1. Kilo metres to metres:
Example: I
Change 7km to metres
1 km = 1000m
7 km = 7 x 1000m
7 km = 7000
Example II
Find the number of metres in 4.7km
1 km = 1000m
4. 7km = 4.7 x 1000m
4.7km = 4700m
2. KiloMetres to centimeters.
Example: I
Convert 2 km to cm.
1 km = 100000cm
2 km = 2 x 100000m
2 km = 200000cm
Example II
Express 3/5 km as cm.
1 km = 100000cm
3/5 km = 3/5 x 100000cm
= 300000cm  5
= 60000cm
3. Metres to centimeters
For more lesson notes, visit www.freshteacheruganda.com
Example I:
Convert 4 m to cm.
1 m = 100 cm
4 m = 4 x 100cm
4 m = 400cm
Example II
Express 86m as cm
1m = 100cm
86m = 86 x 100cm
86m = 8600cm
4. Metres to km.
Example I
Write 42000m as km
1000m = 1km.
1m = 1 km
1000
42000m = 1 x 42000 km
1000
= 42km
5. Centimeters to metres
Example I
Write 6200cm as metres.
100cm = 1m
1cm = 1 m
100
6200cm = 1 x 6200 m
100
= 62 m\.
Example II
Change 530cm to m.
1cm = 1 m
100
530cm = 1 x 530 m
For more lesson notes, visit www.freshteacheruganda.com
100
= 5.3 m
6. Square metres to square centimeters
Example I
Write 4m 2 as cm 2
1m = 100cm
1m 2 = 100cm 2
1m 2 = 100cm x 100cm
1m 2 = 10000cm 2
4m 2 = 4 x 10000cm 2
4m 2 = 40000cm 2
Example II
How many sq cm are there in 20cm 2 ?
1m 2 = 10000cm 2
20m 2 = 20 x 10000cm 2
7. sq. kilometers to sq. metres
Example I
Express 5km 2 as m 2
1 km = 1000m
1km 2 = 1000m 2
1km 2 = 1000m x 1000m
1km 2 = 1000000m 2
5km 2 = 5 x 1000000m 2
5km 2 = 5000000m 2
For more lesson notes, visit www.freshteacheruganda.com
Sq. m to sq. km
Example I
Change 7200000m 2 to km 2
1000000m 2 = 1km 2
1m 2 = 1 km 2
1000000
7200000m 2 = 1 x 7200000km 2
1000000
= 7.2km 2
8. Sq cm to sq m
Example I
Change 190000cm 2 to m 2
10000cm 2 = 1m 2
1cm 2 = 1 m 2
10000
190000cm 2 = 1 x 190000m 2
10000
= 19m 2
PERIMETER OF RECTANGLES
Example:
Find the perimeter of the rectangle below
25 cm
50cm
P = L + W + L + W
P = 50cm + 25cm + 50cm + 25cm
P = 75cm + 75cm
P = 150cm
OR:
P = 2(L +W)
P = 2(50cm + 25cm
P = 2 X 75cm
P = 150cm.
PERIMETER OF SQUARES
Example:
For more lesson notes, visit www.freshteacheruganda.com
What is the perimeter of the figure below?
7mm
P = S +S +S + S
P = 7mm + 7mm + 7mm + 7mm
P = 28mm
OR:
P = 4 X Side
P = 4 X 7mm
P = 28mm
AREA OF RECTANGLES
Example:
Calculate the area of the figure below:
5cm
6cm
A = L X W
A = 6cm X 5cm
A = 30 cm 2
AREA OF SQUARES
Example:
What is the area of the figure below?
12 cm
A = S X S
A = 12cm X 12cm
A = 144 cm 2
NOTE: area is measured in square units.
APPLICATION OF PERIMETER OF RECTANGLES
Length = perimeter – width
For more lesson notes, visit www.freshteacheruganda.com
2
Width = perimeter – length
2
Example:
1. The perimeter of a rectangle is 18cm and its length is 5cm. Find its width.
Width = perimeter – length
2
Width = 18cm – 5cm
2
Width = 9cm – 5cm
Width = 4cm
APPLICATION OF PERIMETER OF SQUARES
Side = perimeter
4
Example:
Find the length of a square whose perimeter is 20 dm.
Length = perimeter
4
Length = 20dm
4
Length = 5dm
APPLICATION OF AREA OF RECTANGLES
Width = Area
Length
Length = Area
Width
Example:
The area of a rectangle is 20cm 2 and its length is 5cm. Find its width.
Width = Area
Length
Width = 20cm 2
5cm
Width = 4cm.
APPLICATION OF AREA OF SQUARES
Example:
The area of a square is 36cm 2 . Find its side.
For more lesson notes, visit www.freshteacheruganda.com
FINDING AREA WHEN GIVEN THE PERIMETER
Example:
</passage>

<passage id="lchk_969b90c21f504e58b1ac129ea32f0905" source="P.6 PRIMARY SIX MTC NOTES.docx TEACHER.AC" part="31">
TOPIC LENGTH, MASS AND CAPACITY
LESSON 1
Subtopic: Length
Content: Measuring
Example: Learners will participate in measuring and recording
length of different objects
i.e Book (length)
book (width)
book (thickness)
Geometry set (length, width, thickness)
pencil (length)
door (length, width )
window (length, width)
table (length, width, thickness)
Activity
Teacher will organize different objects to be measured by the
pupils.
Old Mk 313-315
Remarks:
_____________________________________________________________________
LESSON 2
Subtopic: Length
Content: Changing from small to large units
- metres to kilometres
- centimetres to metres
Examples: Change 2500 metres to kilometres
1000m = 1 km
1 m = 1 km
1000
2500m = 1 x 2500 km
1000
= 25 km
66
10
= 2.5 km
(ii) Change 300 cm to m
100 cm = 1 metre (m)
1 cm = 1 metre
100
300 cm = 1 x 300 m
100
= 3 m
Activity
Pupils will do exercise 13. 5 and 13.6 page 315 – 316 MK BK 6.
Old Mk 315-316
Remarks:
_____________________________________________________________________
LESSON 3
Subtopic: Length
Content: Perimeter of geometrical figures
Example: 1. Find the perimeter of the figure below
10 cm
5 cm 13 cm
15 cm
Perimeter is the total distance around the
figure.
 Perimeter = S 1 + S 2 + S 3 + S 4
= 15 cm + 5 cm + 10 cm + 13 cm
= 43 cm
(2) Find the perimeter
3 cm
2cm
X cm 5 cm
3cm
8 cm
Side X = 2 + 3
X = 5 cm
Perimeter = S 1 + S 2 + S 3 + S 4 + S 5 +
S 6
= 8cm + 3cm + 2 cm + 5 cm + 3cm +
5 cm
= 26 cm
Activity
Pupils will do exercise 13 : 12 and 13.13 page 320- 321 MK BK 6.
Old Mk 320
New MK 125
Remarks:
_____________________________________________________________________
LESSON 5
Subtopic: Area
Content: Area of shapes
Example: Find the area of a square whose side is 6cm
6cm
6 cm
Area = side x side
= 6cm x 6cm
= 36 cm 2
Find the area of a square whose side is pcm
pcm
p cm
Area = side x side
= pcm x p cm
= P 2 cm 2
Content : Find one side of the square.
Example: The area of a square is 64cm 2 . Find the length of
each side of the square.
Let one side be p cm
p cm
67
P cm
S x S = Area Factorise
P x P = 64 (2 64
P2 = 64 (2
32
P = (2 x 2) x (2 x 2) x (2 x 2) (2
16
P = 2 x 2 x 2 (2
8
P = 8 ( 2 4
Each length = 8 cm ( 2
2
1
Activity
Pupils will do exercise 13 :18 page 328 MK BK 6.
Pupils will do exercise 13 :19 page 329 MK BK 6
New MK 122-123.
Remarks:
_____________________________________________________________________
____________________________________________________________________
LESSON 6
Subtopic: Area
Content: Finding the side of a rectangle when area is
given
Example: The area of a rectangle is 56cm 2 . The length is 8cm.
find the width of the rectangle.
Area = 56cm 2 w
8cm
L x W = Area
8cm x w = 56cm 2
7
8cm x w = 56 cm 2
8cm 8 cm
1 1
W = 7 cm
Width = 7 cm
11. A rectangular piece of paper is 4800mm 2 . Its width is
60 mm. Find its length
60 mm Area = 4800mm 2
Length
Length x width = Area
L x W = Area
L x 60 mm = 4800mm 2
80
L x 600mm = 4800mm 2
60mm 1 60mm 1
L = 80 mm
_____________________________________________________________________
Content: Finding area when perimeter is given
Example: 2 The perimeter of the rectangle is 24 cm and the
width is 5cm
Find the (a) length of the rectangle
(b) Area of the rectangle Area
(a) 2 (L + W) = perimeter
2 (L + 5cm) = 24 cm
5cm
2L + 10 cm = 24 cm
2L + 10 – 10 = 24cm – 10cm 7cm
2L = 14 cm Area = L x
W
2L = 14 7 Area = 7cm x 5
cm
2 2 1 cm Area = 35
cm 2
L = 7 cm
Activity
Pupils will do exercise 13 :23 page 333 MK BK 6.
New MK pg123-125
68
Remarks:
</passage>

<passage id="lchk_60186bc8e4de4ba7ae2d61d47ca83692" source="P.6 MTC term 3" part="1">
For more schemes of work, visit www.uganda.madpath.com
PRIMARY SIX THIRD TERM MTC SCHEME OF WORK
ELO: The learner appreciates and recognizes the application of length, mass and capacity in daily life experiences.
W
K
P
D
THE
ME
TOP
IC
SUB
TOPIC
CONTENT COMPETENCES IND. OF
LIFESKILL
S &
VALUES
MTHDS/
TECHNI
QUES
ACTIVIT
Y
IMS REF R
E
M
1 1
&
2
ME
AS
UR
ES
M
E
A
S
U
R
E
S
Length Estimating, measuring and
recording length in centimeters
and millimeters
Conversion of units.
Example
Change 3km to metres.
1km = 1000m
3km = 3x1000m
= 3000m
LANGUAGE SUBJECT Observati
on
Appreciat
ion
Accuracy
Explanat
ion
Demons
tration
Estimati
ng
Measuri
ng
Recordi
ng
Real
object
s
Real
object
s
Chalk
board
illustra
tions
Mk maths
book 6 page
313-314
P.6
curriculum
page 175
and 176
The learner;
- describes
the term
length
- reads
statements
correctly.
The learner;
- measures the
lengths of
different objects.
- records length
of different
objects.
- relates units
- converts
kilometers to
metres & vice-
versa
3 Conversion of units.
Example
100cm = 1m
1cm = 1m
100
480cm = 1 x 480
100
= 48
The learner;
- reads
statements
correctly.
The learner;
- relates units
- converts
metres to
centimetres.
- converts
centimetres to
metres.
Interpreta
tion
Problem
solving
Illustrati
on
Converti
ng units
from
one unit
to
another
A
chart
showi
ng
metric
units.
Chalk
board
Mk maths
book 6 page
315-316
P.6
curriculum
page 175
and 176
For more schemes of work, visit www.uganda.madpath.com
10
= 4.8m
Critical
thinking
illustra
tion
4 Circle Parts of a circle
- relating diameter and radius.
- diameter is twice the radius.
Example
1. Find the radius of a circle
whose diameter is 14cm.
R = D
2
= 14cm
2 = 7cm
2. Calculate the diameter of a
circle whose radius is 3 ½ cm.
D = 2r
= 2xr
= 2x3 ½ cm
= 2 x 7
2 = 7cm
The learner;
- describes a
circle
- reads and
spells new
terms.
The learner;
- names the
parts of a circle.
- relates
diameter and
radius
- finds diameter
and radius
Logical
thinking
Critical
thinking
Interpreta
tion
Problem
solving
Demons
tration
Observa
tion
Explanat
ion
Discussi
on
Naming
parts of
a circle
Finding
radius
and
diameter
A
chart
showi
ng
parts
of a
circle
Findin
g
radius
and
diamet
er
Mk maths
book 6 page
327
P.6
curriculum
page 175
and 176
5 Finding pie ( 𝜋 ) using diameter
and circumference.
- get a circular object and
measure its circumference
- measure its diameter
- divide circumference by
diameter to get pie ( 𝜋 )
𝜋 = C
D
C = 𝜋 D
The learner;
- reads
statements
correctly.
The learner;
- describes
diameter and
circumference
- identifies the
symbol for pie
( )
- finds pie using
diameter and
circumference
Accuracy
Problem
solving
Demons
tration
Observa
tion
Finding
pie
Circul
ar
object
s
Chalk
board
illustra
tion
Mk primary
maths book
6 2000 page
326
P.6
curriculum
page 175
and 176
6 Calculating circumference of
a circle.
Formula used:
C = 𝜋 D or
The learner;
- reads and
interprets
The learner;
- finds
circumference
Interpreta
tion
Explanat
ion
Finding
circumfe
rence
Chalk
board
illustra
tion
Mk maths
book 6 page
328
For more schemes of work, visit www.uganda.madpath.com
2 𝜋 r
Examples
Find the circumference of a
circle whose:
1) radius is 7cm
C = 2 𝜋 r
= 2 x22x7
7
= 2 x 22 = 44cm
statements
correctly.
when given
diameter.
- finds
circumference
when given the
radius.
Critical
thinking
Observati
on
Guided
discover
y
Illustrati
on
P.6
curriculum
page 175
and 176
7 Area of
shape
Square:
- A square is a quadrilateral with
all its sides and angles equal.
</passage>

<passage id="lchk_64bdae1d5ef74fe9886afcba15030680" source="P 6 Primary SIX MTC Notes Docx (ecolebooks Com)" part="32">
(c) Where was Nduga after the first hour?
(d) Calculate Nduga’s average speed for the whole journey.
90
80
70
60
50
40
30
20
10
P
7am 8am 9am 10am
Answers
(b) At 7 am (c) 30 km away (d) A.V speed = 90km = 30km/ hr
3hr
Activity
Pupils will do exercise 2 Nos 1 – 5 on page 109 of Oxford Primary MTC pupils BK 6.
Remarks
_____________________________________________________________________
Distance
in Km
GET MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
GET MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM 65
P.6 MTC TERM III
TOPICAL BREAKDOWN FOR TERM III
Theme Topic Sub topic
Measurements Length, mass
and capacity
• Circumference
• Measuring the length of a
straight spring
• Relationship between diameter
and circumference ( ) pie of
circle.
• Finding circumference of a
circle
• Finding the radius and diameter
when given circumference.
• Area
• Finding area of;
- Triangles
- Rectangle
- Trapezium
- Parallelogram
- Circle
- Kite
• Volume
• Finding value of;
- Cube
- Cuboid
- Cylinder
- Triangular prism
• Capacity
• Litres, half litres and quarter
litres
• Calculating capacity in litres and
millilitres
Geometry Lines,
angles, and
geometrical
figures
• Parallel lines
- Construction of parallel lines
- Using a set square
- Construction of parallel lines
- Using a compass
• Perpendicular lines
- Constructing perpendicular
lines, perpendicular bisector
- Dropping a perpendicular line
from point
- Skew lines
• Angles
- Naming common arms and
adjacent angles, supplementary
angles , vertically opposite
angles, and complementary
angles.
- Construction of angles of 90 0 ,
60 0 and 120 0
- Bisecting angles
- Construction of angles of 30 0 ,
45 0 , 135 0 , 15 0 , and 75 0 etc
- Properties of triangles (types of
triangles)
- Pythagoras theorem
- Constructing a right angled
triangle
• Geometric figures
- Quadrilateral and their
properties
- Application of properties of
quadrilaterals
- Calculating angle of a rhombus
and parallelogram
- Construction of squares
- Construction of a regular
hexagon in a circle
- Construction of a pentagon
when given sides
GET MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
GET MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM 66
- Simple properties of prisms
- Nets of simple prisms
Numeracy Integers • Integers on a number line
• Addition of integers
• Subtraction of integers
• Writing mathematical
statements
• Addition and subtraction of
integers without using a number
line
• Application of integers
Algebra Algebra • Algebra (forming algebraic
equations)
• Collecting like terms
• Substitution
• Simple equations (solving
equations)
• By addition
• By subtraction
• By multiplication
• By division
• Equations involving brackets
• Forming and solving equations
formed from polygons.
GET MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
GET MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM 67
TOPIC LENGTH, MASS AND CAPACITY
LESSON 1
Subtopic: Length
Content: Measuring
Example: Learners will participate in measuring and recording length of
different objects
i.e Book (length)
book (width)
book (thickness)
Geometry set (length, width, thickness)
pencil (length)
door (length, width )
window (length, width)
table (length, width, thickness)
Activity
Teacher will organize different objects to be measured by the pupils.
Old Mk 313-315
Remarks:
_____________________________________________________________________
LESSON 2
Subtopic: Length
Content: Changing from small to large units
- metres to kilometres
- centimetres to metres
Examples: Change 2500 metres to kilometres
</passage>

<passage id="lchk_3c577bebbf324719882a98f517161905" source="P 6 Maths Thematic Schemeii&iii" part="3">
metres per
second
* average
speed.
- travel
graphs.
- Effective communication.
- Decision making, problem solving
- Critical thinking
- converts time
- Solves problems involving
time.
- applies formulae to find
time, speed & distance.
- Solving problems involving
speed.
-Interpretes a travel graph.
- reads distance speed &
time from travel graph.
- plots distance time graphs.
The learner:
reads
uses the
words
distance,
speed, time
in a
sentence
- changing
time
- reading
and writing
time
- converting
from 12 to
24 hr clock
viseverse
- applying
formulae
relating to
dist, time &
speed.
- reading
distance
time from
the graph.
Drawing
graphs.
-Wall clocks
-charts
graph books
-Chalkboard
-illustrations
Discussion
Chalkboar
d
Illustratio
n
Guilded
discovery
Mk bk 6 pg 222 – 241, Sulp. MTC pg 132 – 134, Math Aid std 8 pg
120 – 122, Pr. MTC pg 24 – 26.
END
7
P.6 MATHS SCHEME OF WORK TERM III
Week
Pd
Theme
Topic
Sub-
topic Competences Content Methods &
techniques
Life
skills
&
values
Suggested
activities
T/L aids
Rf
Rm
Subject Language
1 1
MEASUREMENTS
Length, Mass & Capacity
Circumference
The learners.
- Solves
problems
involving
circumference.
- Applies the
use of formulae
for
circumference
in real life
situation.
The learner:
- reads and
uses the
following
vocabularies
correctly:
circumference,
pi, diameter,
radius.
-Find circumference
when diameter is
given.
-Radius is given.
- Finding the
diameter when
circumference is
given.
- finding the radius
when circumference
is given.
Guided
Discovery
Discussion
Demonstration
Creative thinking
Effective communication
Problem solving
-Measuring the
length of a
straight string.
- Making a circle
with the same
string and
measuring the
circumference.
-Comparing the
length and
circumference.
-Text books
-Circular
objects
-Strings
-Threads
Area -Solves
problems
involving area
of different
figures.
- Applies the
use of formulae
for area in real
life situations.
-Reads and
uses area,
square units
correctly.
- Describes area
correctly.
-Constructs
English
sentences using
area.
-Area of triangles
i. Scalene
ii. Triangles
with
different
bases and
heights.
-Area of rectangle.
Area of borders.
-Area of
parallelogram
-Area of trapezium
-Area of rhombus
-Area of kite
-T.S.A of a cube &
cuboids.
Discussion
Guided
Discovery
-Practically
using a small
square to
calculate the
area of the
figure.
-Textbooks
-Boxes
-Squares
8
Volume
-Solves
problems
involving
volume.
-Applies the use
of formulae for
volume in real
life situations.
-reads and uses
correctly.
-Cubic units
-Describes
volume
correctly
-Constructs
English
sentences using
the word
volume.
-Volume of a cube.
-Volume of a cuboid.
-Finding height,
width or length when
volume is given.
-Volume of triangular
prism.
-Packing cubes and
cuboids in a big
container.
-Discussion
-Guided
-Discovery
-Measuring
-Comparing
numbers of
smaller
containers
packed in big
container.
Le
ngt
h,
Ma
ss
&
Ca
pa
cit
y
Capacity
-Solves
problems
involving
capacity.
-Applies the use
of formulae for
capacity in real
life situations.
-reads and uses
capacity, litres,
cubic units.
-Describes
capacity
correctly.
-Constructs
sentences using
capacity.
-Conversion of units
of capacity.
-Relate the units of
capacity to those of
volume.
-Finding capacity of
cubes & cuboids.
-Finding height,
length or width when
capacity is given.
-Application of
capacity.
-Guided discovery
-Discussion
-Demonstration
Creative thinking
Effective communication
Problem solving
-Using stand
-Using standard
</passage>

<passage id="lchk_1d5db782c68947d3a85abe365868153f" source="EOT P.6 MTC BY SMILE" part="1">
WHAT’S APP: +256779680288 1
SMILE EDUCATION CONSULTANCY BUSUNJU
P. 6 End of Term III Examination, 2023.
Mathematics.
Time allowed: 2 hours and 30 minutes
Name: _______________________________________________
SECTION A (40 marks)
1. Work out: 1 7 + 1 1
2. What is the place value of 4 in the
number 3 9 4 6 5?
3. Find the next number in the
sequence: 1, 3, 9, 27, _____
4. Divide: 3 ÷ 2
5 3
5. Work out the value of y: y + 4 =
2(mod 7)
6. A baby slept from 8:50 a.m. to
10:20 a.m., for how long did the
baby sleep?
7. Draw an angle of 55 0 in the space
provided below.
WHAT’S APP: +256779680288 2
8. Describe the relationship between
set A and set B.
9. By selling a shirt at sh. 16,500, a
trader makes a loss of sh. 3300.
How much money did the trader pay
for the shirt?
10. Work out the mean of: 3x , x + 4
and 2x + 5
11. Given that a = 4, b = 3 and c = ¯2;
evaluate ab - c
12. Convert 3.5Km to metres.
13. Find the maximum number of pupils
that can share 12 and 18 apples
without leaving a remainder in each
case.
14. Express 7 / 10 as a decimal.
15. At Down Town Forex Bureau, 1 US
dollar ($) = Ug. Sh. 3600. Martha
exchanged 250 dollars in Ug. Sh.,
How much did she get?
WHAT’S APP: +256779680288 3
16. Work out: 1011 two – 101 two
17. How many lines of folding symmetry
does the figure below have?
18. Subtract (3y – 8) from (5y – 6)
19. Given that set A = {1, 2 , 4, 5}
and set B = {3, 4, 6}.
Find n(A – B).
20. Calculate the area of triangle ABC
below.
Section B: (60 marks)
21. In a group of 53 pupils, 30 like Fanta (F), 28 like Mirinda (M), x like both Fanta and
Mirinda while 7 like neither of the two drinks.
(a) Complete the Venn diagram, below. (2 marks)
WHAT’S APP: +256779680288 4
(b) How many pupils like both types of drinks? (2 marks)
(c) How many pupils don’t like Mirinda? (2 marks)
22(a) Use distributive property to work out: (66 x 36) + (64 x 66) (2 marks)
(b) Given that 2 2x x 2 = 32, find the value of x. (3 marks)
23. Study and complete the table below. (5 marks)
ITEM QUANTITY UNIT COST TOTAL COST
Sugar 3Kg Sh. …………. Sh. 14400
Bread ……. loaves Sh.3200 per loaf Sh. 3200
Milk 2 ½ litres Sh. 800 per half litre Sh. ……
WHAT’S APP: +256779680288 5
Tea leaves 2 packets Sh. ….. per packet Sh. ……
Total Expenditure Sh. 24000
24(a) Simplify: 2 . 4 x 3 . 6 ( 3 mark)
1. 2 x 0.9
(b) 8 men can slash a field in 6 days. How many men can slash the same field in 4 days?
(2 marks)
25. Two bells are used in a school, one rings after every 30 minutes while another rings
after every 45 minutes. If the bells ring together at 8:00 a.m.:
(a) after how long will the bells next ring together? (2 marks)
(b) at what time will they next ring together? (3 marks)
WHAT’S APP: +256779680288 6
26(a) Find the size of the angle marked m . (3 marks)
(b) Given that 4x 0 and x + 30 0 are supplementary angles. Find the value of x. (3 marks)
27. A bus took 2 ¼ hrs to travel from town P to town R at an average speed of 96Km/hr.
(a) Calculate the distance between town P and town R. (2 marks)
(b). If a cyclist covered the same distance at a speed of 54Km/hr. How long did the cyclist
take to cover the same journey? (2 marks)
WHAT’S APP: +256779680288 7
28. The diagram below shows a cuboid. Use it to answer the questions that
follow.
(a) How many edges has the cuboid above? (1 mark)
(b) The area of the shaded face is 24cm 2 . Find the value of k . (2 marks)
(c) Calculate the volume of the cuboid. (2 marks)
</passage>

<passage id="lchk_96f26ff931f143f490a65df45ea0cb26" source="P.6 .MTC" part="2">
- 8 oranges at Sh. 4000 .
a) Work out his total expenditure . (4mks)
b) If the cashier gave him Sh.2,750 as remaining money, find
the total amount of money he had at first. (1mk)
30. Ssemwogerere is 3 years older than Amito. If their total age is
49 years.
a) How old is each of them? (5mks)
10
31. Study the figure below and answer the questions that follow.
11cm
9cm
4cm 8cm
a) Find the area of the outer rectangle. (2mks)
b) Find the area of the inner rectangle. (2mks)
c) Calculate the area of the shaded part . (1mk)
11
32. The pie chart shows how Esther spend her Sh.36,000 .
Rent
Food y
150 0 Fees
i) Find the value of y . (3mks)
ii) How much does she spend on fees? (2mks)
END
</passage>

<passage id="lchk_ebb2c5fc448f4d8ebafce088138dc1ab" source="P6 MID TERM III" part="2">
| | (b) Find the cost of a litre of cooking oil. (02 Marks) |

|
| | (c) Find the cost of 3 exercise books, = = litre of cooking oil and a 2 kg packet of
| wheat flour. (02 Marks)

24 | Study the triangle below and answer the questions that follow.

15cm
12c
b
(a) Find b. (ma marly?
(b) Workout the area of the triangle. (02 marks)

Te 2022. TEL: 0393 283600, (0752 999554, 0772 097028, 0704 924083

B Prime Edueational Consul ON cTHEMATICS mi ERM Ii EXAMINATIONS 2022.

ron ACADEMIC EXCELLENCE, ALWAYS USE THE PINE; SC ESCH open: Meiers HOLIDAY PACKAGES,


(5 A cylindrical container below was to be filled with water-
|

!

| 60cm |
| |
| 28cm |
=>) (03 Marks) |

(a) Find the volume of the container.( 1 = |

(b) Workout its capacity in litres. (02 Marks)

ely.

76 | Gladys, Paul and Allen shared sh.240000 in the ratio 4:6:5 respectiv
(03 Marks)

(a) How much did each get?

(b) How much less did Gladys get than Paul? ; (02 Marks)

=
27 | Acar took 3 hours to cover part of the j
journey at a speed |
another 2 hours at a speed of 80kam/hr. —_————
Calculate the average speed of the car for the whole journey. (04 Marks)


The table below shows marks obtained by pupils of Primary shi
| 50 | 70 | 40 | 80 |

_ a arene, ae Sea |

| TF ney| 2 | 3 4 r

= {i _| |

— |
| (ajJHow many pupils did the test?

|
7
(01 Mark) |

(b)Work out the median mark.

|
(02 Marks) |
|
\
(03 Marks) |

(c)Find their average mark.

"79. Musa borrowed sh.600,000 from a village Sacco at a simple interest rate of 10%

1
| per year for i; years.

(a) Workout the simple interest. (03Marks)

|
|
|
|
|

| (b)Find the total amount Musa paid back to the Sacco. (02 Marks)

/30 | Using a ruler, a sharp pencil and a pair of compasses only, construct a regular
hexagon in a circle of radius 4cm. (03 Marks)

eas .

aa


(02 Marks) |

TT ae oq ee rT hexa on.
(b) Find the perimeter of the gi |

—

5 be - (02 Marks)
(a) At/=

(b)Hadijah is 4 years younger than Hawa. Their total age is 30 years. How old
is Hadijah? (03 Marks) |

The pie-chart below shows how a parent divides some money amongst her
four children.

| (a)Find the value of d in degrees. (02 Marks)

|
|

| ‘
| (b)Find the total amount of mone
|

y they shared if Haula got sh.120,000,
(03marks)

CamScanner

~~J(b) Find the perimeter of the hexagon. (02 Marks)

4

31, | Solve. ;
| (a) K+7=13 (02 Marks)

(b)Hadijah is 4 years younger than Hawa. Their total age is 30 years. How old
is Hadijah? (03 Marks) |

i

(32 The pie-chart below shows how a parent divides some money amongst her
four children.

| | (a)Find the value of d in degrees. (02 Marks)

| (b)Find the total amount of money they shared if Haula got sh.120,000.
(03marks)

2022, TEL: 0393 263600, 0752 999:
TH , 554, 0772 097028, 0704 9240!
FOR ACADEMIC EXCELLENCE, SIME P.6 MATHEMATICS MID TERM ll EXAMINATIONS 2022. a al

CamScanner
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
