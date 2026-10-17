# Job ltsk_39e522d71da14d968d7290a8e3e017e2-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for Christian Religious Education, Primary Three 2026, Term 3.
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


Do NOT write lesson content yet. Each unit and lesson must cite the passage ids it comes from in sourcePassageIds.

Reply shape:
{"title":string,"summary":string,"units":[{"title":string,"theme":string|null,"weekFrom":int|null,"weekTo":int|null,"competences":string|null,"sourcePassageIds":[string],"lessons":[{"title":string,"subtopic":string|null,"kind":"teach"|"practice","objectives":[string],"sourcePassageIds":[string]}]}],"gaps":[string]}

<passages>
<passage id="lchk_6f11d17629e74461865445d9f26369f1" source="NCDC P3 Thematic Curr 21 November" part="1">
THE REPUBLIC OF UGANDA
Ministry of Education and Sports

Primary School Curriculum

Primary 3

National Curriculum Development Centre
May 2008

NATIONAL CURRICULUM DEVELOPMENT CENTRE (NCDC), KAMPALA UGANDA

Copyright © | NCDC. 2008
P.O. BOX 7002,
KAMPALA – UGANDA

URL: www.ncdc.go.ug

All rights reserved. No part of this syllabus should be reproduced, stored in a retrieval system or
transmitted in any form by any means, electronic, mechanical, photocopying, recording or otherwise
without the permission of the publisher. No patent liability is assumed with respect to the use of the
information contained herein.

ISBN 978-9970-117-05-5 (Paperback edition)

Published by National Curriculum Development Centre
Cover Designed by NCDC - Kyambogo

ii

ACKNOWLEGEMENT
The National Curriculum Development Centre (NCDC) gratefully acknowledges the efforts, commitment and contributions of the
different Teacher Resource Book panels who worked very tirelessly on the preparations and production of the Teacher Resource
Books.

NCDC would also like to recognise the invaluable advice offered by the District Language Boards during the process of the
development of the Teacher Resources Books.

Special thanks go to the Permanent Secretary, Ministry of Education and Sports for ensuring the timely release of the funds to
support the development of this document.

There is no doubt that the successful completion of this Curriculum could not have been realised without the cooperation and
willingness of all the different institutions:

• | The Management of the Teacher’s Colleges and Primary Schools for having permitted their members of staff for longer periods
of absence from duty during the writing sessions.

• | The Management of the Primary Schools that allowed NCDC to use their schools for piloting the drafts of the Teacher
Resource Books for the purposes of coming up with a quality book.

• | The District Education Officers in the trial districts for the support, supervision and encouragement to the teachers during the
pilot phase.

Last but not least, thanks to all those behind the scenes – groups of people, organisations and individuals who formed part of the
team that worked hard on the preparation and production of this document.

Connie Kateeba
Director, National Curriculum Development Centre - NCDC

iii

FOREWORD
The Curriculum for Primary One – Primary Three
(P1-P3)

Hon. Geradine Namirembe
Bitamazire (MP)
The failure by a high proportion of the children to attain acceptable levels of proficiency in reading and writing at Primary
Three (3) level is considered to be a barrier to the children’s full enjoyment of their right to education as enshrined in
Section 30 of the Constitution of the Republic of Uganda (1995 Edition). Sector-wide reflection on this phenomenon has
led to identification of challenges which need urgent attention to make schooling more beneficial to the children. The
Ministry commissioned a study which carried out a situational analysis which showed that one of the factors causing
poor learner performance in literacy, numeracy and life skills were the structure of the Primary School Curriculum.

The Curriculum’s emphasis on the acquisition of facts in various subjects at Primary Schools influenced teaching to
focus mainly on recall and other low order cognitive skills. This orientation was further reinforced by leaner assessment
</passage>

