# Job ltsk_d36b234fb08c4f6082b05cccd99967a8-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for Social Studies, Primary Five 2026, Term 3.
The term has 10 teaching weeks and this subject has 5 periods per week. Every lesson is ONE 40-minute period, so keep each lesson small enough to teach in 40 minutes.
There are no weekly review lessons: the subject has a lot of content, so every period teaches or practises.
Give at most 49 teaching/practice lesson entries in teaching order (the last lesson of the term is the end of term assessment).
Each lesson has a kind: "teach" (new content) or "practice" (the same subtopic as the teaching lesson just before it: exercises, oral work, drawing, matching, filling in blanks, ALL taken from the passages).
When the material is thin (common in lower primary), follow each teaching lesson with a practice lesson. Split big subtopics over several teaching lessons.
Never pad with content the passages do not have: if they cannot fill the term, return fewer lessons and list what is missing in gaps. Ledgerly fills the remaining weeks with revision.
You are composing the SCHOOL'S OWN scheme. The passages below (the official NCDC curriculum and guides, plus schemes of work, lesson plans, notes and past papers from the school e-library) are reference material:
The NCDC documents (titles starting "NCDC") are the BASE: their topics, competences and order for this class and term are what the scheme must cover. NCDC lower-primary thematic curricula list every learning area side by side in table columns separated by " | ": take only the Social Studies column.
Every topic the NCDC curriculum lists for this class and term MUST become a unit, in the NCDC order. Share the weeks between ALL of them according to their NCDC periods, competences, content and subtopics. Large topics should receive more lessons than small topics.
combine them in this authority order: curriculum for required coverage; all relevant schemes for sequence and pacing; the strongest detailed notes for accurate teaching depth; past papers for expected applications and activities. Do not copy one reference scheme blindly.
Use this term's part of the material (Term 3) when the passages cover several terms.

REQUIRED NCDC topics/themes for Primary Five 2026, Term 3 (from the NCDC curriculum, in this order). Every one MUST have at least one unit whose title or theme names it, with about this many teaching/practice lessons:
  11. The Government of Uganda: about 24 lessons
  12. Population, Size and Distribution: about 25 lessons
Keep to these evidence-based shares. A broad topic may take substantially more lessons than a small topic when its NCDC scope, competences and subtopics justify it.
Do NOT write lesson content yet. Each unit and lesson must cite the passage ids it comes from in sourcePassageIds.

Reply shape:
{"title":string,"summary":string,"units":[{"title":string,"theme":string|null,"weekFrom":int|null,"weekTo":int|null,"competences":string|null,"sourcePassageIds":[string],"lessons":[{"title":string,"subtopic":string|null,"kind":"teach"|"practice","objectives":[string],"sourcePassageIds":[string]}]}],"gaps":[string]}

<passages>
<passage id="lchk_6d2556c7c2cf4bdaab5bead60ded2e89" source="NCDC P5 Curriculum – Social Studies" part="13">
The learner: | Spells, reads, pronounces | • The concept of | • Explaining what independence
• Explains what political | and writes words, sentences | independent | means.
independence means. | and structures related to | Uganda. | • Discussing good things related to
independence. | independent nations.

P5 Set One Syllabus, National Curriculum Development Centre | 207

  |   |  |  
 
The new words are | • Identifying the date
political independence. | when Uganda attained
independence.
• | Identifies | Spells, reads, pronounces | • The symbols of the nation: | • Explain the symbols
national | and writes words and | - The National Flag. | of the nation.
symbols | sentences related to | - National Anthem.
symbols of the nation. | - Coat of Arms.
and
The new words are | - Emblem.
explains
symbols, anthem, | - Language (English).
their
emblem, coat of arms, | - The Constitution (supreme law).
significanc
constitution and hoisted.
e. | • The significance of the symbols of the nation:
- The Constitution (supreme law).
- The National Flag.
- National Anthem.
- Coat of Arms. | • Discussing the
- Emblem. | significance of symbols
- Language (English). | of the nation.
• | Explains the | Spells, reads, pronounces | • Democracy | • Explaining what
meaning of | and writes words properly. | Ǧ The meaning of democracy. | democracy is.
democracy | Constructs sentences | Ǧ Importance of democracy.
• Discussing and debating
using key words related to | Ǧ Functions of democracy.
and its | the importance and
democracy and elections. | Ǧ Challenges of democracy.
importance. | Ǧ Roles of the citizens in practicing | functions of democracy.
The new words are
democracy. | • Naming the different
challenges, election,
elections.
Role-playing elections.

