# Job ltsk_752fc841aedf4c62820ef15c4252632a-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 6 lesson(s) below of week 1 of the Mathematics scheme for Primary Four 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P4: one 40-minute lesson: 2–4 sections; about 12–24 points; meanings, examples and uses; 5–7 activities.

lessonId=lles_cb0af2b5b0aa467dbec66017f5d82c64: lesson 1, Monday, 1 period(s), 40 minutes.
  Unit: Algebra (theme: Algebra). Lesson: Using letters for numbers — Equations with and without letters.
  Objectives: Use letters to represent numbers of objects.

lessonId=lles_433c91cdf65045de81f9ee8609c699d9: lesson 2, Tuesday, 1 period(s), 40 minutes.
  Unit: Algebra (theme: Algebra). Lesson: Adding letters and writing in short — Adding letters.
  Objectives: Write repeated addition of the same letter in short form.

lessonId=lles_97cf3280620c4879b49c93ee2af57d37: lesson 3, Wednesday, 1 period(s), 40 minutes.
  Unit: Algebra (theme: Algebra). Lesson: Writing in short: exercises — Adding letters.
  Objectives: Complete the supplied writing-in-short exercises.
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points ('- ' points, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

lessonId=lles_a55e2fe0e437486f87b9fd4b6113781a: lesson 4, Thursday, 1 period(s), 40 minutes.
  Unit: Algebra (theme: Algebra). Lesson: Finding perimeter using letters — Perimeter using letters for numbers.
  Objectives: Find perimeter by adding side lengths expressed using letters.

lessonId=lles_3978fa35bf0f4d46a3efa7e540b9be58: lesson 5, Friday, 1 period(s), 40 minutes.
  Unit: Algebra (theme: Algebra). Lesson: Subtracting letters — Subtracting letters.
  Objectives: Subtract terms containing the same letter.

lessonId=lles_f32f8f0b8ab349bd8b522b4a03d7f268: lesson 6, Friday, 1 period(s), 40 minutes.
  Unit: Algebra (theme: Algebra). Lesson: Subtracting letters: exercises — Subtracting letters.
  Objectives: Simplify the supplied expressions involving subtraction of like terms.
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points ('- ' points, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

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
<passage id="lchk_4ae8b6ee7ff74590b4b6ee1bceec1041" source="P 4 MTC Schemes Term III" part="1">
79
SCHEME OF WORK FOR P.4 MATHEATICS TERM III
WK PD THEME SUB THEME CONTENT SUBJECT COMPETECIES LANGUAGE
COMPETENCIES
METHODS LIFE SKILL T/L AIDS T/L ACTS REF
A
L
G
E
B
R
A
Equations
with and
without
letters
 Revision (using
letters for
numbers)
 Adding letters
e.g. P+P = 2P
2k + 4k = 6k
 Finding
perimeter using
letters for
numbers.
 Subtracting
letters.
 Collecting like
terms involving
addition only .
 Substitution.
Equation of:
 Addition
 Subtraction
 Division e.g.
2x = 8, x÷2 = 4
 Forming
equations of
addition and
subtraction.
 Adds letters.
 Uses letters for
numbers.
 Finds perimeter
using letters for
numbers.
 Collects like
terms.
 Does
substitution.
 Solves given
equations.
 Forms
equations and
solve them.
 Reads and
creates
simple
equations
without
letters.
 Guided
discovery.
 Participatory
approach.
 Discussion.
 Brain
storming.
 Effective
communi
cation.
 Critical
thinking.
 Problem
solving.
 Books.
 Pens
 Text
books.
-Adding
-Subtract
-Forming
equations
MK
primar
y
pupils
bk 4
pg.
245-
260
80
M
E
A
S
U
R
E
S
Money  Recognition of
money.
 Coins
 Bank notes
 Change shs. to
cents and vice
versa.
 Subtracting of
money.
 Multiplication of
money.
 Direct
proportions.
 Buying and
selling shopping
bills.
 Division of
money.
 Profit and loss.
 Postage rates.
 Identifies coins
and notes.
 Buying and
selling.
 Calculates simple
profits and loss.
 Costs and
pricing.
 Describes
different
coins and
notes.
 Roles
playing
using
money in
English.
 Uses
examples
to
describe
meaning
of profit
and loss.
 Discussion.
 Explanation.
 Observation.
 Demonstrati
on
 Dramatization.
 Role playing.
 Effective
communicat
ion.
 Critical
thinking.
 Creativity.
 Coins.
 Bank notes.
 Classroom
shape
 Real
objects.
 Backs pens.
 Tins
 Envelopes
 Straws
 Bottles etc
Role
playing
using
money.
Role
playing the
and buyer
seller.
Describing
coins
notes.
Giving
examples
of profit
and loss.
Working
out
problems
involving
profits and
loss.
Time  Revision on time.
 Telling time.
 Changing hours
to minutes.
 Addition of time.
 Word problems.
 Subtraction of
time.
 Word problem
 Time in a.m. and
p.m.
 Uses different
types of clocks
to tell time.
 Converts
measures of
time.

 Tells time
in the
local
language
and
English.
 Gives
months of
the year in
English.
 Explanation.
 Discussion
 Question
and answer.
 observation.
 Demonstrati
on.
 Role playing.
 Effective
communicat
ion.
 Critical
thinking.
 Creative
thinking.
 Logical
thinking.
 Effective
communicat
ion.
 Wall clocks.
 Calendars.
 Timetable.
 Using real
or model
clock, the
learner
tells time.
 Making a
calendar
showing
what
month of
the year.
 Working
New
edition
MTC
MK
pupils
Bk 4
Pg. 161
185
 Changing days
to hours.
 Changing hours
to days.
 Changing weeks
months to
days.
timetable
in his /
her
exercise
book.
  Critical
thinking.
 out
problems
involving
time.
 Reading.
81
to days.
 Changing days
to weeks.
 Addition of
weeks and days
 Subtraction of
time in weeks
and days.
MEASU
REMEN
TS
Capacity  Half and quarter
litres.
 Addition of litres
as half litres.
 Addition of litres
and milliliters.
 Adds litres as half
litres and
milliliters.
 Expresses
capacity of
different
items
 Discussion.
 Explanation.
 Question
and answer.
 Critical
thinking.
 Effective
communicat
ion.
 Logical
reasoning.
 ½ litre
containers.
 1 litre
container.
 Packing
 Adding.
New
MK
MTC
MK Bk.
4 pg.
222 –
227.
Weight
and
</passage>

<passage id="lchk_1d2f5914dfc44d7993d25e1990a7f64b" source="Math P 4 Notes" part="26">
p + 20 0 + 30 0 = 180 0
p + 50 0 = 180 0
p + 50 0 – 50 0 = 180 0 – 50 0
p = 130 0
Activity
Find the missing angles.
a) b) c)
25 0 n r
85 0 z 80 0 30 0 50 0 70 0
d) e)
y 20 0 m
30 0 40 0
92
Contact: 0754895241/0783298434
Email: tekule@tekartlearning.com
Website: www.tekartlearning.com
TERM III
ALGEBRA
Writing in short
Examples
1. m + m + m
= 2m + m
= 3m
2. t + t + t + t + t
= 2t + 2t + t
= 4t + t
= 5t
3. g + g + g + 2g
(g +g) + (g + 2g)
= 2g + 3g
= 5g
Exercise
Write in short.
1. p + p = 2. l + l + l + l =
3. q + q + q + q = 4. m + m + m + m + m
5. d + d + d 6. w + w + w + w + w + w
7. e + e + e + e + e 8. h + h + h + h
9. y + y + y + y 10. 2y + y
11. z + z + z + z 12. a + a + a + a + a
Using letters for numbers
Examples
1. 2 balls + 2 balls
= 4 balls
2. 1 pen + 1 pen + 1 pen + pen
Let each pen be p.
1p + 1p + 1p + 1p
= 4p
= 4pens
3. 3 mangoes + 1 mango + 7 mangoes
Let m stand for mangoes
3m + 1 m + 7m
= 10 m
= 10 mangoes
93
Contact: 0754895241/0783298434
Email: tekule@tekartlearning.com
Website: www.tekartlearning.com
Activity
1. 2 bananas + 2 bananas
2. 4 cows + 10 cows
3. 2 dogs + 5 dogs
4. 9 cats + 5 cats
5. 5 eggs + 5 eggs
6. 12 pots + 8 pots
7. 15 frogs – 5 frogs
8. 1 tree + 2 trees + 1 tree + 6 trees
9. 22 houses – 12 houses
10. 12 ducks + 18 hens
Using letter to find perimeter of different figures
Examples
1. 2.
4b
9h 10h
3b
5h
P = s + s + s + s P = s + s + s
= 4b + 3b + 4b + 3b = 5h + 9h + 10h
= 7b + 7b = 14h + 10h
= 14b = 24h
3. Simplify: 5b + 4b 4. 3d + 4d + 3d
= 5b + 4b = 3d + 4d + 3d
= 9b = 10d
Activity
Find the perimeter of the following figures.
1. 2. 3.
2b 4h 6h 3p
3b 7h
Simplify the following.
4. 10y + 4y 5. 15m + 6m + m
6. 8k + 2k + 3k 7. 10z + 2z + z
8. 3x + 8x 9. m + 2m + m
94
Contact: 0754895241/0783298434
Email: tekule@tekartlearning.com
Website: www.tekartlearning.com
Collecting like terms
Examples
1. Collect like terms a + a + b + b
a + a + b + b
2a + 2b
2. 2a + 2b + a + b
2a + a + 2b + b
3a + 3b
3. x + y + x + 3y + x
x + x + x + y + 3y
3x + 4y
4. m + 3y + m + k
m + m + 3y + k
2m + 3y + k
Activity
1. 2a + 2a + 3b + 3b
2. b + a + b + a
3. 2y + y + y + x
4. 4k + 7h + 3h + 4k
5. 2k + 4m + k + 3d + m
6. b + c + b + d
7. x + 2y + y + 3x
8. 9c + 8c + 2p + p
9. 4z + 4m + z + 6m
10. f + t + f + 3t + f
11. 2x + y + x + y
12. 4z + 8y + 2z + 3x
13. 6p + 5t + 2t + 8t
14. 6x + 2y + 3x + 5y
95
Contact: 0754895241/0783298434
Email: tekule@tekartlearning.com
Website: www.tekartlearning.com
More about collecting like terms
Examples
1. Simplify: 5m – 3m 2. 4z – z + 3p – p
= 2m 3z + 2p
3. 9d + 4c – 3c 4. 5a + a – m
9d + c 6a – m
Activity
Simplify the following
a) 7k – 2k b) 4k – k + n
c) 8d – 4d d) 6x – 6y + y
e) 10p – p f) 12p – p + k
g) 6n – 5n h) 6a + a – m
i) 4f – 2f + k j) 2y + 3y – z
k) 8p + 2p – p l) 8t + 4x – 6t + x
Finding unknowns
- Solving equations with one unknown.
- An equation is an algebraic expression with an equal sign
between.
E.g: x + 3 = 5 is an equation and x is unknown.
Examples
X + 3 = 10 2. 4 + x = 15
X + 3 – 3 = 10 – 3 4 – 4 + x = 15 – 4
X = 10 – 3 x = 15 – 4
X = 7 x = 11
Activity
Solve the following equations
a) n + 6 = 13 b) k + 9 = 17
c) n + 8 = 12 d) m + 12 = 18
e) n + 4 = 9 f) d + 7 = 24
g) m + 5 = 10 h) 7 + k = 19
i) x + 7 = 19 j) 10 + x = 36
k) a + a = 16 l) 9 + m = 18
96
Contact: 0754895241/0783298434
Email: tekule@tekartlearning.com
Website: www.tekartlearning.com
Word problem
Examples
1. I think of a number, add 7 to it and the result is 10. What is
the number?
Let the number be y.
</passage>

