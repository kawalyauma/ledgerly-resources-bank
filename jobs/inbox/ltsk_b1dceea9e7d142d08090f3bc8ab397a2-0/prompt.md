# Job ltsk_b1dceea9e7d142d08090f3bc8ab397a2-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for English, Primary Two 2026, Term 3.
The term has 10 teaching weeks and this subject has 7 periods per week. Every lesson is ONE 40-minute period, so keep each lesson small enough to teach in 40 minutes.
Ledgerly reserves the last lesson of each week for a review of that week.
Give at most 60 teaching/practice lesson entries in teaching order (the last lesson of the term is the end of term assessment).
Each lesson has a kind: "teach" (new content) or "practice" (the same subtopic as the teaching lesson just before it: exercises, oral work, drawing, matching, filling in blanks, ALL taken from the passages).
When the material is thin (common in lower primary), follow each teaching lesson with a practice lesson. Split big subtopics over several teaching lessons.
Never pad with content the passages do not have: if they cannot fill the term, return fewer lessons and list what is missing in gaps. Ledgerly fills the remaining weeks with revision.
You are composing the SCHOOL'S OWN scheme. The passages below (the official NCDC curriculum and guides, plus schemes of work, lesson plans, notes and past papers from the school e-library) are reference material:
The school's SCHEMES OF WORK for this class and term ("P 2 Primary TWO Scheme OF Work General Teacher AC") are the BASE: follow the topics, subtopics and week-by-week order they agree on. Every topic they list for this term MUST become a unit, in their order, and their subtopics become the lessons, with about the pacing they give. Cite their passages in sourcePassageIds of every lesson that follows them.
The NCDC documents (titles starting "NCDC") only FILL GAPS: a topic NCDC lists for this term that the schemes lack gets its own unit where it fits best. Never drop or rename a schemes-of-work topic to fit NCDC. NCDC lower-primary thematic curricula list every learning area side by side in table columns separated by " | ": take only the English column.
Combine them in this authority order: the school's schemes of work for topics, sequence and pacing; NCDC for anything they miss; the strongest detailed notes for accurate teaching depth; past papers for expected applications and activities.
Use this term's part of the material (Term 3) when the passages cover several terms.

NCDC topics for Primary Two 2026, Term 3 that must ALSO be covered. Each needs at least one unit whose title or theme names it; the school's schemes of work decide where it goes and how many lessons it gets:
  1. (Weeks 1-3)
  2. (Weeks 4-5)
Do NOT write lesson content yet. Each unit and lesson must cite the passage ids it comes from in sourcePassageIds.

Reply shape:
{"title":string,"summary":string,"units":[{"title":string,"theme":string|null,"weekFrom":int|null,"weekTo":int|null,"competences":string|null,"sourcePassageIds":[string],"lessons":[{"title":string,"subtopic":string|null,"kind":"teach"|"practice","objectives":[string],"sourcePassageIds":[string]}]}],"gaps":[string]}

<passages>
<passage id="lchk_aa675499326849b4b8f192f968303357" source="NCDC P2 Thematic Curriculum June" part="1">
THE REPUBLIC OF UGANDA
Ministry of Education and Sports

Primary School Curriculum

Primary 2

National Curriculum Development Centre

-1-

Contents

PAGE
Acknowledgement…………………………………………………… | 3

Foreword………………………………………………………………... | 4

Section A: Introduction | 5

1. | The National Aims of Education……………………………………………. | 6

2. | The Aims and Objectives of Primary Education…………………………….. | 6

3. | The Organisation of the Primary Curriculum | 7

4. | The Overall Approach in P1-P3……………………………………………… | 8

5. | The Organisation of the Thematic Curriculum in P1-P3……………………... | 10

6. | The Approach to Assessment………………………………………………… | 12

Section B: Curriculum Scope and Sequence | 13

7. | The Thematic Strands………………………………………………………... | 14

8. | Religious Education………………………………………………………….. | 51

a) CRE……………………………………………………………………… | 51
b) IRE……………………………………………………………………...... | 62

9. | Physical Education…………………………………………………………… | 70

-2-

Acknowledgement

The National Curriculum Development Centre (NCDC) gratefully acknowledges the efforts, commitment
and contributions of the Thematic Curriculum Review Panel (TCRP) who worked very tirelessly on the
preparations and production of the Primary Two Thematic Curriculum.

The NCDC would also like to recognise the invaluable advice offered by the Consultants during the
process of the development of the Curriculum.

