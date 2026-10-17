# Job ltsk_effda01fde214aae853bdefdce91e52b-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for English, Primary Six 2026, Term 3.
The term has 10 teaching weeks and this subject has 6 periods per week. Every lesson is ONE 40-minute period, so keep each lesson small enough to teach in 40 minutes.
There are no weekly review lessons: the subject has a lot of content, so every period teaches or practises.
Give at most 59 teaching/practice lesson entries in teaching order (the last lesson of the term is the end of term assessment).
Each lesson has a kind: "teach" (new content) or "practice" (the same subtopic as the teaching lesson just before it: exercises, oral work, drawing, matching, filling in blanks, ALL taken from the passages).
When the material is thin (common in lower primary), follow each teaching lesson with a practice lesson. Split big subtopics over several teaching lessons.
Never pad with content the passages do not have: if they cannot fill the term, return fewer lessons and list what is missing in gaps. Ledgerly fills the remaining weeks with revision.
You are composing the SCHOOL'S OWN scheme. The passages below (the official NCDC curriculum and guides, plus schemes of work, lesson plans, notes and past papers from the school e-library) are reference material:
The school's SCHEMES OF WORK for this class and term ("P 6 Primary SIX ENG Scheme OF Work T…C", "P.6 PRIMARY SIX ENG SCHEME OF WORK TEACHER.AC", "p.6 english compo and compre scheme term III 2019") are the BASE: follow the topics, subtopics and week-by-week order they agree on. Every topic they list for this term MUST become a unit, in their order, and their subtopics become the lessons, with about the pacing they give. Cite their passages in sourcePassageIds of every lesson that follows them.
The NCDC documents (titles starting "NCDC") only FILL GAPS: a topic NCDC lists for this term that the schemes lack gets its own unit where it fits best. Never drop or rename a schemes-of-work topic to fit NCDC. NCDC lower-primary thematic curricula list every learning area side by side in table columns separated by " | ": take only the English column.
Combine them in this authority order: the school's schemes of work for topics, sequence and pacing; NCDC for anything they miss; the strongest detailed notes for accurate teaching depth; past papers for expected applications and activities.
Use this term's part of the material (Term 3) when the passages cover several terms.

NCDC topics for Primary Six 2026, Term 3 that must ALSO be covered. Each needs at least one unit whose title or theme names it; the school's schemes of work decide where it goes and how many lessons it gets:
  5. Hotels
  6. Using a Dictionary
Do NOT write lesson content yet. Each unit and lesson must cite the passage ids it comes from in sourcePassageIds.

Reply shape:
{"title":string,"summary":string,"units":[{"title":string,"theme":string|null,"weekFrom":int|null,"weekTo":int|null,"competences":string|null,"sourcePassageIds":[string],"lessons":[{"title":string,"subtopic":string|null,"kind":"teach"|"practice","objectives":[string],"sourcePassageIds":[string]}]}],"gaps":[string]}

<passages>
<passage id="lchk_78210c34394d426fb25236bf43264a79" source="NCDC P6 Set One Sept book – English" part="1">
English Syllabus

Introduction to the Primary Six English Language Syllabus
General Background
The teaching and learning of English language has been given a lot of
emphasis since Primary One. As highlighted in the syllabuses of the
previous classes, the syllabus of Primary Six promotes the development
of language competences in an integrated manner, that is, by using topics
from other subjects while developing all the language skills.

It is expected that at this level, learners will fully develop the ability to
use English as a language in and outside the classroom at all times. The
primary concern is to help learners develop the confidence to use English
in a variety of situations.

Rationale
Uganda is a multilingual society where over thirty indigenous languages
are spoken. Until recently when Kiswahili was declared the second official
language, English has been the only official language. For this reason,
English is taught at all levels of education to enable learners develop
communication skills and access information written in English.

General Learning Outcomes
By the end of Primary Six, the learner will have:
• acquired effective use of the four basic language skills, namely,
listening, speaking, reading and writing.
• developed the confidence to express themselves in English.
• acquired the appropriate language to use in a variety of
situations.
Organisation of the Syllabus
In the process of revising the syllabus, some topics have been retained,
others dropped to reduce repetition and duplications and others have
been introduced while at the same time bringing on board concepts that
are familiar to the learners. The purpose of this re-organisation is to ensure
that the content is kept light and simple for the learners at this level. For
instance, the topics ‘Sanitation’ ‘Domestic Animals’ and ‘Safety at Home’
have been left to Science and Social Studies because that is where they fit

