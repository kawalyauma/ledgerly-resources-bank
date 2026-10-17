# Job ltsk_b7eda6aee7c049bca6ba5b8a16c54623-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for Science, Primary Five 2026, Term 3.
The term has 10 teaching weeks and this subject has 6 periods per week. Every lesson is ONE 40-minute period, so keep each lesson small enough to teach in 40 minutes.
There are no weekly review lessons: the subject has a lot of content, so every period teaches or practises.
Give at most 59 teaching/practice lesson entries in teaching order (the last lesson of the term is the end of term assessment).
Each lesson has a kind: "teach" (new content) or "practice" (the same subtopic as the teaching lesson just before it: exercises, oral work, drawing, matching, filling in blanks, ALL taken from the passages).
When the material is thin (common in lower primary), follow each teaching lesson with a practice lesson. Split big subtopics over several teaching lessons.
Never pad with content the passages do not have: if they cannot fill the term, return fewer lessons and list what is missing in gaps. Ledgerly fills the remaining weeks with revision.
You are composing the SCHOOL'S OWN scheme. The passages below (the official NCDC curriculum and guides, plus schemes of work, lesson plans, notes and past papers from the school e-library) are reference material:
The school's SCHEMES OF WORK for this class and term ("P 5 Sci Scheme For Term Lll", "P 5 Science Scheme FOR Term 3 2023", "P 5 Science Scheme Term III", "P 5 Science Term 3", "Third Term P 5 Science Scheme OF Work") are the BASE: follow the topics, subtopics and week-by-week order they agree on. Every topic they list for this term MUST become a unit, in their order, and their subtopics become the lessons, with about the pacing they give. Cite their passages in sourcePassageIds of every lesson that follows them.
The NCDC documents (titles starting "NCDC") only FILL GAPS: a topic NCDC lists for this term that the schemes lack gets its own unit where it fits best. Never drop or rename a schemes-of-work topic to fit NCDC. NCDC lower-primary thematic curricula list every learning area side by side in table columns separated by " | ": take only the Science column.
Combine them in this authority order: the school's schemes of work for topics, sequence and pacing; NCDC for anything they miss; the strongest detailed notes for accurate teaching depth; past papers for expected applications and activities.
Use this term's part of the material (Term 3) when the passages cover several terms.

NCDC topics for Primary Five 2026, Term 3 that must ALSO be covered. Each needs at least one unit whose title or theme names it; the school's schemes of work decide where it goes and how many lessons it gets:
  5. MANAGING CHANGES IN THE ENVIRONMENT
Do NOT write lesson content yet. Each unit and lesson must cite the passage ids it comes from in sourcePassageIds.

Reply shape:
{"title":string,"summary":string,"units":[{"title":string,"theme":string|null,"weekFrom":int|null,"weekTo":int|null,"competences":string|null,"sourcePassageIds":[string],"lessons":[{"title":string,"subtopic":string|null,"kind":"teach"|"practice","objectives":[string],"sourcePassageIds":[string]}]}],"gaps":[string]}

<passages>
<passage id="lchk_5295365097a74b86890d08a1084308f5" source="NCDC P5 Curriculum – Integrated Science" part="1">
Integrated Science

P5 Set One Syllabus, National Curriculum Development Centre | 25

Background
This is Primary Five Science Syllabus. In Primary 1-3 learning is based on themes, learning outcomes and competences. Most of the
Science related competences are covered under the literacy strands of the Thematic Curriculum. In Primary Four learning was based on
subjects and the Science Syllabus outlined learning outcomes, content and language competences.

Learners in Primary Five are expected to have developed sufficient basic literacy skills both in local and English language. The teacher
can now use English only as a medium of instruction. The teacher is required to check from time to time if learners understand the
concepts correctly and are able to consolidate what was acquired in earlier classes.

The instructional process will follow what was in the old syllabus and teachers will be required to use the old instructional materials.

Rationale
This revised Primary Five (P5) Science syllabus has been designed to consolidate the basic literacy and numeracy skills acquired during
the Thematic Curriculum and the transition year. It is also intended to provide the learner with knowledge on basic science, health,
agriculture and environmental knowledge, skills, attitudes, practice and values important to prepare learners for upper classes.

