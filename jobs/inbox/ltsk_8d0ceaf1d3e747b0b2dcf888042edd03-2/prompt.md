# Job ltsk_8d0ceaf1d3e747b0b2dcf888042edd03-2

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for Science, Primary Seven 2026, Term 3.
The term has 10 teaching weeks and this subject has 6 periods per week. Every lesson is ONE 40-minute period, so keep each lesson small enough to teach in 40 minutes.
There are no weekly review lessons: the subject has a lot of content, so every period teaches or practises.
Give at most 59 teaching/practice lesson entries in teaching order (the last lesson of the term is the end of term assessment).
Each lesson has a kind: "teach" (new content) or "practice" (the same subtopic as the teaching lesson just before it: exercises, oral work, drawing, matching, filling in blanks, ALL taken from the passages).
When the material is thin (common in lower primary), follow each teaching lesson with a practice lesson. Split big subtopics over several teaching lessons.
Never pad with content the passages do not have: if they cannot fill the term, return fewer lessons and list what is missing in gaps. Ledgerly fills the remaining weeks with revision.
You are composing the SCHOOL'S OWN scheme. The passages below (the official NCDC curriculum and guides, plus schemes of work, lesson plans, notes and past papers from the school e-library) are reference material:
The school's SCHEMES OF WORK for this class and term ("P 7 Primary Seven SCI Scheme OF Work Teacher AC", "P7 sci") are the BASE: follow the topics, subtopics and week-by-week order they agree on. Every topic they list for this term MUST become a unit, in their order, and their subtopics become the lessons, with about the pacing they give. Cite their passages in sourcePassageIds of every lesson that follows them.
The NCDC documents (titles starting "NCDC") only FILL GAPS: a topic NCDC lists for this term that the schemes lack gets its own unit where it fits best. Never drop or rename a schemes-of-work topic to fit NCDC. NCDC lower-primary thematic curricula list every learning area side by side in table columns separated by " | ": take only the Science column.
Combine them in this authority order: the school's schemes of work for topics, sequence and pacing; NCDC for anything they miss; the strongest detailed notes for accurate teaching depth; past papers for expected applications and activities.
Use this term's part of the material (Term 3) when the passages cover several terms.

NCDC topics for Primary Seven 2026, Term 3 that must ALSO be covered. Each needs at least one unit whose title or theme names it; the school's schemes of work decide where it goes and how many lessons it gets:
  8. Population and Health
Do NOT write lesson content yet. Each unit and lesson must cite the passage ids it comes from in sourcePassageIds.

Reply shape:
{"title":string,"summary":string,"units":[{"title":string,"theme":string|null,"weekFrom":int|null,"weekTo":int|null,"competences":string|null,"sourcePassageIds":[string],"lessons":[{"title":string,"subtopic":string|null,"kind":"teach"|"practice","objectives":[string],"sourcePassageIds":[string]}]}],"gaps":[string]}

<passages>
<passage id="lchk_82be9ea105124b37ada47051cc798ae0" source="NCDC PRIMARY SEVEN SET ONE – Integrated Science" part="2">
– | General outcomes instead of aims and objectives have been
provided for each topic.
– | The background for each topic has been given together with
other necessary guidance to the teacher.
– | Key words for each topic have been included in order to
enrich the learner’s vocabulary and mastery of concepts.

Primary Seven Curriculum

Methodology
During the teaching/learning process, you are expected to enhance
learning through the most effective learner-centred methods and
activities. You will be expected to facilitate learning as the learners do the
activities. Therefore you are expected to make thorough arrangements for
necessary instructional materials, learning activities and how they will
be carried out. The methods you choose to use should promote learner-
centred learning activities.

Ensure that the necessary learning materials are collected and availed to
learners in time for them to be used during the learning activities. Give
adequate guidance and allow learners to carry out the activities you have
prepared.

Guide and supervise all the learning activities. The active verbs used in
expressing the learning competences are all directed to the learner. As a
result of the teaching/learning processes, the learner should be able to
exhibit these competences.

Task analysis is another important approach. It involves breaking down
the available content or activity to be taught into simpler manageable
steps that can be accommodated easily at the pace of every individual
learner.

You should use the environment as much as possible to help the learners
relate science to real life situations and experiences. You are required to
let the learners carry out experiments, exhibitions, projects, field trips and
excursions. Encourage the learners to record and report on their findings.
Use methods that will provide the learner with the opportunity to explore
and acquire knowledge, concepts, skills, abilities, right attitudes, values
and competences.

