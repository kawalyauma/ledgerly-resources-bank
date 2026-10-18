# Job ltsk_d1851fb2bde8422cb6b810aca24117b3-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 6 lesson(s) below of week 1 of the Mathematics scheme for Primary Five 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P5: one 40-minute lesson: 3–5 sections; about 14–28 points (meaning, examples, reasons, problems and solutions as the passages give); 5–8 activities.

lessonId=lles_429f7e0871a646ec832561bdfd1b8e58: lesson 1, Monday, 1 period(s), 40 minutes.
  Unit: Money (theme: Measurements). Lesson: Simple rates — Simple rates.
  Objectives: Find the cost of several identical items.; Find the cost of one item from the cost of several items.

lessonId=lles_3b3c0eb1367046209f47cdc51dd05670: lesson 2, Tuesday, 1 period(s), 40 minutes.
  Unit: Money (theme: Measurements). Lesson: Simple rates exercises — Simple rates.
  Objectives: Solve the supplied simple rate problems involving buying and selling.
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points ('- ' points, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

lessonId=lles_a6d52ec7e18e4cff986542e5f0e8e72d: lesson 3, Wednesday, 1 period(s), 40 minutes.
  Unit: Money (theme: Measurements). Lesson: More about simple rates — More about simple rates.
  Objectives: Use the cost of a given quantity to find the cost of another quantity.

lessonId=lles_8db11c74887a46ef8da9de1161accaea: lesson 4, Thursday, 1 period(s), 40 minutes.
  Unit: Money (theme: Measurements). Lesson: More about simple rates exercises — More about simple rates.
  Objectives: Interpret and solve the supplied problems about the costs of different quantities.
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points ('- ' points, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

lessonId=lles_d331fa292d694abe8f5ed58a727cc865: lesson 5, Friday, 1 period(s), 40 minutes.
  Unit: Money (theme: Measurements). Lesson: Shopping bills and change — Shopping list.
  Objectives: Calculate the amount spent on each item and total expenditure.; Find change.

lessonId=lles_d9e392d2b78745c1a45e580f7c3dc8c9: lesson 6, Friday, 1 period(s), 40 minutes.
  Unit: Money (theme: Measurements). Lesson: Buying and selling exercises — Shopping list.
  Objectives: Work out total expenditure and change in the supplied buying and selling exercise.
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
<passage id="lchk_710d046489f04bcd9e0537b56df7729c" source="NCDC P5 Merged – Mathematics" part="33">
Maize flour | quantity = Total cost = | sh, 9,000
Unit cost | sh. 3,000 | =3

Chicken | unit cost = Total cost =sh. 30,000
Quantity | 2 | = sh. 15,000
(b) After all the above working, complete the table above.
Exercise
Study and complete the shopping bill below.
ITEM | QUANTITY | UNIT PRICE | AMOUNT
Bananas | 3 bunches | Sh. 10,000 each | ______________
Cassava Flour | 5 kg | ______________ | Sh. 5,000
Beans | ______kg | Sh. 3,000 per kg | Sh. 9,000
Irish Potatoes | 2 tins | Sh. 15,000 | _____________
TOTAL | sh. __________
Lesson 2: Buying and Selling using Ugandan money.
In this lesson, you will:
Find the cost of more than one item.
Work out total cost of items bought.
You will need:
An exercise book, a pen and a pencil.
Introduction:
In primary four you have learnt about shopping bills. A shopping bill helps you to know how
much money you have spent on an item and the total cost.
In this lesson, you are going to learn buying and selling using Uganda money.
Remember Uganda money consists of notes of sh.1, 000, sh, 2,000, sh.5, 000, sh.10, 000, sh.20,
000 and sh.50, 000. It also consists of coins of sh.100, sh.200, sh.500 and sh.1000.

MATHEMATICS | PRIMARY FIVE

Step 1:

Activity
In your exercise book prepare your shopping bill for the items your family bought on any
day this
Step 2 week.

Study the following example
Okello went to a shop and bought the items below:
2kg of sugar at sh. 3200 per kg
3kg of rice at sh. 4000 per kg
1 litre of cooking oil at sh. 3000 per litre.
a) How much money did Okello spend altogether?
ITEM | UNIT COST | TOTAL COST
2kg of sugar | sh. 3200 | 2 ×sh. 3200 = sh. 6,400
3kg of Rice | Sh. 4,000 | 3 × sh. 4,000 = sh. 12,000
1 litre of cooking oil | Sh. 3,000 | Sh. 3,000
Sh. 21,400

Example 2
Kataike had sh. 20,000 and bought items for sh.11, 400. How much money did she take back
home?
Sh. 20,000
Sh. 11,400
Sh. 8,600
The money which Kataike took back home is called change.
Exercise
Jalia went to a shop and bought the following items.
2 trays of eggs at sh. 10,000 each tray.
3 bars of soap at sh. 3,000 per bar.
1 kg of sugar at sh. 3,200 per kg.
A) How much money did Jalia spend altogether?
b) If she went with sh. 50,000, how much money did she take back home?

