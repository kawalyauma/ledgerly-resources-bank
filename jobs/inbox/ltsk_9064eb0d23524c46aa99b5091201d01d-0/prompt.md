# Job ltsk_9064eb0d23524c46aa99b5091201d01d-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 5 lesson(s) below of week 7 of the Social Studies scheme for Primary Five 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P5: one 40-minute lesson: 3–4 ideas; 300–500 words; connected explanations and application; 5–8 activities.

lessonId=lles_49060655929c411baa89e1e6b326898e: lesson 31, Monday, 1 period(s), 40 minutes.
  Unit: Population, Size and Distribution (theme: Living together in Uganda). Lesson: Population distribution and the factors that influence it — Population distribution.
  Objectives: Explain what population distribution means.; State the factors that influence population distribution.; Explain how each factor influences where people live.

lessonId=lles_585f0fad7b76424aa251245c4d8128eb: lesson 32, Tuesday, 1 period(s), 40 minutes.
  Unit: Population, Size and Distribution (theme: Living together in Uganda). Lesson: Densely populated areas of Uganda — Population distribution.
  Objectives: Explain what dense population means.; Name densely populated areas in Uganda.; Give reasons why these areas have many people.

lessonId=lles_47445f22fff745c89b31314ed3b9a101: lesson 33, Wednesday, 1 period(s), 40 minutes.
  Unit: Population, Size and Distribution (theme: Living together in Uganda). Lesson: Sparsely populated areas of Uganda — Population distribution.
  Objectives: Explain what sparse population means.; Name sparsely populated areas in Uganda.; Give reasons why these areas have few people.

lessonId=lles_ce6e37ac483541e192bca33e8acc0c04: lesson 34, Thursday, 1 period(s), 40 minutes.
  Unit: Population, Size and Distribution (theme: Living together in Uganda). Lesson: Practice: population distribution — Population distribution.
  Objectives: Answer exercise questions on population distribution and densely and sparsely populated areas.
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points (numbered, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

lessonId=lles_37f5f8212f0c4e4487d30455ba0a8a82: lesson 35, Friday, 1 period(s), 40 minutes.
  Unit: Population, Size and Distribution (theme: Living together in Uganda). Lesson: Population density — Population density.
  Objectives: Explain what population density means.; Calculate the population density of an area.

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

<passage id="lchk_91e897c1be5f461ab3bbc9443993f48c" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="23">
Reason why national population census is carried out every after ten years
 It is very costly
 The period is long enough for population changes to be assessed.
Activity
1. Give the difference between population census and national population census.
2. Give two reasons why the government of Uganda carries out national populaiton census.
3. Name the body that carries out national population census.
4. Which ministry carries out national population census?
5. What is population structure?
6. Why is population census carried out every after ten years?
7. Write short notes on the following terms
a) Census night
b) Enumerators
8. What information is passed to the people during the census night?
Date Class Subject No. of pupils Time
P.5
62
TOPIC: Population size and distribution in Uganda
SUB –TOPIC: Population terms
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic:
Content: POPULATION TERMS ( SUMMARY)
a) Population
 Population is the total number of people living in an area.
b) Population density
 Population density is the number of people living in an area per square kilometer.
c) Optimum population
 This is when the number of people in an a area is equal to the available resources.
d) Population census
 Population census is the general counting of people in an a area.
e) Under Population
 This is when the number of people living in an area is smaller than available resources.
f) Over Population
 This is when the number of people living in an area is greater (more) than the available
resources.
g) Population structure
 Population structure refers to the composition of the population in terms of age and sex.
h) Population growth
 Population growth is the increase in the number of people living in an area. .
i) Census night
 This is the night before the census is carried out.
j) Population explosion
 This is the sudden increase in the number of people living in an area.
k) Dense Population
 This is when the number of people living in an area is bigger compared to the size of the
land.
l) Sparse Population
 This is when the numbers of people in an area is smaller compared to the size of the land.
Topical test on population, size and distribution
1. What is population?
63
2. State two reasons why government conducts population census.
3. Which ministry is responsible for carrying out population census?
4. Give two factors that affect population distribution
5. Why are do some areas have high population?
6. Identify two dangers of a fast growing population to a country like Uganda.
7. Give advantages of a low population to a country.
8. a) What is family planning?
b) Why is family planning encouraged in Uganda?
9. Identify two reasons why Karamoja sub-region is sparsely populated.
10. a) What do we call the night before census?
b) Give two problems government faces during census.
11. Give the meanings of;
a. Population density
b. Population distribution
</passage>

