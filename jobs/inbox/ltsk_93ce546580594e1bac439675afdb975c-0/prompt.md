# Job ltsk_93ce546580594e1bac439675afdb975c-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for Science, Primary One 2026, Term 3.
The term has 10 teaching weeks and this subject has 5 periods per week. Every lesson is ONE 40-minute period, so keep each lesson small enough to teach in 40 minutes.
Ledgerly reserves the last lesson of each week for a review of that week.
Give at most 40 teaching/practice lesson entries in teaching order (the last lesson of the term is the end of term assessment).
Each lesson has a kind: "teach" (new content) or "practice" (the same subtopic as the teaching lesson just before it: exercises, oral work, drawing, matching, filling in blanks, ALL taken from the passages).
When the material is thin (common in lower primary), follow each teaching lesson with a practice lesson. Split big subtopics over several teaching lessons.
Never pad with content the passages do not have: if they cannot fill the term, return fewer lessons and list what is missing in gaps. Ledgerly fills the remaining weeks with revision.
You are composing the SCHOOL'S OWN scheme. The passages below (the official NCDC curriculum and guides, plus schemes of work, lesson plans, notes and past papers from the school e-library) are reference material:
The school's SCHEMES OF WORK for this class and term ("P I Literacy Scheme OF Work Term III", "P1 Schemes Of Work") are the BASE: follow the topics, subtopics and week-by-week order they agree on. Every topic they list for this term MUST become a unit, in their order, and their subtopics become the lessons, with about the pacing they give. Cite their passages in sourcePassageIds of every lesson that follows them.
The NCDC documents (titles starting "NCDC") only FILL GAPS: a topic NCDC lists for this term that the schemes lack gets its own unit where it fits best. Never drop or rename a schemes-of-work topic to fit NCDC. NCDC lower-primary thematic curricula list every learning area side by side in table columns separated by " | ": take only the Science column.
Combine them in this authority order: the school's schemes of work for topics, sequence and pacing; NCDC for anything they miss; the strongest detailed notes for accurate teaching depth; past papers for expected applications and activities.
Use this term's part of the material (Term 3) when the passages cover several terms.

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

<passage id="lchk_addf48554d8a4d42ab505df2e7c469b1" source="P1 Curriculum" part="1">
a
Ministry of Education, Science,
Technology and Sports
The National Primary School
Curriculum for Uganda
Primary 1
Ministry of Education, Science,
Technology and Sports
The National Primary School
Curriculum for Uganda
Primary 1
ii
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
iii
iii
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

