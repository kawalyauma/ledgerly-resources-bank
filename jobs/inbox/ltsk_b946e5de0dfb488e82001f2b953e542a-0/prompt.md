# Job ltsk_b946e5de0dfb488e82001f2b953e542a-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for English, Primary Four 2026, Term 3.
The term has 10 teaching weeks and this subject has 6 periods per week. Every lesson is ONE 40-minute period, so keep each lesson small enough to teach in 40 minutes.
There are no weekly review lessons: the subject has a lot of content, so every period teaches or practises.
Give at most 59 teaching/practice lesson entries in teaching order (the last lesson of the term is the end of term assessment).
Each lesson has a kind: "teach" (new content) or "practice" (the same subtopic as the teaching lesson just before it: exercises, oral work, drawing, matching, filling in blanks, ALL taken from the passages).
When the material is thin (common in lower primary), follow each teaching lesson with a practice lesson. Split big subtopics over several teaching lessons.
Never pad with content the passages do not have: if they cannot fill the term, return fewer lessons and list what is missing in gaps. Ledgerly fills the remaining weeks with revision.
You are composing the SCHOOL'S OWN scheme. The passages below (the official NCDC curriculum and guides, plus schemes of work, lesson plans, notes and past papers from the school e-library) are reference material:
The school's SCHEMES OF WORK for this class and term ("P 4 Composition AND Comprehension Scheme Term III", "P 4 Composition Scheme", "P 4 ENG Grammar Scheme 2023", "P 4 Grammar Scheme Term III") are the BASE: follow the topics, subtopics and week-by-week order they agree on. Every topic they list for this term MUST become a unit, in their order, and their subtopics become the lessons, with about the pacing they give. Cite their passages in sourcePassageIds of every lesson that follows them.
The NCDC documents (titles starting "NCDC") only FILL GAPS: a topic NCDC lists for this term that the schemes lack gets its own unit where it fits best. Never drop or rename a schemes-of-work topic to fit NCDC. NCDC lower-primary thematic curricula list every learning area side by side in table columns separated by " | ": take only the English column.
Combine them in this authority order: the school's schemes of work for topics, sequence and pacing; NCDC for anything they miss; the strongest detailed notes for accurate teaching depth; past papers for expected applications and activities.
Use this term's part of the material (Term 3) when the passages cover several terms.

NCDC topics for Primary Four 2026, Term 3 that must ALSO be covered. Each needs at least one unit whose title or theme names it; the school's schemes of work decide where it goes and how many lessons it gets:
  8. DEMOCRACY
Do NOT write lesson content yet. Each unit and lesson must cite the passage ids it comes from in sourcePassageIds.

Reply shape:
{"title":string,"summary":string,"units":[{"title":string,"theme":string|null,"weekFrom":int|null,"weekTo":int|null,"competences":string|null,"sourcePassageIds":[string],"lessons":[{"title":string,"subtopic":string|null,"kind":"teach"|"practice","objectives":[string],"sourcePassageIds":[string]}]}],"gaps":[string]}

<passages>
<passage id="lchk_3fd760de2ed34af39fd3f1cc3f1aa998" source="NCDC P4 ENGLISH SYLLABUS" part="1">
THE REPUBLIC OF UGANDA

Ministry of Education and Sports

ENGLISH
SYLLABUS
Primary Four

National Curriculum Development Centre,
P.O. Box 7002,
Kampala - Uganda

2010

THE REPUBLIC OF UGANDA

Ministry of Education and Sports

ENGLISH
SYLLABUS
Primary Four

National Curriculum Development Centre,
P.O. Box 7002,
Kampala - Uganda
2010

NATIONAL CURRICULUM DEVELOPMENT CENTRE (NCDC) UGANDA 2009

COPYRIGHT © NCDC, 2010.
BOX 7002, KYAMBOGO, KAMPALA
KAMPALA- UGANDA
URL. www.ncdc.go.ug

ALL rights reserved. No part of this syllabus should be reproduced stored in a retrieval system or transmitted in any form by any means
electronic, mechanical, photocopying, recording or otherwise without the permission of the authors and publisher. No patent liability is
assumed with respect to the use of the information contained herein.