<passage id="lchk_c3b4097a84614d11812f9f508ee4e7b5" source="P 4 Maths Notes Scheme, Notes" part="24">
Equation of:
 Addition
 Subtraction
 Division e.g.
2x = 8, x÷2 = 4
 Forming
equations of
addition and
subtraction.
 Adds letters.
 Uses letters for
numbers.
 Finds perimeter
using letters for
numbers.
 Collects like
terms.
 Does
substitution.
 Solves given
equations.
 Forms
equations and
solve them.
 Reads and
creates
simple
equations
without
letters.
 Guided
discovery.
 Participatory
approach.
 Discussion.
 Brain
storming.
 Effective
communi
cation.
 Critical
thinking.
 Problem
solving.
 Books.
 Pens
 Text
books.
-Adding
-Subtract
-Forming
equations
MK
primar
y
pupils
bk 4
pg.
245-
260
COMPILED BY TEACHER EPIDU PAUL TEL 0788281825/0761119585 82
©LESSON NOTES AND SCHEMES 2022
TOPICAL BREAKDOWN FOR P.4 MATHEMATICS TERM III 2019
THEME TOPIC SUB-TOPIC DURATION OUT COMES
MEASUREMENTS TIME  Days of the week
 Conversion of days to weeks and
vice versa.
 Month of the year.
 Converting years into months and