National Curriculum Development Center

best. Some new areas have been included such as ‘Carpentry’, ‘Tailoring’
and ‘Caring for Animals’ which are now sub-topics under ‘Occupations’.
Topics like ‘Baking’ have been shifted from P7 to P6 so that it is covered
under the general topic ‘Occupations’.

The topic ‘At the Market’, was catered for in P4 under ‘Selling and Buying’
while ‘Traditional Stories’ has been dropped because this was handled
in the lower classes. Instead of ‘Restaurants’, there is now ‘Hotel’ which
provides a wider range of vocabulary than what was in the previous topic.
In each topic, there is a background, learning outcome, values as well as
life skills and their indicators. In addition, each topic comprises content,
competences, suggested teaching activities, assessment guidelines and
important notes to the teacher.

Although the old syllabus had eleven topics, this new syllabus has only
six topics which have been well thought out and enriched with content,
aimed at developing the required competences, life skills and values
appropriate for Primary Six. Content in this syllabus is presented in the
form of vocabulary, grammar and structures. The content is consolidated
through activities such as dialogues, compositions, reading texts,
comprehension, poems, and language games.

Though there are specific periods allocated for each topic the teacher may
break down content according to the abilities of the learner. This implies
that the abilities of learners should determine the pace at which learning
takes place.
</passage>

<passage id="lchk_fc4a0c49508c459fac6f429f0d47516d" source="NCDC P6 Set One Sept book – English" part="2">
The topics in this syllabus are meant to be used as vehicles with which to
teach the aspects of the language namely vocabulary, structure, grammar
and the language skills. The facts of these topics are to be handled in the
different subjects on the curriculum.

Methodology
Effective language teaching calls for active participation of learners.
Learners should therefore be given adequate opportunity to practice the
vocabulary and structures learnt. Oral work should always be given
before written practice. It is important to note that learners have acquired
adequate vocabulary and structures that can enable them write English
legibly or speak it fluently and therefore the teacher should provide

opportunities for them to write legibley and speak it fluently. You will
need to use generic methods such as demonstration, discovery, role-play,
research, group work and dramatisation.

It is important to use methods appropriate for the development of the four
language skills, which are listening, speaking, reading and writing. These
skills are related to each other in different ways and it is very important
for a learner to develop mastery of them all.

1. Listening skills
Listening is a primary skill whose development determines the ability
of the learners to develop the advanced or secondary skills (reading and
writing). At this level, you should design activities that help the learners
to develop the following sub-skills:
• getting specific information.
• organising ideas.
• predicting what is going to follow.
The following are suggested activities appropriate for the development
of the above competences:
• | listening to stories.
• | dialogue
• | songs
• | listening to recorded information.
• | listening to and repeating after you.
• | listening to and completing oral sentences.
• | listening to and comparing sounds.
• | whispering game.
• | carrying messages .

2. Speaking skills
Speaking is the second primary after listening. At this level, you should
design activities that enable the learners to:
• participate in dialogues and debates.
• ask and answer questions.

National Curriculum Development Center

• explain events orally.
• report incidences orally and in written.
• give brief oral descriptions.
Some of the suggested activities to develop the above competences
include:
• | repeating words and sentences with appropriate intonation.
• | acting out dialogues and short plays.
• | narrating stories fuently.
• | reading texts loudly.
• | talking about identified topics confidently.

3. Reading skill
This is one of the advanced skills whose development is based on the
full development of the listening and speaking skills also known as the
primary skills. At this level, you need to help the learners carry out silent
reading for both intensive and extensive reading.

The sub-skills that the learners need to develop at this level include:
• | proper book handling.
• | recognising letters and numbers.
• | recognising words, phrases and sentences.
• | avoiding bad reading habits.
• | extracting information stated in the passage.
• | reading phrases.
• | guessing the meaning of words from a context.
• | reading for comprehension.
• | reading for leisure.
Some of the suggested activities to develop reading skills include:
• | look and say.
• | look/read and do.
• | read and match.
• | matching questions to answers.
• | read
• | arranging jumbled sentences into a paragraph.