The main changes which have been made in this Primary Five syllabus are:
- Topic overflows from P4 e.g. the Digestive Systems and measurements have been included. Topics like Primary Health Care, part of
Digestive System from has been simplified and is presented for P5. These are shown in the matrix below on topic shifts.
- Contents in some topics have been reduced in order to keep the learning experience light and simple. The more complex content
has been shifted to upper classes while others have been redesigned to suit P5 learners’ level.
- The scope and sequencing of content has been based on progression of outcomes and competences.
- Literacy skills and Language competences have been included in each topic to clarify concepts.
- Possible life skills which can be developed have been suggested in each topic.
- Subject competences and language competences have been included to replace objectives. These are arranged in order of
cognitive levels namely knowledge, comprehension and application.
- Language competences have been included especially to reinforce literacy skills and to help clarify concepts.
- General outcomes instead of aims and objectives have been provided for each topic.
- The background for each topic has been given together with other necessary guidance to the teacher on how to handle the topic.

26 | P5 Set One Syllabus, National Curriculum Development Centre

General Methodology
It is strongly suggested that the teacher uses those methods and activities which put the learner at the centre of the teaching/learning
process. The active verbs used in expressing the learning competences are all directed to the learner. This implies that as a result of
teaching/learning process, the learner should exhibit these competences.

The teacher of Integrated Science is expected to use a variety of books of the old curriculum. This will not enrich teachers content but will
help the teacher to prepare the correct contents on the topics. The teacher is expected to constantly help relate science to real life
</passage>

<passage id="lchk_8b4fcf781fc7493e8a198bca6fecf619" source="NCDC P5 Curriculum – Integrated Science" part="2">
situations and experiences. Not all schools in Uganda may have same learning environment. The teacher should feel free to use
examples which provide the learner with the opportunity to acquire the same knowledge, concepts, skills, values and competences.

The methods a teacher chooses to use should be those which contribute towards the achievement of competences, learning outcomes
and eventually lead to the achievements of aims and objectives of primary education. Such methods therefore, should cater for the spiral
nature of the science syllabus. At Primary Four the topics introduced and content covered should pave way for further study of the topics
in upper classes. Primary four class will be useful in preparing learners for effective participating in P5-7.

Assessment Guidelines
In principle continuous assessment is recommended and should be based on the summarized competences suggested in each topic. All
assessments of learning shall be based on the learning competences given in this syllabus. Besides the Continuous Assessment, there
shall be end of term and end of year assessment carried out and records kept.

General Learning Outcomes
When the learners go through this syllabus they will be able to:
• Survey, identify and distinguish the attributes of plants, animals, other objects and conditions in the environment.
• Use characteristics to compare and classify animals, plants and other objects in the environment.
• Identify the features and describe the functions of different parts of the human body.
• Take care of the different parts of their bodies and practice good health habits.
• Keep safe and avoid accidents.
• Understand the conditions for proper growth of living things.
• Apply correct scientific processes in investigations of various phenomena.
• Show knowledge of and take care of the environment for its sustainable use.

P5 Set One Syllabus, National Curriculum Development Centre | 27

P5 Integrated Science Topic Outline

Themes or Unit | Topic
1. The Environment | Components of the environment: The Soil

Immunization

Food and Nutrition
2. Human Health
Primary Health Care and Family Care

3. The World of Living Things | Bacterial and Fungi

4. The Human Body | The Digestive System

5. Matter and Energy | Measurement

Heat Energy

6. Managing changes in the Environment | Types of Change

7. Science in Human activities and occupation | Keeping goats, sheep and pigs

Occupation in our community: Crop growing

Keeping Poultry and Bees

Community Health and Social Problems among young
8. Community Population and Family Life | people

28 | P5 Set One Syllabus, National Curriculum Development Centre

TERM I
THEME: SCIENCE IN HUMAN ACTIVITIES AND OCCUPATIONS
Topic: Keeping Poultry and Bees
General Background
Keeping poultry and bees is a very important topic which helps learners to develop interest and basic skills for managing simple projects
like poultry and bee keeping for self-reliance. It is important to note that this topic will help learners to appreciate poultry and bee farming
as a business. This topic has been retained from the old syllabus.

Learning Outcome
- | The learner is able to know and use basic scientific knowledge and skills in the management of poultry and bees.
   |   |  |  
The learner:
• Identifies different types | • | Names the different | •  Types of poultry | • | Naming types of poultry.
</passage>

<passage id="lchk_3735f33eff604b31a70316822fad2742" source="NCDC P5 Curriculum – Integrated Science" part="15">
• | capacity | • | density (ies)