vice versa.
 Converting months to days
 Telling time
 Changing days to hours and vice
versa
 Changing hours to minutes and vice
versa.
 Finding duration.
2 week
(1-3)
 The learner is able
to apply the
knowledge of time in
real life situation.
Length
Mass
Capacity
 Measuring length (M and cm)
 Finding perimeter and area of a
square, rectangle and triangle.
 Measuring mass
 Converting mass (Kg to g and vice
versa)
 Measuring capacity.
 Litres to milli8litres
 Word problems involving capacity
4 weeks
(8 – 9)
(3 – 7)
 The learner is able
to recognize and use
standard instruments
and units for
measuring mass,
length and capacity
ALGEBRA Equations  Collecting like terms
 Finding the missing numbers in
(1)addition,(2)subtraction,
(3)multiplication and (4)division.
 Word problems on missing numbers.
 Substitution.
 Equations with addition
 Subtraction
 Multiplication
 Division
 Forming and solving equation.
2 weeks
(7 – 9)
 The learner is able
to solve
mathematical
problems and
puzzles using the
knowledge of
Algebra.
COMPILED BY TEACHER EPIDU PAUL TEL 0788281825/0761119585 83
©LESSON NOTES AND SCHEMES 2022
P.4 MATHEMATICS NOTESTERM III
LESSON 1
TOPIC : MONEY
SUBTOPIC : Recognition of money
Finding the value of small denominations
CONTENT :
Example: Peter had 2 notes of 1000/=. How much money was he having?
COINS BANK NOTES
50 /= 1000/=
100/= 2,000/=
200/= 5,000/=
500/= 10,000/=
1000/= 20,000/=
50,000/=
ACTIVITY : Exercise 8a page MK bk 4 page 148.
LESSON 2
TOPIC : MONEY (measurements)
SUBTOPIC : Addition of money
CONTENT : Example: A man had 4800/= and he was given sh. 1200 by his
friend. How much money did he have altogether?
Sh. 4800
+ Sh. 1200
Sh. 6000
A man had sh. 6000 altogether.
ACTIVITY: Exercise 8b page 149 MK 4
COMPILED BY TEACHER EPIDU PAUL TEL 0788281825/0761119585 84
©LESSON NOTES AND SCHEMES 2022
LESSON 3
TOPIC : MONEY (Measurements)
SUBTOPIC : Subtraction of money
CONTENT : Example: How much change will you get from a one thousand
shilling note if you spend sh. 350?
You had sh. 1000
You spent sh. 350
Sh. 650
ACTIVITY: Exercise 8c page 150 of MKbk4
LESSON 4
TOPIC : MONEY (Measurements)
SUBTOPIC : Multiplication of money
CONTENT : The cost of 1 loaf of bread is sh. 1800. Find the cost of 3 loaves.
Shs 1800
x 3
Sh. 5400
ACTIVITY: Exercise 8d page 151 of MKbk4
LESSON 5
TOPIC : MONEY (Measurements)
SUBTOPIC : Buying and selling (Shopping Bills) (Price list)
CONTENT : Example
Item Price in shillings
1 bar of soap 1000/=
1 kg of sugar 1800/=
1 kg of maize flour 1200/=
1 packet of salt 400/=
</passage>