ISBN 978-9970-117-43-7

Published by:
National Curriculum Development Centre

Table of Content
Acknowledgement ....................................................................................................................................................................................... iv
FOREWORD .................................................................................................................................................................................................. v
Background to English Syllabus ................................................................................................................................................................ vi
Teaching Procedures ................................................................................................................................................................................ viii
SCOPE AND SEQUENCE ............................................................................................................................................................................. 1
TERM I ........................................................................................................................................................................................................... 1
TOPIC 1: DESCRIBING PEOPLE AND OBJECTS 22 PERIODS ................................................................................................................ 1
Sub-topic 1 A: Describing People ................................................................................................................................................................. 2
Sub-Topic 1.B: Describing Objects............................................................................................................................................................... 3
TOPIC 2: GIVING DIRECTIONS .................................................................................................................................................................. 4
Sub–Topic: Directing People to Places ........................................................................................................................................................ 5
TOPIC 3. WHAT I LIKE AND HOW I FEEL .................................................................................................................................................. 7
Sub-Topic 3A: What I like ............................................................................................................................................................................. 8
</passage>

<passage id="lchk_444f98e993b247748333f43dbd7add27" source="NCDC P4 ENGLISH SYLLABUS" part="2">
Sub-Topic 3B: How I Feel ............................................................................................................................................................................ 8
TERM II .......................................................................................................................................................................................................... 9
TOPIC 4: BEHAVIOUR ................................................................................................................................................................................ 9
SUB TOPIC 4.A: GOOD BEHAVIOUR 9 LESSONS .................................................................................................................................. 10
Sub–Topic 4. B Bad Behaviour .................................................................................................................................................................. 12
SUB-TOPIC 5.A: BUYING AND SELLING ................................................................................................................................................. 14
TOPIC 6: TIME ........................................................................................................................................................................................... 15
Sub-topic 6.A Past Simple Tense 14 Lessons............................................................................................................................................ 17
Sub – Topic: 6.B Past continuous tense 9 Lessons ................................................................................................................................... 17
TERM III ....................................................................................................................................................................................................... 18
TOPIC 7: EXPRESSION OF THE FUTURE ............................................................................................................................................. 18
Sub-topic 7.A: Expression of the future ...................................................................................................................................................... 19
Sub-topic 7.B: Keeping a diary ................................................................................................................................................................... 20
Sub-topic 7.C: Using study time ................................................................................................................................................................. 20
TOPIC 8: DEMOCRACY ............................................................................................................................................................................ 21
SUB-TOPIC 8.1: GAMES AND SPORTS ................................................................................................................................................... 22
SUB – TOPIC 8.2: MUSIC, DANCE AND DRAMA..................................................................................................................................... 23
SUB-TOPIC 8.3: ELECTIONS ................................................................................................................................................................... 24

ŝŝŝ | iii

Acknowledgement
</passage>

<passage id="lchk_cbb17378b9d847eb9a822635040ce304" source="NCDC P4 ENGLISH SYLLABUS" part="16">
Subject competences | Content | Suggested activities
• | Using vocabulary and structures to
The learner: | Vocabulary: | describe given music events
• Describes a given music | sing, recite, conductor, costume, actor, actress, festival, | • | Reading short texts related to music,
festival. | rhyme, instruments, drama, best, worst, choir, concert, | dance and drama.
• Acts in a given play.
• Spells selected words | • | Writing guided compositions on given
Grammar.
correctly. | events.
• The use of superlatives
• Composes simple songs | • | Reading and reciting simple poems
using vocabulary learnt | and rhymes.
• Reads simple texts related | Language Structures
• .... when …… | • | Writing short texts related to music, dance
to music events
• Reads short poems or | e.g. She sang the best song Which …. will …… | and drama.
plays. | • E.g. which song will Daudi sing?
• Writes simple short texts

ϮϯNational Curriculum Development Centre
P4 English Syllabus, | 23

SUB-TOPIC 8.3: ELECTIONS