<passage id="lchk_8a908ba4886e4d62ac30811dbe54f9e4" source="NCDC P3 Thematic Curr 21 November" part="50">
• | Jesus’ example of prayer and | • | Identifying different situations which require | • | Interpersonal relationship | • | Appreciation
teaching | prayer and teaching | • | Effective communication | • | Forgiveness
• | When, where and how to pray | • | Talking about different occasions on which | • | Creative thinking | • | Faithfulness
• | The Lord’s prayer | Jesus prayed and taught | • | Critical thinking | • | Unity
• | Praying for others | • | Talking about when, where and how to pray | • | Problem-solving | • | Cooperation

Mark 1: 35 | • | Reciting the Lord’s Prayer | • | Obedience
Mathew 6: 9-13 | • | Asking and answering questions
Luke 22: 32 | • | Singing songs about prayer and teaching
John 17: 20-21

Assessment Guidelines (Weeks 10-12)
• Talk about the importance of different personal abilities.
• Sing songs about different personal abilities.
• Talk about the different ways in which family members resemble.
• Talk about different occasions on which Jesus prayed and taught.
• Recite the Lord’s Prayer.

TERM III
Theme: | Christians Grow in Jesus Weeks 1-3:
Learning Outcome: The child appreciates and practices the value of tolerance and forgiveness for maintaining good relationship with others in society.
Sub-theme | Content | Competences | Life skills | Values
Forgiveness and | • Traditional ways of encouraging | • Talking about traditional ways of encouraging | • Critical thinking | • Care
Acceptance | forgiveness | forgiveness | • Creative thinking | • Acceptance
Mathew 18: 15-16 | • Talking about the importance of forgiveness | • Friendship formation | • Tolerance
Luke 17: 23 | • Telling and retelling stories | • Effective communication | • Kindness
• Ways of forgiveness | • Asking and answering questions | • Problem-solving | • Responsibility
- wrong doings that required | • Singing songs about forgiveness | • Non-violent conflict
forgiveness | • Reciting the gospel message Luke 17: 23 | resolution

• | Resolving differences without | • | Identifying wrong doings which require forgiveness | • | Friendship formation | • | Acceptance
violence | • | Talking about how to resolve differences without | • | Empathy | • | Tolerance
• | Desire for forgiveness | violence | • | Self-awareness | • | Unity
Genesis 27: 30-36 | • | Telling and retelling stories | • | Non-violent conflict | • | Concern
Genesis 33: 1-11 | • | Asking and answering questions | resolution | • | Friendliness
Mathew 18: 15-35 | • | Role-playing forgives | • | Coping with stress | • | Responsibility
Genesis 37: 25-28 | • | Reciting a memory verse | • | Coping with emotions
Luke 15: 11-24 | Numbers 5:7
Mathew 6: 12
Mathew 5: 38-42
• | Acceptance | • | Identifying causes of conflicts | • | Critical thinking | • | Acceptance
- need to accept others | • | Telling and retelling the story of Joseph and his | • | Coping with emotions | • | Forgiveness
- the joy of good relationship | brothers | • | Coping with stress | • | Tolerance
- the help of the Holy Spirit in | • | Talking about ways of accepting and being tolerant | • | Creative thinking | • | Friendliness
forgiving others | of others differences | • | Love
• | Asking and answering questions | • | Concern

Assessment Guidelines (Weeks 1-3)
• Talk about traditional ways of encouraging forgiveness.
• Talk about the importance of forgiveness.
• Talk about how to resolve conflict without violence.
• Role play forgiveness.
• Identify causes of conflicts.
</passage>

<passage id="lchk_801d58ef610b45fc98ad724cde437368" source="NCDC P3 Thematic Curr 21 November" part="51">
• Talk about ways of accepting and being tolerant of others’ differences.

