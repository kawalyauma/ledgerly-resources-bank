# Job ltsk_e0675dc1ae534fffbae03d23a2354164-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 5 lesson(s) below of week 8 of the Social Studies scheme for Primary Five 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P5: one 40-minute lesson: 3–4 ideas; 300–500 words; connected explanations and application; 5–8 activities.

lessonId=lles_91ebe7a2cab8447a9f82e828eea5d791: lesson 36, Monday, 1 period(s), 40 minutes.
  Unit: Population, Size and Distribution (theme: Living together in Uganda). Lesson: Practice: calculating population density — Population density.
  Objectives: Calculate the population density of places from given figures.
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points (numbered, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

lessonId=lles_b268d2c1ef994c3e8dd3361ea4df43ec: lesson 37, Tuesday, 1 period(s), 40 minutes.
  Unit: Population, Size and Distribution (theme: Living together in Uganda). Lesson: High population density: advantages and problems — High population density.
  Objectives: Explain high population density and name areas with it.; State the advantages of high population density.; State the problems associated with high population density.

lessonId=lles_4696fba35a244ef3abdd7cf74d8fa684: lesson 38, Wednesday, 1 period(s), 40 minutes.
  Unit: Population, Size and Distribution (theme: Living together in Uganda). Lesson: Solutions to problems of high population density — Solutions to high population density.
  Objectives: State solutions to the problems of high population density.; Explain how the government can deal with a fast growing population.

lessonId=lles_4aef6b6e793e4a91aecbcac2889dcddf: lesson 39, Thursday, 1 period(s), 40 minutes.
  Unit: Population, Size and Distribution (theme: Living together in Uganda). Lesson: Practice: high population density — High population density.
  Objectives: Answer exercise questions on high population density, its problems and solutions.; List the problems found in a crowded community such as a slum.
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points (numbered, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

lessonId=lles_8ddd49572447439caf046235db906564: lesson 40, Friday, 1 period(s), 40 minutes.
  Unit: Population, Size and Distribution (theme: Living together in Uganda). Lesson: Low population density: advantages, disadvantages and solutions — Low population density.
  Objectives: Explain low population density.; State advantages and disadvantages of low population density.; State solutions to low population.

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

<passage id="lchk_7c4fd5c6685b4ef5b553c7be3359c183" source="Excel P 5 SST Term III" part="22">
(iii) A Deficit budget.
48. Mention the two parts of a budget.
49. Name the government ministry responsible for making a national budget.
50. Mention the three types of budgets.
51. Give any two ways budgeting is important to an individual.
52. State any two ways a surplus budget is important to a family.
53. Mention any two causes of a deficit budget in a country.
54. State any two ways a deficit budget is dangerous to a family.
55. Give any two ways a country like Uganda can overcome a deficit budget.
56. Give the meaning of the term Citizenship.
57. Mention any two ways one can acquire citizenship of Uganda.
58. State any three obligations of a good citizen.
59. Give any one condition that can make one lose citizenship of Uganda.
60. What name is given to an official government document that permits one to travel to other
countries?
61. Give any two ways a National identity card is useful to the citizens of Uganda.
62. Why is food regarded to as a basic need?
63. State any three problems people face when getting their basic needs.
64. Mention any two forms of child abuse.
65. State any two causes for the increasing cases of child abuse in Uganda today.
66. Give any two ways children can contribute towards violation of their rights.
67. How is the LC I Vice-chairperson useful to children in your community?
68. Give any two ways cases of child abuse can be reduced in the society today.
69. Give the meaning of Human rights.
70. Mention any three examples of fundamental human rights.
71. Name the body that is responsible for protecting therights of the people of Uganda.
72. State one role a citizen can play to protect other people’s rights .
73. Give any two ways children are subjected to child labour in the society today.
74. Mention two ways child labour affects children in your community.
75. Give any one way child abuse practices can be reduced in our community today.
Page 41
TOPIC 12: POPULATION SIZE AND DISTRIBUTION.
.
Population is the total number of people living in an area at a given time .
Uganda has a population of over 45 million people according to the 2020 national
population census statistics.
Population distribution is the way people are spread in an area.
Population growth is the increase in the number of people in an area.
Population explosion is the sudden increase in the number of people in an area.
Population census is the official counting of people in a country.
Population density is the number of people living in an area per square kilometre.
Population structure is the composition of people in terms of age and sex.
POPULATION GROWTH .
Population growth is an increase in the number of people in an area of a country.
Factors that encourage Population growth.
• High fertility rate among women.
• Improved medical services.
• Early marriages.
• Polygamous marriage.
• Availability of food.
• Improved security and peace.
• Unplanned family size.
• Immigration.
• Producing children for prestige.
• Refugee influx.
Cultural factors that promote population growth.
• Polygamy
• Producing children for prestige.
• Forced early marriages.
Advantages of population growth in an area.
❖ It creates a large market for goods produced in an area.
❖ It provides cheap labour force in an area.
❖ The government collects more taxes from the people in areas with a large
population.
❖ It leads to development of an area.
Disadvantages(dangers) of population growth.
</passage>

<passage id="lchk_f2bbe26a485b4f19a8d163a63cee3aef" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="20">
b)Why should a country have a national constitution?
5. Mention the two parts of a national budget.
6. Which government ministry is responsible for preparing the National Budget?
7. State the ways through government revenue get revenue.
8. Define
a. A balanced budget
b. A surplus budget
9. Outline advantages of a surplus budget.
10. Study the diagram below and answer questions that follows:
a) What time of budget is illustrated?
53
b) Give the reason for your answer in (a) above.
c) Give one disadvantage of the above type of budget.
11. What is the major source of government revenue?
Date Class Subject No. of pupils Time
P.5
TOPIC: Population size and distribution in Uganda
SUB –TOPIC: Population distribution
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic: population, distribution, fertility
Content: Population
What is population?
 Population is the total number of people living in an area.