Subject competences | Content | Suggested activities
• | Uses appropriate | • | Using appropriate vocabulary and
language in convincing | Vocabulary | structures accurately.
others. | • | prefect, vote, voter, ballot paper, head girl, head | • | Asking and answering questions
• | Conducts simple | boy, elect, monitor, candidate, election, stand, leader,
dialogues | • | Role playing electing school prefects.
rig, post, captain., campaign. | • | Conducting conversations
• | Narrates simple stories
• | Responds to instructions | • | Narrating simple stories about elections.
• | Reads simple texts. | Grammar | • | Reading short simple texts related to
• | Reads and interprets | • The use relative pronouns who and whom. | elections.
simple posters related | • | Reading and interpreting posters with
Language Structures
to elections | campaign messages
Reads simple data related | • …… who ……
• | • | Writing guided composition.
E.g. John is the boy who won the post of head boy.
to elections | • | Reading and interpreting data
• ………/are electing ……. as the ……
• | Illustrates election | • | related to elections.
E.g. We are electing Nambawa as the head-girl.
activities | • | Illustrating election activities.
• | Writes campaign | • …will …… on/in ………. | • | Drawing posters.
messages | • They will elect Mariko on Monday. Whom … | • | Writing guided compositions
• Whom are we electing as the food prefect? Is ……. | • | Writing simple campaign
standing for the post of …… | messages
E.g. Is Akiiki standing for the post of class monitor Yes | • | Writing short and simple conversations
Akiiki is standing for the post of class monitor No, Akiiki | or dialogues.
is not standing for the post of class monitor

Suggested assessment competences
• Participates in democratic activities at school level.
• Writes text related to democratic practices
• Reads simple texts on democratic practices.

24 | ϮϰNational Curriculum Development Centre
P4 English Syllabus,

P4 English Syllabus, National Curriculum Development Centre | 25

www.ncdc.go.ug
</passage>

<passage id="lchk_36dd3e5d0c764c52b4e88f44cb68de27" source="Primary 4 English Abridged Curriculum 2021" part="8">
pronounce/sign words.
- constructing sentences
using the given structure
and vocabulary.
- reading texts (passages/
dialogues/poems/notices).
- reciting /signing poems.
- acting/signing dialogues
- answering
comprehension questions
- spelling/finger
spellingwords
- completing sentences.
- writing/brailling
compositions
- re-writing stories.
Suggested Activities for Assessment
15
- Reading/signing stories and answering comprehension questions
- Constructing both oral and written sentences using the learnt vocabulary.
- Using given structures to construct sentences
- Composing poems/songs/chants
- Completing stories/dialogues
- Writing/Brailling guided and free compositions
Topic 8: DEMOCRACY
Overview:
This topic introduces the learner to vocabulary related to democratic activities. It will enable them
to express themselves using appropriate language in different situations.
Sub-topic A: Games and Sports
Competences Content Suggested teaching and
learning activities
The learner:
• narrates/signs stories
related to games and
sports.
• reads/ signs texts
related to games and
sports.
• writes/signs
texts/stories related to
Games and sports.
Vocabulary
run, jump, play, football, netball, skip, race,
throw high, long, kick, player, lose, win,
happy. clap, shout, game, support, slow,
ordinal numbers, fast, quickly volleyball,
watch, coach, umpire, referee
Grammar
Use of adjectives
Language Structures
- What will … do?
What will Akello do?
- … will …
Akello will play football.
- Who was the ……. ?
- …. was …. the …….
Who was the first?
Opendu was the first.
- Why was …… the …?
Why was Delia the last?
- ….. was the ……. because…………
Delia was the last because she was slow.
- ……want(s) to …… when …….
I want to play volleyball when I join Primary
Five.
-guiding learners to
pronounce/sign words.
- constructing sentences
using the given structure
and vocabulary.
- reading texts (passages/
dialogues/poems/notices).
- reciting /signing poems.
- acting dialogues
- answering
comprehension questions
- playing spelling games
- completing sentences.
- writing compositions
- re-writing stories.
Suggested Activities for Assessment
- Constructing both oral and written sentences using the learnt vocabulary.
16
- Using given structures to construct sentences
- Reading/signing texts and answering comprehension questions.
- Completing stories/dialogues
- Writing/brailling guided compositions
Sub-topic B: Music, Dance & Drama
Competences Content Suggested teaching and learning
The learner:
• narrates/signs stories
related to Music,
Dance and Drama.
• reads/ signs texts
related to Music,
Dance and Drama.
• writes/signs
texts/stories related to
Music, Dance and
Drama.
Vocabulary
sing, recite, conductor,
actor, costume, actress,
festival, best, rhyme,
instruments, drama, worst,
choir, concert
Grammar
The use of superlatives
Language Structures
- Which …. will ……
Which song will Daudi
sing?
-guiding learners to pronounce/sign words.
- constructing/signing sentences using the
given structure and vocabulary.
- reading texts (passages/
dialogues/poems/notices).
- reciting/signing poems.
- acting/signing dialogues
- answering comprehension questions
- playing spelling games
- completing sentences.
- writing/brailling compositions
- rewriting stories.
Suggested Activities for Assessment
- Constructing both oral and written sentences using the learnt vocabulary.
- Using given structures to construct sentences
- Reading/signing storiesand answering comprehension questions.
</passage>

