# Job ltsk_67b7fe23c3f14d2b9233a9c9a7216db3-1

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 2 lesson(s) below of week 9 of the Social Studies scheme for Primary Five 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P5: one 40-minute lesson: 3–4 ideas; 300–500 words; connected explanations and application; 5–8 activities.

lessonId=lles_57f504f6277e458eb4be459052544c00: lesson 42, Tuesday, 1 period(s), 40 minutes.
  Unit: Population, Size and Distribution (theme: Living together in Uganda). Lesson: HIV/AIDS: spread, prevention and care — Effects of HIV/AIDS on population.
  Objectives: Write HIV and AIDS in full.; State how HIV/AIDS spreads and how it can be prevented (ABC).; State how TASO helps AIDS patients.

lessonId=lles_f225353b542644da978ad93d8ea3b37a: lesson 43, Wednesday, 1 period(s), 40 minutes.
  Unit: Population, Size and Distribution (theme: Living together in Uganda). Lesson: Social and economic effects of HIV/AIDS on the population — Effects of HIV/AIDS on population.
  Objectives: State the social effects of HIV/AIDS on the population.; State the economic effects of HIV/AIDS on the population.

Write, using ONLY the passages below. Passages from "NCDC" documents are the official base for what to teach; NCDC lower-primary thematic curricula put every learning area in columns separated by " | ": use only the Social Studies column.
For EACH lesson:
- notes: the CHALKBOARD NOTES the teacher writes on the board for learners to copy into their exercise books, in Markdown, at exactly this class level.
  Use the detailed notes in the passages as the factual base, not merely the short scheme wording.
  Learner-facing CONTENT ONLY. Never write instructions or activities in the notes: no 'discuss', 'in your groups', 'tell the story', 'sing', 'act out', 'read with your teacher', 'say aloud', 'think of'. Those go in methods.
  Write the content itself: state the facts, meanings, examples and lists. For a Bible or Quran passage, give the reference AND what it says or teaches in one or two sentences (not 'read John 8:12').
  Structure:
    # TOPIC: <unit title in capitals>
    ## SUB-TOPIC: <lesson title>
    then short sections, each under a ### heading that names its content (e.g. ### Meaning of independence, ### Symbols of Uganda, ### Ways Christ is the light of the world, ### Importance of a census, ### Example 1).
    Inside a section: a definition or short explanation in one to three plain sentences, then numbered points (1. 2. 3.) for lists, each a short complete sentence a learner can copy.
    Bold the key words. Use a small Markdown table only for comparisons (e.g. organ of government | its work).
    Examples ('### Example 1', '### Example 2', ...) are ONLY for Mathematics, English and Reading: worked examples taken from the passages, set out step by step. Other subjects have no Example sections.
    Write mathematics in LaTeX: $\frac{3}{4}$ inline, $$...$$ on its own line. Column sums and long division are coded diagrams, not LaTeX.
    When the curriculum names new words, list them once near the top as '### New words' followed by the words separated by commas (no tables, no pronunciation drills).
    End with '### Exercise': 3–8 numbered questions on this lesson, taken from the activities, for learners to answer in their books.
  Keep it board-sized: about as long as a teacher would write in one lesson; no greetings, no 'In this lesson we will', no notes to the teacher.
  Where a matching past-paper question exists, use it as a worked example, an Activity, or a clearly marked 'NB / Exam practice' item; do not let an exam paper determine the curriculum order.
- methods: ONLY the names of the teaching methods, comma separated, for the scheme of work's Methods column (e.g. 'Story telling, Discussion, Guided Bible reading, Question and answer'). At most 6 names, no sentences.
- teachingGuide: the CLASS ACTIVITIES, step by step: what the teacher does and what learners do (discussion, group work, story telling, songs, dramatisation, guided Bible/Quran reading, oral work, drawing, games), as given or implied in the passages. Everything taken out of the notes because it is an instruction goes here.
- materials, lifeSkills, assessment: as given or implied in the passages; null when the passages are silent.
- lessonPlan: the LESSON PLAN in the Ugandan format: competences (subject and language competence), objectives, prior knowledge, methods, materials, references (titles of the passages used),
  and steps (Introduction, Lesson development, Conclusion; split development into parts when useful) with minutes adding up to the lesson's minutes, each with the teacher's and the learners' activity, plus assessment, homework and life skills.
  The content of the plan comes from this lesson's notes; plan when the teacher writes each part on the board, and put the class activities from teachingGuide into the steps.
