# Job ltsk_579d1b4625e04f55909bc9cb7d73888e-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for Christian Religious Education, Primary One 2026, Term 3.
The term has 10 teaching weeks and this subject has 3 periods per week. Every lesson is ONE 40-minute period, so keep each lesson small enough to teach in 40 minutes.
Ledgerly reserves the last lesson of each week for a review of that week.
Give at most 20 teaching/practice lesson entries in teaching order (the last lesson of the term is the end of term assessment).
Each lesson has a kind: "teach" (new content) or "practice" (the same subtopic as the teaching lesson just before it: exercises, oral work, drawing, matching, filling in blanks, ALL taken from the passages).
When the material is thin (common in lower primary), follow each teaching lesson with a practice lesson. Split big subtopics over several teaching lessons.
Never pad with content the passages do not have: if they cannot fill the term, return fewer lessons and list what is missing in gaps. Ledgerly fills the remaining weeks with revision.
You are composing the SCHOOL'S OWN scheme. The passages below (the official NCDC curriculum and guides, plus schemes of work, lesson plans, notes and past papers from the school e-library) are reference material:
The NCDC documents (titles starting "NCDC") are the BASE: their topics, competences and order for this class and term are what the scheme must cover. NCDC lower-primary thematic curricula list every learning area side by side in table columns separated by " | ": take only the Christian Religious Education column.
Every topic the NCDC curriculum lists for this class and term MUST become a unit, in the NCDC order. Share the weeks between ALL of them according to their NCDC periods, competences, content and subtopics. Large topics should receive more lessons than small topics.
combine them in this authority order: curriculum for required coverage; all relevant schemes for sequence and pacing; the strongest detailed notes for accurate teaching depth; past papers for expected applications and activities. Do not copy one reference scheme blindly.
Use this term's part of the material (Term 3) when the passages cover several terms.
Theme-only references (Primary ONE Scheme OF Work Grammar): general thematic schemes covering every learning area. Use them ONLY for the term's theme name and week order; ignore their content for other learning areas (reading, spelling, drawing, literacy, songs). Every lesson must be Christian Religious Education content.
REQUIRED NCDC topics/themes for Primary One 2026, Term 3 (from the NCDC curriculum, in this order). Every one MUST have at least one unit whose title or theme names it, with about this many teaching/practice lessons:
  1. God's family with Jesus our friend: about 5 lessons
  2. God's family and our concern for sharing: about 5 lessons
  3. Interpersonal relationship in the home: about 5 lessons
  4. God's family and his love: about 5 lessons
Keep to these evidence-based shares. A broad topic may take substantially more lessons than a small topic when its NCDC scope, competences and subtopics justify it.
Do NOT write lesson content yet. Each unit and lesson must cite the passage ids it comes from in sourcePassageIds.

Reply shape:
{"title":string,"summary":string,"units":[{"title":string,"theme":string|null,"weekFrom":int|null,"weekTo":int|null,"competences":string|null,"sourcePassageIds":[string],"lessons":[{"title":string,"subtopic":string|null,"kind":"teach"|"practice","objectives":[string],"sourcePassageIds":[string]}]}],"gaps":[string]}

<passages>
<passage id="lchk_06bae8bec78742e590918e32d60c7b77" source="NCDC CRE P.1 TEACHERS RESOURCE" part="1">
TEACHER’S RESOURCE BOOK

PRIMARY ONE

CHRISTIAN RELIGIOUS EDUCATION

TEACHER’S RESOURCE BOOK

CHRISTIAN
RELIGIOUS
EDUCATION
P R I M A R Y | O N E

Copyright © National Curriculum Development Centre, Uganda, 2020

A product of the National Curriculum Development Centre for the
Ministry of Education and Sports with support from the Government
of Uganda

FIRST EDITION

National Curriculum Development Centre
P.O. Box 7002,
Kampala- Uganda
www.ncdc.co.ug

ISBN: 978-9970-494-96-5

All rights reserved: No part of this publication may be reproduced,
stored in a retrieval system or transmitted in any form or by any means,
electronic, mechanical, photocopying, recording, or otherwise, without
the prior permission of the copyright holder

PRIMARY ONE | TEACHER’S RESOURCE BOOK