The preparation of this Curriculum benefited greatly from the support and valuable contributions of the
Curriculum Task Force (CTF). NCDC would therefore like to express sincere appreciation to those
members of the CTF who provided extremely useful comments, suggestions and inputs during the
drafting and finalisation of the Curriculum.

Special thanks go to the Permanent Secretary, Ministry of Education and Sports for ensuring the timely
release of the funds to support the development of this document.

There is no doubt that the successful completion of this Curriculum could not have been realised without
the cooperation and willingness of all the different institutions:

• | The Management of the Teacher’s Colleges and Primary Schools for having permitted their members
of staff for longer periods of absence from duty during the writing sessions.

• | The Management of the Primary Schools that allowed NCDC to use their schools for piloting the
drafts of the Thematic Curriculum for the purposes of coming up with a quality final Curriculum.

• | The District Education Officers in the trial districts for the support, supervision and encouragement
to the teachers during the pilot phase of this Curriculum.

Last but not least, thanks to all those behind the scenes – groups of people, organisations and individuals
who formed part of the team that worked so hard on the preparation and production of this document.

Connie Kateeba
Director, National Curriculum Development Centre - NCDC

-3-

FOREWORD
The Curriculum for Primary One – Primary Three
(P1-P3)
Hon. Geradine Namirembe
Bitamazire (MP)

The failure by a high proportion of the children to attain acceptable levels of proficiency in reading and writing at Primary
Three (3) level is considered to be a barrier to the children’s full enjoyment of their right to education as enshrined in Section
30 of the Constitution of the Republic of Uganda (1995 Edition). Sector-wide reflection on this phenomenon has led to
identification of challenges which need urgent attention to make schooling more beneficial to the children. The Ministry
</passage>

<passage id="lchk_5eb337d321c141418c9df1b957220895" source="NCDC P2 Thematic Curriculum June" part="39">
Learning Outcome 9: | The child understands and appreciates the concepts and values of “honesty” and “fairness”.

Sub-theme | Content | Competences | Life skills | Values
• How dishonesty brings | • Talking about the meaning of honesty and fairness | • Effective | • Loyalty
Honesty and Fairness | conflict e.g. Jacob and | • Narrating our experiences in relation to honesty | communication | • Honesty
Rebecca, Cain and Abel, | and fairness | • Assertiveness | • Cooperation
Esau and Jacob. | • Identifying ways of being fair and honest | • Self esteem | • Togetherness
- (Gen 27: 1-44) | • Explaining results of honesty and dishonesty | • Problem-solving | • Trust
• Talking about occasions when we can be fair in | • Critical thinking | • Appreciation
• | The need for honesty and | different situations | • Coping with stress | • Endurance
its benefits | • Writing words and sentences on honesty and | • Coping with emotions | • Patience
- | (Psalms 5: 2-5) | fairness
• Telling stories
• | Occasions when we can | • Singing songs
be fair in different | • Debating
situations

Assessment Guidelines for Weeks 1-3
• Narrate some parts of the story of Esau and Jacob.
• Identify different ways of being dishonest and its consequences.
• Talk about the importance of honesty.
• Talk about situations in which we need to be fair.
• Talk about benefits of being fair to others.

- 59 -

THEME: | CHRISTIANS LIVING TOGETHER IN GOD’S FAMILY
Weeks 4-6
Learning Outcome 10: | The child shows concern for others and appreciates the importance of kindness and generosity to those in need.

Sub-theme | Content | Competences | Life skills | Values
Concern for others | • Showing concern for others e.g. David | • Talking about ways of showing concern | • Empathy | • Appreciation
and Jonathan, (1 Sam 20-23) | • Explaining ways of showing concern for others | • Effective | • Loyalty
• The widow and Elisha (2 Kings 4: 1-7) | • Telling / re-telling / signing stories | communication | • Kindness
• Ways of showing concern (Ruth and | • Identifying ways of expressing concern for others | • Friendship formation | • Patience
Naomi) | • Role-playing | • Coping with emotions | • Care
• Ruth 1: 16-18 | • Drawing | • Problem-solving | • Love
• Ways we can show concern for others | • Singing | • Coping with stress
in our daily life. | • Practising concern for others in the community

Assessment Guidelines for Weeks 4-6:
• Talk about situations in which we can show concern for others.
• Narrate some parts of the story of Ruth and Naomi.
• Talk about the importance of showing concern for others.