<passage id="lchk_bc264fd781ad4bb08d611f7b2f3f85f3" source="P I Literacy Scheme OF Work Term III" part="1">
TERM THREE – PRIMARY ONE
LITERACY SCHEME OF WORK
SCHEME OF WORK FOR PRIMARY ONE TERM THREE
W
K
D
P THEME SUB-
THEME
COMPETENCES CONTENT METHODS ACTIVITIES Instruction
al materials
L/SKILLS RMK
S
1 Transport Types of
transport
A learner
- Defines transport
- States the types of
transport
- Reads, spells and
pronounces words
correctly
- Draws the types of
transport
- Writes the words
correctly
Transport
- Transport is the movement of
people and goods from one
place to another.
Types of transport
There are four types of transport
- Road transport
- Water transport
- Air transport
- Railway transport
Guided
discussion
Guided
discovery
Question
and answer
- Reading
- Writing
- Spelling
- Drawing
A chart
showing
types of
transport
Self
awareness
Kobta simplified lit Bk 1 Pg 93 – 94
2 Means of
transport
- Defines water transport
- States the means of
water transport
- Reads, spells and
pronounces words
correctly.
- Draws means of water
transport.
- States people who use
water transport.
- Writes the words
correctly
Water transport (text book teaching)
This is the movement of people with their goods
on water.
It is the slowest type of transport
Means of water transport
- Boats, ferries, yacht, canoes, ships
People who use water transport
- Sailors – boat, captains – ship
- - - Critical
thinking
- Creative
thinking
- Preserve
race
3 - Defines railway
transport.
- States the means of
railway transport
- Reads, spells and
pronounces words
correctly.
- Writes correct spellings
- Draws the means of
railway transport
- States places where we
find different of
transport.
- - - - -
Kobta simplified lit Bk 1 Pg 96
1 A learner
- Defines air transport
- States the means of air
transport
- Reads, spells and
pronounces words
correctly.
- Draws means of air
transport
- States people who use
air transport
Air transport
This is the movement of
people with their goods above
water and land
It is the most expensive type of
transport
It is the quickest type if
transport
Means of air transport
- Aeroplanes
- Helicopters
- Parachutes
- Rockets
- Jet fighters
- People who fly aeroplanes are
called pilots and they’re helped
by navigators.
- People who travel in an
aeroplane are passengers.
- Ladies who work in the
aeroplane are hostess.
- Guided
discussion
- Guided
discovery
- Question
and
answer
- Reading
- Writing
- Spelling
- Drawing
- A chart
showing
means of
air
transport
- Perseveran
ce
- Appreciate
Rs them lit I Bk I pg.100Kobta simple Bk I pg 94
2 - Defines road transport
- States the means of
road transport
- Reads, spells and
pronounces words
correctly.
- Draws means of road
transport.
- States people who use
road transport
Road transport
This is the movement of
people with goods on land.
The most common type of
transport.
Types of road
- Tarmac roads
- Murram roads
Means of road transport
- Bus - bicycle
- Car - lorry
- Motorcycle - horse
- Camel - donkey
- Carts
People who use roads
transport
- Pedestrians, passengers
- Cyclists/ motorcycle
- Bicycle, riders
- Motorists, conductors
- Drivers
- Importance of a stage and its
meaning.
- - - A chart
showing
means of
road
transport
-
Rs them. Lit I Bk I pg.98Kobta simple lit Bk I pg 93
3 Road signs A learner
- Defines roads signs
- Identifies different road
signs
- Reads, spells and
pronounces words
correctly
- Draws and names road
signs
- Writes the words
correctly
Road signs
These are symbols put on
roads to guide road users.
They help in reducing traffic
and road accidents.
Examples
</passage>

