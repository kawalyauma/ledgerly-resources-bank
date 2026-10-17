# Job ltsk_4101feeaf8844f56865042bbc9ca9c00-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 5 lesson(s) below of week 2 of the Social Studies scheme for Primary Seven 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P7: one 40-minute lesson: 3–6 sections; about 18–36 points; concise candidate-level points, worked examples and exam tips; 6–10 activities.

lessonId=lles_3745add6250f42289d2007a5435bebc5: lesson 6, Monday, 1 period(s), 40 minutes.
  Unit: Economic Developments in Africa (theme: Living together in Africa). Lesson: Vegetation resources — Vegetation resources.
  Objectives: Identify and describe vegetation resources.

lessonId=lles_a95a8f0385cb4e0b9aa625af14eff200: lesson 7, Tuesday, 1 period(s), 40 minutes.
  Unit: Economic Developments in Africa (theme: Living together in Africa). Lesson: Climate as a resource — Climate as a resource.
  Objectives: Identify and describe climate as a resource.

lessonId=lles_719cd0fd5429446487a9ecb607133e68: lesson 8, Wednesday, 1 period(s), 40 minutes.
  Unit: Economic Developments in Africa (theme: Living together in Africa). Lesson: Water resources — Water resources.
  Objectives: Identify and describe water resources.

lessonId=lles_842d6ec1c8864216a846513be7859e56: lesson 9, Thursday, 1 period(s), 40 minutes.
  Unit: Economic Developments in Africa (theme: Living together in Africa). Lesson: Problems in using resources — Problems in using resources.
  Objectives: Identify and describe problems in using resources.

lessonId=lles_d2aa3de8bd33401fb404dc2b95f38fce: lesson 10, Friday, 1 period(s), 40 minutes.
  Unit: Economic Developments in Africa (theme: Living together in Africa). Lesson: Caring for resources — Caring for resources.
  Objectives: Identify and describe caring for resources.

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

<passage id="lchk_bcfdfd36126440009097fbf1315f366d" source="NCDC PRIMARY SEVEN SET ONE – Social Studies" part="18">
will also be introduced to the advantages and disadvantages of forming
economic groupings.

Learning Outcome
The learner appreciates the values of independence, what happened after
independence and the importance of cooperation among states.

Life Skills
• Effective communication
• Friendship formation
• Non-violent conflict resolution
• Problem-solving
SST Skills
• Inquiry
• Reading
• Writing

National Curriculum Development Centre

Values
• Cooperation
• Love
• Respect
• Appreciation

Subject | Language | Content | Suggested
Competences | Competences | Activities.
The learner: | The learner | • Formation of | • Discussing
• explains why | correctly uses the | OAU: | why the OAU
OAU was | following words | – When it was | was formed
formed. | related to the | formed | • Explaining
topic: | – Why it was | the objectives
– unity | formed | of OAU and
– founder | – Founder | stating how it
– objective | members | functioned
– Objectives of | • Drawing the
OAU | map of Africa
– Functions of | and shading
OAU | founder
member
countries
• states | The learner | • Achievements of | • Discussing the
achievements | correctly uses the | OAU: | achievements
of OAU. | following words | – Ended | and failures of
• discusses the | related to the | colonialism in | OAU
failures of | topic: | Africa
OAU. | – failure | – Solved some
• explains | – challenge | border conflicts | • Discussing the
why AU was | – apartheid | e.g. in Morocco | formation of
formed | – policy | and Algeria | AU
• describes the | – dependence | – Ended Apartheid
organs of AU. | – funds | Policy in South
• discusses | Africa
challenges of | – Gave birth to
AU. | Africa Union
• suggests
the possible
solutions to
challenges of
AU.

Primary Seven Curriculum

Subject | Language | Content | Suggested
Competences | Competences | Activities.
– Failures of OAU
such as it failed | • Describing the
to stop civil | organs of AU
wars in some | • Discussing the
countries in | challenges of
Africa such as | AU
Sudan | • Suggesting
• Formation of AU | the possible
and its objectives | solutions to the
• Organs of AU | challenges of
• Challenges of | AU
AU:
– Limited funds to
operate all affairs
of AU
– Constant civil
wars
– Different
political
ideologies
– Dependence
on developed
countries
• Possible solutions

• states the | The learner | • Regional | • Identifying
functions | correctly uses the | economic | reasons why
of regional | following words | groupings: | regional
economic | related to the | – COMESA | economic
groupings in | topic: | (Common | groupings
Africa. | – market | Market for East | were formed
• discusses | – community | and Southern | • Discussing
advantages | – development | Africa) | advantages
and | – cooperation | and
disadvantages | disadvantages
of economic | of cooperation
cooperation.

National Curriculum Development Centre