Weeks 4-6:
Learning Outcome: The child appreciates the concept and practice of fairness as well as forgiveness in different daily
life situations.
Sub-theme | Content | Competences | Life skills | Values
Treating Others Fairly | • Fair and unfair behaviour | • Identifying the causes of unfair | • Critical thinking | • Sharing
Genesis 27: 1-29 | behaviour | • Coping with emotions | • Cooperation
Genesis 37: 1-4 | • Talking about the causes of unfair | • Coping with stress | • Friendliness
Luke 3: 10-14 | behaviour | • Effective communication | • Care
Mathew 18: 21-34 | • Talking about the importance of fair | • Interpersonal relationship | • Love
behaviour
• Telling and retelling stories
• Asking and answering questions
• | Being fair | • Talking about the need to treat others | • | Friendship formation | • | Sharing
- at home | fairly | • | Interpersonal relationship | • | Love
- at school | • Telling / retelling Bible stories | • | Self esteem | • | Concern
- community | Exodus 16: 4-26 | • | Coping with emotions | • | Friendliness
Luke 3: 10-14 | John 6: 1-13 | • | Coping with stress. | • | Acceptance
Mathew 20: 1-16 | • Asking and answering questions | • | Care
Exodus 16: 4-26 | • | Obedience
John 6: 1-13
• | Cheating | • | Identifying causes of cheating | • | Coping with emotions | • | Acceptance
- causes of cheating | • | Talking about how to avoid cheating | • | Coping with stress. | • | Concern
- how to avoid cheating | • | Telling and retelling stories | • | Non-violent conflict | • | Care
Luke 19: 1-7 | • | Asking and answering questions | resolution. | • | Responsibility
• | Dramatising cheating | • | Respect
• | Love

Assessment Guidelines (Weeks 4-6)
• Talk about the causes of unfair behaviour.
• Talk about the importance of fair behaviour.
• Tell and re-tell Bible stories Exodus 16: 4-26, John 6: 1-13.
• Talk about how to avoid cheating.
• Ask and answer questions.

Weeks 7-9:
Learning Outcome: The child relates the prophecies in the Old Testament to the coming of Jesus and appreciates the Messiahship and joy brought by Jesus to all Christians for
harmonious living.
Sub-theme | Content | Competences | Life skills | Values
Jesus Brings Joy | • Prophecies and the fulfilment | • Naming different prophets in the Old Testament who | • Critical thinking | • Love
- prophecies from the Old | prophesied the coming of Jesus Christ | • Interpersonal | • Cooperation
Testament about Jesus | • Talking about the importance of the prophecy about the | relationship | • Unity
Isaiah 40: 1-10 | coming of Jesus | • Creative thinking | • Sharing
Micah 5: 2 | • Telling and retelling stories about the prophecy of Jesus’ | • Effective | • Acceptance
Luke 3: 3-6 | coming | communication | • Respect
- events of the first | • Talking about the events of the first Christmas in relation | • Friendship formation. | • Obedience
Christmas related to the | to the prophecy in the Old Testament | • Responsibility
prophecies of the Old | • Asking and answering questions | • Faithfulness
Testament
• Care
• Tolerance
• | Events of the first Christmas | • | Identifying the most important events of the first | • | Friendship formation | • Love
related to the prophecies in the | Christmas | • | Coping with emotions | • Obedience
Old Testament. | • | Describing the birth of Jesus | • | Coping with stress | • Care
</passage>