Immunization
• | immunity | • | hemophilia influenza
• | vaccine(s) | • | Hepatitis B
• | immunisable | • | whooping cough
• | symptoms | • | Tuberculosis
• | diphtheria | • | Tetanus
• | meningitis | • | Yellow fever

Digestive System
• | digestion | • | ulcers
• | aesophagus | • | intestinal obstruction
• | rectum | • | constipation
• | salivary glands | • | vomiting
• | pancreas | • | digestive system
• | disorder(s) | • | habit
• | efficiency | • | maintain(ing)

Components of the Environment: Soil
• | fertilizers | • | properties | • | loam | • | humus
• | artificial | • | harmful | • | clay | • | green manure
• | mulches | • | components | • | bacteria | • | organic manure
• | erosion | • | fungi | • | habitat
• | agent(s) | • | chemicals | • | mining
• | conservation | • | fertility | • | polythene
• | compost | • | manure | • | mineral

58 | P5 Set One Syllabus, National Curriculum Development Centre

Heat Energy
• | solutes | • | dissolving | • | potential energy
• | solvents | • | mixtures | • | exerts
• | characteristics | • | forms | • | pressure
• | transfer | • | kinetic energy | • | solid
• | expansion | • | gases | • | magnetism
• | evaporation | • | contraction | • | melting
• | sublimation | • | freezing | • | condensation
• | conduction | • | radiation | • | vacuum
• | Fahrenheit scale | • | convection | • | Celsius scale
• | conversion | • | clinical thermometer

Occupations in our Community: Crop Growing
• | tuber crops | • | rotting | • | rogging
• | tubers | • | spraying | • | storage
• | pests | • | crop rotation | • | potato blight
• | cassava mosaic

Bacteria and Fungi
• | organisms | • | harmless
• | agent(s) | • | fungal diseases
• | bacterial diseases

Types of Changes – Biological, Physical and Chemical Changes
• | biological | • | rusting | • | placement faults
• | chemical | • | fermentation
• | adolescents | • | respiration
• | melting | • | decaying
• | freezing

P5 Set One Syllabus, National Curriculum Development Centre | 59

Keeping Goats, Sheep and Pigs
• | parasite(s) | • | swine flue | • | flock

Food and Nutrition
• | proteins | • | minerals | • | convalescents
• | carbohydrates | • | vulnerable | • | nutrition
• | vitamins | • | weaning | • | balanced diet
• | staple food(s) | • | consumption

Primary Health Care (PHC)
• | elements | • | disposal
• | principles | • | suitable
• | hygiene | • | practices
• | excreta

60 | P5 Set One Syllabus, National Curriculum Development Centre
</passage>

<passage id="lchk_06c5496f4a7d4334b58fc6962665d823" source="P5 Curriculum" part="1">
THE REPUBLIC OF UGANDA
Ministry of Education and Sports
2010
National Curriculum Development Centre,
P.O. Box 7002,
Kampala - Uganda
Set One: English, Integrated Science, Local Language, Mathematics and
Religious Education (Christian Religious Education & Islamic Religious
Education) and Social Studies.
Primary 5 Curriculum
PRIMARY FIVE CURRICULUM
SET ONE
National Curriculum Development Centre
NATIONAL CURRICULUM DEVELOPMENT CENTRE (NCDC) UGANDA 2010
COPYRIGHT © NCDC, 2010.
BOX 7002, KYAMBOGO, KAMPALA
KAMPALA- UGANDA
URL. www.ncdc.go.ug
ALL rights reserved. No part of this syllabus should be reproduced stored in a retrieval system or transmitted in any form by any means elec-
tronic, mechanical, photocopying, recording or otherwise without the permission of the authors and publisher. No patent liability is assumed
with respect to the use of the information contained herein.
ISBN 978-9970-117-91-8
Published by:
National Curriculum Development Centre
iii
TABLE OF CONTENTS
ACKNOWLEDGEMENT ..............................................................................................................................................................................ix 
FOREWORD ................................................................................................................................................................................................ x 
1.0  Introduction ...........................................................................................................................................................................................xi 
2.0  The National Aims of Education ..........................................................................................................................................................xi 
3.0 Aims and Objectives of Primary Education in Uganda .....................................................................................................................xi 
4.0 Rationale ..............................................................................................................................................................................................xii 
5.0 Structure of the Curriculum ................................................................................................................................................................xii 
6.0 General Methodology .........................................................................................................................................................................xiv 
7.0 Assessment Guidelines ......................................................................................................................................................................xv
English ........................................................................................................................................................................................................ 1 
TERM I ......................................................................................................................................................................................................... 5 
TOPIC 1:  VEHICLE REPAIR AND MAINTENANCE 23 periods ............................................................................................................ 5 
</passage>

