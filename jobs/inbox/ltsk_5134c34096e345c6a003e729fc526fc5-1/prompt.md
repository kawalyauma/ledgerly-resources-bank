# Job ltsk_5134c34096e345c6a003e729fc526fc5-1

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for Mathematics, Primary One 2026, Term 3.
The term has 10 teaching weeks and this subject has 7 periods per week. Every lesson is ONE 40-minute period, so keep each lesson small enough to teach in 40 minutes.
Ledgerly reserves the last lesson of each week for a review of that week.
Give at most 60 teaching/practice lesson entries in teaching order (the last lesson of the term is the end of term assessment).
Each lesson has a kind: "teach" (new content) or "practice" (the same subtopic as the teaching lesson just before it: exercises, oral work, drawing, matching, filling in blanks, ALL taken from the passages).
When the material is thin (common in lower primary), follow each teaching lesson with a practice lesson. Split big subtopics over several teaching lessons.
Never pad with content the passages do not have: if they cannot fill the term, return fewer lessons and list what is missing in gaps. Ledgerly fills the remaining weeks with revision.
You are composing the SCHOOL'S OWN scheme. The passages below (the official NCDC curriculum and guides, plus schemes of work, lesson plans, notes and past papers from the school e-library) are reference material:
The school's SCHEMES OF WORK for this class and term ("P I Mathematics Scheme OF Work Term Iiii") are the BASE: follow the topics, subtopics and week-by-week order they agree on. Every topic they list for this term MUST become a unit, in their order, and their subtopics become the lessons, with about the pacing they give. Cite their passages in sourcePassageIds of every lesson that follows them.
The NCDC documents (titles starting "NCDC") only FILL GAPS: a topic NCDC lists for this term that the schemes lack gets its own unit where it fits best. Never drop or rename a schemes-of-work topic to fit NCDC. NCDC lower-primary thematic curricula list every learning area side by side in table columns separated by " | ": take only the Mathematics column.
Combine them in this authority order: the school's schemes of work for topics, sequence and pacing; NCDC for anything they miss; the strongest detailed notes for accurate teaching depth; past papers for expected applications and activities.
Use this term's part of the material (Term 3) when the passages cover several terms.
Theme-only references (P 1 Term 3 Scheme; P 1 Term 3 Scheme 2019 (ecolebooks Com)): general thematic schemes covering every learning area. Use them ONLY for the term's theme name and week order; ignore their content for other learning areas (reading, spelling, drawing, literacy, songs). Every lesson must be Mathematics content.
NCDC topics for Primary One 2026, Term 3 that must ALSO be covered. Each needs at least one unit whose title or theme names it; the school's schemes of work decide where it goes and how many lessons it gets:
  9. Our Transport
  10. Things We Make
  11. Our Environment
  12. Peace and Security
Do NOT write lesson content yet. Each unit and lesson must cite the passage ids it comes from in sourcePassageIds.

Reply shape:
{"title":string,"summary":string,"units":[{"title":string,"theme":string|null,"weekFrom":int|null,"weekTo":int|null,"competences":string|null,"sourcePassageIds":[string],"lessons":[{"title":string,"subtopic":string|null,"kind":"teach"|"practice","objectives":[string],"sourcePassageIds":[string]}]}],"gaps":[string]}

<passages>
<passage id="lchk_b6b48e9ad75e4e459fa9bf5877391140" source="NCDC P1 Curriculum" part="1">
Ministry of Education, Science,
Technology and Sports

The National Primary School
Curriculum for Uganda

Primary 1

a

Ministry of Education, Science,
Technology and Sports

The National Primary School
Curriculum for Uganda

Primary 1

© National Curriculum Development Centre, Uganda

Reprinted, 2016
National Curriculum Development Centre,
P.O. Box 7002,
Kampala.

ISBN: 978-9970-00-158-3

All rights reserved. No part of this publication may be reproduced,
stored in a retrieval system, transmitted in any form or by any means;
electronic, mechanical, photocopying, recording or otherwise without
the prior written permission of the publisher.

Website: www.ncdc.go.ug

ii

Table of Contents