THEME: | CHRISTIANS LIVING TOGETHER IN GOD’S FAMILY
Weeks 7-9
Learning Outcome 11: | The child knows Jesus as God’s greatest gift to us and appreciates celebrating Christmas.
Sub-theme | Content | Competencies | Life skills | Values
• God’s promise of His Son to be | • Drawing pictures of Christmas events | • Creative thinking | • Appreciation
God’s Gift of His Son | born for us (Matt 1: 21) | • Telling why God gave his Son to us | • Critical thinking | • Endurance
- Isaiah 9: 6-7 | • Telling the importance of giving out to others | • Interpersonal | • Loyalty
• Narrating incidences when we have given and received | relationship | • Honesty
• | How and why God gave his | gifts | • Coping with emotions | • Respect
beloved Son, Jesus as a gift to us | • Explaining how we feel when we give or receive gifts | • Coping with stress | • Love
</passage>

<passage id="lchk_57e08c1671f04ec4bde84554a7024b7a" source="NCDC P2 Thematic Curriculum June" part="49">
• Frog jump | • Arranging | communication | • Confidence
• Aim and target | • Dodging | • Leadership
• Nyonyi telima muwemba (Luganda) | • Counting | • Acceptance
• Nyanyanya (Adhola) | • Singing
• Apoliapoli camo poto (Luo) | • Dancing
• Kolabwoti kola ssebo (Luganda)

Assessment Guidelines (Weeks 7-9)
• Batting balls (accuracy, target, speed, timing)
• Squatting (balance persistence)
• Arranging (orderliness, speed, timing)
• Dodging ( co-ordination, speed, timing)

Term III, Weeks 10-12 | Games for Lower Primary
Content | Activities | Competences | Life skills | Values
(abilities, skills and knowledge)
• Dress up | • | Dressing | • | Self-esteem | • | Cooperation
Games for Lower Primary | • Keep the basket full | • | Drumming | • | Interpersonal relationship | • | Acceptance
Reaction games | • Drum relay | • | Running | • | Coping with emotion | • | Appreciation
• Three-legged race | • | Identifying | • | Critical thinking | • | Endurance
• Blind fold | • | Balancing | • | Confidence
• Sack race | • | Responsibility
• He / she game | • | Respect
• Status

Assessment Guidelines (Weeks 10-12)
• Alertness and steadiness
• Obey commands
• Respond to instructions correctly
• Balance in three-legged race
• Coordination

- 78 -
</passage>