<passage id="lchk_87cb86fc55d24d8389bd459fec5ac4d8" source="P 4 Primary Four MTC Scheme OF Work Teacher AC" part="10">
▪ ▪ Critical
thinking.
▪ out
problems
involving
time.
▪ Reading.
MEASU
REMEN
TS
Capacity • Half and quarter
litres.
• Addition of litres
as half litres.
• Addition of litres
and milliliters.
• Adds litres as half
litres and
milliliters.
• Expresses
capacity of
different
items
▪ Discussion.
▪ Explanation.
▪ Question
and answer.
▪ Critical
thinking.
▪ Effective
communicat
ion.
▪ Logical
reasoning.
▪ ½ litre
containers.
▪ 1 litre
container.
▪ Packing
▪ Adding.
New
MK
MTC
MK Bk.
4 pg.
222 –
227.
Weight
and
volume
(mass)
• Half and quarter
Kg.
• Changing Kg and
gm and vice
versa.
• Add and
subtract kg and
gm.
• Dozens, crates,
trays.
• Volume of cubes
and cuboids.
• Changes Kgms go
gms and vice
versa.
• Adds and
subtracts kgms
and gms.
• Expresses
weight and
volume of
different
items.
▪ Discussion.
▪ Explanation
▪ Question
and answer.
New
MK
MTC
pupils
Bk 4
Pg. 228
– 235
22
A
L
G
E
B
R
A
Equations
with and
without
letters
▪ Revision (using
letters for
numbers)
▪ Adding letters
e.g. P+P = 2P
2k + 4k = 6k
▪ Finding
perimeter using
letters for
numbers.
▪ Subtracting
letters.
▪ Collecting like
terms involving
addition only .
▪ Substitution.
Equation of:
▪ Addition
▪ Subtraction
▪ Division e.g.
2x = 8, x÷2 = 4
▪ Forming
equations of
addition and
subtraction.
▪ Adds letters.
▪ Uses letters for
numbers.
▪ Finds perimeter
using letters for
numbers.
▪ Collects like
terms.
▪ Does
substitution.
▪ Solves given
equations.
▪ Forms
equations and
solve them.
▪ Reads and
creates
simple
equations
without
letters.
▪ Guided
discovery.
▪ Participatory
approach.
▪ Discussion.
▪ Brain
storming.
▪ Effective
communi
cation.
▪ Critical
thinking.
▪ Problem
solving.
▪ Books.
▪ Pens
▪ Text
books.
-Adding
-Subtract
-Forming
equations
MK
primar
y
pupils
bk 4
pg.
245-
260
23
TOPICAL BREAKDOWN FOR P.4 MATHEMATICS TERM III 2016
THEME TOPIC SUB-TOPIC DURATION OUT COMES
MEASUREMENTS TIME • Days of the week
• Conversion of days to weeks and
vice versa.
• Month of the year.
• Converting years into months and
vice versa.
• Converting months to days
• Telling time
• Changing days to hours and vice
versa
• Changing hours to minutes and vice
versa.
• Finding duration.
2 week
(1-3)
• The learner is able
to apply the
knowledge of time in
real life situation.
Length
Mass
Capacity
• Measuring length (M and cm)
• Finding perimeter and area of a
square, rectangle and triangle.
• Measuring mass
• Converting mass (Kg to g and vice
versa)
• Measuring capacity.
• Litres to milli8litres
• Word problems involving capacity
4 weeks
(8 – 9)
(3 – 7)
• The learner is able
to recognize and use
standard instruments
and units for
measuring mass,
length and capacity
ALGEBRA Equations • Collecting like terms
• Finding the missing numbers in
(1)addition,(2)subtraction,
(3)multiplication and (4)division.
• Word problems on missing numbers.
• Substitution.
• Equations with addition
• Subtraction
• Multiplication
• Division
• Forming and solving equation.
2 weeks
(7 – 9)
• The learner is able
to solve
mathematical
problems and
puzzles using the
knowledge of
Algebra.
</passage>