Instructional Materials
You are expected to use a variety of books and charts available to help you
prepare the correct content on the topics. The specification of the suitable
learners’ textbooks, teachers’ guides, readers and charts on Science topics
have been provided in a separate (Implementation Guidelines). Refer to it
for more guidance. The existing materials based on the old curriculum,

National Curriculum Development Centre

are still useful and cover the required Science content. However, new
textbooks which cover language competences should be used as well.
Your classroom should possess different attractive incidental reading
materials in form of pictures, word cards, educational charts, models and
equipment improvised from locally available materials. These should be
of low or no cost and learner friendly. They should be able to boost the
teaching/learning process.

Assessment Guidelines
Continuous Assessment is recommended and should be based on the
summarised competences found at the end of each topic in the syllabus.
Assessment should be included as part of each lesson activity and should
be part of every lesson plan. When you teach, you are teaching a class of
individual learners. In order to help them learn, you need to know their
weaknesses and strengths on a continuous basis. This will help you to
structure any follow-up strategies.

One of the principles of the Revised Primary Curriculum is its emphasis
on developing competences. The P7 Curriculum covers both subject
</passage>

<passage id="lchk_da019de53f0e488d81add591eec37554" source="NCDC PRIMARY SEVEN SET ONE – Integrated Science" part="3">
and language competences. The Curriculum aims at mastering various
skills with understanding rather than memorising content. While all
curricula include specific skills, the revised Primary Curriculum is built
on measurable competences, for example, the learner:
1. | names different bones and muscles of the human arm.
2. | describes different joints found in the human body.
Like in P4, P5 and P6, assessment guidelines are provided to assist the
teacher carry out, manage and keep records on each individual learner
on class progress and on end of term performance. You are therefore
encouraged to record the innovative products of the learner that may not
have been planned but indicate how the learner is progressing.

Besides continuous assessment, there shall be end of term and end of year
assessment carried out. However, you will be required to distribute your
continuous assessment activities each term as follows:

Primary Seven Curriculum

Assessment Areas | Suggested No. of Assessment Activities
and Weighting
No. of Activities | Weighted
Class Exercise | 10 | 12%
Class Tests | 4 | 8%
Projects | 1 | 8%
Experiments | 2 | 6%
Oral (tests) Exercise | 4 | 6%
Subtotal | 40%
End of Term | 1 | 60%
Grand Total | 100%

End of primary cycle written examinations (Primary Leaving
Examinations) will be based on this syllabus and Integrated Science
content covered right from Thematic Curriculum through to P7. End of
cycle paper at P7 will be called Primary Integrated Science. It will consist
of section A of 40 short answer questions and section B of 15 structured
questions. Section A will carry 40% marks while section B 60%. Primary
Integrated Science will be marked out of 100%.

General Learning Outcomes
When the learners go through this syllabus, they will be able to:
• survey, identify and distinguish the attributes of plants, animals,
other objects and conditions in the environment.
• use characteristics to compare and classify animals, plants and
other objects in the environment.
• identify the features and describe the functions of different
parts of the human body.
• take care of the different parts of their bodies and practice good
health habits.
• keep safe and avoid accidents.
• understand the conditions for proper growth of living things.
• apply correct scientific processes in investigations of various
phenomena.

National Curriculum Development Centre

• show knowledge of and take care of the environment for its
sustainable use.
Competences
The learner is able to:
• survey, identify and distinguish the attributes of plants, animals,
other objects and conditions in the environment by making trips
and excursions to observe, collect, group things, make records,
interpret results and make reports.
• use characteristics to compare and classify animals, plants and
other objects in the environment by making trips and excursions
to:
– collect specimens of plants and animals
– observe plants and animals grow
– group/classify plants and animals (kingdoms)
– compare plants and animals
– record
– report
– care for plants and animals
• identify the characteristics and functions of different parts of
the human body by:
– | identifying and naming the different parts of the human
body
– | describing functions of each part
– | relating the different parts of the body to human activities

• take care of the different parts of the human body and practice
good health habits by:
– | identifying the different parts of the body
</passage>