<passage id="lchk_31436551020a48908d5964bdb363d262" source="P 2 Primary TWO Scheme OF Work General Teacher AC" part="1">
1
PRIMARY TWO SCHEME OF WORK
W
K
P
D
THEME S/THEME L/A CONTENT COMPETENCE METHODS ACTIVITY LIFE SKILLS L/AIDS REF R
M
1
TUE
OUR ENVIRONMENT
COMMON ANIMALS
GOING THROUGH HOLIDAY WORK
WE
DD
DD GOING THROUGH HOLIDAY WORK
THU
R GOING THROUGH HOLIDAY WORK
FRI
ENG
Adjectives
Comparison of
adjectives
Reads the
words given .
Adds er and est
to show
superlative and
comparative
degree
Demonstration
Dramatization
Discussion
Reading the
words and
using them in
sentences.
Writing and
using the
adjectives in
sentences.
Creative
thinking
.Effective
communic
ation.
Critical
thinking.
Chalkboar
d
illustrations.
A chart
showing
adjectives.
Junior English Bk 2 Page 80.
FRI
LIT
• Sound ng
• Words and
sentences
Pronounces
given words.
Spellls words
using the
structures learnt
Whole class
discussion
Pronouncing
given words
Answering oral
and written
questions
Creative
thinking
Critical
thinking
A chart
showing
animals
and their
young
ones
Junior English bk 2
pg 41-42
2
1
FRI
NEWS
R
E
V I S I O N
FRI
MTC
Counting from 501 –
600
Writing number words
- counts
- writes number words.
2
MON
ENG
Alphabetical order by
the second letters e.g
Craw, close, chicken,
cow
Identifies the
second letters
of the given
words.
Arranges words
in alphabetical
order.
Whole class
discussion
Brainstorming
Arranging
words in ABC
order
Creative
thinking
Critical
thinking
Chalkbo
ard
illustratio
n
Junior English bk 2 pg 28
MON
OUR ENVIRONMENT
COMMON ANIMALS
NEWS
Domestic and wild
animals
Definition of domestic
and wild animals.
Examples of domestic
and wild animals.
Caring for animals
Gives the
differences
between wild
and domestic
animals.
Names the
animals
Whole class
discussion
Brainstorming
Writing
Naming
Drawing
Creative
thinking
Effective
communic
ation
Critical
thinking
Textbook
s
A chart
C/b
illustratio
n
Mk integrated prim Scie bk 2
page 7-9
3
2
MON
LIT
Sound ‘ng’ wing, sing,
bring
Sentences
Letter pattern
Kk Kk Kk Kk Kk
Identifies the
words
ReadS
Writes words
correctly
Whole class
discussion
Brainstorming
Reading and
writing
Creative
thinking
Effective
communic
ation
A chart
C/b
illustratio
n
Tr’ s collection
MON
MTC
Counting from 601 –
700
Writing number words
Counts the
given numbers.
Reads and
Writes number
words.
Whole class
discussion
Brainstorming
Counting
Reading
Writing
Creative
thinking
Appreciati
on
Respect
Textbook
s C/b
illustratio
ns
Vikas Gollgen Maths
P g 33
TUE
OUR ENVIRONMENT
COMMON ANIMALS
LIT
Spelling and dictation Pronounces
given words
Spells given
words
Whole class
discussion
Brainstorming
Spelling
writing
Critical
thinking
Creative
thinking
Effective
communic
ation
A chart
C/b
illustratio
ns
4
TUE
MATHS
Counting from 701 -
800
Counts the
given numbers.
Reads and
writes number
words.
Whole class
discussion
Brainstorming
Counting
Reading
Writing
Critical
thinking
Text
books
C / B
Illustrastio
ns
Vikas Golden Maths
pg 34
2
TUE
ENG
Alphabetical order by
the third letter.
Writes given
words in
alphabetical
order.
Whole class
discussion
Brainstorming
Writing given
words in
alphabetical
order.
Creative
thinking
Effective
communic
ation
Critical
thinking
C/b
illustratio
ns
Standard English Book3
B33.Junior
TUE
NEWS
How animals and
birds move.
Birds – fly
People – walk
Snakes - Glide
Identifies the
words
Names the
animal
movements
Whole class
discussion
Brainstorming
Identifying
Naming
Writing
Creative
thinking
Critical
thinking
A chart
C/b
illustratio
ns
MK Integrated Prim
Scie BK 2 pg 2-3
WED
OUR ENVIRONMENT
COMMON ANIMALS
LIT
Comprehension Reads
Answers
</passage>

