# Job ltsk_de9a2f907e5b473db26449101aa29d98-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for Christian Religious Education, Primary Two 2026, Term 3.
The term has 10 teaching weeks and this subject has 3 periods per week. Every lesson is ONE 40-minute period, so keep each lesson small enough to teach in 40 minutes.
Ledgerly reserves the last lesson of each week for a review of that week.
Give at most 20 teaching/practice lesson entries in teaching order (the last lesson of the term is the end of term assessment).
Each lesson has a kind: "teach" (new content) or "practice" (the same subtopic as the teaching lesson just before it: exercises, oral work, drawing, matching, filling in blanks, ALL taken from the passages).
When the material is thin (common in lower primary), follow each teaching lesson with a practice lesson. Split big subtopics over several teaching lessons.
Never pad with content the passages do not have: if they cannot fill the term, return fewer lessons and list what is missing in gaps. Ledgerly fills the remaining weeks with revision.
You are composing the SCHOOL'S OWN scheme. The passages below (the official NCDC curriculum and guides, plus schemes of work, lesson plans, notes and past papers from the school e-library) are reference material:
The school's SCHEMES OF WORK for this class and term ("P 2 Primary TWO CRE Scheme OF Work Teacher AC") are the BASE: follow the topics, subtopics and week-by-week order they agree on. Every topic they list for this term MUST become a unit, in their order, and their subtopics become the lessons, with about the pacing they give. Cite their passages in sourcePassageIds of every lesson that follows them.
The NCDC documents (titles starting "NCDC") only FILL GAPS: a topic NCDC lists for this term that the schemes lack gets its own unit where it fits best. Never drop or rename a schemes-of-work topic to fit NCDC. NCDC lower-primary thematic curricula list every learning area side by side in table columns separated by " | ": take only the Christian Religious Education column.
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

<passage id="lchk_c5772b8209c64ec29f34357a8c5bd24d" source="CRE P.2 TEACHERS RESOURCE BOOK 18.01.2023 Web file" part="1">
P
R
I
M
A
R
Y
2
TEACHER’S RESOURCE BOOK
CHRISTIAN RELIGIOUS EDUCATION
TEACHER’S RESOURCE BOOK
P
R
I
M
A
R
Y
2
CHRISTIAN
RELIGIOUS
EDUCATION
Copyright © National Curriculum Development Centre, Uganda, 2020
A product of the National Curriculum Development Centre for the
Ministry of Education and Sports with support from the Government
of Uganda
FIRST EDITION
National Curriculum Development Centre
P.O. Box 7002,
Kampala- Uganda
www.ncdc.co.ug
ISBN: 978-9970-494-95-8
All rights reserved: No part of this publication may be reproduced,
stored in a retrieval system or transmitted in any form or by any means,
electronic, mechanical, photocopying, recording, or otherwise, without
the prior permission of the copyright holder
TEACHER’S RESOURCE BOOK PRIMARY TWO iii
iii
Contents
FOREWORD ............................................................................................... VIII
ACKNOWLEDGEMENTS ................................................................................. IX
LIST OF ACRONYMS ....................................................................................... X
1.0 INTRODUCTION ....................................................................................... 1
2.0 THE PURPOSE OF THE TEACHER’S RESOURCE BOOK ............................................1
3.0 HOW TO USE THIS RESOURCE BOOK ......................................................................2
4.0 THE GENERAL PROCEDURE OF TEACHING CHRISTIAN RELIGIOUS EDUCATION ....3
5.0 THE LESSON PLAN STRUCTURE IN THIS RESOURCE BOOK ....................................4
SAMPLE SCHEME OF WORK FOR CHRISTIAN RELIGIOUS EDUCATION - P2 ........... 6
THEME: CHRISTIANS LIVING TOGETHER IN GOD’S FAMILY ...........................................6
THEME: CHRISTIANS LIVING TOGETHER IN GOD’S FAMILY ................................. 8
SUB THEME: MY HOME AND COMMUNITY .....................................................................8
LESSON: FAMILY MEMBERS ...........................................................................................8
TERM 1 WEEK 1 ......................................................................................... 11
THEME: CHRISTIANS LIVING TOGETHER IN GOD’S FAMILY ................................ 11
SUB-THEME: MY HOME AND COMMUNITY...................................................................11
LESSON 1: FAMILY MEMBERS ......................................................................................11
LESSON 2: ROLES OF DIFFERENT FAMILY MEMBERS ..................................................13
LESSON 3: IMPORTANCE OF FAMILY MEMBERS TO EACH OTHER............................... 15
WEEK 2 ....................................................................................................... 17
LESSON 1: MY NEIGHBOUR .........................................................................................17
LESSON 2: RESPECT AND CARE FOR NEIGHBOURS ....................................................18
LESSON 3: RESULTS OF DISRESPECT FOR THE NEIGHBOUR .....................................20
WEEK 3 ....................................................................................................... 22
LESSON 1: THE CHURCH AS GOD’S FAMILY .................................................................22
LESSON 2: GOD’S LOVE THROUGH THE CHURCH FAMILY ..........................................23
LESSON 3: ACTIVITIES DONE BY THE CHURCH FAMILY ...............................................25
</passage>