<passage id="lchk_67a879e38ffa4f29b1e8e08240cd5c0c" source="P 5 Sci Scheme For Term Lll" part="1">
For more schemes of work, visit www.uganda.madpath.com
PRIMARY FIVE
SCIENCE
SCHEME OF WORK
TERM III
For more schemes of work, visit www.uganda.madpath.com
WK PD THEME TOPIC S-TOPIC COMPETENCES CONTENT METHODS L/ SKILLS
& VALUE
T/AIDS L/
ACTIVITES
REF
LANGUAGE SUBJECT BIOLOGICAL CHANGES
1 1 Managing
Changes
in
The
Environm
ent
Types of
changes
Biologic
al
changes
The learner:
-Spells words like
growth, germination
-Write
SentencesAbout
biological changes.
Outlines the various
examples of
biological Changes.
The learners:
-Defines
biological
Changes
-Mentions the
Examples of
Biological
changes.
-States the
characteristics of
Biological changes
Give the
importance
and dangers of
biological
changes
These are changes that
take
Place in the life of living
Things.
Examples
-growth, germination
Characteristics of
Biological changes
- importance and dangers
of biological changes
- Good and bad effects
of biological changes
-
Demonstratio
n
-Guided
discovery
-Guided
discussion
-Self
awareness
- Critical
thinking
- Love
- Appreciati
on
-Chart showing
stages of
growth in
plants and
animals
-Observing
growth in
germinati
on and in
human
beings.
-discussing
effects of
some
biological
changes
like
transpirati
on
Compsci
bK 5.
Integrated sci
Pupils Bk. 5
-Mk int
Sc
pupils Bk.5.
1 2 Chemical
Changes.
The
Learner:
-Pronounce Words
LikeRotting,Rusting
Burning.
-Write poems
about
the effects of
rusting.
-Draws diagramsto
Showrusting.
The learners:
-defines the term
Chemical change.
-mentions the
Examples of
Chemical changes.
-States the
characteristics of
chemical
changes.
-Describes the
Experiment about
Rusting.
-Effects.
Chemical changes
A type of change
where new
Substances are
formed.
Examples of
Chemical changes.
Rusting , burning,
rotting.
Experimentat
ion
Demonstratio
n
Guided
discussion
observation
-Problem
Solving
logic
Match box,
water ,nails or
pins
Drawing
experiments
observing
burning of
papers
discussing
observed
results of
experime
nts
Comp
primary
science
bk. 5
-integrated
Primary
Science
Bk 5
-Mk
Integrated
Primary
Science
Bk. 5
For more schemes of work, visit www.uganda.madpath.com
3 Physical
Changes
The learners:
-Spells words like
condensation,
Evaporation, melting.
-Physical changes
In the environment.
The learner:
1. Defines physical
Changes
2.Mentions the
examples of
Physical changes.
3. States the
Characteristics
Of physical
Changes.
Physical change is a type
Change where no new
substance is formed.
Examples of physical
Changes
-Condensation , melting
Sublimation, freezing.
Evaporation
- characteristics of physical
change
- importance and dangers of
physical changes
- Good and bad effects of
physical changes
-Explanation
-demonstrate
Ion
-Guided-
discovery
-Problem
Solving
-Self
esteem
Kettle or sauce pan
stove, bottle
Bucket
Candle wax
-Collecting
Materials
-observing
Changes of
State.
-drawing a
Conclusion
About the
experiment
Comp
Pr
Scie
Bk 5
Supplementary
science bk8
Contemporary
science bk for
upper primary
.
1 4 Manag
ing
changes
in the
environ
ment
Types of
Changes
Natural
Changes
The learner:
-Spell s words like
Landslides, Earth
Quakes Floods
-Pronounces words
Like Earth quakes
The learners:
-defines natural
Changes.
-mentions the
Examples of
natural
Changes.
-State the effects
Natural changes
in
the environment.
-cites the control
of natural
changes
natural changes
-examples of natural changes
- effects of natural changes
in the environment
- control of natural changes
-Guided discussion
- Discovery
- Brain storming
</passage>