• | answering questions about the story.
</passage>

<passage id="lchk_db29091ee57847f3b69d56532a5ecf0a" source="P6 Materials" part="1">
©National Curriculum Development Centre, 2020 1
ENGLISH LANGUAGE
LESSON 1: Use of Adverbs
Learning Outcomes
By the end of this lesson, you should be
able to:
i) identify ways of doing things.
ii) use of adverbs in your daily life
activities.
You will need :
• a pen
• a book
Introduction
An adverb is a word that tells more
about a verb, an adjective and another
adverb. Adverbs tell us how an action is
done: when? why? how? and where?
Examples
i) The cyclist is riding slowly .
ii) Children should cross the road
carefully .
Activity 1
Use the correct form of the word in the
brackets to complete the sentences
below.
Examples have been given to guide you.
1. Tino cleverly avoided the
punishment. (clever)
2. Uganda’s population is steadily
rising. (steady)
3. St Thomas choir sang the second
compulsory song ________. (beauty)
4. The host welcomed us __________.
(cheer)
5. We ___________ waited for
his return from Ojipaku market.
(patience)
6. Italians have seen the ________
coronavirus attacked. (worse)
7. They answered the
question_________. (wise)
8. A machete is ___________ bigger
than a knife. (usual)
9. The hungry boy ate the mango
__________. (greed)
10. The hunter _________ attacked the
lion in its den. (brave)
Activity 2
Order of Adverbs
When more than one adverb is used in
a sentence, they usually follow in this
order: manner (how?), place (where?)
and time (when?).
Example
The pedestrian crossed the road
carefully (how?) at the zebra crossing
(where ? ) yesterday (when ? ) .
From the sentences below, underline the
adverbs of manner, place and time.
1. The traffic officer called the driver
loudly at the junction in the morning.
2. Many cyclists ride carelessly at the
traffic lights every day.
3. The bus driver spoke politely to the
passenger on the bus on Tuesday.
4. My mother nicely made cakes from
the kitchen last weekend.
5. It rained heavily in our area last
year.
LESSON 2: Informal Letter Writing
Learning Outcomes
By the end of this lesson, you should be
able to:
i) express your views on safety on
the road.
ii) write a letter about safety on the
road.
Introduction
Letter writing is one way of sending a
message between or among people. You
can write a letter to a friend, parents,
relatives and many others.
Activity 1
1. (a) Write a letter to your father
appreciating him for his effort to
keep everybody well in this period
of COVID-19 pandemic. Wish him
a longer stay in this life. Use your
school address.
(b) The letter below has some words
missing. Using the words in the box,
complete it by filling in the gaps
correctly.
reap advise purpose academic not
arua discussions hear dear examinations
Owayi Primary School,
P.O Box 135,
_________________
19th March, 2020.
____________ Maxwell,
How is Komendaku? Hoping you are fine.
The __________ of writing to you is to
___________ you about how to prepare
to excel in ____________. On my side,
I am very seriously engaged in group
____________ and research as well.
I wish to ____________ from you too,
on what you are doing to cross that
______________ river. Hoping you are
______________ wasting time in
a disco and playing cards under the
big mahogany tree near the football
pitch. The proverb states “You
______________ what you sow.”
I wish you the best in your struggle.
Yours,
Akasa Brian.
PRIMARY SIX
SELF STUDY MATERIALS Ministry of Education
and Sports
©National Curriculum Development Centre, 2020 2
( HEALTH TIP: Stay home and observe
social distance to stay safe. )
</passage>

