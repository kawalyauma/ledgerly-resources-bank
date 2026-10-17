# Job ltsk_9d047f5608954a5cb2b62f5352c6f979-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 5 lesson(s) below of week 1 of the Social Studies scheme for Primary Seven 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P7: one 40-minute lesson: 3–6 sections; about 18–36 points; concise candidate-level points, worked examples and exam tips; 6–10 activities.

lessonId=lles_8c09ac95dd1e4a87b38af9f548f928d4: lesson 1, Monday, 1 period(s), 40 minutes.
  Unit: Economic Developments in Africa (theme: Living together in Africa). Lesson: Major economic resources of Africa — Major economic resources of Africa.
  Objectives: Identify and describe major economic resources of africa.

lessonId=lles_9c27f9fa4ea047169f971e27e8225c3c: lesson 2, Tuesday, 1 period(s), 40 minutes.
  Unit: Economic Developments in Africa (theme: Living together in Africa). Lesson: Land and soil resources — Land and soil resources.
  Objectives: Identify and describe land and soil resources.

lessonId=lles_a5189fe111cb4d19bcfc773e34147557: lesson 3, Wednesday, 1 period(s), 40 minutes.
  Unit: Economic Developments in Africa (theme: Living together in Africa). Lesson: Mineral resources — Mineral resources.
  Objectives: Identify and describe mineral resources.

lessonId=lles_4c60b10e375147859a0438631099197e: lesson 4, Thursday, 1 period(s), 40 minutes.
  Unit: Economic Developments in Africa (theme: Living together in Africa). Lesson: Animals as resources — Animals as resources.
  Objectives: Identify and describe animals as resources.

lessonId=lles_2f6d4e7be3064d3fb0bff1b3d4827a0a: lesson 5, Friday, 1 period(s), 40 minutes.
  Unit: Economic Developments in Africa (theme: Living together in Africa). Lesson: People as resources — People as resources.
  Objectives: Identify and describe people as resources.

Write, using ONLY the passages below. Passages from "NCDC" documents are the official base for what to teach; NCDC lower-primary thematic curricula put every learning area in columns separated by " | ": use only the Social Studies column.
For EACH lesson:
- notes: the CHALKBOARD NOTES the teacher writes on the board for learners to copy into their exercise books, in Markdown, at exactly this class level.
  Use the detailed notes in the passages as the factual base, not merely the short scheme wording.
  Learner-facing CONTENT ONLY. Never write instructions or activities in the notes: no 'discuss', 'in your groups', 'tell the story', 'sing', 'act out', 'read with your teacher', 'say aloud', 'think of'. Those go in methods.
  Write the content itself: state the facts, meanings, examples and lists. For a Bible or Quran passage, give the reference AND what it says or teaches in one short point (not 'read John 8:12').
  HOUSE STYLE: POINT FORM, like a good Ugandan pupil's notebook. NO PARAGRAPHS. Every content line is a short point starting with '- ': one fact per point, about 3 to 15 words, in the passages' own wording.
    A meaning is a point too ('- Altitude is the height above the sea level.'). Lists of names are one name per point with no explanation ('- Mbale', '- Kapchorwa').
    Never pad or link points: no 'This shows…', 'These help…', 'In the supplied notes…', 'according to the passages', 'In this lesson…', no summary sentence at the end of a section. Shorten; never stretch.
  Structure:
    # TOPIC: <unit title in capitals>
    ## SUB-TOPIC: <lesson title>
    then sections, each under a ### heading in the usual notebook wording: ### <Thing> (its meaning), ### Examples of …, ### Reasons why …, ### Importance of …, ### Advantages of …, ### Disadvantages of …,
    ### Causes of …, ### Effects of …, ### Economic activities carried out in …, ### Problems faced by …, ### Possible solutions to the problems …, ### Ways of …, ### Duties/Roles of … (use whichever the passages support).
    ### Note at the end of the content: 2 to 5 key facts or exam tips from the passages that a learner must remember (e.g. '- Heavy rainfall is the major cause of landslides in highland areas.'). Leave it out when the passages give none.
    Bold only the key word being defined. Use a small Markdown table only for comparisons (e.g. organ of government | its work).
    Examples ('### Example 1', '### Example 2', ...) are ONLY for Mathematics, English and Reading: worked examples taken from the passages, set out step by step (each step on its own line). Other subjects have no Example sections.
    Write mathematics in LaTeX: $\frac{3}{4}$ inline, $$...$$ on its own line. Column sums and long division are coded diagrams, not LaTeX.
    When the curriculum names new words, list them once near the top as '### New words' followed by the words separated by commas (no tables, no pronunciation drills).
    End with '### Exercise': 3–8 numbered questions on this lesson, taken from the activities, for learners to answer in their books.
  Keep it board-sized: as much as a teacher writes in one lesson; no greetings, no 'In this lesson we will', no notes to the teacher.
  Where a matching past-paper question exists, use it as a worked example, an Activity, or a clearly marked 'NB / Exam practice' item; do not let an exam paper determine the curriculum order.