<passage id="lchk_96bc7ba6b902405fb41b3f97c50bbeeb" source="P 5 Science Scheme FOR Term 3 2023" part="1">
1
SCIENCE SCHEME OF WORK
FOR PRIMARY FIVE
TERM THREE 2023
THEME TOPIC
Managing changes in the environment Types of changes
Science in human activities and
occupation
Keeping Goats, Sheep and Pigs
Human health Food and nutrition
Human health Primary health Care (PHC)
WK PD THEME TOPIC SUB TOPIC COMPETENCES CONTENT METHOD/
TECHNIQUE
ACTIVITY LIFE
SKILLS/
VALUES
REF
LANGUAGE SUBJECT
1
2
Going through holiday work.
2 1
MANAGING CHANGES IN THE
ENVIRONMENT
TYPES OF CHANGES IN THE
ENVIRONMENT
Types of
changes
-Reads
words
-Spells
words
-Explains
how changes
take place
in the
environment
-Lists
examples of
changes in
the
environment
-Agents of change.
-Different
changes in the
environment.
• Biological
• Chemical
• Physical
-Group
discussion.
-Guided
discovery
Classifying
changes.
-Critical
thinking.
-
Creative
thinking.
Baroque
Int
Science
bk 5
pg148-9
St
Bernard
int sci bk
5 pg 160
2
&
3
Effects of
changes in
the
environment
• Read words
correctly.
• Writes
words
correctly.
• Describes
biological
changes.
• Lists down
example of
biological
changes.
• Biological
• Chemical
• Physical
• Group
discussion.
• Observation.
• Question and
answer.
• Describing
biological
changes.
• Listing
biological
changes
• Planting
seeds.
• Critical
thinking
• Problem
solving.
• Effectiv
e com.
• Fountain
integrate
d science
book 5
pg 43.
• Baroque
integrate
d science
pg 148-
150.
3
2
4 Managing
changes in
the
environment
-Reads the
words
correctly.
-Spells
words
correctly
Describes
ways of
managing
changes in
the
environment
• Managing
different
changes;
-Floods
-Drought
-Landslides
-Volcanic
eruptions
-Pollution
-Discussion
-
Brainstormin
g
-Excursions
-Observing
changes in
the
environment.
-Problem
soving.
-
Effectiv
e
communi
cation.
• Mk
integrate
d science
book 5
pg 60
5
SCIENCE IN HUMAN
ACTIVITIES
AND OCCUPATION
KEEPING GOATS, SHEEP
AND PIGS External
parts of a
goat.
• Reads
words
sentences
and stories
about
goats.
• Writes
sentences
• Describes
goats.
• Defines the
terms used
in goat
keeping.
• Gives the
uses of
• Reviewing rabbit
keeping
• Describe goats.
• Structure of a
goat
• Naming parts of a
goat.
• Giving uses of
• Class
discussion.
• Observation.
• Drawing a
goat.
• Naming
external
parts of a
goat.
• Care
• Confiden
ce
• Mk
integrate
d science
bk 5.
• Fountain
integrate
d science
bk 5
4
about
goats.
goats. goats. • Baroque
inte
science
book 5
pg 160-
161.
3 1 -Reads
words,
sentences
and stories
about
goats.
-Writes
sentences
about goat
keeping.
- Describes
local breeds
of goats.
• Describes
exotic
breeds of
goats.
• Examples of
exotic
breeds of
goats.
• Describe a
breed.
• Examples of local
and e of goats
• Types of goats.
-Meat goats
-dairy goats
-Dual
purpose
goats.
Discussion
• Listing
products
from goats.
• Giving
examples of
breeds of
goats.
• Audibilit
y
• Confiden
ce.
• Self-
expressi
on.
• Apprecia
te.
• Integrat
ed
science
Bk 5.
• Fountain
integrate
d science
k5
• Baroque
int.
science
book 5
page 161-
162.
5
7
&
8
Advantages
of keeping
local breeds
of goats.
• Write
words,
sentences
and stories
about
breeds of
goats.
• Gives
advantages
of keeping
local breeds
of goats.
• Gives
disadvantag
es of
keeping
local breeds
of goats.
• Give
disadvantag
es of
keeping
exotic
breeds of
goats.
• Advantages of
keeping local
breeds of goats.
• Disadvantages of
keeping local
breeds of goats.
• Disadvantages of
keeping exotic
breeds of goats.
• Advantages of
keeping local over
exotic and vise-
versa.
• Explanation.
• Observation.
• Observing
different
</passage>

