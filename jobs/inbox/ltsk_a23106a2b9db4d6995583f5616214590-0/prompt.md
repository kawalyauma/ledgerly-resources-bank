# Job ltsk_a23106a2b9db4d6995583f5616214590-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for Mathematics, Primary Five 2026, Term 3.
The term has 10 teaching weeks and this subject has 6 periods per week. Every lesson is ONE 40-minute period, so keep each lesson small enough to teach in 40 minutes.
There are no weekly review lessons: the subject has a lot of content, so every period teaches or practises.
Give at most 59 teaching/practice lesson entries in teaching order (the last lesson of the term is the end of term assessment).
Each lesson has a kind: "teach" (new content) or "practice" (the same subtopic as the teaching lesson just before it: exercises, oral work, drawing, matching, filling in blanks, ALL taken from the passages).
When the material is thin (common in lower primary), follow each teaching lesson with a practice lesson. Split big subtopics over several teaching lessons.
Never pad with content the passages do not have: if they cannot fill the term, return fewer lessons and list what is missing in gaps. Ledgerly fills the remaining weeks with revision.
You are composing the SCHOOL'S OWN scheme. The passages below (the official NCDC curriculum and guides, plus schemes of work, lesson plans, notes and past papers from the school e-library) are reference material:
The school's SCHEMES OF WORK for this class and term ("P 5 Mathematics Schemes Of Work Term III", "P 5 Maths Scheme OF Work Term III", "P 5 Mtc Term 3", "P 5 Primary Five MTC Scheme OF Work Teacher AC") are the BASE: follow the topics, subtopics and week-by-week order they agree on. Every topic they list for this term MUST become a unit, in their order, and their subtopics become the lessons, with about the pacing they give. Cite their passages in sourcePassageIds of every lesson that follows them.
The NCDC documents (titles starting "NCDC") only FILL GAPS: a topic NCDC lists for this term that the schemes lack gets its own unit where it fits best. Never drop or rename a schemes-of-work topic to fit NCDC. NCDC lower-primary thematic curricula list every learning area side by side in table columns separated by " | ": take only the Mathematics column.
Combine them in this authority order: the school's schemes of work for topics, sequence and pacing; NCDC for anything they miss; the strongest detailed notes for accurate teaching depth; past papers for expected applications and activities.
Use this term's part of the material (Term 3) when the passages cover several terms.

NCDC topics for Primary Five 2026, Term 3 that must ALSO be covered. Each needs at least one unit whose title or theme names it; the school's schemes of work decide where it goes and how many lessons it gets:
  2. Length, Mass and Capacity
  3. Integers
  6. ALGEBRA
Do NOT write lesson content yet. Each unit and lesson must cite the passage ids it comes from in sourcePassageIds.

Reply shape:
{"title":string,"summary":string,"units":[{"title":string,"theme":string|null,"weekFrom":int|null,"weekTo":int|null,"competences":string|null,"sourcePassageIds":[string],"lessons":[{"title":string,"subtopic":string|null,"kind":"teach"|"practice","objectives":[string],"sourcePassageIds":[string]}]}],"gaps":[string]}

<passages>
<passage id="lchk_7253a847cae746818252ce85be05db5c" source="NCDC P5 Curriculum – Mathematics" part="1">
Mathematics

P5 Set One Syllabus, National Curriculum Development Centre | 91

Introduction
This mathematics syllabus has been divided into six themes and twelve topics.
The Themes are: Sets, Numeracy, Interpretation of Graphs and Data, Measurements, Geometry and Algebra.

The topics include:
Ǧ Set concepts | Ǧ Fractions. | Ǧ Length, Mass and Capacity
Ǧ Whole numbers | Ǧ Data handling | Ǧ Lines, Angles and Geometric figures.
Ǧ Operations on whole numbers | Ǧ Money | Ǧ Integers
Ǧ Patterns and sequences | Ǧ Time | Ǧ Algebra

