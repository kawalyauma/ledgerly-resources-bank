# Job ltsk_cc88775b0c8d416e93dae55a7d61d0ff-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for Mathematics, Primary Six 2026, Term 3.
The term has 10 teaching weeks and this subject has 6 periods per week. Every lesson is ONE 40-minute period, so keep each lesson small enough to teach in 40 minutes.
There are no weekly review lessons: the subject has a lot of content, so every period teaches or practises.
Give at most 59 teaching/practice lesson entries in teaching order (the last lesson of the term is the end of term assessment).
Each lesson has a kind: "teach" (new content) or "practice" (the same subtopic as the teaching lesson just before it: exercises, oral work, drawing, matching, filling in blanks, ALL taken from the passages).
When the material is thin (common in lower primary), follow each teaching lesson with a practice lesson. Split big subtopics over several teaching lessons.
Never pad with content the passages do not have: if they cannot fill the term, return fewer lessons and list what is missing in gaps. Ledgerly fills the remaining weeks with revision.
You are composing the SCHOOL'S OWN scheme. The passages below (the official NCDC curriculum and guides, plus schemes of work, lesson plans, notes and past papers from the school e-library) are reference material:
The school's SCHEMES OF WORK for this class and term ("P 6 Maths Thematic Schemeii&iii", "P.6 MATHEMATICS SCHEME TERM 3", "P.6 MTC term 3") are the BASE: follow the topics, subtopics and week-by-week order they agree on. Every topic they list for this term MUST become a unit, in their order, and their subtopics become the lessons, with about the pacing they give. Cite their passages in sourcePassageIds of every lesson that follows them.
The NCDC documents (titles starting "NCDC") only FILL GAPS: a topic NCDC lists for this term that the schemes lack gets its own unit where it fits best. Never drop or rename a schemes-of-work topic to fit NCDC. NCDC lower-primary thematic curricula list every learning area side by side in table columns separated by " | ": take only the Mathematics column.
Combine them in this authority order: the school's schemes of work for topics, sequence and pacing; NCDC for anything they miss; the strongest detailed notes for accurate teaching depth; past papers for expected applications and activities.
Use this term's part of the material (Term 3) when the passages cover several terms.

NCDC topics for Primary Six 2026, Term 3 that must ALSO be covered. Each needs at least one unit whose title or theme names it; the school's schemes of work decide where it goes and how many lessons it gets:
  1. Sets
  3. Length, Mass and Capacity
  5. Geometry
Do NOT write lesson content yet. Each unit and lesson must cite the passage ids it comes from in sourcePassageIds.

Reply shape:
{"title":string,"summary":string,"units":[{"title":string,"theme":string|null,"weekFrom":int|null,"weekTo":int|null,"competences":string|null,"sourcePassageIds":[string],"lessons":[{"title":string,"subtopic":string|null,"kind":"teach"|"practice","objectives":[string],"sourcePassageIds":[string]}]}],"gaps":[string]}

<passages>
<passage id="lchk_6017d2dc5f734f2a955fc21767ded797" source="NCDC P6 Set One Sept book – Mathematics" part="1">
Mathematics Syllabus

Introduction to the Primary Six Mathematics Syllabus

General Background
The new Primary Education Curriculum for Uganda emphasises
integrated production skills and an integrated approach in all disciplines.
Therefore, the Mathematics Syllabus has been designed in such a way that
will provide the learners with the means of developing logical thinking
and numerical skills which will be a powerful tool in their further study
and later work in exploring the environment.

In this P6 syllabus, you have the task of making Mathematics a reality in
life. Methods and approaches to learning experiences should be mostly
practical and based on the experience of the learners. Hence, teaching
methods to be emphasised are those that allow the learners to explore,
try different procedures and solve problems practically. In this way,
Mathematics should be concretised as much as possible so as to assist the
learners to visualise it properly.

The syllabus is arranged in six major themes and in each theme there
are various topics. The themes include Sets, Numeracy, Geometry,
Interpretation of Graphs and Data, Measurement and Algebra. There are
twelve (12) topics in this syllabus, namely:
• Sets
• Whole Numbers
• Operation on Whole Numbers
• Patterns and Sequence
• Fractions
• Integers
• Data Handling
• Money
• Distance, Time and Speed
• Length, Mass and Capacity
• Lines, Angles and Geometric Figures
• Algebra

National Curriculum Development Center

The above topics are taught in the three school year terms as follows:

Term I
• | Sets
• | Whole Numbers
• | Operation on Whole Numbers
• | Patterns and Sequence
Term II
• | Fractions
• | Data Handling
• | Money
• | Distance, Time and Speed
Term III
• Length, Mass and Capacity
• Lines, Angles and Geometric Figures
• Integers
• Algebra
Mathematics must be integrated with and related to other subjects. In order
to do so, you will need to seek opportunities for drawing mathematical
experiences out of wide range of a pupil’s activities. Very many curricular
areas and activities give rise to the need to use mathematical concepts,
principles or ideas. Measurement and symmetry arise frequently in
Art and Technology and many patterns have some geometrical basis.
Environmental Education and Social Studies use measurements of many
kinds and the study of maps introduces the concepts of direction, scale
and ratio. A great deal of measurement can arise in the course of cooking,
including cost calculations, in the study of Home Economics.

Rationale
The constant use of the mathematical approach to situations and the
formation of important concepts are the main aims of this syllabus. Often
familiar facts are emphasised to illustrate a mathematical idea so that
a concept can be firmly established before being used to discover new
facts.

Primary 6 Curriculum

Throughout the primary school, emphasis should be laid on recording,
reporting and discussing investigations carried out.

Mental mathematics and its integration into other subjects must be
encouraged. This will in turn make learning mathematics much easier
and interesting. Remember the learners may know much more than
you expect them to know. Practical work will therefore play a big role
in consolidating what the learners already know before new ideas are
brought in.

Assessment Guideline
Mathematics appears on the timetable every day. Mathematics has seven
lessons per week, this gives you a chance to assess the learners every day
</passage>

<passage id="lchk_c71bf2915fb740eaba8076169281688a" source="NCDC P6 Set One Sept book – Mathematics" part="2">
as you teach. Continuous assessment is very much encouraged. Pupils can
be assessed through observation as they do their exercises. They can also
be assessed through quizzes, assignments, tests/examinations and many
other ways. As you assess your learners according to the competences
laid down in the syllabus, the number of questions given in one exercise
should depend upon what you want to assess. Give enough numbers to
the learners for practice.

Assessing the learners can be done within or out of the classroom. Life
skills and values can also be assessed especially through observation.
Emphasis should be put on assessing the language competences. Give
a chance to learners to express themselves verbally or through written
work as you make corrections where necessary. Summative evaluation of
learners can be done at the end of the year. Assessing learners daily does
not necessarily mean assessing each learner in every lesson, but you can
assess a group of learners. What is needed in this method of assessment
is to make sure that each learner is assessed before the end of the topic.
You are encouraged to keep a record of assessment for each learner. This
will help you to organise remedial teaching for your learners.

General Methodology
Mathematics content/topics have been arranged in a spiral form and
when teaching, you should follow the order as arranged in the syllabus.
Some topics require knowledge learnt from the previous topics. Time to
be spent on each topic is indicated in the syllabus.

National Curriculum Development Center

Mathematics should be taught practically, using examples drawn from
the learners’ real life situation. The methods to be used are those which
encourage the learners’ active participation such as assignment, group
work, discussion, field work, projects and many others. Learners should
be allowed to do activities on their own with little assistance from you.
Your role is to guide the learners when they are doing the activities.

A four step plan is one of the strategies you and learners may use to solve
a problem. Understanding the problem is the first step to solving it.

• Read and understand the problem.
Understand | • Know what is given and what you have to
find.

• Make a plan.
Plan
• Choose a problem-solving strategy.

• Carry out the plan.
Work | • Use the strategy and do any necessary
calculations.
• Check any calculations and answer the
Answer | problem.
• Interpret the answer if necessary.

This syllabus if well implemented will go a long way in providing a
foundation to a dynamic society.

Term 1

Theme 1: Sets | 4 Periods

Topic 1: Set Concepts

Background
This is not a new topic since it has been explored in the previous classes.
However, at this level, learners will be introduced to some new concepts.
Real life experiences or examples should be used while handling this
topic. Practical work should be emphasised. The learners should be
given opportunities to get actively involved during lessons and should
be encouraged to apply the knowledge gained.

Learning Outcome
The learner demonstrates the knowledge of sets to solve problems in real
life situations.

Life Skills
• Creative thinking
• Critical thinking
• Problem-solving
• Effective communication
• Interpersonal relationship

Primary 6 Curriculum

Subject | Language | Suggested
Content
Competences | Competences | Activities
The learner; | The learner; | • Types of sets: | • Colleting
• forms: | • describes | items.
– equivalent sets
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