<passage id="lchk_6fcb22bbbfa8421c9154444f4cb0387d" source="Primary Four Abridged Curriculum: Draft Syllabi" part="38">
Assessment guidelines:
Let the learner;
- Write individually on the work in the church today.
- Talk about the history of the early church in simple sentences.
- Tell ways how the Holy Spirit helps the believers in the church today.
80
TERM THREE.
Topic: Jesus our example in the service.
Overview:
Topic 6 of Primary four curriculum has been merged with topic 7 “Voluntary service in
response to God’s love” of the same curriculum. They bring out the concept of service
which is defined as providing something to someone. Jesus wanted to be a living
example in service. Jesus taught people to be servants and do voluntary service. This
topic will help the learner to identify good services done by people in the community,
he/ she will be able to participate in and appreciate the different services of people.
Competences content Suggested Activities.
- Describes ways in
which Jesus served
His parents and
other people.
- Describes ways
learners can do
voluntary work at
home, school,
community and
nation.
- Explains the meaning
of the word
Voluntary.
- Mentions different
examples of unpaid
service in the Bible,
Church and
community.
- Mentions different
Voluntary
organizations.
- Sensitizes learners
and staff on a
voluntary project
- Ways Jesus served
others,
- Jesus showing true
example of service.
- Serving his parents
and others.(Luke
2:51,4:40)
- Washing his
disciples feet,et.c
(John 13:4-17)
- Good service in the
Community.
- Examples of good
service(Luke 10:25-
37,Matthew 8:5-13)
- Ways of serving
others.
- (Galatians 6:2,
Romans 16:12-13).
- Unpaid service.
- Meaning of the
word “voluntary”.
- Examples of unpaid
service from the
Bible(John4:1-12,
Luke 10:25-36)
- Church and
community.
-
- Co-operating in
voluntary service
- Reading/signing the
scripture (Luke2:51,
4:40).
- Listing ways
learners can serve
others at home,
school and nation.
- Talking/signing
simple ways about
how Jesus served
His parents and
other people.
- Roleplaying the
washing of the
disciple’s feet.
- Re-telling/signing in
simple words the
meaning of
voluntary.
- Listing examples of
unpaid service in
the Bible, church
and community.
- Demonstrating
exchange of gifts
with classmates.
- Listing from
discussion the aims,
work and benefits of
voluntary
organizations.
81
(Nehemiah 3,
2corinthian 8:1-7).
- Ways in which co-
operation was
important in the
Bible.
- Some voluntary
organizations.
- Aims of voluntary
organizations.
- Work of voluntary
organizations.
- Benefits of
voluntary service.
- Voluntary service
project.
- Planning.
- Preparation.
- Implementation of
the project.
- Evaluation of the
project.
- Contributing items
for the project.
- Seeking
qualifications on the
project.
- Participating in the
project.
- Contributing to the
evaluation of the
project.
Assessment guidelines.
The learner;
- Tell the true services people can give to others.
- Do voluntary work at home, school and community.
- Write the benefits of voluntary service.
- Start a project at school/at home.
Topic; 2, Making our decision as Christians
Overview :
This topic brings out the concept of “making a decision” this means that God gave man
the ability to make their own decisions. When human beings make right decisions God
bless them, when they make bad decisions they have to suffer. The learner should
always seek assistance in order to make right decisions. Before deciding of what to do,
the learner should consider the effects of their decisions.
Competences. content Suggested activities.
</passage>