<passage id="lchk_3a383fbc96074ae394f9b05f836cf4e7" source="P 5 Creative Printers Science ALL Year" part="31">
2. Useful bacteria help in making cheese butter and yoghurt by fermenting milk.
3. Useful bacteria help in digestion of food in ruminants.
4. They are used to break down volumes of garbage and faeces in latrines, septic
tanks and sewage systems.
Useful/harmless bacteria to soil
1. Bacteria help in the decaying and rotting of organic matter
2. Nitrogen fixing bacteria found in root nodules of legumes trap nitrogen from the air
and change it to nitrates.
Note: That is why it is not good to pour dangerous chemicals like paraffin
and insecticides in latrines.
Similarities between bacteria and fungi
a. They both cause diseases.
b. They both have two ways of feeding that is parasitically or saprophytically.
c. They are both living organisms.
Differences between bacteria and fungi
1. Most fungi reproduce by means of spores while bacteria reproduce by means of
binary fission. (cell division)
2. Bacteria are single celled while most fungi are multicellular
90
P.5 SCIENCE LESSON NOTES
TERM III
CHANGES IN OUR ENVIRONMENT
There are three changes in our environment:
a. Chemical changes.
b. Biological changes.
c. Physical changes.
CHEMICAL CHANGES
Chemical changes are changes in which new substances are formed from.
Characteristics of chemical changes
a) The changes are irreversible.
b) A new substance is always formed.
c) There is a change in weight.
d) Heat or light or both are produced.
Examples of chemical changes
1. Burning of wood to ash.
2. Rusting of metals.
3. Burning of candle wick to ash
4. Burning of paper to ash
5. Burning of wood to charcoal..
PHYSICAL CHANGES
Physical changes are changes in which no new substances are formed.
Characteristics of physical changes
i. The changes are reversible.
ii. No heat or light is given out.
iii. There is no change in weight.
iv. There is no new substance formed.
Examples of physical changes
1. Melting of ice to water.
2. Melting of plastic.
3. Melting of butter.
4. Melting of candle wax.
5. Freezing of water to ice.
6. Evaporation of water to steam.
7. Water turning into water.
8. Vapour turning into water.
BIOLOGICAL CHANGES
Biological changes are changes which take place in the life of living things.
Characteristics of Biological changes
a) Young ones grow mature and become old.
b) Small ones change size and become big.
91
Examples of biological changes
1. Body growth.
3. Development of breasts in females.
4. Growth of nails in animals.
5. Growth of hair.
6. Growing of a seed to seedlings/Germination.
OTHER CHANGES IN THE ENVIRONMENT
1. Formation of clouds.
2. Temperature change.
3. Occurrence of day and night .
Man made changes
1. Man has built roads t.
2. Draining swamps.
3. Man has improved on animals, plants and birds by crossbreeding.
4. Man has built bridges across rivers, lakes and valleys.
5. Forests have been cut to create land for Agriculture.
6. Man has planted trees.
Natural changes
1. Earthquake
2. Drought
3. Floods
4. Change in season
5. Land slides
6. Rain formation
7. Days and night
Effects of various types of changes to people, animals and plants
1. People change from young one to old ones and later die.
2. Animals grow old and become useless.
3. Plants grow and later die.
4. Some animals are improved by crossbreeding.
5. New varieties of seeds are produced after research work.
6. Through research, plants and animals grow and mature quickly.
7. Cutting trees cause drought.
8. Earthquakes destroy life and property.
9. Droughts cause plants to die.
</passage>