Lesson 3: Finding profit and loss
In this lesson, you will:
● Find profit when buying and selling price is given.
● Find loss when buying and selling price is given.
You will need:
A Pen, a pencil, an exercise book and a ruler.

SELF-STUDY LEARNING

Introduction:
Sometimes traders get a loss or a profit when they sell the items.
A profit is the money you get when the selling price is higher than the buying price.
A loss is the money you get when the buying price is higher than the selling price.
Learning Profit and loss helps you to manage your business properly when you grow up.
So you notice that when you buy an item at a lower price and sell it at a higher price, you get a
profit
Step 1:
Activity
a) Arafat buys sugar at sh. 2,800 and sells it at sh. 3,000.
b) Asia buys sugar for sh. 3,000 and sells it at sh. 2,500.
Who got a profit? (Give a reason)
Who made a loss?

Step 2
Study the example below.
A trader bought a pen for sh.1,000 and sold it at sh.1,500. Find his profit.
Cost price (buying price) is sh. 1,000
Selling price is sh. 1,500
Profit = selling price – cost price.
= sh. 1,500
- sh. 1,000
Sh 500
Therefore his profit was sh.500.
Example 2
Kalete bought a handkerchief for sh. 2,000 and later sold it at sh. 1,800. Find his loss.
</passage>

<passage id="lchk_310b141c67c0492a9e93e9528fc5afee" source="P 5 Maths Scheme OF Work Term III" part="1">
P.5 MATHEMATICS SCHEME TERM III
WK PD THEM
E
TOPI
C
SUB
TOPIC
COMPETENCES CONTENT METHOD ACTIVITY L/SKILLS REF T/L
AID
S
Subject Language
1 1
Measurements
Money
Simple rates
The learner
solves
practical
problems
related to
buying and
selling
The learner;
Reads,
pronounces, spells
and writes the
words such as;
Currency
Rates
Cents
Shillings correctly
Role plays buying
and selling
Examples
A book costs shs. 500. What is the cost of 3 similar books?
1 book costs sh. 500.
3 books cost sh. 500 x 3
Sh. 500
X 3
Sh. 1500
5 books cost sh. 2000. Find the cost of one book
5 books cost sh. 2000
400
1 book costs sh. 2000
5
Sh. 400
1 book costs sh. 400 answer
Guided
discovery
Question and
answer
Role play
Role playing
buying and
selling
Interpreting
the question
Fluency
Confidenc
e
Critical
thinking
Real
objects
like
coins
and
paper
notes ,
Books
Text
books
Pens
MK Primary Maths books page 238 and Essential Ug. Primary Maths book 5
page 140-141
2
Measurements
Money
More about simple rates
The learner
Interprets the
questions
given correctly
Solves
practical
problems
related to
buying and
selling
The learner;
Reads, spells,
pronounces and
writes words
correctly
Such as;
-cost
-sells
-rates
-bought
More about simple rates
Examples
The cost 6 cups is sh. 1200. Find the cost of 10 similar cups
6 cups – sh. 1200
1 cup – sh. 1200
6
2
10 cups – sh. 1200 x 10
6
1
Sh. 200 x 10
Sh. 2000
3 pencils cost sh. 450. How many penils can Abey buy with sh. 4500?
Guided
discovery
Question and
answer
Role play
Interpreting
the
questions
Solving
problems
related to
buying and
selling
Neatness
Fluency
Critical
thinking
MK book 5 page 239 EssentialUg. Primary MTC 5 page 141
3
Measurements
Money
Shopping list
The learner;
Interprets the
questions
given correctly
Works out the
amount for
each item
Finds the total
expenditure
correctly
The learner;
Reads, spells,
pronounces and
uses the words like
change, expense,
each, per amount
in the sentences
correctly
Shopping bills and change
Examples
A man had sh. 50,000, he bought 2kg of sugar at sh. 1200 per kilo, 3 bars of
soap at 4000 a bar. How much change did he have?
Sugar Soap Total
Sh.1200
X 2
Sh. 2400
Sh. 4000
X 3
12000
Sh. 12000
Sh. 2400
Sh. 14400
Change
Sh. 50000
-sh. 14400
Sh. 35600
Guided
discovery
Question and
answer
Interpreting
the
questions
Working out
the amount
for each
item and the
total
Accuracy
Neatness
Fluency
Articulatio
n of words
Patience
Balance
beam
Spring
balance
Weighin
g scale
Window
or
kitchen
scale
Mk pupils book 5 page 240 , MK pupils book 4 page 177 and
Fountain book 4 page 172
4
Measurements
Money
Completing the bill
The learner;
Interprets the
question
correctly
Draws the bill
tables correctly
Completes by
fill in the table
correctly
The learner;
Reads, spells,
pronounces and
writes the words
like quantity, unit,
cost, item correctly
Completing the tables
A mother gave the shopping list below to her child. Study it and complete
Item Quantity Unit Total
Blue band
Bread
Tea leaves
Sugar
½
3 loaves
1/4kg
4kg
Sh. 4600
Sh. 800
Sh. 6000
Sh. 1200
Sh. 2300
Sh. 2400
Sh. 1500
Sh. 4800
Total
Total
Q x U.C
2300
2
1 x 4600
Sh. 2300
Unit cost
T – Q
2400
3
= 800
Guided
discovery
Explanation
Question and
answer
Interpreting
the question
Drawing the
table
Working out
and filling
the table
Accuracy
Neatness
Fluency
Articulatio
n of words
Patience
Balance
beam
Spring
balance
Weighin
g scale
Window
or
kitchen
scale
EssentialUg. Primary Mathematics book 5 page 141
5
Measurements
Money
Profit
The learner;
Describes how
</passage>