<passage id="lchk_b28499144e76424abfa8ce46c8f61e5c" source="NCDC P3 Thematic Curr 21 November" part="52">
- the birth of Jesus | • | Talking about different categories of people who | • | Problem-solving | • Sharing
- the visit of Angels to the | worshipped baby Jesus as a king | • | Interpersonal | • Cooperation
shepherd | • | Naming the gifts which were offered to baby Jesus | relationship | • Unity
- the visit of the wise men | • | Telling and retelling stories about the birth of Jesus | • | Creative thinking | • Acceptance
Mathew 1: 18-24 | • | Asking and answering questions about the birth of Jesus | • | Critical thinking | • Concern
Luke 2: 8-20 | • | Singing songs about the birth of Jesus | Negotiation
• | • Respect
Mathew 2: 1-12
• Responsibility
Luke 2: 1-7
• | Preparation for Christmas | • | Talking about how to prepare for Christmas at home and | • | Interpersonal | • | Sharing
- how to prepare for | in the church | relationship | • | Responsibility
Christmas | • | Naming different people with whom we celebrate | • | Friendship-formation | • | Love
- celebrating with others | Christmas | • | Critical thinking | • | Care
Luke 1: 39-48 | • | Identifying different activities of entertainment that we | • | Creative thinking | • | Respect
Luke 2: 4-20 | engage in during Christmas | • | Effective | • | Team work
Luke 2: 25-25 | • | Asking and answering questions | communication | • | Obedience
Isaiah 9: 6 | • | Telling and retelling stories about the celebrations of | • | Cooperation
Christmas
• | Singing / signing songs about Christmas
• | Dramatising the birth of Jesus

Assessment Guidelines (Weeks 7-9)
• Name different prophets in the Old Testament who prophesied the coming of Jesus Christ.
• Tell and re-tell stories about the prophecy of Jesus’ coming.
• Talk about the events of the first Christmas in relation to the prophecy in the Old Testament.
• Talk about different categories of people who worshipped baby Jesus as a king.
• Talk about how to prepare for Christmas at home and in the church.

Weeks 10-12:
Sub-theme | Content | Competences | Life skills | Values
The Joy of | • Preparation for Christmas play | • Talking about the importance of Christmas | • Critical thinking | • Respect
Christmas | - making Christmas cards | • Identifying different activities we do in | • Creative thinking | • Responsibility
- making Christmas costumes | preparation for Christmas | • Friendship formation. | • Unity
Mathew 2: 1-12 | • Designing Christmas cards | • Assertiveness | • Cooperation
• Writing Christmas messages | • Interpersonal relationship. | • Sharing
• Designing and making Christmas costumes | • Effective communication | • Creativity
• Telling and retelling stories related to | • Care
preparation for Christmas
• Singing / signing songs related to Christmas
celebrations
• Asking and answering questions
• | Preparation for Christmas play | • Singing Christmas carols. | • | Effective communication | • | Making choice
- Christmas carols | • Talking about the importance of the messages | • | Critical thinking | • | Acceptance
- different roles in the play (from | in Christmas carols | • | Creative thinking | • | Responsibility
the visit of the Angel to the Virgin | • Identifying different roles in the Christmas play | • | Interpersonal relationship | • | Respect
Mary , to the birth of baby Jesus | • Acting the first part in the Christmas play | • | Friendship formation | • | Obedience
in the manger as Part 1) | • Asking and answering questions | • | Decision-making | • | Sharing
Luke 2: 1-19 | • | Self-esteem | • | Cooperation
</passage>

<passage id="lchk_ae56dcaa6e2e43ee975880eec54f3475" source="NCDC P3 Thematic Curr 21 November" part="58">
• Reading the Arabic alphabet | • | Talking about the Arabic alphabet with vowels | • | Creative thinking | • | Respect
- recognising the vowels | • | Identifying vowels in the words. | • | Critical thinking | • | Responsibility
• Formation of words out of combined letters | • | Identifying one vowel and two different letters to form two-letter | • | Effective communication | • | Care
• Pronouncing words | words with similar vowels | • | Decision making | • | Sharing
- letters with vowels | • | Asking and answering questions
• | Writing Arabic alphabet

Weeks 4-6
Theme: | Tawhiid (Faith) Sub-theme: | Uniqueness of the Qur’an
Learning outcome: The child appreciates and recognises the uniqueness of the Qur’an for meaningful spiritual insight and growth.
Content | Competences | Life skills | Values
• Uniqueness of the Qur’an | • Explaining what ‘uniqueness’ means | • Critical thinking | • Respect
- the unique nature of the Qur’an | • Talking about unique nature of the Quran | • Effective communication. | • Care
(miracle) | • Asking and answering questions | • Creative thinking. | • Responsibility
- universality of its message
- other Holy books
- its authenticity

