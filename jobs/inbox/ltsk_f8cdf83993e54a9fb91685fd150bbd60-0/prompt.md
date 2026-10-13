# Job ltsk_f8cdf83993e54a9fb91685fd150bbd60-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 5 lesson(s) below of week 4 of the Social Studies scheme for Primary Five 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P5: one 40-minute lesson: 3–4 ideas; 300–500 words; connected explanations and application; 5–8 activities.

lessonId=lles_529bf896c21648cabee818df6221c4b9: lesson 16, Monday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: Practice: duties of the government and communication — Duties of the government.
  Objectives: Answer exercise questions on duties of the government, social services and communication.
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points (numbered, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

lessonId=lles_3d493ec03f774947852bca69a4619b33: lesson 17, Tuesday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: Sources of government revenue and taxation — Sources of revenue.
  Objectives: Explain what revenue is.; Name the sources of government revenue.; Explain direct and indirect taxes with examples.

lessonId=lles_1d4da50b746348108a2445f276eab1ca: lesson 18, Wednesday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: The Uganda Revenue Authority, why people pay taxes and smuggling — Sources of revenue.
  Objectives: State the roles of URA.; Give reasons why people pay taxes and why some do not.; Explain smuggling, its effects and how it is controlled.

lessonId=lles_14401be165eb46afafc2da17d9cfc70a: lesson 19, Thursday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: Government expenditure and the national budget — Expenditure.
  Objectives: Explain what expenditure is and how the government spends its revenue.; Explain what a budget and a financial year are.; Describe surplus, balanced and deficit budgets.

lessonId=lles_03b1a41f0e4f4154bc98566da660f9fa: lesson 20, Friday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: Practice: revenue, expenditure and budgets — Sources of revenue and expenditure.
  Objectives: Answer exercise questions on revenue, taxes, expenditure and budgets.; Draw a chart showing how government gets revenue and spends it.
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points (numbered, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

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

<passage id="lchk_25c87084edb64ed283eda12ac857fc84" source="P 5 SST Scheme Term III 2019 (ecolebooks Com)" part="4">
of legislative
and Judiciary
-Pictures of
judges
-Resource
person
-Pictures of
High Court
building
Mk std
Bk 5
Page
134
Ecolebooks.com
DOWNLOAD MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
5 1
&
2
LIVING TOGETHER IN
UGANDA
The government of Uganda
Roles of the government -Explaining
the roles of
the
government.
-State the
types of the
gov’t and
their roles.
-spell, read
and
pronounce
and use
words like
roles.
Roles of the gov’t
- Types of the gov’t
-Central government
(National)
-Local government
-Role of the central
government.
-Roles of the local
government.
-Question
and answer
-Discussion
-Explanation
-Role play
-Respect
-Co-operation
-Critical
thinking
-Discussing the
roles of the
government.
-Discussing
how different
types of the
government
carry out their
duties
-Pictures
connected
to the
activities of
the gov’t
Mk
stdbk 5
Page
131
Functio
nal bk 5
Pg 179
3
&
4
LIVING TOGETHER IN UGANDA
The government of Uganda
The Constitution
-Explaining
the term
constitution
-Stating the
functions and
importance
of
constitution
-Read,
pronounce
and use
words
related to
the
constitution
The Constitution
-Meaning
-Functions of the
constitution
-Importance of a
constitution
-The constitutions of
Uganda.
❖ The 1962
constitution
❖ The 1967
constitution
❖ The 1995
constitution
-Description
-Role play
-Discussion
-Explanation
-Brain
storming
-Respect
-Writing
-Sharing
-Reading
-nationalism
-Explaining the
meaning of a
constitution.
-Discussing the
importance of
a constitution
-The school
rules
-hand books
Mk STD
BK 5
Pg
Ecolebooks.com
DOWNLOAD MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
6
5
&
1
The sources of government income
-Explaining
the sources
of
government
income and
revenue
-Spells,
reads,
pronounces
and uses
words
related to
sources of
revenue
❖ Taxation
❖ Value
❖ Donation
s
❖ Tourism
❖ License
❖ loans
-Revenue
-Taxation
Types of taxes
-Examples of taxes
Body responsible for
collecting taxes
(URA)
-Roles of the URA
-Others sources of
government revenue
❖ Grants
❖ Loans
❖ Donations
❖ Fines
❖ Tourism
❖ Sales
❖ Licenses
-Discussion
-Explanation
-Question
and answer
-Sharing
-Writing
-Reading
-Discussing
how the gov’t
earns its
income
-Pictures
and
photograph
s
-License
cards
Mk
stdbk 5
pg 138-
139
6 2
LIVING TOGETHER IN UGANDA
The government of Uganda
The government Expenditure
-Explaining
expenditure
-Discussing
ways how
the gov’t
spends the
revenue
Spells, reads,
pronounce
and uses
words
related to
expenditure
like security
Expenditure
-meaning
- Ways how the gov’t
spends revenue.
❖ Salaries &
allowances
❖ Dev’tprogramme
s
❖ Rent
❖ Security
❖ Social services
❖ Problems in
spending
revenue
-Discussion
-Explanation
-Question
and answer
-Appreciation
-Love
-Sharing
-Co-operation
-Listening
-Discussing
ways how the
gov’t spends its
revenue
-Pictures
connected
to ways how
gov’t spends
its revenue.
Mk
stdbk 5
pg 139
Ecolebooks.com
DOWNLOAD MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
3
&
4
The budget
-Explaining
the term
budget
-Discussing
the different
types of
budgets.
-Discussing
the
importance
of the budget
-spell, read,
pronounce
and use
words
related to
the budget
-surplus
-balanced
deficit
The budget
-Meaning
-Types of budgets
❖ Surplus
❖ Balanced
❖ Deficit
budget
-Importance of the
budget
-Explanation
-Discussion
-Discovery
-Question
and answer
-Drawing
-Care
-Sharing
-Observation
-Drawing the
types of
budget.
-Naming the
parts of the
budget
-Pictures of
different
budgets
Mk
stdbk 5
pg 140-
141
Functio
nal bk 5
Pg 187-
188
5
The Human Rights
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

<passage id="lchk_18c7f38f15a34cac818d9f873981b6a6" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="16">
 This is a group of people who come together to elect a representative.
Write short notes on the following
Suff-rage
 The right to vote in political elections.
Universal adult suf-frage
 The right of all adults to vote.
Elections of a president
Qualifications of a president
 A person to be elected as a president in Uganda must be:
a) A citizen of Uganda.
b) Not less than thirty five years and not more than seventy five years of age.
c) Educated to minimum level of education of senior six
Activity
1. Mention one electoral system that is used in Uganda.
2. State one advantage of the above electoral system.
3. Which electoral system is commonly used in villages?
4. Give one qualification for a person to be elected as a president in Uganda.
5. Give one example of a universal suf-frage election
6. Give one political leader elected through the Electoral College.
Date Class Subject No. of pupils Time
P.5
How elections are conducted
1. Nominating the candidates
2. Registering of voters
3. Giving out of voters cards
4. Civic education
5. Voting on polling day
41
6. Counseling / compiling of votes
7. Announcing and declaring election results
Bad practices before election
1. A voter who registers more than once
2. Giving wrong information about the voter
3. Misdirecting the voters
4. Recording wrong information about voters
5. Making it impossible for voters to vote
6. Unfair splitting of constitutions/ gerrymandering
7. Manipulation of the population make up
8. Blocking candidates from campaigning freely
9. Giving false information about a partner candidate / smear campaign.
10. Threats to voters / candidates by other voters and candidates
11. Bribing voters to win their fowler / vote
Bad practices during elections
- Bribing voters near or at the polling station
- Harassing voters of a particular candidate
- Giving wrong direction to the voters
- Campaigning on the election day
- Giving a voter a pre- ticked ballot paper
- Ballot stuffing
- Grabbing or stealing the ballot boxes.
Bad practice after elections
- Miscounting of votes
- Delay to announce the winners
- Alteration of results
Date Class Subject No. of pupils Time
P.5
TOPIC: The Government of Uganda
SUB –TOPIC: Sources of government revenue
42
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic: revenue, tax, loan, donation,
excise duty
Content:
Meaning of Government revenue
 This is the money that the government collects from various sources.