<passage id="lchk_9cc062c74d864f4a9331182a56d862c4" source="P 5 Mtc Term 3" part="1">
For more schemes of work, visit www.uganda.madpath.com
P.5 MATHEMATICAL SCHEME OF WORK FOR TERM THREE
E.L.O: The learner is able to solve practical problems related to utilization of Ugandan currency in
everyday life.
The learner is able to use the number line to properly work out problems related to integers
The learner is able to solve mathematical problems and puzzles using the knowledge of algebra.
W
K
P
D
THEME TOPIC S/TO
PIC
CONTENT COMPETENCES LSKIL
LS
MET
HODS
L/AID
S
REF R
E
M
SUBJECT LANGUAG
E
1 1 Measure
ment
Money Buyin
g and
sellin
g
Examples
Kamwine went shopping
with 30,000/= and bought 2
tins of blue band at 3000
each.
4kg of rice at 2600/= per kg
3 loaves of bread at 3,300@
a) What was her total
expenditure?
Blue band Rice Bread
3000 2600 3300
X 2 x 4 x 3
6,000/= 10,400/= 9,900/=
10400
9,900
The learner
-explains
expenditure
-explains
change
-solves
given
problems
involving
buying and
selling
the learner
-gives
correct
sentences
involving
new words
Logical
thinki
ng
Interp
retatio
n
Proble
m
solving
Expla
nation
Guide
d
discus
sion
Price
tags
Shopp
ing
list 6
Mk
Pri
Mtc
Bk
5
pag
e
237
For more schemes of work, visit www.uganda.madpath.com
+ 6000
26,300/=
2 Simpl
e
rates
Examples
1. Find the cost of 8 books if
each costs 700/=.
1 book costs 700/=
8 books will costs 700/=
X 8
5600/=
2. 3 cakes cost 2400/= what
is the cost of one cake
3 cake cost 2400
1 cake will cost 2400÷3 =
800/=
interprets
given
problems
correctly
reads given
problems
correctly
Critical
thinki
ng
Interp
retatio
n
Interp
retatio
n
Proble
m
solving
Expos
ition
Guide
d
discov
ery
Questi
on
and
answe
r
Chalk
board
illustr
ation
Mk
Pri
Mtc
bk
5
Pg
238
3 Examples
5 books cost of 1,000/=.
Find the cost of 12 similar
books
5 books cost 1000/=
1 book will cost 1000
5
=200/=
12 book will cost 200
X 12
400
+ 200
2,400/=
-interprets
given
problems
-solves
given
problems
-reads
given
problems
correctly
Logical
thinki
ng
Interp
retatio
n
Proble
m
solving
Expla
nation
Guide
d
discov
ery
Chalk
board
illustr
ation
Mk
Pri
bk
5
pag
e
239
For more schemes of work, visit www.uganda.madpath.com
2. 10 mangoes cost 5000/=
what is the cost of 7
mangoes?
10 mangoes cost 5000/=
1 mango will cost 10
= 500/=
7 mangoes will cost 500
X 7
3,500/=
4 Shopp
ing
bills
and
chang
e
Example
A man had sh. 7000 and
bought the following
2½kg of sugar at 1200/= @
kg
3 bars of soap at 700/= per
bar
How much change did he
have
Sugar soap
2½ = 2 x 2 + 1 700 1800
2 x 3 +2100
2100 3900
3 x 600
=1800/=
Change
71000
- 3900
3100/=
-interprets
given
problems
correctly
-solves
given
problems
involving
bill tables
-completes
given bill
tables
correctly
-reads
given bills
correctly
Critical
thinki
ng
Interp
retatio
n
Proble
m
solving
Expos
ition
Questi
on
and
answe
r
Chalk
board
illustr
ation
Mk
Pri
Mtc
Bk5
pag
e
240
For more schemes of work, visit www.uganda.madpath.com
5 Compl
eting
bill
tables
Examples
S father gave a shopping bill
below to his children
Study it and complete it.
Item Q’ty U.C Total
b. band
bread
t leaves
sugar
½kg
3
loaves
¼kg
4kg
Sh.4000a
kg
Sh800per
Sh 4800
Sh1200
2000
2400
Sh.1200
Sh.4800
10400
b.band bread
½x4000 800 1200÷¼
=2000/= x 3 1200x¼
2400/= 4800/=
b)If he gave 20,000/= to the
children, what was their
change
20,000
-10400
9 600/=
-observes
the given
information
correctly
-solves
given
problems
involving
bill tables
-completes
given bill
tables
correctly
-reads
given bills
correctly
Analys
is
Critical
thinki
ng
Observ
ation
Proble
m
solving
Expos
ition
Guide
d
discov
ery
</passage>