Weeks 4-6
Theme: | Fiqh (Practice) Sub-theme: | Impurities and Toilet Manners
Learning outcome: | The child appreciates and practices the teaching about impurities, Najasah and Istinjal for meaningful performance of Wudhu in order to
live a healthy religious life.
Content | Competences | Life skills | Values
• Impurities | • Explaining what Najasah means | • Coping with stress | • Obedience

- | definition of Najasah (impurities) | • | Identifying the examples of impurities | • | Coping with emotions | • | Responsibility
- | types of impurities | • | Asking and answering questions | • | Effective communication | • | Sharing
- | examples of impurities on salat, Wudhu | • | Critical thinking | • | Cleanliness
and reading the Qur’an | • | Care
• | Islamic teaching in respect to Istinjae (toilet | • | Talking about how Moslems should use toilets with or without | • | Critical thinking | • | Cleanliness
manners) | water | • | Creative thinking | • | Care
• | Ablution | • | Explaining the conditions under which ablutions become | • | Coping with stress | • | Responsibility
• | Condition why ablution becomes necessary | necessary | • | Coping with emotions | • | Obedience
a) Salat | • | Effective communication | • | Sharing
b) Recitation of the Qur’an
• | Asking and answering questions

Assessment Guidelines (Weeks 4-6)
• Talk about uniqueness nature of the Qur’an.
• Explain what Najasah means.
• Identify the examples of impurities.
• Talk about how Moslems should use toilets with or without water.
• Explain the conditions under which ablutions becomes necessary.

Weeks 7-9
Theme: | Moral and Spiritual Teachings, Sub-Theme: | Dua
Learning outcome: The child understands, appreciates and participates in the practice of Duas for appropriate occasions in order to acquire
meaningful religious experiences and relationships with others.
Content | Competences | Life skills | Values
• Dua | • Reciting Duas related to knowledge | • Effective communication | • Obedience
- acquisition of knowledge | • Talking about each Dua | • Creative thinking | • Cleanliness
- reciting Duas | • Role-playing the Dua practices | • Critical thinking | • Care
a) Rabizidin ilmawar | • Talking about the importance of seeking knowledge | • Coping with stress | • Responsibility
</passage>

<passage id="lchk_558a97a0e05c4c8d94be54acb4d9d9d5" source="NCDC P3 Thematic Curr 21 November" part="64">
• Jumps | • | Jumping from various heights | • | Coping with emotions | • | Appreciation
• Heights | • | Running and jumping | • | Creative thinking | • | Tolerance
• Run | • | Standing long jump, high jump | • | Determination

Assessment Guidelines (Weeks 7-9)
• Jump in time to signal
• Jump off, on and over objects
• Run as instructed

Theme: | Athletics for Lower Primary | (Weeks 10-12)
Content (abilities, skills and | Activities | Competences | Life skills | Values
knowledge)
Throwing Experiences | • | Throwing and catching with partner | • | Throwing | • | Effective communication | • | Confidence
• Throwing and aiming over | • | Throwing a few metres from the target, then gradually | • | Targeting | • | Coping with emotions | • | Acceptance
objects | increase distance (using large balls and large targets) | • | Aiming | • | Decision-making | • | Appreciation
• Throwing games and targets | • | Rolling the ball at a target | • | Playing | • | Creative thinking | • | Respect
• | Throwing and catching the ball (individual) | • | Critical thinking | • | Patience
• | Tolerance
• | Cooperation

Assessment Guidelines (Weeks 10-12)
• Throw to a partner.
• Catch from partner or individually.
• Aim at the target from a given position.
</passage>

<passage id="lchk_76d6f78605744cabb34657b1da5a5b88" source="NCDC CRE P.3 TEACHERS RESOURCE BOOK" part="1">
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
PRIMARY THREE

Copyright © National Curriculum Development Centre, Uganda, 2020

