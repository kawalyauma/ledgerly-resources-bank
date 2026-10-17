# Job ltsk_db3d2f25e09d4d9da5ea73abda908d11-0

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
  9. Our Transport: about 5 lessons
  10. Things We Make: about 5 lessons
  11. Our Environment: about 5 lessons
  12. Peace and Security: about 5 lessons
Keep to these evidence-based shares. A broad topic may take substantially more lessons than a small topic when its NCDC scope, competences and subtopics justify it.
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

<passage id="lchk_2a4cb1eb7c05417791f508fa111303fc" source="NCDC P1 Curriculum" part="3">
competences that will need to be clearly specified within each of the learning areas.
e) The local language policy specified in the White Paper should remain basically unchanged.
Wherever practicable, a local language should be used as the medium of instruction in P1-P3 with
English as the medium of instruction from P5 onwards. P4 should be a transition year with special
characteristics where local language as the Language of Instruction (LOI) is phased out and English
is phased in.
f) English should be used as the medium of instruction from P1 only in those schools, where a majority
of enrolled learners do not speak a common local language as their first or dominant language.
g) The local language selected as the medium of instruction in P1 to P3 should be taught as a subject
in P4 to P7 and should be examined.

Following the recommendations of the curriculum review team, the MoESTS developed and piloted a
thematically based curriculum for P1. The results of the pilot showed great success. As a result, the
same process is to be extended to P2 and P3.

I am sure that if this Curriculum is fully implemented, it will improve the levels of learning for learners
in P1 to P3 across the country.

I, therefore, call upon all stakeholders and the Ministry of Education, Science, Technology and
Sports (MoESTS) as a whole to play their part in this initiative.

Hon. Geraldine Namirembe Bitamazire (MP)
Minister of Education, Science, Technology and Sports
October 2006

v
v

vi
vi

SECTION 1:
INTRODUCTION

Introduction

1. The National Aims of Education
This Curriculum is designed to address the national aims of education as specifically stated in the
Government White Paper on the Education Policy Review Commission Report (1992). The
aims are:

a) To promote understanding and appreciation of the value of national unity, patriotism and cultural
heritage, with due consideration to international relations and beneficial interdependence.

b) To inculcate moral, ethical and spiritual values in the individual and to develop self-discipline,
integrity, tolerance and human fellowship.

c) To inculcate into Ugandans a sense of service, duty and leadership for participation in civic,
social and national affairs through group activities in educational institutions and the community.

d) To promote scientific, technical and cultural knowledge, skills and attitudes needed to enhance
individual and national development.

e) To eradicate illiteracy and equip the individual with basic skills and knowledge to exploit the
environment for self-development as well as national development; for better health, nutrition
and family life, and the capacity for continued learning.

f) | To equip the learners with the ability to contribute to the building of an integrated, self-sustaining
and independent national economy.

2. The Aims and Objectives of Primary Education
a) To enable individuals to acquire functional, permanent and developmental literacy, numeracy
and communication skills in English, Kiswahili and, at least, one Uganda Language.

b) To develop and maintain sound mental and physical health among learners.

c) To instil the values of living and working cooperatively with other people and caring for others in
the community.

d) To develop and cherish the cultural, moral and spiritual values of life and appreciate the
richness that lies in our varied and diverse cultures and values.
</passage>

<passage id="lchk_84af9f3b65dc469786636ee0e0ef5f8e" source="NCDC P1 Curriculum" part="4">
e) To promote understanding and appreciation for the protection and utilisation of the natural
environment, using scientific and technological knowledge and skills.

f) | To develop an understanding of one’s rights and civic responsibilities and duties for the purpose
of positive and responsible participation in civic matters.

g) To develop a sense of patriotism, nationalism and national unity in diversity.

h) To develop pre-requisites for continuing education.

i) | To acquire a variety of practical skills for enabling one to make a living in a multi-skilled manner.

j) | To develop an appreciation for the dignity of work and for making a living by one’s honest effort.

k) To equip the child with the knowledge, skills and values of responsible parenthood.

l) | To develop skills in management of time and finance and respect for private and public property.

m) To develop the ability to use the problem-solving approach in various life situations.

n) To develop discipline and good manners.

3. The Layout of the Lower Primary Curriculum
The P1 Curriculum is part of the planned Primary School Curriculum which is divided into three clear
cycles, each with its own structure of knowledge, skills and learning outcomes specified in terms of
the type and level of skills to be achieved.

3.1 | Cycle 1 (P1-P3): | Basic Skills

A thematic approach has been used as the organising principle for the arrangement of the
competences and knowledge content. The themes have been selected as those most likely to be
relevant to children, reflecting their everyday interests and activities as well as the national aims and
objectives.

All learning materials used in these three years will be provided in the child’s own language or a
language familiar to the child. Any written tests that are used for assessment purposes, apart from
assessment of English language competence for non-English medium schools, will also be in the
local language. Only when the mix of languages in a school is such that there is no predominant
local or area language will the curriculum be delivered and assessed in English.