<passage id="lchk_920ab54bd9f744038ae3f9b61fdcde05" source="P5 Mathematics Lesson Notes, Term 3" part="1">
1
P.5 MATHEMATICS LESSON NOTES TERM III
Topic : Money
Subtopic : Simple rate
Competences
Subject : The learner;
- Solves practical problems related to buying and
selling
Language : Reads, pronounces, spells and writes the words;
- Current, rate, cent, shillings, correct
Methods : Role playing, guided discovery
Content : A book cost sh.500. What is the cost of 3 similar books
1 book = sh. 500
3 books = sh. 500 x 3
3 books cost = sh. 1500
The cost of 5 books is 2,000/=. Find the cost of one book?
5 books = sh. 3,000/= 5 bks = sh. 2,000/=
1 book = sh.
1
400
5
2000 1bk = sh. 5
2000
= Sh. 400
Therefore, one book costs sh. 400.
Activity
1. Sarah bought 4 trays of eggs at sh. 80,000, what is the cost of one tray?
2. Amos bought 5kg of meat at sh. 7,000 per kilo. How much did he pay for
5kg?
3. 2 books cost sh. 24,000. What can 1 pay if one needs only a book?
4. Find the cost 12 coloured pencil if each pencil costs sh. 200.
5. 4 sweets cost sh. 2,000. What is the cost of the sweet?
6. 1 school bag costs sh. 35,000. What will be the cost of 1 orange?
7. A heap of 20 orange cost 1,000/=. Find the cost of 1 orange
8. 10 mangoes costs 5,000/=. What is the cost of 1 mangoes?
2
9. 10 mangoes cost 5,000/=. What is the cost of 1 mangoes?
10. 1 kg of sugar costs sh. 3200. Find the cost of 6kg.
11. A dozen of dresses costs sh. 144,000. What is the cost of one dress?
Topic : Money
Subtopic : More about simple rate
Competences
Subject : The learner;
- Interprets the given questions correctly, solves
practical questions related to buying and selling
Language : Reads, spells, pronounces the words correctly
- Cost, costs, equivalent
Methods : Guided discovery, question and answer
Content : The cost of 6 cups is sh. 1200. Find the cost of 10 similar
cups
6cups = sh . 1200
1 cup = sh . 6
1200
10 cups = sh .
1
200
6
10 1200 x
= sh . 200 x 10
= sh . 2000
3 pencils cost sh. 1500. How many pencils will Abel buy with sh. 4500
Sh. 1500 = 3 pencils
1 sh = sh. 1500
3 x sh. 4500 3
= (3 x 3) pencils
= 9 pencils
3 pencils = sh. 1500
1 pencil = sh.
1
500
3
1000
= sh. 500
Therefore = sh. 500
4500
= 5
45 9
= 9 pencils
3
Activity
1. The cost of 2 boxes is sh. 1000. What is the cost of 10 boxes?
2. 5 Mathematical sets cost sh. 5,000. What is the cost of 4 such sets?
3. 7 bars of soap cost sh. 49,000. What is the cost of 9 similar bars of soap?
4. 8 show tickets cost sh. 8000. Find how much will 12 such tickets buy?
5. A boy bought 12 pencils at sh. 2400. How was he to pay for 3 similar
pencils?
6. 4 boxes of chalk cost sh. 10,000. What is the cost of 11 similar boxes of
chalk?
7. 8 dresses cost sh. 64000. Find the cost of 10 similar dresses.
8. 3 pencils cost sh. 450. What is the cost of 10 pencils?
9. Sempa went to buy 7kg of sugar. How much will he pay if 6kg costs sh.
72,000?
Topic : Money
Subtopic : Shopping list
Competences
Subject : The learner;
- Interprets the question given correctly
- Works out the amount for each item
- Finds the total expenditure correctly
Language : Reads, spells, pronounces and uses the;
- Changes, expense, each, per amount in the
sentence correctly
Methods : Guided discovery, question and answer
Content : Working out the shopping lists
Examples
A man had sh. 50,000, he bought 2kg of sugar at sh. 1200 per kilo, 3 bars of
soap at 4,000 per bar. How much change did he have after buying?
Sugar
Sh. 1200
x 2
sh. 2400
Sugar
Sh. 4000
x 3
sh. 124000
Total
Sh. 12000
+ 2400
sh. 14400
Change
Sh. 50000
- Sh. 14400
sh. 35,600
A man had a change of sh. 35,600
</passage>