<passage id="lchk_b7287a834b564c0d9633ee281421ed53" source="P 4 Primary Four MTC Scheme OF Work Teacher AC 1" part="10">
  Critical
thinking.
 out
problems
involving
time.
 Reading.
MEASU
REMEN
TS
Capacity  Half and quarter
litres.
 Addition of litres
as half litres.
 Addition of litres
and milliliters.
 Adds litres as half
litres and
milliliters.
 Expresses
capacity of
different
items
 Discussion.
 Explanation.
 Question
and answer.
 Critical
thinking.
 Effective
communicat
ion.
 Logical
reasoning.
 ½ litre
containers.
 1 litre
container.
 Packing
 Adding.
New
MK
MTC
MK Bk.
4 pg.
222 –
227.
Weight
and
volume
(mass)
 Half and quarter
Kg.
 Changing Kg and
gm and vice
versa.
 Add and
subtract kg and
gm.
 Dozens, crates,
trays.
 Volume of cubes
and cuboids.
 Changes Kgms go
gms and vice
versa.
 Adds and
subtracts kgms
and gms.
 Expresses
weight and
volume of
different
items.
 Discussion.
 Explanation
 Question
and answer.
New
MK
MTC
pupils
Bk 4
Pg. 228
– 235
22
A
L
G
E
B
R
A
Equations
with and
without
letters
 Revision (using
letters for
numbers)
 Adding letters
e.g. P+P = 2P
2k + 4k = 6k
 Finding
perimeter using
letters for
numbers.
 Subtracting
letters.
 Collecting like
terms involving
addition only .
 Substitution.
Equation of:
 Addition
 Subtraction
 Division e.g.
2x = 8, x÷2 = 4
 Forming
equations of
addition and
subtraction.
 Adds letters.
 Uses letters for
numbers.
 Finds perimeter
using letters for
numbers.
 Collects like
terms.
 Does
substitution.
 Solves given
equations.
 Forms
equations and
solve them.
 Reads and
creates
simple
equations
without
letters.
 Guided
discovery.
 Participatory
approach.
 Discussion.
 Brain
storming.
 Effective
communi
cation.
 Critical
thinking.
 Problem
solving.
 Books.
 Pens
 Text
books.
-Adding
-Subtract
-Forming
equations
MK
primar
y
pupils
bk 4
pg.
245-
260
23
TOPICAL BREAKDOWN FOR P.4 MATHEMATICS TERM III 2016
THEME TOPIC SUB-TOPIC DURATION OUT COMES
MEASUREMENTS TIME  Days of the week
 Conversion of days to weeks and
vice versa.
 Month of the year.
 Converting years into months and
vice versa.
 Converting months to days
 Telling time
 Changing days to hours and vice
versa
 Changing hours to minutes and vice
versa.
 Finding duration.
2 week
(1-3)
 The learner is able
to apply the
knowledge of time in
real life situation.
Length
Mass
Capacity
 Measuring length (M and cm)
 Finding perimeter and area of a
square, rectangle and triangle.
 Measuring mass
 Converting mass (Kg to g and vice
versa)
 Measuring capacity.
 Litres to milli8litres
 Word problems involving capacity
4 weeks
(8 – 9)
(3 – 7)
 The learner is able
to recognize and use
standard instruments
and units for
measuring mass,
length and capacity
ALGEBRA Equations  Collecting like terms
 Finding the missing numbers in
(1)addition,(2)subtraction,
(3)multiplication and (4)division.
 Word problems on missing numbers.
 Substitution.
 Equations with addition
 Subtraction
 Multiplication
 Division
 Forming and solving equation.
2 weeks
(7 – 9)
 The learner is able
to solve
mathematical
problems and
puzzles using the
knowledge of
Algebra.
</passage>