<passage id="lchk_367b42becba24b9f82fd4cafbb002690" source="NCDC PRIMARY SEVEN SET ONE – Integrated Science" part="16">
• Emphasise ways of avoiding sexual deviation and activities
that address health concerns.
• Ensure that learners do not get exposed to what is beyond their
age.
• You will need to work with your learners on population survey,
population problem identification and planning course of
action.
• Encourage learners to carry out projects which include gathering,
organising, interpreting and sharing data about population and
health concerns in the community.
• Help learners to evaluate activities of health clubs as they
conclude their primary school cycle.

National Curriculum Development Centre

Suggested Competences for Assessment
The learner:
• names types of sicknesses in a home and community.
• lists forms of anti-social behaviour and sexual deviations.
• collects information and data on human population and health
in homes and the community.
• carries out population surveys and identifies community health
problems.
• plans and carries out population-related health activities.
• prepares a simple report on a survey on health activities.

Primary Seven Curriculum

Word List
These words are considered important vocabulary in the P7 Integrated
Science Syllabus. Ensure that your learners understand, can spell and use
them in correct sentences.
Term I
Topic 1: Muscular – | Topic 2: Electricity | Topic 3: Energy
Skeletal System | and Magnetism | Resources in the
Environment
• Skeleton | • Electricity | • Resource
• Hinge joint | • Fuse | • Hydro
• Ball and socket | • Circuit | • Tidal
• Pivot joint | • Switch | • Fossil
• Gliding joint | • Insulator | • Coal
• Voluntary muscle | • Magnet | • Petroleum
• Involuntary muscle | • Dynamo | • Bio gas
• Posture | • Electro-magnet | • Bio fuel
• Device | • Wood fuel
Topic 4: Simple | Topic 5: Excretory | Topic 6: Light Energy
Machines and Friction | System
• Beams
• Friction | • Translucent
• Excretion
• Force | • Opaque
• Ureter
• Nuisance | • Shadows
• Urinary system
• Moments | • Eclipse
• Wastes
• Mechanical | • Solar
advantage | • Lunar
• Wedges | • Optical
• Inclined | • Periscope
• Plane | • Spectrum
• Screws | • Prism
• Axles
Topic 7: | Topic 8: Population
Interdependence | and Health
of Things in the
Environment | • Community
• Demography
• Dependence
• Survey
• Agro-forestry
• Data
• Pollarding
• Sex deviations
• Lopping
• Anti social
• Coppicing
behaviours
• Welfare
• Rearing
• Interdependence
• Caring | 94
</passage>

<passage id="lchk_60cf526c26874d9a832da5e945a9b04b" source="KESK SCIENCE P.7 1" part="1">
[DOCUMENT TITLE]
[Document subtitle]
Bridged Curriculum Notes For P.7 Integrated Science 2022
A product of Kolfram Educational Services Kampala 0777886622
For Quality assessment & learning materials, always trust KESK products 1
TABLE OF CONTENTS
TERM I
Topic 1: Sanitation …………………………………………….…
Topic 2: Accidents and First Aids ……………………….….…
Accidents
First aid
Topic 3: Science at home and our community …… . …….…
Topic 4: Muscular and Skeletal System …………………..…
Skeletal system…………………………………………
Muscular system: ……………………..………………
Topic 5: Respiratory system ………..………………… . ...……
Topic 6: Reproductive System ……………………………..……
TERM II
Topic 7: The Excretory System ……………………….…..……
Topic 8: Light Energy ……………………………………….……
Topic 9: Electricity and Magnetism ………………………...…
Electricity
Magnetism
Topic 10: Simple Machines and Friction:.. …………….……
Simple Machines : …………………………………….
Friction : …………………………………………………
Topic 11: Interdependence of things in the Environment……
TERM III
Topic 12: Resources In the Environment ……………………
Topic 13: Population and Health ………………………………
2
6
13
19
19
19
37
37
53
58
82
103
117
125
132
TOPIC PAGES
Bridged Curriculum Notes For P.7 Integrated Science 2022
A product of Kolfram Educational Services Kampala 0777886622
For Quality assessment & learning materials, always trust KESK products 2
THEME : HUMAN HEALTH
TOPIC 1 : SANITATION
1) Sanitation : is the general cleanliness of an area.
2) Sanitation are the steps taken to promote public cleanliness involving
community effort to disease prevention.
3) Sanitation is the general cleanliness of the environment.
Elements of sanitation
1. Provision of good housing
2. Proper disposal of human wastes
3. Supply and use of safe water
4. Vector control
5. Safe guarding of food
6. Prevention of pollution of air and water.
Ways of keeping the environment clean.
1. Draining away all stagnant water to deny mosquitoes breeding grounds.
2. Digging rubbish pits and provision of dustbins for proper disposal of rubbish.
3. Having a latrine or toilet for proper disposal of faeces and urine.
4. Spraying vectors with insecticides.
Reasons for practising good sanitation
1. Good sanitation prevents spread of diseases.
2. It prevents accidents like cuts from broken bottles.
3. It prevents water and air pollution.
4. Good sanitation prevents food contamination.
Latrines
A latrine is a place for urination and defecation.
Types of latrines;
1. Ordinary pit latrines
2. VIP latrines
3. Toilets
4. Potties
Characteristics of pit latrines;
1. They are deep to hold faeces of the users for so many years.
2. They have strong floors to stand on and smooth enough to sweep and clean .
3. They have enough hole to allow in faeces and urine but small enough to
prevent children from falling in.
4. They have a lid to cover the hole completely and keep houseflies out of it.
5. They have walls and doors for privacy.
6. They have a roof which protects people from rain and sunshine.
Bridged Curriculum Notes For P.7 Integrated Science 2022
A product of Kolfram Educational Services Kampala 0777886622
For Quality assessment & learning materials, always trust KESK products 3
Structures of VIP latrines.
Differences between a VIP latrine and an ordinary pit latrine;
1. A VIP latrine has a vent pipe where as an ordinary pit latrine doesn’t have a
vent pipe.
2. A VIP latrine doesn’t have a lid where as an ordinary pit latrine has a lid.
3. A VIP latrine has a screen whereas an ordinary pit latrine doesn’t have a
screen.
</passage>