208 | P5 Set One Syllabus, National Curriculum Development Centre

  |  |  |  
  |  
citizen, conduct, bad | Ǧ | Types of elections. | • Discussing
practices. | Ǧ  How elections are conducted. | challenges of
Ǧ Bad practices during elections: before | democracy.
voting. | • Drawing different
during voting. after | election materials.
voting.
Ǧ Electoral commission, electoral officials, | • Suggesting two things
electoral materials and their functions. | people who get the
Ǧ Respect for democracy and elections. | least votes should do
after elections.
• Role-playing voting
exercise.
• Discussing importance of
electing leaders.

Suggested Competences for Assessment
• Identify the symbols of an independent nation.
• Explain the importance of those symbols of a nation.
• Explain the principles of democracy.

TOPIC 11: The Government of Uganda
General Background to the Topic
In the last topic, the learner learnt how Uganda became an independent nation; its symbols and their significance. The learner was also
exposed to democracy and its principles.

In this topic, he/she is going to learn about the government, the three organs of government, the constitution, duties of government,
sources of revenue and expenditure as well as rights and responsibilities of citizens of Uganda.
P5 Set One Syllabus, National Curriculum Development Centre | 209

Learning Outcomes
The learner is able to understand the organs of the government, the constitution and duties of citizens; explain the sources of revenue
and expenditure by government and understand the rights and responsibilities of the citizens of Uganda.
</passage>

<passage id="lchk_81d55cd06942488eb3d7927c27264ea9" source="NCDC P5 Curriculum – Social Studies" part="14">
Skills and Values/attitudes to be Developed

Skills | Values/attitudes
• Critical thinking | • Respect
• Observation | • Care
• Listening | • Cooperate
• Love
• Sharing
• Sympathy

    |   |  |  
The learner: | Spells, reads, pronounces | • The role of a government (the ruling | • Explaining the role
• Identifies the | and writes words, | body of a country). | of the government.
three organs of | sentences and | • The organs of the government: | • Discussing the roles of
government. | structures related to | Ǧ Executive (administer and implement | organs the government
organs of government. | decisions and programmes). | and their significance.
The new words are | Ǧ | Legislature (to make laws which
• Explaining the necessity
government, organs of a | people must observe and respect).
government, executive, | of the separation of
ǦJudiciary (to interpret laws made by | legislature and judiciary.
legislature, judiciary. | the legislature).
Explains the | Spells, reads, | • The constitution | • Explaining the meaning
meaning of the | pronounces and writes | of a constitution.
constitution, its | words, sentences and | - | Meaning of a constitution.
functions and | - | Functions of a constitution. | • Discussing the importance
structures related to the
importance. | constitution. | of a constitution.
- | Importance of a constitution.
The new words are | • Explaining the
constitution, function, | relationship
210 | P5 Set One Syllabus, National Curriculum Development Centre

    |   |  |  
relationship. | - Relationship between a | between the
constitution and the
constitution and elections.
elections.
• Explains the | Spells, reads, pronounces | • Duties of the government | • Explaining the
duties of the | and writes words, | duties of the
 | Communication:
government. | sentences and structures | government.
related to duties of the | Ǧ meaning of
government. | communication.
The new words are
Ǧ types of communication.
foreign affairs, budget,
sanity, election. | Ǧ importance of
communication.
Ǧ barriers of communication.
 | Administration/leadership.
 | Conduct elections.
 | Provide social studies.
 Making a budget.