Acknowledgements ......................................................................................................................iv
Foreword ...................................................................................................................................... v
SECTION 1: INTRODUCTION ................................................................................................... 1
Introduction .................................................................................................................................. 2
1. The National Aims of Education .............................................................................................. 2
2. The Aims and Objectives of Primary Education ...................................................................... 2
3. The Layout of the Lower Primary Curriculum .......................................................................... 3
4. The Overall Approach in P1-P3 ............................................................................................... 4
5. The Organisational Approach of the Thematic Curriculum...................................................... 6
6. The Approach to Assessment ................................................................................................. 8
SECTION II: CURRICULUM CONTENT ................................................................................... 9
Theme 1: Our School ................................................................................................................. 10
Theme 2: Our Home .................................................................................................................. 13
Theme 3: Our Community.......................................................................................................... 17
Theme 4: The Human Body and Health .................................................................................... 21
Theme 5: Weather ..................................................................................................................... 25
Theme 6: Accidents and Safety ................................................................................................. 28
Theme 7: Living Together .......................................................................................................... 31
Theme 8: Food And Nutrition ..................................................................................................... 35
Theme 9: Our Transport ............................................................................................................ 39
Theme 10: Things We Make ...................................................................................................... 43
</passage>

<passage id="lchk_01989bff14fa4b43a565c48b7ebbcc49" source="NCDC P1 Curriculum" part="2">
Theme 11: Our Environment...................................................................................................... 46
Theme 12: Peace And Security ................................................................................................. 49
CHRISTIAN RELIGIOUS EDUCATION ..................................................................................... 52
ISLAMIC RELIGIOUS EDUCATION .......................................................................................... 61
PHYSICAL EDUCATION (PE) ................................................................................................... 67

iii
iii

Acknowledgements
The NCDC wishes to thank the following for their role in the Thematic
Curriculum Review and for designing the new Thematic Curriculum:

Baale Remegious | NCDC – TCRP Coordinator
Kyagaba Angela | NCDC – Asst Coordinator
Acuro Margaret Lomoro | Gulu Town P/S
Adupa Lorika Dinah | Moroto Municipality, Education Office
Agaba Gertrude | Bushenyi core PTC
Ahurra Katherine Joyce | Buhinga P/S
Akech Oboth Angela | Achilet P/S
Bakahuuna Elizabeth | Nakaseke PTC
Bakehena Edinance | NCDC
Bukenya Gerald Nakatumba | NCDC
Busobozi Godfrey | Greenhill Academy
Eron Lawrence | Kyambogo University
Kagimba Evah | Rukungiri PTC
Karungi Charity | Kikulu P/S
Migando Oliver | Bundibugyo PTC
Muheirwe Monica | Kyambogo University
Natunga Sarah | Namungoona Orthodox P/S
Neumbe Catherine Gimei | NCDC
Ongom Fresher Ben | St Mary’s PTC, Bukedea
Wambi Moses | Bishop Willis PTC, Iganga

Connie Kateeba
Director,
National Curriculum Development Centre - NCDC

iv
iv

Foreword
In 2003-2004 the Ministry of Education, Science, Technology and Sports (MoESTS), believing that many
learners in the country were failing to achieve acceptable levels of literacy and mathematics in primary
education, carried out a wide-ranging review of the primary school curriculum. The results of the review
showed need for:

a) A greater concentration on the development of those key skills in early childhood education that are
particularly valued by the community and that are also fundamental to continuing effective
educational performance - especially literacy, mathematical and life skills.
b) A curriculum that is focused more on the development of key skills, values and attitudes than on the
inculcation of factual knowledge. This does not mean that content is not considered to be important,
but rather that content has to be relevant and capable of being used effectively by learners.
c) A flexible curriculum with a realistic content load, which allows for a greater level of choice to be
made by different geographical areas according to their local needs, interests and resources.

On the basis of the above major concerns, the review made the following recommendations:

a) The current primary school curriculum should be divided into distinct cycles – P1 to P3, P4, and P5
to P7 – with separate aims and objectives and separate structures for each.
b) The curriculum for P1-P3 should be based on the fast development of basic skills, with emphasis on
the development of literacy, mathematics and key life skills. This should be achieved by re-
structuring the current main curriculum requirements around a thematic base.
c) Religious Education and Physical Education should be maintained as separate learning areas within
the P1- P3 Curriculum.
d) The curriculum for P4 and P5 to P7 should be based on identifiable and transferable skills and
</passage>

