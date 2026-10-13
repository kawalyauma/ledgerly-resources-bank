# Job ltsk_99bd282318294b1e9367370ee0d9f372-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 5 lesson(s) below of week 5 of the Social Studies scheme for Primary Five 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P5: one 40-minute lesson: 3–4 ideas; 300–500 words; connected explanations and application; 5–8 activities.

lessonId=lles_c8bb4f7bc386455ab766c0ecaa74b071: lesson 21, Monday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: Citizenship and responsibilities of citizens — Rights and responsibilities.
  Objectives: Explain who a citizen is.; State the ways of becoming a citizen of Uganda and how one can lose citizenship.; State the responsibilities of a good citizen.

lessonId=lles_8a73de64fc3040c58e720ef1a13746dd: lesson 22, Tuesday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: Human rights — Rights and responsibilities.
  Objectives: Explain what human rights are and give examples.; Explain human rights abuse.; Name organisations that protect human rights and state roles citizens play.

lessonId=lles_3bb6529a3787427f985106672e609551: lesson 23, Wednesday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: Children's rights, child abuse and child labour — Child labour.
  Objectives: State children's rights and their importance.; Name forms and causes of child abuse.; Explain child labour, its effects and ways of controlling it.

lessonId=lles_2b70aad512364bf69bc3150e844618f9: lesson 24, Thursday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: Practice: rights and responsibilities of citizens and child labour — Rights and responsibilities.
  Objectives: Answer exercise questions on citizenship, human rights, children's rights and child labour.
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points (numbered, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

lessonId=lles_ac0e70beda0f479ea48a91b94343ea29: lesson 25, Friday, 1 period(s), 40 minutes.
  Unit: Population, Size and Distribution (theme: Living together in Uganda). Lesson: Meaning of population and census — Meaning of population and census.
  Objectives: Explain what population and census mean.; Explain who teenagers are.; Explain what a census night and enumerators are.

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

<passage id="lchk_5b12ef04e65245cdb076e27f5801b923" source="Primary 5 Social Studies Scheme of Work, Term III" part="4">
Meaning of human rights
Examples of human rights
Human rights organizations
Human rights abuses
Ways of preventing human rights
abuses
Children’s rights
Ways how children’s rights are violated
How to protect human rights
Roles of children
Subject
The learner;
Gives the meaning of human rights
Mentions ways of preventing human
rights abuses
Language
The learner pronounces, reads,
spells and writes words correctly
e.g. violation, human rights
Story telling
Guided discussion
Stating the ways how
human rights are
violated
Answering questions
orally and written
exercises
Effective
communication
Critical thinking
Patriotism
Text
books
MK SST pupils book 5 page 142
3
The Government
Citizenship
Meaning of a citizen
Meaning of citizenship
Types of citizenship
Ways of becoming as citizen
Ways of losing citizenship
Qualities of a good citizen
Duties / responsibilities of a good
citizen
Subject
The learner
Gives the meaning of words such as
citizenship, a citizen, adoption,
descent and naturalization
Describes different ways how
governments are formed
Explains the two systems of
government
Language
The learner reads, spells and writes
words correctly such as citizenship,
military, dictatorial and multi-party
Environment based
approach
Question and answer
Giving the meaning of
the new words
Describing different
forms of government
Critical thinking
Love
Responsibility
Text
books
MK Standard SST pupils book 5 page 173 /
149
4
&
5
The Government
How governments are formed
Forms of government
Democratic government
Military government
Dictatastial government
Ways how governments are formed i.e.
Through elections
Through inheritance
Through appointment
Through military coups
Systems of government
Single party system
Multiparty system of government
Advantages and disadvantages of
each system in a country
Where they are applied
Current system of government in
Uganda
Subject
The learner;
Mentions the forms of government
in Uganda
Gives the advantages and
disadvantages of single and multi-
parfism
Language
The learner pronounces, reads and
spells the words correctly like
military, dictatorial, inheritance,
elections, coups e.t.c.
Story telling
Inquiry
Text books
6 1
The Government
Elections
Meaning of elections
Types of elections i.e. General local
and By-elections
Conditions for by-elections
The electoral Commission
Electoral terms
Materials and officials involved in an
election
Problems facing the electoral process
before, during and after elections
Explains the electoral system
Subject
The learner
Gives the meaning of the term
elections, referendum, bye-election,
general election
Explains the electoral systems
employed in Uganda today
Language
The learner pronounces, reads,
spells and writes words correctly like
referendum, by-election, electorate,
commission, vote
Guided discussion
Inquiry
Answering oral and
written activities
Responsibility
Co-operation
Respect
Wall
chart
showing
stages
involved
in an
election
MK standard SST pupils book 5 page 151 -159
2
The Government
Electoral systems
Electoral system
Secret ballot systems
Open election
Electoral college
Advantages and disadvantages of
each system
Qualifications of a president
Subject
The learner
Gives the meaning of the systems of
voting
Mentions the qualities for one to be
chosen a president
Language
The learner pronounces, reads,
spells and writes words correctly like
electoral, college, voting by proxy,
secret ballot, voting
Guided discussion
Inquiry
Answering oral and
written activities
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

<passage id="lchk_34a5d4a3b16d47f5967a8c7c879ba1ab" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="13">
The learner:- Spells and uses words related to the sub -topic: expression, associations,
discrimination, victimization
Content : Human rights in Uganda
 Human rights refer to the basic rights and freedom to which all people are entitled simply
because they are human beings.
 These rights apply to people of any race, colour, sex, language, religion and social origin.
32
Human rights / rights of citizens
 Protection of right to life.
 Right to fair hearing in courts of law.
 Freedom of speech, worship and assembly.
 Right to a clean and healthy environment.
 Right to privacy of home and property.
 Right to free expressions, movement and association
 Right to belong to a tribe, clan or lineage.
 Right to access public information
 Freedom from discrimination on basis of race, education , opinion etc
Protection of human rights
 It is the responsibility of the government of Uganda to ensure that individuals in Uganda
enjoy their human rights.
Organizations that were set up to protect human rights
 The Uganda Human Rights Commission (UHRC)
 The Inspector General of Government (IGG)
 The Federation of Women Lawyers (FIDA)
 The Uganda Human Rights Initiative (UHRI)
Internal Organizations that protect Human Rights
 Amnesty International based in Britain
 The human rights Watch Dog based in USA
Human Rights abuse
 Human rights abuse is the violation of one’s fundamental rights.
Examples of human rights abuse
i) Victimization ie.
- This involves unfair treatment of a person.
ii) Arbitrary arrest and imprisonment
iii) Lack of fair judgment in courts of law.
33
iv) Lack of freedom of movement
v) Denying people freedom of expression
vi) Lack of freedom of worship
vii) Torture or an assault
Activity
1. Briefly describe the term human rights.
2. Give any two examples of human rights
3. Define human rights abuse.
4. Write down two ways human rights have been abused today.
5. Give two internal organizations that help to protect human rights.
6. Mention two internal organizations that protect human rights.
Date Class Subject No. of pupils Time
P.5
TOPIC: The Government of Uganda
SUB –TOPIC: Responsibilities/ Duties of citizens
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic: loyalty, obedience, Naturalization
Content : Citizenship
Citizenship refers to the legal rights to belong to a particular country
Who is a citizen?
 A citizen is a person who enjoys full civil democratic and human rights in a country.
