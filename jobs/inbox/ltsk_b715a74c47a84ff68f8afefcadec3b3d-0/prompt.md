# Job ltsk_b715a74c47a84ff68f8afefcadec3b3d-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 5 lesson(s) below of week 7 of the Social Studies scheme for Primary Five 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P5: one 40-minute lesson: 3–5 sections; about 14–28 points (meaning, examples, reasons, problems and solutions as the passages give); 5–8 activities.

lessonId=lles_cf576b542124477bbe8959a6c665509e: lesson 31, Monday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: Responsibilities of a citizen — Responsibilities of a citizen in developing Uganda.
  Objectives: State the responsibilities of a citizen; Explain how citizens contribute to the development of Uganda

lessonId=lles_ebb648ef2b1149e4b4581f733d12e7bf: lesson 32, Tuesday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: Child labour — Children's rights and child labour.
  Objectives: Define child labour; State ways of controlling child labour

lessonId=lles_78aea8dfc8d9478cbcaf5d9e756e8531: lesson 33, Wednesday, 1 period(s), 40 minutes.
  Unit: Population, Size and Distribution (theme: Living together in Uganda). Lesson: Population and the population census — Meaning of population and census.
  Objectives: Define population and population census; Give reasons why the government carries out a census

lessonId=lles_dba4204db0164ee6b065363b9025c4fe: lesson 34, Thursday, 1 period(s), 40 minutes.
  Unit: Population, Size and Distribution (theme: Living together in Uganda). Lesson: Population growth — Factors that influence population growth.
  Objectives: Define population growth; State the factors that influence population growth

lessonId=lles_3a76846a2551482ebeb77fe8fc86caca: lesson 35, Friday, 1 period(s), 40 minutes.
  Unit: Population, Size and Distribution (theme: Living together in Uganda). Lesson: Population distribution — Factors affecting population distribution.
  Objectives: Define population distribution; State the factors affecting population distribution

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

<passage id="lchk_f4e043f39e034c8eaac37e82506c59dc" source="P.5 Social Studies Lesson Notes Term 3" part="9">
 Presence of mineral deposits
 Historical factors e.g. slave trade
 Employment opportunities
 Presences of social services
 Biological factors e.g. fertility in women
 Political stability
 Urbanization and industrialization
NB: Explain how each factor affects population growh
 Population and resources
 The number of people in Uganda varies according to the natural resources in
that area
 Uganda is classified as a developing country because of the quality of its
citizen
Signs of Uganda’s backwardness
 Ignorance
 Illiteracy
 Poverty
 Diseases
 Hunger
 Low life expectancy
 High infant mortality rate
 Belief in superstitions
The above indicators show that Uganda’s population cannot top its resources to
the full utilization
DIVINE EDUCATION CENTRE:0784540287/0751565742 Page 26
Population growth
 This refers to the increase of people in an area
Factors affecting population growth
 Birth rate
 Death rate
 Migration rate
 Early marriages
 Peace and political stability
 Good medical services etc
Nb: explain how each factor affects population growth
Natural population increase
 This is the difference between the number of births and the number of
deaths
Problems of population growth
 Food scarcity
 Easy spread of epidemic diseases
 Lack of accommodation
 High crime rate
 Lack of proper social services
 Land shortage
 Land fragmentation
 Environmental degradation
 Development of slums
Ways of controlling population growth
 Family planning campaigns
 Tax benefits for small families
 Education benefits
 Act of parliament or government decree
 Sensitizing the masses
 Legalising abortion
Hazards which check on population growth
 Hazards are bad things that check on population growth
 Natural hazards
 Pests and diseases
DIVINE EDUCATION CENTRE:0784540287/0751565742 Page 27
 Floods
 Earth quakes
 Lightening
 Strong winds
 Drought
 Volcanoes
 Wars
 Pollution
 Transport accidents
Ways of reducing population hazards
 Providing proper medical services
 Practicing scientific agricultural methods
 Advancement in communications
 Technological advancement
Advantages of population growth
 Ready market for produced goods
 Cheap labour force
 Full utilization of resources
 Enough skilled labour force
 Good security services
 Enough tax collection base
Problems of low population
 Under utilization of resources
 Low labour force
 Low market for manufactured goods
 Low tax collection
 Low skilled labour force
 Poor security services
Population census
 This is the general counting of people in an area
 In Uganda it is held every after ten years
Reasons for a population census
 To know the birth and death rates
 For proper planning for the population
 For proper allocation of services
 To know the age structure.
DIVINE EDUCATION CENTRE:0784540287/0751565742 Page 28
Difficulties involved in population census
 It is expensive
 Lack of skilled enumerators
 Wide spread illiteracy
 Poor civic education
 Walking long distances
 False information by the population
 Ignorance among the people
Population terminology
 Population density : this is the average number of people per square kilometer
 Population density = total population = number of people per square kilometer