• Handles foreign affairs and
sanity of the nation.
• Explains the | Spells, reads, pronounces | Revenue is income by government
sources of | and writes words,
□ Taxation
revenue and | sentences and structures
expenditure by the | related to the sources of | - Income Tax | • Explaining what income
government. | revenue and expenditure | - Value Added Tax (VAT) | is.
by the government. | - Property Tax
The new words are value | • Discussing how
□ Tourism | government earns
added tax, donation, | □ Licenses | money.
tourism, license, loan, | □ Donations and gifts
P5 Set One Syllabus, National Curriculum Development Centre | 211

    |   |  |  
grant, bill, property. | □ Loans and grants
□ Sale of government
bills and properties
□ Expenditure
-  salaries and allowances
• Explaining the ways
-  development | in which government
Ǧ | Expenditure is how | programmes | spends its revenue.
government uses or spends | - rent
money. | - security
- social services
• Explains the rights and | Spells, reads, pronounces | • Rights | • Explaining the rights of
responsibilities of citizens of | and later makes sentences | citizens of Uganda.
What a citizen must
</passage>

<passage id="lchk_4edd4afd1d254374a6c93da86c0debc8" source="NCDC P5 Curriculum – Social Studies" part="15">
Uganda. | using words related to rights
and responsibilities of citizen | have (life, food, shelter,
of a country. | education, cloth, water,
The new words are right, | medical care and
responsibility, child labour, | security) | • Explaining the
security, development. | responsibilities of
• Responsibilities | Ugandans.
What a citizen should do to
contribute to the | • Discussing causes
development of Uganda. | and ways of child
labour and how to
• Child Labour Education. | stop it.

Suggested Competences for Assessment
• Explain the various organs of a nation and their significance.
• Discuss the importance of a constitution to a nation.
• Draw a chart showing how government gets revenue and spends it.

212 | P5 Set One Syllabus, National Curriculum Development Centre

TOPIC 12: Population, Size and Distribution
General Background to the Topic
The learner has idea of numbers of learners in different classes in the school. This is called population. Every morning there is roll call
and the totals are put together, this is a simple census.

In this topic, the learner will learn about the population of Uganda, its growth and the importance of a census in a country. He/she will
also learn the size of the population and its settlement patterns or distribution. The high and low population densities have problems to
the social, economic and political environments.

The learner therefore needs to equip him/herself with possible solutions to the problem. This topic demands the learner as a member of
the young generation to develop positive attitudes of controlling population growth through family planning, and better reproductive health
practices.

Learning Outcome
The learner is able to promote and practice desirable values in society and show respect for his/her own and other cultures.

Skills and Values/attitudes to be developed

Skills | Values/attitudes
Ǧ Drawing | Ǧ Love
Ǧ Interpretation of information | Ǧ Care
Ǧ Critical thinking | Ǧ Co-operation
Ǧ Observation | Ǧ Respect
Ǧ Inquiry | Ǧ Sharing
Ǧ Effective communication | Ǧ Sympathy
Ǧ Description | Ǧ Respect
Ǧ Creativity

P5 Set One Syllabus, National Curriculum Development Centre | 213

  |   |  |  
 
Learner: | Reads, spells and | • Meaning of population and | • Explaining what
• Explains the | constructs sentences | census | population and census
importance of a | using words related to | means.
Ǧ | Population is the number of
census. | the census.
people in a given demarcated | • Counting the number of
The new words are
area, e.g. a nation. | learners, teachers and non-
census, population,
Ǧ | Census is an official count | teachers in the school
teenage, teenager.
population. In this case the | (mini- census).
population of Uganda is 41.49
million (2016). | • Grouping them by sex and
tribes.
Ǧ | Meaning of teenagers (people
between 13-19 years of age).
Ǧ | Figures of teenagers by 2007 is
4,823,600 (13-19 years)
• Importance of census:
Ǧ | Know the total number of
people
Ǧ Plan for them (social,
political and economic).
• | Explains the | Reads and | • Meaning of population growth: | • Explaining what
influence of | constructs sentences | population, size or number
Ǧ | The increase of people’s
population | using words related | means.
numbers in the country.
to the population
growth on
growth. | • The factors that influence | • Discussing the factors that
communities. | The new words are: | lead to population
population growth:
</passage>