<passage id="lchk_37ef9a279a18476bad458e97a038ffd6" source="Primary 5 Mathematics Lesson Notes, Terms 1–3" part="15">
ma and vice versa.
 Calculating perimeter and area of
figures i.e. squares, triangles and
rectangles only.
 Perimeter of a square, triangle and
rectangle
 Conversion of mass; kg to grams and
vice versa.
 Solving mathematical problems
involving mass. (addition and
subtraction)
 Conversion of units in capacity.
 Solving problems in measurement of
capacity.
 Addition and subtraction of capacity.
2 ½
weeks
The learner is able to
recognize and use
standard instruments
and units for
measuring length,
mass and capacity.
Numeracy Integers  Drawing numberlines and identifying
positive and negative integers
 Arranging integers
 Comparing integers using symbols ≤,≥
 Addition and subtraction of integers
 Mathematical statements and
interpreting numberlines.
 Solving word problems involving
integers.
2 weeks The learner is able to
solve mathematical
problems and puzzles
using the knowledge
of integers.
Algebra  Forming algebraic expressions
 Collecting like terms
 Substitution
 Solving equations by (subtracting ,
adding)
 Word problems involving addition and
subtraction.
 Solving by dividing
 Solving by multiplying
 Word problems involving division and
multiplication
 Solving equations involving mixed
equations.
 Solving equations involving square