<passage id="lchk_a9c2033869604d00a20a918b336cc508" source="NCDC P1 Curriculum" part="44">
Traditional Games Involving Imitation
Content (abilities, skills | Competences | Life Skills | Values
and knowledge)
IMITATIONAL | Making movement involving: |  | Coordination |  | Coordination
MOVEMENTS |  Pushing and pulling |  | Decision making |  | Endurance
 Traditional games |  Throwing and catching |  | Critical thinking |  | Leadership and group
involving various |  Jumping off and on objects |  | Creative thinking | organisation
imitational activities |  Lifting objects appropriate to |  | Interpersonal |  | Cooperation

and movement like | the age | relationship |  | Appreciation
work, animals and |  | Timing movements |  | Self esteem
natural happenings

Assessment Guidelines
Making movement involving:
 Pushing and pulling
 Throwing and catching
 Jumping off and on objects
 Lift objects appropriate to the age
 Timing movements
 Being observant
 Respond and perform timely

Weeks 10-12

Games for Lower Primary
Content (abilities, skills and | Competences | Life Skills | Values
knowledge)
SIMPLE GAMES |  | Perform various skills in |  | Coordination |  | Appreciation
 Reaction games | given games |  | Interpersonal |  | Determination
 Imitation games |  | Identify the winner and a | relationship |  | Cooperation
 Running and chasing | looses |  | Creative thinking |  | Sharing
games |  | Follow the rules of the |  | Friendship formation |  | Endurance
 Cooperative games | game. |  | Critical thinking |  | Time
 | Move enthusiastically |  | Conflict resolution | management

Assessment Guidelines
 Perform various skills in given games
 Identify the winner and the loser
 Follow the rules of the game
 Move enthusiastically

National Curriculum Development Centre
Ministry of Education, Science, Technology and Sports,
P.O. Box 7002, Kampala, Uganda

Website: www.ncdc.go.ug
</passage>

<passage id="lchk_cd516a1123334aabaa48f14476aa58b0" source="P I Mathematics Scheme OF Work Term Iiii" part="1">
P.I MATHEMATICS SCHEME OF WORK TERM 3
W
K
P
D
THEME TOPIC SUB –
TOPIC
COMPETENCES CONTENT Act MTD LIFE SKILLS
& VALUES
INST
MAT
REF
1 1
Transport
Number patterns and sequence
Counting and writing number names 1 -
10
- A learner
- Identifies number
symbols correctly
- Counts and writes
number symbols
correctly
- Writes number
names correctly
- Reads, spells and
pronounces words
correctly
Number symbols 1 – 1000
1 , 2, 3, 4, 5, 6, 7, 8, 9, 10
11 12, 13, 14, 15, 16, 17
18, 19, 20, 21,
22,…………………...100
Writing number names
10 – ten 40 – forty
20 – twenty 50 – fifty
30 thirty 60 – sixty
70 – seventy 100 – one hundred
Countin
g
numbers
1 – 100
Writing
numbers
Spelling
number
names
Observati
on
Question
and
answer
Brain
storming
Guided
discovery
Accuracy
Creative
thinking
Appreciatio
n
A chart
showin
g
number
symbol
s and
names
Flash
cards
Straws
Ne
w
Mk
Bk
pg
49
and
42
Und
st,
mat
h
Bk
pg
32
2
Operation on numbers
Multiplying by 2
- A learner
- Identifies the
symbol for times
(x)
- Counts in twos
correctly
- Multiplies using
groups and groups
in twos
- Reads and
interprets the
instructions
correctly
- Writes the
multiplication
symbol correctly
Multiplication of 2 ( x 2)
1. 0 x 2 = 0
2. 2 x 2 = 4
3. 2 4
x 3 x 2
6 8
4. 2 groups of 4 equals = 8
5. 1 group of 2 equals 2
6. Count in twos
0, 2, 4, ___, 8, ___, ___ 14
Groupin
g objects
Countin
g
numbers
orally
Writing
3 -
2 1 -
2 -
3 - -
4 - -
5 - -
1 -
3
3 1 -
2 -
3 - -
4 -
4 1 - -
2 -
3 - -
4 - -
5 - -
5 1 - -
2 - -
3 - -
4
5 - - -
6 1 - -
2 - - -
7 1 - - -
2 - - -
3
4
5 -
-
8 1 -
-
2 -
-
3 -
-
4 -
5 -
9 1 -
2 -
3 -
-
</passage>