<passage id="lchk_4a558b3e2f454208955d3d35fc4fce0d" source="P 4 Maths Notes Scheme, Notes" part="29">
SUBTOPIC : addition of letters for numbers
CONTENT : example I
1. Add m + m + m + m 2. Simplify 2y + y + 3y
M+m+m+m = 3m 2y+3y + y = 6y
3. Find the perimeter of the figure
P = s+s+s
2p 4p = 3p+4p+2p
= 9p
3p
Activity  Exercise 16 Mk bk 4 pg 250
LESSON 2:
TOPIC : ALGEBRA
SUBTOPIC : Subtraction of letters for numbers
1. Workout 2. Simplify;
3m - m 7 y – 4y
3m – m = 2m 7y – 4y = 3y
Activity: Exercise 5k pg 252 Mk 4 old edition
COMPILED BY TEACHER EPIDU PAUL TEL 0788281825/0761119585 101
©LESSON NOTES AND SCHEMES 2022
LESSON 3:
TOPIC : ALGEBRA
SUBTOPIC : collecting like terms involving addition only
1. Collect like terms
a) 2k + 5m + k b) 7x +10 y + 2x + y
(2k+k) + 5m 7x + 2x + 10 y + y
3k + 5m 9x + 11y
Activity: exercise 16 j Mk bk 4 pg 257 old edition
LESSON 4
TOPIC : ALGEBRA
SUBTOPIC : Equations with and without letters
CONTENT : Solving equations involving addition.
Examples: (a) + 3 = 9 (b) P + 5 =
+ 3 – 3 = 9 – 3 P + 5 – 5 = 11 - 5
= 6 P = 6
ACTIVITY: Exercise 16c and 16d MK bk 4 pg. 246 and 247
LESSON 5
TOPIC : ALGEBRA
SUBTOPIC : Solving equations involving subtraction
CONTENT : Finding the value of the unknown
Examples: (a) - 4 = 6 (b) y - 7 = 21
- 4 + 4 = 6 + 4 y - 7 + 7 = 21 + 7
= 10 y = 28
ACTIVITY: Exercise 16e pg. 247
COMPILED BY TEACHER EPIDU PAUL TEL 0788281825/0761119585 102
©LESSON NOTES AND SCHEMES 2022
LESSON 6
TOPIC : ALGEBRA
SUBTOPIC : Adding letters for numbers
CONTENT : Example:
(a) m + m + m = 3m (b) x + x + x + x + x = 5x
ACTIVITY: Exercise 16f Mk Bk4 pg. 248
LESSON 7
TOPIC : ALGEBRA
SUBTOPIC : Collecting like terms
CONTENT : Example:
(a) 7x + 8x + x = 16x (b) 5c + 4c + 3c = 12c
ACTIVITY: Exercise 16h Mk Bk4 pg. 250
LESSON 8
TOPIC : ALGEBRA
SUBTOPIC : Finding perimeter using unknowns
CONTENT : Find the perimeter of this figure below:-
ACTIVITY: Exercise 16 MkBk 4 pg. 250
LESSON 9
TOPIC : ALGEBRA
SUBTOPIC : Collecting more like terms
CONTENT : Example:
(a) Collect like terms
= x + y + x + 3y + x
= x + x + x + y + 3y
= 3x + 4y
ACTIVITY: Exercise 16j Mk Bk4 pg. 251 and 252
2p
3p
4p
Perimeter = s + s + s
= 3p + 4p + 2p
Perimeter = 9p
(b) Collect like terms
= 8b + 2p + 12b + 3p
= (8b + 12b) + (2p + 3p)
= 20b + 5p
COMPILED BY TEACHER EPIDU PAUL TEL 0788281825/0761119585 103
©LESSON NOTES AND SCHEMES 2022
LESSON 10
TOPIC : ALGEBRA
SUBTOPIC : Collecting like terms (addition and Subtraction)
CONTENT : Example:
(a) Collect like terms
= 9d + 4c – 3c
= 9d + c
CTIVITY: Exercise 5k page 252
LESSON 11
TOPIC : ALGEBRA
SUBTOPIC : SUBSTITUTION
CONTENT : Example: (a) If P = 3 and m = 6, find the value of
(i) P + 4 = 3 + 4
= 7
ACTIVITY: Exercise 16m Mk pg. 253
LESSON12
TOPIC : ALGEBRA
SUBTOPIC : MORE SUBSTITUTION
CONTENT : Examples: If x = 3, y = 4 and z = 5, Find the value:
(a) = x + y + z
= 3 + 4 + 5
= 12
ACTIVITY: Exercise 16n Mkbk 4 pg. 253
LESSON 13
TOPIC : ALGEBRA
SUBTOPIC : Solving equations involving addition
CONTENT : Example:
ACTIVITY: Exercise 16d Mk bk4 page 247
(b) Collect like terms
= 6a + a - m
= 7a - m
(b) xyz
= x x y x z
= 3 x 4 x 5
= 60
(a) + 3 = 9
+ 3 – 3 = 9 – 3
= 6
(b) 4 + y = 10
4 – 4 + y = 10 - 4
y = 6
COMPILED BY TEACHER EPIDU PAUL TEL 0788281825/0761119585 104
©LESSON NOTES AND SCHEMES 2022
LESSON 14
TOPIC : ALGEBRA
SUBTOPIC : Solving equations involving subtraction
CONTENT : Example:
ACTIVITY: Exercise 16e Mk bk 4 page 247
LESSON 15
TOPIC : ALGEBRA
SUBTOPIC : Solving equations involving multiplication
CONTENT : Examples.
LESSON 16
TOPIC : ALGEBRA
SUBTOPIC : Solving equations involving division
</passage>