<passage id="lchk_b4de5bdff6334e9db4e9022e2dc59908" source="P1 Schemes Of Work" part="1">
1
P.1 LITERACY ONE ENGLISH SCHEMES OF WORK
W
K
DA
Y
LESSO
N
THEM
E
S/THEM
E
L/AREA CONTENT COMPETEN
CES
METHODS ACTIVITY LIFE
SKILLS
AND
VALUES
MATERIAL
S
REF RE
M
1
MON 1
WEATHE
R
Types
and
elements
of
weather
News Telling/signing
news about what
they did during
the holidays
Drawing them
Naming
elements of
weather
Naming types
of weather
Story telling Telling
news
Listening
Speaking
Drawing
Effective
communicati
on
Cooperation
Story book The
National
Primary
School
Curricul
um for
Uganda
page 222
(Trs.
Guide)
2 Mathemat
ics
Counting 1-40
Adding numbers
whose
Sum is less than
20 (Vertically)
Counting
numbers 1-40
Adding
numbers
vertically
Discussion
Problem
solving
Counting
Adding
number
A wall chart
with nos. 1-
50
2
3 Literacy I Identifying and
describing
elements of
weather
Reading new
words related to
weather e.g sun,
rain, clouds, wind
Matching
pictures to words
Playing a reading
game
Identifying
and
describing
elements of
weather
Reading new
words
Watching
Listening to
stories
Identification
Discussion
Question and
answer
Identifying
Describing
Reading
Matching
Playing
games
Decision
making
Identificatio
n
Endurance
Weather
chart
Primary
School
Curricul
um for
Uganda
page 29
Literacy II Writing letter
pattern ‘u’
Writing letter ‘u’
Drawing
elements of
weather
Labelling
pictures
Writing letter
pattern
Draw and
labelling
elements of
weather
Identification
Observation
Writing
patterns
Drawing
Labelling
Weather
chart
4 English Vocabulary: sun,
rain, clouds, wind
Structures
Is it…?
Yes it is
No, it is not
Naming
elements of
weather
Naming the
types of
weather
Group work Naming
elements
and types of
weather
Self esteem
Effective
communicati
on
Creative
thinking
-do-
1 5 Creative
performin
g arts
Singing
Listening
Dancing
(movement)
Singing and
dancing
Rote method Singing
Dancing
Environmen
t
The
National
Primary
School
Curricul
um for
Uganda
page 222
TUE 1 Types of
weather
News Telling news
about weather
(wind)
Answering
questions
Story telling
Discovery
Listening
Speaking
Confidence
Creative
thinking
3
2 Mathemat
ics
Counting nos. 1-
50
Adding numbers
whose sum is less
than 20
(vertically)
Counting
numbers
Adding
numbers
Discussion
Problem
solving
Counting
Adding
Negotiation
Wall chart
(Trs.
Guide)
Primary
School
Curricul
um for
Uganda
page 29
3 Literacy I Interpreting
pictures about
weather
Reading words eg
clouds, wind etc
Reacting a rhyme
about weather
Matching word to
word
Interpreting
pictures
Reading
words and
reciting
rhymes
Matching
words to
words
Explanation
Discussion
Interpreting
Matching
3 Literacy II Writing letter
pattern “v”
Writing letter ‘v’
Writing words
like cloudy,
sunny, rainy,
windy, clouds
Drawing pictures
about weather
Writing letter
patterns
Drawing
pictures
Demonstratio
n
Observation
Writing
Drawing
4 English Vocabulary:
wind, shine, rain,
blowing, raining
Structures
It is
….(shining/rainin
g)
Yes, it is……
No, it is not….
Naming
elements of
weather
Constructing
sentences
using
different
structures
Direct
approach
Look say and
use
Naming
Constructin
g sentences
Self-
awareness
Appreciation
Endurance
Our
environmen
t
Percussion
Instruments
Weather
chart
The
National
Primary
School
Curricul
um for
Uganda
page 222
(Trs.
Guide) 5 Creative
performin
g arts
Singing
Listening
Instrumental
work
Listening
Singing
Playing
instruments
Rote method
Demonstratio
n
Listening
Singing
Playing
instruments
4
WED
1 Types
and
elements
of
weather
News Singing/telling
news on what I
did after school
Talking about
weather chart
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