The scope and sequence has been designed in such a way that the topics have been further broken down into manageable teachable
sub-topics. The material in this mathematics syllabus differs markedly from the traditional Mathematics in that it is more directly
concerned with application of mathematics in everyday life. A brief background has been made for each topic, which lays a firm
foundation for the concept to be developed.

Mathematics has been allocated six (6) lessons per week. Some of the exercises are supposed to be done outside the allocated time.
Encourage the learners to always do maths in their time.

Rationale
The constant use of the mathematical approach to situations and formation of important concepts are the main aims of this syllabus.
Often familiar facts are emphasized to illustrate a mathematical idea so that a concept can be firmly established before being used to
discover new facts.

Throughout the primary school, emphasis should be laid on recording, reporting and discussing investigations carried out.

Mental mathematics and its integration into other subjects must be encouraged. This will in turn make the learning of mathematics much
easier and interesting. Remember the learner may know much more than you expect him/her to know. Practical work will therefore play a
big role in consolidating what the learner already knows before new ideas are brought in.

A four step plan is one of the strategies a mathematics teacher and learner may use to solve a problem. Understanding the problem is
the first step to solving it.
92 | P5 Set One Syllabus, National Curriculum Development Centre

UNDERSTAND | • | Read and understand the problem.
• | Know what is given and what you have to find.
PLAN | • | Make a plan.
• | Choose a problem-solving strategy.
WORK | • | Carry out the plan.
• | Use the strategy and do any necessary calculations.
ANSWER | • | Check any calculations and answer the problem.
• | Interpret the answer if necessary.

This syllabus if well implemented will go a long way in providing a foundation to a dynamic society.

SCOPE AND SEQUENCE
THEME 1: SETS

TOPIC: | Set Concepts
In the previous classes, the learner was introduced to the concept of sets. This continues with the work on sets that has already been
covered. The task for the teacher is to help learners draw examples from everyday life related to sets. As you introduce them to Venn
diagrams and some notation in sets, they need enough practical work to master correct use of symbols and language used in set
concepts.

Learning Outcome
The learner is able to demonstrate the knowledge of sets to solve problems in real life situations.

Life Skills: Critical thinking, creative thinking, effective communication.

P5 Set One Syllabus, National Curriculum Development Centre | 93

   |  |  |  
 
The learner: | • | Names and | • Sets | • Forming and drawing the sets.
</passage>

<passage id="lchk_2c77b5a8c138449f816d2e9952b96d1e" source="NCDC P5 Curriculum – Mathematics" part="2">
• Forms sets. | describes the | - Equivalent | • Drawing Venn diagrams.
• Identifies the union | sets. | - Empty | • Identifying members of the union and
and intersection of | - Equal | intersection of sets on the Venn diagram.
• | Distinguishes
- Union of sets | • Drawing Venn diagrams and using them.
sets using Venn | equal sets from | - Intersection of sets
diagrams. | equivalent sets. | • Venn diagrams.

Teacher’s Notes
Ǧ Let the learners form different sets of objects of different colours, shapes and different numbers.
Ǧ The learners should pick two sets and compare the number of members of each set to find out whether the sets are equal or
equivalent.
Ǧ The learners should identify the common members of the sets being compared.
Ǧ Guide the learners to draw Venn diagrams.
Ǧ Introduce different shapes of Venn diagrams to the learners.

Assessment Competences
The learner is able to:
1. Form sets
2. Draw Venn diagrams to show union and intersection of sets.
3. Write down the union and intersection of sets from given sets.

94 | P5 Set One Syllabus, National Curriculum Development Centre

THEME 2: NUMERACY
TOPIC: 1 Whole Numbers

This topic provides the basis for learners to develop the attitude of determination to solve problems in real life by calculation. It is when
the learner can properly count, read and write whole numbers that he/she can eventually be introduced to operations on numbers. Let the
learner use examples of real objects, such as cows, goats, chairs, etc.

Learning Outcome
The learner is able to appreciate the need of counting in everyday life and work with whole numbers up to 999,999.