- activities (activities and exercise questions are the same thing): questions for learners copied from the passages, drawn from the variety of notes, workbooks and past papers supplied. Set origin='source'.
  For each one set sourcePassageId and sourceQuote = the question's exact words copied from that passage, so it can be verified.
  Give answer only when the passage gives it or it is plain arithmetic; otherwise null. concept = the subtopic it tests, skill = what the learner does (e.g. 'identify', 'compute', 'explain').
  kind is one of: computation, short_answer, multiple_choice, fill_blank, true_false, matching, structured, essay, drawing. cognitiveLevel is one of: remember, understand, apply, analyse, evaluate, create.
- Never write a question, example or activity that is not in the passages, and never change a sourced question's numbers to make a new one. If the passages have too few, use what there is and list the shortfall in gaps.
- diagrams: up to 3 teaching pictures per lesson of things the passages describe that learners must SEE. Skip them when nothing in the lesson is visual.
  NEVER make a table, list or text box into a diagram; tables belong in the notes as Markdown tables. Choose a method per picture:
  * method "illustration" for real things: animals, plants, body parts and organs, tools, apparatus, objects, scenes (e.g. the external parts of a domestic fowl, a beehive, a flower).
    Give concept = a precise description of what to draw (e.g. 'side view of a domestic hen, full body') and parts = the exact part names from the passages to label. No svg. Ledgerly draws it once and reuses it.
    For a picture comparing two things, name each part with its owner so both get labelled, e.g. 'comb (cock)', 'comb (hen)'.
  * method "coded" for exact maths pictures, with coded = one of:
    {"type":"shape","shape":"circle|square|rectangle|triangle|right-triangle|equilateral-triangle|isosceles-triangle|parallelogram|rhombus|trapezium|kite|pentagon|hexagon|octagon"}
    {"type":"fraction","shape":"circle|bar","numerator":3,"denominator":4}   {"type":"number-line","from":0,"to":10,"step":1,"marks":[3,7]}
    {"type":"map","region":"uganda","layers":["lakes","rivers","mountains","towns","neighbours","regions","equator"],"highlight":["Northern"]} for any map of Uganda (pick the layers needed; parts = the lakes, rivers, mountains, towns, neighbours or regions to label, e.g. 'Lake Kyoga', 'River Victoria Nile', 'Mount Elgon', 'Kenya', 'Northern Region'),
    {"type":"clock","hour":3,"minute":30}   {"type":"bar-chart","title":"...","yLabel":"...","bars":[{"label":"Mon","value":4}]} (only with data given in the passages)
    {"type":"column-sum","operation":"add|subtract|multiply","numbers":[345,278],"showAnswer":true} for vertical working   {"type":"long-division","dividend":756,"divisor":6,"showWorking":true}
    {"type":"angle","degrees":60,"label":"x"}   {"type":"venn","sets":[{"label":"Even","items":["4"]},{"label":"Prime","items":["3"]}],"both":["2"]} (numbers always from the sourced question)
  All pictures are printed in BLACK: black outlines on white, mostly outline, simple grey or hatched shading only where needed, never colour.
  * method "svg" for simple schematics only (cycles, food chains, flow of a process): a self-contained SVG, viewBox="0 0 640 420", white background, black outlined shapes (fills white or light grey #e6e6e6 only),
    labels font-size 16-18 joined by leader lines, arrows via <marker>, a title at the top, nothing outside the viewBox. No scripts, images, links, CSS or external fonts.
  Label only parts the passages name. key is a short slug, unique within the lesson; put [[diagram:key]] on its own line in that lesson's notes where it belongs; sourcePassageId is the passage it depicts.
- sourcePassageIds: every passage id that lesson used.

Reply shape:
{"lessons":[{"lessonId":string,"notes":string,"methods":string|null,"teachingGuide":string|null,"materials":string|null,"lifeSkills":string|null,"assessment":string|null,"sourcePassageIds":[string],"lessonPlan":{"competences":[string],"languageCompetence":string|null,"objectives":[string],"priorKnowledge":string|null,"methods":[string],"materials":[string],"references":[string],"steps":[{"stage":string,"minutes":int,"teacherActivity":string,"learnerActivity":string}],"assessment":string|null,"homework":string|null,"lifeSkills":[string]},"diagrams":[{"key":string,"title":string,"caption":string|null,"method":"illustration"|"coded"|"svg","concept":string|null,"parts":[string],"coded":object|null,"svg":string|null,"sourcePassageId":string|null}],"activities":[{"question":string,"answer":string|null,"options":[string]|null,"kind":string,"concept":string,"skill":string,"cognitiveLevel":string,"difficulty":1-5,"origin":"source"|"generated","sourcePassageId":string|null,"sourceQuote":string|null}],"gaps":[string]}]}

Your previous reply for these lessons was rejected by the quality gate:
- lessonId=lles_57f504f6277e458eb4be459052544c00: only 2 activities; need at least 4
- lessonId=lles_f225353b542644da978ad93d8ea3b37a: only 1 activities; need at least 4
Rewrite each of these lessons in full, with its lesson plan. Keep every fact grounded in the passages, remove repetition, and meet the class depth and activity requirements.

<passages>
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

<passage id="lchk_e9bf3ccc4d0740c9b05e37f9727a64cd" source="P 5 SST Scheme Term III 2019 (ecolebooks Com)" part="6">
Population
Distribution
-Defining
-Factors affecting
population
distribution.
• Urbanization
• Industrialization
• Medical services
• Climate
• Physical features.
-Discussion
-Explanation
-Question
and answer
-Appreciation
-Observation
-Map reading
-Sharing
-Respect
-Discussing
how the
factors affect
the population
distribution
-School
- neighborhood
-Pictures
and
photograph
Mk std
Bk 5
Pg 145-
147
Ecolebooks.com
DOWNLOAD MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
8 1
&
2
LIVING TOGETHER IN UGANDA
Population size and distribution
Population Density
-Explaining
population
density and
high
population
density
-Density
-Square
kilometer
Population density
-Definition
-Method of
calculation
Popn density=No of pple
Sq k/m
-High population
density
-Low population
density
-Illustration
-Explanation
-Question
and answer
-Observation
-Appreciation
-Critical
thinking
-Discussing the
high and how
population
density
-Calculating
population
density
-Chalkboard
illustration
Functio
nal
Bk 5
Page
198
Ecolebooks.com
DOWNLOAD MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
3
&
4
Population
-Discussing
the problems
associated to
high and low
population.
-Pronounce ,
read , spell
and use
words
related to
population.
-Advantages and
disadvantages of high
population (social
factors)
-Problems associated
with low population.
-Solutions to high
population density
and ways of
controlling
population growth.
-Explanation
-Discussion
-Question
and answer
-Critical
thinking
-Inquiry and
answer
-Discussing the
problems
associated with
high and law
population.
-Discussing the
solutions to the
high
population
density and
ways of
controlling
population
growth.
-Discussing the
effects of HIV
on population
and economic
production
- An Atlas
-School
environmen
t
School
neighbourh
ood
Functio
n
Bk 5
Pg 198-
199
Mk std
Bk 5
Pg 148
Ecolebooks.com
DOWNLOAD MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
8 5
LIVING TOGETHER IN UGANDA
Effects of HIV / AIDs on population and economic development -Discussing
the effects of
HIV/ AIDS on
population
and
economic
production
-HIV
-AID
-Economic
-Production
Effects of HIV / AIDS
on population and
economic production
-Inquiry
-Discussion
-Discovery
-Critical
thinking
-Self
awareness
-Discussing the
effects of HIV
on population
and economic
production
School
neighbourh
ood
Ecolebooks.com
DOWNLOAD MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
9 1
Uganda as an Independent nation
Democracy
-Explaining
terms used in
democracy
and related
words like
-Elections
-Polling
stations
-Bullot box&
paper
-polling
assistant
-Pronounce,
read and
spell words
related to
democracy
Revision work
• Democracy
• Meaning
• Importance
• Functions
• How
democracy is
practiced
• Challenges of
democracy
• Elections
• How
elections are
conducted
-Explanation
-Discussion
-Inquiry
-Question
and answer
-Discovery
-Testing
-Observation
-Drawing
-Critical
thinking
-Sharing
-Appreciation
-Answering
written
exercises
-Discussion
-Pictures
and
photograph
s of people
voting
MK
stdbk 5
pg 117-
150
9 2
Government of Uganda
-Explaining
taxation,
budget and
their types
- Taxation
- Budget
- Loans
- Expendit
ure
- Income
- Revenue
• Bad practices
in elections
• Electoral
commission
and its
functions.
• Taxation
• Types of
taxes
• Ways how
the
government
spends its
revenue
• Budget
• Types of
budget
Pictures of
different
types of
budgets
MK bk 5
pg 140-
141
</passage>

<passage id="lchk_de8fddce4e9d4f858bcd933118db47b3" source="Primary Five Social Studies Scheme of Work" part="7">
 Customs duty
 Exercise duty
Definition of a
budget
Parts of the budget
Definition of the
national budget
Reasons for
budgeting
Sources of
government
revenue
Types of taxes
Ways how the
government spends
its revenue
Problems faced
during collection of
taxes
Dangers of
smuggling
122 – 127
Page 14
Population
size and
distribution in
Uganda and
their
relationship
to economic
planning and
development
Terms related
to population
 By the end of all
lessons the children
should be able to
 Define all the terms
related to population
 Population
 Population
census
 National
population
census
 Enumerators
 Population
growth
 Population
distribution
 Population
explosion
 Sparse
population
 Dense
population
 Optimum
population
 Over population
 Census night
 Under
population
Writing
Reading
Answering
oral
questions
Chalkboard
Atlas
Text book
MK bk 5 pg 148
Population
size and
distribution
Population
census
Should
 Identify reasons why
population census is
conducted
 Identify information
collected during
census
 State the problem
faced during census
 Identify the ministry
responsible for
census
 Reasons why
census is
conducted
Information
collected from
people during
census
Problems the
government faces
during census
Ministry
responsible for
conducting
population census
Answering
oral
questions
151
Factors
affecting
population
distribution
 Should be able to
 Identify the factors
affecting population
distribution
 Identify factors that
attract people in an
area
 Sparse
 Dense
Factors affecting
population
distribution
Factors that attract
people in an area
Reasons why some
areas are densely
Text book
And atlas
Pg 141
Page 15
 State reasons why
some areas are
sparsely populated
 State reasons why
some areas are
densely populated
populated
Reasons why some
areas are sparsely
populated
Population
growth
 Should be able to
 Identify the factors
affecting population
growth
 State the factors that
lead to high
population growth
 State the causes of
high birth rate
 Ways of controlling
high birth rate
 Way of controlling
high population
growth
 Birth rate
 Family planning
Factors affecting
population growth
Factors that can
lead to high
population growth
Causes of high
birth rate
Ways of controlling
high birth rate
Ways of controlling
high population
growth rate
Text book
And
Atlas
Pg 151
Advantages
and
disadvantages
of a large
population
Advantages
and
disadvantages
of small
population
 Should be able to
 Identify the economic
advantages of a
large population
 Identify the
disadvantages of
large population
 State the advantages
of a small population
 Identify the
disadvantages of a
small population
 Economic
advantages of a
large population
Disadvantages of a
large population
Advantages of a
small population
Disadvantages of a
small population
Writing
Answering
oral
questions
Text books
and atlas
Population
size and
distribution
Hazards that
check on
population
growth
 Should be able to
 Identify the natural
hazards that check
on population
growth
 Identify the
manmade disaster
that check on
population growth
 Hazards Natural hazards
that check on
population growth
Manmade hazards
that check on
population growth
Text books
Page 16
Effects of HIV
/ AIDS on the
population
 Mentions the social
and economic
effects of HIV /
AIDS on the people.
 Discusses the
effects of HIV /
AIDS in society.
Economic and
social effects of
HIV / AIDS.
</passage>

<passage id="lchk_a89f8a96f35c42f7a1dee9e9583a10c8" source="Excel P 5 SST Term III" part="26">
❖ It promotes proper utilisation of resources in
an area.
Problems associated/ caused with a High
population density.
• Unemployment.
• Shortage of food.
• Easy spread of communicable diseases.
• Development of slums.
• Poor hygienic condition leading to disease outbreak.
• Environmental degredation.
• High crime rate.
Solutions to problems associated with a High population density.
❖ People in urban areas should build storeyed buildings to solve a problem of land
shortage.
❖ Government should provide better social services in rural areas to promote urban-
rural migration.
❖ Empowering the youths to start small scale businesses (projects).
❖ By extending electricity to rural areas.
❖ Educating people to use modern methods of farming to increase food production.
b) LOW POPULATION DENSITY.
This is when an area has a small number of people compared to the available
resources .
Advantages of a low population density .
• People have enough land.
• Low crime rate.
• There is enough accommodation.
• It promotes conservation of the
natural environment in an area.
• Communicable diseases can not easily spread from one homestead to another.
Disadvantages of a low population density.
• There is low market for local goods or imported goods.
• There is low labour force.
• There is low tax base for the government.
Storeyed houses can help to solve
shortage of land in towns
Page 48
• There is poor social service provision.
• There is limited social security.
• There is under utilisation of resources in an area.
Solutions to a low population census.
• By improving social services to attract more people.
• By setting up industries in an area.
• By encouraging mechanisation to increase food production.
• By encouraging people to marry many wives.
EFFECTS OF HIV/AIDS ON POPULATION.
HIV stands for Human Immunodeficiency Virus.
AIDS stands for Acquired Immune Deficiency Syndrome.
AIDS patients are people who suffer from AIDS.
AIDS patients in Uganda are cared for by The AIDS Support Organisation
(TASO).
How TASO helps AIDS patients.
❖ It provides them with counselling services.
❖ It provides them with Anti-Retroviral drugs (ARVs)
❖ It provides relief aid in terms of food.
How AIDS is spread.
❖ By sharing sharp objects with an infected person.
❖ Contact of wounds with blood of an infected person.
❖ Having unprotected sexual intercourse with an infected person.
❖ Using unsterilised sharp objects during some cultural practices like circumcision.
❖ Through blood transfusion with an infected person.
Use of ABC to prevent AIDS.
• A=Abstain from sex (to unmarried people)
• B=Be faithful to your partner (to married couples)
• C=Condom use.
Social effects of HIV/AIDS on the population.
❖ It leads to death of people.
❖ It causes misery to the infected person.
❖ It leads to isolation.
❖ It leads to many orphans due to deth of the parents.
Economic effects of HIV/AIDS on population.
❖ It leads to loss of efficiency at work.
❖ It leads low labour supply due to death of many people.
❖ It leads to poverty in a family as a result of overspending on drugs treating those
infected.
❖ It leads to low market for goods due to death of many people.
Page 49
Testing Exercise.
1. Give the meaning of each of the following;
(i) Population
(ii) Population growth
2. Give any three causes of high population growth in Uganda.
3. State any two advantages of a high population in an area.
4. Mention any two problems an area is likely to face as a result of having a large population.
</passage>