<passage id="lchk_0ddfbfb9e8a946889e11832f87f4b83d" source="P 1 Term 3 Scheme" part="16">
Inquiry
Class discussion
Reading the
statements
and counting
the numbers
on a number
line.
Adding and
subtracting
numbers on a
number line.
Critical thinking
Appreciation
Sharing
Problem solving
Confidence
Chalkboard illustration
& prepared work on
paper
Tr’s
own
collecti
on
ENG
(Grm)
Similar words
Def. What are
similar words ?
Examples of similar
words
- Describes the similar
words.
- Identifies words with
the same meaning but
different spelling and
pronunciation.
- Reads and spells
similar words.
Demonstration
-Class
discussion
-Question and
answer
- Brain storming
- Describing
the similar
words.
- Identifying
words with
the same
meaning but
different
spelling and
pronunciation.
- Reading and
spelling
similar words.
Appreciation
Effective
communication
Creative and
critical thinking
A
chart
relate
d to
the
lesson
Junior
Eng.
Book 1
pg.32 &
63
book 2
pg. 23
& 59
LIT I REVISION WORK IN LITERACY ONE.
LIT II REVISION WORK IN LITERACY II
WEEK
DAY
SUB-
THEME
L/AREA CONTENT COMPETENCES MTHDS ACTIVITY L/SKILLS L/MTRLS REF.
FRIDAY
MATH
WEEKLY TESTS EVERY FRIDAY
ENG
LIT I
LIT II
WEEK
DAY
SUB-
THEME
L/AREA CONTENT COMPETENCES MTHDS ACTIVITY L/SKILLS L/MTRLS REF.
MONDAY - FRIDAY
MATH
END OF TERM III EXAMS INTERNAL :
MATHEMATICS, LITERACY I, ENGLISH,
LITERACY II, READING/WRITING
CORRECTIONS
ENG
LIT I
LIT II
WEEK
DAY
SUB-
THEME
L/AREA CONTENT COMPETENCES MTHDS ACTIVITY L/SKILLS L/MTRLS REF.
MONDAY - FRIDAY
MATH
END OF TERM III EXAMS EXTERNAL :
MATHEMATICS, LITERACY I, ENGLISH,
LITERACY II, READING/WRITING -
CORRECTIONS
ENG
LIT I
LIT II
</passage>

<passage id="lchk_73f42cce93f54a598f3ca9718dc2c84c" source="NCDC P1 Curriculum TG" part="1">
Primary School Curriculum , Teacher’s Guide- Primary 1

Ministry of Education, Science,
Technology and Sports

a

Ministry of Education, Science,
Technology and Sports

© National Curriculum Development Centre, Uganda

Reprinted, 2016
National Curriculum Development Centre,
P.O. Box 7002,
Kampala.

ISBN: 978-9970-00-162-0

All rights reserved. No part of this publication may be reproduced,
stored in a retrieval system, transmitted in any form or by any means;
electronic, mechanical, photocopying, recording or otherwise without
the prior written permission of the publisher.

Website: www.ncdc.go.ug

Primary School Curriculum , Teacher’s Guide- Primary 1

Abbreviations
CCT | Coordinating Centre Tutor
DIS | District Inspector of Schools
LoI | Language of Instruction
MIS | Municipal Inspector of Schools
TP | Teaching Procedure
TRB | Teacher‘s Resource Book

This Teacher's Guide was developed by the Thematic Curriculum Review Panel:

Baale Remegious | NCDC - TCRP Coordinator
Kyagaba Angela | NCDC - Asst. TCRP Coordinator
Acuro Margaret Lomoro | Gulu Town P/S
Adupa Dinah | Moroto Municipality, Education Office
Agaba Gertrude | Bushenyi core PTC
Ahurra Katherine Joyce | Buhinga P/S
Akech Oboth Angela | Achilet P/S
Bakahuuna Elizabeth | Nakaseke PTC
Bukenya Gerald Nakatumba | NCDC
Bakehena Edinance | NCDC
Busobozi Godfrey | Greenhill
Eron Lawrence | Kyambogo University
Kagimba Evah | Rukungiri PTC Karungi
Charity | Kikulu P/S
Migando Oliver | Bundibugyo PTC Muheirwe
Monica | Kyambogo University Natunga
Sarah | Namungoona Orthodox P/S
Neumbe Catherine Gimei | NCDC
Ongom Fresher Ben | St. Mary's PTC
Wambi Moses | Bishop Willis PTC, Iganga