Life Skills
• | Critical thinking.
• | Problem-solving.
   |   |  |  
The learner: | • Names place values up | • Numbers | • Identifying place values
• Identifies place value of | to millions. | - Place value | up to 6 digits.
each digit in 6-digit | - Value up to 999,999. | • Working out values of digits.
numbers. | • Reads numbers in | - Natural numbers up to | • Rounding off whole
• Finds values of digits. | expanded form. | 999,999. | numbers.
• Expands six-digit | - Rounding off whole | • Reading and writes
numbers. | numbers to nearest | Roman numerals.
• Writes expanded
• Rounds off whole numbers to | 10,000. | • Converting Hindu –
numbers in words.
the nearest ten thousands. | - Roman numerals. | Arabic numerals to
• Reads and writes Roman
• Reads and writes Roman | Roman and vice versa.
numerals up to fifty in
numerals.
words.

Teacher’s Notes
• Let the learners make abaci. The abacus should be used in naming and identifying place values.
• Help the learners to round off the numbers using abacus. The meaning of placing a small Roman numeral on the left or right hand
side of the bigger Roman numeral should be emphasized to the learners.

P5 Set One Syllabus, National Curriculum Development Centre | 95

Assessment Competences
The learner is able to:
1. Name place values up to hundred thousand’s.
2. Read and writes whole numbers up to 999,999.

TOPIC: 2 | Operations on whole numbers
This topic should not be handled in isolation. The learner should be helped to realize that everyday they add something to another. For
instance they add sugar to tea, salt to soup, welcome other members to our families, etc.

Always relate these operations to real life and bring out other words that will consolidate the concepts further, for example increase,
decrease, reduce, more, less.
</passage>

<passage id="lchk_de1a0df7223f494daf6f02fbe485501f" source="NCDC P5 Curriculum – Mathematics" part="10">
112 | P5 Set One Syllabus, National Curriculum Development Centre
</passage>

<passage id="lchk_e5f54bebfb934f079a60d951024cd15a" source="P 5 Mathematics Schemes Of Work Term III" part="1">
For more schemes of work, visit www.uganda.madpath.com
P.5 mathematics Term 3
3 Measurement
s
Length,
Mass and
capacity
Units used to
measure
length
Estimating
length
Measuring
length of
objects
Conversion
of units e.g.
cm to mm
and vice
versa.
M to cm and
vice versa
Km to m and
vice versa
Converting
mm to cm
Cm to m
Km to m
And vice
versa
Constructin
g sentences
using mm,
cm, m, km
Guided
discovery
Discussion
Explanation
Logical
thinking
Effective
communicatio
n
Problem
solving
Ruler
Books
Stick
Metric
tables
Converting
cm to m
M to k and
vice versa
Mk new
edition pg 151
– 156
Functional
MTC bk5 pg
161
P.5 curri pg
94-95
4 1
to
2
Perimeter Perimeter of
figures
Calculates
perimeter
Reads and
interprets
Do Do Do Calculating
perimeter
For more schemes of work, visit www.uganda.madpath.com
Area Triangles,
rectangles,
squares,
pentagon,
hexagon
Combined
figures
Area of
figures
triangles,
rectangles,
squares,
combined
figures
Difference in
area
and area of
figures
perimeter
and area
and area of
figure
5 1
to
1
0
Volume
Total
surface
area
Capacity
Weight
(mass)
Volume
cuboid and
cubes
Application
of volume
Total surface
area of a
cuboid
Unity for
capacity
Litres to
ML/cm 3 and
vice versa
Describing
mass or
weight
Basic units of
mass
Solving
problem
involving
volume
and total
surface
area
Reads and
interprets
word
problem
involving
volume,
total surface
area,
capacity
and mass
Demonstratio
n
Discovery
Explanation
Do Boxes
Container
Cups
Jerry cans
etc
Working
out
problems
involving
volume
TSA
capacity
and mass
New mk bk5
pg 161 – 163
Understandin
g MTC bk5 pg
161
For more schemes of work, visit www.uganda.madpath.com
Kg to gm
and vice
versa
1 1
to
1
0
Integers Positive
and
negative
integers
Inverse of
integers
Operation
on integers
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
integers
using a
number line
Subtraction
of integers
using a
number line
Forming
mathematica
l sentences
Addition of
integers
without a
number line
Subtraction
of integers
Draws
number
lines
Identifies
positive
and
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
simple
word
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
Greater
than
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
and
positive
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
edition bk5 pg
95 – 114
Mk new
edition bk 6
pg 103 – 111
Functional
MTCbkpg 109
– 121
For more schemes of work, visit www.uganda.madpath.com
without a
number line
2 1
to
1
2
Algebra Collecting
like terms
Substitutio
n
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
Collecting
like terms
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
expression
s
Collect like
terms
Solves
simple
equations\
Forms
algebraic
equations
Collects
like terms
Solves
simple
equations
Pronounces
substitution
Equations
Spells
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

