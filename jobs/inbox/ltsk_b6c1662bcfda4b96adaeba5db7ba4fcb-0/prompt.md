# Job ltsk_b6c1662bcfda4b96adaeba5db7ba4fcb-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for Mathematics, Primary Three 2026, Term 3.
The term has 10 teaching weeks and this subject has 7 periods per week. Every lesson is ONE 40-minute period, so keep each lesson small enough to teach in 40 minutes.
Ledgerly reserves the last lesson of each week for a review of that week.
Give at most 60 teaching/practice lesson entries in teaching order (the last lesson of the term is the end of term assessment).
Each lesson has a kind: "teach" (new content) or "practice" (the same subtopic as the teaching lesson just before it: exercises, oral work, drawing, matching, filling in blanks, ALL taken from the passages).
When the material is thin (common in lower primary), follow each teaching lesson with a practice lesson. Split big subtopics over several teaching lessons.
Never pad with content the passages do not have: if they cannot fill the term, return fewer lessons and list what is missing in gaps. Ledgerly fills the remaining weeks with revision.
You are composing the SCHOOL'S OWN scheme. The passages below (the official NCDC curriculum and guides, plus schemes of work, lesson plans, notes and past papers from the school e-library) are reference material:
The school's SCHEMES OF WORK for this class and term ("P 3 Primary Three MTC Scheme OF Work Teacher AC", "P.3 MATHEMATICS SCHEME OF WORK TERM III") are the BASE: follow the topics, subtopics and week-by-week order they agree on. Every topic they list for this term MUST become a unit, in their order, and their subtopics become the lessons, with about the pacing they give. Cite their passages in sourcePassageIds of every lesson that follows them.
The NCDC documents (titles starting "NCDC") only FILL GAPS: a topic NCDC lists for this term that the schemes lack gets its own unit where it fits best. Never drop or rename a schemes-of-work topic to fit NCDC. NCDC lower-primary thematic curricula list every learning area side by side in table columns separated by " | ": take only the Mathematics column.
Combine them in this authority order: the school's schemes of work for topics, sequence and pacing; NCDC for anything they miss; the strongest detailed notes for accurate teaching depth; past papers for expected applications and activities.
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

<passage id="lchk_8323980623d34f6084b18726676782c6" source="P3 Material A3 1" part="1">
©National Curriculum Development Centre, 2020 1
Ministry of Education
and Sports
PRIMARY THREE
SELF STUDY MATERIALS
MATHEMATICS
LITERACY
3 4 7
+ 5 2 1
8 6 8
5 7 6
+ 4 1 3
2 5 7
+ 6 4 1
7 8 2
+ 2 4 3
3 9 2
+ 5 0 0
LET US STAY SAFE OFF CORONA VIRUS
Wash your hands with soap and water.
Avoid touching your eyes, nose and mouth with
unwashed hands.
Stay at home and avoid crowds.
Keep corona virus away.
HEALTH TIP
©National Curriculum Development Centre, 2020 2
LET US STAY SAFE OFF CORONA VIRUS
Remind everybody at home to wash hands with soap
and clean water all the time.
HEALTH TIP
ENGLISH
©National Curriculum Development Centre, 2020 3
LET US STAY SAFE OFF CORONA VIRUS
Avoid moving out of your home unless you must. This
will protect you from getting infected with CORONA.
HEALTH TIP
MATHEMATICS
7 5 2
- 6 4 1
9 5 2
- 6 2 0
7 8 7
- 2 4 3
©National Curriculum Development Centre, 2020 4
ENGLISH
©National Curriculum Development Centre, 2020 5
LITERACY
MATHEMATICS
1 1 3
+ 2 0
©National Curriculum Development Centre, 2020 6
4 9 0
- 2 7 0
9 2 5
- 2 1 4
LITERACY
People cutting trees
People burning
charcoal
People cutting trees
People burning bush
Brick laying
People growing
crops
©National Curriculum Development Centre, 2020 7
LITERACY
©National Curriculum Development Centre, 2020 8
National Curriculum
Development Centre ,
P.O. Box 7002,
Kampala.
</passage>