- methods: ONLY the names of the teaching methods, comma separated, for the scheme of work's Methods column (e.g. 'Story telling, Discussion, Guided Bible reading, Question and answer'). At most 6 names, no sentences.
- teachingGuide: the CLASS ACTIVITIES, step by step: what the teacher does and what learners do (discussion, group work, story telling, songs, dramatisation, guided Bible/Quran reading, oral work, drawing, games), as given or implied in the passages. Everything taken out of the notes because it is an instruction goes here.
- materials, lifeSkills, assessment: as given or implied in the passages; null when the passages are silent.
- lessonPlan: a COMPLETE lesson plan in the Ugandan format that a head teacher or supervisor would accept, written from this lesson's notes:
  competences: 2-4 subject competences, each 'The learner ...' with a concrete verb (defines, names, explains, draws, calculates, locates) and this lesson's actual content.
  languageCompetence: the key words of the lesson learners pronounce, spell, read and write (name them).
  objectives: 2-4 measurable objectives ('By the end of the lesson, learners should be able to ...'), not copies of the competences.
  priorKnowledge: what learners already know that this lesson builds on (the previous lesson or everyday experience), in one or two sentences.
  methods: at least 3 method names. materials: at least 2 specific teaching aids (e.g. 'chart of the three arms of government', not only 'chalkboard'). references: the source titles, with page numbers when the passages give them.
  steps: 4-7 steps whose minutes add up exactly to the lesson's minutes: Introduction (how the teacher links to prior knowledge, with the starter question asked); one Lesson development step for each notes section (or two small sections together); a Practice / Exercise step; and a Conclusion (summary and evaluation).
  Every step has: stage; minutes; content = the exact points taught or written on the board in that step, taken from the notes; teacherActivity = what the teacher does and says in 2-4 sentences, quoting the actual questions asked and the examples used; learnerActivity = what learners do in 1-3 sentences (answer, copy, discuss in pairs, draw, read aloud, demonstrate, act).
  Never write generic steps such as 'Explain key terms', 'Give questions' or 'Review the lesson': name the terms, quote the questions, say what is reviewed.
  assessment: how learning is checked, listing at least 3 actual oral or written questions (from the notes' Exercise). homework: one specific task. lifeSkills: 2-4 life skills and values shown in the lesson.
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
{"lessons":[{"lessonId":string,"notes":string,"methods":string|null,"teachingGuide":string|null,"materials":string|null,"lifeSkills":string|null,"assessment":string|null,"sourcePassageIds":[string],"lessonPlan":{"competences":[string],"languageCompetence":string|null,"objectives":[string],"priorKnowledge":string|null,"methods":[string],"materials":[string],"references":[string],"steps":[{"stage":string,"minutes":int,"content":string,"teacherActivity":string,"learnerActivity":string}],"assessment":string|null,"homework":string|null,"lifeSkills":[string]},"diagrams":[{"key":string,"title":string,"caption":string|null,"method":"illustration"|"coded"|"svg","concept":string|null,"parts":[string],"coded":object|null,"svg":string|null,"sourcePassageId":string|null}],"activities":[{"question":string,"answer":string|null,"options":[string]|null,"kind":string,"concept":string,"skill":string,"cognitiveLevel":string,"difficulty":1-5,"origin":"source"|"generated","sourcePassageId":string|null,"sourceQuote":string|null}],"gaps":[string]}]}

<passages>
<passage id="lchk_ff110c6b16684b4bbf56de29c7e48fff" source="NCDC PRIMARY SEVEN SET ONE – Social Studies" part="19">
• Discuss with the learners why Africans formed OAU.
• Explain the process through which OAU came into existence
and its aims.
• Guide learners to identify the economic groupings of Africa.
• Discuss with learners the reasons for formation of economic
groupings, their achievements and challenges.

Primary Seven Curriculum

• This topic has a lot of details in existing textbooks. Use maps,
charts newspapers, magazines and radios as sources of
information to teach this topic effectively. Read extensively to
get enough content.
• You are advised to teach this topic using the following methods
and techniques; question and answer, group discussions,
explanations, brainstorming and guided discovery.
Suggested Competences for Assessment
The learner:
• discusses why OAU was formed.
• draws the map of Africa showing OAU founder member
countries.
• states the achievements of OAU.
• discusses the challenges and failures of OAU.
• explains why the formation of AU was necessary.
• describes the organs of the AU.
• states the challenges of AU.
• suggests possible solutions to the challenges of the AU.
• names the different economic groupings in Africa.
• discusses advantages | and | disadvantages | of | economic
cooperation.

Term III

Topic 9: Economic Developments in
Africa | 30 Periods

Background
In the previous topic, the learner was introduced to the period of post
independent Africa and what happened during the years that followed
independence.

The learner learnt about the formation of OAU, which led to the
formation of economic groupings that are trying to promote the economic
development of Africa and subsequently the African Union which also
aims at developing Africa.

This topic covers economic developments in Africa, the natural resources
and their importance to economic development. These natural resources
include people, land, minerals, water, animals, vegetation, climate and
relief. The learner will be introduced to how these resources are used,
problems faced when utilising the resources and how they influence
development. Some African countries have been identified as case
studies. These include Nigeria, Uganda, Libya, Sudan, South Africa and
Democratic Republic of Congo. Each of these countries contributes to
the economic development of Africa. The case study countries represent
different regions of Africa.

Learning Outcome
The learner identifies and examines natural resources and their
importance in the economic development of Africa.

Life Skills
• Effective communication
• Creative thinking
• Critical thinking

National Curriculum Development Centre

SST Skills
• Drawing
• Observation
• Inquiry
• Reading
• Investigating
Values
• Appreciation
• Cooperation
• Care
• Respect
• Love

Primary Seven Curriculum

Subject | Language | Suggested
Content
Competences | Competences | Activities
The learner: | The learner | • Major economic | • Discussing
• identifies major | correctly uses the | resources: | major economic
economic | – Land and soils | resources of
following words
resources of | – Minerals | Africa
Africa and | related to the topic: | – Animals | • Drawing
explains how | – resource | – People | various maps
each contributes | – natural | – Vegetation | of Africa to
to economic | resources | – Climate | show where
development. | – Water | the economic
• discusses the | • Problems faced in | resources are
problems faced | the utilisation of | found
in the utilisation | resources | • Explaining
</passage>

<passage id="lchk_08b4203996574de4b3f2914bd9384c2c" source="NCDC PRIMARY SEVEN SET ONE – Social Studies" part="20">
of resources. | • Care for our | how people
• identifies ways | resources | use natural
of caring for our | resources
natural resources. | within their
environment to
develop
• Discussing
ways of caring
for our natural
resources
• Explaining
problems faced
in the utilisation
of resources
• identifies major | The learner correctly | • Major economic | • Identifying
economic | uses the following | development | major economic
developments | words related to the | in Africa (case | activities in case
in Africa (case | topic: | studies) | study countries
studies). | – drilling | a) Nigeria: | • Comparing
– nomadism | – Climate | economic
– irrigation | – Oil drilling | activities carried
– industrialisation | – Farming | out in case
– tourism | – Nomadism | study countries
– lumbering | – Hydro-electric | with Uganda
power project: | • Comparing
Kainji dam | Uganda’s
– Trade and | climate with
transport | that of the case
study countries