<passage id="lchk_07493ecf76284952ac25980ea5d5e3cb" source="P 7 Primary Seven SCI Scheme OF Work Teacher AC" part="1">
Page 1
PRIMARY SEVEN SCHEME OF WORK FOR SCIENCE I
WK PD THEME TOPIC/ SUB
TOPIC
SUBJECT COMPETENCES LANGUAGE
COMPETENCES
CONTENT SUGGESTED
ACTIVITIES
T/L AIDS REF
1
&
2
Human
Body
Muscular
skeletal
system.
The
structure of
human
skeleton.
The learner,
 Draws and names the parts.
 Defines the skeleton
 Explains types and importance
of the skeleton.
The learner,
 Writes words
connected to the
skeleton.
 Names different
parts of the
skeleton.
- The structure of
the human
skeleton.
- Types of
skeletons.
- Importance of
skeleton.
- Drawing and naming
the parts of the
skeleton.
Chart
Chalk board
Illustration
Text bks.
-do-
3 Names of
different
bones.
The learner,
 Names the different bones in the
body.
The learner,
 Spells he names of
different bones in
the body.
- The Names of
different bones.
- Long bones
- Short bones
- Irregular
bones
- Flat bones
- Examples of;
- Long bones
- Short bones
- Irregular
bones
- Flat bones
- Naming the bones
- Spelling the words.
Chart
Chalk board
Illustration
Text bks.
-do-
4 Human
Body
Joints The learner,
 Lists types of joints.
 Gives examples of each type of
joints.
 Describes uses of joints.
The learner,
 Writes down the
name of joints.
- What are joints
- Types of joints.
- Examples of
each type of
joints.
- Importance of
joints.
- Naming the joints
found in the body.
Chart
Chalk board
Illustration
Text bks.
Mk
integrated
Science Bk.7
Comprehens
ion Science
BK 7
Fountain
integrated
Sci. BK 7
5 Muscles The learner,
 Tells what muscles are.
 States the type of muscles.
The learner,
 Describes how
muscles work.
- The meaning of
muscles.
- Type of
- Defining the term
muscles.
- Stating the type of
Chalk board.
Illustration.
Page 2
Human
Body
Mentions the importance of muscles. muscles.
- Examples of
each type.
- Importance of
muscles.
muscles.
- Outlining importance
of muscles.
-do-
6
&
7
Diseases
and
disorders of
the skeletal
system.
Prevention
of muscular
and skeletal
diseases.
The learner,
 Identifies the disorders and
diseases of the system.
 Explains the preventive
measures of the above diseases.
The learner,
 Spells the words