roots
2 weeks The learner is able to
solve mathematical
problems and puzzles
using the knowledge
of algebra.
DIVINE EDUCATION CENTRE:0784540287/0751565742 Page 68
 Application of algebra in (perimeter,
area and volume)
DIVINE EDUCATION CENTRE:0784540287/0751565742 Page 69
TOPIC: MONEY
Lesson 1
Sub topic: money
Content: denominations
Types of money
Coins, e.g. 50, 100, 200, 500
Notes e.g. 1000, 2000, 5000, 10000, 20000, 50000
Examples
Peter had 3notes of 1000/= each. How much money did he have?
1 note = 1000/=
3 notes = (3 x 1000)/=
3notes = 3000/=
NB: do also calculations on a number of coins and notes of different denominations
REF
Teacher‟s collections
Lesson 2
Sub topic: buying and selling
Content: using price list
Example
1 book costs 200/= what is the cost of 5 similar books?
1book = 200/=
5books = (5 x 200)/=
5books = 1000/=
Ref
New MK mathsbk 5 pg143
Old Mk pp 222
Lesson 3
Sub topic: buying and selling
Content: more simple rates
Examples
Find the cost of 12 similar books
5books cost 1000/=
1bk costs
1bk = 200/=
12bks costs (200 x 12)
12bks costs 2400/=
Ref
New MK pg 239
DIVINE EDUCATION CENTRE:0784540287/0751565742 Page 70
Old MK pg 222
Lesson 4
Sub topic: shopping bills and change
Content:
Examples
Kiyaga had 10,000/= he bought 2kg of sugar at shs.1600 per kg, 3bars of sopa at 1000/= each bar, ½ kg of
salt at 400/= @ kg
(a) How much did he spend altogether?
(b) How much did he spend altogether?
(c) What was his balance
10,000
- 6400
3600/=
Item Method Amount
2kg of sugar at 1600/= @ 2 x 1600/= 3200/=
3bars of soap at 1000/=@ 3 x 1000/= 3000/=
½ kg of salt at 400/=@ ½ x 400/= 200/=
Total 6400/=
Ref
New mkmaths bk5 pg145-146
Old MK pg 223
Lesson 5
Sub topic: completing bill tables
Content:
Examples
A father gave the shopping list below to his children
Item Quantity Unit cost Total
Blue band ½ kg Shs. 4600 each kg Shs.2300
Bread .......loaves Shs. 800 each loaf Shs.2400
Tea leaves ¼ kg Shs.........@kg Shs.1500
Sugar 4kg Shs.1800 @ kg Shs............
Total Shs.............
Complete the shopping bill
Show all the calculations and fill in later and add
Bread tea leaves sugar
800/= can buy 1 loaf ¼ kg cost 1500/= 1kg cost 1800/=
</passage>

<passage id="lchk_40e8aded33fd444b8d4413e55054ff4b" source="Primary 5 Mathematics Lesson Notes, Term III" part="1">
©https://azsolver.com
CALL/WHATSAPP: 0787416804 FOR MORE OF THE SAME
1
PRIMARY FIVE MATHEMATICS NOTES
TERM III
Topical breakdown
Theme Topic Sub-topic
Measurements Money • Recognition of money
• Simple rates
• Buying and selling (Shopping bill)
• Table
• Listing
• Find profits and losses
• Cost price and selling price
Length, • Conversion of length into cm/km to ma and vice
Mass, versa.
Capacity
• Calculating perimeter and area of figures i.e.
squares, triangles and rectangles only.
• Perimeter of a square, triangle and rectangle
• Conversion of mass; kg to grams and vice versa.
• Solving mathematical problems involving mass.
(addition and subtraction)
• Conversion of units in capacity.
• Solving problems in measurement of capacity.
• Addition and subtraction of capacity.
Numeracy Integers • Drawing number lines and identifying positive and
negative integers
• Arranging integers
• Comparing integers using symbols ≤, ≥
• Addition and subtraction of integers
• Mathematical statements and interpreting number lines.
• Solving word problems involving integers.
Algebra • Forming algebraic expressions
• Collecting like terms
• Substitution
• Solving equations by (subtracting, adding)
• Word problems involving addition and subtraction.
• Solving by dividing
• Solving by multiplying
• Word problems involving division and multiplication
• Solving equations involving mixed equations.
• Solving equations involving square roots
• Application of algebra in (perimeter, area and volume)
©https://azsolver.com
CALL/WHATSAPP: 0787416804 FOR MORE OF THE SAME
2
Week One
Theme: Measurements
Topic One: MONEY
Lesson 1
Sub Topic: Denominations of Money
Coins e.g. 50, 100, 200, 500 and 1000
Notes e.g. 1000, 2000, 5000, 10000, 20000, 50000
Example One
Peter had 3 notes of Sh. 1000 each. How much money did he have?
1 note = Sh. 1000
3 notes = Sh. (3 x 1000)
3 notes = Sh. 3000
Example Two
Alex had 5 coins of 500 Shillings in his wallet. Calculate the amount of money he had
altogether.
1 coin = 500 Shillings
5 coins = Sh. (5 x 500)
= Sh. 2500
©https://azsolver.com
CALL/WHATSAPP: 0787416804 FOR MORE OF THE SAME
3
Example Three
How many five hundred Shillings coins can be changed from a Ten Thousand Shillings
note?
Number of Sh. 500 = Sh. 10,000 ÷ Sh. 500
= 20 coins
Therefore, one would get 20 five hundred Shillings coins in exchange for Ten
Thousand Shillings.
NB: Do also calculations on a number of coins and notes of different denominations
Ref: Teacher’s collections
Lesson 2
Sub topic: Buying and Selling
Example One
a) 1 book costs Sh. 200 what is the cost of 5 similar books?
1 book = Sh. 200
5 books = Sh. (5 x
200)
5 books = Sh. 1000
Trial Numbers
a) Grace bought 1 kg of sugar at Sh. 4000 and 3 kgs of maize flour at Sh. 1200 each.
Calculate the amount of money She paid for all the items. b) Marion sold 2 sacks of beans at Sh. 120,000 each and 4 sacks of sweet potatoes at Sh.
65,000 each. How much money did She earn altogether? Ref
New MK Maths bk 5 Pg 143
©https://azsolver.com
CALL/WHATSAPP: 0787416804 FOR MORE OF THE SAME
4
Old Mk pp 222
Lesson 3
Sub Topic: Shopping Bills and Change
Example One
Kiyaga had 10,000/= he bought 2kg of sugar at Sh.s.1600 per kg, 3bars of soap at
1000/= each bar, ½ kg of salt at 400/= @ kg
(a) How much did he spend altogether?
(b) How much did he spend altogether?
(c) What was his balance?
10,000
- 6400
3600/=
Item Method Amount
2kg of sugar at 1600/= @ 2 x 1600/= 3200/=
3bars of soap at 1000/=@ 3 x 1000/= 3000/=
</passage>