<passage id="lchk_19ae9eddea0f464f95a6cac4d7262973" source="P 4 Primary Four MTC Notes Teacher AC" part="16">
LESSON 43
TOPIC : LENGTH, MASS AND CAPACITY
SUBTOPIC : converting mililitres to litres
Express 4000ml to litres
1000 ml = 1 litre
4000ml = 4000
1000
= 4 litres activity: pg184 .new Mk bk 4
LESSON 44
TOPIC : LENGTH, MASS AND CAPACITY
SUBTOPIC : Changing kilograms to grams
CONTENT : Example
(a) Change 4 2
1 kg into grams
1kg = 1000g
4kg = 4000g 2
1
kg = 500g
4 2
1 kg = 4500g
ACTIVITY: Exercise 14c page 230 of Mk bk 4
LESSON 45
TOPIC : LENGTH, MASS AND CAPACITY
SUBTOPIC : Changing grams to kilograms
CONTENT : Example
(a) Change 2000g into kg
1000g = 1kg
2000g = g
g
1000
2000 x 1kg
= 2kg
(b) Change 5
4 kg into grams
1kg = 1000g 5
4
kg = 5
4 x 1000g
= 800g
200
(b) Change 4500g into kg.
1000g = 1kg
4500g = 1000
4500 = 10
45
= 4.5kg or 4 2
1 kg.
73
ACTIVITY: Exercise 14d pages 230 and 231 of MK bk 4
LESSON 46
TOPIC : LENGTH, MASS AND CAPACITY
SUBTOPIC : Addition of kilograms and grams
CONTENT : Example
Add: Kg g
2 250
+ 3 150
5kg 400g
ACTIVITY: Exercise 14e page 231
LESSON 47
TOPIC : LENGTH, MASS AND CAPACITY
SUBTOPIC : Addition of kilograms and grams in word problems
CONTENT : Examples
Trevor’s father weighs 53kg 550g and his mother weighs 46kg 850g. Find their total
weight.
Kg g
53 550
+ 46 850
100 400
============
ACTIVITY: Exercise 14g page 232
LESSON 48
TOPIC : LENGTH, MASS AND CAPACITY
SUBTOPIC : Subtraction of kilograms and grams
CONTENT : Examples
Subtract : Kg g
75 640
- 28 450
47 190
ACTIVITY : Exercise 14h page 234
Example II
Add: 104kg 420g + 187kg 350
Kg g
104 420
+187 350
291 770
Subtract 59kg 423g – 39kg 651
Kg g
59 423
- 39 651
19 772
74
LESSON 49
TOPIC : LENGTH, MASS AND CAPACITY
SUBTOPIC : Subtraction of kilograms and grams in word problems.
CONTENT : Example
Babirye had 40kg 350g of ghee. She sold 26kg 850 of it. How much ghee did she
remain with?
Kg g
She had 40 350
She sold - 26 850
She remained with 13 500
ACTIVITY: Exercise 141 page 234 MK bk 4
LESSON 1
TOPIC : ALGEBRA
SUBTOPIC : addition of letters for numbers
CONTENT : example I
1. Add m + m + m + m 2. Simplify 2y + y + 3y
M+m+m+m = 3m 2y+3y + y = 6y
3. Find the perimeter of the figure
P = s+s+s
2p 4p = 3p+4p+2p
= 9p
3p
Activity  Exercise 16 Mk bk 4 pg 250
LESSON 2:
TOPIC : ALGEBRA
SUBTOPIC : Subtraction of letters for numbers
1. Workout 2. Simplify;
3m - m 7 y – 4y
3m – m = 2m 7y – 4y = 3y
Activity: Exercise 5k pg 252 Mk 4 old edition
75
LESSON 3:
TOPIC : ALGEBRA
SUBTOPIC : collecting like terms involving addition only
1. Collect like terms
a) 2k + 5m + k b) 7x +10 y + 2x + y
(2k+k) + 5m 7x + 2x + 10 y + y
3k + 5m 9x + 11y
Activity: exercise 16 j Mk bk 4 pg 257 old edition
LESSON 4
TOPIC : ALGEBRA
SUBTOPIC : Equations with and without letters
CONTENT : Solving equations involving addition.
Examples: (a) + 3 = 9 (b) P + 5 =
+ 3 – 3 = 9 – 3 P + 5 – 5 = 11 - 5
= 6 P = 6
ACTIVITY: Exercise 16c and 16d MK bk 4 pg. 246 and 247
LESSON 5
TOPIC : ALGEBRA
SUBTOPIC : Solving equations involving subtraction
CONTENT : Finding the value of the unknown
Examples: (a) - 4 = 6 (b) y - 7 = 21
- 4 + 4 = 6 + 4 y - 7 + 7 = 21 + 7
= 10 y = 28
ACTIVITY: Exercise 16e pg. 247
76
LESSON 6
TOPIC : ALGEBRA
SUBTOPIC : Adding letters for numbers
CONTENT : Example:
(a) m + m + m = 3m (b) x + x + x + x + x = 5x
ACTIVITY: Exercise 16f Mk Bk4 pg. 248
LESSON 7
TOPIC : ALGEBRA
SUBTOPIC : Collecting like terms
CONTENT : Example:
(a) 7x + 8x + x = 16x (b) 5c + 4c + 3c = 12c
ACTIVITY: Exercise 16h Mk Bk4 pg. 250
LESSON 8
TOPIC : ALGEBRA
SUBTOPIC : Finding perimeter using unknowns
</passage>