<passage id="lchk_ad50725e14a945a590b8fed2849875dd" source="Lesson Notes P6 Term III MTC VOL 2 (2021)" part="1">
LENGTH , MASS AND CAPACITY LENGTH , MASS AND CAPACITY LENGTH , MASS AND CAPACITY LENGTH , MASS AND CAPACITY LENGTH , MASS AND CAPACITY
)
The The The The The KEC KEC KEC KEC KEC PREMIER MATHEMATICS BOOK.
PRIMARY SIX (TERM III)
The The The The The KEC KEC KEC KEC KEC PREMIER MATHEMATICS BOOK
PRIMARY SIX (TERM III) VOLUME II
⇒ ⇒ ⇒ ⇒ ⇒ Perimeter is the distance around a given figure. Perimeter is the distance around a given figure. Perimeter is the distance around a given figure. Perimeter is the distance around a given figure. Perimeter is the distance around a given figure.
⇒ ⇒ ⇒ ⇒ ⇒ Perimeter is the length of the outline of a shape. Perimeter is the length of the outline of a shape. Perimeter is the length of the outline of a shape. Perimeter is the length of the outline of a shape. Perimeter is the length of the outline of a shape.
Therefore, perimeter of a parallelogram is the distance around it. Therefore, perimeter of a parallelogram is the distance around it. Therefore, perimeter of a parallelogram is the distance around it. Therefore, perimeter of a parallelogram is the distance around it. Therefore, perimeter of a parallelogram is the distance around it.
⇒ ⇒ ⇒ ⇒ ⇒ Perimeter of a parallelogram is got by adding all its sides. Perimeter of a parallelogram is got by adding all its sides. Perimeter of a parallelogram is got by adding all its sides. Perimeter of a parallelogram is got by adding all its sides. Perimeter of a parallelogram is got by adding all its sides.
     State the formula for finding the perimeter of a parallelogram State the formula for finding the perimeter of a parallelogram State the formula for finding the perimeter of a parallelogram State the formula for finding the perimeter of a parallelogram State the formula for finding the perimeter of a parallelogram
i.e i.e i.e i.e i.e P = l + b + l + b OR P = 2l + 2b OR P = 2(l + b) where
“P” is perimeter , “l” is the length , “b” is the base .....
     Substitute in correctly. Substitute in correctly. Substitute in correctly. Substitute in correctly. Substitute in correctly.
     Compute accurately and the product is the perimeter. Compute accurately and the product is the perimeter. Compute accurately and the product is the perimeter. Compute accurately and the product is the perimeter. Compute accurately and the product is the perimeter.
PERIMETER OF A PARALLELOGRAM PERIMETER OF A PARALLELOGRAM PERIMETER OF A PARALLELOGRAM PERIMETER OF A PARALLELOGRAM PERIMETER OF A PARALLELOGRAM
)
OR OR OR OR OR
procedure (steps taken) procedure (steps taken) procedure (steps taken) procedure (steps taken) procedure (steps taken)
EXAMPLE EXAMPLE EXAMPLE EXAMPLE EXAMPLE 1 11 1 1 ) Find the perimeter of the parallelogram below.
6cm
14cm
10cm p = l + b + l + b
p = 14cm + 10cm + 14cm + 10cm
p = 24cm + 24cm
p = 48cm
Approach I Approach I Approach I Approach I Approach I
24
+ 24
48
Approach III Approach III Approach III Approach III Approach III Approach II Approach II Approach II Approach II Approach II
p = 2l + 2b
p = (2 x 14cm) + (2 x 10cm)
p = 28cm + 20cm
p = 48cm
28
+ 20
48
p = 2 (l + b)
p = 2 (14cm + 10cm)
p = 2 (24cm)
p = 24cm
x 2
48cm p = 48cm
KAMPALA EDUCATION CONSULTANTS
TEL: 0758656565/ 0779656565/ 0703374083
/ 0708231210 PRIMARY SIX.
THE OBVIOUS TREND TO PASSING IN GRADE “A”
“ REAL ACADEMIC EXCELLENCE IN REAL PRIMARY
SCHOOLS” 2
PAGE
EXAMPLE EXAMPLE EXAMPLE EXAMPLE EXAMPLE 2 2 2 2 2 ) Approach I Approach I Approach I Approach I Approach I
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