related to system.
 Outlines the ways of
preventing the
diseases of the
system.
- Diseases and
disorders of the
system.
- Prevention of
Muscular and
skeletal
system.
- Outlining of the
diseases and
disorders.
- Discussing of the
preventive measures.
-do- -do-
8
&
9
Posture and
it’s
importance.
How to keep
the skeletal
system
healthy.
The learner,
 Defines the posture.
 Illustrates and demonstrates the
correct body posture.
 Describes good health habits for
the system.
The learner,
 Writes guided notes
on good health
habits.
- The meaning of
body posture.
- Good and bad
body posture.
- Importance of
good body
posture.
- How to keep
the healthy
skeletal
system.
- Writing guided notes
on good health
habits.
Chalk board
Illustration
Chart
Text bks
-do-
1
&
2
ELECTRICITY
(Types of
electricity)
 The learner
i) defines electricity
ii) identifies sources and types of
electricity
iii)experiments with static
electricity
 The learner:
i) Reads words and
sentences on
electricity
ii) Write words,
sentences and short
stories about
electricity
i) What electricity
is.
ii)Types of
electricity
- Current
electricity
- Static
electricity
iii) Forms of
electricity
- - Generating static
electricity
Dry cells, combs,
torches Mk
intergrated
science bk
7
Page 3
3
&
4
MATTER
AND
ENERGY
Sources of
electricity
The learners:
i) Identifies sources of electricity
</passage>

<passage id="lchk_bd3163da19c2416499fc60d2377fac21" source="P7 sci" part="1">
Contact: 0754895241/0783298434
Email: tekule@tekartlearning.com
Website: www.tekartlearning.com
1
Primary Seven Science Scheme of Work
WK
PD
THEME
/
TOPIC
SUBTOPIC
/
CONTENT
SUBJECT
COMPETENCES
LANGUAGE
COMPETENCES
METHOD
S
ACTIVI
TY
SKILLS VALUE
S
INS
T.M
AT.
REF R
M
1 1 to 3 Orientation.
Going through holiday work.
4
HUMAN BODY
Muscular-Skeletal system
Description
of muscular
skeletal
system.
Types of
skeleton
Structure of
skeletal
system and
its parts.
-the learner names
different bones and
muscles of the
human body
-Draws and labels
the skeleton and
voluntary muscles
-the learner reads
words, sentences
muscles and joints
of the body.
-Write guided notes
on the system.
- Names the
different bones and
muscles of the
human skeleton.
Discussio
n
Demonstr
ation.
Observati
on
Discovery
method.
Making
observat
ions.
Naming
different
bones
Drawing
Labeling
Critical
thinking
Decision
making
Logic
Taking
decision
Respons
ibility
Hum
an
skele
ton
Intro
ducti
on to
Biolo
gy pg
119
5 Classificatio
n of bones.
Classificatio
n and types
of Joints.
-Identifies
different classes of
bones in the
human body.
-Describes
different joints in
the body.
-Explain the work
of ligaments and
tendons.
-Reads words,
sentences and stories
about muscles and
joints of the body.
-Write guided notes
on the system.
Discussio
n
Demonstr
ation.
Observati
on
Discovery
method.
Making
observat
ion
Naming
different
bones
Drawing
Labeling
.
Problem
solving.
Critical
thinking
Decision
making
Logic
Taking
decision
Making
right
choices.
Confide
nce
A
well
draw
n
chart
Hum
an
skele
ton
Intro
ducti
on to
Biolo
gy pg
120 -
122
Contact: 0754895241/0783298434
Email: tekule@tekartlearning.com
Website: www.tekartlearning.com
2
2 1 Muscles
Types of
muscles
Functions of
muscular
skeletal
system.
Diseases
and
disorders of
the system
-Names different
muscles of the
human body
-Discusses
functions of the
muscular skeletal
system.
-States diseases
and disorders of
the bones, muscles
and the system.
-Recites a poem on
diseases and
disorders of muscles
and bones.
-Write guided notes
on the system.
-Draws and labels
the structure of the
skeletal system and
voluntary muscles.
Discussio
n
Demonstr
ation.
Observati
on
Discovery
method.
Drawing
Labeling
Reading
stories.
Describi
ng
diseases
and
disorder
s
Creative
thinking
Decision
making
Effectiv
e
commun
ication
Logic
Taking
decision
Making
right
choices.
Confide
nce
Respons
ibility
A
well
draw
n
chart
Intro
ducti
on to
Biolo
gy pg
123
2 Prevention
of diseases
and
disorders of
the system.
Health
habits that
keep the
system in a
healthy
working
condition.
Posture.
Importance
of correct
posture.
Dangers of
poor
posture.
-States diseases
and disorders of
the skeletal
system.
-Explain ways of
caring for the
muscular-skeletal
system.
-Describes the
importance of
good posture
-Reads words,
sentences and stories
about muscles and
joints of the body.
-Recites a poem on
diseases and
disorders of muscles
and bones.
-Write guided notes
on the system.
Discussio
n
Demonstr
ation.
Observati
on
Discovery
method.
Making
observat
ion
Naming
different
bones
Drawing
Labeling
Problem
solving.
Creative
thinking
Decision
making
Effectiv
e
commun
ication
Logic
Taking
decision
Making
right
choices.
Confide
nce
A
well
draw
n
chart
Mk
book
four.
Contact: 0754895241/0783298434
Email: tekule@tekartlearning.com
Website: www.tekartlearning.com
3
3
MATTER AND ENERGY
Electricity and Magnetism
Electricity
Sources of
electricity
Cells
Structure of
a dry cell.
Parts of a
</passage>