The major expected learning outcomes of this cycle are that learners will develop:

 | basic literacy, mathematics and life skills as well as values in a first language or familiar
language at a level that will enable the child to mature and be prepared for further learning.

 | sufficient skills in English to act as basis for developing English as the medium of instruction in
the upper primary cycle.

 | an appreciation of their culture and the roles they can play in the society.

3.2 | Cycle 2 (P4): The Transition Year

This will be a single year in which learners will change from theme-based to subject-based
curriculum and gradually from their local language to English as a language of instruction. The
emphasis will be on rearranging content, concepts and skills rather than introducing new content or
concepts. Thus, the organising principle will now be subject-based. Learners and teachers will
start the year using the local language during the teaching and learning process, and there will be a
steady development in the use of English as the medium of instruction. By the end of P4 the local
language will be used only for explaining the most difficult concepts. Written materials, including
textbooks, will be in simple English and all assessment will be in English.

The aims of this cycle will be for learners to achieve:
</passage>

<passage id="lchk_2d179efb100b4b3bbf889be69049cc67" source="NCDC P1 Curriculum" part="5">
 | English skills, both oral and written, to a level in which learning can take place in English across
all subjects.

 | a transfer of all competences acquired in the first or familiar language into English.

 | building on the content, knowledge and competences already acquired through the theme-
based curriculum but now transferred to a subject-based framework.

 | applying the developed skills and the ability to think creatively in English using knowledge and
concepts already acquired in P1-P3.

3.3 | Cycle 3 (P5-P7): | Subject-based Development

This cycle will be similar to the current curriculum, where the concepts, knowledge and skills are
arranged in subjects. Care will be taken to ensure that the Primary School subject based curriculum
align with the Secondary School syllabi in such a way that a good foundation is laid.

The aims of this cycle will remain the same as already expressed in the current curriculum for upper
primary, including preparing learners for:
 Secondary Education
 The World of Work
 Scientific and technical application of knowledge
 Life skills

4. The Overall Approach in P1-P3
4.1 | Learning Outcomes and Competences

The Thematic Curriculum consists of several learning outcomes that are derived from the general
aims of education. The learning outcomes describe what the learner is expected to know,
understand and be able to do in relation to each theme. The themes have been selected not only
as a means of organising the curriculum but also are in themselves important aspects of daily life
that learners in Uganda need to be aware of and responsive to.

The learning outcome is often expressed in the form of a broad Life Skill (for example, the learning
outcome for Theme 7 is: ‘The child is able to identify people, relate and appreciate ways to living
with them harmoniously’). A learning outcome is generally acquired over a longer period than a
competence.

Learning outcomes define the overall direction of the teaching and learning process. They do not
contain specific learning objectives1 that can be assessed. However, they are achieved through
competences. Competences describe the genuine abilities of the learner to demonstrate that

The Thematic Curriculum does not use the term ‘objectives’ as an organising principle. While all teaching
has objectives, the Thematic Curriculum has chosen a competence-based rather than an objective-based
approach. This is based on the belief of the curriculum planners that objectives refer more to the teaching
than the learning process.

he/she has understood the concepts and has acquired clearly measurable skills.2 Competences
emphasise the transfer of learning.

Teachers need not be too concerned with the difference between a competence and a skill. In this
curriculum, the idea of competence includes the idea of skill but extends it to wider levels of
operations. When a learner is competent in a particular area of learning, he/she has not only
mastered the ability to carry out an action but also knows why he/she is doing that action and when
to employ it. Acquiring a competence is not only about learning a particular behaviour but it is also
about understanding it. It is therefore more in keeping with the overall purpose of a learner-
centred approach.

The following diagram shows the relationship between Aims, Learning Outcomes and
Competences. Learning Outcomes are derived from Aims, while Competences are derived from
Learning Outcomes.

AIMS
</passage>

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

<passage id="lchk_eea150274265402da2ada2ae6ff10ef2" source="NCDC IRE P.1 TEACHERS RESOURCE BOOK" part="80">
Lastly, effective teaching and learning requires availability of teaching &
learning materials.
Teaching and learning materials:
Availability of instructional materials in local languages also needs to be
considered as part of the long-term planning process (USAID, 2015; Ball,
2011). Decentralised educational planning and budgeting can help countries
develop their own local-language materials (Benson, 2004). Local
communities can collaborate with government agencies and linguists to
create mother-tongue materials (Ball, 2011; Benson, 2004; Pinnock, 2009b).
Basing materials on standardised templates produced in the national or
official language can be rapid and cost-effective, since it uses centralised
technical expertise in curriculum development, illustrations, formatting, and
other elements (Mackenzie and Walker, n.d.). Open educational materials and
technology can help make instructional materials more widely available
(UNESCO, 2016).

National Curriculum
Development Centre,
P.O. Box 7002, Kampala.
www.ncdc.go.ug
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
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