Subject | Language | Content | Suggested
Competences | Competences | Activities.
• suggests ways | – ECOWAS | • Suggesting
of solving | (Economic | ways of solving
problems | Community of | problems of
affecting | West African | economic
economic | States) and | groupings
groupings. | ECOMOG
(Economic
Community
Monitoring
Group)
– East African
Community
(EAC)
– SADC
(Southern Africa
Development
Community)
– IGAD (Inter-
governmental
Authority and
Development)
• Advantages and
disadvantages
of economic
cooperation
• Ways of solving
problems faced
by economic
groupings

Guidance to the Teacher
</passage>

<passage id="lchk_6189871e1121435bb424a22e5d3e2b1f" source="NCDC PRIMARY SEVEN SET ONE – Social Studies" part="21">
• Discuss with learners the problems faced in resource utilisation.
Use local examples from Uganda first before talking about
others elsewhere.
• Organise learners to demonstrate or role-play how corruption
is practised.
• Organise field visits, surveys and data collection about
developmental projects in the neighbourhood.
• Guide learners to compare economic developments in Uganda
with other case study countries.
• Guide learners to write compositions and reports about the
challenges affecting the economic development of Africa.
• Use the immediate environment within the learner’s reach such
as family and the community to enable him/her to understand
the concept of economy better.
• You are advised to use the following materials to teach this
topic effectively: various textbooks, maps, atlases, wall charts,
diagrams, newspapers and magazines.
• Collect products of different natural resources from the
environment.
• Organise trips to the local environment.
• You are also advised to use resource persons.
• Encourage learners to participate in environmental maintenance.
Encourage learners to write compositions and organise debates
and quizzes about the topic. Using prompting questions is also
important.

Primary Seven Curriculum

Suggested Competences for Assessment
The learner:
• writes posters on how to improve the economy of Africa.
• organises peaceful demonstrations on corruption, poor
leadership and civil wars.
• visits the local environment to see development projects and
writes a report.
• plans any economic developmental project in the school.
• states the major economic resources of Africa.
• draws various maps of Africa to show economic resources.
• discusses how natural resources contribute to economic
development in Africa.
• identifies major economic activities of African countries of the
case study.

Topic 10: Major World Organisations
10 Periods
Background
In the previous topic, the learner covered economic development in
Africa. In this topic, the learner will be introduced to the international
community and gain knowledge and information on how the world
interrelates. He/she will also learn about the United Nations (UN), its
agencies and the Commonwealth of Nations, how they function and the
challenges they face. In the process of teaching this topic, bring out the
relationship between the United Nations and the two world wars.

Learning Outcomes
The learner:
• appreciates the interdependence of nations and how the United
Nations and its agencies are helping to solve challenges in
Africa and the rest of the world.
• appreciates the role-played by the Commonwealth of Nations.
Life Skills
• Effective communication
• Friendship formation
• Non-violent conflict resolution
SST Skills
• | Recording
• | Reading
• | Writing
• | Interpretation
Values
• Cooperation
• Appreciation
• Love
• Sympathy
• Sharing

Primary Seven Curriculum

Subject | Language | Content | Suggested
Competences | Competences | Activities
The learner: | The learner | • Formation of the | • Explaining
• explains how | correctly uses | United Nations | briefly how
the two world | the following | – Origin | the two world
wars led to the | words related | – Objectives | wars led to the
formation of the | to the topic: | – Functions | formation of
United Nations | – technical | • Membership of the UN | the UN
and how it | assistance | • Organs of the UN | • Explaining
works. | – agency | • Importance of the | why the United
</passage>

<passage id="lchk_45b3b7d8a19b431c93f6a52f1f12a1e9" source="P.7 PLE UNIQUE SET SST 1" part="11">
 Patrice Lumumba
 Osman Daar
 Herbert Maga
 Haman Diari
 Maurice Yameogo
 Felix Boigny
 Francois Tambel berry
 David Dacko
 Filbert Youlou
 Leon M’ba
 NnamdiAzikiwe
 Moyar Oud Daddah
 Milton Magal
 Julius KambarageNyerere
 GregoireKayibanda
 Mwambutsa iv
 Ahmed Ben Bella
 Apollo Milton Obote
 Jomo Kenyatta
c) Why is Durban city important in the formation of African
Union?
 The African Union was launched in Durban on 9th
July 2002
30
42. a) What is a national budget?
 This is an estimation of a country's income and
expenditure for a given financial year.
b) Mention the two parts of a budget.
 Income
 Expenditure
c) Give any one advantage of a surplus budget.
 It promotes development
 It promotes saving
 It controls debts
 It controls losses
43. a) Give any two reasons for the construction of the
Kenya-Ugandarailway.
 To stop slave trade.
 To promote legitimate trade.
 To promote agriculture
 To promote economic development
 To ease transportation of British administrators from
the coast to the interior.
 To ease transportation of goods from Uganda to the
coast.
 To ease transportation of raw materials to processing
centers
b) What was the following personalities remembered for in the
construction of the Kenya-Uganda railway?
i) Sir William Macknon.
 He suggested he construction f the Uganda railway
ii) George White House.
 He was the chief engineer during the construction
of the Uganda raiilway
44. a)What is fishing?
 Fishing is the catching of fish from water bodies
 Fishing is the extraction of aquatic life from water