<passage id="lchk_431a10a6115348558b9c964e10effa8c" source="P 6 MTC Notes Final 123kqk" part="53">
SUB TOPIC: Writing solution sets
Examples:
1. Write down the integers for the following inequalities.
(i)
(ii)
(iii)
2. Write the solution sets for the following
h
b
y
-3 0 1 2 3 4 5 6 -1 -2 -4
-3 0 1 2 3 4 5 6 -1 -2 -4
-3 0 1 2 3 4 5 6 -1 -2 -4
𝟎 𝟕 𝟕 𝟔 𝟗 𝟗 𝟎 𝟑 𝟐 𝟕 𝑷 . 𝟔 𝑴 T C 𝒂 𝒎 𝒐 𝒏 𝒂 𝒉 𝒆 𝒓 𝒆 𝒛 𝒂 𝟎 𝟐 @ 𝒈 𝒎 𝒂 𝒊 𝒍 . 𝒄 𝒐 𝒎 Page 213
SUB TOPIC: Solving in e qualities and writing their solution sets
Examples:
Solve the following and write the solution set
1.
2.
𝒎 𝟔 𝟕 𝟖 𝟗
3.
4.
When diving by a negative co-efficient ,
the sign changes at the step of division.
𝟎 𝟕 𝟕 𝟔 𝟗 𝟗 𝟎 𝟑 𝟐 𝟕 𝑷 . 𝟔 𝑴 T C 𝒂 𝒎 𝒐 𝒏 𝒂 𝒉 𝒆 𝒓 𝒆 𝒛 𝒂 𝟎 𝟐 @ 𝒈 𝒎 𝒂 𝒊 𝒍 . 𝒄 𝒐 𝒎 Page 214
Solve the following and write the solution sets
a)
b)
c)
d)
e)
f)
g)
SUB TOPIC: Compound inequalities(writing solution sets)
Examples
1. Write the solution set for
(a)
(b)
(c)
(d)
(e)
SUB TOPIC: Solving and writing solution sets with compound inequalities.
Examples
Solve the following and write the solution sets
1.
-3 0 1 2 3 4 5 6 -1 -2 -4
-3 0 1 2 3 4 5 6 -1 -2 -4
𝟎 𝟕 𝟕 𝟔 𝟗 𝟗 𝟎 𝟑 𝟐 𝟕 𝑷 . 𝟔 𝑴 T C 𝒂 𝒎 𝒐 𝒏 𝒂 𝒉 𝒆 𝒓 𝒆 𝒛 𝒂 𝟎 𝟐 @ 𝒈 𝒎 𝒂 𝒊 𝒍 . 𝒄 𝒐 𝒎 Page 215
2.
𝟐 𝒙
𝟐
𝟑
𝟑𝒙
𝟑
𝟐𝟒
𝟑
𝟒
𝒙 𝟓 𝟔 𝟕
3.
𝟑 𝟑𝒙 𝟐 𝟒
𝟑 𝟐 𝟑𝒙 𝟐 𝟐 𝟒 𝟐
𝟓 𝟑𝒙 𝟔
𝟓
𝟑
𝟑𝒙
𝟑
𝟔
𝟑
𝟓 𝒙 𝟐
𝒙 𝟐 𝟑 𝟒 𝟓
4.
5.
6.
TOPICAL WORK ON ALGEBRA
1.
2.
3. Solve for b in
4. If . Find the value of x.
5. Solve
6. What is the value of when b = 8, c = 3 and d = 6?
7. Solve:
8. Simplify:
9. Solve:
10. Solve:
11. Simplify:
12. Solve
𝟎 𝟕 𝟕 𝟔 𝟗 𝟗 𝟎 𝟑 𝟐 𝟕 𝑷 . 𝟔 𝑴 T C 𝒂 𝒎 𝒐 𝒏 𝒂 𝒉 𝒆 𝒓 𝒆 𝒛 𝒂 𝟎 𝟐 @ 𝒈 𝒎 𝒂 𝒊 𝒍 . 𝒄 𝒐 𝒎 Page 216
13. The area of the trapezium is 50cm 2 . Find the value of t.
14. Given that a = ½, b = and c = ¼ .Find the value of .
15. Subtract
16. Zahara‟s mother bought 8 books at shs each and 2 Mathematical sets at
each. She spent shs 5300 altogether. Find the amount of money spent on
books.
17. Tom has three daughters; Amanda, Brenda and Kate. Brenda is 2 years younger than
Amanda, Kate‟s age is ½ that of Brenda. The total age of the three girls is 27 years. How old
is Kate?
18. Find the solution set for the following inequalities:
(i)
(ii) Solve and give the solutions for x.
(i) (ii)
(iii) (iv)
(iii) Solve and find the solution set for y.
(iv) Solve the inequality below:
i Amonahereza02@gmail.com
3tcm
tcm
tcm
</passage>

<passage id="lchk_853a244a720545528e7e48b2b0a51cd0" source="P 6 Primary SIX MTC Notes Docx (ecolebooks Com)" part="48">
Remarks __________________________________________________________
GET MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
GET MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM 103
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
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