<passage id="lchk_f716af72c8cc4a5a82acd048b8952822" source="P 4 Composition AND Comprehension Scheme Term III" part="1">
P.4 ENGLISH SCHEME COMPO AND COMPRE TERM III
WK PD TOPIC ASPECT SKILLS CONTENT COMPETENCE METHODS ACTIVITIES L/SKILLS AIDS T/AID REF REM
1 1 Time
Composition
Listening
Speaking
Reading
Writing
Vocabulary
Learning the meaning of these words
tomorrow
next day
next week
shall not
will not
arrive
reach
library
lend
borrow
The learner;
Pronounces,
reads the
words, spells
the new words
and uses the
new words in
sentences
Guided
discussion
Question and
answer
Brain
storming
Pronouncin
g, reading
and
spelling the
new words
Using given
words in
sentences
Effective
communication
Self esteem
Co-operation
Effective
communication
Dictionary , chart esteem, co-operation and effective communication
St. Bernard’s English book 4 page 125
2 Time
Composition
Listening
Speaking
Reading
Writing
Structures
Using will / shall .......
Examples
Jane will go to school tomorrow
We shall not go to the market next
week
The learner;
Reads given
sentences,
forms own
sentences
using the given
structures ,
joins the given
sentences
using the given
structures
Guided
discussion
Question and
answer
Brain
storming
Reading
given
sentences
Forming
own
sentences
Joining
sentences
Effective
communication
Self esteem
Co-operation
Effective
communication
3 Time
Composition
Listening
Speaking
Reading
Writing
Conversation
We shall miss / Mr. Guma
Read the conversation and
answer the questions in full
sentences
The learner;
Reads the
passage
correctly and
answer
questions
about it in full
sentences
Guided
discussion
Question and
answer
Brain
storming
Reading
the
conversatio
n correctly
Answering
the
questions
about the
conversatio
n
Effective
communication
Self esteem
Co-operation
Effective
communication
2 1 Time
Comprehension
Listening
Speaking
Reading
Writing
Passage
My family
Read the passage and answer
questions in full sentences
The learner;
Reads the
passage
correctly and
answers
questions
about it in full
sentences
Guided
discussion
Question and
answer
Brain
storming
Reading
the
passage
correctly
Answering
questions
about the
passage in
full
sentences
Effective
communication
Self esteem
Co-operation
Effective
communication
Dictionary , chart esteem, co-operation and
effective communication
St. Bernard’s English book 4 page 125
2 Time
Comprehension
Listening
Speaking
Reading
Writing
Keeping a diary
Study Amanya’s Diary and answer
the questions in full sentences
The learner;
Studies the
diary carefully
and answer
the questions
about it in full
sentences
Questions
and answer
Guided
discussion
Brain
storming
Question and
answer
technique
Studying
the diary
answering
questions
in full
sentences
Self esteem,
Pull out
St. Bernard English book 4 page 133
3 Time
Comprehension
Listening
Speaking
Reading
Writing
Class time table for P.4
Study the time table and answer the
given written questions
The learner;
Studies the
time table
carefully and
answers the
questions in
full sentences
Questions
and answer
Guided
discussion
Brain
storming
Question and
answer
technique
Studying
the time
table
Answering
the
questions
Effect
communication
Text book and class time table
The Winner English book 4 page 102
3 1 Time
Comprehension
Listening
Speaking
Reading
Writing
Keeping a diary
Vocabulary
diary, read, months, text book, day,
year, date, borrow, lend, revise, time
table
The learner;
Reads, spells
and
pronounces
words
correctly,
forms
sentences
correctly and
use the words
in sentences
correctly
Questions
and answer
Guided
discussion
Brain
storming
Question and
answer
technique
Reading
spelling
</passage>