<passage id="lchk_36cc06e9deb2490aaa604fa1d52c8b9e" source="Primary 5 Mathematics Lesson Notes, Term III" part="22">
 Constructing rehabilitation centres for people with disabilities.
 Organising communal work to improve on sanitation.
 Organising public fumigation to kill vectors like mosquitoes, houseflies, tsetse flies, e.t.c
SUITABLE LIFESTYLES AND HEALTH PRACTICES
 All people should live in a way that reduces chances of catching diseases e.g.
 Eating a balanced diet.
 Getting enough rest and sleep for body and brains to get refreshed.
 Maintain good body posture to avoid deformations.
 Avoiding drug abuse to minimize health problems like diseases.
 Washing and ironing clothes and bedding to kill germs.
 Doing physical exercise daily to refresh our bodies, burn excess fats, strengthen our
body muscles, improve on the internal body organs, e.t.c. Visiting health workers early
in case of any problem.
 Caring for other people with disabilities or health problems / complications.
 Reporting health problems like diseases outbreak early.
Good health practices in schools
i. Health parades to promote personal hygiene in the school.
ii. Having a school health committee to:
 Organise fellow children to do communal work.
 Encouraging parents to take their children for Immunization.
 Inviting health workers to have talks on health matters with Children.
©https://azsolver.com
CALL/WHATSAPP: 0787416804 FOR MORE OF THE SAME
85
 Promoting gardening to impart good farming methods in earners, promote
good Nutrition and develop a positive attitude towards farming in learners among others.
Child to child programmes
Child to child programme is a programme where older children teach the younger ones
good health habits.
They perform which help activities children learn how to work together and help each
other on health matters.
Activities which are involved in child to child programme?
Older children teaching young children how to maintain personal hygiene e.g brushing
teeth.
Older children can play with young children.
Helping the disabled children in washing their clothes, cooking food, fetching water for
them, etc.
Teaching young children toilet habits.
Caring for other children who are sick.
TOPICAL QUESTIONS
1. Write P.H.C in full.
2. What is Primary Health Care?
3. Give any one principal of primary health care.
4. Which element of P.H.C promotes prevention of the six killer diseases.
5. Which activities can primary five pupils do to promote P.H.C
6. A part from the elements of P.H.C mentioned above give any other two elements of
P.H.C.
7. How can people in the community promote good sanitation?
8. Identify any roles of a family in promoting P.H.C.
9. Give any one suitable lifestyle that can promote good health in an individual.
10. Give any two roles of a school health committee.
11. Why is it very necessary to have the following in a home?
i. a latrine
ii. A rubbish pit
12. Give any one activity of a health club in a school.
</passage>