<passage id="lchk_b5a2dafc02bb40f9bb8d7f1ae949bbe2" source="Primary Six Curriculum@2023" part="1">
THE REPUBLIC OF UGANDA
Ministry of Education and Sports
Primary School Curriculum
Primary Six Curriculum
Set One: English, Integrated Science, Local Language, Mathematics,
Religious Education (Christian Religious Education and
Islamic Religious Education) and Social Studies.
2010
National Curriculum Development Centre (NCDC) Uganda 2010
P. O. Box 7002, KYAMBOGO
KAMPALA – UGANDA
URL www.ncdc.go.ug
ALL rights reserved. No part of this syllabus should be reproduced
stored in a retrieval system or transmitted in any form by any means
electronic, mechanical, photocopying, recording or otherwise without the
permission of the publisher. No patent liability is assumed with respect to
the use of the information contained herein.
Published by National Curriculum Development Centre
Copyright © NCDC 2010
ISBN: 978-9970-117-93-2
iii
Contents
Acknowledgement ................................................................................................. v
Foreword ................................................................................................................ vi
Introduction to Set one P6 Curriculum ................................................................ viii
English Syllabus ........................................................................................ 1
Term I.......................................................................................................... 12
Term II ........................................................................................................ 20
Term III ....................................................................................................... 34
Integrated Science Syllabus .................................................................... 43
Term I.......................................................................................................... 58
Term II ........................................................................................................ 74
Term III ....................................................................................................... 88
Local Language Framework ...................................................................... 103
Term I.......................................................................................................... 112
Term II ........................................................................................................ 122
Term III ....................................................................................................... 133
Mathematics Syllabus ............................................................................... 143
Term 1 ......................................................................................................... 148
Term II ........................................................................................................ 161
Term III ....................................................................................................... 174
Religious Education Syllabus ................................................................... 187
Part I: Christian Religious Education ....................................................... 189
Term I.......................................................................................................... 195
Term II ........................................................................................................ 208
</passage>

<passage id="lchk_6cd7b6e16c3341cfb29fdb45262b718d" source="P 6 Primary SIX ENG Scheme OF Work T…C" part="1">
1
SCHEME OF WORK FOR PRIMARY SIX ENGLISH I -III
Wk Pd Topic/ subtopic Competence Methods Skills/Values Suggested activity Instructional
material
References Rema
rks
1 5pds Punctuation / punctuation marks
• Capital letters ( A, B, C…..)
• Full stop (.)
• Question mark (?)
• Exclamation mark (!)
• Apostrophe (‘)
• Comma (,)
• Semi colon (;)
• Hyphen (-)
• Quotation marks (“ ”)
Learner
I. Uses the
punctuation marks
in the sentences
correctly.
II. Punctuates the
sentences correctly.
• Discussion through
questions and
answers.
• Explanation
Listening
Speaking
Reading
Writing
Critical thinking
Effective
communication
Punctuate the given
sentences
A chart showing
punctuation marks
and how they are
used.
Essential Eng. Pgs 40,
55, 56.
Detailed Eng. Grammar
pgs 1-10
1 3pds Comprehension safety on the
road.
• Traffic dangers
Vocabulary- bend crossroads,
cyclist, first aid, hand signal,
junction, motorist, pedestrians,
pavement, roundabout, side path,
traffic, traffic police, zebra
crossing.
• Structural patterns
using ….as soon as…
….because …..
….must……
Where must ……
…….should not….
• Dialogue
Crossing the road
• Poem
Safety on the road.
Learner:
• Reads, pronounces
and writes the
vocabulary words
correctly.
• Uses the
vocabulary words in
oral and written
sentences correctly.
• Uses the oral
structural patterns
in oral and written
sentences correctly.
• Reads the given
texts and answers
the oral and written
questions correctly.
• Discussion
through
questions and
answer
• Explanation
• Listening
• Speaking
• Reading
• Writings
• Creative
thinking
• Problem
solving
Reading the given
texts
Construct oral and
written sentences.
Pupils’ text books. MK Primary English
pps. Bk 6 pgs 1-13
2 4pds COMPREHENSION
• Traffic dangers
• A visit by the traffic officer.
• Guided composition
• Composition writing
• Poem (traffic dangers)
• Passage (narrow escape)
Learner:
• Reads the passage
and answers
questions about it.
• Writes sentences
about the pictures.
• Writes a letter to the
traffic officer about
causes of road
accidents.
• Discussion
through questions
and answers.
• Explanation
• Listening
• Speaking
• Reading
• Writing
• Critical
thinking
• Problem
solving
• Reading given
texts
• Write a
composition about
road accidents.
• Write a letter to
the traffic officer.
MK Pri Eng PPS
Bk 6 1 -13
PPS text bks.
2 4pds Nouns
Types of nouns
• Proper nouns e.g Kampala, Tom
• Common nouns e.g. pen, book
Learner :
• Defines nouns
• Classifies nouns
• Explanation
• Discussion through
questions and
answers.
Listening
Speaking
Reading
Writing
Classifying nouns
Do the given texts
A chart showing
kinds of nouns
and examples.
Detailed Eng. Grammar
pgs 79 – 103
2
• Collective nouns e.g. herd of
cattle.
• Abstract nouns e.g. poor –
poverty.
• Formation of abstract nouns
• Uses the given nouns
in sentences
correctly.
• Forms abstract nouns
correctly.
3 2pds NOUNS
Singulars and plurals
• How plurals are formed
• By adding “s” “es” “ies”
• By changing “f” to “v” add “es”
• Nouns which have the same
form for both singular and plural
e.g. fish, deer.
• Irregular formations
• Compound nouns
• Uncountable nouns
Learners:
• Differentiates btn
singular and plural.
• Forms plurals of
nouns using s,
es,ies or ves.
• Completes given
exercise.
• Discussion through
question and
answer.
• Explanation
• Listening
• Speaking
• Reading
• Writing
• Critical
thinking
• Effective
communication
• Differentiates btn
singular and
plural.
• Forming plurals of
nouns as guided.
• Changing from
</passage>