Area
 Over population : this is when the population of an area is greater than its
resources
 Under population : this is when the population of an area is less than its
resources
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

<passage id="lchk_c87f35f3e8f2469c85eaf42fab2293e6" source="P.5 SST SCHEME TERM III 2019" part="4">
-Explaining the term constitution
-Stating the functions and importance of constitution
-Read, pronounce and use words related to the constitution
The Constitution
-Meaning
-Functions of the constitution
-Importance of a constitution
-The constitutions of Uganda.
The 1962 constitution
The 1967 constitution
The 1995 constitution
-Description
-Role play
-Discussion
-Explanation
-Brain storming
-Respect
-Writing
-Sharing
-Reading
-nationalism
-Explaining the meaning of a constitution.
-Discussing the importance of a constitution
-The school rules
-hand books
Mk STD
BK 5
Pg
6
5
&
1
The sources of government income
-Explaining the sources of government income and revenue
-Spells, reads, pronounces and uses words related to sources of revenue
Taxation
Value
Donations
Tourism
License
loans
-Revenue
-Taxation
Types of taxes
-Examples of taxes
Body responsible for collecting taxes (URA)
-Roles of the URA
-Others sources of government revenue
Grants
Loans
Donations
Fines
Tourism
Sales
Licenses
-Discussion
-Explanation
-Question and answer
-Sharing
-Writing
-Reading
-Discussing how the gov’t earns its income
-Pictures and photographs
-License cards
Mk stdbk 5 pg 138-139
6
2
LIVING TOGETHER IN UGANDA
The government of Uganda
The government Expenditure
-Explaining expenditure
-Discussing ways how the gov’t spends the revenue
Spells, reads, pronounce and uses words related to expenditure like security
Expenditure
-meaning
-Ways how the gov’t spends revenue.
Salaries & allowances
Dev’tprogrammes
Rent
Security
Social services
Problems in spending revenue
-Discussion
-Explanation
-Question and answer
-Appreciation
-Love
-Sharing
-Co-operation
-Listening
-Discussing ways how the gov’t spends its revenue
-Pictures connected to ways how gov’t spends its revenue.
Mk stdbk 5 pg 139
3
&
4
The budget
-Explaining the term budget
-Discussing the different types of budgets.
-Discussing the importance of the budget
-spell, read, pronounce and use words related to the budget
-surplus
-balanced
deficit
The budget
-Meaning
-Types of budgets
Surplus
Balanced
Deficit budget
-Importance of the budget
-Explanation
-Discussion
-Discovery
-Question and answer
-Drawing
-Care
-Sharing
-Observation
-Drawing the types of budget.
-Naming the parts of the budget
-Pictures of different budgets
Mk stdbk 5 pg 140-141
Functional bk 5
Pg 187-188
5
The Human Rights
-Discussing the rights of a citizen.
-Explaining the UHRC and its roles
-Spells, reads, pronounces words related to human rights.
-rights
Rights of a citizen
-Ways how human rights are abused.
-UHRC and its roles in protecting human rights.
-Explanation
-Discussion
-Discovery
-Question and answer
-Tolerance
-Love
-Explaining the rights of the citizen and roles of the UHRC
-Pictures showing human rights are abused
Mk std
bk 5
pg 142-143
7
1
LIVING TOGETHER IN UGANDA
Responsibilities of a citizen
-Discussing the responsibilities of a citizen in developing a country.
-Responsibility
-Citizen
-Development
Responsibilities of a citizen in developing Uganda.
-Ways how citizen has contributed towards the dev’t of a country.
-Discussion
-Explanation
-Question and answer
-Tolerance
-Loyalty
-Appreciation
-Hard work
-Patriotism
-Co-operation
-Sharing
-Respect
-Explaining the responsibilities of the citizen in developing Uganda
-Discussing the causes and types of child labour and how to control it
-Pictures showing how a citizen shows his/her responsibilities
-Pictures showing how rights of children are abused.
Mk std
Bk 5
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

<passage id="lchk_77346614385440e7b018b227acc0e2f9" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="14">
 This is where a person is born by parents whose ancestors were Ugandans.
v) Citizenship by adoption
vi) Citizenship by foundling
 A foundling is an abandoned child of unknown parents and is found in Uganda.
Loss of citizenship
Ways one can lose citizenship in Uganda
 When he/ she voluntarily becomes a citizen of another country.
 When he/ she joins the army of a hostile country to Uganda.
 When he/ she spies against Uganda.
 Acquisition of Uganda citizenship by fraud.( illegally )
Good citizenship
Qn. Who is a good citizen?
 A good citizen is a person who has certain qualities that make his/ her to become a useful
member of his/her community and country.
Quality / elements of a good citizen
 Patriotism
 Refers to a strong love one has for one’s country.