<passage id="lchk_7685308ccbde482cb6da1bdbb89736ea" source="P 4 ENG & SST Lesson Notes Term III 2023" part="1">
Page | 1
PRIMARY FOUR ENGLISH LESSON NOTES FOR
TERM THREE
WEEK ONE
TOPIC 1: EXPRESSION OF THE FUTURE
Topic 1 a: Expression of the Future
Vocabulary
1. tomorrow 5. shall not
2. next week 6. will not
3. next month 7. shan’t
4. next year 8. won’t
Activity 2
Use the vocabulary above to construct meaningful sentences.
Activity 3.
Look at the table below and write five sentences.
I
We
She
They
shall
shall not
will
will not
play with my friends.
go with him.
go on holiday.
swim in the lake.
disturb you today.
For example.
(a) We shall not play with him.
(b) We shall go with him
Activity 4.
Read the passage and answer the questions about it in full sentences
AKOT’S PLAN TO GO TO THE ZOO
Next Sunday,my sister Joyce and I will visit the Zoo. We shall see many
animals and birds.We shall see lions,chimpanzees and monkeys.But we shall
not see the elephants because they are not in the Zoo.
On our way to the zoo,we shall eat some pancakes and drink soda. We shall
take some bananas for chimpanzees and the monkeys.
Page | 2
We shall come back home in the evening when we are very tired.We shall bathe
with warm water.After that, we shall go to bed to rest.We shall then be able to
wake up early and go to school the next day.
Questions
1.When will Akot go to the zoo?
2.With whom will Akot go to the zoo?
3.What will they eat on their way to the zoo?
4.Why will they not see the elephants at the zoo?
5.What will they take for the chimpanzees and the monkeys?
6.Will they see lions at the zoo?
7.How many people will go to the zoo next Sunday?
Activity 5 Written Work.
Study Namata’s work plan for next week and answer questions that follow
in full.
Sunday  She will go to church.
 She will feed the rabbits at 10:00 a.m.
Monday  She will clean the kennel.
Tuesday  She will read a novel.
Wednesday  She will go for P.E at school.
Thursday  She will visit aunt Suzan after school.
 She will wash her P.E uniform.
Friday  She will start on her mixed exercise.
Saturday  She will go to the beach with her parents.
Questions:-
1. Who will feed the rabbits?
2. On which day will the rabbits be fed?
3. What will Namata do on Monday?
4. At what time will Namata feed the rabbits?
5. What is a kennel?
6. Write P.E in full.
7. At what time will Namata visit her aunt?
8. What is the name of Namata’s aunt?
9. On which day will Namata wash her P.E uniform?
10. What will Namata do on Friday?
11. With whom will Namata go to the beach?
TOPIC 1B: KEEPING A DIARY
Vocabulary
1. diary
2. read
3. note
4. date
5. day
6. daily
7. month
8. year
9. calendar
10. time
Page | 3
Activity 2
Read the words and use them to construct sentences.
Activity 3.
Read the words in the box and use them to fill the gaps below.
1. The …………today is Monday, 15 th August, 2011.
2. Have you seen my …………? I need to write in it.
3. I am ten now, so I shall be eleven next………….
4. It’s August now, so next……………… is September.
5. A ………………….shows you all the days of the year.
6. How many ……………….are there in a week?
diary
date
days
month
calendar
year
Monday Tuesday Wednesday Thursday Friday Saturday Sunday
1
Wrote an
invitation
card to
uncle
2 3
Sent the
invitation
card to
uncle
4 5
6 7 8 9 10 11
We went to
the village
for my
birthday
party
12 Father
bought for
me a new
party dress.
13 14
Aunt
Monica
baked
my
birthday
cake
15 16
I
celebrated
my ninth
birthday
17 18 19
20 21 22 23 24 25 26
I attended
thanks
giving
service.
27 28 29 30
We
returned
to our
home.
Page | 4
Activity 4.
</passage>

