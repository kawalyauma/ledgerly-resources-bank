# Job ltsk_3ae3f0297c3349fd90d59eb72b4cf658-1

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for Mathematics, Primary Seven 2026, Term 3.
The term has 10 teaching weeks and this subject has 6 periods per week. Every lesson is ONE 40-minute period, so keep each lesson small enough to teach in 40 minutes.
There are no weekly review lessons: the subject has a lot of content, so every period teaches or practises.
Give at most 59 teaching/practice lesson entries in teaching order (the last lesson of the term is the end of term assessment).
Each lesson has a kind: "teach" (new content) or "practice" (the same subtopic as the teaching lesson just before it: exercises, oral work, drawing, matching, filling in blanks, ALL taken from the passages).
When the material is thin (common in lower primary), follow each teaching lesson with a practice lesson. Split big subtopics over several teaching lessons.
Never pad with content the passages do not have: if they cannot fill the term, return fewer lessons and list what is missing in gaps. Ledgerly fills the remaining weeks with revision.
You are composing the SCHOOL'S OWN scheme. The passages below (the official NCDC curriculum and guides, plus schemes of work, lesson plans, notes and past papers from the school e-library) are reference material:
The school's SCHEMES OF WORK for this class and term ("P 7 Primary Seven MTC Scheme OF Work Teacher AC") are the BASE: follow the topics, subtopics and week-by-week order they agree on. Every topic they list for this term MUST become a unit, in their order, and their subtopics become the lessons, with about the pacing they give. Cite their passages in sourcePassageIds of every lesson that follows them.
The NCDC documents (titles starting "NCDC") only FILL GAPS: a topic NCDC lists for this term that the schemes lack gets its own unit where it fits best. Never drop or rename a schemes-of-work topic to fit NCDC. NCDC lower-primary thematic curricula list every learning area side by side in table columns separated by " | ": take only the Mathematics column.
Combine them in this authority order: the school's schemes of work for topics, sequence and pacing; NCDC for anything they miss; the strongest detailed notes for accurate teaching depth; past papers for expected applications and activities.
Use this term's part of the material (Term 3) when the passages cover several terms.

NCDC topics for Primary Seven 2026, Term 3 that must ALSO be covered. Each needs at least one unit whose title or theme names it; the school's schemes of work decide where it goes and how many lessons it gets:
  10. Length, Mass and Capacity
Do NOT write lesson content yet. Each unit and lesson must cite the passage ids it comes from in sourcePassageIds.

Reply shape:
{"title":string,"summary":string,"units":[{"title":string,"theme":string|null,"weekFrom":int|null,"weekTo":int|null,"competences":string|null,"sourcePassageIds":[string],"lessons":[{"title":string,"subtopic":string|null,"kind":"teach"|"practice","objectives":[string],"sourcePassageIds":[string]}]}],"gaps":[string]}

<passages>
<passage id="lchk_48cd5d43ea9e4b658254fbc43c471bde" source="NCDC PRIMARY SEVEN SET ONE – Mathematics" part="1">
Mathematics Syllabus

Primary Seven Curriculum

General Background
This is the revised P7 Mathematics Syllabus for Uganda. It aims at helping
learners to:
• appreciate the value of Mathematics and its usefulness.
• develop confidence in their ability to foster a sense of personal
achievement.
• encourage continuing and creative interest in Mathematics.
The syllabus has been designed in such a way that learners develop a
variety of problem-solving strategies, thinking ability, logical reasoning
and numerical skills. These will be powerful tools in their further study
and later work in exploring the environment. In P7, you have the task
of making Mathematics a reality in life by emphasising learning by
doing and collaborating. The curriculum emphasises the development of
skills, concepts, understanding and attitudes in the learner which will
enable him/her to cope confidently with the Mathematics of everyday
life. Therefore, integrated skills and approaches in all disciplines are
important.

Mathematics is not an isolated skill or procedure. It is everywhere and
relates to other subjects. Therefore, Mathematics must be integrated with
and related to other subjects. In order to do so, there is a need to seek
opportunities for drawing mathematical experiences out of a wide range
of learner’s activities. Many curricular areas and activities give rise to the
need to use Mathematical concepts, principles or ideas.

Rationale
The constant use of the Mathematical approach to situations and the
formation of important concepts are the main aims of this syllabus. The
learning of Mathematics at all levels involves more than acquisition
of basic concepts and skills. It also involves an understanding of the
underlying Mathematical thinking, general strategies of problem-
solving, positive attitude and appreciation of Mathematics. Therefore, a
strong command of Mathematics knowledge and thinking is essential to
enable learners solve new problems on a regular basis. Teachers should
know the philosophy and rationale underlying the intended curriculum
and pay special attention to the scope, depth and linkages of different