iii

National Curriculum Development Centre

Foreword

The P1 Thematic Curriculum Teacher's Guide

Hon. Geraldine Namirembe
Bitamazire
This Teacher's Guide to the Primary One Thematic Curriculum provides enduring
support to the teachers in interpreting the curriculum into lessons designed for effective
learning. It is the source of guidance to the teachers on:
(a) Teaching resources that make learning easier and enjoyable.
(b) How t o a c q u i r e t e a c h i n g /learning resources from the schools' immediate
environment.
(c) How to set an appropriate scope of content in lessons for Primary One learners.
(d) Basic instructional exercises and class drills that set a desirable pace in various
activities for learning.
This Teacher’s Guide presents complete schemes of work and lesson plans for the initial
part of the curriculum and gradually enables the teacher to make own schemes of work and
lesson plans for the rest of the P1 Thematic Curriculum. Thus, the document provides a
readily available continuous orientation to the teaching of this curriculum.

The Teacher's Guide to the P1 Thematic Curriculum is written in such a way that the teacher
has resource to it:
(a) While planning the lesson.
(b) During lesson time, as the bare minimum of what the planned lesson should be.
(c) For self-appraisal on how well the completed lessons were conducted.
(d) As a constant reference when drawing up realistic schemes of work and effective
lesson plans.
This Teacher's Guide should be the first reference resource on the teaching of the P1
Thematic Curriculum. The effectiveness of the lesson is judged by the learning outcome by
the pupils; and thus, the Teacher's Guide is a ready-made tool for this purpose.

I, therefore, recommend the P1 Thematic Curriculum Teacher's Guide for use in all primary
</passage>

<passage id="lchk_d45df310ebfb4db5bb10f3304fdce1d8" source="P 1 Mathematics Lesson Notes Term III" part="1">
1
PRIMARY ONE MATHEMATICAL LESON NOTES FOR TERM 3
Date Class No. of children Time
THEME: Transport
SUB THEME: Types and means of transports
TOPIC: Whole number
S. TOPIC: Counting and writing number names
METHODS: - mental work
- Guided discovery
- Question and answer
COMPETENCES: Count numbers and read number names
- pronounces words correctly
- reads and spells words Correctly
- fills in the missing numbers
REFERENCE : Mk Book 1 pupils gride page 49 and 42
CONTENT: Counting 1 – 90
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
21, 22, 23, 24, 25, 26, 27, 28, 29, 30, __, ___, ___, ___, ___, 90
Reading number names 1 – 100
1 – one 8 – eight
2 – two 9 – nine
3 – three 10 – ten
4 – four 11 – eleven
5 – five 12 – twelve
6 – six 7 – seven etc up to 100.
EXERCISE:
2
1. Fill in the missing number
20, 21, ____, ___, ___, 25, ____, ____, ____, 29, 30
50, 51, ____, ___, ___, 55, ____, ____, ____, 59, 60
30, 31, 32, ____, ____, ____, 36, ____, ____, ____, 40
2. Write number names.
20, 40, 8, 60, 80
30, 50, 13, 70, 90
12, 11, 15, 13, 2
3. Match number symbols to words .
64 forty three
90 seventy eight
78 ninety
43 sixty four
4. Count and write in words.
= _______
= _______
5. Count down wards
10, 9, __, ___, 6 ___, 4, ____, 12 ___ 0
Date Class No. of children Time
THEME: Transport
SUB THEME: Types and means of transports
TOPIC: Operations on Numbers
S. TOPIC: Multiplication by 2 and 3
METHODS: - mental work
- Observation
- Question and answer
COMPETENCES: - groups in two’s
- Reads the instructions correctly
- Writes the multiplication symbols correctly
- Reads and interprets the statements
INTRODUCTION: Review of the previous lesson
3
CONTENT: Multiplying by 2
0 x 2 = 0 3 6
0 groups of 2 = 0 x 2 x 2
1 x 2 = 2 6 12
1 groups of 2 = 2
2 x 2 = 4
2 groups of 2 = 4
2 groups of 3 equals 6
NB:
The first number shows the groups.
The second number shows the balls in each group.
Multiplying by 3
0 x 3 = 0
0 groups of 3 = 0
1 x 3 = 3
1 group of 3 = 3
2 x 3 = 6
2 groups of 3 = 6
Use repeated addition
2 + 2 = 4 count in twos
2 + 2 + 2 = 6 2 4 6 ___ 10
3 + 3 = 6 count in threes
3 + 3 + 3 + 3 = 12 3 6 ___ 12 ___
EXERCISE:
1. Multiply by 2. Count in twos
4
2 x 2 = 2 + 2 + 2 = _______
3 x 2 = 2 + 2 + 2 + 2 = _______
5 x 2 = 3 + 3 + 3 + 3 = _______
8 x 2 = 3 + 3 = ________
2. Multiply by 3.
1 x 3 = 5 x 3 =
2 x 3 = 4 x 3 =
3 x 3 = etc
LESSON EVA’L:
Date Class No. of children Time
5
THEME: Transport
SUB THEME: Types and means of transports
TOPIC: Operations on numbers
S. TOPIC: Multiplication by 5 and 10
METHODS: - mental work
- Observation
- Question and answer
Competences : a learner
- Reads and interprets statement
- Counts in fives
- Identifies the symbols correctly
- Multiples by 10 correctly
INTRODUCTION: Review of the previous lesson
Counting 100 – 150 orally
REFERENCE :
CONTENT: Multiplying by 5 and 3
0 x 5 = 0 3
0 groups of 5 x 5
1 x 5 = 5 1 5
1 group of 5
2 x 5 = 10equals
2 groups of 5
Multiplying by 10
2 x 10 = 20 10
2 groups of 10 x3
1 x 10 = 10 30
Use repeated addition
6
5 + 5 = 10
5 + 5 + 5 = 15
10 + 10 + 10 = 30
EXERCISE:
Let us multiply .
1. 1 x 5 = 3 x 10 = 4 x 5 =
5 x 10 = 3 x 5 = 1 x 10 =
4 x 4 = 2 x 10 = 0 x 10 =
2. 10 + 10 + 10 = 10 + 10 =
5 + 5 + 5 = 5 + 5 =
3. 10 10 10
x 2 x 5 x 3
4. _____ as the first day of the week.
5. 4 groups of 3 equals
6. Fill in the missing numbers
100, 101, ____, 103, ___, 105, ___ 107
120, 121, ___, ____, 124
LESSON EVALUATION:
Date Class No. of children Time
7
THEME: Transport
</passage>