<passage id="lchk_a8b51257a7204350820a66c1c782842d" source="P 4 ENG & SST Lesson Notes Term III 2023" part="2">
Study Amanya’s Diary and answer the questions about it.
Questions:-
1. Whose diary is this?
2. On which day of the week did this month begin?
3. What did Amanya do on the first Wednesday of this month?
4. When did Amanya send the invitation card to her uncle?
5. What did Amanya’s father buy for her ?
6. Who baked Amanya’s birthday cake?
7. On which day did Amanya celebrate her birthday?
8. When did the month end?
9. When did Amanya attend thanks giving service?
10.Who bought Amanya a new dress?
Activity 5.
Written Exercise
Study Kivi’s activity plan for a whole week and answer questions that follow in
full.
October Morning Afternoon
Sunday, 13 th Prayers Ironing clothes
Monday, 14 th Reciting a poem Singing
Tuesday, 15 th Spellings and dictation Computer lessons
Wednesday, 16 th Writing a composition Drawing and painting
Thursday, 17 th Debating Swimming lessons
Friday, 18 th Attending school
assembly
Doing mixed work
Saturday, 19 th Helps mother with
domestic work
Visits his friend in Kansanga.
Questions:-
1. When will Kivi go for prayers?
2. What will Kivi do on Sunday afternoon?
3. What will Kivi do on Monday, 14 th ?
4. When will Kivi go for computer lessons ?
5. Apart from drawing, what else does Kivi do on Wednesday?
6. What does Kivi do on Thursday morning ?
7. At what time of the day will Kivi attend the school assembly?
8. Whom will Kivi help on Saturday?
9. What kind of work will Kivi help his mother?
10. Whom will Kivi visit on Saturday?
11. Where does Kivi’s friend stay?
Page | 5
TOPI 1 C: USING STUDY TIME.
Vocabulary
1. borrow 6. usually
2. lend 7. return
3. library 8. notes
4. librarian 9. notebook
5. revise 10. textbooks
Activity II
Use the vocabulary above to construct sentences.
Activity III
Use the words in the box to fill in the gaps correctly.
1. We write ………………in our exercise books.
2. It is very important to …………………for end of term exams.
3. A ………………works in a library.
4. A ………………..is a collection of books.
5. He told me to …………………….. him my jacket.
Activity IV
Study Mukaga’s plan for tomorrow and answer the questions that follow in
full sentences.
8:00 a.m Having breakfast at Doso’s restaurant.
8:30 a.m Boarding a vehicle to Entebbe with friends.
10:30 a.m Getting special hire taxi to the zoo.
11:00 a.m Looking at different animals and birds.
12:30p.m Taking photographs at the zoo.
I:00 p.m Having lunch with my friends.
2:00 p.m Swimming with my friends.
2:45 p.m Boarding a vehicle back to Jinja.
Questions
1.Where will Mukaga go tomorrow?
2.Where will he have breakfast from?
3.For how long will he have his breakfast?
4.With whom is he going to Entebbe?
5.What will Mukaga do at 11:00 a.m?
6.What will he do after looking at the animals?
librarian
lend
library
notes
revise
Page | 6
7.At what time will he have lunch?
8.What means of transport will he use to go to the zoo?
9.Where does Mukaga stay?
10.Write in full:
(a) a.m
(b)p.m
Written Exercise
Study Nanono’s timetable and answer questions that follow in full.
9:00a.
10.00a.m
10:00a.m
11:00a.m
11:00a.m
12:00p.m
12:00p.m
1:00p.m
1:00p.m
2:00p.m
2:00p.m
3:00p.m
3:00p.m
4:00p.m
Math English Art L S.S.T Science
Sci Maths S.ST Eng Music
Maths Reading
and
Writing
Sci P.E R.E
Eng Maths Computers Debate S.ST
Assembly S.ST Eng Swimming Sci
Questions
1. Whose timetable is written above?
2. What subject is taught after maths on Monday?
3. What subject is taught on Tuesday after break?
4. At what time does Nanono go for break?
5. On which day is music taught?
</passage>

<passage id="lchk_4630fb819e70455bb36f77aead3c2f97" source="P 4 ENG & SST Lesson Notes Term III 2023" part="27">
2. Why is corruption a bad practice in our district?
3. Name two products get from a petrol station
4. Write the following abbreviations I full.
a) UPE
b) USE
c) NWSC
d) HEP
5. Why is education very important to people in our district?
6. What type of education was introduced by missionaries in Uganda?
7. Which type of road is the best for all seasons
8. In which district is Entebbe international airport?
9. Name two examples of mass media.
10. Give one reason why newspapers are not the best means of
communication.
11. Write short notes about
a) Surgeons
b) Midwives
c) Opticians
SOCIAL ACTIVITIES
Qn . What are social activities?
Social activities are activities that bring people together
Examples of social activities
- Circumcision ceremony
- Wedding ceremonies
- Graduation ceremonies
- Clan meetings
- Birth day parties
- Naming of twins
- Coronation of kings
Page | 74
- Games and sports
- Music, Dance and Drama
Importance of social activities
- They promote unity
- They promote friendship
- They promote culture
- They bring happiness.
</passage>