National Curriculum Development Centre

Subject | Language | Suggested
Content
Competences | Competences | Activities
• Libya: | • Comparing oil
– Climate | mining in Libya
– Oil mining | with that of
– Irrigation farming | Nigeria
– Industrialisation | • Discussing
– Tourism | the influence
of climate
on economic
activities in
the case study
countries
• Sudan:
– Climate
– Gezira Irrigation
Scheme
– Hydro-electric
power project
– The Nile Valley
• South Africa:
– Mining
– Farming
– Trade
– Tourism
– Industrialisation
• Democratic
Republic of
Congo:
– Climate
– Mining
– Lumbering
– Farming
• Uganda
– Climate
– Farming
– Mining
– Tourism
– Irrigation
schemes
– Pastoralism

Primary Seven Curriculum

Subject | Language | Suggested
Content
Competences | Competences | Activities
 identifies | The learner correctly | • Social challenges | • Writing
challenges | uses the following | such as: | problems
affecting | words related to the | – Illiteracy | affecting
economic | topic: | – Poverty | economic
developments | – poverty | – Ignorance | developments
in Africa | – ignorance | – Diseases | in Africa
and possible | – mortality | – High infant
solutions. | – teenage | maternal and
– contraceptive | mortality rate
– technology | – High fertility rate
– Teenage
pregnancies and
early marriages
– Low | • Discussing how
contraceptive use | communication
– Famine | is important in
• Economic | the economic
challenges: | development of
– Poor | Africa
transport and
communication | • Describing how
– No money/funds | electricity is
– Low level of | produced and
technology/ skills | its importance
– High dependency | to the
ratio | development of
– Unemployment | Africa
– Corruption
– Economic collapse
– Brain drain
• Political | • Discussing
challenges: | the political
– Wars, coups, | challenges faced
conflicts and | in Africa
violation of | • Mentioning
human rights | common
– Political | challenges in
instability | their lives and
– High numbers of | suggesting
refugees | solutions to
– Poor governance | them