<passage id="lchk_099286fd9988461b92bca1780922d342" source="P 6 Primary SIX ENG Notes Teacher AC" part="23">
2. I want to see the menu. May I see the menu, please?
3. I wish to have rice and chicken. May I have rice and chicken, please?
Activity
Rewrite the following beginning: May I ……….., please?
1. Pass me the sugar bowl.
2. I would like a glass of cold water.
3. I need some more salt
4. Send me a tooth pick.
5. I want to see the chef
6. Where is the cashier
7. I need a bottle of soda
8. I wish to have a cup of milk
9. Pass me a serviette
10. I need some more sauce
Using ………..may………
Examples
1. Victorious primary school pupils may hold their jamboree in Sheraton Hotel
2. The customer may pay the bill in dollars
3. The guest may have a rest in the lounge
Activity
Write ten sentences using………….may………….
49
Lesson four
No sooner………….than………
No sooner is used to show the shortest possible time something happened. It gives the same meaning as shortly after,
immediately, as soon as etc
Note: No sooner comes at the beginning of the sentence
1. No sooner is used to show what happened soonest after the other thing or action
2. The verb after No sooner ‘did’ should be in present simple e.g. go, do, sing, play, see
3. The verb after No sooner ‘had’ should be in past participle e.g. gone, done, sung, eaten, seen, paid
4. Never use No sooner than and as soon as immediately in the same sentence
Example
1. The boss paid for his lunch. The driver came for him.
2. No sooner had the boss paid for his lunch than the driver came for him
3. No sooner did the boss pay for his lunch than the driver cam for him
4. As soon as we started eating, it began raining. No sooner had we started eating, than it began raining
5. No sooner did we start eating than it began raining
Activity
Rewrite the following sentences using: No sooner……….”
1. Jessica followed her father immediately he left the hotel.
2. The waiter saw the customer. He stood up.
3. As soon as she laid the table, she served the guest
4. Timothy paid the bill shortly after he finished eating breakfast
5. Immediately the workers felt hungry, they went to the hotel
6. The bell rang, the pupils lined up for lunch
7. They washed the dishes as soon as the customers stopped eating
8. We served the guest of honour immediately he arrived
Lesson five
Using: Hardly, barely/ scarcely
These words are negative and they go with ‘when’
Examples
1. The boss paid for his lunch. The driver came for him.
2. Hardly had the boss paid for his lunch when the driver came for him
3. Barely had the boss paid for his lunch when the driver came for him
4. Scarcely had the boss paid for his lunch when the driver came for him
Activity
Rewrite the following sentences using ‘No sooner / hardly/ scarcely
1. As soon as the chef gave us food, the waitress brought the cutlery
2. Immediately we entered the conference room, the guest arrived
3. Immediately the guests checked out, the waitress cleaned the room
4. Just as we booked the room, the room attendant gave us the key
5. We served the guest – of – honour just as he arrived
COMPREHENSION
Lesson six
Dialogue
AT THE HOTEL
50
Read the dialogue below and answer questions that follow in full sentences
Waitress: Hello, I am pleased to see you Dr. Kizito
Customer: Thank you, madam
Waitress: Good evening sir
Customer: Good evening madam
Waitress: May I take your order please?
Customer: That is good for you! I have a look at the menu please?
Waitress: Here it is sir, please?
Customer: You know as a doctor, I always prefer a balanced diet
</passage>