<passage id="lchk_2df278fedc064552b6e6ebff58156b62" source="P 1 Maths Term III Notes" part="4">
Mathematical statements on addition
Words used in addition
- Add
- Altogether
- And
- Both
- Sum
- Total
- Plus
- Put together
- More
a) Two plus five equals _________________________________
b) What is the sum of three, two and four?
__________________________________________________
c) Jane has four apples. John has three apples
How many apples do they have altogether?
____________________________________________________
d) Find the total of five and six oranges
__________________________________________________
e) What is six and four?
___________________________________________________
f) Tom had six books. Teo had five books.
Both had ___________books altogether.
g) Daddy had 2 sweets. Mummy gave him more 7 sweets. How many
sweets did daddy have altogether?
________________________________________________________________
Mathematical statements on subtraction
Words used in subtraction
- Subtraction
- Take away
- Less
- Minus
- Remain
- Remove
For more lesson notes, visit www.freshteacheruganda.com
a) Subtract 4 mangoes from 11 mangoes
_______________________________________________________________
b) What is 8 take away zero
_______________________________________________________________
c) Twelve minus six equals ________________________________________
d) What is four less two? __________________________________________
e) A hen had 8 eggs. Five eggs were broken. How many eggs
remained?__________________________________________________________
f) Remove 4 pens from 10 pens. How many pens remain?
________________________________________________________________
Mathematical statements on the multiplication
Words used in multiplication
- Multiplication
- groups of
- times
Note: teacher will give examples using words above.
Mathematical statements on division
Words used in division
Share
Divide
Among
Equally
Between
give
Note : Teacher will give examples using words above.
</passage>

<passage id="lchk_b8e237bc42134fbf9bef9971634a56d3" source="Primary ONE Maths" part="12">
_______________________________________________________________
f)Remove 4 pens from 10 pens. How many pens remain?
_____________________________________________________________
Mathematical statements on the multiplication
Words used in multiplication
- Multiplication
- Groups of
- Times
Note: teacher will give examples using words above.
Mathematical statements on division
Words used in division
COLLECTED, PRINTED & MARKETED BY ACOSMA EDUCATIONAL SERVICES (0752614244 ) Page 58
Share
Divide
Among
Equally
Between
Give
Note: Teacher will give examples using words above.
ACOSMA EDUCATIONAL SERVICES-0752614244
</passage>

