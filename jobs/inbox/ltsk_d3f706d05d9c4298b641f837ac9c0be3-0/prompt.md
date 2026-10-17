# Job ltsk_d3f706d05d9c4298b641f837ac9c0be3-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for English, Primary One 2026, Term 3.
The term has 10 teaching weeks and this subject has 7 periods per week. Every lesson is ONE 40-minute period, so keep each lesson small enough to teach in 40 minutes.
Ledgerly reserves the last lesson of each week for a review of that week.
Give at most 60 teaching/practice lesson entries in teaching order (the last lesson of the term is the end of term assessment).
Each lesson has a kind: "teach" (new content) or "practice" (the same subtopic as the teaching lesson just before it: exercises, oral work, drawing, matching, filling in blanks, ALL taken from the passages).
When the material is thin (common in lower primary), follow each teaching lesson with a practice lesson. Split big subtopics over several teaching lessons.
Never pad with content the passages do not have: if they cannot fill the term, return fewer lessons and list what is missing in gaps. Ledgerly fills the remaining weeks with revision.
You are composing the SCHOOL'S OWN scheme. The passages below (the official NCDC curriculum and guides, plus schemes of work, lesson plans, notes and past papers from the school e-library) are reference material:
The school's SCHEMES OF WORK for this class and term ("P 1 English Comprehension Scheme Of Work Term III", "P I English Grammar , Composition & Comprehension Scheme OF Work Term III") are the BASE: follow the topics, subtopics and week-by-week order they agree on. Every topic they list for this term MUST become a unit, in their order, and their subtopics become the lessons, with about the pacing they give. Cite their passages in sourcePassageIds of every lesson that follows them.
The NCDC documents (titles starting "NCDC") only FILL GAPS: a topic NCDC lists for this term that the schemes lack gets its own unit where it fits best. Never drop or rename a schemes-of-work topic to fit NCDC. NCDC lower-primary thematic curricula list every learning area side by side in table columns separated by " | ": take only the English column.
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

<passage id="lchk_ff7da0e0a6d4466fab01a6c633e4ad9a" source="P 1 English Comprehension Scheme Of Work Term III" part="1">
ENGLISH COMPREHENSION SCHEME OF WORK FOR P.1 THIRD TERM
W
K
P
D
THEM
E
SUB
THEME
CONTENT COMPETENCES METHODS/
TECHNIQU
ES
L/ACTIVITY IND. OF
L.SKILLS &
VALUES
L/AIDS REF RE
M
1 1 OUR
TRANS
PORT
Rhyme
in
relation
to
transpor
t
The Traffic Light
Stop says the red light.
Go says the green.
Get set the amber one.
Blinking in between.
That’s what they say.
And that’s what they mean.
All must obey them.
Even the queen
The learner;
- reads and writes the
rhyme correctly.
- answers oral and written
questions.
discussion
explanation
recitation
reciting the
rhyme
answering
oral and
written
question
fluency
articulation
effective
communica
tion
Chalkb
oard
illustrati
on
Monitor
English
Course
book 1
page 68
2 A story
related
to
transpor
t
MY FATHER
My father was driving a…… As he
was driving, we saw a-----moving
on rails. The bus by passed us
driving very fast. My father drove
up to Airport. (train, driver car,
Entebbe)
The learner;
- reads the story carefully.
- tells the missing words
according to given list.
- fills in the missing words
to complete a meaningful
story.
observation
explanation
question
and answer
reading the
story
filling the
missing
words in the
story
effective
communica
tion
fluency
self esteem
Chalkb
oard
illustrati
on
Teachers
collection
2 1 OUR
TRANS
PORT
Speech
exercise
and
tongue
twister
Travellers travelling to Toronto
travelled with travellers travelling
to different countries.
Mark the carpenter parked his car
at the far car park.
The learner;
-makes different sounds
imitating the teacher and
animal sounds.
-pronounces words
correctly.
imitation
recitation
story telling
explanation
telling
stories
reciting
tongue
twisters
fluency
articulation
self esteem
Chalkb
oard
illustrati
on
Mk
Precise
page 80
-recites tongue twisters
correctly.
question and
answer
2 A story
related
to
measure
s and
transpor
t
MY HOME
My home is near Mbale town.
There is a big tree near my home.
I go to study at Aloi Primary
School. My home is far away from
my school. I use a lorry to go to
school. It is very fast. It takes me a
few minutes to reach school.
The learner;
- reads the story correctly.
- explains new words in
the story correctly.
- answers oral and written
questions about the story.
explanation
discussion
question
and answer
story telling
reading the
story
answering
oral and
written
question
articulation
verbal and
non verbal
logical
thinking
Chalkb
oard
illustrati
on
Thematic
curriculum
Trs guide
page 357
3 1 OUR
TRANS
PORT
A
substitut
ion table
about
past
tense
A substitution table about the past
tense
The learner;
- reads the words
correctly.
- constructs oral and
written sentences in past
tense.
discussion
explanation
reading the
words
correctly
makes good
sentences
from the
table
articulation
creative
and critical
thinking
Chalkb
oard
illustrati
on
MK Pupils
book
standard 2
page 133
2 A
dialogue
about
measure
s
A dialogue
Nathan: Good morning Susan.
Suzan: Good morning Nathan.
Nathan: Where do you live?
Suzan: I live at Gayaza.
Nathan: What do you use when
coming to school?
Suzan: I use a car.
Nathan : I like using a motor cycle
because I stay near the school.
Suzan: Oh! That is good.
The learner;
- reads the dialogue.
- answers oral and written
questions.
discussion
explanation
question
and answer
answering
the
questions
acting the
dialogue
articulation
fluency
self esteem
Chalkb
oard
illustrati
on
Teachers
collection
4 1 OUR
TRANS
PORT
A rhyme
about
travellin
g
Rhyme
Travelling is good
by road by air
by water by rail
</passage>