National Curriculum Development Centre

Subject | Language | Suggested
Content
Competences | Competences | Activities
• discusses the | – Foreign | • Discussing
possible solutions | domination | the possible
to problems that | – Riots | solutions that
affect economic | • Possible solutions | affect economic
development in | development of
Africa. | Africa

Guidance to the Teacher
• Guide learners to describe the major economic resources in
Africa.
</passage>

<passage id="lchk_d2861670341541fc82e4b0a679a47bf0" source="NCDC PRIMARY SEVEN SET ONE – Social Studies" part="15">
• gives reasons why foreigners came to Africa.
• mentions groups of foreigners who came into Africa.
• names European countries that colonised Africa.
• draws the map of Africa showing sphere of influence.
• discusses problems faced by explorers.
• identifies the effects of European explorers.
• explains the causes of the Great Trek.
• discusses the effects of the Great Trek.
• discuses methods used by colonialists to acquire colonies.
• describes the methods used by colonialists to administer colonies.

Topic 7: Nationalism and the Road to
Independence of Africa
20 Periods

Background
In the previous topic, the learner was introduced to how foreigners came
to Africa, reasons for their coming, how they introduced colonial rule
and how the people reacted to colonial rule. They also learnt about how
the people of Uganda, Tanzania, Rwanda and Burundi and Kenya got
independence. In this topic, bring out the meaning of the terms “Pan-
Africanism” and “nationalism”.

Pan-Africanism is a feeling of uniting and promoting political, economic
and social interests of Africa. Nationalism is a deep love and pride for
one’s country. These movements spearheaded the struggle for Africa’s
independence.

Learning Outcomes
The learner demonstrates knowledge and appreciates the rights of an
individual, society and collective responsibility in bringing social justice,
and political order.

Life Skills
• Effective communication
• Self-awareness
• Self-esteem
• Assertiveness
SST Skills
• Reading
• Writing
• Analysing

Primary Seven Curriculum