<passage id="lchk_a8bf4b84729e467e90e868625ca681a3" source="Primary 5 Social Studies Scheme of Work, Term III" part="6">
Examples of densely populated areas
Examples of sparsely populated areas
Subject
The learner
Gives the meaning of population
distribution
Identifies the factors influencing
population distribution in Uganda
Gives examples of densely
populated and sparsely populated
areas in Uganda.
Language
The learner pronounces, reads and
spells words with stress intonation
and fluency
Group work
Question and answer
Answering oral and
written questions
Effective
communication
Critical thinking
Responsibility
Co-operation
Visit to
Mukono
town
MK pupils SST book page ..., Atlases on population
distribution in Uganda
4
Population size and distribution of Uganda
Map work
The map of Uganda showing
population distribution in different
areas
Subject
The learner
Draws the map of Uganda
Indicates the areas with as dense
population
Shows areas with a sparse
population
Language
The learner pronounces, reads,
spells and writes words correctly for
example Dense, sparse e.t.c
Exhibition
Representation
Drawing the map Creative
thinking
Assertiveness
Drawn
map on
a chart
MK SST pupils book 5 page 177
5
Population size and distribution of Uganda
Population density
Meaning of population density
Developing a formula of calculating
population density
Calculating the population densities of
different places
Subject
The learner;
Gives the meaning of population
density
Calculates population density of
different places
Language
The learner, pronounces, reads,
spells and writes the words correctly
like density, calculate, explosion,
distribution
Guided discussion
Inquiry
Giving the meaning of
population density
Critical thinking
Co-operation
Text
book
reading
MK SST pupils book 5 page 182
8 1
Population size and distribution of Uganda
Population growth
Meaning of population growth
Factors responsible for population
growth
Advantages of a high population
Disadvantages of a high population
Ways of controlling population growth
Subject
The learner
Gives the meaning of population
growth
Identifies the factors responsible for
population growth
Gives the advantages and
disadvantages of low and a high
population.
Language
The learner reads, spells and writes
the following words correctly i.e.
sparse population, utilization,
infant,. Mortality e.t.c
Guided discussion
Inquiry
Answering oral and
written activities
Assertiveness
Self esteem
Responsibility
Love
Care
Chalkbo
ard
illustratio
n
MK Standard SST pupils book 5 page 179
2
Population size and distribution of Uganda
Low / sparse population
Meaning of a low / sparse / under
population
Advantages of low population
Disadvantages of low population
Ways how the government
Can deal with a past growing
population
Advantages of small family
Disadvantages of having
Subject
The learner;
Gives the meaning of low population
Writes the advantages of low
population
Language
The learner pronounces, reads,
spells and writes words correctly like
immigration, emigration, fertility rate.
Guided discussion Answering oral and
written activities
Love
Care
Sharing
Demonst
ration
Chalkbo
ard
illustratio
n
3
Population size and distribution of Uganda
Population census
Meaning of population census
National population census
The ministry responsible for conducting
a national census
The officials involved in the census
Reasons for carrying out population
census
Information collected during population
census
Problems faced during population
census
Reasons why population census take
long to be conducted
Subject
The learner;
Gives the meaning of population
</passage>