A patriotic citizen is a person who has or shows great love for his / her country.
35
 Respect
 Co- operation
 obedience
 loyalty
 justice
Duties / responsibilities of a good citizen
 Keeps law and order.
 Pays tax promptly
 Preserves his environment
 Respects and preserves the rights and freedom of others
 Upholds the national constitution
 Respects the nation’s attributes.
 Renders national services whenever they are required.
 Participates in the national activities which promote democracy and good governance
e.g. general elections
 Participate in self help projects.
Activity
1. Briefly give the meaning of a citizen
2. Point out two ways one can become a citizen of Uganda.
3. Define dual citizenship
4. How can one lose his chance of being a citizen of Uganda?
5. What do you understand by the term patriotism?
6. State any four responsibilities of a good citizen in Uganda.
Date Class Subject No. of pupils Time
P.5
TOPIC: The Government of Uganda
SUB –TOPIC: How the government is formed
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic: elections, electoral, constituency,
poling station, referendum
Content :
36
Ways a government can be formed
 Through elections
 Through hereditary
 Through an alliance
 Through violence e.g. military coup.
Elections
Meaning of an election
 An election is an integral process of a democratic government.
 An election is a democratic way of choosing leaders.
Types of elections
i) General elections/ parliamentary elections
 This is when the parliamentary representatives are elected at national level.
ii) Presidential elections
 These are direct elections for a president
iii) Local elections
 These are elections when councilors for town or district councils are elected.
iv) Referendum
 This is a vote organized to decide on a political issue.
v) Bye elections
 These are elections carried out to fill a vacant political post.
O r
 A bye – election is the election carried out for replacement of a vacant post.
Conditions that can cause a by – election
 When there is vote of no confidence
 When the elected leader dies.
 When an elected leader has been exiled.
 When an elected leader resigns
Organization of elections
 The organization and releasing of results of elections, at the national level, is the
responsibility of the electoral commission.
Electoral commission
37
 The members of the electoral commission are appointed by the president on advice of
the cabinet ministers and approved by parliament
Duties of the electoral commission
 To organize and supervise elections
 To demarcate constituencies.
 To demarcate polling stations
 To declare the results of the elections
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

<passage id="lchk_c39ba86482504f359b37660b3e5a1d42" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="22">
3. Give two benefits of a small family size.
4. How can the government of Uganda deal with its fast growing population?
Date Class Subject No. of pupils Time
P.5
TOPIC: Population size and distribution in Uganda
SUB –TOPIC: Family planning
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic: sanitation , abortion, polygamy
Content: Family planning
What is family planning?
 Family planning is the spaced way of producing children.
Methods used in family planning
59
 Natural methods
 Artificial methods (use of condoms, injector plan)
Advantages of family planning
 Prevents un wanted births
 Control population explosion
 Improves on the financial status of the family
 It reduces high maternal mortality rate among women
 It helps the family to plan for the children effectively.
Disadvantages of family planning
 It discourages the population growth.
 It brings limited productive man power,
 It reduces tax base in a country.
 It brings shortage of labour force in a home.
Advantages of having a small family
 Easy to plan for
 Easy to provide basic needs.
 Easy to educate the children
 Doesn’t need a lot of land
 Reduces quarrels among family members
 Children enjoy parental love
Disadvantages of small family size
 Shortage of labour
 Shortage of security in a home
 Shortage of income due to less labour force
Activity
1. What is family planning?
2. Why does the government of Uganda encourage family planning?
3. Give two reasons why people have got negative attitude towards family planning.
4. State how a small family is easy to plan for.
60
5. Give one problem that can be caused by small family size.
6. Give two reasons why most families live in poor conditions.
Date Class Subject No. of pupils Time
P.5
TOPIC: Population size and distribution in Uganda
SUB –TOPIC: Population Census
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic: census, population census,
enumerator, statistics, bureau
Content: Population census
a) Population census?
 Population census is the general counting of people in an area.
b) National population census
 National population census is the general counting of people in a country.
c) Census night
 Census night is the night before the census is carried out.
People are advised not to move away from their homes before they are counted for the
following day:
Reasons for carrying out national population census
 To know the number of people and plan for them.
 To know the birth rate and death rate
 To know the rate of population growth
 It helps the government to know the population structure.
Qn. Mention the ministry that carries out national population census
 The ministry of finance, planning and economic development
Qn. Which body in Uganda, carries out national population census?
 The Uganda national bureau of statistics
Information collected during population census
61
 Sex
 Age
 Race
 Marital status
 Religion
 Language
 Level of education
 Types of housing
 Occupation
Note : Uganda had its recent population census in the year 2003
Qn. What title is given to the official who carry out population census.
Enumerators
Problems faced during national population census
 Poor transport in some areas.
 Some people give false information
 Ignorance among some people
 Poor climatic condition some times
Qn. State the period when national population census is carried out.
 It is carried out every after ten years
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