A product of the National Curriculum Development Centre for the
Ministry of Education and Sports with support from the Government
of Uganda

FIRST EDITION

National Curriculum Development Centre
P.O. Box 7002,
Kampala- Uganda
www.ncdc.co.ug

ISBN: 978-9970-494-93-4

All rights reserved: No part of this publication may be reproduced,
stored in a retrieval system or transmitted in any form or by any means,
electronic, mechanical, photocopying, recording, or otherwise, without
the prior permission of the copyright holder

PRIMARY THREE | TEACHERS’ RESOURCE BOOK

CONTENTS
FOREWORD.................................................................................................. IX
ACKNOWLEDGEMENTS ................................................................................... X
LIST OF ACRONYMS ...................................................................................... XI
INTRODUCTION ............................................................................................. 1
THE PURPOSE OF THE TEACHER’S RESOURCE BOOK ................................................. 1
HOW TO USE THE TEACHER’S RESOURCE BOOK ......................................................... 2
THE GENERAL PROCEDURE OF TEACHING CHRISTIAN RELIGIOUS EDUCATION ......... 3
THE LESSON PLAN STRUCTURE IN THE TEACHER’S RESOURCE BOOK....................... 3
SAMPLE SCHEME OF WORK FOR CHRISTIAN RELIGIOUS EDUCATION ......................... 6
SAMPLE LESSON PLAN FOR CHRISTIAN RELIGIOUS EDUCATION ................................ 8
TERM I WEEK 1 ............................................................................................ 11
THEME: CHRISTIANS GROW IN JESUS CHRIST ................................................ 11
SUB-THEME: TRADITIONS .......................................................................................... 11
LESSON 1: TRADITIONAL CUSTOMS ........................................................................... 11
LESSON 2: INDIVIDUAL SOCIETAL TRADITIONAL PRACTICES .................................... 13
LESSON 3: INDIVIDUAL SOCIETAL TRADITIONAL PRACTICES AND VALUES ............... 15
WEEK 2 ....................................................................................................... 17
LESSON 1: INDIVIDUAL SOCIETAL TRADITIONAL CUSTOMS ...................................... 17
LESSON 2: IMPORTANCE OF TRADITIONAL PRACTICES AND VALUES ........................ 19
LESSON 3: TRADITIONS AND CUSTOMS FROM OTHER CULTURES ............................ 21
WEEK 3 ....................................................................................................... 23
LESSON 1: IMPORTANCE OF OTHER PEOPLE’S CUSTOMS AND PRACTICES .............. 23
LESSON 2: CHRISTIAN PRACTICES/CUSTOMS ........................................................... 25
LESSON 3: IMPORTANCE OF CHRISTIAN PRACTICES AND CUSTOMS (PROJECT) ...... 27
WEEK 4 ....................................................................................................... 29
THEME: CHRISTIANS GROW IN JESUS CHRIST ................................................ 29
SUB-THEME: LEADERSHIP .......................................................................................... 29
</passage>

<passage id="lchk_a83013cd383c48de90628d362d713da2" source="NCDC IRE P.3 TEACHERS RESOURCE BOOK" part="79">
Lastly, effective teaching and learning requires availability of teaching &
learning materials.

Teaching and learning materials: Availability of instructional materials in
local languages also needs to be considered as part of the long-term planning
process (USAID, 2015; Ball, 2011). Decentralised educational planning and

PRIMARY THREE | TEACHERS’ RESOURCE BOOK

budgeting can help countries develop their own local-language materials
(Benson, 2004). Local communities can collaborate with government agencies
and linguists to create mother-tongue materials (Ball, 2011; Benson, 2004;
Pinnock, 2009b). Basing materials on standardised templates produced in the
national or official language can be rapid and cost-effective, since it uses
centralised technical expertise in curriculum development, illustrations,
formatting, and other elements (Mackenzie and Walker, n.d.). Open
educational materials and technology can help make instructional materials
more widely available (UNESCO, 2016).