<passage id="lchk_a01e36dd448d47d79f90c135700c0116" source="100 Report Card Comments Teachers CAN USE While Writing Report Cards OF Students Or Pupils 1 1" part="1">
100 REPORT CARD COMMENTS TEACHERS CAN USE WHILE WRITING REPORT
CARDS OF STUDENTS/PUPILS
1. I have truly enjoyed being __________'s teacher and will miss him/her next
year.
2. _______ is making good/excellent/outstanding progress in _______ grade.
3. _______ has done a(n)/fantastic/exemplary/wonderful job this year in ______
grade and has worked so very hard.
4. I appreciate ____________'s quality work/motivation to do well/attitude and
have enjoyed being his/her teacher.
5. _______ is intelligent but works below his/her capacity/potential due to a lack
of motivation/attention to quality work.
6. _______ succeeds at whatever task he/she puts his/her mind to.
7. I am so proud of ________ and wish him/her well for _______ grade and
beyond.
8. _______ has worked very hard this year and I am proud of all of his/her
accomplishments.
9. _______ has strengthened his/her skills in _________.
10. _______ is respectful to his/her classmates and is very well-liked.
11. I am concerned about _________'s organizational skills and his/her
responsibility related to turning in assignments on time.
12. _______ sets high standards for himself/herself and reaches them.
13. _______ is helpful and kind and is a pleasure to be around.
14. _______ has done well in many areas but I am concerned that his/her lack of
listening/focus/motivation and following directions/working
independently/working quietly has contributed to his lower grade in
______________.
15. ________ has made good/excellent/outstanding progress in all academic
areas.
16. ________ is bright, motivated, and hard working and can be proud of his/her
accomplishments this year.
17. Unfortunately, _________'s grades have suffered from missing assignments.
18. ________ is gaining confidence in _____________ but would benefit from
__________________.
19.________ follows classroom rules consistently and is a good role model.
20. Please encourage ________ to ______________ each day to help him/her
improve in _____________.
21. ________ has a positive attitude and is a joy to teach.
22. ________ seems to find __________ challenging and would benefit from
reading nightly/practicing math facts/working online...
23. ________ is a(n) awesome/wonderful/fabulous ________ grader and I have
enjoyed getting to know him/her this year.
24. ________ is capable of achieving a higher grade in ________ but needs to
______________ in order to make progress.
25. ________ excels in creative/narrative/opinion writing.
26. ________ produces stories/essays/paragraphs that are well-organized/well
developed.
27. ________ has strong reading comprehension skills.
28. ________ seems to have difficulty at times with reading comprehension and
would benefit from __________.
29. ________ has made great improvement in the area of ______________.
30. ________ works well with other students.
31. ________ not only works well with his/her classmates, but is a natural leader.
32. ________ is intrinsically motivated and strives to please.
33. ________ is doing an excellent/outstanding/wonderful/fantastic/great job
overall this year.
34. ________ enjoys participating in class lessons and his/her background
knowledge adds a great deal to our discussions.
35. ________ is very compassionate and is always kind to others.
36. ________ is a creative student and I have enjoyed seeing the wonderful
writing/art projects/drawings he/she has created/written.
37. ________ is on task regardless of the activity.
</passage>