<passage id="lchk_b4d3b58a64c44079b56622075ebfe9d9" source="P I English Grammar , Composition & Comprehension Scheme OF Work Term III" part="1">
1
TERM III – PRIMARY ONE ENGLISH
SCHEME OF WORK
2
GRAMMAR SCHEME OF WORK FOR PRIMARY ONE TERM III
W
K
D
P
THEME SUB-
THEME
CONTENT COMPETENCES METHODS ACTIVITIES L/AIDS REF REMARK
S
1 Our
transport
Types &
means of
transpor
t
Plurals
Plural means many
Nouns with letter ( s)
Examples
car – cars
road – roads
bicycle – bicycles
boat – boats
train – trains
ship – ships
pencil – pencils
pen – pens
ball – balls
bag – bags
pot – pots
toy – toys
doll – dolls
basket – baskets
- Reading the words
correctly
- Spelling and
writing answers
and the words
correctly
- Reading the words
correctly
- Spelling and
writing the words
correctly.
- Question
and
answer
- Reading
- Spelling
- Writing
- Answering
- A chart
showing
plurals
which take
(s)
- Effecti
ve
commu
nicatio
n
- Critical
thinkin
g
-
2 Plurals
Nouns which take ( es)
bus – buses
mango – mangoes
bench – benches
church – churches
- Reading the words
correctly
- Spelling and
writing the words
correctly
- Question
and
answer
- Reading
- Spelling
- Writing
- answering
- A chart
showing
plurals
which
takes (es)
- Effecti
ve
commu
nicatio
n
- Critical
thinkin
g
-
3
3 Plurals
Nouns which take ( ies)
Examples
lorry – lorries
baby – babies
lady – ladies
body – bodies
- - Look and
say
- Question
and
answer
- Reading
- Spelling
- Writing
- answering
- a chart
showing
plurals
ehich
takes (ies)
- critical
thinkin
g
- effectiv
e
commu
nicatio
n
-
1
Plurals
Nouns which take ( ves)
Examples
knife – knives
leaf – leaves
loaf – loaves
Plurals which change vowels
Examples
man – men
woman – women
tooth – teeth
foot – feet
goose – geese
- Reading the words
correctly.
- Spelling and
writing the words
correctly.
- Differentiating the
nouns which
change completely
- Look, say
and use
- Question
and
answer
- Reading
- Spelling
- Writing
- Answering
- A chart
showing
these
nouns
which take
( ves) and
those
which
change
completel
y
- Creativ
e
thinkin
g
- Effecti
ve
commu
nicatio
n
- Critical
thinkin
g
-
4
2 Nouns
Nouns which remain the same in
singular ( one) and plural (
many)
One many
sheep sheep
furniture furniture
luggage luggage
money money
firewood firewood
- - - - - -
3 Pronouns
A pronoun is a word used instead
of a noun .
Examples
He is used for (male)
Boy and man
She is used for (female)
Woman and girl
Anita is a girl.
She is a girl.
Deo is a boy
He is a boy.
Other pronouns like
We, they, I, it etc
- Reads the words
and sentences
correctly
- Identifies the
pronouns correctly
- Answers correctly
the given activity
- Guided
discussio
n
- Explanati
on
- Chalk board
- illustration
- reading
- writing
- self
awaren
ess
- effectiv
e
commu
nicatio
n
- critical
thinkin
g
-
5
1 Our
transport
Means of
transport
Tenses
Everyday tense
We add S, ies to the verb
when we are in singular but
the verb remains when we are
in plural.
e.g
- She goes to school
everyday. (go)
- Sarah washes her uniform
everyday. (wash)
- They eat food everyday.
(eat)
Children play good games
everyday.(play)
- Reading sentences
correctly
- Changing the verbs
correctly
- Guided
discovery
- Reading
- Spelling
- Writing
- A chart
showing
everyday
tense
- -
2 Yesterday tense ( past tense )
Verb yesterday tense
pray prayed
play played
read read
stop stopped
give gave
write wrote
take took
- Reads the words
correctly
- Changes the given
verbs into yesterday
tense correctly
- Attempts the given
activity correctly
- Guided
discussio
n
- Explanati
on
- Whole
word
- A chart
showing the
yesterday
tense
- Reading
- Spelling
- Writing
- Effecti
ve
commu
nicatio
</passage>