<passage id="lchk_699717cc5b2442fead3c75b1947455c4" source="P6–P7 English: Holiday Plans – 'Going to' Structures and Question Tags" part="1">
Ecolebooks.com
DOWNLOAD MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
P.6, 7 ENGLISH LANGUAGE
Topic: Holiday Plans.
01 Language
Structures
By Yasaba Angelo
NB: In order to understand structures at P7, we need to do the following:
a) To know the meaning of the structure.
b) To understand and appreciate its position in a sentence that is at the beginning, within or at the
end of a sentence.
c) To find other related structures which do similar or the same purpose as the one you are going to
teach/learn.
d) Remember to teach/learn this structure with one or two of those related to it.
Topic: Holiday plans.
Structure (1) ----- going to ------ A)
Read these sentences.
a) We are going to plan for our holidays.
b) John is going to buy a new bicycle.
c) These girls are going to weave nice baskets.
B) These sentences mean
a) We shall plan for our holidays
b) John will buy a new bicycle.
c) These girls will weave nice baskets.
Remember: (Primary 4) we use ‘shall’ w ith, I, we
‘Will, with: you, you, he, she, it, they
John, the man, the goat, my mother, etc.
The above sentences can also be written as :
a) We are likely to plan for our holidays.
b) John is likely to buy a new bicycles.
c) These girls are likely to weave nice baskets.
We can also rewrite the above sentences using ‘’……look(s) forward to ……..’
Ecolebooks.com
DOWNLOAD MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
a) We look forward to planning for our holidays.
b) John looks forward to buying a new bicycle.
c) These girls look forward to weaving nice baskets.
Remember : All the above sentences tell us of the future (time to come)
Exercise:
a) Rewrite the sentences using:…………going to ………………..
(i) I look forward to visiting my friend next term.
(ii) We are likely to hold a sports day this term.
(iii) Kepere will bake a cake for us tomorrow.
(iv) You and I shall play tennis during the holidays.
(v) You look forward to building a hutch for your rabbit.
(vi) The teachers will mark our examinations.
(vii) Okello looks forward to attending remedial lessons.
(viii) (viii)Will the boy attend the bath?
(ix) Do you look forward to celebrating the birthday?
(x) Shall I go with you to the picnic?
(xi) Are the children likely to stage a drama show?
b) Rew rite the sentences using: Will……or……..shall……….
(i) Tomasi is likely to repair his bicycle.
(ii) The farmers look forward to plaiting their crops.
(iii) Jacinta is going to write a composition.
(iv) The mechanic is not likely to repair my bicycle.
(v) We are not going to travel during the holidays . (c) Rewrite the sentences
using:…………. Likely to…………..
(i) I shall tour the national park.
(ii) We shall do the homework next week.
(iii) Yasaba is looking forward to joining the scouts club.
(iv) Dr Batima is going to visit the patients next Monday.
(v) We don’t hope to miss classes this afternoon.
(vi) Are the health officers going to have a holiday?
(vii) Kibone won’t write a letter to Hannah this term.
(viii) Porombo and Sarah are going to the national theatre.
(ix) All our parents may visit school tomorrow.
(x) You and I look forward to going the market.
Ecolebooks.com
DOWNLOAD MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
(d) Rewrite the sentences using:……….look(s) forward to……
(i) Iam likely to start a poultry farm.
(ii) Josephine is go ing to go to her parent’s home.
(iii) All the choir members will have a trip to Jinja.
(vi) The teachers may give us presents at the end of the term.
(iv) We shall break up for holidays on Sunday.
</passage>

<passage id="lchk_1f27f60dccfb4be1a52dd816a77c1ed2" source="Primary Six English Lesson Notes 2020 – Yudesi Primary School" part="31">
It is used when something was done and yet it was not necessary.
1. Kato needn’t stone the teacher, he will know.
Kato needn’t have stoned the teacher, he would know.
2. It was not necessary for me to go to church .
I needn’t have gone to church.
Activity
1. There was no need for him to go away.
2. It was not necessary for me to revise since I finished my exams.
3. There was no need for us to walk to town, but we did.
Lesson seven
Use of should and ought to
They have the same meaning.
Examples
You should respect elders.
You ought to respect elders.
Activity
Make twenty sentences using should and ought to
NB: The negative form of should and ought to is oughtn’t to
Examples
You should abuse people.
You oughtn’t to abuse people.
Activity
Rewrite the following sentences using ‘oughtn’t to’
1. Don’t fight with friends.
2. You should play in class.
3. Peter should stay at home today.
4. Don’t go to the forest alone.
</passage>