<passage id="lchk_a82566f2577140ddad1714590a0f606f" source="P 3 Primary Three MTC Scheme OF Work Teacher AC" part="12">
what is the
cost of 1
book?
Sh 2100
÷7 = 300
shillings.
given correctly.
3-Read and
comprehend word
problems.
books
Chart
Real
money
s 2000
book 3
page 187
5&6 Shopping
Item
cost
Pen sh
500
Book sh
700
Pencil sh
200
Find the
cost of all
the above
items.
Pupils should be
able to
1-Identify the
money given.
2-Read and
comprehend word
problems.
Whole class
discussion
Brain storming
Accuracy
Neatness
Writing
Answering oral
questions
C/board
illustrati
on
Pupils
text
books
Chart
Real
money
Teachers
collection
MK
Primary
Mathematic
s 2000
book 3
page 181-
184
7&8 Topical
questions
Pupils should be
able to:
1-Answer the given
questions correctly.
2-Be time
conscious
Whole class
discussion
Brain storming
Accuracy
Neatness
Writing
Answering oral
questions
C/board
illustrati
on
Teachers
collections
MATHS SCHEME OF WORK TERM THREE
W
K
PD THEME SUB-
THEME
COMPETENCES METHODS SKILLS ACTIVITIES T/AIDS REF RM
1
1 to
8
Holiday work Pupils should be
able to:
1-Write corrections
for holiday work
Whole class
discussion
Neatness
Observati
on
Measuring
perimeter and
area of
different
shapes
Past
papers
Chalk
board
Past papers
2 1&2 BASIC
TECHNOL
OGY
Length
-What is
length?
-Measuring
things in the
class.
Tables, books,
chalk,
chalkboard
charts.
Pupils should be
able to:
1-Explain what
length is.
2-Measure some
things in the class.
3-Name the units
used in measuring
length (
introduction of
units)
Whole class
discussion
Brain storming
Accuracy
Neatness
Measuring
perimeter and
area of
different
shapes
Pupils text
books
C/board
illustration
MK
Primary
Mathematic
s 2000 bk3
pgs 141-
144
Understand
ing
Mathematic
s bk3
pgs77-80
3&4 Converting
different units
-Changing to
cm.
1m = 100cm
3m = 3x100 =
300cm
Changing to
m.
1m = 100cm
800cm =
800 ÷ 100 =
8m
Pupils should be
able to:
1-Change the given
units correctly.
Whole class
discussion
Brain storming
Accuracy
Neatness
Counting in
tens, hundreds
and
thousands.
Converting
different units
of length
Pupils text
books
C/board
illustration
MK
Primary
Mathematic
s 2000 bk4
pgs 186
Understand
ing
Mathematic
s bk3 pg79-
80
5&6 Adding length
M cm
12 34
+ 34 40
46 74
Pupils should be
able to:
1-Add the given
length correctly.
2-Read the word
Whole class
discussion
Brain storming
Accuracy
Neatness
Reading and
adding
numbers
correctly
Pupils text
books
C/board
illustration
MK
Primary
Mathematic
s 2000 bk3
pgs 147-
problems and
comprehend.
148 MK
Primary
Mathematic
s 2000 bk4
pgs 187-
188
7&8 Subtraction in
length
M cm
34 40
-19 22
15 18
Pupils should be
able to:
1-Subtract the
given length
correctly.
2-Read the word
problems and
comprehend.
Whole class
discussion
Brain storming
Accuracy
Neatness
Subtracting
numbers
correctly
Pupils text
books
C/board
illustration
MK
Primary
Mathematic
s 2000 bk3
pgs 149-
150 MK
Primary
Mathematic
s 2000 bk4
pgs 188-
189
3 1&2 Mass
What mass is
Units used in
measuring
mass
The metric
system,
Pupils should be
able to:
1-Define mass.
2-Name the basic
unit used for
measuring mass.
3-Demonstrate.
Whole class
discussion
Brain storming
Accuracy
Neatness
Writing
Answering
oral questions
Demonstratio
n and
measuring
masses of
different
objects
Pupils text
books
C/board
illustration
MK
Primary
Mathematic
s 2000 bk3
pgs 167-
170
Understand
ing
Mathematic
s bk3 pg 86
3&4 Converting
Kg to g
1kg = 1000g
4kg = 4x 1000
4000g
g to Kg
1kg = 1000g
3000g = ?
3000÷1000 =
3kg
Pupils should be
able to:
1-Change Kg to g
and vice versa.
Whole class
discussion
Brain storming
Accuracy
Neatness
Converting
</passage>