<passage id="lchk_9e5f427d52f544aaaf907aac40433bf3" source="P 5 Scie Lesson Notes 2" part="1">
PRIMARY FIVE
2022
SCIENCE LESSON NOTES
TERM III
2022
C O M P I L E D B Y : O S C A R L O D D A
85
P.5 SCIENCE LESSON NOTES TERM III
CHANGES IN OUR ENVIRONMENT
There are three changes in our environment:
a. Chemical changes.
b. Biological changes.
c. Physical changes.
CHEMICAL CHANGES
Chemical changes are changes in which new substances are formed from.
Characteristics of chemical changes
a) The changes are irreversible.
b) A new substance is always formed.
c) There is a change in weight.
d) Heat or light or both are produced.
Examples of chemical changes
1. Burning of wood to ash.
Rusting of metals.
Burning of candle wick to ash Burning of paper to ash Burning of wood to
charcoal..
PHYSICAL CHANGES
Physical changes are changes in which no new substances are formed.
Characteristics of physical changes
i. The changes are reversible.
ii. No heat or light is given out.
iii. There is no change in weight.
iv. There is no new substance formed.
CN1 CO 'vj" LO
86
Examples of physical changes
1. Melting of ice to water.
2. Melting of plastic.
3. Melting of butter.
4. Melting of candle wax.
5. Freezing of water to ice.
6. Evaporation of water to steam.
7. Water turning into water.
8. Vapour turning into water.
BIOLOGICAL CHANGES
Biological changes are changes which take place in the life of living things.
Characteristics of Biological changes
a) Young ones grow mature and become old.
b) Small ones change size and become big.
Examples of biological changes
1. Body growth.
1. Development of breasts in females.
2. Growth of nails in animals.
3. Growth of hair.
4. Growing of a seed to seedlings/Germination.
OTHER CHANGES IN THE ENVIRONMENT
1. Formation of clouds.
2. Temperature change.
3. Occurrence of day and night.
Man made changes
1. Man has built roads t.
2. Draining swamps.
3. Man has improved on animals, plants and birds by crossbreeding.
4. Man has built bridges across rivers, lakes and valleys.
5. Forests have been cut to create land for Agriculture.
6. Man has planted trees.
Natural changes
1. Earthquake
2. Drought
3. Floods
4. Change in season
5. Land slides
6. Rain formation
7. Days and night
Effects of various types of changes to people, animals and plants
1. People change from young one to old ones and later die.
2. Animals grow old and become useless.
87
Plants grow and later die.
Some animals are improved by crossbreeding.
New varieties of seeds are produced after research work. Through research, plants
and animals grow and mature quickly. Cutting trees cause drought.
Earthquakes destroy life and property.
Droughts cause plants to die.
Floods destroy property and lives.
GOATS
Reasons for keeping goats Meat production.
Milk production.
Skin.
Some provide us with mohair.
Source of income.
Cultural purposes.
Hooves and horn are used in the making of buttons and glue. Animal droppings are
used as manure (farmyard manure)
External parts of a goat
Tail
Udder
Belly
Leg
Breeds of goats reared in Uganda Mubende goats.
The East African small goats.
Boar goats.
Saanen
The Somali goats.(Galla) Toggenburg
Horns
Eye
Ear
Nose 1 Muzzle
Mouth]
Breast
Hoof
7.
88
A mubende male goat is widely kept in Uganda. It weighs
between 40kg to 50 kg when mature.
1. The East African small goats are widely kept in Uganda, Kenya and Tanzania. A mature goat
can weigh between 25kg to 30kg.
The East African small goats are of mixed colours.
Anglo Nubian Mubende goats
1.
2.
The East African small ooats
1.
2.
The Somali goats (Galla)
Galla goats are kept in most parts of
</passage>

<passage id="lchk_6b5b31c299744b7a98430b9923fe831d" source="P 5 Science Lesson Notes Term III" part="14">
 Inviting health workers to talk to the children on health matters
Activities carried out in P.H.C (General)
 Learn better skills of farming for improvement of food production
 Sweeping or mopping the house at home
 Slashing grass in the house hold compound
 Construction of health centres
 Construction of public latrines or toilets
 Digging public rubbish pits
 Forming a health committee in the village
 Immunizing infants
TOPICAL TEST ON PHC
SECTION A
1. Write PHC in full.
2. Explain the meaning of community hygiene.
3. Give any one activity on individual can engage in to promote PHC.
4. State any one principle of PHC.
5. What is PHC?
6. Write BHC in full.
7. What is a community?
8. Write CDD in full.
9. Which element of PHC is promoted by bathing daily?
10. Give any one role of a family in promoting PHC.
38
SECTION B
11. Write down any four elements of PHC.
12. (a) What are health parades?
(b) Give any two activities done on health parades.
(c) Name one importance of health parades.
13. Write in full;
(a) CHWs
(b) TBAs
(c) EHC
(d) MCH
14. State any four activities done by the community to promote PHC.
15. Suggest any four activities carried out in PHC.
</passage>

<passage id="lchk_59a1f8ab7a7a4022ab0f32ebc5750eb7" source="P 5 Term I, II, III Scie" part="39">
5. It organises members at school to clean the school by picking litter.
HEALTH PARADES
These are assemblies intended to check children’s health and hygiene.
Activities carried out on health parade.
1. Teachers check r children whose heads and bodies are not well cleaned.
2. Teachers check children whose nails are not well groomed.
3. Teachers check children who do not brush their teeth.
4. Teachers check children who do not comb their hair.
5. Teachers check children who do not clean their clothes and bags.
Note: While checking is going on, records are made on each individual child.
</passage>