Or
 A citizen is a person who is recognized by the government to belong to a particular
country.
Types of citizenship
i. Dual citizenship
This refers to the possession of citizenship of two different countries at the same time.
ii. Single citizenship.
Refers to the possession of citizenship of only one country.
34
Ways of becoming a citizen.
i) Citizenship by birth
 A person born by parents who are Ugandans becomes a citizen of Uganda by birth.
ii) Citizenship by registration
The following categories of people can become citizens of Uganda by registration or
application
 A person who has lived in Uganda since independence continuously.
 A person married to a Uganda citizen for at least a period of three years.
 Legal and voluntary migrants who have been living in Uganda for at least ten years.
iii) Citizenship by Naturalization
 This is where a person from another country is made a citizen of a specified country
after spending many years (20years)
iv) Citizenship by descent
</passage>

<passage id="lchk_5d9fca1a0c194c47a0d551561d1abf1b" source="Primary Five Social Studies Notes 2020" part="58">
Duties of the Uganda Human Rights Commission
To promote human rights
To fight the misuse of human rights
To inspect prisons
To educate citizen about their right
Examples of human right
 Right to live
 Right to fair hearing in courts of law
 Freedom of speech
 Right of own property and privacy of home
 Freedom of movement
 Freedom of worship
252
 Right to access public information
Responsibilities of citizens
Define the following
1. Citizen
This is a person who has legal right to belong to a country
Citizenship
This is the legal right to belong to a particular country
Types if citizen ship
 Single citizenship
 Dual citizenship
How one can become a citizen of Uganda?
i) By birth
 This is when one is born by parents who are Uganda
ii) By registration
 This is when a foreigner register with the immigration department of
Uganda government to belong to a country
 The immigration department belong to ministry of internal affairs
Iii) Naturalisation
 This is when a person has spent many years in Uganda
iv) By descent
 This is a person whose ancestors where Ugandans
v) By adoption
253
 This is a person who has been brought up by parents who are
Ugandans before 18 years
How some one can lose citizenship of Uganda?
 If a person becomes a citizen of another country
 If a person joins the army of an enemy country to Uganda
 If a person spies on his her country for another country
 When one gets citizenship through fraud
Responsibilities of citizen
 To keep law and order
 To pay taxes promptly
 To take part in self help projects
 To respect the rights of other citizens
 To fight misuses of public property
 To respect the country national attributes
 To help police to identify criminals