<passage id="lchk_9e897a759907470d87aa3142469afddf" source="P 2 Primary TWO Scheme OF Work General Teacher AC" part="2">
questions
Whole class
discussion
Brainstorming
Reading
Writing
Answering
questions
Creative
thinking
Effective
communic
ation
Critical
thinking
A chart
c/B
Illustratio
n
5
WED
MATHS
Counting from 801
To 1000
Counts the
given numbers
Writes the
number words
Whole class
discussion
Brainstorming
Counting
Reading
Critical
thinking
Problem
solving
c/B
Illustratio
n
Text
books
VIikas Golgen Maths
Pg 35__38
2
WED
NEWS
How animals protect
themselves.
Bee/ wasp-sting
Names
Identifies
Describes
Imitating
Brainstorming
Naming
Writing
Creative
thinking
Effective
communic
ation
Text
books
Charts
C/b
illustratio
n
MK Integrated Prim
Scie BK 2 page 5
WED
OUR ENVIRONMENT
COMMON ANIMALS
LIT
Composition Reads
Writes
Answers
questions
Whole class
discussion
Brainstorming
Reading
Writing
Answering
questions
Creative
thinking
Effective
communic
ation
Critical
thinking
C/B
Illustratio
n
MK Integrated Prim Scie
BK 2 page 1.
6
THUR
ENG
Structure ‘when’
Re-writing as
instructed
Re-writes as
instructed.
Whole class
discussion
Brainstorming
Reading and
writing
Creative
thinking
Effective
communic
ation
Critical
thinking
Text
books
C/B
Illustratio
n
Read and Write Bk Two pg
THUR
MATHS
Finding the missing
numbers
Fills in the
missing number.
Finds numbers
before and
after.
Whole class
discussion Writing
Counting
Filling
Creative
thinking
Effective
communic
ation
Critical
thinking
C/B
Illustratio
n
Vikas Golden Maths
Pgs 32 ___38
THUR
NEWS
Uses of animals and
birds (domestic)
Names the birds
Identifies
Describes
Whole class
discussion
Writing
Answering
questions
Creative
thinking
Effective
communicat
ion
Critical
thinking
C/B
Illustratio
n
MK Integrated Prim Scie
BK 2 page 7.
7
THUR
LIT
Sound ‘le”
Let
Letter
-Letter pattern
Ss Ss Ss Ss Ss Ss Ss
Pronounces the
given letter
sounds.
Whole class
discussion
Brainstorming
Reading
Writing
Creative
thinking
Effective
communicat
ion
C/B
Illustratio
n
FRI
WEEKLY TESTS
3
MON
ENG
Adjectives that
double the last letter.
Finds adjectives
which double
the last letter to
form adjectives.
Whole class
discussion
Brainstorming
Writing
opposites
Creative
thinking
Effective
communicat
ion
Critical
thinking
Textboo
ks
C/B
Illustratio
n
Junior English bk 1 pg
86.
MON
Capacity
MATHS
Writing number words
in figures
Writes number
words.
Whole class
discussion
Brainstorming
Writing
Rreading
Creative
thinking
Effective
communicat
ion
Critical
thinking
Textboo
ks
C/B
Illustratio
n
Vikas Golden Maths
Pg 32 ___ 38
8
MON
OUR ENVIRONMENT
COMMON ANIMALS
NEWS
Uses of animals and
birds (wild)
Names
Identifies
Describes uses
of the birds
Whole class
discussion
Brainstorming
Naming the
uses of the
given
animals.
Creative
thinking
Effective
communicat
ion
Critical
thinking
Textboo
ks
C/B
Illustratio
n
MK Integrated Prim Scie
BK 2 page 10.
3
MON
LIT
Spelling and dictation
Stems, roots, water,
e.t.c
Spells given
words.
Whole class
discussion
Brainstorming
Spelling
Writing
Creative
thinking
Effective
communicat
ion
Critical
thinking
Textboo
ks
C/B
Illustratio
n
MK Integrated Prim Scie
BK 2 page 63-73
TUE
ENG
A passage about
plants.
Pronounces
new words.
Spells words
learnt.
Reads and
answers in full
sentences.
Whole class
discussion
Brainstorming
Spelling
words
Constructing
sentences.
Creative
thinking
Effective
communicat
ion
Critical
thinking
C/B
Illustratio
n
Prim Currr. Bk 2.
9
TUE
Place values and values
MATHS
Place values up to
1000
Works out place
values up to
1000.
Whole class
discussion
Brainstorming
Oral work
Working out
place values
Creative
</passage>