<passage id="lchk_9165db1c36eb45b2a8432062e4285ab1" source="P I English Grammar , Composition & Comprehension Scheme OF Work Term III" part="9">
the rhyme.
- Recitati
on
- Questio
n and
answer
- Reading
- Writing
- Reciting
- Confiden
ce
- Fluency
- Self
awarenes
s
- -
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

<passage id="lchk_4d3bb157950f4b09a1125a012931b17a" source="P 1 English And Comprehension Notes Term 3" part="1">
For more lesson notes, visit www.freshteacheruganda.com
PRIMARY ONE ENGLISH LESSON NOTES TERM III
Week 1&2
Holiday work
Week 3
THEME: TRANSPORT
Lesson 1
Arrange these words to make a meaningful sentence.
1. flying is The over the plane.
2. driving is a car The woman.
3. is The ship sailing on the lake.
4. big is airport The very.
5. station is the train at The.
6. aeroplane Where is the ?
Lesson 2
Read the conversation and answer the questions that
follow.
Sarah: Good morning, Peter ? Our friend Jacob didn’t
For more lesson notes, visit www.freshteacheruganda.com
come to school today.
Peter: Why ? What happened ?
Sarah: He fell off the bicycle.
Peter: Oh, how did it happen ?
Sarah: He was riding down the hill when the bicycle
got a flat tyre.
Peter: You mean a flat tyre can cause an accident ?
Sarah: Oh yes, especially if you are driving at a high
speed.
Questions:
1. How many people are in the conversation ?
__________________________________________
2. Why didn’t Jacob come to school ?
___________________________________________
3. What caused the accident ?
__________________________________________
4. Who are the people talking in the conversation ?
___________________ ___________________
Week4
Lesson1
Guided composition related to transport
aeroplanes, taxis, buses, bus park,
ships, helicopters, railway station,
lorries,
There are many things we use for transport. Some of
them are bicycles, _______________ and _____________.
We use ____________ to move on water. _______________
and ______________ are used for air transport. Buses
For more lesson notes, visit www.freshteacheruganda.com
collect at the____________ and we catch the train at
the __________________.
Lesson 2&3
Comprehension passage about transport.
Transport is the movement of people and their goods
from one place to another. The four types of transport
are; air transport, water transport, road transport and
railway transport. The commonest type of transport is
road transport. Air transport is the quickest type of
transport. A pilot flies an aeroplane.
Questions:
1. What is transport ?
2. Name the four types of transport.
a)____________ b)______________ c)_____________
d)___________
3. Why is air transport the best type of transport ?
_______________________________________________
4. Which type of transport is commonly used ?
________________________________________________
5. How do we call a person who flies an aeroplane ?
____________________________________________
Week 5
Lesson 4
Picture interpretation related to transport. (Monitor
English course bk 3 pg 43- 46)
a. The taxis are at a taxi park.
b. The buses are not at the bus park.
For more lesson notes, visit www.freshteacheruganda.com
c. The train is not at the railway station
d. The aeroplane is at the airport.
e. The lorry is carrying cows.
f. The ship is sailing on the lake.
Lesson 5&6
Comprehension passage about means of transport.
Rose had an uncle who lived in Nairobi. One day, he
invited Rose to Nairobi. She was escorted to the airport
by her mother and father. At the airport, she saw many
aeroplanes kept in the hangar . In the aeroplane, she
saw a pilot and an air hostess. When Rose reached
Nairobi, she visited the railway station where she had a
ride on the train. Her aunt and uncle took her to a sea
port at Mombasa. She saw many ships, boats, ferries
and rafts. She picked some shells that she brought to
her parents.
Questions:
1. Who lived in Nairobi ?
2. Who escorted Rose to the airport ?
</passage>