Child abuse
 This is the violation /abuse of children rights
Causes of child abuse
 Alcoholism
 Death of parents
 Separation of parents
 Drug abuse
 Poverty
 Wars
 Ignorance
Example of child abuse
 Defilement
 Beating
 Child battering
254
 Child labour
 Kidnapping
 Child sacrifices
 Denial of food
Forms of child abuse
 Physical
 Psychological
 Emotional
 Sexual
Qn: Who is a child?
 A child is a person below the age of eighteen years
Children’s right
 These are natural freedoms children are supposed to get in their daily
life
Examples of children’s right
 Right to food
 Right to medical care
 Right to be protected
 Right to shelter
 Right to clothes
 Right to play
 Right to education
 Right to speak with respect
 Right to have a name
 Effects of child abuse
 It leads to death of children - early marriage
 It caused injuries to a child – early pregnancy
 It leads to street children
 It deterioties children’s health
 It leads to school dropout
255
Suggested solution to child abuse
 Children should be educated about their rights
 Heavy fines should be imposed on people who abuse children’s right
 People should be educated about to children’s right
 Imprison people who abuse childrens right
How children to violation of their rights
 Stating in lonely places
 Walking alone at night
 Disobeying elders
 Failure to perform duties
 By stealing household property
Causes of street children in Uganda toady
 Death of parent
 Heavy domestic work
 Denial of basic needs
 Separation of parents
 Insecurity in villages
 Heavy punishments at home
Groups of people who may abuse children’s right
 Step parents
 Drug addicted people
 Fellow children
 Kidnappers
 Insane people
Importance of childrens
</passage>

<passage id="lchk_0291abf81e8944708feb2b71e64574c2" source="Primary 5 Social Studies Lesson Notes (2018)" part="30">
- It helps one identify sources of income
- It ensures enough money for the required essentials
- It helps to plan how to spend its income
© 2018 Page 80
Sources of revenue
Revenue means income of a government
Sources of income include;
- Taxes - Airport charges
- Loans - Tourism
- Grants - Parastatal bodies
- Court fines
- Donations
TAXATION
A tax is a sum of money paid by the people of the country to the government
Types of taxes
Direct taxes
These are taxes which the government gets directly from tax payers e.g. PAYE,
income tax
Indirect taxes
These are taxes incurred on spending e.g. VAT, Customs duty, and excise duty.
Customs duty : it’s a tax levied on imports and exports
Excise duty: it’s a tax levied on locally manufactured goods.
VAT – value added tax charged on goods and services
Why people pay taxes
- To construct roads
- To construct schools
- To pay civil servants
- To construct and maintain hospitals
- To cater for security services
Why people don’t pay taxes
- Lack of tax information
- High tax rates
- Corruption among tax collectors
- Most tax information is written in English
Rights and responsibilities of the citizens
A citizen is a person who enjoys full, civil, democratic and human rights in a
country
Ways of becoming a citizen in Uganda
© 2018 Page 81
By birth: is a person whose parents or grandparents were members of the
indigenous communities when Uganda’s boundaries were drawn in 1926.
A foundling is abandoned child of unknown parents. If found and is less than five
years that child qualifies to be a citizen by birth.
Registration
A person may become a citizen of Uganda by registration under the following ways
(a) An adopted child under the age of 18years
(b) A person who has lived in Uganda continuously since independence
(c) A person married to a Ugandan citizen for a period of 3years
(d) Legal and voluntary migrants who have lived in Uganda for atleast
10years
By naturalization
This is where a person from another country is made a citizen of a specified
country
Dual citizenship
Is the possession of citizenship of two different countries at the same time
Loss of citizenship in Uganda
A person may lose citizenship in Uganda under the following grounds;
(a) Spying against Uganda
(b) Acquiring citizenship un lawfully
(c) Serving in an army of a hostile country to Uganda
Duties of the national citizenship and immigration board in Uganda
- Registration of citizens
- Issues national identity cards
- Issues Uganda passports and other travel documents
- Granting and canceling citizenship by registration and naturalization
NB: this board is under the ministry of Internal Affairs
The body handling this is the Directorate of citizenship and immigration
Duties of a citizen
- Pay taxes promptly
- Keep law and order
- Register for electoral purposes
- Protect and preserve public property
- Respect other people’s rights and freedom
- Defend Uganda at all times
- Take part in self-help projects
© 2018 Page 82
- Take children and other vulnerable persons against any form of abuse
Rights of a citizen
- Human rights are basic rights and freedom any human being is entitled to
- They include;
- Freedom of protection to life
- Freedom of speech
- Freedom of worship
- Freedom of assembly
- Right to clean and healthy environment
- Right to privacy
- Right to belong to a tribe, clan and lineage
- Right to access public information
Population size and distribution in Uganda and their relationship to
economicplanning and development
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
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