<passage id="lchk_92d8ba79ca2b4c63b4ccd273d6a95ebd" source="Excel P 5 SST Term III" part="27">
5. Give any two economic benefits of a large population to the development of a country.
6. Mention any three natural disasters that may lead to the reduction in the number of
people in an area.
7. Name the body that is responsible for conducting a national census in Uganda.
8. Mention any three types of information that is collected by enumerators during the
census.
9. Which ministry is responsible for conducting a national census in Uganda?
10. Give any one reason why a national census in Uganda is conducted after ten years.
11. State any three reasons why the government conducts a national census.
12. Mention any three problems faced by the enumerators during the census exercise.
13. Why is population census in Uganda conducted after ten years?
14. State any three problems the government faces when conducting a national population
census.
15. Give the meaning of Population distribution.
16. Mention any three factors that influence population distribution.
17. Give one reason why steep slopes of mountains are sparsely populated.
18. Mention any three factors that lead to a sparse population in an area.
19. State any one two reasons why slopes of most mountains in East Africa are densely
populated.
20. Why are there many people living around the shores of lake Victoria?
21. Mention any three examples of sparsely populated areas in East Africa.
22. Why is the North Eastern part of Uganda sparsely populated?
23. Give the meaning of Population density.
24. Which East African country has the biggest population density?
25. Calculate the population density of town W which has a population of 4500 people living in
an area of 90km 2 .
26. Give one way the government can encourage the settlement of people in rural areas.
27. What is Population structure?
28. Give any two ways TASO helps AIDS victims in Uganda.
29. How can married people safeguard themselves against AIDS?
30. State any two ways HIV/ AIDS affects economic development in an area.
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

<passage id="lchk_f68ad912b104484b8b665e3e19a53590" source="NCDC P5 Merged – Social Studies" part="24">
increase such as improved diet, immigration, polygamy, low death
rates, improved medical care, early marriages.

Lesson 3:
Factors that influence population distribution.
You will be able to;
i) State the meaning of population distribution.
ii) Identify the factors that influence population distribution.
iii) Locate areas on a map of Uganda with large and small population.
Materilas you will need:
A pen, pencil, note book, P.5 S.ST text book (if possible)
Instructions:
You will need to get help from an adult to find out why some areas have
many people while others few. Use the neighbouring villages or homes;
take note of the ways houses are near or far from each other.
Introduction:
In this lesson, you are going to look at why some districts have more peo-
ple than others. Urban areas have more people than rural areas. You will
also be able to find out the areas in Uganda with large and small popula-
tion.
Procedure:
Step I:
Write the meaning of population distribution. Let an elder brother or sis-
ter to help you to find out the places in your local area with many and few
people. Ask him/her why the number of people in those areas is different.
Step II:
Identify the factors that influence population distribution.
Population distribution is the way people are settled in an area or coun-
try.
This differs from place to place. Some areas have many people while oth-
ers few . This means that some areas are densely populated while others
are sparsely populated. The factors that influence population distribu-
tion include; climate of an area, presence of soil fertility, the nature of
relief, presence pests and diseases.

SOCIAL STUDIES | PRIMARY FIVE

Activity:
1. Give the meaning of population distribution.
2. Mention places in Uganda that have a very high population.
3. Give factors that make the shores of Lake Victoria to have many peo-
ple.
4. Identify the type of work people in villages do.
5. State factors that influence population distribution.

National Curriculum
Development Centre,
P.O. Box 7002,
Kampala.

www.ncdc.go.ug
</passage>

<passage id="lchk_89377846af3241ba84ea0652b03431af" source="NCDC P5 Merged – Social Studies" part="23">
Population is the number of people in a given area. home, village, dis-
trict ,region ,country, . Census is the official counting of people living in a
country. The national population census is carried out after every ten (10)
years. This is done by people known as Enumerators. Step II: List the
information collected during census.
Step III: State the importance of population census.
Enumerators are trained people who move from home to home counting
people. During census, they collect the following information; Names of
family members, sex, education level of people in a family, age, occupation
and relationship with the head of the family, religion, and number of
children.