a) Income
 Income is the money earned by the government or someone (people)
b) Government expenditure
 This is the money spend by the government through the provision of various social services
required by the people.
Sources of government Revenue
 Taxation
 Court fines
 Tourism
 Exports
 Parastatal bodies
 Grants
 Donations
 Loans
Qn. Mention the major source of government revenue
 Taxation/ taxes
Taxes
What is Tax?
 Tax is the money a person or company is asked by the government to pay
OR
 Tax is the money paid to the government by the citizens , organizations and businessmen
Types of taxes
a) Direct tax.
b) Indirect tax
a) Direct tax
 This is the tax paid directly by the people
Examples of direct tax
 Graduated tax
 Income tax
43
(Pay As You Earn/ Income tax)
Graduated tax
 This is the tax paid by any able person who is eighteen years and above.
Groups of people who are exempted from paying tax
 Students
 Prisoners
 People who are mad
</passage>

<passage id="lchk_fd05c8c2ac564ce5a4511b9fe2aa1468" source="Primary Five Social Studies Notes 2020" part="56">
 Written communication
Sources of government income
Revenue
 This is the government income
Income
 This is the amount of money earned
Sources of government income
 Taxes
 Grants
 Donations
242
 Courtfines
 Tourism
 Licenses
 Sales of government properties
 Agricultural exports
 Sale of minerals
 Sales of electricity