CONTENTS
FOREWORD ....................................................................................... IX
ACKNOWLEDGEMENT .......................................................................... X
LIST OF ACRONYMS ............................................................................ XI
1.0 INTRODUCTION ............................................................................. 1
2.0 THE PURPOSE OF THE TEACHERS’ RESOURCE BOOK ...................................1
3.0 HOW TO USE THIS RESOURCE BOOK ...........................................................2
4.0 THE GENERAL PROCEDURE OF TEACHING CHRISTIAN RELIGIOUS
EDUCATION ........................................................................................................3
5.0 THE LESSON PLAN STRUCTURE IN THIS RESOURCE BOOK ...........................4
SAMPLE SCHEME OF WORK FOR P1 CHRISTIAN RELIGIOUS EDUCATION .........6
THEME: DISCOVERING GOD’S GIFT TO ME ........................................................6
SAMPLE LESSON PLAN FOR CHRISTIAN RELIGIOUS EDUCATION .......................8
PRIMARY ONE .....................................................................................................8
SELF-EVALUATION ............................................................................................10
TERM 1 ............................................................................................. 11
WEEK ONE: ORIENTATION .................................................................. 11
SCHEMES OF WORK AND LESSON PLAN GUIDELINES ......................................11
The orientation week .......................................................................................11
WEEK TWO........................................................................................ 16
THEME: DISCOVERING GOD’S GIFT TO ME ......................................................16
SUB-THEME: I am part of God’s creation ........................................................16
LESSON 1: Who am I? .......................................................................................16
LESSON 2: Names and their meaning ..............................................................17
LESSON 3: Names and their meaning (of the people in the Bible) ..................19
WEEK THREE ..................................................................................... 21
LESSON 1: God knows each individual intimately ...........................................21
LESSON 2: Our bodies.......................................................................................22
LESSON 3: Uses of our bodies ..........................................................................24
</passage>

<passage id="lchk_3ad484a8bc434ca6b784417b97e149aa" source="NCDC IRE P.1 TEACHERS RESOURCE BOOK" part="4">
LESSON 3: A RHYME ABOUT THE CLAN AND TRIBE OF PROPHET MUHAMMAD
(PBUH) ............................................................................................................ 123
WEEK 11 .......................................................................................... 125
LESSON 1: THE CHARACTER OF PROPHET MUHAMMAD (PBUH) AS A CHILD
(KIND, RESPECTFUL, PEACEFUL, COOPERATIVE, FRIENDLY) ........................ 125
LESSON 2: OTHER CHARACTER TRAITS OF MUHAMMAD (PBUH) AS YOUTH
(TRUSTWORTHY, HONEST, FAITHFUL, TRUTHFUL, NEVER WORSHIPPED
IDOLS .............................................................................................................. 127
LESSON 3: BENEFITS OF IMITATING PROPHET MUHAMMAD’S CHARACTERS AS
A YOUTH ......................................................................................................... 128
WEEK 12 .......................................................................................... 131
LESSON 1: THE WORK OF MUHAMMAD AS A YOUTH ...................................... 131
LESSON 2: KHADIJAH’S PROPOSAL OF MARRIAGE TO PROPHET MUHAMMAD
(PBUH) ............................................................................................................ 132
LESSON 3: ROLE PLAYING CHARACTERS OF PROPHET MUHAMMAD ............ 134
TERM 3 ............................................................................................ 136
WEEK 1: THEME 1: READING FROM THE HOLY QUR’AN ......................... 136
SUB-THEME: SURAT NAS ............................................................................... 136
LESSON 1: RECITING SURAT AN-NAS ............................................................. 136
LESSON 2: MEANING OF SURAT AN-NAS ....................................................... 137
LESSON 3: READ SURAT ANNAS IN ARABIC (VERSES 1-6) .............................. 139
WEEK 2 ............................................................................................ 141
LESSON 1: READ SURAT AN-NAS IN THE LANGUAGE OF INSTRUCTION (VERSES
1-6) ................................................................................................................. 141
LESSON 2: IMPORTANCE OF SURAT AN-NAS ................................................. 142
LESSON 3: MEMORISING SURAT AN-NAS ....................................................... 143

vi

vi

PRIMARY ONE | TEACHERS’ RESOURCE BOOK

WEEK 3 ............................................................................................ 145
LESSON 1: INCIDENTS THAT LED TO THE REVELATION OF SURAT AN-NAS .. 145
LESSON 2: MAIN PURPOSE FOR THE REVELATION OF SURAT AN-NAS ......... 146
LESSON 3: RECITING A DUA USING SURAT AN-NAS ....................................... 148
WEEK 4: THEME 2: TAWHIID (FAITH) ................................................... 149
SUB-THEME: ALLAH AND HIS CREATION ....................................................... 149
LESSON 1: BELIEF IN THE EXISTENCE OF ALLAH ........................................... 149
LESSON 2: THINGS CREATED BY ALLAH ......................................................... 151
LESSON 3: SIGNS THAT SHOW ALLAH’S EXISTENCE...................................... 152
WEEK 5 ............................................................................................ 154
LESSON 1: THE IMPORTANCE OF THE THINGS ALLAH CREATED ................... 154
LESSON 2: THE ONENESS OF ALLAH .............................................................. 155
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

<passage id="lchk_24f00223669749ceb2d3134bfd2cbb0a" source="CRE P.1 NOTES" part="72">
- He created a strong army
- He was a forgiving king
- He built up a well discipline army.
However, Saul had the following failures in Israel during his reign:-
- Spared the Amelekites.
- Spared the best animals of the Amelekites.
- Spared king Agag of the Amelekites.
- He was disobedient to fulfilling the act of Herem
- He only destroyed useless animals and human beings at the war with the Amelekits.
- He lied to Samuel that he had destroyed all.
- He showed that he was a materialistic by sparing best animals.
- He was unrepentant
- He was impatient
- He lacked faith in God.
- He built a monument in himself after the war with the Amelekites.
- Respected his soldiers more than God.
- Attempted to make political alliances.
- The spirit of God left him and he became possessed by an evil spirit.
- Lacked total control over his army.
- Encouraged Baalism in Israel
- Failed to kill Goliath.
- He committed suicide.
- He was never accepted by all the Israelites.
- He was a killer who attempted to kill David many times.
- He was jealous of King David.
Question:
To what extent did Saul’s act of sparing king Agag of the Amelekites contribute to his own
downfall (reject)?
To the lesser extent, Saul sparing King Agag contributed to his own downfall as follows:-
The act showed him as disobedient to Yahweh hence his own downfall.
It showed his lack of faith in Yahweh hence causing his own downfall.
</passage>

<passage id="lchk_dc64760a07f04fa1ad6e228d2b409aa5" source="P 1 RE BOT III" part="1">
1
© 2023 OSEB EDUCATIONAL CONSULT -KAMPALA 0775787978/0742845900
OUTREACH SCHOOLS EXAMINATION BOARD
BEGINNING OF TERM III EXAMINATION 2023
PRIMARY ONE
RELIGIOUS EDUCATION
My name is _____________________________________________
I am in __________________________________________________
My school is ____________________________________________
1. Draw these things which give us light.
star moon lamp candle
2. Moslems go to the _______________on Friday.
3. Christians go the ______________on Sunday.
(town, mosque, shop, church)
4. Circle the uses of water at home.
cooking food, writing, sleeping, clapping,
bathing, drinking, dancing
5. __________________and _________________lived in the garden of
Eden. (Adam, Kato, Eva)
2
© 2023 OSEB EDUCATIONAL CONSULT -KAMPALA 0775787978/0742845900
6. Draw these things man has made.
chair radio mat book
7. Who died on the cross? _________________________________
(God, Allah, Jesus)
8. Name three people found at home.
i) _______________________________________________________
ii) _________________________________________________________
iii) _________________________________________________________
9. God is in ______________________ and everywhere.(heaven, hell)
10. Good children ____________________their parents.
11. Match our senses to their uses.
eyes tasting
nose hearing
tongue feeling
ears seeing
skin smelling
12. Rain gives us ___________ (soil, water)
13. Underline the Christian names.
Ali, Joseph, Abdul, Alice, Mohammed, Mary, Musoke
3
© 2023 OSEB EDUCATIONAL CONSULT -KAMPALA 0775787978/0742845900
14. Match the needs of people.
water /drinks
shelter
food
clothes
15. Name the things we use to clean our bodies.
(comb, soap, tooth paste, Vaseline, handkerchief, water, brush,
tooth brush)
4
© 2023 OSEB EDUCATIONAL CONSULT -KAMPALA 0775787978/0742845900
16. Match animals to their young ones.
cow lamb
duck piglet
pig kid
sheep calf
goat duckling
**** GOD BLESS YOU****
</passage>