PRIMARY THREE | TEACHERS’ RESOURCE BOOK

National Curriculum
Development Centre,
P.O. Box 7002, Kampala.
www.ncdc.go.ug
</passage>

<passage id="lchk_4618ea35e3104a36aa29f27bacbf6419" source="P3 CRE" part="3">
 Micah: He foretold that a Saviour was to be born in a town called Bethlehem.
For more lesson notes, please visit www.freshteacheruganda.com
 Zachariah: He foretold that Jesus was to be born and live an exemplary life. He
also foretold that Jesus was to go to Jerusalem riding a donkey.
 John the Baptist:
 He preached about the coming of Jesus Christ and baptized many people.
 He told people to repent for their sins.
 The mother of John the Baptist was called Elizabeth.
 Elizabeth was a sister to Mary the Mother of Jesus Christ.
 The Father of John the Baptist was called Zechariah
 John the baptized Jesus in River Jordan and other people.
 Messages brought by angels .
 Angels are spirits who live in heaven with God.
 Angel Gabriel: He announced the birth of John the Baptist and Jesus
Christ.
 Angel Gabriel told Joseph to marry the Virgin Mary.
 He also told the parents of Jesus Christ to take Baby Jesus to Egypt to run
away from King Herod who wanted to kill him.
Ways how God speaks to us :
 Through the things he created.
 Through messengers.
 Through angels
 Through the Bible.
Activity ;
1. Write down any four ways how God speaks to Christians.
2. Name any one of the prophet of God.
3. List down any four prophets who foretold the coming of Jesus Christ.
4. Who was the Mother of John the Baptist?
5. Who is an angel?
For more lesson notes, please visit www.freshteacheruganda.com
</passage>

<passage id="lchk_9c9307d24eba4110b8493160dcb29021" source="A.JJEB.IRE. P 3. 2020" part="1">
P235/3
ISLAMIC
RELIGIOUS
EDUCATION
Paper 3
HISTORY OF ISLAM
DECEMBER, 2020
2
½ hours
JINJA JOINT EXAMINATIONS BOARD
Uganda Advanced Certificate of Education
MOCK EXAMINATIONS – DECEMBER, 2020
ISLAMIC RELIGIOUS EDUCATION
HISTORY OF ISLAM
Paper 3
2 hours 30 minutes
INSTRUCTIONS TO CANDIDATES :
Answer any FOUR
questions.
ALL questions carry equal marks.
© 2020 Jinja Joint Examinations Board
Turn Over
_________________________________________________________________________________________________
1. (a) Analyse the political life of the arabs during Jahiriyya period
(b) In what ways was their political system oppressive?
2. Account Prophet Muhammad’s (PBUH) Expulsion of the Jewish clans
from Medina
3. Why did unrest emerge during Ali’s reign?.
4. Assess the Muawiyah’s contribution to the establishment of the
Ummayad dynasty.
5. “Ummayyad rulers valued the work of the military as well as religious
institutions. Assess the validity of the statement.
6. (a) Discuss the challenges faced by caliph Abu Jaffar al – Mansur.
(b) Explain the role of the military in consolidating peace during
his reign.
7. Examine the following aspects of life under the Abbasids.
(a) The political organization and
(b) Scholarship learning.
8. Account for the delay in the establishment of the Fatimid rule despite
the early development of their sect.
9. Discuss the political organization of fatimids.
(a) Explain the weakness of the Fatimid rulers.
(b) Explain the weakness of the Fatimid rulers.
10. Assess the impact of the anti-Islamic movement on the Muslim
world between the 11 th to the 13 th centuries
11. Account for the rise of the Safavids to power.
12. Examine the contributions of Sulaiman the magnificent to the
prosperity of the Ottoman Empire.
_________________________________________________________________________________________________
© 2020 Jinja Joint Examinations Board
End
_________________________________________________________________________________________________
2
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