<passage id="lchk_241ec21aefe94b29affbe9e824f82ca6" source="P 2 Primary TWO Scheme OF Work General Teacher AC" part="3">
thinking
Effective
communicat
ion
Critical
thinking
Text
books
C/B
Illustratio
n
MK BK 3 , Understanding
Mtc bk 2
3
TUE
NEWS
Names of common
insects.
Useful insects e.g.
Grasshoppers.
Names
Identifies
Groups
Describes
Whole class
discussion
Brainstorming
Oral and
Written work
Creative
thinking
Effective
communicat
ion
Critical
thinking
Some
insects
Chart
C/B
Illustratio
n
MK Integrated Prim Scie
BK 2 page 19.
TUE
OUR ENVIRONMENT
COMMON ANIMALS
LIT
Comprehension
about plants.
Reads
Writies
Answers
questions.
Whole class
discussion
Brainstorming
Reading
Writing
Answering
questions
Creative
thinking
Effective
communicat
ion
Critical
thinking
C/B
Illustratio
n
10
WED
ENG
Uses of some and any Identifies
Sentences to fill
in with some
and any.
Whole class
discussion
Filling in
missing
words.
Creative
thinking
Effective
communicat
ion
Critical
thinking
Text
books
C/B
Illustratio
n
Eng aid bk 3 pg 46.
WED
MTC
Values of numbers Finds values of
numbers.
Whole class
discussion
Brainstorming
Identifies
values of
numbers.
Creative
thinking
Critical
thinking
C/B
Illustratio
n
MK Primary MTC
BK 2. Pri Sch Mtc
b
3
WED
NEWS
Harmful insects. These
are insects which are
dangerous to us.
Identifies
dangerous
insects.
Whole class
discussion
Brainstorming
Identifying
Writing
Creative
thinking
Effective
communicat
ion
Critical
thinking
Env’t
MK Integrated Scie bk 2 pg
17, Teacher’ s collection.
11
WED
LIT
Guided composition
about plants.
Reads
Writes
Answers
questions.
Whole class
discussion
Brainstorming
Reading
Writing
Answering
questions.
Creative
thinking
Effective
communicat
ion
Critical
thinking
C/B
Illustratio
n
THU
ENGLISH
Opposites of
adjectives
Identifies
opposites of
adjectives.
Reads spells
correctly.
Whole class
discussion
Brainstorming
Identifying
Opposites of
adjectives
Filling in
exercise.
Creative
thinking
Effective
communicat
ion
Critical
thinking
A chart
on
opposite
s of
adjectiv
es
Std Eng Book 3 pg 39.
THUR
Forming
numbers
MTC
Forming numbers from
3 digit numbers
Forms numbers
Group
discussion
Brainstorming
Forming new
numbers
Critical
thinking
Sharing.
Textboo
ks
Real
objects.
Understanding
Mtc bk 2
3
THUR
NEWS
The life cycles of
insects
Names
Explains
Whole class
discussion
Brainstorming
Naming
Drawing
Creative
thinking
Effective
communicat
ion
Textboo
ks
Charts
MK Integrated
Scie bk 2 pg 15,
12
THUR
LIT
Sound “oo”
Sentences
Letter pattern
Ee Ee Ee Ee
Spells
Reads
Whole class
discussion
Brainstorming
Reading
Spelling
Writing
Critical
thinking
A chart
on
pronoun
s
Teacher’ s
collection.
FRI
ENG
Possessive pronouns Identifies
possessive
pronouns
Underlines
possessive
pronouns
Whole class
discussion
Brainstorming
Identifying
Underlining
Creative
thinking
Effective
communicat
ion
Critical
thinking
A chart
on
pronoun
s
Std Eng Pg 35,
Eng aid bk 3 pg 61
FRI
Operation of
numbers
MTC
Addition of 2 digit
numbers with re-
grouping
Adds numbers
Re – groups
numbers
Whole class
discussion
Demonstration
Adding orally
Writing
written work
Critical
thinking
Problem
solving
Paper
pair of
scissors
Fruits
MK Primary MTC
BK 2 and Bk 3
3
FRI
NEWS
Naming the main
parts of an insect.
Names each
part of an
insect.
Whole class
discussion
Brainstorming
Writing
Drawing
Creative
thinking
Effective
communicat
ion
Critical
thinking
Textboo
ks.
A chart
MK Integrated Scie bk 2
pg 13.
13
4
MON
LIT
Spellings and
dictations.
Spells the given
words.
Whole class
discussion
Brainstorming
Spelling
Writing
Creative
thinking
Effective
communicat
ion
Critical
thinking
C/B
</passage>

<passage id="lchk_75b570bf3ffa43249f1c0d052d783c26" source="NCDC P2 English Teachers Resource book" part="1">
Teacher’s Resource Book, Primary 2

Ministry of Education, Science,
Technology and Sports

The National Primary School
Curriculum for Uganda

ENGLISH
Teacher’s Resource Book
Primary Two

A

Ministry of Education, Science,
Technology and Sports

The National Primary School
Curriculum for Uganda

ENGLISH
Teacher’s Resource Book
Primary Two

© National Curriculum Development Centre, Uganda

Reprinted, 2016
National Curriculum Development Centre,
P.O. Box 7002,
Kampala.

ISBN: 978-9970-00-161-3

All rights reserved. No part of this publication may be reproduced,
stored in a retrieval system, transmitted in any form or by any means;
electronic, mechanical, photocopying, recording or otherwise without
the prior written permission of the publisher.

Website: www.ncdc.go.ug

Teacher’s Resource Book, Primary 2