<passage id="lchk_e32ed6adc8eb4ff29a62ceae42e7d5eb" source="Basic 7 Integrated Science" part="1">
1
Table of contents
STRAND 1: DIVERSITY OF MATTER
Sub-strand 1: Materials................................................................3
Sub-Strand 2: Living Cells...........................................................12
STRAND 2: CYCLE .....................................................................22
Sub-strand 1: Earth Science........................................................22
Sub-strand 2: Life Cycle of life Organisms...................................24
Sub-Strand 3: Crop Production...................................................29
Sub-strand 4: Animal Production................................................33
STRAND 3: SYSTEMS............................................................. 36
Sub-strand 1: The Human Body System......................................36
Sub-strand 2: Solar System.........................................................44
Sub-strand 3: Ecosystem.............................................................46
Sub-strand 4: Farming System....................................................56
STRAND 4: FORCES AND ENERGY......................................... 61
Sub-strand 1: Energy..................................................................61
Sub-Strand 2: Electricity and Electronics....................................79
Sub-strand 3: Conversion and Conservation of Energy................81
Sub-strand 4: Force and Motion..................................................85
Sub-strand 5: Agricultural Tools..................................................98
STRAND 5: HUMAN AND THE ENVIRONMENT ........................103
Sub-strand 1: Waste Management.............................................103
Sub-strand 2: Human health....................................................108
Sub-strand 3: Science and Industry..........................................116
2
STRAND 1: DIVERSITY OF MATTER
Sub-strand 1: Materials
Content Standard: B7.1.1.1:
Recognise materials as important resources for providing human
needs.
Indicator B7.1.1.1.1:
Classify materials into liquids, solids and gas
Materials
There are many materials around us and they come in different
shapes, colours texture and sizes. A material is a substance or
mixture of substances that constitute an object. A substance is
anything that can be seen, touched or measured. Examples of
materials; water, wood, oxygen, milk, table, chair, sand, alcohol,
soft drink, pito, lemon juice, cooking oil, soap, computer, ‘sobolo’,
water vapour, palm wine, vinegar, carbon dioxide, diesel, Dettol,
petrol, kerosene, gravel, etc. Materials can be classified based on
their state (solid, liquid and gas).
Classification of materials Into Solids, Liquids And Liquids.
The above listed materials have been classified or grouped into
solids, liquids and gases
SOLIDS LIQUIDS GASES
Wood
Table
Chair
Soap
Sand
Computer
Gravel
Water
Milk
Soft drink
Palm wine
‘Sobolo’
Lemon juice
Cooking oil
“Pito”
Vinegar
Dettol
Kerosene
Petrol, alcohol,
diesel
Water vapour
Oxygen
Carbon dioxide
Difference between solids, liquids and gases
SOLIDS 1.Have a definite shape
2.Can be held in the hand
3.Solids do not flow
3
4.They have fixed shape.
5.They have fixed volume
6.They are difficult to compress.
7.Particles in solids are closely packed
LIQUIDS 1.They do not have fixed shape. They
take the shape of a container.
2.Liquids flow
3.They have definite volume
4.They cannot be compressed
5.Particles in liquids are quite closely
packed.
GASES 1.Gases flow
</passage>

<passage id="lchk_9322ac454ffd4295a353ca3259c1854c" source="P 7 Primary Seven SCI Notes Teacher AC" part="34">
11. Name the lens used to correct:
a) Shortsightedness.
b) Long sightedness.
12. Define the term “dispersion of light.”
13. Which part of the eye has a similar function as the film in a photographic camera?
14. Name the eye disease caused by bacteria.
15. Identify one health practice one can perform to promote good health of the eyes.
16. What type of mirrors are sued in a periscope?
17. State the type of surface which causes regular reflection.
18. What type of natural shadow is formed when the moon comes between the sun and the Earth?
19. Name the part of the eye that controls the amount of light entering it.
20. In which way are the vitreous and aqueous humours important to the eye?
LIGHT ENERGY - ANSWERS
1. The sun / stars / Firefly / Glow worms / Erupting volcanoes.
2. A luminous object is one which produces / gives out its own light while a non- luminous object is one that doesn’t
produce its own light.
3. a) Opaque objects.
b) Translucent objects.
4. Formed when the moon comes between the sun and the earth.
5. Converging beam.
6. A shadow is formed when light rays are obstructed by an opaque object.
7. Reflection is bouncing back of light rays while refraction is the bending of light rays when they move from one
medium to another of different densities
8.  i 0 =  r
Since  i 0 = 68 0 .
  i 0 =  y = 68 0 .
  r = 68 0 .