<passage id="lchk_e0031cef799c413f9438d6584be3e476" source="NCDC P5 Curriculum – Social Studies" part="16">
population, growth | Ǧ Climate. | increase.
immigration and better | Ǧ Fertility rate of women. | • Explaining the dangers of
health. | Ǧ Immigration. | fast population growth.
214 | P5 Set One Syllabus, National Curriculum Development Centre

  |  |  |  
  |  
Ǧ  Occupation. | Discussing how to control population
Ǧ  Food. | growth.
Ǧ  Better health (reproductive
health).
Ǧ Social services.
Security and peace.
• Explains what | Reads, spells, | • Population distribution and | • Explaining what population
population | pronounces | reasons. | distribution means.
distribution | and writes | Ǧ The spread of people in an area
means. | words related | and in this case Uganda.
to the topic.
Ǧ Some districts have more
Makes
people than others.
sentences using
those words. | Ǧ Some places like urban
centres have more people
than rural areas.
Ǧ Some places like the plateau
have more people than some
mountains.
Ǧ Some climatic areas have more
people than others.
• Discusses | Constructs | • Meaning of population density. | • Discussing factors that are
problems | sentences using | • Meaning of high population. | associated with:
associated | related words in | Ǧ high population density.
with high and | the topic. | • Meaning of low population | Ǧ low population density.
low | density.
population | • Discussing how HIV/AIDS affects
density. | • Effects of HIV/AIDS on population | population.
and economic production. | • Social and economic effects of
HIV/AIDS on the population.
P5 Set One Syllabus, National Curriculum Development Centre | 215

    |   |  |  