<passage id="lchk_7e914abcd1f34c67935e12ca2588d5ec" source="P.5 SST SCHEME TERM III 2019" part="5">
Page 142-143
2
Child labour
-Discussing and explaining the child labour and child rights.
-Child
-Labour
-Abuse
Child labour
-Definition
-Examples of children’s rights.
-Responsibilities of children.
-Ways how children’s rights are abused.
-Ways of controlling child labour
3
Population size and distribution
Population census
-Explaining population and population census.
-Discussing the reasons why the gov’t carries out the population census and problems encountered.
-spells, reads , pronounces and uses words related to
-population
-census
-enumerator
-census rights
Population
-Meaning
-Population census
-Reasons why the government carries out population census.
-Ministry responsible for population census.
-Problems in conducting population census.
-Discussion
-Illustration
-Question and answer
-Observation
-Planning
-Co-operation
-Interpretation
-Description
-Explaining what population and census means.
-Counting the number of children by sex, tribe and age.
-Pictures showing a census being carried out.
Mk std
Bk5
Pg 145
7
4
LIVING TOGETHER IN UGANDA
Population size and distribution
Population growth
-Defining population growth.
-Discussing factors influencing population growth.
-Reads , spell, pronounce and use words like growth .
-Immigration
-Fertile
Population growth.
-Definition
-Factors that influence population growth.
Climate
Fertility rate of woman
Immigration
Occupation
Food
Better health
Health service
Social service
Security and peace
-Ways how the above influence population growth.
-Dangers of fast population growth.
-Explanation
-Question and answer
-Discussion
-Description
-Inquiry
-Critical thinking
-Care
-Explaining what population size and number means.
-Discussing the factors that lead to population increase.
-Explain the danger of fast population growth.
-Text book
-Pictures
Mk stdbk 5
Page 148-149
5
Population Distribution
-Explaining population distribution.
-Discussing the factors affecting population distribution
-Pronounce, read , spell and use words like-urbanization
-Industrialization
-Medical services
Population Distribution
-Defining
-Factors affecting population distribution.
Urbanization
Industrialization
Medical services
Climate
Physical features.
-Discussion
-Explanation
-Question and answer
-Appreciation
-Observation
-Map reading
-Sharing
-Respect
-Discussing how the factors affect the population distribution
-School
-neighborhood
-Pictures and photograph
Mk std
Bk 5
Pg 145-147
8
1
&
2
LIVING TOGETHER IN UGANDA
Population size and distribution
Population Density
-Explaining population density and high population density
-Density
-Square
kilometer
Population density
-Definition
-Method of calculation
Popn density=No of pple
Sq k/m
-High population density
-Low population density
-Illustration
-Explanation
-Question and answer
-Observation
-Appreciation
-Critical thinking
-Discussing the high and how population density
-Calculating population density
-Chalkboard illustration
Functional
Bk 5
Page 198
3
&
4
Population
-Discussing the problems associated to high and low population.
-Pronounce , read , spell and use words related to population.
-Advantages and disadvantages of high population (social factors)
-Problems associated with low population.
-Solutions to high population density and ways of controlling population growth.
-Explanation
-Discussion
-Question and answer
-Critical thinking
-Inquiry and answer
-Discussing the problems associated with high and law population.
</passage>