Note
 The main source of government revenue in Uganda is taxes/ tax
collection
TRADE
 Taxation is the system of collecting money as taxes
Taxes
 This is money paid by people to the government in order to provide
public services
Types of taxes
 Direct tax
 Indirect tax
Direct tax
 This is tax collected directly from the person who pays it
Examples of direct tax
 Income tax
 Pay as you earn( PAYE)
 Property tax
Income tax
 This is the amount of money paid to the government according to how
much you earn
243
 It is usually paid by civil servants
Pay As You Earn
 It is an example of an income tax
 This is tax paid to the government by the employers from the wages of
their workers
Property tax
 This is tax paid by the people on the commercial buildings they own
Trade
What is trade?
 Trade is the buying and selling of goods
Types of trade
 Home trade
 Foreign trade
Foreign trade
 This is trade carried out across the borders of a country
Home trade
 This is trade carried out within the country
Problems faced by home trade
 High taxation
 Limited market
 Poor transport network
 Poor quality goods
Importance of trade
 It is a source of income
 It provides raw materials to industries
 It is a source of revenue
 It promotes development
244
Define the following
i) Bi – lateral trade
 This is the trade carried out between two countries
ii) Multilateral trade
 This is the trade carried out among many countries
People exempted from paying taxes in Uganda
 Students
 Prisoners
 House wives
 Elders
Indirect tax
 This is the tax imposed on goods bought by buyers
Examples of indirect tax
1. Excise duty
 This is tax paid on locally manufactured goods i.e goods made with in
Uganda
2. Value added tax(VAT)
 This tax is added to the price of goods and services
 This tax is charged on all goods
 It was introduced in 1996 in Uganda
 It is charges as value added to a commodity
3. Custom duty
 This is tax charged on goods that are imported /entering a country
 It is called import tax
NOTE:
245
Grants :
 This is foreign aid given to a country to solve particular problems and
to be paid back without interests
Loan
 This is the money given to a country by another country to promote
development and paid back with interest
Donation
 This is foreign aid given to any country according to the needs a
country may be having and is not paid back
Fine
 This is money charged from people who have been found guilty of