bodies
31
b) Why is fishing called an industry?
 It generates government revenue
 It creates employment
 It is a source of income
c) Give one way the fishing industry has promoted economic
development of a country.
 It has created employment
 It led to development of infrastructures
 It has increased government revenue
 It has promoted tourism
 It has created market for some fishing equipment
d) Give any one problem faced by the fishing industry in
Uganda.
 Pirates
 Bad weather
 Overfishing
 Poor transport
 The water weed
 Fish poisoning
 Limited market
 Water accidents
 Shortage of capital
 Dangerous aquatic animals
 Poor storage facilities
 Poor government fishing policies
45. a) Mention any two reasons why European explorers were
interested in Africa.
 To study the geography of Africa
 To find new settlement
 To find the source of river Nile
 To find out the culture of Africans
 To complete the work of other explorers
 To find ways of ending slave trade
 To get prestige
 To open up ways for missionaries
 To find trade opportunities
b) Give any two ways European explorers led to the coming of
colonialists to Africa.
 They wrote positive reports on Africas resources which
attracted the colonialists.
 They drew maps which eased movement of colonialists.
32
46. Study the map of CountryT below and use it to answer the
questions that follow.
a) Name the prevailing winds that bring rain to the shaded part
onthe map.
 Westerly winds/ westerlies
b) Why is country marked R called an enclave?
 Country marked R is completely found in another
country.
c) State one factor that disqualifies country marked K to be
calledan enclave.
 It shares boundaries/ boarders with other countries
d) Give any one factor that has led to the industrial developmentof
Country T .
 Presence of enough raw materials
 Presence of enough cheap labour
</passage>

<passage id="lchk_2d29d7724d2449769a73a781aefc6250" source="P.7 PLE UNIQUE SET SST 2" part="11">
 Patrice Lumumba
 Osman Daar
 Herbert Maga
 Haman Diari
 Maurice Yameogo
 Felix Boigny
 Francois Tambel berry
 David Dacko
 Filbert Youlou
 Leon M’ba
 NnamdiAzikiwe
 Moyar Oud Daddah
 Milton Magal
 Julius KambarageNyerere
 GregoireKayibanda
 Mwambutsa iv
 Ahmed Ben Bella
 Apollo Milton Obote
 Jomo Kenyatta
c) Why is Durban city important in the formation of African
Union?
 The African Union was launched in Durban on 9th
July 2002
30
42. a) What is a national budget?
 This is an estimation of a country's income and
expenditure for a given financial year.
b) Mention the two parts of a budget.
 Income
 Expenditure
c) Give any one advantage of a surplus budget.
 It promotes development
 It promotes saving
 It controls debts
 It controls losses
43. a) Give any two reasons for the construction of the
Kenya-Ugandarailway.
 To stop slave trade.
 To promote legitimate trade.
 To promote agriculture
 To promote economic development
 To ease transportation of British administrators from
the coast to the interior.
 To ease transportation of goods from Uganda to the
coast.
 To ease transportation of raw materials to processing
centers
b) What was the following personalities remembered for in the
construction of the Kenya-Uganda railway?
i) Sir William Macknon.
 He suggested he construction f the Uganda railway
ii) George White House.
 He was the chief engineer during the construction
of the Uganda raiilway
44. a)What is fishing?
 Fishing is the catching of fish from water bodies
 Fishing is the extraction of aquatic life from water
bodies
31
b) Why is fishing called an industry?
 It generates government revenue
 It creates employment
 It is a source of income
c) Give one way the fishing industry has promoted economic
development of a country.
 It has created employment
 It led to development of infrastructures
 It has increased government revenue
 It has promoted tourism
 It has created market for some fishing equipment
d) Give any one problem faced by the fishing industry in
Uganda.
 Pirates
 Bad weather
 Overfishing
 Poor transport
 The water weed
 Fish poisoning
 Limited market
 Water accidents
 Shortage of capital
 Dangerous aquatic animals
 Poor storage facilities
 Poor government fishing policies
45. a) Mention any two reasons why European explorers were
interested in Africa.
 To study the geography of Africa
 To find new settlement
 To find the source of river Nile
 To find out the culture of Africans
 To complete the work of other explorers
 To find ways of ending slave trade
 To get prestige
 To open up ways for missionaries
 To find trade opportunities
b) Give any two ways European explorers led to the coming of
colonialists to Africa.
 They wrote positive reports on Africas resources which
attracted the colonialists.
 They drew maps which eased movement of colonialists.
32
46. Study the map of CountryT below and use it to answer the
questions that follow.
a) Name the prevailing winds that bring rain to the shaded part
onthe map.
 Westerly winds/ westerlies
b) Why is country marked R called an enclave?
 Country marked R is completely found in another
country.
c) State one factor that disqualifies country marked K to be
calledan enclave.
 It shares boundaries/ boarders with other countries
d) Give any one factor that has led to the industrial developmentof
Country T .
 Presence of enough raw materials
 Presence of enough cheap labour
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