<passage id="lchk_b088c4c9073c46478c9a80b544e2db7d" source="Literacy P1 Moes" part="1">
i
ii
iii
iv
v
vi
1
HOME-STUDY MATERIAL
LITERACY ONE
PRIMARY ONE
2
OUR SCHOOL
PEOPLE IN OUR SCHOOL
LESSON ONE
Dear learner, in this lesson we are going discuss the people found in the school.
What can you see in the picture?
Read words
teacher head teacher schoolboy schoolgirl
Read letters
Draw the picture
teacher head teacher schoolgirl schoolboy
Practise writing
AAA A
AA
Ateacher
A A A
A A A
A A A
My name is ____________________________________
3
PEOPLE IN OUR SCHOOL
LESSON 2
Dear learner in this lesson we are going to see more people found at school.
What can see in the picture?
Read words
cook guard bursar nurse
Read letters
Draw these pictures
askari bursar cook nurse
a a a
a a a
a a a
4
Practice writing the letters
A A
a a
askari
My name is
___________________________________________________
5
THINGS IN OUR SCHOOL
LESSON 3
In this lesson you are going to see things in the classroom
What can you see in the picture?
Read these words
table chair desk blackboard
Build some words
as, _______________
Draw the pictures
table chair blackboard book
s a a
a s s
a s s
6
Practise writing
S S
s s
school
My name is
__________________________________________________
7
THINGS IN OUR SCHOOL
LESSON 4
Dear learner in this lesson we are going to see more things found in the
classroom.
What can you see in the picture?
Read these words bell flag gate uniform
Read words
bag, ____________ , _________________
Draw the things found at school
bell flag gate ball
b a s
a s a
g a s
8
Practice writing
B B
bb
bell ball
9
ACTIVITIES IN OUR SCHOOL
LESSON 5
In this lesson we are going to see different activities at school.
What are they doing?
Read these words
reading sweeping writing playing
Build words
at, ________________, __________________
t a t
a t a
s a t
10
Read the story
Kato goes to Kira Primary school. Kato is in P 1. His teacher is Miss Kumi. She teaches
reading. Kato loves Miss Kumi.
Draw activities in Kato’s school
A boy sweeping A girl reading A boy writing Children playing
Practise writing
T T
t t
teacher
11
Read and draw
People at school
teacher head teacher guard
Things at school
ball chair flag
Activities at
school
sweeping playing reading
Practise writing the letters and words
A aaskari
B b bell
S sschool
T t teacher
12
OUR HOME
PEOPLE IN OUR HOME
LESSON 1
Dear learner, in this lesson we will see the people at home.
What can you see in the picture?
Read these words
father mother brother sister
Build words
fat, _________________, ____________
Draw the picture
mother father sister brother
f a t
a t a
t a t
13
Practise writing
F F
ff
father
My name is_________________________________________________
14
ROLES ANDRESPONSIBILITIES OF FAMILY MEMBERS
PEOPLE AT HOME
LESSON 2
Dear learnerwe are going to see responsibilities of family members
What can you see in the picture?
Read these words
milking cooking winnowing digging
Build words
at, _______________ , ________________
What is she doing?
She is cooking.
…………………………………
…………………………………
m a t
a t a
t a t
15
…………………………………
Practise writing
M M
m m
milking
My name is
___________________________________________________
16
THINGS FOUND IN OUR HOME
LESSON 3
Dear learner, in this lesson we will see things found at home.
What can you see in the picture?
Read these words
pot plate knife cup
Build words
pot, ________________, ________________
Draw the picture
pot fork spoon knife
Practise writing
P P
p p
potplate
p o t
a t a
t a p
17
THINGS IN OUR HOME
LESSON 4
</passage>

<passage id="lchk_ee4a226977d645bc9f51e8335564196c" source="P 1 Literacy All Terms Notes" part="16">
a) are the things around us.
b) Mention any two things plants give us.
c) Where do we get fish from?
d) Why do people live in houses?
TEST FOUR 1. Make words
y ……………………
ip ……………………
ain …………………..
2. Re-write the words correctly
a) ntpla
b) mentronenvi
For more lesson notes, visit www.freshteacheruganda.com
c) kela
For more lesson notes, visit www.freshteacheruganda.com
3. Answer correctly
a) Are these leaves?
………………………………………………………………
b) What are these?
…………………………………………………………..
c) Is this a flower?
…………………………………………………………….
4. Make sentences using these words
a) animal …………………………………..
b) river ……………………………………
c) book ……………………………………
5. Fill in the gaps correctly
The .............................................. hold the plant firmly in the soil.
The ……………….takes water from the roots to the branches. The
………………….make food for the plant. They also help the plant to
breathe. We can make juice from ……………………..
6. W rite two words for sound ‘tion’
7. Answer correctly
a) A............................... treats sick people.
b) A policeman keeps law and ……………………
c) Our teachers and prefects provide peace and security at ………
tr
For more lesson notes, visit www.freshteacheruganda.com
8. Underline words with sound ‘oa’
beef goat cow road
tree bus coat pencil
</passage>