<passage id="lchk_50e4d1a9b8724edfad514d3a0c9b86de" source="P2 Thematic Curriculum June 2011" part="1">
- 1 -
THE REPUBLIC OF UGANDA
Ministry of Education and Sports
Primary School Curriculum
Primary 2
National Curriculum Development Centre
- 2 -
Contents
PAGE
Acknowledgement…………………………………………………… 3
Foreword………………………………………………………………... 4
Section A: Introduction 5
1. The National Aims of Education……………………………………………. 6
2. The Aims and Objectives of Primary Education…………………………….. 6
3. The Organisation of the Primary Curriculum 7
4. The Overall Approach in P1-P3……………………………………………… 8
5. The Organisation of the Thematic Curriculum in P1-P3……………………... 10
6. The Approach to Assessment………………………………………………… 12
Section B: Curriculum Scope and Sequence 13
7. The Thematic Strands………………………………………………………... 14
8. Religious Education………………………………………………………….. 51
a) CRE……………………………………………………………………… 51
b) IRE……………………………………………………………………...... 62
9. Physical Education…………………………………………………………… 70
- 3 -
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
• The Management of the Teacher’s Colleges and Primary Schools for having permitted their members
of staff for longer periods of absence from duty during the writing sessions.
• The Management of the Primary Schools that allowed NCDC to use their schools for piloting the
drafts of the Thematic Curriculum for the purposes of coming up with a quality final Curriculum.
• The District Education Officers in the trial districts for the support, supervision and encouragement
to the teachers during the pilot phase of this Curriculum.
Last but not least, thanks to all those behind the scenes – groups of people, organisations and individuals
who formed part of the team that worked so hard on the preparation and production of this document.
Connie Kateeba
Director, National Curriculum Development Centre - NCDC
- 4 -
The failure by a high proportion of the children to attain acceptable levels of proficiency in reading and writing at Primary
Three (3) level is considered to be a barrier to the children’s full enjoyment of their right to education as enshrined in Section
30 of the Constitution of the Republic of Uganda (1995 Edition). Sector-wide reflection on this phenomenon has led to
identification of challenges which need urgent attention to make schooling more beneficial to the children. The Ministry
commissioned a study which carried out a situational analysis which showed that one of the factors causing poor learner
</passage>