<passage id="lchk_7682272c0fdb4b93a290837e483bcf34" source="P.5 SST SCHEME TERM III 2019" part="6">
-Discussing the solutions to the high population density and ways of controlling population growth.
-Discussing the effects of HIV on population and economic production
- An Atlas
-School environment
School neighbourhood
Function
Bk 5
Pg 198-199
Mk std
Bk 5
Pg 148
8
5
LIVING TOGETHER IN UGANDA
Effects of HIV / AIDs on population and economic development
-Discussing the effects of HIV/ AIDS on population and economic production
-HIV
-AID
-Economic
-Production
Effects of HIV / AIDS on population and economic production
-Inquiry
-Discussion
-Discovery
-Critical thinking
-Self awareness
-Discussing the effects of HIV on population and economic production
School neighbourhood
9
1
Uganda as an Independent nation
Democracy
-Explaining terms used in democracy and related words like
-Elections
-Polling stations
-Bullot box& paper
-polling assistant
-Pronounce, read and spell words related to democracy
Revision work
Democracy
Meaning
Importance
Functions
How democracy is practiced
Challenges of democracy
Elections
How elections are conducted
-Explanation
-Discussion
-Inquiry
-Question and answer
-Discovery
-Testing
-Observation
-Drawing
-Critical thinking
-Sharing
-Appreciation
-Answering written exercises
-Discussion
-Pictures and photographs of people voting
MK stdbk 5 pg 117-150
9
2
Government of Uganda
-Explaining taxation, budget and their types
Taxation
Budget
Loans
Expenditure
Income
Revenue
Bad practices in elections
Electoral commission and its functions.
Taxation
Types of taxes
Ways how the government spends its revenue
Budget
Types of budget
Pictures of different types of budgets
MK bk 5 pg 140-141
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
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