<passage id="lchk_32ef90b007b846ae93829003b1e25503" source="Primary Four Mathematics Mid Term III Examination 2023" part="2">
| |
|
| (b) How many more marks did the pupil get in MTC than SCI? (02 marks) |
(c) Find the total marks scored by the pupils? (02 marks)

| 8
(23 Use “<", “>” or “=” to complete the statement. : |
z
(a) * hour > hour (02 marks)
| | (b) 14 days 2 weeks. (01 mark)
(c) L hour 60 minutes. (01 mark) R
|(d) 12 months 6 months. 02 marks)

© Prime Educational Consult 2023. TEL: 0393 283600, 0752 999554, 0772 097028, 0704 924083 Page [3
THE PRIME P.4 MATHEMATICS MID TERM III EXAMINATIONS 2023,
FOR ACADEMIC EXCELLENCE, ALWAYS USE THE PRIME; SCHEMING FRAMEWORKS, HOLIDAY PACKAGES, LEARNING GAMES,
LESSON COURSE BOOKS AND PUPILS’ WORKBOOKS,
Visit: aaupapnimne-Jeath com’ for Online Video lessons, Exercises’and Trial tests with Marking guides

CamScanner

FS 24 nT 1S a Magic square, study it and use it to answer questions about it. |

| 8 | 1
4 b

NENA

La 5
(a) Find the magic sum.

l(ija

(iii) ¢

(ii) b

(01 mark)

(01 mark each)

25 | Below is a rectangle.
P

12m
| (a) Find the value of p.

| (b) Find the value of m.

| (c) Find the area of the figure.

| | (d) Find the perimeter of the figure.

L

|
|

(01 mark)

(01 mark)

(02 marks) §

© Prime Educational Consult 2023, TEL; 0393 283600, 0752 999554, 0772 097028, 0704 924083

THE PIUAL P.4 MATHEMATICS MID TERIA Il EXAMINATIONS 2023,

FOR ACADEMIC EXCELLENCE, ALWAYS USE THE PRIME; SCHEMING FRAMEWORKS, HOLIDAY PACKAGES, LEARNING GAMES,

LESSON COURSE BOOKS AND PUPILS’ WORKBOOKS.,

Page | 4
PTO

isi“ www.prime-learn.com “for Online Video lessons, Exercises and Trial tests with Marking guides,

—«

CamScanner

Collin is 56kg and Shakoor is 24kg.
(a) Who is (i) heavet? : (01 marks each)

(ii) lighter?

(b) Find the total weight of the two boys. (02 marks)

Given the figure below.

(a) Find the nittBer of; : (01 mark each)
(i) faces (ii) edges __- (iii) vertices
| (b) Find the area of the shaded part. (02 marks)

28 | Study the shopping list below and use it to answer the questions that follow.

A ruler at sh 800

A book at sh 1500
A pen at sh 500
A set at sh 3000

(a) How much can one pay for a ruler and a pen? (02 marks)

(b) What is the most expensive item on the list? (02 marks)

© Prime Educational Consult 2023, TEL: 0393 283600, 0752 999554, 0772 097028, 0704 924083 Page |S
THE PRIME P.4 MATHEMATICS MID TERM Ill EXAMINATIONS 2023,
FOR ACADEMIC EXCELLENCE, ALWAYS USE THE PRIME; SCHEMING FRAMEWORKS, HOLIDAY PACKAGES, LEARNING GAMES,
LESSON COURSE BOOKS AND PUPILS’ WORKBOOKS,

% . Visit S www. prime-learn.com” for Online Video lessons, Exercises and Trial tests with Marking guides,

ICS} CamScanner

| (c) How much money did Peter pay if he bought all the items? (01 mark)

329 | Workout. (02 marks each)

(a) Hrs Mins ‘ (b) Weeks Days
| 8 28 5 3
| 2 15 -2 6
|
|
(c) How many minutes are contained in 3 hours? (02 marks)

| 30 | (a) Given; 3+3+3+3, represent the statement diagrammatically and write
| the answer. (02 marks)

| (b) Use repeated subtraction to work out 15 +5. (02 marks)

31 | The diagram belows shows the number of litres of milk produced on Moses’
farm during the month of March: ,

ff VG.

Mon Tue Wed Thur [ri Sat Sun
Days of the week
© Prime Educational Consult 2023, TEL: 0393 783600, 0757 999554 0 7
9 }, O75 4, 0772 097
THE PRIME P.4 MATHEMATICS MD TERM Ill EXAMINATIONS ne eae veel PTO

FOR ACADEMIC EXCELLENCE, ALWAYS USE THE PRIMES SCHEMING FRAMEWORKS, HOLIDAY PACKAGES, LEARNING GAMES,
. KS AND PUPILS’ WC s
sit Svvvew peime-learn.com’ for-Online-Video.1essotse Ese xe Seeieoey
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