Contents
Acknowledgment ................................................................................................................. v
Foreword .............................................................................................................................vi
PART A: INTRODUCTION TO THE TEACHER’S RESOURCE BOOK .................... 1
What is a Teacher’s Resource Book? .............................................................................................. 1
Rationale .............................................................................................................................................. 1
Objectives............................................................................................................................................ 1
How to use the Teacher’s Resource Book ..................................................................................... 1
PART B: CONCEPT WORDS............................................................................................ 2
Theme 1: Our School and Neighbourhood ................................................................................... 2
Theme 2: Our Home and Community ........................................................................................... 2
Theme 3: Human Body and Health ................................................................................................ 2
Theme 4: Food and Nutrition .......................................................................................................... 3
Theme 6: Things we Make................................................................................................................ 3
Theme 7: Transport in Our Community ........................................................................................ 3
Theme 8: Accidents and Safety in Our Community ..................................................................... 4
Theme 10: Child Protection ............................................................................................................. 4
Theme 11: Measures .......................................................................................................................... 4
Physical Education ............................................................................................................................. 4
Christian Religious Education .......................................................................................................... 5
Sight Words......................................................................................................................................... 5
</passage>

<passage id="lchk_e54641066cc54deeb3180c39cd998459" source="NCDC P2 Teachers Guide" part="1">
Teacher’s Guide, Primary 2

Ministry of Education, Science,
Technology and Sports

The National Primary School
Curriculum for Uganda

Teacher’s Guide, Primary 2

a

Ministry of Education, Science,
Technology and Sports

The National Primary School
Curriculum for Uganda

Teacher’s Guide, Primary 2

National Curriculum Development Centre

© National Curriculum Development Centre, Uganda

Reprinted, 2016
National Curriculum Development Centre,
P.O. Box 7002,
Kampala.

ISBN: 978-9970-00-160-6

All rights reserved. No part of this publication may be reproduced,
stored in a retrieval system, transmitted in any form or by any means;
electronic, mechanical, photocopying, recording or otherwise without
the prior written permission of the publisher.

Website: www.ncdc.go.ug

ii

Teacher’s Guide, Primary 2

Contents
Acknowledgment ............................................................................................................................ vi
Foreword ....................................................................................................................................... vii
Abbreviations ................................................................................................................................ viii
PART A: BACKGROUND AND METHODOLOGY ................................................................. 1
1. | How to Use this Teacher‟s Guide ................................................................................... 1
2. | Methodology for Teaching the Thematic Curriculum ................................................... 2
2.1 Learner-centred Learning ....................................................................................................................... 2
2.2 Class Management ................................................................................................................................... 2
2.3 Using Instructional Materials ................................................................................................................. 4
2.4 Working with Learners who have Special Needs ............................................................................... 5
2.5 The Timetable .......................................................................................................................................... 5
3. | Life Skills and Values ...................................................................................................... 7
4. | Teaching Mathematics.................................................................................................. 10
4.1 Rationale | ........................................................................................................................................ 10
4.2 Teaching Procedures (TPs) for Mathematics .................................................................................... 16
4.3 Suggested Materials for Mathematics in P2 ....................................................................................... 18
5. | Teaching Literacy ......................................................................................................... 20
5.1 Rationale | ........................................................................................................................................ 20
5.2 What do we Mean by Literacy? ........................................................................................................... 20
</passage>