<passage id="lchk_b9b7353935074ab9b1174a03b96cce54" source="P.3 MATHEMATICS SCHEME OF WORK TERM III" part="1">
TERM THREE – PRIMARY
THREEMATHEMATICS SCHEME OF
WORK
P.3 MATHEMATICS SCHEME OF WORK FOR TERM III
W
K
P
D
THEME TOPIC SUB –
TOPIC
COMPETENCES CONTENT MTDS ACTIVITY LIFE
SKILLS
&
VALUES
T/ L
AIDS
REF
LANGUAGE SUBJECT
1 1
Culture and gender in our sub county
Measures
Time
Days of
week
- The learner states the
days of the week
correctly in their order.
- Calculates the number
of days in a week
- Changes days of weeks
- Identifies the days
before and after
- Reads and pronounces
- Spells the days of the
week
- Focus on spellings of
days of a week
Days of the week
7 days make a week
1 week – 7 days
Days of the week
1 st – Sunday ( sun)
2 nd – Monday – (Mon)
3 rd – Tuesday – (tue)
4th – Wednesday (wed)
5 th - Thursday (Thur)
6 th – Friday ( fri)
7 th – Saturday (sat)
Changing week’sto days
Example
How many days are in 3 weeks.
1 week = 7 days
3 weeks = (3 x 7) days
21 days
Examples 2
12 weeks
1 week = 7 days
12 weeks = 12 x 7 12
84 day x7
84
Guided
discussion
Question
and answer
techniques
Effective
communicat
ion
ion
Critical
thinking
Stating
the
days of
the
week
Convertin
g weeks
to days
Identifyin
g the
units
A chart
showing
days of
the
week
A
calendar
Mk
bk 3
pg
126
2 Changing
of days of
weeks
- The learner changes
days of weeks
- Reads the questions
given
- Divides the days given
Changing days to weeks
Change 14 days to weeks
7 days = 1 week
Guided
discussion
Questions
and answer
Effective
communicat
ion
Problem
Identifyi
ng the
days of
the
week
Chalk
board
Illustrati
on
to get the week
- Identifies that 1 day –
1 week
- Solves the work
application
14 days = 14 days
= 2 weeks
techniques solving
Appreciatio
n
Care
Solving
the
word
applicati
on
Converti
ng
weeks
to days
3 Completi
ng table
The
learner
draws the
table
Fills in the
missing
numbers
- Reads the given
questions
- Interprets the given
questions
WK 1 2 3 4 5
DS 7 14 21 28 35
1 WK = 7days
2 weeks = ( 2 x 7) days
= 14 days
3 x 7 = 21 days
4 x 7 = 28 days
5 x 7 = 35 days
Examples
WK 1 2 5 6 8
DS 7 14 35 42 56
35 ÷ 7 = 5 weeks
42 ÷ 7 = 6 weeks
56 ÷ 7 = 8 weeks
-
2 1 Adding
days and
weeks
Reads the question given
Interprets the given
questions
Adds the days and weeks
- Addition of days and weeks
Wks Days
2 3 3 + 2 = 5
+1 2 2 + 1 = 3
3 5
- Examples
Tom spent 4 week and 2 days
planting bean and 1 week and 3
days. Planting rice. Find the
total number of days and week
spent planting his crops
4 2 2 + 3 = 5
+ 1 3 4+1 = 5
5 5
Subtractio
n of weeks
and days
Reads the weeks and days
correctly
Subtracts the weeks and
days correctly
Work out
Wks Days
5 4 4-1 = 3
-3 1 5-3 = 2
2 3
Subtract
Wks Days
9 3 7+3 = 5
-4 6 10 – 6 = 4
4 4
8 – 4 = 4
A
new
Mk
bk 4
pag
e
181
– 82
2 Months of
the year
- Identifies that 1 year
has 12 months
Months of the year
12 months = 1 year
Guided
discovery
Creative
thinking
- Conver
ting
Chalk
board
Mk
bk 3
8 7
- The learner reads, spells
and pronounces the
months of the year
- Writes the months of
the year
- Converts years to
months
- Reads and interprets the
question
- Identifies the units for
the questions
- Solves the word
application
January = 31 days
February = 28 / 29 days
March = 31 days
April = 30 days
May = 31 days
June = 30 days
July = 31 days
August = 31 days
September = 30 days
October = 31 days
November = 30 days
December = 31 days
Conversation of years to months
Examples
How many months are in 3 years
1 year = 12 months
3 years = (3 x 12) months
3 years = 36 months
Change 2 years to months
1 year = 12 months
2 years = ( 2 x 12) months
= 24 months
Discussion
</passage>

<passage id="lchk_9e929da8cf7449a2b2bed12c60427b67" source="NCDC P.3 teachers guide Book" part="1">
National Primary School Curriculum
for Uganda

Teacher’s Guide
Primary Three

National Curriculum Development Centre, Kampala
2008

NATIONAL CURRICULUM DEVELOPMENT CENTRE (NCDC),
KAMPALA UGANDA

Copyright © NCDC. 2008

P.O. BOX 7002,
KAMPALA – UGANDA

URL: www.ncdc.go.ug