<passage id="lchk_8b8dda24371942b78a7e9842bec435a0" source="P 1 Literacy Term 3 Notes" part="5">
10. very donkey A ears long has.
Activity: Reading and re-arranging words to form
meaningful sentences.
For more lesson notes, visit www.freshteacheruganda.com
LESSON: 3 & 4
Free composition writing about things we make.
Guiding words:(mats, ropes, clay, weaving, modeling,
palms, pots etc...)
LESSON:5 & 6
THEME: PEACE AND SECURITY AT HOME.
SUB-THEME: PEACE AND SECURITY
What is environment?
Environment is the
Letter writing(A friendly letter)
GREENHILL ACADEMY,
P.O.BOX 7490,
KAMPALA .
DATE: 4 th September, 2013.
Dear Timothy,
How are you? I hope you arrived safely. Thank you for the
present of a toy train you gave me on my birthday.
I enjoyed playing with it. I will give you a present on your
birthday too.
For more lesson notes, visit www.freshteacheruganda.com
Have a lovely day.
For more lesson notes, visit www.freshteacheruganda.com
Yours, Simon Wadada.
Questions
1. Who wrote this letter?
2. To whom was the letter written?
3. What did Jane give Mary?
4. When was the letter written?
5. To which school does Mary go to?
Activity:
a.Reading the letter, answering oral and written
questions.
b.Pupils will write a letter of their own.
WEEK: 10
LESSON: 1 & 2
Free composition writing about uses of water.
Guiding words:[drinking, bathing, cooking, washing,
clean water, boiled, safe]
</passage>

<passage id="lchk_11a69188f0c9439e8ca348c8fc3b15b2" source="P 1 Literacy 1" part="5">
Topic 2: THINGS WE MAKE
www.tekartlearning.com ©Tekart Learning Revision Books
7. Write any two materials used for playing with.
a. ______________________
b. ______________________
8. Pots are made by
_________________________________________
9. Name these things we make.
10. What does the name Emmanuel mean?
___________________________________________________
11. Where do we find these holy symbols?
________________________
________________________
www.tekartlearning.com ©Tekart Learning Revision Books
1. What is environment?
___________________________________________________
2. Mention any two components of the environment.
______________________ _______________________
3. Things that have life are called.
____________________________
4. List two examples of non-living things.
________________________
________________________
5. Write any two things living things do.
___________________________________________________
__________________________________________________
6. Name the two groups of living things.
__________________________
__________________________
7. Draw these examples of plants.
sugarcane plant banana plant
8. How do we call plants which bear flowers?
___________________________________________________
9. Give any two uses of plants to us.
___________________________________________________
Topic 3: OUR ENVIRONMENT
www.tekartlearning.com ©Tekart Learning Revision Books
__________________________________________________
10. Name the main parts of a plant.
a a ______________
b ______________
b b c ______________
c
11. Name these animals
12. Mention any two sources of water.
____________________
____________________
13. How is water useful to us? (Give two reasons)
___________________________________________________
___________________________________________________
14. Tick activities that spoil the environment.
a) Cleaning the compound
b) Cutting down trees
c) Watering plants
www.tekartlearning.com ©Tekart Learning Revision Books
1. ________________is living in harmony without fighting and
quarrelling with one another.
2. Write any two factors that promote peace and security at
home.
i) ____________________________
ii) ____________________________
3. Draw these people who promote peace and security at
home.
4. Underline the causes of insecurity at home.
a) Fighting
b) Playing with one another
c) Stealing
5. Mention any two factors that promote peace and security at
school.
____________________________
____________________________
6. Name any two people who promote peace and security at
school.
________________________
______________________
7. Write out two causes of insecurity at school.
i) Sharing ii) fighting iii) playing together
iv) not respecting teachers.
________________________________________
________________________________________
Topic 4: PEACE AND SECURITY
www.tekartlearning.com ©Tekart Learning Revision Books
8. Write true or false .
a) Guards promote peace and security at school __________
b) Fighting is good. ____________
c) It is good to listen to our teachers and elders.
__________
9. Give two examples of people who promote peace and
security in our community.
____________________
____________________
10. ____________________is living with protection and freedom
with one another.
11. Tick the causes of insecurity in our community.
a) Quarrelling with one another.
b) Sharing with others.
c) listening to our teachers and elders.
12. How can we prevent insecurity in our community?
(Give two ways)
i)
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