<passage id="lchk_35a9ba8196ef4fdfac4206b20bc2f990" source="Eng P.2 notes" part="22">
Vocabulary and structures
28. Collective nouns
TERM III TOPICAL BREAKDOWN
1 Theme: peace and security
Vocabulary: teacher, child, prefect, prison
2 Structures
Show me a/ an/ the ……….
This / that is a/ an ………..
Who ………… teaches, preaches?
A teacher/ Imam……..
3 Present continuous tense
Those that add ‘ing’ straight away
Those that end with ‘e’
Those that double the last letter
4 Present simple tense
Contact: 0754895241/0783298434
Email: tekule@tekartlearning.com
Website: www.tekartlearning.com
58
Verb s that add ‘s’
Verbs that add ‘es’
Verbs that drop the last letter ‘y’ and add ‘ies’
Vocabulary: bank, obey, give, friend, share
5 Structures
What do you like?
Do you like……….? Playing, praying) (Yes, I do, No I don’t)
6 Homophones
Vocabulary: work, share, people, beat, bit
7 Structures
It is good/ bad to…………….
We should not……………….
Always………………….
8 Synonyms
Vocabulary: fear, worry, pain, blind
9 Structures
Are you………..?
Yes, I am / No I am not
Vocabulary: parent, advise, guide, help
10 Structures
It is good t o…….
What should you do always?
You/ I / we should always …………others
11 Gender
12 Past simple tense
Verbs that add ‘d’
Verbs that double the last letter before adding ‘ed’
Verbs that drop ‘y’ and add ‘ied’
13 Past tense of irregular verbs
14 Adjectives: forming adjec tives by adding ‘;ful’
Vocabulary: days of the week
15 Structures
What is the ………day of the week?
……………is the …………day of the week.
16 Cardinal numbers and ordinal numbers (1 – 100)
1 – one – 1 st – first
2 – two – 2 nd – second
17 Months of year
Vocabulary (January, February, March, April
18 Structures
Which month comes before ……..?
………………comes before ……………..
What is the …………….month of the year?
……………is the ………………month of year
Contact: 0754895241/0783298434
Email: tekule@tekartlearning.com
Website: www.tekartlearning.com
59
19 Short forms (days of the week, months of the year
20 Calendar
Vocabulary: day, time, week, hour, year, months
21 Minutes, a quarter past, a half past
22 Use of ‘some’ and ‘any
23 Apostrophe: ownership / short forms
24 Commas
Vocabulary: shillings, coins
25 Structures
May I have………….kilograms/ litres of …….please
How much is a kilo/ litre / packet of…………?
It is…………….
It costs…………….
26 Conjunction ‘and’
27 Adjectives
Examples
28 Opposites
29 Comparisons
Vocabulary: triangle, square, circle
30 Structures
What shape is this?
It is a …………….
How many sides has a triangle?
A triangle has…………..sides
Is this a triangle / circle / square?
Yes, it is/ No it is not
31 Conjunction ‘but’
32 Similes
33 Conjunction ‘because’
34 Future tense
35 proverbs
</passage>

<passage id="lchk_93bfcd0a7ce242c8b51b1f1719458a5d" source="English Language Paper 2 (UCE) Set R – Kiira College Butiki" part="1">
1
KIIRA COLLEGE BUTIKI
Uganda Certificate of Education.
ENGLISH LANGUAGE
Paper 2
1. Read the following passage and answer the questions that follow .
One of the definitions of “democracy” is a system in which all the people
of a country are allowed to freerly elect their representatives. Basic principles
of democratic governments are recognized universally. These principles often
become part of the constitution or bill of rights in a democratic society.
One of the most basic characteristics of democracy is citizen
participation in government. It is not only a right, but also a duty. Citizen
participation may take many forms, including acting as election officials, voting
in elections, becoming informed, debating issues, attending community or civil
meetings, being members of private voluntary organizations and paying taxes.
Participation builds a better democracy.
Secondly, democratic societies emphasize that all people are equal.
“Equality” means that all individuals are valued equally, have equal
opportunities and may not be discriminated against because of their race,
religion, ethic group, gender or sexual orientation.
In democracy individuals and groups still maintain their right to have different
cultures, personalities, languages and beliefs.
Thirdly, democratic societies are tolerant. This means that while the
majority of people rule in a democratic country, the rights of the minority must
be protected. People who are not in power must be allowed to speak out.
Minorities are sometimes referred to as “opposition” because they have ideas
which are different from those of the majority. Individual citizens must also
learn to be tolerant of each other. A democratic society is often composed of
people from different cultures, races, religion and ethnic groups who have
different viewpoints from a majority of the population. A democratic society is
enriched by diversity. If the majority deny rights to and destroy their
opposition, then they also destroy democracy.
Fourthly, in democracy, elected and appointed officials have to be
accountable to the people. They are responsible for their actions. Officials
must make decisions and perform their duties according to the will and wishes
of the people not for themselves.
2
Fifthly, a democratic government must be transparent. A transparent
government holds public meetings and allows citizens to attend. In democracy,
the press and the people are able to get information about what decisions are
being made, by whom and why.
Lastly, it is important for a democratic government to insist that elected
officials are chosen and peacefully removed from the office in a free and fair
manner. Intimidation, corruption and threats to citizens during or before an
election are against the principles of democracy. In democracy, elections are
held regularly. Participation in elections should not be based on a citizen’s
wealth. For free and fair elections to occur, most adult citizens should have
the right to vie for government positions. Additionally, obstacles should not
exist which make it difficult for people to vote.
Question
1. In about 120 words state how a democratic government operates.
ROUGH COPY
………………………………………………………………………………………………………
………………………………………………………………………………………………………
………………………………………………………………………………………………………
………………………………………………………………………………………………………
………………………………………………………………………………………………………
………………………………………………………………………………………………………
………………………………………………………………………………………………………
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