<passage id="lchk_e8bced7e2c844676a11742eb7f44165a" source="Primary ONE END OF Term III 2022" part="4">
he teacher is takina the television
1
2
3
4
1
2
3
4
his is our school motto
1
2
3
4
1
2
3
4
1. Write these words correctly .
(a) ythe ________________ (d) loost _______________
(b) tpo _________________ (e) aycl_______________
(c) lldo _________________ (f) skde_______________
2. Find the hidden words and underline them .
(a) x p t o y z k
(b) o e x m a t c
(c) b a g c m n i
3. Write the sentences correctly .
(a) aeroplane He an flies.
____________________________________________________
(b) weaving a mat She is.
_____________________________________________________
(c) two pots Peter has.
______________________________________________________
(d) van by I come to school.
______________________________________________________
4. Fill in the missing vowels .
a ____ i _____ u
5. Write a word for the picture . 6. Match sounds to the picture .
(basket, kite, bird, stool)
Primary One Reading page 1
PRIMARY ONE END OF TERM III EXAMS
READING
Name: _________________________________________________
School: ____________________________________Class ______
p
b
c
m
b
c
h
f
7. Read the poem and in full sentences, answer the questions that
follow. TIM’s TOY CAR
Tim has a big toy car
It is blue and pink
The toy car has four tyres
Tim plays with his car every day
His daddy bought it for him.
Questions:
(a) Who has a toy car ? _________________________________
(b) Write the colours of the toy car.
(i)__________________________ (ii)______________________
(c) The toy car has ________________ tyres.
(d) Who bought it for him ?
_____________________________________________________
(e) Write the title of the poem.
_____________________________________________________
8. Circle sounds for the picture and write the word .
(a)
(b)
(c)
(d)
9. Join and form words .
Primary One Reading end page 2
s c p a n r s = car
f t z r m e e = ________
r p o a f d = _________
d x t r w u n m = ________
op
eep
irt
ip
a
1.___________
ll
sh
2.___________
3.___________
4.___________
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