Step IV: Identify the problems faced during population census.

SELF-STUDY LEARNING

Importance of population census.
• To plan for the country.
• To know the number of people.
• To know the death rate.
• To know the birth rate.

Problems faced during population census
• Insecurity in some areas. | -
• Poor transport especially in highland areas.
• Bad weather conditions especially if it is a rainy season.
• People give wrong information.
Activity:
1. …………………………. is the number of people in a given area.
2. Give the meaning of population census.
3. After how long is population census carried out in Uganda?
4. State any three reasons why the government counts people.
5. Identify problems faced during population census.
Lesson 2: Influence of population growth on communities.
You will be able to;
i) Give the meaning of population growth.
ii) Mention the factors that influence population growth.
iii) Outline the effects of population growth.
iv) Identify the ways of controlling population growth.
Materials you will need: a pen, pencil, note book, P.5 S.ST text book (if
possible)
Introduction:
In this lesson, you are now going to study about the meaning of popula-
tion growth, factors that influence population growth, effects of popula-
tion growth and ways of controlling population growth.
Procedure:
Step I:

SOCIAL STUDIES | PRIMARY FIVE

Find out from an adult how the number of people at your community in-
creased. This is population growth.
Step II:
Now you can learn about the factors that influence population growth.
Availability of food. Once a lot of food is available, the number of people
will grow because they do not starve neither die of hunger.
Presence of better social services like health and clean piped water often
allow
many people to survive because diseases are minimised.
Ignorance about family planning services also leads to population in-
crease. High fertility rate among women also leads to population growth.
Step III:
Outline the effects of population growth in a country.
Negative effects of population growth.
• | It leads to unemployment.
• | It leads to high crime rate.
• | It leads to shortage of land.
• | It leads to environment destruction.
Positive effects of population growth.
• Leads to high tax collection.
• Provides enough labour force.
Ways of controlling population
• Encouraging use of family planning methods.
• Discouraging early marriages.
• Discouraging polygamy.
Activity:
1. Write down;
a) The causes of large families.
b) The dangers of large families.
2. What is population growth?
3. State any three ways in which government of Uganda can control popu-
lation growth.

Summary
Population growth is the increase in the number of people in a coun-
try or area. There are many factors that make the number of people

SELF-STUDY LEARNING
</passage>

<passage id="lchk_b532d3c1e8be45d5bfa157ec2d63678b" source="Primary 5 Social Studies Scheme of Work, Term III" part="7">
census
Identifies the ministry responsible
for conducting a national census
States the reasons why the national
census is conducted
Gives the problems faced by
enumerators
Language
The learner pronounces, spells,
reads and writes words correctly like
enumerator, census, teenage,
teenager, occupation, sex e.t.c.
Guided discussion
Inquiry
Answering oral and
written activities
Assertiveness
Critical thinking
Co-operation
Text
books
MK Standard SST pupils book 5 page 177
4
Population size and distribution of Uganda
Population explosion
Meaning of population explosion
Causes of population explosion
Effects of population explosion
Man-made factors which affect
population growth in an area.
Natural factors which affect
Landslides floods, earth quake,
volcanic eruptions
Subject
The learner
Gives the meaning of population
explosion
Identifies the causes of population
explosion
States the manmade and natural
factors that u check on population
explosion
Language
The learner pronounces, reads,
spells and writes words correctly like
landslides, wars, earthquake,
volcanic, eruption, diseases
Case study Giving the meaning of
population explosion
Giving the meaning of
population explosion
Writing the causes of
population
Responsible
living in the
environment
Text
book
reading
MK SST pupils book 5 page ...
5
Population size and distribution of Uganda
Summary of population terms
Population
Population distribution
Population increase
Population growth
Population density
Over population
Under population
Optimum population
Sparsely populated areas
Densely populated areas
Population structure
Population explosion
Population census
Census night
Dense population
Sparse population
Subject
The learner gives the meaning of
the population terms effectively
Language competences
The learner pronounces, spells ,
reads and writes words related to
population terms like distribution,
increase, growth, density e.t.c.
Guided discussion
Guided discovery
Giving the meaning of
the terms related to
population
Spelling different
words
Answering written
assignments
Critical and
creative
thinking
Chalk
board
illustratio
n
Teacher’s collection
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
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