National Curriculum Development Centre

topics. This will enable learners make connections and use Mathematics
knowledge to develop transferable skills in numeracy in order to become
the emotionally intelligent and flexible learners needed for the 21st century.
Note
Learning Mathematics does not occur as learners take in Mathematics
knowledge in ready-made pieces but as they build up Mathematical
meaning on the basis of their experiences in the classroom. Therefore,
practical work plays a big role in consolidating what the learners already
know before new ideas are brought in.

Methodology
Methods and approaches to learning experiences should emphasise
higher order thinking and creativity in Mathematics. Therefore, teaching
Mathematics should be done effectively through the application of
concepts and skills in an interesting and realistic context that is personally
meaningful to the learners. This implies that Mathematics is best taught
by helping learners to solve problems drawn from their own experiences.
Therefore, teaching methods to be emphasised are those that allow the
learners to learn from their mistakes. This will help the learners to develop
stronger Mathematical habits that make the future of Mathematics
more efficient. In this way, Mathematics should be taught following the
</passage>

<passage id="lchk_2ac1f09b979f44c5a134d3d041d38438" source="NCDC PRIMARY SEVEN SET ONE – Mathematics" part="2">
concrete, pictorial and symbolic approach so as to assist the learners to
easily discover and actively experiment during learning. The choice of
a method to use in a lesson largely depends on a number of factors. It
is, however, important to note that all methods used are always learner-
centred. The following are examples of learner-centred methods:
1. | Group discussion
2. | Think- pair- share
3. | Demonstration
4. | Guided discovery
5. | Role-play
Note
• You are encouraged to use concrete objects and learner’s real life
experiences while teaching. This will help to enhance retention
of Mathematics concepts besides making learning meaningful
and enjoyable.

Primary Seven Curriculum

• Give learners time to solve problems on the chalkboard and
allow them to explain to their classmates. This will enhance
their confidence and ability to attempt Mathematics problems.
• Take time to read ‘guidance to the teacher’ notes at the end of
each topic. This will enable you make lesson preparations and
presentations better.
Competences
Subject competences
These are the abilities the learner demonstrates to show that learning
has occurred. While making your lesson, use verbs that can help you to
develop the learner’s competences. Think carefully about activities that
develop competences without much difficulty. At the end of every topic,
these are the very competences that will be assessed.

Language competences
In this syllabus, emphasis is put on language competences. These will help
the learner to communicate effectively using the appropriate vocabulary
for a particular topic. You will realise that each topic has its own technical
words and therefore you should ensure that the learner develops the
language competences throughout the teaching/learning process.

Life Skills
Life skills are abilities that will help the learner to develop positive
behaviour and to function purposely in society. Skills cannot be developed
in a short period, there are indicators for every life skill which you expect
to identify in the learner. For example, critical thinking as a skill has the
following indicators:
• Responding to questions appropriately
• Giving reasons for action taken
• Analysing statements
In your scheme of work and lesson plan, always show life skills and
indicators.

National Curriculum Development Centre

Values
Values, on the other hand, are the desired standards or qualities that
are generally acceptable in society. For example, endurance, patience,
appreciation, perseverance, care, respect, trustworthiness, togetherness,
self-reliance, empathy, independence, responsibility and cooperation.

Role of the Teacher
Your role as a teacher is to put in place an environment that will enable
learners develop as many skills and values as possible by the end of a
lesson, through various activities, especially using the practical methods.
Build the mental capacity of the learners by providing mental work at
every beginning of a lesson. Make it a routine exercise and put much
emphasis on multiplication tables.

Use a variety of textbooks to support your teaching.

Assessment Guidelines
Assessment is aimed at finding out the attainment of the learner. Use
continuous assessment to supplement on the formative and summative
assessments. This can be done through observation, class work, homework
and topical tests.