<passage id="lchk_0385c6ae55944b4b93836eec4fd75808" source="P 5 Maths Scheme OF Work Term III" part="2">
profit is made
well.
Applies and
uses the
formula for
profits correctly
The learner;
Reads, spells,
pronounces the
words like profit,
gain, increase,
more, high and
increment correctly
Defines the term
profit using simple
language
Finding profit
Examples
Abdul bought a shirt at sh. 3000 and sold it at sh. 3200. What was his profit?
SP = sh. 3200
C.P = sh. 3000
Profit = S.P – C.P
Sh. 3200
Sh. 3000
Sh. 200
Profit = sh. 200
The marked price of a sofa set is sh. 450,000. If it was sold ast sh. 550,000,
how much was the profit?
Guided
discovery
Question and
answer
Explanation
Interpreting
the
questions
Applying
and using
the suitable
formulae for
profit
Confidenc
e
Appreciati
on
Love
Neatness
Care
Fluency
Text
books
Tomato
es
Sugarca
ne
Money
MK Pupils book 5 page 245, MK pupils book 4 page 143 and
Essential Ug. Primary MTC book 5 page 144
6
Measurements
Money
Profit selling price and buying price
The learner;
Interprets the
questions
correctly
States or
applies the
formulae
correctly
The learner;
Reads, pronounes,
spells the key
words like selling
price, buying price,
profit, gains, old/
new price correctly
Finding the selling price or buying price when profit is given
Profit = S.P – C.P
SP = P + C.P
C.P / B.F = SP = Profit
Annet bought a tin of orange at sh. 14000. He sold oranges and made a profit
of sh. 4000. At what price did he sel the oranges?
SP = CP + P
Sh. 14000 + sh. 4000
= sh. 18000
Guided
discovery
Explanation
Interpreting
the question
Stating the
formulae
Applying the
suitable
formulae for
working out
the number
Confidenc
e
Appreciati
on
Love
Neatness
Care
Fluency
Text
books
Tomato
es
Sugarca
ne
Money
New MK pupils book 5 149, MK pupils book 247 and
Essential U. Primary book 5 page 145
7
Measurements
Money
Loss
The learner;
Describes how
a loss is made
in the business
Interprets the
questions
correctly
Applies and
uses the
formulae for
loss correctly
The learner;
Reads, spells,
pronounces and
writes words like
loss, decrease,
depreciate, loss,
reduce and
discount correctly
Defines a loss
using simple
language
Role plays loss in
business
Loss It is when the cost price of an item is higher than its selling price
Hence, loss = C.P – S.P
Example
Jagwe bought a goat at sh. 120,000. He sold it to Deo at sh. 105,000. What
was his loss?
C.P = sh. 120,000
S.P = sh. 105,000
Sh. 120,000
Sh. 105,000
Jagwe made a loss of sh. 15,000
Guided
discovery
Role playing
Explanation
Role playing
a feel for a
loss in
business
Describing
how a loss
is made
Applying
and using of
formulae for
a loss
Critical
thinking
Patience
Fluency
Confidenc
e
Articulatio
n
Text
books
Money
notes
MK pupils books page 247 and Essential Ug.
Primary MTC book 5 page 145
2 1
Measurements
Money
Loss , C.P and S.P
The learner;
Interprets the
questions
correctly
States and
applies of uses
the formulae
correctly
The learner;
Reads, spells,
pronounces and
writes words in the
sentences correctly
Finding the cost price or selling price when one and loss are given
Loss = C.P – S.P
Cost Price = Losts + S.P
Selling price = Cost price - Lose
Examples
Kizito bought a ball at sh. 15,000, he sold it and made a loss of sh. 3000. What
was the selling price of the ball?
S.P = C.P – Loss
=sh. 15,000 – sh. 3,000
= sh. 12,000
Kizito sold the ball at sh. 12,000
Guided
discovery
Questions
and answer
technique
Interpreting
the question
Stating the
formulae
Solving
problem
that involve
loss, cost
price and
selling price
Text
books
Confidenc
e
Critical
thinking
Appreciati
on
Text
books
Money
</passage>