<passage id="lchk_d23a32b43174471a9c36acbfa6a81ae7" source="P 1 English Notes 2016" part="24">
7. Doubling the last letter add(ed)
8. Use of a comma
9. Use of a capital letters
10. Short forms for days of the week
11. Short forms for months of the year
12. Opposites
13. Adjectives
14. Comparing adjectives
15. Pronouns
16. Past tense of adding ‘d’
17. Past tense of adding ‘ed’
18. Past tense of adding ‘ied’
19. Present simple tense of adding ‘s’
20. Present simple tense of adding ‘ies’
GCSS NOTES 2016 Page 86
21. Do or does
TERM III TOPICAL BREAKDOWN FOR ENGLISH 2016 PRIMARY ONE
Theme 1: Our transport
1. Vocabulary: Types of transport (road, air, water, railway)
Structures: What is this / that………?
Where is the ………….?
2. Vocabulary: Means of transport (road – car, bus, bicycle etc and Air – aeroplane
Structures: Is this a car? Yes/ No it is……….
3. Vocabulary: far , near, heavy, light
Structures: The ……………is heavier than a ……………..
Is it far/ near?
Theme 2: Things we make
1. Vocabulary: (examples of things we make) balls, ropes, baskets
Structures : Are these……….?
Can you make a ………….?
2. Vocabulary: (Things used to make crafts) banana fibres, papyrus, clay
Structures: What do you use to make…………..?
3. Vocabulary: (Where we get things used to make crafts) swamps, plants etc
Structures: Where do we get………?
Theme 3: Our environment
1. Vocabulary: (animals found in the environment) cow, goat, sheep etc
Structures: Is this a …………?
2. Vocabulary: (plants found in the environment pawpaw, mango, orange
Structures: Is this a………..?
Theme 4: Peace and security
1. Vocabulary: (fight, fire, like, hate, play, pray, share)
Structures: What do you like/ hate…………?
2. Vocabulary: (gun, spear, knife, needle, stone, stick)
Structures: Do you have a……….
What is this?
3. Vocabulary: (peace, love, safe, share, play, talk) What are they doing?
Structures: dialogue
4. Vocabulary: (policeman/ woman, teacher, elder, soldier)
GCSS NOTES 2016 Page 87
Structures : What can you see?
5. What is she/he?
1. And
2. But
3. Similes
4. Because
5. Group names
6. Collective nouns
7. Use of a comma
8. Use of a question mark
9. Past tense
10. Plurals (man – men)
11. Synonyms
12. Analogies
13. Homophones
14. Things we make
15. Gender
16. Comparing adjectives
17. Apostrophe
18. Short forms using an apostrophe
</passage>

<passage id="lchk_45833300cc6d4b9f98ebccea3f00d8a6" source="English Language Paper 1 (112/1) Holiday Package 1 – UCE Composition Practice" part="1">
PRACTICE MAKES PERFECT MY EFFORT MY FURURE Page 1
112/1
ENGLISH
LANGUAGE
PAPER 1
2HRS
Uganda Certificate of Education
ENGLISH LANGUAGE
PAPER 1
INSTRUCTIONS TO CANDIDATES:
 This paper has two sections: Section A and Section B.
 Answer ALL questions in all.
 Answer question one (1) in Section A (compulsory) and ALL other question
in Section B.
HOLIDAY PACKAGE 1
PRACTICE MAKES PERFECT MY EFFORT MY FURURE Page 2
SECTION A
1. You are a candidate whose guardian is severely sick of Covid-19 disease
and cannot support the family anymore. Write a letter to your nephew
who stays abroad informing him of the condition/situation at home.
You may use the following;
 Pain your guardian is going through
 Insufficient finances
 School closed
 No food
 The house helper ran away
 The home is in the road reserve
 You are scared of your security.
SECTION B
For each of the following topics and write a composition of
500 – 600words.
2. Write a story beginning “I was ushered into a pitch-dark room….”
3. “Girl –students should be allowed to wear skimpy school uniform
skirts.” Do you agree?
4. Write a story based on the saying; “Birds of a feather flock together”
5. “Co-curricular activities are essential in Schools.” Discuss.
6. Write a story ending “…. I sighed with relief when the baby came
crawling with a mobile phone.”
**** END ****
</passage>

<passage id="lchk_1b13c587235d4ba58fc3874a35a0180a" source="UCE English Language Paper 1 (112/1) Set H – Composition and Speech Writing" part="1">
112/1
English Language
Paper 1
2 hours
UGANDA CERTIFICATE OF EDUCATION
ENGLISH LANGUAGE
PAPER 1
TIME: 2 HOURS
Instructions to Candidates;
Attempt two questions
Section A is compulsory
SECTION A:
Use 250 – 300 WORDS
1. Your school is holding a campaign assembly. Imagine you are campaigning for the post
of Head prefect in your school. Write a speech you will give to the audience.
SECTION B:
Use 500 – 600 WORDS
Attempt one question from this section
2. Write a story ending …….if it had not been for the traitor, I would be a different person
altogether.
3. Discuss the uses of media in your country.
4. “People are deceitful” Write a composition based on the above statement.
5. Narrate an incident when you were discovered guilty.
6. Boxing is a sport that can cause death and thus it should be abolished” Write your
argument in support or rejection of the above statement.
7. Explain how your friendship with someone has helped you become a better person.
END
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