All rights reserved. No part of this publication should be reproduced, stored in a retrieval system
or transmitted in any form by any means, electronic, mechanical, photocopying, recording or
otherwise without the permission of the author’s publisher. No patent liability is assumed with
respect to the use of the information contained herein.

ISBN 978-9970-117-05-5 (Paperback edition)

Published by National Curriculum Development Centre
Cover Designed by NCDC - Kyambogo

ii

Acknowledgement
The National Curriculum Development Centre (NCDC) gratefully acknowledges the efforts, commitment and
contributions of the Thematic Curriculum Review panel(TCRP) who worked very tirelessly on the preparations
and production of the Primary Three Thematic Curriculum.

The NCDC would also like to recognise the invaluable advice offered by the Consultants during the
process of the development of the Curriculum.

The preparation of this Curriculum benefited greatly from the support and valuable contributions of the Curriculum
Task Force (CTF).NCDC would therefore like to express sincere appreciation to those members of the TCTF
who provided extremely useful comments, suggestions and inputsduring the drafting and finalisation of the
Curriculum.

Special thanks go to the Permanent Secretary, Ministry of Education and Sports for ensuring the timely
release of the funds to support the development of this document.

There is no doubt that the successful completion of this Curriculum could not have been realised without the
cooperation and willingness of all the different institutions:
The Management of the Teacher’s Colleges and Primary Schools for having permitted their members of
staff for longer periods of absence from duty during the writing sessions.

The Management of the Primary Schools that allowed NCDC to use their schools for piloting the drafts of
the Teacher Resource Books for the purposes of coming up with a quality book.

The District Education Officers in the trial districts for the support, supervision and encouragement to the
teachers during the pilot phase.

Last but not least, thanks to all those behind the scenes – groups of people, organisations and individuals who
formed part of the team that worked hard on the preparation and production of this document.

Connie Kateeba
Director, National Curriculum Development Centre - NCDC

iii

Foreword
The Curriculum for Primary One – Primary Three
(P1-P3)

Hon. Geradine Namirembe

T
Bitamazire (MP)
he failure by a high proportion of the children to attain acceptable levels of proficiency in reading and writing at Primary
Three (3) level is considered to be a barrier to the children’s full enjoyment of their right to education as enshrined in
Section 30 of the Constitution of the Republic of Uganda (1995 Edition). Sector-wide reflection on this phenomenon has
led to identification of challenges which need urgent attention to make schooling more beneficial to the children. The Ministry
commissioned a study which carried out a situational analysis which showed that one of the factors causing poor learner
performance in literacy, numeracy and life skills were the structure of the Primary School Curriculum.
</passage>

<passage id="lchk_aea7af1e20484af99b15129d1e0896a0" source="P 3 Mathematics Term Three 1" part="1">
For more lesson notes, please visit www.freshteacheruganda.com
PRIMARY THREE
TERM THREE
MATHEMATICS
THEME: HEALTH IN OUR SUB COUNTY/DIVISION
SUBTHEME: MEASURES (TIME)
TELLING TIME IN HOURS
- We tell tine in hours and minutes
- 1 hour = 60 minutes
- A long hand tells minutes and a short hand tells hours
Examples
What is the time?
It is 8 0’clock it is 4 o’clock
For more lesson notes, please visit www.freshteacheruganda.com
Exercise
Tell the time
(i) (ii) (iii)
______________________ ___________________ _________________
(iv) (v) (vi)
(vii) (viii) (ix)
_____________________ __________________ __________________
(x)
For more lesson notes, please visit www.freshteacheruganda.com
Telling time in hours and minutes (a half past)
Examples when the long hand (minute hand) reaches 6, we say that it is half past. The short hand will then
point between two numbers.
It is a half past 1 o’clock It is a half past 11 o’clock
Exercise
1. 2. 3.
For more lesson notes, please visit www.freshteacheruganda.com
______________________ ______________________ __________________
5. 6. 7.
_____________________ __________________ __________________
8.
Telling time in a quarter past
- When the minute had points to 3 we say quarter past or 15 minutes past the hour.
Examples
It is a quarter past 4 o’clock. It is a quarter past 1 o’clock. It is a quarter past 7
For more lesson notes, please visit www.freshteacheruganda.com
Exercise
What is the time?
Using a quarter to
- The time after half past any hour can be told using to.
- When the minute hand points to 9. We say 15 minutes to or a quarter to the next hours.
For more lesson notes, please visit www.freshteacheruganda.com
Examples
It is a quarter to 6 o’clock It is a quarter to 1 o’clock.
It is a quarter t0 3 o’clock It is a quarter to 11 o’clock
Showing Time on the Clock Faces
Examples
It is 25 minutes past 1 o’clock It is 35 minutes past 11 o’clock
For more lesson notes, please visit www.freshteacheruganda.com
It is a quarter to 3 o’clock
Exercise
Show the time on the clock faces below.
It is a half past three It is 7 o’clock It twelve o’clock
It is a quarter past ten o’clock it is a quarter past six it is six o’clock
It is twenty five minutes past eight o’clock
For more lesson notes, please visit www.freshteacheruganda.com
More about time
- We tell time in hours, minutes, seconds, days, weeks, months, years.
- We also need to know about the calendar.
NB: There are 60 minutes in 1 hour
Therefore 60 min = 1 hour
-There are 24 hours in a day.
Examples
1. How many hours are in 2 days
1 day = 24 hours
2 days = 24 x 2
= 48 hours
More about time
24 hours = 1 day
7 days = 1 week
4 weeks = 1 month
12 months = 1 year
52 weeks = 1 year
365/366 days = 1 year
Days of the week
- 7 days make a week.
These are Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday
October 2012
Sun Mon Tue Wed Thurs. Fri Sat
1 2 3 4 5
6 7 8 9 10 11 12
13 14 15 16 17 18 19
For more lesson notes, please visit www.freshteacheruganda.com
20 21 22 23 24 25 26
27 28 29 30
Questions
1. What is the first day of the week?
2. What is the fourth day of the week?
3. What is the last day of the week?
4. How many days are in 2 weeks?
5. Write down the days of the week with letter T.
6. What is the second day of the week?
7. How many days are in 7 weeks?
8. Complete the table.
Weeks 1 2 3 4 ______ ______ 6
Days 7 14 ___ ___ 35 49 ___
Exercise
1. What day is the first in the month of October?
2. How many Saturdays are in the month?
</passage>