breaking the law with in Uganda
Qn: which tax is charges on the following?
i) Locally made goods
Excise duty
ii) Imports
Customs duty
Qn: What is graduated tax?
 This is tax paid by able adults
Qn: Which tax replaced sales tax and commercial transactions levy (CTL)
 Value added tax
Uganda Revenue Authority (URA)
 URA is the body in charge of collecting taxes in Uganda
Duties of URA
 It collects tax(main)
 It assesses tax payers
246
 Fight smuggling
 Educates the public about the importance of paying tax
 It issued out car number plates
 It gives out trade lincenses
Problems affecting revenue collection
 Smuggling of goods
 Corrupt revenue officers
 Tax defaulting
 Tax evasion
</passage>

<passage id="lchk_b90a97cd7a9b42e7ad9e1945579a049e" source="P.5 Social Studies Lesson Notes Term 3" part="7">
BAD PRACTICES DURING ELECTIONS
 Vote rigging
 Intimidation of voters
 Bribing voters.
ELECTORAL COMMISSION
The electoral commission is the government body responsible for organizing genral
elections in Uganda.
ROLES OF THE ELECTORAL COMMISSION
 Organizing general elections in Uganda
 Supplying voting materials like ballot papers
 Announcing the elected leaders.
 Registering voters
 Vetting candidates.
ELECTORAL OFFICIALS
1- Chairperson electoral commission: heads the electoral commission.
2- The general secretary
3- Returning officer: He is the head of elections in a district.
4- Presiding officer.
5- Polling agents.
ELECTORAL TERMS
 Ballot paper: This is a piece of a paper on which one marks who he/ she is voting for.
 Ballot box: This is a box in which people put their ballots after voting.
 Polling station: This is a place where people go to vote in an election.
 Polling day: This is a day on which people go and vote in an election.
 Polling agent: This is a person who represents a candidate at the polling station.
 Returning officer: This is a person in charge of elections in a district.
 Presiding officer: This is a person in charge of elections at the polling station.
 A constituency: This is an area which is represented in the parliament.
DIVINE EDUCATION CENTRE:0784540287/0751565742 Page 20
 Electoral College: This is a group of people who are chosen to represent the rest of
the members of a political party.
 Elector: This is a person who has a right to vote in an election.
 Election constable: This is a police officer in charge of security at a polling station.
 Election monitor: This is a local person who supervises elections.
 Election observers: These are people who supervise elections.
The ministry of Justice and constitutional affairs.
General elections in Uganda are held every after 5 years.
A voter in Uganda must be 18 years and above and registered with the electoral
commission.
NATIONAL REVENUE AND EXPENDITURE
Revenue is the government’s income.
Expenditure is the way how money is spent.
SOURCES OF NATIONAL REVENUE.
Taxes, loans, grants, donations, court fines, tourism, exports, privatization
1- TAXES:
A tax is a sum of money paid to the government to provide social services.
Types of taxes
a) Direct tax
This is a type of tax which people pay directly.
Examples of Direct taxes
i) Income tax
ii) Graduated tax
iii) Pay as you earn (PAYE)
The major source of government revenue is taxation.
b) Indirect tax
This is the type of tax paid on goods and services indirectly.
Examples of indirect taxes.
i) Excise duty
ii) Customs duty (import tax)
iii) Value added tax (VAT)
iv) Court fees
DIVINE EDUCATION CENTRE:0784540287/0751565742 Page 21
v) licenses
Excise duty
This is the type of tax charged on goods made within a country.
Customs duty
This is the type of tax charged on goods entering a country. It is also called import tax.
Value added tax
It is a tax paid by people who buy certain commodities.
Court fees
This is the money a person pays to court when he is registering a case.
License fees
This is money paid to the government in order to be allowed to operate a business.
2- LOANS
This is the money the government borrows to be paid back with interest.
Sources of loans
- The world bank
- International monetary fund (IMF)
- East African Development Bank
- African Development Bank
- Rich countries
3- GRANTS
This is the money given to a country to solve a particular problem. This money is paid
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
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