Values
• Cooperation
• Love
• Respect
• Appreciation
Subject | Language | Content | Suggested
Competences | Competences | Activities
The learner: | The learner | • Meaning of pan- | • Discussing the
• discusses pan- | correctly uses the | Africanism, pan | meaning of
Africanism and | following words | – Africanists, | pan-Africanist,
nationalism. | related to the | nationalism, | nationalist,
• explains the | topic: | nationalists, | patriotism and
work of pan- | – nationalism | patriotism | nationalism.
Africanisists | – pan- | • The work of pan- | • Debating the
and nationalists. | Africanism | Africanists and | work of pan-
• identifies | – patriotism | nationalists | Africanists and
countries | – independence | • African countries that | why nationalists
that were not | – freedom | were not colonised: | succeeded
colonised in | – detention | Ethiopia and Liberia | in their
Africa. | • Reasons for | movements
• discusses | maintaining their | • Discussing
the reasons | independence | problems pan-
why Ethiopia | Africanists and
and Liberia | nationalists met
maintained | in their struggle
their
• Discussing
independence.
reasons why
Ethiopia and
Liberia were not
colonised
• discusses | The learner |  Reasons for | • Stating reasons
reasons why | correctly uses the | independence such | why Africans
Africans | following words | as to: | wanted
wanted | related to the | – control of national | independence
independence. | topic: | resources
– discrimination | – revive African | • Drawing a
– resources | culture/ | map of Africa
– oppression | independence | showing African
– equality | – stop exploitation by | independent
– dignity | former colonial rulers | countries and
– freedom | – regain land from | their former
European settlers | colonial masters

National Curriculum Development Centre

Subject | Language | Content | Suggested
Competences | Competences | Activities
– stop oppression
– desire for social
</passage>

<passage id="lchk_c8e10e5097074644ad353ff3556c7e2b" source="NCDC PRIMARY SEVEN SET ONE – Social Studies" part="1">
Social Studies Syllabus

Primary Seven Curriculum

Background
The P7 learner has gone through a variety of experiences on the physical
and social environments. By this time, the learner has been exposed to
living together in an expanding environment, starting with the familiar
ones such as a home, school, neighbourhood, sub-county, municipality,
district, Uganda and East Africa. The learner will now be exposed to the
rest of Africa, under the theme “Living together in Africa”.

A number of physical, social, political and economic aspects have been
covered to enhance the learners’ knowledge and skills on how human
beings interact with other living things to survive in different types of
environments.

Rationale
Social Studies (SST) is designed to equip the learners with knowledge,
skills, values and desired attitudes which are required to prepare them
for living in a physical, social, political and economic environment as
knowledgeable and as participating citizens of society. Primary Seven
SST competences are intended to prepare learners in their final year of
primary school education to higher academic levels. Learners will use
the knowledge, skills and values to interact with others from various
communities and backgrounds and this is why they should be exposed to
the wider community for a harmonious living.

Social Studies can provide learners with the skills for productive
problem-solving and decision-making, as well as for assessing issues
and making thoughtful value judgements. Above all, Social Studies helps
learners to integrate these skills and understandings into a framework for
responsible citizen participation, whether in their play group, the school,
the community or the world.

Social Studies content integrates knowledge, skills and attitudes within
and across disciplines. This helps learners to view and relate the concepts
of physical, social, political and economic factors which will enable them
cope with multiple perspectives in the dynamic world.

It is important for learners to begin to understand, appreciate and apply
knowledge, skills and values in other academic disciplines as a way of

National Curriculum Development Centre

disciplinary integration. Such interdisciplinary-based learning draws
simultaneously from several disciplines in clarifying specific concepts.
Social Studies addresses the contemporary conditions of real life and
academic scholarship.

Learning Outcomes
The following are the expected learning outcomes of the P7 SST learning
and teaching process:
1. | Promotes an appreciation of Africa as a continent, where our
own country exists.
2. | Demonstrates the usage of lines of latitudes and longitudes to
locate Africa, its regions and member countries.
3. | Explores, identifies and appreciates the value of one’s
immediate and distant environment for better and harmonious
living.
4. | Identifies and appreciates the importance of climate and how it
determines and supports human, animals and plant life.
5. | Appreciates the value of vegetation and endeavours to care for
it for better and harmonious living.
6. | Demonstrates and promotes values, social practices in the
society and shows respect for his/her own and other cultures.
7. | Identifies the importance of interdependence of nations and
continents.
8. | Demonstrates and explains the use of map reading skills,
interpretation and analysis of data.
9. | Demonstrates knowledge and appreciates the rights of
</passage>