Population distribution
 Population distributions the way people are spread in different areas of the country.
OR
 Population distribution is the differing number of people living in different areas.
Factors that affect population distribution
 Climate of the area.
 Fertility of the land.
 Social services
 Economic opportunities
a) Climate
 Areas that have a good climate attract a high population density
 Areas with poor climatic conditions are sparsely populated.
b) Soil fertility
 Areas that have fertile soils attract high population density to practice agriculture.
c) Social services
 Areas that have well developed social services like health , education, and transport
attract large population.
 People migrate to urban areas where social services are available.
54
How better health services lead to population increase
 Better health services lead to decreased death rates in an area.
 It increases fertility rate among women
d) Economic opportunities
 Economic opportunities refer to situations whereby people are able to work and earn
income.
 Economic opportunities lead to migration of people in search of employment in market
places, schools , industries , hospitals, banks, and hotels.
Examples of densely populated areas in Uganda
 Areas of Kisoro
 Areas of Kabale
 Areas around L. Victoria
 Areas around Mt. Elgon in Mbale and Kapchorwa , central, Eastern and western regions)
Areas which are sparsely populated (have few people)
 North Eastern Uganda (Karamoja due to poor climate)
 Northern Uganda due to poor climate and insecurity
Reasons why dry areas have few people
 There is scarcity of food in dry areas.
 There is scarcity of water in dry areas.
 People migrate from dry areas to places with reliable rainfall.
How does industrialization affect the population of an area?
 people come from other areas to look for jobs in industries
A map of Uganda showing population distribution
55
Activity
1. Define the following terms:
a) Population
b) Population distribution
2. Point out two factors that affect population distribution.
3. Give two reasons why some places have many people than others.
4. Explain how each of the factors below affect population of a place
a) Urbanization
b) Soil fertility
c) Physical features
d) Medical services
Date Class Subject No. of pupils Time
P.5
TOPIC: Population size and distribution in Uganda
SUB –TOPIC: Population density
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic:
- Kilometer
- Square
- Growth
- sudden
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

<passage id="lchk_5cb1ddb635cb41eaa8e64a34bbd7172a" source="P.5 Social Studies and Religious Education End of Term III Exam 2023 – Smile Education" part="1">
WHAT’S APP: +256779680288 1
SMILE EDUCATION CONSULTACY BUSUNJU
P. 5 End of Term III Examination 2023
Social Studies and Religious Education.
Time allowed: 2 hours and 15 minutes
Name: __________________________________________________________
SECTION A: (40 marks)
1. Name the element of a map that enables map-readers to tell what a map is about.
______________________________________________________________________
2. What was the main reason for the coming of European explorers to Uganda?
______________________________________________________________________
3. State one way swamps are economically important.
_____________________________________________________________________
_____________________________________________________________________
4. Name the first Indian to open up a sugar factory in Uganda in 1924.
______________________________________________________________________
5. How is Mt. Rwenzori similar to the rift valley in terms of formation?
______________________________________________________________________
______________________________________________________________________
6. How did the pastoralists like the Iteso benefit from the neighbouring Bantu?
______________________________________________________________________
______________________________________________________________________
7. What type of climate is experienced in most parts of Uganda?
______________________________________________________________________
8. How was Kabaka Muteesa I responsible for the coming of Christian missionaries to
Uganda?
______________________________________________________________________
______________________________________________________________________
9. Name the first mission hospital to be opened in Uganda.
______________________________________________________________________
WHAT’S APP: +256779680288 2
10. Give any one-problem caused by a high population to the environment.
______________________________________________________________________
______________________________________________________________________
11. Write IBEACO in full.
______________________________________________________________________
12. What is the direction of Uganda from Kenya?
_____________________________________________________________________
13. The arrow of a wind vane is pointing to the north. To which direction is the wind
blowing?
_____________________________________________________________________
14. Why did Henry Morton Stanley call Mountain Rwenzori the ‘the Mountains of the
Moon’?
______________________________________________________________________
______________________________________________________________________
15. Name the agreement that was signed with the British colonialists to allow Kabaka
Muteesa II to return from exile.
______________________________________________________________________
16. State any one way river Nile has contributed to the development of industries in
Uganda.
______________________________________________________________________
______________________________________________________________________
17. Mention any one natural disaster that led to the collapse of Bunyoro Kitara kingdom.
______________________________________________________________________
18. Name the last colonial flag to be raised in Uganda.
______________________________________________________________________
19. What title is given to the political head of a district?
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