<passage id="lchk_a164765cea1f4e5d90d753d48350bfcd" source="P 5 Primary Five MTC Scheme OF Work Teacher AC" part="6">
Ordering
integers
Comparing
integers
Simple
word
problems
Defining
integers
Identifying
positive and
negative
integers
Representing
integers on a
numberline
Ordering
integers
Comparing
integers
Finding
inverse of
integers
Addition of
integers using
a number line
Subtraction of
integers using
a number line
Forming
mathematical
Draws
number
lines
Identifies
positive and
negative
integers
Arranges
integers
Compares
integers
using >,<
or =
Adds
integers
Subtracts
integers
Solves
simple word
problems
Pronounces
integers
Spells the
word
integers
Positive and
negative
Uses the
words
Greater than
Less than
Equal to
Reads word
problems
involving
integers
Demonstratio
n
Discussion
Explanation
Discovery
Problem
solving
Critical
thinking
Charts
showing
into
Adding and
subtracting
integers
Using
number
lines to
describe
negative
and positive
Writing
integers in
ascending
and
descending
order
Comparing
integers
using
symbols
Mk new
edition bk5
pg 95 – 114
Mk new
edition bk 6
pg 103 –
111
Functional
MTCbkpg
109 – 121
16
sentences
Addition of
integers
without a
number line
Subtraction of
integers
without a
number line
2 1
to
1
2
Algebra Collecting
like terms
Substitution
Forming
algebraic
expressions
Solving
equation
Forming
and solving
equations
Forming
algebraic
expression
Collecting like
terms
Substitution
Solving
equations by
Subtracting
Adding
Word
problems
involving
subtraction
and addition
Solving by
dividing
Solving by
multiplying
Word
problems
involving
division and
multiplication
Forms
algebraic
expressions
Collect like
terms
Solves
simple
equations\
Forms
algebraic
equations
Collects like
terms
Solves
simple
equations
Pronounces
substitution
Equations
Spells
Like terms
Uses
substitution
and equation
in sentences
Do Do Chalk board
illustrations
Forming
algebraic
expressions
Collecting
like terms
Solving
simple word
problems
Mk bk5 pg
271 – 283
3 1
to
1
0
Algebra Removing
brackets
Mixed
equations
Equations
involving
squares
Solving
equations
involving
squares
Solving
equations
involving
Solves
simple word
problems
Applying
algebraic in
volume,
area, and
Pronounces
Brackets
Equations
Squares
Spells
Brackets
Equations
Do Do Do Solving
simple and
problems
Oral and
written
exercises
Mk bk 5 pg
280 – 287
17
squares and
square roots
Application of
algebraic
Perimeter
Area
Volume
perimeter Squares
</passage>

<passage id="lchk_e2828c4247444179ba941def67468c4d" source="P 5 Mathematics Schemes Of Work Term III" part="2">
Like terms
Uses
substitution
and
equation in
sentences
Do Do Chalk
board
illustration
s
Forming
algebraic
expression
s
Collecting
like terms
Solving
simple
word
problems
Mk bk5 pg
271 – 283
3 1
to
1
0
Algebra Removing
brackets
Mixed
equations
Equations
involving
squares
Solving
equations
involving
squares
Solving
equations
involving
squares and
square roots
Solves
simple
word
problems
Applying
algebraic in
volume,
area, and
perimeter
Pronounces
Brackets
Equations
Squares
Spells
Brackets
Equations
Squares
Do Do Do Solving
simple and
problems
Oral and
written
exercises
Mk bk 5 pg
280 – 287
For more schemes of work, visit www.uganda.madpath.com
Application
of algebraic
Perimeter
Area
Volume
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