<passage id="lchk_728e36b0120442d489e34403b0fba003" source="ALL SST NOTES P.4 TO P.7 ALL TERMS EXCEL 3" part="25">
4. Give the meaning of each of the following;
(i) A tributary
(ii) A river confluence
5. Mention any three major waterfalls in Uganda.
6. Give any two ways waterfalls are economically important to a country.
7. Mention the three stages of river development.
8. Give any four ways rivers are important to people in your community.
9. State any three problems caused by rivers in an area.
10. Which type of electricity is generated from fast flowing water?
General importance of physical features.
❖ Lakes and rivers are a source of fish.
❖ They help in the formation of rain.
❖ They are source of income through tourism.
❖ Lakes and rivers provide water for domestic use.
❖ Rivers help in the generation of Hydro Electric Power/ hydroelectricity.
❖ They act as recreation centres.
❖ Mountain slopes and lake shores have fertile soils which support crop
cultivation.
❖ Hills and mountains are used by telecommunication companies to place on masts.
❖ Some mountains are a source of rivers.
❖ Some physical features are a source of minerals eg.Osukuru hills in Tororo
which provide limestone.
❖ Mountains provide building materials eg.stones
❖ Lakes and rivers provide water for irrigation.
❖ They form natural boundaries between places/ districts.
Dangers of physical features
❖ Some of them are hiding for wrong doers
❖ They harbour dangerous wild animals
❖ They are bleeding places for disease vectors
Page 62
❖ Lakes and rivers flood which kills people.
❖ They hinder road construction.
❖ Mountains hinder agricultural mechanisation.
❖ Some mountains erupt and destroy property.
❖ Hills and mountains have steep slopes which promote soil erosion.
❖ Mountains are greatly affected by landslides. and soil erosion.
Ways of caring for the physical features
❖ BY Planting trees on shores of lakes and mountain slopes and river banks
❖ BY discouraging people from dumping rubbish in water bodies
❖ By terracing land to control soil erosion in highlands.
❖ By sensitising people about the importance of different physical features.
❖ By using proper fishing methods.
❖ By filling holes after mining.
❖ By treating wastes before disposing them in water bodies.
Testing Exercise
1. Write HEP in full.
2. How do lakes and rivers help to modify climate of an area?
3. Name the major mineral mined from Osukuru hills in Tororo.
4. Mention any one building material obtained from mountains.
5. Give one way physical features are politically important in the environment.
6. Give any three ways lakes and rivers are economically important.
7. State any two problems faced by people living near lakes and rivers.
8. Mention any two problems faced by people living in mountainous areas.
9. State any two ways lakes and rivers can be cared for.
10. Give one way mountains hinder economic development in an area.
Page 1
FIRST EDITION
BY
EXCEL PUBLISHERS
All rights reserved. No part of this publication may be reproduced, stored in a retrieval
system or transmitted in any form or by any means of electronic, mechanical,
photocopying, recording or otherwise, without the prior written permission of the
publisher.
Copyright © Excel publishers
Page 2
ACKNOWLEDGEMENT
Developing a book of this nature requires a lot of support from colleagues, friends
and family. I would like to register my deep-rooted gratitude to the following people
for their unlimited assistance offered towards the completion of this book.
All teachers of Social Studies in Victoria Mutundwe Primary School and Makindye
</passage>