<passage id="lchk_56c14fc20cae423c893d543e97e25962" source="Paramount SCI T1 T3 P 5" part="68">
 Use tsetse fly traps to control tsetse flies
INTERNAL PARASITES
 These are parasites that live inside the body of the host.
 They live in muscles, intestines and liver
Examples of endoparasites (internal Parasites)
 Tape worms  Hook worms  Thread worms
</passage>

<passage id="lchk_c74ad7fa44ad452c962f9a3f5b6f3db7" source="Broad Examinations P.5 Integrated Science Mid-Term III Exam 2023" part="1">
BROAD EXAMINATIONS®

P.5 INTEGRATED SCIENCE EXAMINATION
MID - TERM III 2023

Time allowed: 2 hours 15 minutes

District Name: ....

Read the following instructions carefully: FOR EXAMINERS’

1. This paper is mad up of two sections: A and B. USE ONLY

2. Section A has 40 « iestions (40 Marks)

3. Section B has 15 questions (60 Marks)

4. Answer ALL questions in both sections A and B.

5. Ail answers must be written in the space provided in

blue or black ball point pens and ink. Only diagrams should

be done in pencil.

6. Unnecessary crossing of answers will lead to loss of marks.

~

Any handwriting, which cannot be easily read, may lead to

loss of marks

oo

Do not fill anything in the boxes indicated for

Examiners’ use only

Educational Cansult 2023. Tel: 0486 - 442077, 0786-68930), 0772864523 Page | of 8

brome
P.S int. Science Mid-Term Ill 2023

FON ACADEME EXEELLEMEE, AVOID MISSING BROAD HOLIDAY PACKAGES, WORK BOOKS & PAST PAPER ROORLETS,

SECTION .A. (40 Marks)

1. Write down any one example of physical changes.

2. Mention any one way germs enter our bodies.
Fa oP

3. State the use of a sponge while bathing.

4. Name the force that pulls objects thrown in air downwards.

5. Mention any one advantage of living in an extended family.

Use the diagram of a tooth below and answer question 6.

6. Name the tooth shown above.

7. In which any one way are swamps useful to people in a community?

8. Name any one exotic breed of goats kept for milk production,

9. Give a reason why oxygen can’t be used in fire extinguishers.

10. Give any one way of preserving meat in a local home.

11.Name the injury caused by direct contact with steam from hot food.
12. Mention the function of kidneys in the human body.

13.What does the term bush fallowing mean as used in improving soil fertility?

SE a ah
£75 RR TY CS ERR enn ese
Broad Educational Consult 2023. Tel: 0486 - 442077, 0786-6

59301, 0772-86482; of 8
P.5 Int, Science Mid-Term Ill 2023 ‘ ue

FOR ACADEMIC EXCELLENCE, AVOID MISSING BROAD HOLIDAY PACKAGES, WORK BOOKS & PAST RapeR soci. FS:

14.Write down the use of secateurs in caring for crops.

15. In which one way can pupils control diarrhoeal diseases at school?

The diagram below shows a container in which oil and water were put and left to
settle. Study and use it to answer question 15.

—
WS
»

16.Why did oil settle on top of water?

17.Why is docking 1n important practice in sheep rearing?

18.Give one reason why medicine and poison bottles should be kept where children cannc
reach,

19.In which one way is food useful to the body?

20. Why is contour ploughing encouraged in hilly areas?

21.Name the part of air used by plants to make food.

Study the life cycle of an insect and answer question 22.

22.Name the stage marked X.

23. Suggest a reason why people should not open soda bottles with teeth.
Broad Educational Consult 2023. Tel: 0486 - 442077, 0786-659301, 0772-864523 Page 3 of 8

.5 Int. Science Mid-Term Ill 2023
FOR ACADEMIC PXCHLLENE, ——— HOLIDAY PACKAGES, WORK BOOKS & PAST PAPER BOOKLETS:


; ?
24. In which way is moulting an important process in insects and snakes?

25.State the function of hydrochloric acid found in the human stomach.

aa EF SS A RPO PS ata a :

26. Mention any one disease spread by aedes mosquito.

27.Name the type of energy possessed by a rock rolling downhill.

28. How does draining stagnant water help to control mosquitoes?
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