<passage id="lchk_89b42330f4534f47b4c5293f6cac7b9c" source="P 4 Junior English Term III" part="1">
1
2020
2
WEEK 2
COLLECTIVE NOUNS.
▪ Nouns are names of things.
▪ Collective nouns are names given to a group of things.
For example
Nouns Collective Nouns Collective
1. birds flock 17. bees swarm
2. sheep flock 18. fish shoal
3. thieves gang 19. whales school
4. flowers bunch 20. lions pride
5. furniture suite 21. friends party
6. puppies litter 22. dancers troupe
7. kittens litter 23. angels host
8. stones pile 24. musicians band
9. teachers staff 25. magistrates bench
10. trees forest 26. bananas bunch
11. tools set 27. actors company
12. cattle herd 28. employees staff
13. books library 29. pupils
class/school
14. singers choir 30. pilgrims band
15. bishops bench
16. directors board
Fill in the gaps with correct collective nouns.
1. A ____________of thieves held up the mail van and robbed it.
2. The tourist saw a _____________of elephants at Kazinga channel.
3. A _____________ of fish was swimming across the river.
4. Ben invited a _____________ of friends on his birthday party.
5. A ____________ of bees had settled on an orange tree.
6. The cat was very proud of her__________ of kittens.
7. A _____________of puppies was seen crossing the road.
8. The bride was holding a beautiful ______________of flowers.
9. His whole _______________of cattle has been affected by drought.
10. The stubborn boy was told to collect a _____________ of stones.
11. A ______________ of birds flew over our house.
12. Musoke has a big ___________of sheep on his farm.
13. The meeting was attended by ___________ of directors.
14. A ______________of bishops made their vows last Sunday.
15. We were entertained by a _______________of dancers.
Fill in the collectives nouns of the following words.
16. a ________________of books.
17. a ________________ of teachers.
18. a _________________of musicians.
19. a _______________ of angels.
20. a ________________of tools
3
WEEK THREE
ADVERBS
An adverb is a word that tells us more about a verb, an adjective or another verb.
Examples of adverbs.
Fast,hard,quietly,slowly,quickly,rudely,nicely,smartly,heavily,carefully,loudly,etc.
Look at these sentences.
1. Keno walks to school very fast.
2. He talked to me loudly.
3. I slept soundly last night.
4. It rained heavily last night.
5. She does her work neatly. Underline the adverbs from the following sentences.
1. My sister reads properly.
2. The monkeys ate the bananas hurriedly.
3. Our teacher entered the room quietly.
4. Sonia writes her work slowly.
5. Most girls speak softly.
6. I can’t see clearly from a distance.
7. She spoke to me rudely.
8. The lady hugged her daughter immediately.
9. He is smartly dressed today.
10. The boys ate their food greedily.
11. Kate danced happily,
12. The twins sang merrily.
13. She was told to walk quickly not to reach school very late.
14. Ingrid wrote her work carefully.
15. Tom hit his head on the table accidentally.
WEEK FOUR
ADVERBS
FORMATION OF ADVERBS
An adverb is a word which describes an action. It shows how an action is done.
Some adverbs are formed by adding --- ly
Examples
ADJECTIVES ADVERBS
Quick + ly = Quickly
Slow +ly = Slowly
Clear +ly = Clearly
Soft + ly = Softly
Proud + ly = proudly etc
EXERCISE
Revised Junior Pg 17 and 18.
4
Form adverbs from the following words
1. cheap 6. careful
2. poor 7. happy
3. quiet 8. lucky
4. smart 9. heavy
5. rude 10. patient
Fill in the gaps with a correct adverb
11. The lion jumped over the kob-------------- (swift)
12. The patient was called ------------for a check up. (immediate)
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