<passage id="lchk_ea90bd16daed4f3a8d0daef89b79ef61" source="ALL SST Notes P 4 TO P 7 ALL Terms Excel Copy" part="25">
4. Give the meaning of each of the following;
(i) A tributary
(ii) A river confluence
5. Mention any three major waterfalls in Uganda.
6. Give any two ways waterfalls are economically important to a country.
7. Mention the three stages of river development.
8. Give any four ways rivers are important to people in your community.
9. State any three problems caused by rivers in an area.
10. Which type of electricity is generated from fast flowing water?
General importance of physical features.
❖ Lakes and rivers are a source of fish.
❖ They help in the formation of rain.
❖ They are source of income through tourism.
❖ Lakes and rivers provide water for domestic use.
❖ Rivers help in the generation of Hydro Electric Power/ hydroelectricity.
❖ They act as recreation centres.
❖ Mountain slopes and lake shores have fertile soils which support crop
cultivation.
❖ Hills and mountains are used by telecommunication companies to place on masts.
❖ Some mountains are a source of rivers.
❖ Some physical features are a source of minerals eg.Osukuru hills in Tororo
which provide limestone.
❖ Mountains provide building materials eg.stones
❖ Lakes and rivers provide water for irrigation.
❖ They form natural boundaries between places/ districts.
Dangers of physical features
❖ Some of them are hiding for wrong doers
❖ They harbour dangerous wild animals
❖ They are bleeding places for disease vectors
Page 62
❖ Lakes and rivers flood which kills people.
❖ They hinder road construction.
❖ Mountains hinder agricultural mechanisation.
❖ Some mountains erupt and destroy property.
❖ Hills and mountains have steep slopes which promote soil erosion.
❖ Mountains are greatly affected by landslides. and soil erosion.
Ways of caring for the physical features
❖ BY Planting trees on shores of lakes and mountain slopes and river banks
❖ BY discouraging people from dumping rubbish in water bodies
❖ By terracing land to control soil erosion in highlands.
❖ By sensitising people about the importance of different physical features.
❖ By using proper fishing methods.
❖ By filling holes after mining.
❖ By treating wastes before disposing them in water bodies.
Testing Exercise
1. Write HEP in full.
2. How do lakes and rivers help to modify climate of an area?
3. Name the major mineral mined from Osukuru hills in Tororo.
4. Mention any one building material obtained from mountains.
5. Give one way physical features are politically important in the environment.
6. Give any three ways lakes and rivers are economically important.
7. State any two problems faced by people living near lakes and rivers.
8. Mention any two problems faced by people living in mountainous areas.
9. State any two ways lakes and rivers can be cared for.
10. Give one way mountains hinder economic development in an area.
Page 1
FIRST EDITION
BY
EXCEL PUBLISHERS
All rights reserved. No part of this publication may be reproduced, stored in a retrieval
system or transmitted in any form or by any means of electronic, mechanical,
photocopying, recording or otherwise, without the prior written permission of the
publisher.
Copyright © Excel publishers
Page 2
ACKNOWLEDGEMENT
Developing a book of this nature requires a lot of support from colleagues, friends
and family. I would like to register my deep-rooted gratitude to the following people
for their unlimited assistance offered towards the completion of this book.
All teachers of Social Studies in Victoria Mutundwe Primary School and Makindye
</passage>

<passage id="lchk_4de06718fff148298d102ca2becf0839" source="P.7 PLE UNIQUE SET SST 1" part="9">
 To demand for independence
 To promote respect for human rights
 To preserve African culture
 To improve the welfare of Africans
 To improve the education standards of Africans
 To oppose the white dominance in Africa
 To promote trade among Africans
16. Give one reason why the colonial government introduced the
growing of cash crops in Uganda.
 To get cheap labour
 To enable Africans get money to pay taxes
 To develop African countries economically
 To get raw materials for their home industries
 To utilise the free fertile land in Africa
24
P
17. Mention any one reason for the formation of political parties in a
country.
 To promote unity
 To promote respect for human rights
 To promote democracy
18. Give any one factor that leads to high population in an area.
 Ready market
 Enough security
 Cheap labour
 Better health services
 Fertile soil
 Better banking system
 Better education services  Enough job opportunities
 Reliable rainfall/ good climate
 Better transport Network
 Better communication service
 Enough and cheap trade items
19. Why do veterinary officers sometimes restrict movement of
livestockin an area?
 To control spread of animal diseases
20. Give one reason why a person below 18 years is not allowed to
participate in national elections.
 He or she is not yet an adult according to the Uganda
national constitution.
 He or she is still a child according to Uganda National
constitution
21. Mention any one way of controlling the effect of plastic wastes in
thecommunity.
 By minimizing generation of waste
 By reusing plastic waste
 By returning plastic waste to shops and manufacturer.
 By rejecting the production of some plastic materials
 By recycling plastic materials that are already used to
make new products.
 Through proper disposal of waste
 By allocating places to dispose plastic materials
 By using plastic materials wisely
22. Why should children be taught their rights?
 To control child abuse
25
 To promote respect for human rights
 To produce responsible citizens
 To promote peace and security
 To easily identify people who abuse children rights