<passage id="lchk_71cfb189aaeb4efca7c5f99e3f692a4f" source="P5 Mathematics Revision Work – Set One (2020)" part="1">
1 | P a g e
NAMAGUNGA PRIMARY BOARDING SCHOOL
P.5 REVISION WORK – SET ONE
(MATHEMATICS; 2020)
Time allowed: 2 Hours 30 Minutes
Name:…………………………………………………………………………….
Signature:………………………………………Stream:……………………..
DO NOT OPEN THIS BOOKLET UNTIL YOU ARE TOLD TO DO SO
Read the following instructions carefully:
1. This paper has two Sections: A and B .
2. Section A has 20 questions (40
marks)
3. Section B has 12 questions (60
marks).
4. Answer ALL questions: All answers to
both Sections A and B must be
written in spaces provided in full
sentences.
5. All answers must be written using a
blue or black ballpoint pen or ink but
not pencil. All work done in pencil
except diagrams will NOT be marked.
6. Unnecessary alteration of work will
lead to loss of marks.
7. Any handwriting that cannot be easily read, may lead to loss
marks.
FOR EXAMINERS’ USE
ONLY
FOR EXAMINERS’ USE ONLY
QN. NO. MARK SIGN
1 - 5
6 - 10
11 - 15
16 - 20
21 - 22
23 - 24
25 - 26
28 - 30
31 - 32
TOTAL
2 | P a g e
SECTION A: (40 MARKS)
1) Multiply: 2 4 × 3
2) Write 2,020 in words.
3) Think of a number, add 14 to it and the sum is
21.What is the number?
4) Find the sum of the next two numbers in the
sequence,
1, 4 , 9 , 16 , ______, ________
5) Using symbols, describe the shaded part of the Venn
diagram below:
A B
______________________
6) Draw a line segment PQ = 4.5 cm.
3 | P a g e
7) Using a number line, multiply: 3 × 4.
8) Work out: - =
9) Andrew ran round a rectangular field twice. If it was
measuring 9 m long and 5 m wide. Calculate the total
distance he covered.
10) A trader sold a try of eggs at sh. 1,200 making a profit
of sh. 2,500. Find the cost price.
11) Add:
Hrs mins
7 30
+ 4 55
4 | P a g e
12) If represent 9 flowers. Draw pictures to represent
27 flowers.
13) A dice was rolled once. Find the probability that a
prime number appeared on top.
14) Find the number that has been prime factorized to get
2 3 × 3 × 5 2
15) Name the sold figure drawn below.
___________________
16) Write the expanded number below in Roman numerals:
(9 × 10 1 ) × (7 × 10 0 )
17) Express 5 as an improper fraction
5 | P a g e
18) The Ministry of Health gave out 3,535 masks to 5
hospital. How many masks did each hospital get?
19) Simplify: m + 2y + 2m + y
20) Convert 2 kg to grams
SECTION B: 60 MARKS
21) Given that D = {All even numbers less than 18}
E = {1 , 3 , 6 , 10 , 15 }
(a) List all the elements of set D.
(b) Represent the above pair of sets on the Venn
diagram below:
E D
(c) Find the number of proper subsets in the E.
6 | P a g e
22) Given the number 47,358;
(a) Expand the numeral in value form.
(b) Find the difference of the values of 7 and 5 in the
above numeral.
23) In a class of 105 pupils, of them are girls and the rest
are boys.
(a) Find the fraction of boys
(b) How many girls are in that class?
(c) How many more boys than girls are in that class?
7 | P a g e
24) Study the solid figure below and answer the questions
that follow:
5m
9m
12m
(a) Write the number of vertices on the above figure
(b) Find the area of the shaded face.
(c) Calculate the volume of the figure above.
25) Give that a = 4, b = a and c = 7. Find the values of the
following:
a) a + b + c b) c) 3b 2
8 | P a g e
26) Use the Venn diagram below to answer the questions
that follow:
PF M PF 60 (a) Find the value of:
(i) M
3 1 2 1
5 1 x
(ii) x
(b) Find the L.C.M of M and 60.
(c) Work out the GCF of M and 60
27) (a) Change 150 minutes to hours.
(b) An examination started at 8: 20 a.m. and ended at
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