<passage id="lchk_b23e898b48884dc083324ea2b9a9bbfb" source="P.3 MATH" part="1">
LA MENNAIS SCHOOLS EXAMINATIONS COMMITTEE
BEGINNING OF TERM III EXAMINATIONS - 2022
MATHEMATICS P.3
Time: 2hours 30 minutes
: 2 hours 15 minutes
Name:___________________________________________________________________________________
School: __________________________________________________________Stream_______________
SECTION: A
1. Work out:
2. Shade X∪Y
3. Write 243 in words
4. Multiply:
5. Divide:
6. Workout:
7. Circle the smallest number
16, 45, 15, 100
8. Find the missing number
9. Subtract:
10. What fraction has been shaded?
11. Given that set below
How many elements has set B?
12. Fill in the missing numbers.
3, 6, ________, 12 , ____________
13. Use the numberline to work out:
5+2= _________________
14. Name the shape.
____________________________
15. What number has been shown on the abacus?
16. What time is it on the clock face?
_____________________________
17.How many days make up 2 weeks?
18. Draw a symbol of equivalent set.
19.Find the value of 6 in 67.
20. Express 9 as a roman numeral.
SECTION B (60 MARKS)
21. a) Add: b) Subtract: 2 marks @
22. Name the shapes. 2 marks
23. Put these on the abacus 2 marks @
c) Write one hundred twenty seven in figures.
24. Given that set
A=(a, b, o, d, e, f, g)
B=(a, e, i, o, u)
a)Represent the above information on the Venn diagram. 3 marks
b)Find (1 mark)
c) Find (2 marks)
25. What is the place value of 3 in
a) 3450? (1 mark)
_________________________________________
b) 127= ____________ hundreds ________________Tens _______________ ones. (1 mark)
26.Study the price list below and answer the questions.
a)How much can one pay for a pencil? (1 mark)
b) What is the cheaper item? (1 mark)
c)Find the total cost of the three items. (2 marks)
27. Write in short form. 2 marks@
a) 3000+500+80+9
b) Expand 234
c) Write the value of 3 in the number 4232.
28. Find the missing number. 2 marks@
a) b)
c) ÷ 4 = 5
29. Show 10 o’clock on the clock face. 2 marks @
a)
b) Workout;
30. Use the magic square to answer questions.
a)Find the magic sum. 1 mark
b) Find the value of ; 2 marks@
a = b =
c =
31. Workout: 2 marks @
a)
b) A man sold 123 litres of milk and remained with 115 litres of milk. How many litres of milk were there altogether.
32. Use the graph below to answer the questions that follow.
a)How many books did Paul get? 1 mark
b) Who got the least number of books. 1 mark
c) How many books did Tom and John get altogether? 2 marks
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