23. How was Semei kakungulu helpful to the British government in
Uganda?
 He extended colonial rule to Eastern Uganda
 He promoted formal education
 He built roads
 He encouraged the growing of Cash crops
 He helped the British to arrest some resistors
 He collected taxes on behalf of the British government
24. How do ocean currents influence climate of an area?
 They bring rainfall to the surrounding areas(warm ocean
currents)
 They don't bring rainfall to the surrounding areas (cold
ocean currents)
25. Name the point of a compass formed between North and South.
 East
26. What is national population census?
 This is the official / general counting of people living in a
country.
Study the sketch map of Uganda below and answer questions 27 to 30 .
T
P
R
X
26
27. Mention the main cash crop grown in area marked X .
 Tobacco
28. Name the main economic activity done in area marked P .
 Fishing
29. Identify the town labeled R .
 Nimule
30. State any one factor that favours the growth of Arabica coffee on
theslopes of the mountain marked T .
 Presence of fertile volcanic soil
 Presence of reliable rainfall (good climate)
31. Apart from giving us rainfall, state any one other importance of
clouds.
 They regulate temperature
 They protect us from direct sunrays
</passage>

<passage id="lchk_1f13711ef701441893006b0bf53f0666" source="P.7 PLE UNIQUE SET SST 2" part="9">
 To demand for independence
 To promote respect for human rights
 To preserve African culture
 To improve the welfare of Africans
 To improve the education standards of Africans
 To oppose the white dominance in Africa
 To promote trade among Africans
16. Give one reason why the colonial government introduced the
growing of cash crops in Uganda.
 To get cheap labour
 To enable Africans get money to pay taxes
 To develop African countries economically
 To get raw materials for their home industries
 To utilise the free fertile land in Africa
24
P
17. Mention any one reason for the formation of political parties in a
country.
 To promote unity
 To promote respect for human rights
 To promote democracy
18. Give any one factor that leads to high population in an area.
 Ready market
 Enough security
 Cheap labour
 Better health services
 Fertile soil
 Better banking system
 Better education services  Enough job opportunities
 Reliable rainfall/ good climate
 Better transport Network
 Better communication service
 Enough and cheap trade items
19. Why do veterinary officers sometimes restrict movement of
livestockin an area?
 To control spread of animal diseases
20. Give one reason why a person below 18 years is not allowed to
participate in national elections.
 He or she is not yet an adult according to the Uganda
national constitution.
 He or she is still a child according to Uganda National
constitution
21. Mention any one way of controlling the effect of plastic wastes in
thecommunity.
 By minimizing generation of waste
 By reusing plastic waste
 By returning plastic waste to shops and manufacturer.
 By rejecting the production of some plastic materials
 By recycling plastic materials that are already used to
make new products.
 Through proper disposal of waste
 By allocating places to dispose plastic materials
 By using plastic materials wisely
22. Why should children be taught their rights?
 To control child abuse
25
 To promote respect for human rights
 To produce responsible citizens
 To promote peace and security
 To easily identify people who abuse children rights
23. How was Semei kakungulu helpful to the British government in
Uganda?
 He extended colonial rule to Eastern Uganda
 He promoted formal education
 He built roads
 He encouraged the growing of Cash crops
 He helped the British to arrest some resistors
 He collected taxes on behalf of the British government
24. How do ocean currents influence climate of an area?
 They bring rainfall to the surrounding areas(warm ocean
currents)
 They don't bring rainfall to the surrounding areas (cold
ocean currents)
25. Name the point of a compass formed between North and South.
 East
26. What is national population census?
 This is the official / general counting of people living in a
country.
Study the sketch map of Uganda below and answer questions 27 to 30 .
T
P
R
X
26
27. Mention the main cash crop grown in area marked X .
 Tobacco
28. Name the main economic activity done in area marked P .
 Fishing
29. Identify the town labeled R .
 Nimule
30. State any one factor that favours the growth of Arabica coffee on
theslopes of the mountain marked T .
 Presence of fertile volcanic soil
 Presence of reliable rainfall (good climate)
31. Apart from giving us rainfall, state any one other importance of
clouds.
 They regulate temperature
 They protect us from direct sunrays
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