<passage id="lchk_fcc4910f9e0348669563c7e0f6f79b36" source="EOT MTC P 1 BY Smile" part="1">
WHAT’S APP: +256779680288 1
SMILE EDUCATION CONSULTANCY BUSUNJU
P.1 End of Term III Examination, 2023
Mathematics
Name:______________________________________
SECTION A (1 mark each)
1. Write the number shown by these counters:
2. Write 36 in words.
_____________________________________________
3. Subtract: 18 – 15 = ___________
4. Circle the item where we can keep water.
5. Complete correctly: 5 tens + 4 ones = _______
WHAT’S APP: +256779680288 2
6. Tell the time on the clock face below.
7. Use the number line to find the answer.
3 + 4 = _______
8. How many members does set A have.
9. Arrange the numbers from lowest to highest.
89, 29, 98, 92, 99: __________________________
10. How many rectangles can you count ?
WHAT’S APP: +256779680288 3
11. Multiply: 2 x 3 = _________
12. Write the number shown on the abacus.
13. Find the missing number: _____ + 5 = 9
14. What is the place value of 6 in 69 ?
_________________________________________________
15. Name the day of the week that comes before
Friday.
_______________________________________________
16. Write the missing number:
59, 58, _____, 56, 55.
WHAT’S APP: +256779680288 4
17. Who is shorter ?
18. Draw 12 objects in the enclosure given below.
19. Write the number that comes after 74.
20. Write 64 in expanded form.
SECTION B (2 marks each)
21. Study the picture and answer the questions that
follow.
(a) Write the statement for the picture above:
______ x ______ = ______
WHAT’S APP: +256779680288 5
(b) How many oranges are in each basket ?
_______________________________________________
(c) How many oranges are in the baskets altogether ?
_______________________________________________
(d) A man has 5 bags. Each bag contains 4 apples.
How many apples are in the 5 bags altogether ?
_________________________________________________
22(a) Name the shapes below.
(b) Draw the following below.
WHAT’S APP: +256779680288 6
23. Match set N with set M.
24. Add:
(a) 36 + 11
(b) 1 7 (c) 5 0
+ 2 + 2 4
(d) Mary has 23 sweets. Ann has 53 sweets, How many
sweets do the two girls have altogether?
_________________________________________________
25. Fill in the missing numbers.
(a) _____ + _____ = 13 (b) ____ x _____ = 8
(c) _____ – _____ = 5 (d) 0 + ______ = 7
WHAT’S APP: +256779680288 7
26. Complete the puzzle below.
27. Write “Yes” or “No” to fill the gaps.
(a) triangle has five sides. ____________
(b) Seven plus zero equals nine. _____________
(c) A square is made of straight lines. _____________
(d) Nine minus five equals thirteen. _____________
28. Subtract:
(a) 27 – 27 = ___________
(b) 5 7 (b) 8 9
– 5 – 2 3
(d) A boy picked 58 oranges. 24 oranges were green
and the rest were yellow. How yellow oranges did the
boy pick ?
_________________________________________________
WHAT’S APP: +256779680288 8
29. Use +, – , x or to fill the gaps.
(a) A set of boys with 8 legs each. _______________
(b) 6 _______ 2 = 4 (c) 9 ______ 5 = 4
(d) 3 _____ 0 = 3
30. The graphs shows the heap of apples Joel sold.
(a) How many apples were in each heap ?
_________________________________________________
(b) How many heaps did Joel sell on Tuesday ?
_________________________________________________
(c) On which day did Joel sell the highest number of
apples ? _____________________________________
(d) How many apples did Joel sell on Thursday ?
_________________________________________________
***END***
</passage>
</passages>

Your previous outline was rejected because it does not follow the school's schemes of work and the required topics for this term:
- only 0 of 29 teaching lessons cite the school's schemes of work; they must follow the schemes' topics, subtopics and order (cite their passages)
Redo the WHOLE outline from the school's schemes of work (their topics, subtopics and order, citing their passages), adding any missing NCDC topic.

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