• Problems of high
population density.
Problems associated with
low population density.
• Discusses the | Constructs sentences using | • Solutions to high | • Ex` the solutions for
solutions to | related words in the topic. | population density | low population.
problems of high and | The new words are | • Discussing the
low population | population density, sensitise, | solution for low
density. | export, labour. | population.
• Explains possible | Constructs sentences that | • Control of population | • Discussing ways of
ways of controlling | have words related to the | growth. | controlling population
population growth. | topic. | growth.
The new words are high | • Debating the
population, low population | disadvantage of
and population growth. | population growth.

Suggested Competences for Assessment
• | Write the causes of population growth.
• | List the difficulties a family finds in looking after a big number of children.
• | List the problems found in a crowded community such as a slum.
• | Write a composition “The country I want to live in”.

216 | P5 Set One Syllabus, National Curriculum Development Centre

www.ncdc.go.ug
</passage>

<passage id="lchk_27b180ca68bb4d96babb91d578834092" source="P 5 SST Scheme Term III 2019 (ecolebooks Com)" part="1">
Ecolebooks.com
DOWNLOAD MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
SCHEME OF WORK:
SUBJECT: SOCIAL STUDIES CLASS: P.5 SUBJECT TEACHER ………………………………………………….. TERM THREE YEAR ………………….
WK PD Theme Topi
c
Sub-
Topi
c
Competence Content Methods and
Techniques
Life skills and
values
( Indicators)
Suggested
activities
Teaching /
learning aids
Ref R
e Subject Language
1 1
LIVING TOGETHER IN UGANDA
Uganda as an independent nation
Independence
-Explain the
word political
-
Independence
-Independent
-Pronounce,
spell, write ,
read words to
independence
Independence
-definition – is the state
of being free from
foreign control or rule.
Characteristics of an
independent nation
-Territory of land.
-Government
-Constitution
-Parliament
-Judiciary
-Freedom
-Police to keep law and
order
-Citizens
-Control its affairs
-Explanation
-Discussion
-Brain
storming
-Question and
answer
-Self esteem
-Negotiation
-Problem
solving
-Define and
explain the word
independence.
-Discuss the
characteristics of
an independence
nation
-Dramatizing
-Text books
- Children’s
properties
-
Function
al SST
book 5
page 165
MK
Standard
page 117
Ecolebooks.com
DOWNLOAD MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
2
Symbols of a nation (The national flag)
-Identify
national
symbols and
explain their
significances
Spells , reads,
pronounces
and writes
words and
sentences
related to
symbols of the
nation.
The symbols of the
nation.
-The National flag.
-National Anthem
-Coat of Arms
-Emblem
-language (English)
-The constitution
(supreme law)
National flag
-Concept
-The designer
(Grace Nsingira)
-The colours of the flag
-Areas where it can be
flown.
-How and when its
flown.
-Signifance of the
national flag.
-Explanation
-Discussion
-Question and
answer
-Self discovery
-Effective
communication
-Appreciation
-Self awareness
-observation
-Respect
-love
-caring
-Drawing and
shading
-Practice how to
raise fly the
national flag.
-national flag
-Pictures of
the national
flag.
-Text book
Mk std
\bk 5
Pg 12506
Teachers
guid
Pg 222
Ecolebooks.com
DOWNLOAD MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
1 3
LIVING TOGETHER IN UGANDA
Uganda as an independent nation
Symbols of a nation (The National Anthem -Identify and
explain the
National
Anthem.
(stanza) and
the coat of
Arms
-Reads, spell,
pronounce
and write
words found
in the Anthem
and Coat of
Arms
National Anthem
-Concept (3 stanzas)
-The composer (George
William Kakoma)
-Occasions when its
sung.
(British National
Anthem) was sung
before Independence.
-Significances.
-Discussion
-Discovery
-Explanation
-Appreciation
-Self awareness
-Effective
communication
-Observation
-Analyse
-Respect
-Singing and
practicing the
Anthem
-Papers
having the
National
Anthem
MK stdbk
5 pg 123-
4
Ecolebooks.com
DOWNLOAD MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
4
&
5
The national coat of Arm
National Coat of Arms.
-Concepts
-Features of the coat of
Arms.
-The National Motto
-Significance of The
Coat of Arms.
-Significances of the
features of the coat of
Arms.
-Discussion
-Question and
answer
-Drawing
-Patriotism
-Respect
-Drawing and
indicating the
features of he coat
of Arms
-Coat of
Arms.
-Chart
showing the
coat of Arms
MK stdbk
5 page
126-127
Ecolebooks.com
DOWNLOAD MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
2 1
LIVING TOGETHER IN UGANDA
Uganda as an independent nation
Symbols of a nation (The
Emblem)
-Name and
identify the
emblem and
give its
significances
-Spell, read,
pronounce
the words
related to
the National
emblem
Emblem
-Concepts (crested
crane)
</passage>

<passage id="lchk_1162553670784949a6a5f4ead61c3374" source="P.5 SST SCHEME TERM III 2019" part="1">
SCHEME OF WORK:
SUBJECT: SOCIAL STUDIES CLASS: P.5 SUBJECT TEACHER ………………………………………………….. TERM THREE YEAR ………………….
WK
PD
Theme
Topic
Sub-Topic
Competence
Content
Methods and Techniques
Life skills and values
( Indicators)
Suggested activities
Teaching / learning aids
Ref
Re
Subject
Language
1
1
LIVING TOGETHER IN UGANDA
Uganda as an independent nation
Independence
-Explain the
word political
-Independence
-Independent
-Pronounce, spell, write , read words to independence
Independence
-definition – is the state of being free from foreign control or rule.
Characteristics of an independent nation
-Territory of land.
-Government
-Constitution
-Parliament
-Judiciary
-Freedom
-Police to keep law and order
-Citizens
-Control its affairs
-Explanation
-Discussion
-Brain storming
-Question and answer
-Self esteem
-Negotiation
-Problem solving
-Define and explain the word independence.
-Discuss the characteristics of an independence nation
-Dramatizing
-Text books
-Children’s properties
-Functional SST book 5 page 165
MK Standard page 117
2
Symbols of a nation (The national flag)
-Identify national symbols and explain their significances
Spells , reads, pronounces and writes words and sentences related to symbols of the nation.
The symbols of the nation.
-The National flag.
-National Anthem
-Coat of Arms
-Emblem
-language (English)
-The constitution (supreme law)
National flag
-Concept
-The designer
(Grace Nsingira)
-The colours of the flag
-Areas where it can be flown.
-How and when its flown.
-Signifance of the national flag.
-Explanation
-Discussion
-Question and answer
-Self discovery
-Effective communication
-Appreciation
-Self awareness
-observation
-Respect
-love
-caring
-Drawing and shading
-Practice how to raise fly the national flag.
-national flag
-Pictures of the national flag.
-Text book
Mk std
\bk 5
Pg 12506
Teachers guid
Pg 222
1
3
LIVING TOGETHER IN UGANDA
Uganda as an independent nation
Symbols of a nation (The National Anthem
-Identify and explain the National Anthem. (stanza) and the coat of Arms
-Reads, spell, pronounce and write words found in the Anthem and Coat of Arms
National Anthem
-Concept (3 stanzas)
-The composer (George William Kakoma)
-Occasions when its sung.
(British National Anthem) was sung before Independence.
-Significances.
-Discussion
-Discovery
-Explanation
-Appreciation
-Self awareness
-Effective communication
-Observation
-Analyse
-Respect
-Singing and practicing the Anthem
-Papers having the National Anthem
MK stdbk 5 pg 123-4
4
&
5
The national coat of Arm
National Coat of Arms.
-Concepts
-Features of the coat of Arms.
-The National Motto
-Significance of The Coat of Arms.
-Significances of the features of the coat of Arms.
-Discussion
-Question and answer
-Drawing
-Patriotism
-Respect
-Drawing and indicating the features of he coat of Arms
-Coat of Arms.
-Chart showing the coat of Arms
MK stdbk 5 page 126-127
2
1
LIVING TOGETHER IN UGANDA
Uganda as an independent nation
Symbols of a nation (The Emblem)
-Name and identify the emblem and give its significances
-Spell, read, pronounce the words related to the National emblem
Emblem
-Concepts (crested crane)
-Reasons why it was chosen as the emblem.
-Documents where its found.
-Significances.
-Discussion
-Explanation
-Discovery
-Appreciation
-Description
-Inquiry
-Drawing
-Critical thinking
-Love
-Caring
-Respect
-Drawing the emblem and shading
-Pictures of the emblem
Mk stdbk 5 page 128
2
The National Language
-Name the Local languages.
</passage>

<passage id="lchk_92cd49544d9648a5b46aae68c7907b16" source="Primary 5 Social Studies Scheme of Work – Term 3" part="10">
writes the
words
related to
the topic
Signs of
Uganda’s
backwardness
-Ignorance
-Illiteracy
-Superstition
-Poverty
-evaluating
-analyzing
Inquiry
Guided
discussion
Explanation
Discussing
Uganda’s
backwardne
ss
Chalk
board
Mk
stan
dar
d
soci
al
stud
For more schemes of work, visit www.uganda.madpath.com
-Diseases
-Hunger
-High infant
mortality rate
ies
for
upp
er
clas
ses
pg
12,1
3
2 How to
overcome
Uganda’s
backward
ness
A learner
-Outlines at
least seven
ways that
can help
Uganda over
come its
backwardnes
s
A learner
spell, reads,
write and
pronounces
words
related to
the topic
correctly
-Develop social
services
-Boost job
creation
-Encourage
industrialization
-Encourage
foreign investors
-Improve
education
standards
-evaluating
-analyzing
Inquiry
Guided
discussion
Explanation
Discussing
ways of
overcoming
Uganda’s
backwardne
ss
Chalk
board
Mk
stan
dar
d
soci
al
stud
ies
for
upp
er
clas
ses
pg
13,
14
</passage>

<passage id="lchk_154f8943cbfe46e4af8f596d4ecad834" source="ALL SST Notes P 4 TO P 7 ALL Terms Excel 3" part="3">
Voluntary leaders …………………………………………………………………………………… .140
Cultural leaders ……………………………………………………………………………………… 142
How leaders are chosen in our dist rict ………………………………………………………… .143
Qualities of a good leader ………………………………………………………………………… ..143
Elections ……………………………………………………………………………………………… ..143
Rights and responsibilities of people in our district …………………………………………. 146
Citizenship …………………………………………………………………………………………….. 149
Topic 5. How to meet people’s needs in the district .
Introduction to social services ………………………………………….………………………… .151
Education service…………………………………………………………………………………… ..151
Health service ………………………………………………………………………………………… 154
Transport service …………………………………………………………………………………… ..155
Communication service …………………………………………………………………………… ..165
Secur ity service ……………………………………………………………………………………… .173
Banking service ……………………………………………………………………………………… .178
Housing service ……………………………………………………………………………………… .181
Electricity service ……………………………………………………………………………………. .182
Water supply service ………………………………………………………………………………… 183
Problems faced in meeting people’s needs ……………………………………………………… 184
Social service centres ………………………………………………………………………………. .185
Social service providers …………………………………………………………………………… ..186
Caring for social service centres ………………………………………………………………… ..186
Page 6
TOPIC 1: LOCATION OF OUR DISTRICT IN UGANDA.
MAPS AND PICTURES.
A map is a drawing/ representation of an object as seen from above.
Maps show how objects look like when viewed directly from above.
We use symbols to help us understand and interpret a map of a detailed area.
The boundary of a map determines the size and shape of the map.
A picture is a representation of an object drawn as seen from aside.
All features on a picture can be clearly seen as real objects.
Pictures are more detailed than maps.
Maps and Pictures of different objects
Object name Picture Map
a tree
a plate
a pot
a house
a chair
a cup
a hut
Page 7
a car
a table
Similarity between maps and pictures.
❖ Both are representations of objects.
Difference between a picture and a map.
❖ A picture is drawn as seen from aside while a map is drawn as seen from above.
❖ A picture is more detailed than a map.
Testing Exercise.
1. Give the meaning of each of the following;
(i) A picture
(ii) A map
2. Give one way a map is similar to a picture.
3. Why is it easier for one to understand a picture of an object than its map?
4. How is a map different from a picture?
5. Draw the maps of the following objects.
a cup a circular table a pot a tree
ELEMENTS OF A MAP.
▪ A key
▪ A scale
▪ A heading/ title
▪ A compass direction
▪ A frame.
Importance of different elements of a map.
Element Importance
❖ A compass direction ❖ It helps to show the direction of places on a map
❖ A title/ heading ❖ It helps one to know what the map is all about.
❖ A key ❖ It helps a map reader to interpret symbols used on a
map.
❖ A scale ❖ It helps a map reader to calculate the actual ground
distance on a map.
❖ A frame ❖ It shows the extent of the area represented by the
map.
Page 8
Problems a map reader may face when reading a map without the map elements.
Element missing Challenge a map reader is likely to face
▪ Without a compass
direction • Failure to know the direction of places on a map
▪ Without a title/
heading • Failure to know what the map is all about.
▪ Without a key • Failure to interpret symbols used on a map.
▪ Without a scale • Failure to calculate the actual ground distance on a map.
</passage>

<passage id="lchk_de607580e44240119fc7d47aeb50c2a6" source="ALL SST Notes P 4 TO P 7 ALL Terms Excel Copy" part="3">
Voluntary leaders …………………………………………………………………………………… .140
Cultural leaders ……………………………………………………………………………………… 142
How leaders are chosen in our dist rict ………………………………………………………… .143
Qualities of a good leader ………………………………………………………………………… ..143
Elections ……………………………………………………………………………………………… ..143
Rights and responsibilities of people in our district …………………………………………. 146
Citizenship …………………………………………………………………………………………….. 149
Topic 5. How to meet people’s needs in the district .
Introduction to social services ………………………………………….………………………… .151
Education service…………………………………………………………………………………… ..151
Health service ………………………………………………………………………………………… 154
Transport service …………………………………………………………………………………… ..155
Communication service …………………………………………………………………………… ..165
Secur ity service ……………………………………………………………………………………… .173
Banking service ……………………………………………………………………………………… .178
Housing service ……………………………………………………………………………………… .181
Electricity service ……………………………………………………………………………………. .182
Water supply service ………………………………………………………………………………… 183
Problems faced in meeting people’s needs ……………………………………………………… 184
Social service centres ………………………………………………………………………………. .185
Social service providers …………………………………………………………………………… ..186
Caring for social service centres ………………………………………………………………… ..186
Page 6
TOPIC 1: LOCATION OF OUR DISTRICT IN UGANDA.
MAPS AND PICTURES.
A map is a drawing/ representation of an object as seen from above.
Maps show how objects look like when viewed directly from above.
We use symbols to help us understand and interpret a map of a detailed area.
The boundary of a map determines the size and shape of the map.
A picture is a representation of an object drawn as seen from aside.
All features on a picture can be clearly seen as real objects.
Pictures are more detailed than maps.
Maps and Pictures of different objects
Object name Picture Map
a tree
a plate
a pot
a house
a chair
a cup
a hut
Page 7
a car
a table
Similarity between maps and pictures.
❖ Both are representations of objects.
Difference between a picture and a map.
❖ A picture is drawn as seen from aside while a map is drawn as seen from above.
❖ A picture is more detailed than a map.
Testing Exercise.
1. Give the meaning of each of the following;
(i) A picture
(ii) A map
2. Give one way a map is similar to a picture.
3. Why is it easier for one to understand a picture of an object than its map?
4. How is a map different from a picture?
5. Draw the maps of the following objects.
a cup a circular table a pot a tree
ELEMENTS OF A MAP.
▪ A key
▪ A scale
▪ A heading/ title
▪ A compass direction
▪ A frame.
Importance of different elements of a map.
Element Importance
❖ A compass direction ❖ It helps to show the direction of places on a map
❖ A title/ heading ❖ It helps one to know what the map is all about.
❖ A key ❖ It helps a map reader to interpret symbols used on a
map.
❖ A scale ❖ It helps a map reader to calculate the actual ground
distance on a map.
❖ A frame ❖ It shows the extent of the area represented by the
map.
Page 8
Problems a map reader may face when reading a map without the map elements.
Element missing Challenge a map reader is likely to face
▪ Without a compass
direction • Failure to know the direction of places on a map
▪ Without a title/
heading • Failure to know what the map is all about.
▪ Without a key • Failure to interpret symbols used on a map.
▪ Without a scale • Failure to calculate the actual ground distance on a map.
</passage>

<passage id="lchk_f7987b7f64ac40acb0ec5439a8dd7722" source="Standard Social Studies Primary Five Lesson Notes P 5 2019" part="32">
NB: the population department is under the ministry of finance planning and
economic development
</passage>

<passage id="lchk_3b51923ae97b421788a1db01c87760a6" source="P.5 Social Studies & RE Beginning of Term III Examination 2023" part="5">
(a) Give two reasons why Allah created man.
(i) ____________________________________________________________
(ii) ____________________________________________________________
(b) How did man disobey Allah?
____________________________________________________________
(c) How do people disobey Allah today?
____________________________________________________________
55. FOR BOTH
(a) What is Authority?
____________________________________________________________
____________________________________________________________
(b) State any two types of authority.
(i) ____________________________________________________________
(ii) ____________________________________________________________
(c) How do leaders misuse their authority?
____________________________________________________________
********END*******
</passage>

<passage id="lchk_75e0d4f8463c4ec08bc4ffdd52317588" source="P.5 Social Studies & RE Mid Term III Examination 2023 – Outreach Schools" part="5">
miracles that Jesus performed.
i) _______________________________________________________________
ii) _______________________________________________________________
Or: Who was the father of prophet Muhammad?
_________________________________________________________________
b) Who was the mother of Prophet Muhammad?
_________________________________________________________________
c) Write down any two miracles that Mohammad performed.
i) ________________________________________________________________
ii) _______________________________________________________________
55. Either: Name the two parts of the Bible.
i) ________________________________________________________________
ii) _______________________________________________________________
b) Write two gospel books.
i) _____________________________ ii) ______________________________
Or: Write down four pillars of Islam.
i) ________________________________________________________________
ii) ______________________________________________________________
iii) _______________________________________________________________
iv) _______________________________________________________________
************EN D*************
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