<passage id="lchk_efa31369f7934c45b374951d6c7d3574" source="BOT III P6 ENG" part="1">
Name:

NAMAGUNGA PRIMARY BOARDING SCHOOL
BEGINNING OF TERM III EXAMINATION - 2022

ENGLISH
PRIMARY SIX

Time allowed: 2 Hours 15 Minutes

Read the following instructions carefully.

BF WwNe

This paper has two sections: A and B.
Section A has 50 questions (50 marks)
Section B has 5 questions (SOmarks)
Answer all questions. All answers to both
sections A and B must be written in spaces
provided.

All answers must be clearly written using
blue or black ball point pen or ink.
Unnecessary changes of work may lead to
loss of marks.

Any handwriting that cannot be easily read,
may lead to loss of marks.

Do not fill anything in the boxes indicated

For examiner’s use only.

FOR EXAMINER'S USE ONLY
Qn. No. MARKS | EXR’S NO.
LL a

1-10
11-20
[= =30 | ~
31-40 7 7
41-50
Z |
61
52
|
53
84 T
65 |
[ v
TOTAL
=

CamScanner

SECTION A

SUB SECTION 1 . _
stions 1 to 5, fill the blank space with a suitablé word.

In que
¢ herdsmen were stung by a ......eeseesereeeerees

. Th
> Most vcseessereeeteeseestens make beds and chairs for their customers.
Bo ceeeeneeeerereeneeeeeeess high Mount Rwenzori is!
4, Juma did the exercises all by «0.0... escecsseereneresereee
5. cescesseececereeseeseeeneeees is the new teacher’s name?

For each of the questions 6-15, fill the blank space with the
correct form of the word in brackets.

6. Daniel received the news about his good performance with

(please)

7. The bus driver Arove SO .....ccsseeeeseeeeeeeeeeeenn ees that he caused an

accident. (care)

8. Tom attends computer lessons a week. (two)

on Mr. Guna’s

9. The pupils have gone to see the

poultry farm. (goose)
10. Mrs. Mubirtt is & ....ceeeereeeneeeeseeeees baker in Kayunga Town, (fame:

11. Had my friends helped me, I
time. (complete)

12. The National Anthem is being
choir now. (sing) .
13. None of the waiting travellers knows the ara
of the plane. (depart)

14. Orne Of 0... eeceeeec eee ee eee ee

brothers is sick. (they)

CamScanner

entered our house and stole the

10 people
an revision set. (steal)
17, construct correct sent i
tions 16 and > : ences using these
Jn ques how that you know the difference in their meaning.

words to §
16, bath esvsvssssreeesseesesennnneneereseenetensaasseeeecnsetesuneeeuaaennaaessense

In questions 18 and 19, arrange the words alphabetically.

18. Wednesday Tuesday Sunday Monday

In questions 20 and 21, write the short form of these words.

QO. SECTION ..cceceeseeceecececeeneeeeeeneneeneees |

In questions 22 and 23, rewrite the sentence giving the plural

form of the underlined words.

22. The thief was arrested by the policemen.

In questions 24 and 25, arrange the words to form a correct
sentence. ;
24. cyclist his to remember helmet did wear the?

25. I related Kate and are. X

In questions 26 and 27, rewrite the sentence giving We EoE KS,
the underlined words.

26. My father filled a deposit form when he went to the bank.

In questions 28 to 30, rewrite the sentence giving one word for
the underlined group of words.

28. My cousin is still a man who is unmarried upto now.

29. The driver braked the bus the moment he saw a pedestrian
crossing the road.

SUB SECTION II
In questions 31 to 50, rewrite the sentence as instructed in

brackets.
31. How much money did that dress cost you?


32. My father has not withdrawn the money.
My mother has not withdrawn the money.
(Join beginning: Neither.............. TOF. eeeeeeeeeeees )

33. The teacher gave us questions which were not direct.
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