9. - Angle of incidence is equal to angle of reflection.
- The normal, incident ray and reflected ray at the point of incidence all lie on the same plane.
10. Images in the camera are real those in place mirror are virtual.
</passage>

<passage id="lchk_22fade59c6a14fccbe39812009dc7238" source="P.7 MID 3 SCI" part="1">
Tel: 0758299602 1
`
SUCCESS INTEGRATED PRIMARY SCHOOL
PRIMARY SEVEN PRE-PLE EXAMINATION, 2022
MID TERM 3
Integrated Science
Time allowed: 2 hours and 15 minutes
NAME: ______________________________________________________________________
Signature: _________________________
EXAMINER’S USE ONLY
District ________________________
Date: ________________________
Read the following instructions carefully:
1. The paper is made up of section A and B.
2. Section A has 40 short answer questions (40 marks).
3. Section B has 15 questions (60 answers).
4. Answer ALL questions. All answers to both section A and B must be written
in the spaces provided.
5. All answers must be written in blue ink.
6. Any handwriting that cannot easily be read will lead to loss of marks.
7. Unnecessary alteration of work may lead to loss of marks.
8. Do not write anything in the box indicated examiner’s use only.
PARENT’S COMMENT SIGNATURE
A
B
TOTAL
Tel: 0758299602 2
SECTION A
1. Why do people wash their hands before eating food?
…………………………………………………………………………………
2. A part from protection of delicate body organs, give one other importance of
the human skeleton.
…………………………………………………………………………………
3. In which one way can metallic objects be prevented from rusting?
…………………………………………………………………………………
The diagram below shows a simple machine. Use it to answer questions 4 and 5 .
4. Using an arrow show the position of the fulcrum.
5. To which class of lever does the machine above belong?
…………………………………………………………………………………
6. By what process does ice change to water?
…………………………………………………………………………………
7. If the mass of an object is 45g and its volume is 5cc. find its density.
…………………………………………………………………………………
8. Mention the vector which spreads germs that cause trachoma.
…………………………………………………………………………………
9. Give a reason why coal is called a non renewable resource.
…………………………………………………………………………………
10. Which disorder of the digestive system can be prevented by eating food rich
in roughages?
…………………………………………………………………………………
Tel: 0758299602 3
11. Write down one difference between a cock a hen.
…………………………………………………………………………………
12. Give one advantage of breast feeding to a mother.
…………………………………………………………………………………
13. To which group of crops do groundnuts, bean and soya belong?
…………………………………………………………………………………
14. Name the type of lens shown below.
……………………………………………
15. Mention any one mineral salt lost during diarrhoea?
…………………………………………………………………………………
16. A part from hunting, state one other importance of a dog to man.
…………………………………………………………………………………
17. What makes milk left on the table for some days go bad?
…………………………………………………………………………………
18. Give one reason why a cow is regarded as a ruminant.
…………………………………………………………………………………
19. Identify one example of a biological change in the environment.
…………………………………………………………………………………
20. Mention one cause of a short circuit.
…………………………………………………………………………………
21. Which type of cattle has the body shape shown below?
…………………………………………………………………………………
Tel: 0758299602 4
22. Name one common poultry vice.
…………………………………………………………………………………
23. State any one use of fungi to man.
…………………………………………………………………………………
24. Name the second stage in the life cycle of a cockroach.
…………………………………………………………………………………
25. Which general name is given to material that does not allow heat or electricity
to pass through them?
…………………………………………………………………………………
26. Give a reason why a nursery bed should have a shade.
…………………………………………………………………………………
</passage>
</passages>

Your previous outline was rejected because it does not follow the school's schemes of work and the required topics for this term:
- only 14 of 48 teaching lessons cite the school's schemes of work; they must follow the schemes' topics, subtopics and order (cite their passages)
Redo the WHOLE outline from the school's schemes of work (their topics, subtopics and order, citing their passages), adding any missing NCDC topic.

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