The syllabus should be your major guide in formulating competences for
assessment (at the end of every topic, there are assessment competences
</passage>

<passage id="lchk_61c0c091fa7543daab11fbffcbe24b3d" source="P 7 Primary Seven MTC Scheme OF Work Teacher AC" part="1">
1
TOPICS IN MATHS
THEME TOPIC S/TOPIC DURATION LEANING OUT COMES
SETS Set concepts • Types of sets
- Finite sets
- Infinite sets
- Subsets
• Venn diagrams ( two events)
- Time , length and Algebra
• Probability
- Working out probability of sample events
- One coin
- Two coins
- One dice
- Two dice
The learner
demonstrates the
knowledge of sets in real
life situations.
NUMERACY WHOLE
NUMBERS
• Reading and writing numbers in words up to
99,999,999
• Reading and writing numbers in figures up to
99,999,999
• Roman numerals
- Reading and writing Roman numerals up to MM
- Converting Roman numerals to Hindu ,Arabic and
vice versa
• Bases
- Grouping in twos
- Place values of base two digits
- Changing base two to base ten and vice versa
- Adding in Base two
- Subtracting in base two.
- Multiplication of numbers in Base two.
20 periods The learner manipulates
and converts whole
numbers.
2
• Finding place values of other digits.
- Changing from other bases to base ten and vice
versa
- Finding the un known base
Do OPERATION
ON WHOLE
NUMBERS
• Addition and subtraction on whole numbers
- Multiplying whole numbers by three digit numbers.
- Dividing whole numbers by three digit numbers
25 The learner applies the
basic concept and
operations achieved to
solve.
• Properties of numbers.
- Cumulative property
- Associative property
- Distributive property
- Powers on natural numbers
- Expanding numbers using exponents
- Expressing numbers using standard forms.
(Scientific notation).
- Prime factorization of numbers.
- Finding squares and square root of numbers
Real life problems
PATTERNS
AND
SEQUENCES
• Divisibility test
- For 6
- For 7
- For 8
- For 9
- For 11
- For 12
• Finding square numbers and square roots
• Finding cube numbers.
• Finding triangular numbers.
11
3
• Identifying prime and composite numbers.
• Reading sequences and finding missing numbers
• Finding consecutive odd and even numbers
TERM II
Fractions • Applying fractions in daily life
- Finding unknown fractions
- Tabs
- Remainders
• Decimal fractions
- Identifying repeating and non-repeating decimal
fractions.
- Changing repeating decimals to fractions and vice
versa.
• Rounding off decimals up to hundred thousandths.
- Writing decimals in scientific notation.
• Applying direct proportions in daily life
16 Learner applies decimals
and fractions in daily life
experiences
Do INTEGERS • Applying inverse proportion in daily life
• Applying percentages in daily life
• Increase and decrease in finding percentage.
- Finding original number after percentage increase
or decrease
- Finding percentage decrease or increase.
• Finding simple interest and amount.
- Finding percentage rate, principal and time
• Applying integers in daily life
• Expressing numbers in Finite 5 and 7
• Operation of integers
- Adding numbers in finite 5 and 7 using a dial
10 Learner recognizes,
manipulates and applies
the knowledge of
integers in real life
4
- Subtracting numbers in finite 7
- Multiplying numbers in finite 7
• Application of finite system
situation.
INTERPRET
ATION OF
GRAPHS
AND DATA
Data handling • Interpreting picto graphs .
• Measures of central tendencies.
- Mode
- Range
- Median
- Modal frequency
- Mean
• Review interpretation of bar graphs
• Review interpretation of line graphs.
• Interpretation of pie- charts
• Drawing pie- charts
• Interpretation of travel.
• Drawing travel graphs
19
Learner collects,
organizes, records,
presents and interprets
simple mathematical
data in various forms.
</passage>

<passage id="lchk_1bcedbf0ff1447baa4625871f060b7b3" source="P 7 Primary Seven MTC Scheme OF Work Teacher AC" part="12">
Adds figures
Regrouping figures
Subtracts figures
- Reads the
given metric
unit s
Question and
answer
Demonstration
- Problem solving
- Critical thinking
Wall face
Metre rule
- Adding
- Measuring
- Subtracting
- Macm 260-261 -
19
- Describes the
given metric
units
Multiplication of metric
units
Division of metric units
Multiplies metric units
Divides metric units
Regroups metric units
- Reads the
metric units
- Describes the
given units
Guided
discovery
Discussion
- Decision making
- Critical thinking
Chalkboard
illustration
Metre rule
- Multiplying
- Dividing
Do -
Money Review
Shopping bill and bill
tables
Currency notes
Exchange rates
Multiples figures
Adds
Divides
Simplifies
- Reads word
problems
- Interprets the
given words
- Writes and
uses words
- Exchange
- Currency
- Forex
- Foreign
exchange
Demonstration
Explanation
- Effective
communication
- Decision making
- Problem solving
Money
Items
Like books,
pens etc
- Role playing
- Reading
Mk old edition -
Perimeter Find perimeter
quadrilaterals
Perimeter of combined
shapes
Perimeter of regular
polygons
Number of poles in line
and perimeter
Draws figures
Names figures
Add sides of figure
- Describes
perimeter
- Interprets
different
shapes
- Writes names
of the shapes
Demonstration
Guided
discovery
- Do Cutouts
Chalkboard
illustration
- Cutting
- Naming
- Tracing
- Drawing
Fountin 173
Mk ncdc 162
-
Circumference
of a circle
Find circumference of a
circle given the radius
Finding the circumference
of a circle given diameter
Draws circles
Finds the circumference
Simplifies expressions
- Describes the
word
circumference
- Interprets the
parts of a circle
Guided discovery
Demonstration
- Problem solving
- Critical thinking
Cutouts
Chalkboard
illustration
Basins
Tins
Wires
String
- Drawing
- Naming
- Measuring
Fountain 176
Mk ncdc 167
-
Finding radius
/diameter of
the circle
given
circumference
Finding radius given
circumference
Find the diameter given
circumference
Draws shapes
Identifies missing parts
- Reads word
statement
- Interprets word
statements
Discussion
Question and
answer
- Effective
communication
- Problem solving
Chalkboard
illustration
Cutout
- Reading
- Drawing
- Tracing
- Shading
-
Application of
circumference
Finding number of
revolutions
Finding length of a piece
of wire
Finding diameter of given
length of the wire
Measures object s
Cut out strings
Interprets word statements
Solves problems
- Reads word
problem
- Interprets word
statements
- Spells words
- Revolution
- Circumference
Guided discovery
Discussion
- Problem solving
- Critical thinking
Tins
String
Razorblade
Cutouts
Wires
Tins
- Cutting
- Drawing
- Measuring
Fountain 184-
186
-
Areas Finding area of triangles
Finding missing parts
given area of a triangle
Word statement involving
a triangle
Draws figures
Interpret word statements
Finds area
- Describes the
term area
- Interprets word
problem
Effective
communication
Problem solving
- Cutouts
- Chalkboard
illustration
Drawing
Tracing
- Mk ncdcn 160 -
20
Comparing area of a
triangle
Finding missing part of
triangle by comparing its
area
Draws interprets triangles
Forms equations
Solves word problem
- Interprets
statements
- Read given
statements
Guided discovery
Discussion
- Problem solving
- Critical thinking
Cut out
Chalkboard
illustration
- Drawing
- Reading
-
Area of quadrilateral
Rectangle
Square
Rhombus s
Parallelogram
Kite
Trapezium
Areas and lectures
Draws figures
List properties of figures
Finds area
- Reads the
names of
quadrilaterals
- Spells the
</passage>

<passage id="lchk_dafbc1708c7c4ee7ad41fe07bd1383fb" source="P 7 Primary Seven MTC Scheme OF Work Teacher AC" part="13">
names of
quadrilateral
Guided discovery
Discussion
- Problem solving
Critical thinking
Cut outs
Wall charts
- Drawing
- Cutting
- Tracing
- Scriting
Mk ncdc 161
Macm 262
Fountain 186
-
Area of a circle
Finding area of a circle
Word problem involving
area of a circle
Draws circles
Measures objects
Finds area of a circle
- Interprets
statements
- Reads word
problems
Guided discovery
Explanation
- Problem solving
- Critical thinking
Wall charts - Drawing
- Cutting
- Shading
- Tracing
Fountain 190
Mk ncdc 134
-
Find are of a circle given
circumference
Finding parts of a circle
given tis area
Forms equation for
unknown
Finds missing parts
- Reads word
statements
- Interprets word
problems
Discussion
Questions and
answer
- Do Do - Do Fountain 190 -
Area of parts
of a circle
Area of a semi circle
Area of a quadrant
Area of a sector using
R
360
Names parts of a circle
Shades parts of the circle
Draws parts of the circle
Finds area of the sector
- Reads and
uses words
semi circle,
quadrant
- Sector
- Describes
names of parts
of a circle
Guide discovery
Explanation
Question and
answer
- Critical thinking
- Problem solving
Cutout
Wall charts
- Naming
- Drawing
- Shading
Fountain 195
Mk ncdc
-
Area of
combined
shapes of
circle
Finding are of circles
combined with
Rectangles
Squares
Triangles
Other regular polygons
Draws figures
Interprets combined
Shapes
- Names parts of
combined
shapes
- Interprets the
given shapes
Explanation
Questions and
answer
- Critical thinking
- Problem solving
Cuts outs
Chalkboard
illustration
- Drawing
- Cuttings
- Reading
Fountain 193 -
Shaded
regions
involving circle
Area of shaded regions of
circles combined with
Rectangles
Squares
Triangles
Other regular polygons
Draws shades shapes
Finds shaded shapes
- Describes
shaded part
- Names the
given shapes
- Interprets
figures given
Guided discovery
Question and
answer
- Effective
communication
- Problem solving
- Critical thinking
Cutouts
Wall charts
- Drawing
- Shading
- Painting
- Cutting
-
Application of
area of circle
Finding number of pieces
of cards, circular sheets,
etc that can be cut from a
manila card ,. Iron sheet ,
metric sheet etc
Draws from interpretation
Interprets word problems
Cuts objects given
- Reads word
problem
- Interprets word
statements
Demonstration
Discussion
- Do Manila cards
Paper
Razorblade
Wall charts
- Cutting
- Drawing
- Shading
Mk 389 -
Finding radius
or diameter of
a circle given
area
Finding radius of a circle
given area
Finding diameter of a
circle given area
Interprets word statements
Forms unknown
Solves for unknown parts
- Interprets word
problems
- Interprets given
statements
Guided discovery
Question and
answer
- Do Do - Do Mk 391 -
21
Finding
circumference
given area of
a circle
Calculating the
circumference of circle
given area
Finds the radius
Interprets word problem
Calculates the
circumference
- Reads the word
problem
- Interprets word
problem
Guided discovery
Explanation
Discussion
- Critical thinking
- Problem solving
Wall charts
Chalkboard
illustration
- Reading
- Drawing
- Forming
equation
Fountain 193 -
Total surface
area
Finding total surface are
of a cuboid
Finding total surface area
of a cube
Finding missing side
given total surface area of
a cube
Draws accurate figures
States the properties of
each figure
Finds total surface areas
- Describes
cuboid
- Cubes
- Reads and
uses words
cuboid and
cubes
Demonstration
Guided discovery
Explanation
- Problem solving
- Effective
communication
Boxes
Papers
Manila cards
</passage>

<passage id="lchk_4d661396b95f48799170008c4e2b1edf" source="P 7 Primary Seven MTC Scheme OF Work Teacher AC" part="16">
communication
Do - Do Mk bk 7 449
Word problems involving
inequalities
Example
The Headteacher’s car
can accommodate
maximumly 5 people.
Show this inequality
Solution
x ≤ 5
Reads word problem
Forms inequalities
Forms inequalities
Solves inequality
Simplifies
- Reads word
statements
- Describes word
statements
- Interprets
symbols
- Guided
discovery
Discussion
Problem solving
- Critical thinking
- Pens
- Bottle tops
- Straws
- Pencils
Wall chart
Reading
Drawing
Counting
- Solving
Mk bk 7 450-
451
</passage>

<passage id="lchk_a991f2c3cf1c4b90be96cf2d2bdb566a" source="P 7 MTC Notes Final 1 KQK" part="3">
 Distance, speed and time
 Changing from km/hr to m/sec and viceversa
 Average speed
 Time tables
 Travel graphs
 Drawing travel graphs
TERM THREE
 LENGTH, MASS AND CAPACITY……………………………………………181
 Conversion of length, mass and capacity. (review)
 Finding perimeter. (review)
 Finding area of simple shapes. (review)
 Finding area of square, rhombus and kite using diagonals.
 Finding perimeter and area of parallelogram
 Comparing sides of polygons
 Using apothem to find area
 More about area
 Circle properties
 Finding circumference of a circle and parts of a circle
 Finding perimeter of a circle and parts of a circle
 Finding radius or diameter when given circumference
 Finding radius or diameter when given perimeter
 More about perimeter (irregular figures)
 Finding area of a circle and parts of a circle
 Finding radius or diameter when given area
 Finding area of combined shapes
 Finding shaded area
 More about circumference (revolutions)
 More about perimeter. (no. of poles)
 VOLUME AND SURFACE AREA……………………………………………………………….169
 Converting from square metres (cm 2 ) to square centimetres (cm 2 ) and viceversa
 Converting from square kilometres (km 2 ) to square metres (m 2 ) and viceversa
 Converting from cubic metres (cm 3 ) to cubic centimetres (cm 3 ) and viceversa
 Volume and capacity of cylinders
0776990327 AHEREZA AMON P.7 Mathematics Page 7
 Finding missing sides when given volume of a cylinder
 Volume and capacity of triangular prisms
 Finding missing sides when given volume of a triangular prism
 More about cylinders
 Volume and capacity of trapezoidal prisms
 TSA of cubes and cuboids
 Find missing sides when given TSA of cubes and cuboids
 TSA of a triangular prism
 TSA of a trapezoidal prism
 TSA of closed cylinders
 TSA of cylinders closed one end
 TSA of hollow cylinders
 Packing boxes in boxes
 Packing cylinders in boxes
 Comparing volume of different objects
THEME:ALGEBRA
 ALGEBRA…………………………………………………………………………………213
 Substitution
 Collecting like terms
 Addition and subtraction of fractional algebraic terms
 Multiplication and division of fractional algebraic terms
 Factorizing completely
 Removing brackets
 Removing brackets in fractional algebraic terms
 Solving simple equations
 Solving equations involving squares and square roots
 Solving equations involving brackets
 Solving equations involving fractions
 Forming and solving equations
 Application of algebra in ages
 Finding solution sets
 Solving and writing solution sets
 Finding solution sets with compound inequalities
 Solving and writing solution sets with compound inequalities
0776990327 AHEREZA AMON P.7 Mathematics Page 8
Key words : universal, complement, subsets, union, intersection, empty, finite, infinite,
probability
SUBTOPIC: FINITE AND INFINITE SETS
A finite set is a set whose members can be listed down and has an end.
e.g set T = {even numbers between 4 and 12}
T = {6, 8, 10}
An infinite set is a set whose members are endless.
e.g. a set of odd numbers, a set of all stars in the sky, a set of all integers.
Set K= {all prime numbers}
K= {2, 3, 5, 7, 11, 13…..}
Activity
1. State whether the following sets are finite or infinite:
G = {girls in your class}
B = {boys in your class}
W= {days of the week}
K = {square numbers}
P= {pupils who like football}
T = {multiples of three}
H = {all alphabetical letters}
F = {months of the yea }
REFERENCE
Fountain pri. maths book 7 pg 9
</passage>

<passage id="lchk_19286b632de24d398cbfc0f267a2f7bb" source="P 7 Mtc Notes 1" part="1">
Email: tekule@tekartlearning.com Website: www.tekartlearning.com
1
P.7 math notes
2022
________________________________________
TOPIC ONE:
TOPIC: SET CONCEPTS
LESSON 1:
SUB TOPIC: REVIEW OF SETS
CONTENT: Regions/describing points of venn diagram
AnB
A B Set B
A-B

Set A AUB (AUB)1
Learners will be guided in describing the different regions on venn diagrams.
` A B
EVALUATION ACTIVITY:
MK New Edition BK 7 Pg 5 and Pgs 12 – 13/Fountain bk/NCDC bk
Remarks :
_____________________________________________________________________________
_____________________________________________________________________________
LESSON 2:
SUB TOPIC: LISTING ELEMENTS
CONTENT: Given the venn diagram below:
A B
1 7
4 2
5 3 6
List members of the following using the above venn diagram:
(i) Set B
(ii) Set A 1
(iii) (BnA)
(iv) (AuB)
(v) A-B
EVALUATION ACTIVITY:
Mathematics Revision Hand Book Primary 5, 6, & 7 Pg 18 Exercise 1:2
Remarks :
_____________________________________________________________________________
_____________________________________________________________________________
LESSON 3:
Email: tekule@tekartlearning.com Website: www.tekartlearning.com
2
SUB TOPIC: REPRESENTING SETS ON VENN DIAGRAMS
CONTENT:
Example:
If P = {Factors of 24}
Q= {Multiples of 4 less than 25}
(i) List elements of : P = {1, 2, 3, 4, 5, 6, 8, 12, 24, }
Q = {4, 8, 12, 16, 20, 24}
(ii) Represent the above sets on a venn diagram below:
P Q
(iii) What is: (a) P Ո Q (b) (P ∪ Q)
EVALUATION ACTIVITY:
1. Given that set A = {Even numbers less than 15}
B = {Composite numbers less than 15}
(a) List down the members of the above sets.
(b) Represent the above sets on a venn diagram
2. Given that ɛ = {whole numbers less than 15}
Set P = {4, 6, 14, 8, 0, 12, 3, 7}
Set Q = {1, 3, 5, 7, 9, 11, 13}
Write down the numbers of PnQ
Represent the above sets on a venn diagram
Remarks :
_____________________________________________________________________________
_____________________________________________________________________________
LESSON 4:
SUB TOPIC: NUMBER OF ELEMENTS ON VENN DIAGRAMS
CONTENT:
Example:
The diagram below shows the number of pupils who eat apples (A) and beans (B). Use it to
answer questions that follow:
A B
9 6 8
(i) How many pupils eat both apples and beans?
(ii) How many pupils eat beans n(B) = 6 + 8 = 14
(iii) How many pupils eat apples?
(iv) How many pupils eat only one type of food?
(v) Find the number of pupils in the whole class.
EVALUATION ACTIVITY:
A New MK Maths Revised Edition Bk 7 Pg 9 Exercise 1:6 and exercise 1:9 Pg 14
Remarks :
_____________________________________________________________________________
_____________________________________________________________________________
LESSON 5:
SUB TOPIC: SOLVING PROBLEMS USING VENN DIAGRAMS
CONTENT: Given that n(A) = 30, n(B) = 25 and n(AUB) = 45.
(a) Draw a venn diagram to show the above information.
n(A) = 30 n(B)=25
30 – r r 25 - r
(b) Find n(AnB)
Let the number in (AnB) be r.
30 – r + r + 25 – r = 45
30 + 25 + r – r – r = 45
55 – r = 45
55 – 55 – r = 45 – 55
- r = -10
- r = -10
- 1 - 1
Email: tekule@tekartlearning.com Website: www.tekartlearning.com
3
R = 10
(ii) A only
Probability of elements in the intersection.
EVALUATION ACTIVITY:
A New MK Primary Maths ppls Bk 7 Pg 10 – 11 exercise 1:7
Remarks :
_____________________________________________________________________________
_____________________________________________________________________________
</passage>

<passage id="lchk_afda0fd0df524f3eb3938c3ef0962d84" source="Primary Seven Maths" part="48">
1 st 2 nd 3 rd 4 th 5 th 6 th 7 th 8 th 9 th 10 th 11 th
By counting we have ten poles btn 1 st and tenth pole and nine spaces.
No. of spaces = No of poles – 1
Distance = (10 – 1) X 20m
= 9 X 20m
= 180m.
2. Closed fences:
In closed fences the number of poles corresponds with the number of
spaces. In the illustration below the number of poles is 10 and the number
of spaces is also 10 1 2 3
1 2 3 4
10 4
10
5
9
9 8 7 6
8 7 6
Example:
Mukasa’s rectangular flower garden measures 10m by 8m. He fenced it,
putting the poles 2m apart. How many poles did he need?
Solution:
COLLECTED,UPGRADED,PRINTED AND MARKETED BY ACOSMA EDUCATION SERVICES(0752614244) Page 79
Perimeter of flower garden
= 2(l + w)
= 2(10 + 8)m
= 2(18)
= 36m
No. of poles
= Perimeter
Space btn poles
= 36m 18
2m
= 18 poles
ACTIVITY:
1. When sprinting, Ivan athlete covers 180cm with every stride.
(a) How many strides does he take to finish 100m.
(b) How far does he run in 200 strides?
2. Telephone poles are 20m apart. What is the distance from the first pole to the 16 th pole?
3. The distance around my farm is 400m. If I want posts for fencing spaced 4m, how many
posts will I need?
EVALUATION ACTIVITY:
Macmillan Primary Mathematics Bk 7 exercise 1 Pg 81.
Remarks :
_________________________________________________________
Lesson : 6
SUB TOPIC: TRIANGLE
CONTENT : Area of a triangle
Examples:
1. Find the area of triangle ABC
A
10cm
8cm
B 12cm C
A = ½ x b x h
= ½ x 12 x 8
=6 x 8
A = 48cm 2 .
EVALUATION ACTIVITY:
A New MK Primary Mathematics Bk 7 exercise 19:1 and 18:1 Pg 351
Remarks :
_____________________________________________________________________________
_____________________________________________________________________________
LESSON 7:
SUB TOPIC: TRIANGLE
CONTENT : Finding the missing side when given the area.
Examples:
1. Find the height marked h.
16cm
h
6cm
12cm
½ x b x h = ½ x b x h
½ x 12 x h = ½ x 16 x 6
6h = 48
6h = 48
6 6  h = 8cm
EVALUATION ACTIVITY:
A New MK Primary Mathematics Bk 7 exercise 19:2 and 18:1 Pg 352
Remarks :
_____________________________________________________________________________
_____________________________________________________________________________
COLLECTED,UPGRADED,PRINTED AND MARKETED BY ACOSMA EDUCATION SERVICES(0752614244) Page 80
LESSON 8
SUB TOPIC: TRIANGLE
CONTENT : Application of Pythagoras theorem in a triangle.
Examples:
1. Find the value of x and the area of the figure below.
A Value of x=
a 2 + b 2 = c 2
4 2 + x 2 = 5 2
4 x 4 + x2 = 5 x 5
X 5cm 16 + x 2 = 25
16 – 16 + x 2 = 25 – 16
X 2 = 9
____ _____
B C  X 2 =  9
4cm X = 3cm
2. Area of the triangle
A = ½ x b x h
= ½ x 4 x 3
= 2 x 3
= 6cm 2
EVALUATION ACTIVITY:
A New MK Primary Mathematics Bk 7 exercise 19:3 Pg 353
Remarks :
_____________________________________________________________________________
_____________________________________________________________________________
LESSON 9
SUB TOPIC: QUADRILATERALS
CONTENT : Area of: square, rectangle and parallelogram
Examples:
1. Find the value of x and the area of the figure below.
A = S x S
= 7 x 7
= 49cm 2
7cm
9cm
2. A = L x W
5cm = 9 x 5
= 45cm 2
11cm
3. A = b x h
6cm = 11 x 6
= 66cm 2
EVALUATION ACTIVITY:
A New MK Primary Mathematics Bk 7 exercise 19:4 Pg 354
Remarks :
_____________________________________________________________________________
_____________________________________________________________________________
COLLECTED,UPGRADED,PRINTED AND MARKETED BY ACOSMA EDUCATION SERVICES(0752614244) Page 81
LESSON 10
</passage>

<passage id="lchk_e3fe8895a7be41a186b869b10a1cb4ac" source="BOT 3 MTC" part="1">
HILLSIDE PRIMARY SCHOOL-NAALYA
BEGINNING OF TERM THREE EXAMINATIONS
2022

MATHEMATICS (SET SEVEN)
Time Allowed: 2 Hours 30 Minutes

Index No. | | |
Candidate’s Name... cccccsssssssssssensescensneseesesees bebe oUaceresenceeyenaees
Candidate's Signature........0.....ccccccsssssssesesssesesesesesesssecscseseeseseseeesseeeeees
SS Stream: ...........ccceeeeeeeeeeeee
District Name... ceccccecccscsesesessesesescccscsssesesecscsesscscsevscscesensssecauseeeese
Read the following instructions carefully:
1. The paper has two sections: A and B. FOR EXAMINERS’
Section A has 20 questions and Section B USE ONLY
has 12 questions [@n. No. | MARKS] EXRS’
NO
2. Answer all questions. All answers to both 1-5
sections A and B must be written in the
spaces provided. 6-10
1-15 |
3. All working must be done using a blue or
black ball-point pen or fountain pen. Any work 16- 20
written in pencil other than graphs and diagrams 4 |
21-22 ]
will not be marked
23-24 |
4. No calculators are allowed in the examination a
room. 25- 26
5. Unnecessary changes in work may lead to ET}
loss of marks. Any handwriting that cannot easily be . |
read may lead to loss of marks. 29- 30 4 |
6. Do not fill anything in boxes 31-32] r
indicated: “For Examiners’ Use Only” TOTAL
and those inside the paper.

© 2022 Hillside Primary School-Naalya; Office of the Deputy Head Teacher-Academics 1. Turn Over

SECTION A: 40 MARKS
Answer all questions in this section
Questions 1 to 20 carry two marks each

.- Add 35 + 23

. Write 419 in words.

. A lesson which lasted 40minutes ended at 8:10a.m. At what time did it
start?

. Kapere has 8.75 kg of carry powder to be packed in packets of 0.25 kg
each. How many packets will Kapere make?

5. Study and complete the sequence below:

1,.3, 7, 13, 21,

6. Simplify: 4k -— 5m + 2k -— 3m

7. Write “twenty thousand, four hundred four” in figures.

8. Solve: 3(x + 4) = 24

9. Express 3 kg to grams.

10. What number has been expanded to get:
(4 x 107) + (2 x 10°) + (6 x 107) + (1 x 10°’)?

11.Given that p = ~4, q = 3 andc = "2, find the value of --

12. Work out the value of x: 3 + 4 = x (finite 5)

13. Solve: 2°* + 2" = 16

14. Bisect angle ABC in the figure below.

A Cc

15. The probability that a car picked at random from the park is made in
Japan is =. What is the probability of picking one that is not made from
Japan?

16. The price of a skirt increased by 10%. If the new price is sh. 44,000, find
the original price of the skirt.

17. Shade the complement of H

T H

CO)

18. Study the pie-chart below and use it to find the value of k.

19. Find the square root of 5 ‘.

20.A fisherman saw a boat on water on a bearing of 060°. What is the
bearing of a fisherman from the boat?

SECTION B: 40 MARKS
21. Given the digits 2, 0 and 8

a) Form the smallest 3-digit number using the digits above. (1 mark)

b) Write the numeral formed in (a) above in scientific notation. (2 marks)

c) Show the above numeral on the abacus. (2 marks)

22.a) Subtract 6m — 8 from 4m — 6 (2 marks)

b) Solve the equation: 2+r= 2r+6 (3 marks)

23. The following items were bought by a pupil for the school:

» 2 dozens of books at sh. 6,000 each
» A geometry set at sh. 3,500

> 3 dozens of pencils at sh. 3,000 each
> 6 pens at sh. 500 per pen.

a) Calculate the total expenditure. (4 marks)

b) Work out his change if he went with sh. 30,000 to the shop.
(1 mark)

24.At a gathering of men, 2y men ate beef (B) only, 50 men ate chicken (C),
</passage>
</passages>

Your previous outline was rejected because it does not follow the school's schemes of work and the required topics for this term:
- only 12 of 38 teaching lessons cite the school's schemes of work; they must follow the schemes' topics, subtopics and order (cite their passages)
Redo the WHOLE outline from the school's schemes of work (their topics, subtopics and order, citing their passages), adding any missing NCDC topic.

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