<passage id="lchk_2128e27e72b8437b8274ca544b1fbf8e" source="P 2 Primary TWO CRE Scheme OF Work Teacher AC" part="4">
d bk 2
Pg 1
Bible
8 1 Service • Ways of helping
people with
special needs
• • • • - Real life
situation
2 • Importance of
helping people
with special needs
• Singing
• Naming
• Identifying
• • • -
3 • Story of Jesus’
visit to Mary and
Martha
• God’s message
(Luke 11:38 – 41
• Role playing
• Listening
• Explaining
• Story telling
• Discussing
• • • - Bible Bible
Luke
11:38 -
9 1 Service • Difficulties Jesus
met in healing the
sick.
• God’s message
(Matthew 12:9-14
• Praying
• Identifying
• Role playing
• Singing
• Answering
questions
• Story telling
• Reading
• Spelling
• Pronunciati
on
• Writing
• Brain
storming
• Role
playing
• Story
telling
• Explanati
on
• Discussio
n
• Singing
• Praying
• Identifying
• Story telling
- Effective
communicatio
n
- Critical
thinking
Values
- Love
- Care
- Respect
- Empathy
real life
situation
bible
Matthew
12: 9-14
2 • Ways in which we • Story telling • • • - real life MK
10
get discouraged
as we help others
• Role playing
• Explaining
situation Standar
d bk 2
Pg. 64 –
65
3 • Enduring when
we get
discouraged
• • • • -
TERM III
THEME: CHRISTIAN LIVING TOGETHER IN GOD’S FAMILY
Learning outcome: The child understands and appreciates the concepts and values of “Honesty and fairness”
COMPETENCES
WK pd Subtheme Content Subject Language Methods Activities Life skills T/L Aids Ref.
1 1 Honesty and
Fairness
Meaning of
• Honest
• Honesty
• Dishonest
• defining
• interpreting
• answering
questions
• story telling
• narrating
• reading
• spelling
• pronunciatio
n
• writing
• explanation
• discussion
• brain
storming
• story telling
• role playing
• defining
• narrating
• story telling
- creative
thinking
- friendship
formation
- assertiveness
Values
- love
- care
- respect
- obedience
- share
Real life
situation
MK
Standard
bk 2 Pg 6
2 Examples of
dishonest amongst
people
• story telling
• mentioning
• narrating
• listing
• role playing
• • • -
3 How dishonesty
brings conflict.
The story of Cain
and Abel
• story telling
• drawing
• shading
• mentioning
• role playing
• • • - Bible Bible
Gen. 27:
2 1 Honesty and Story of Jacob and • listening • reading • brain • listening - friendship story Bible
11
fairness Rebecca
God ’s message
(Gen: 27:1 – 44)
• answering
questions
• narrating
• interpreting
• pronouncing
• spelling
• writing
storming
• explanation
• discussion
• story telling
• answering
questions
• narrating
• interpreting
formation
- creative
thinking
- self esteem
Values
- love
- care
- respect
- obedience
- share
- empathy
books
bible
Gen
27:1-44
2 Story of Esau and
Jacob
• • • • -
3 The need for honest
and its benefits
• identifying
• telling stories
• singing songs
• • • - real life
situation
MK
Standard
bk 2
Pg…..
3 1 Ways of being
honest
• identifying
• listing
• telling stories
• • • - MK
Standard
bk 2 Pg.
69
2 Occasions when we
need to be
fair/honest
• Listing
• Telling
stories
• Role playing
• • • - curr. Pg.
59
3 Ways of being
unfair and
dishonest
• Identifying
• Explaining
• Story telling
• Role playing
• Reading
• Spelling
• Pronouncing
• Writing
• Brain
storming
• Role play
• Story
telling
• Explanatio
n
• Story telling
• Role playing
explaining
• Identifying
- Creative
thinking
- Friendship
formation
- Assertiveness
Values
- Love
- Care
- Respect
Real life
situation
4 Concern for
others
Story of David and
Jonathan
God’s message (1 st
Samuel 19:21)
• Listening
• Story telling
• Role playing
• Reading
• Spelling
• Pronouncing
• Writing
• Story
telling
• Brain
storming
• Listening
• Story telling
</passage>

<passage id="lchk_2e0d2ea551da484893d9056da27e32a0" source="NCDC CRE P.2 TEACHERS RESOURCE BOOK" part="1">
TEACHER’S RESOURCE BOOK

M AR
RI

Y
P

CHRISTIAN RELIGIOUS EDUCATION

TEACHER’S RESOURCE BOOK

CHRISTIAN
RELIGIOUS
EDUCATION
M AR
RI

Y
P

Copyright © National Curriculum Development Centre, Uganda, 2020

A product of the National Curriculum Development Centre for the
Ministry of Education and Sports with support from the Government
of Uganda

FIRST EDITION

National Curriculum Development Centre
P.O. Box 7002,
Kampala- Uganda
www.ncdc.co.ug

ISBN: 978-9970-494-95-8

All rights reserved: No part of this publication may be reproduced,
stored in a retrieval system or transmitted in any form or by any means,
electronic, mechanical, photocopying, recording, or otherwise, without
the prior permission of the copyright holder

PRIMARY TWO | TEACHER’S RESOURCE BOOK

Contents
FOREWORD ............................................................................................... VIII
ACKNOWLEDGEMENTS ................................................................................. IX
LIST OF ACRONYMS ....................................................................................... X
1.0 INTRODUCTION ....................................................................................... 1
2.0 THE PURPOSE OF THE TEACHER’S RESOURCE BOOK ............................................1
3.0 HOW TO USE THIS RESOURCE BOOK ......................................................................2
4.0 THE GENERAL PROCEDURE OF TEACHING CHRISTIAN RELIGIOUS EDUCATION ....3
5.0 THE LESSON PLAN STRUCTURE IN THIS RESOURCE BOOK ....................................4
SAMPLE SCHEME OF WORK FOR CHRISTIAN RELIGIOUS EDUCATION - P2 ........... 6
THEME: CHRISTIANS LIVING TOGETHER IN GOD’S FAMILY ...........................................6
THEME: CHRISTIANS LIVING TOGETHER IN GOD’S FAMILY ................................. 8
SUB THEME: MY HOME AND COMMUNITY .....................................................................8
LESSON: FAMILY MEMBERS ...........................................................................................8
TERM 1 WEEK 1 ......................................................................................... 11
THEME: CHRISTIANS LIVING TOGETHER IN GOD’S FAMILY ................................ 11
SUB-THEME: MY HOME AND COMMUNITY...................................................................11
LESSON 1: FAMILY MEMBERS ......................................................................................11
LESSON 2: ROLES OF DIFFERENT FAMILY MEMBERS ..................................................13
LESSON 3: IMPORTANCE OF FAMILY MEMBERS TO EACH OTHER...............................15
WEEK 2 ....................................................................................................... 17
LESSON 1: MY NEIGHBOUR .........................................................................................17
LESSON 2: RESPECT AND CARE FOR NEIGHBOURS ....................................................18
LESSON 3: RESULTS OF DISRESPECT FOR THE NEIGHBOUR .....................................20
WEEK 3 ....................................................................................................... 22
LESSON 1: THE CHURCH AS GOD’S FAMILY .................................................................22
LESSON 2: GOD’S LOVE THROUGH THE CHURCH FAMILY ..........................................23
LESSON 3: ACTIVITIES DONE BY THE CHURCH FAMILY ...............................................25
</passage>

<passage id="lchk_2742cf98b42742ec8845de81163a714d" source="NCDC IRE P.2 TEACHERS RESOURCE BOOK" part="1">
ISLAMIC
RELIGIOUS
EDUCATION
TEACHER’S RESOURCE BOOK

M AR
RI
Y

P

ISLAMIC RELIGIOUS EDUCATION

TEACHER’S RESOURCE BOOK

ISLAMIC
RELIGIOUS
EDUCATION

M AR
RI

Y
P

Copyright © National Curriculum Development Centre, Uganda, 2020

A product of the National Curriculum Development Centre for the
Ministry of Education and Sports with support from the Government
of Uganda

FIRST EDITION

National Curriculum Development Centre
P.O. Box 7002,
Kampala- Uganda
www.ncdc.co.ug

ISBN: 978-9970-494-80-4

All rights reserved: No part of this publication may be reproduced,
stored in a retrieval system or transmitted in any form or by any means,
electronic, mechanical, photocopying, recording, or otherwise, without
the prior permission of the copyright holder

PRIMARY TWO | TEACHERS’ RESOURCE BOOK

TABLE OF CONTENTS
FOREWORD ....................................................................................................................... ix
ACKNOWLEDGEMENT ........................................................................................................ x
LIST OF ACRONYMS .......................................................................................................... xi
1.0 INTRODUCTION ........................................................................................................... 1
2.0 THE PURPOSE OF THE TEACHER’S RESOURCE BOOK ............................................... 2
3.0 HOW TO USE THIS RESOURCE BOOK .......................................................................... 2
4.0 GENERAL PROCEDURE OF TEACHING ISLAMIC RELIGIOUS EDUCATION ................... 3
5.0 LESSON PLAN STRUCTURE IN THIS RESOURCE BOOK .............................................. 4
SAMPLE SCHEME OF WORK ............................................................................................ 7
SAMPLE LESSON PLAN .................................................................................................... 10
P2 IRE Lesson Plan, Term 3, 2019 ................................................................................... 10
TERM 1 ....................................................................................................... 13
WEEK ONE ........................................................................................................................ 13
THEME 1: READING FROM THE HOLY QUR’AN ............................................................ 13
SUB-THEME: Surat Al-Falaq ....................................................................................... 13
Lesson 1: Reciting Surat Al-Falaq............................................................................... 13
Lesson 2: Writing Surat Al-Falaq in Transliteration .................................................. 15
Lesson 3: The Meaning of Surat Al-Falaq ................................................................... 17
WEEK TWO ....................................................................................................................... 19
Lesson 1: Writing Surat Al-Falaq in the language of instruction .............................. 19
Lesson 2: Importance of Surat Al-Falaq..................................................................... 21
Lesson 3: Reading Arabic vowels Surat Al-Falaq ...................................................... 22
WEEK THREE .................................................................................................................... 24
</passage>

<passage id="lchk_d6092e52d77a40ada19f661beba1a21c" source="P 2 CRE All Terms" part="6">
- We learn to pay our debts
Activity:
Draw the old widow filling the many jars oil.
Ways of showing concern.
- By helping
- By sharing
- By directing
- By praying for the sick
- By caring for others.
Story of Ruth and Naomi
Naomi was a widow
Her husband and two sons had died
She was left poor and helpless.
Ruth was Naomi’s daughter-in-law
Ruth decided to stay with Naomi for all of her life.
Activity
Children will act (dramatise) the story.
For more lesson notes, please visit www.freshteacheruganda.com
Why God gave us the greatest gift?
God gave us his only begotten son, Jesus Christ to protect us from doing bad
things and also forgiving us our wrongs.
Christians remember the birth of Jesus on every 25 th of December of the year
and that day is called Christmas.
God wants us to behave well in order to live happily like Jesus Christ.
Question; What happens during Christmas?
The importance of giving to others
- To promote love
- To promote friendship
- To promote unity
- To please God
- To get blessings
Examples of gifts
- Christmas cards
- Money
- Shoes
- Watch
- Milk
- Clothes
Why do we give gifts
- To show love
- To keep good relationships
- To make friends
- To make others happy
- To appreciate others
- We give gifts to the needy people
Importance of giving gifts
- It keeps a good relationship with others
- It shows love
- You make friends
- You make others happy
- You show others appreciate
- You serve the needy people
SUBTHEME: GOD’S GIFT OF HIS SON.
For more lesson notes, please visit www.freshteacheruganda.com
Learning outcome : The child knows Jesus as God’s greatest gift to us
and appreciates celebrating Christmas.
God’s promise to give us His Son
Draw the pictures of Christmas events
People at church Eating food Father Christmas Gifts
Matthew 1:21
Story of Jesus’ birth
One day, a baby boy was born by the Virgin Mary.
The baby was named Jesus Christ.
God gave us His Holy son, Jesus Christ, to protect us from doing bad things.
Christians remember the birth of Jesus on every 25 th of December. That day is
call Christmas day.
God gave us Jesus Christ so that we become his friends again.
Refer: MK Standard RE book 2 page 85 – 86.
</passage>

<passage id="lchk_f535052f09bd4effabc4f3e6a249ed8a" source="P.2 CRE LESSON NOTES" part="6">
Christians remember the birth of Jesus on every 25th of December. That day is call Christmas day.
God gave us Jesus Christ so that we become his friends again.
Refer: MK Standard RE book 2 page 85 – 86.
</passage>

<passage id="lchk_8ffbb0abe143460c84373fcda277f36e" source="CRE p2 ms" part="1">
GOLDEN ELITE EXAMINTIONS 2020
Kenya Certificate of Secondary Education
313/2
CHRISTIAN RELIGIOUS EDUCATION
PAPER 2
MARKING SCHEME
a) The characteristics of the suffering servant of Yahweh according to prophet Isaiah (Isaiah53)
Is despised, rejected, ignored, arrested and sentenced to death.
Is humble and simple.
Will be buried in a rich man’s tomb.
Suffers innocently.
Will suffer as willed by God.
Will be highly honoured and will succeed in His work.
Will suffer and die for the salvation of humankind.
Will be allotted with the sinners in his death. 9 x 1 = 9 Marks
b) Ways in which Jesus fulfilled prophesies given to King David by Prophet Nathan
Jesus’ foster father, Joseph was a descendant of David.
Was the son of God as prophesied by Nathan.
Established an everlasting kingdom.
Was supported by God as the witness of the voice from heaven at his baptism affirms.
Is the great king whose kingdom is kept strong.
The angel Gabriel confirmed that Jesus’ kingdom will have no end and that he will rule over Israel for ever. 5 x 1 = 5 Marks
c) The relevance of God’s promises to David by Prophet Nathan
Jesus Christ is a descendant of David and is an heir to the Kingdom of God.
Christians are assured of God’s love and mercy through Jesus who is an eternal one i.e. God had promised David an everlasting kingdom.
Christians believe that they are spiritual descendants of David through their faith in Christ
Christians are promised eternal homeland (heave) to live in.
Christians believe the promises made to David have been fulfilled in Jesus Christ.
Christians are assured of God’s protection through Jesus Christ. 6 x 1 = 6 Marks
a) Ways in which John the Baptist prepared the way for the Messiah.
Baptized people in River Jordan.
Advised people to live holy lives by doing what was right.
Preached repentance of sin.
Baptized those who repented.
Encouraged the rich to share with the poor.
Advised people to lead honest lives e.g. the tax collectors were not to collect what was illegal.
Advised workers not to misuse their offices.
Warned people of the coming judgement.
Acknowledged Jesus’ greatness over him.
He introduced Jesus to his disciples.
He told the people that he was not the Messiah but his forerunner.
He preached the good news that the Messiah would baptize with fire and the Holy Spirit.
Reprimanded Herod for marrying his brother’s wife.
Baptized Jesus in River Jordan.
Cautioned the Jew’s not to boast about being Abraham’s descendants but to bear fruits that befit repentance. 10 x 1 = 10 Marks
b) Reasons why Jesus was rejected in Nazareth
He annoyed the people by telling them that their forefathers rejected God’s prophets.
He failed to perform the kind of miracles that he had performed in Capernaum.
He told the people that prophets are ignored in their own country.
He declared that he had come to fulfill Isaiah’s prophecy concerning the Messiah.
He was the son of Joseph. 4 x 1 = 4 Marks
c) How church leaders are put to test today.
Human suffering which hinders people from accepting the message of hope.
Lack of cooperation from the congregation.
Problems of how to react/relate objectively when expectations are not met.
Inadequate knowledge on how to deal with various groups/women/youth/choir/rival groups/relatives.
There are temptations to acquire property unjustly.
Difficulties in harmonizing the message of the gospel and innovations of science and technology.
Too much time/service is expected out of them.
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
