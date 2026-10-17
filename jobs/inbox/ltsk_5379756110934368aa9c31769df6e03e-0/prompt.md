# Job ltsk_5379756110934368aa9c31769df6e03e-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 5 lesson(s) below of week 6 of the Social Studies scheme for Primary Five 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P5: one 40-minute lesson: 3–5 sections; about 14–28 points (meaning, examples, reasons, problems and solutions as the passages give); 5–8 activities.

lessonId=lles_0e3d74135c0f4f6f80b4d30ff78ae628: lesson 26, Monday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: Sources of government revenue — The URA and other sources of government revenue.
  Objectives: State the roles of the Uganda Revenue Authority; Name other sources of government revenue

lessonId=lles_15330e8405cb4dee8ac9ab3d4833090b: lesson 27, Tuesday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: Government expenditure — How the government spends its revenue.
  Objectives: Define expenditure; State ways the government spends its revenue and problems in spending it

lessonId=lles_a16157293c3a451cae534b029ef86937: lesson 28, Wednesday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: The national budget — Meaning and types of budgets.
  Objectives: Define a budget; Name the types of budgets

lessonId=lles_802e6f2f3cde4c4c8750e1423d4f2f27: lesson 29, Thursday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: Importance of the budget — Surplus, balanced and deficit budgets.
  Objectives: Explain surplus, balanced and deficit budgets; State the importance of a national budget
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points ('- ' points, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

lessonId=lles_1ad6e9d8b9cf42f0a2107524966a7bdd: lesson 30, Friday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: Human rights — Rights of a citizen and the Uganda Human Rights Commission.
  Objectives: Name the rights of a citizen; State the roles of the Uganda Human Rights Commission

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

<passage id="lchk_75679631316b42868d58f327c564a4ad" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="18">
 It must be economical to administer . It should earn more money than that costs to collect.
( incurred in collecting it)
 It should be convenient to pay.
Activity
1. Give two reasons why it is important for the people to pay tax.
2. Give two factors that may discourage people from paying tax,.
3. Give two problems that the government is most likely to face when people don’t pay.
4. How does the government of Uganda spend its income?
5. Mention one way public funds are being misused
6. Outline any two qualities of a good tax.
Date Class Subject No. of pupils Time
P.5
TOPIC: The Government of Uganda
SUB –TOPIC: Types of budgets
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic: budget, surplus, expenditure,
deficit
Content: Budget
What is a budget?
 This is the estimation of income and expenditure for a given period of time.
Parts of a budget
 Income
 Expenditure
Types or a budget
 Surplus budget
 Balanced budget (profit budget)
 Deficit budget (Loss budget)
47
Surplus budget
 This is the type of budget where the income is greater than the expenditure
 The surplus budget can be calculated by subtracting expenditure from income
Income Expenditure Surplus
8m - 5m = 3m
Illustration of a surplus budget
Expenditure Income
Advantages of a surplus budget
 It encourages development in a country.
 It enables the country to modernize infrastructure and agriculture.
 It prevents debts in a country.
 It prevents over dependence on foreign aid.
Balanced budget
 This is when the income and expenditure are equal.
 It has neither surplus nor debts
Deficit budget (loss budget)
 This is when the expenditure is greater than the income
Diagram
48
Disadvantages of a deficit budget
 A deficit budget brings the country in debts
 It makes a country depend on other countries for foreign aid.
 It limits the government from providing the necessary services to the citizens as a
required.
 It discourages development and progress in a country.
Ways of servicing the deficit budget
 Diversifying the economy
This means creating more sources of foreign exchange.
 Widening the tax base
This means enlarging the taxable areas as much as possible
 Through getting donations and grants
 Through getting loans
 Though privatization of the economy
Activity
1. What is a national budget?
2. Why should the government of Uganda carry and national budgeting?
3. Why would you advise Kirabo a P.5 child at Cornerstone to budget for her pocket money
before spending?
4. If you were a minister of finance, planning an economic development, what type of
budget would you prefer for your country to have?
5. Give a reason for your answer.
6. What is privatization
Date Class Subject No. of pupils Time
P.5
TOPIC: The Government of Uganda
SUB –TOPIC: problems of revenue collecting
LANGUAGE COMPETENCE :
49
The learner:- Spells and uses words related to the sub -topic: corruption, smuggling, defaulting
Content:
Problems faced during revenue collection
 Smuggling of goods which leads to low revenue collections.
 Tax defaulting among traders and some organizations.
 Corruption among the revenue officers who bribe and under value some goods.
Solutions to the problems
 The government set up the special revenue protection service to curb smuggling.
 The government can improve on the methods of collecting tax.
 Honest and faithful revenue officers would be employed.
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

<passage id="lchk_0e9d4c93cd8f4cc4a7ae4e92a9bb8b7c" source="P.5 Social Studies Lesson Notes Term 3" part="8">
back without interest.
4- DONATION
This is an assistance given to a country according to its needs. The donations are not
paid back.
Examples of donations:
 Finance assistance
 Material assistance
 Equipment assistance
5- COURT FINES
This is the money paid by a person who has been found guilty for breaking the law.
HOW THE GOVERNMENT SPENDS MONEY
- BY paying salaries
- By constructing roads
DIVINE EDUCATION CENTRE:0784540287/0751565742 Page 22
- By building schools
- By extending electricity to rural areas.
- By buying drugs.
Challenges faced by government while collecting taxes.
 Lack of enough labour
 Political interference in tax collection
 Corrupt tax collectors
 Smuggling of goods into the country.
 Low tax base
 People dodge paying taxes
 Ignorance
Smuggling of goods
This is illegal importation and exportation of goods.
Disadvantages of smuggling goods.
 It allows expired goods to enter the country.
 It reduces the government revenue
 It allows substandard goods to enter our country.
 It kills market for the locally manufactured goods
THE UGANDA REVENUE AUTHORITY (URA)
This is the government’s body responsible for collecting taxes.
URA is under the ministry of finance and economic planning.
Functions of URA
- It collects taxes
- It assesses taxes
- It fights smuggling.
- It educates people on the importance of paying taxes.
- It issues number plates to vehicles
Note : The Uganda National Bureau of Standards (UNBS) promotes standards of goods in
our country.
Special revenue protection service (SRPS) fights smuggling of goods in Uganda.
DIVINE EDUCATION CENTRE:0784540287/0751565742 Page 23
A NATIONAL BUDGET
A national budget is a country’s estimate of income and expenditure.
A BUDGET
Is an estimate of income and expenditure for a good time.
The financial year begins 1 st July and ends on 30 th June the following year.
Types of budgets
1- Surplus budget 2- Balanced budget 3- Deficit budget
SURPLUS BUDGET
This is the type of budget where the income is grater than the expenditure.
Advantages of a surplus budget.
1- It does not lead to debts
2- It encourages development in a country.
Note: A surplus budget is calculated by subtracting expenditure from income i.e
8million – 5 million = 3 million.
Expenditure income
5millions 8millions
A balanced budget: This is the type of budget where the income is equal to the
expenditure.
3 million 3 million
income expenditure
DIVINE EDUCATION CENTRE:0784540287/0751565742 Page 24
Advantages of a balanced budget
A balanced budget does not lead to debts.
A DEFICIT BUDGET
Is a type of budget where the expenditure is greater than the income.
Disadvantages of a deficit budget
- It leads to debts
- It leads to under development in the country.
Note : Most African countries have got deficit budgets.
5m expenditure
income 2m
How the government can solve the problem of a deficit budget
 By increasing taxes
 By creating more sources of income
 By getting grants
 By getting loans
 By reducing luxury expenditure
DIVINE EDUCATION CENTRE:0784540287/0751565742 Page 25
TOPIC :4
POPULATION, SIZE AND DISTRIBUTION
Population size and distribution in Uganda and their relationship to economic
planning and development
 Population is the number living in an area at a particular time
Population distribution
 Population distribution refers to the way people are spread in an area
Factors that affect population distribution
 Relief of the area
 Rainfall availability
 Soil drainage and fertility
</passage>

<passage id="lchk_361554dd9b104fc5b63f30a6d1205302" source="Primary Five Social Studies Notes 2020" part="57">
Solution to problems facing
Note
 Customs for enforcement unit has been set up to fight smuggling in
Uganda
Dangers of smuggling
 It leads to low revenue collection
 Expired goods can be imported into the country
 It lowers market for locally made goods
 Dangerous and poor quality goods can be imported
Solution to smuggling
 Arrestling and prosecuting smugglers
 Enforcing laws against smuggling
 Imposing fair taxes on goods
BUDGET
A budget is an estimate of income and expenditure for a given time
National budget
 A country’s estimate of income and expenditure for a given financial
year
247
Finacial year/ fisical year
 This is a period in which a national budget is implemented
Parts of a budget
 Income
 Expenditure
 Income This is money earned
Expenditure
 This is amount of money to be spent
How the government spend its revenue
i) Paying salaries and pensions
ii) Repayment of loans
iii) Maintaining and constructing roads
IV) Buying weapons
v) Buying medicine
vI) Providing education services
Why is budgeting important to a country?
It helps government to identify sources of income
It helps government to cater for priorities
To prevent money misuses
Qn: Name the body that prepares a national budget
 National Planning Authority
Qn: Identify the ministry responsible for preparing a national budget
 Ministry of finance , planning and economic development
Qn: Which arm of government approves a national budget
 Legislature
248
Qn: Name the arm of government that prepares a national budget
 Executive
Qn: What is family budget?
 A family budget is an estimates of income and expenditure for a family
Types of budget
 Surplus budget
 Balanced budget
 Deficit budget
SURPLUS BUDGET/ SAVING BUDGET
 This is the type of budget where income is more than expenditure
Advantages of surplus budget
 Limits debts and borrowing
 Promotes saving and investment
 Promotes development
 It encourages proper service delivery
Diagram showing surplus budget
Shopping bill
249
A drian had Uganda shillings 50,000/= He bought the following items after
preparing his budget
a) Food 10,000/=
b) Drinks 15,000/=
c) Clothes 10,000/=
d) Saving 15,000/=
Qn: Which type of bought did Adrian prepare
 Surplus budget
Qn: Given the reason to support the answer given above
 The income is greater than the expenditure
Qn: How much money did he spend?
15000/=
BALANCED BUDGET/ EQUILIBRIUM BUDGET
This is the type of budget where by income is equal to expenditure
Diagram showing balanced budget
250
Advantages of balanced budget
 It limits debts
 It promotes development
DEFICIT BUDGET
 This is the type of budget where by the expenditure is greater than the
income
Causes of a deficit budget
 Falls in price of exports
 Constant wars
 Corruption
 Unreliable sources of income
 Failure to exploit natural resources
 Smuggling of goods
Disadvantages of deficit budget
 It leads to debts
 Limits savings and investments
 It leads to over dependence
 Promotes poor living standards
Solution to problems caused by a deficit budge
 By creating more tax avenues
 Promoting tourism
 Modernizing agriculture
 By encouraging foreign investors
 By diversifying the economy
 By carrying out privatization
Diagram a deficit budget
251
The rights of citizens
Rights
These are natural freedoms that people must enjoy
Human rights
These are basic freedoms of human beings must enjoy
Qn: Which body protects human rights in Uganda?
Uganda Human Rights Commission (UHCR)
</passage>

<passage id="lchk_6dd64f60202a49f7807c72cd6775b286" source="Excel P 5 SST Term III" part="20">
❖ By encouraging children to behave well.
Page 37
❖ By enforcing laws against child abuse.
HUMAN RIGHTS
Human rights are basic natural freedoms to which all people are entitled.
These are natural freedoms that people must enjoy.
Examples of fundamental human rights
▪ The right to life
▪ Freedom from discrimination.
▪ Freedom from slavery.
▪ Freedom from unfair detainment.
▪ The right to trial.
▪ Freedom from torture.
▪ We are all equal before the law.
▪ Freedom to move.
▪ The right to seek a safe place to live in.
▪ Right to a nationality.
▪ The right to own property.
▪ Freedom of thought.
▪ Freedom of expression.
▪ The right to democracy.
▪ Right to social security.
▪ The right to education.
▪ The right to food and shelter.
▪ The right to play.
▪ Every grown up has the right to do a job.
▪ Every grown up has the right to marry.
Human rights violation
This is the denial of the basic human freedoms people are entitled to.
Forms of human rights abuse
▪ Torturing of political opponents.
▪ Raping of women.
▪ Killing of political opponents.
▪ Slavery.
▪ Mob justice.
▪ Denial of the freedom of movement.
▪ Imprisonment without trial
▪ Death penalty.
How the government can protect people against the human rights violation.
❖ By teaching people about their rights.
❖ By enforcing laws against human rights abuse.
❖ By promoting peace and security in the country.
❖ By forming organisations that ensure the protection of human rights.
Note: The Uganda Human Rights Commission (UHRC) was set up in Uganda to
ensure protection of human rights
Roles that can be played by the citizens in preventing the human rights violation.
❖ By respecting other people’s rights.
❖ By reporting the cases of human rights abuse.
❖ By helping the police in arresting people who violate human rights.
❖ By sensitising other people about their rights.
Duties of the Uganda Human Rights Commission.
❖ To educate the citizens about their rights.
❖ To investigate the violation of human rights.
❖ To promote human rights.
❖ To receive complaints from people who feel that their rights have been violated.
Page 38
CHILD LABOUR
Child labour is when children are employed to do work.
Children are paid money/wages/salaries after performing such heavy tasks.
Forms of child labour.
❖ Carrying heavy goods for other people.
❖ Employing children as house maids.
❖ Working in building sites.
❖ Doing a lot of domestic work.
❖ Employing children in mines.
❖ Offering children for prostitution.
❖ Tasking them to sell goods as hawkers.
❖ Employing them in stone quarries.
Causes of child labour.
❖ Poverty
❖ Child neglect by the parents.
❖ Desire for money by the parents
❖ Death of parents.
❖ Need for cheap labour provided by the children.
❖ Limited number of family members.
Dangers of child labour.
❖ It can lead to early marriages.
❖ It leads to high risks of diseases.
❖ It can leasd to death of children.
❖ It leads to school dropouts.
❖ It can lead to body injuries.
❖ It can lead to stunted growth among
children.
Ways of controlling child labour.
❖ By enforcing strict laws against child labour.
❖ By educating people about the dangers of child labour.
❖ By promoting developmental programmes to eliminate poverty.
❖ By sensitising people to use family planning practices in order to produce children
they are able to care for.
❖ By providing free formal education to keep children in schools.
❖ By encouraging people to care for their children.
Testing Exercise.
1. What is a Government?
</passage>

<passage id="lchk_308194d2a0674ce7b8a2824efae4d3b8" source="Excel P 5 SST Term III" part="18">
Surplus budget is a type of budget where by the income is greater than the
expenditure.
The amount of money earned is more the amount spent.
A diagram showing a Surplus budget.
Importance of a surplus budget.
❖ It promotes development.
❖ It encourages saving and investment.
❖ It limits debts.
❖ It improves people’s living standards.
(ii) Balanced budget.
A balanced budget is a type of budget where by the income equal to the
expenditure.
It has neither a surplus nor debts. JJJJJJJJ
50M
20M
expenditure
income
Page 33
A diagram showing a Balanced budget.
(iii) Deficit budget.
A deficit budget is a type of budget where by the expenditure is more income.
The amount of money earned is less than the amount of money spent.
Under developed countries like Uganda usually make this type of budget.
A diagram showing a Deficit budget.
Causes of a Deficit budget.
▪ Corruption.
▪ Failure to exploit natural resources.
▪ Smuggling of goods.
▪ Fall in prices of goods.
▪ Constant civil wars.
▪ Lack of reliable sources of income/ limited investment.
Dangers of the deficit budget.
❖ It leads to debts.
❖ It limits saving and investment.
❖ It leads to over dependence. HHH
kkk
50M 50M
income expenditure JJJJJJJJ
50M
20M
income
expenditure
Page 34
❖ It limits development.
❖ It limits services the government provides to people.
Solutions to the deficit budget.
❖ By widening the tax base.
❖ By diversifying the economy of the country.
❖ By privatisation.
❖ By mechanising agriculture.
❖ By getting loans from international institutions.
❖ By encouraging foreign investors in the country.
GOVERNMENT EXPENDITURE.
This refers to the ways how the government spends its income.
How the government spends its revenue.
❖ By building schools.
❖ By providing education services.
❖ By paying salaries for civil servants.
❖ By paying back loans and grants.
❖ By buying weapons.
❖ By funding developmental programmes like Operation Wealth Creation, NAADS.
❖ By constructing roads in the country.
❖ By helping people hit by disasters eg. refugees.
❖ By providing health services.
RIGHTS AND RESPONSIBILITIES OF CITIZENS
CITIZENSHIP:
Citizenship is the legal right of belonging to a particular country.
A citizen is a person who has the legal right of belonging to a particular country.
How one acquires citizenship of Uganda.
❖ Through birth (is the legal right of belonging to a country when one’s parents are
citizens in that particular country)
-it is acquired by people born by parents who are Ugandans.
❖ Through descent (is the legal right of belonging to a country a person gets when
his / her ancestors were citizens in that country)
❖ Through registration. (is the legal right of belonging to a country granted to a
foreigner who has applied for citizenship in a particular country)
-In Uganda, this registration is done under the Ministry of Internal affairs.
eg.if a woman who is not a Ugandan gets officially married to a Ugandan, she can
apply to become a citizen and she is registered.
❖ Through naturalisation (is the legal right of belonging to a country granted to a
person after having spent a very long time in a particular country)
❖ Through adoption. (is the legal right of belonging to a country granted to
foreigner who was brought up by a person who is a citizen in a particular country)
-It is granted to children below 18 years of age whose parents are not known and
have been adopted by citizens of Uganda.
Page 35
Factors that determine one’s citizenship.
▪ Area of birth
</passage>

<passage id="lchk_982495b08d4d48d2a5231b80808ea485" source="Excel P 5 SST Term III" part="17">
Groups of people exempted from paying direct taxes.
▪ Prisoners
▪ House maids
▪ Elderly people
▪ Students
(b) Indirect tax.
This is the tax paid by the final consumers of the commodities.
It is passed on by thye traders to the consumers (final users) in form of price
increase.
Examples of indirect taxes.
(i) Customs duty tax.
➢ This is tax paid on imports/ goods entering a country.
➢ It is also called import tax.
(ii) Excise duty tax.
➢ This is tax paid on locally manufactured goods/ goods made within the
country.
(iii) Value Added Tax (VAT).
➢ This is tax paid by all people who buy goods and services.eg. When paying
for water, electricity, telephones, cars, shoes etc.
➢ VAT is charged on imports, manufactured goods, goods supplied for sale and
on services.
➢ It is charged as value added to a commodity.
Why people should pay taxes.
❖ To provide money to support government programmes.
❖ To provide money to pay civil servants.
❖ Government raises money to provide social services.
Why some people do not pay taxes.
❖ They lack knowledge about tax education.
❖ Taxes are too high.
❖ Some revenue collectors are corrupt.
Page 31
THE UGANDA REVENUE AUTHORITY (URA)
This is the body responsible for collecting taxes
in Uganda.
It assesses tax payers and also educates the
public about the importance of paying taxes.
Roles of the URA.
❖ To collect taxes.
❖ To assess the tax payers.
❖ It conduct tax education.
❖ It controls smuggling.
Problems faced by the URA.
❖ Smuggling of goods.
❖ Tax evasion/tax defaulting.
❖ Corrupt revenue officers.
❖ Declaration of false goods.
Possible solutions to the problems facing URA.
❖ By educating the public on the importance of paying taxes.
❖ By paying attractive salaries to revenue officers.
❖ By employing honest revenue officers.
❖ By punishing corrupt revenue officers.
❖ By imposing fair taxes on tax payers.
SMUGGLING.
Smuggling is the illegal importation and exportation of goods.
Special Revenue Protection Services (SRPS) has been set up to control/ curb
smuggling in Uganda.
SPRS replaced the Anti-smuggling Unit.
Dangers of smuggling.
❖ It reduces tax income.
❖ It may lead to importation of low quality goods into the country.
❖ It lowers market for locally manufactured goods.
❖ Expired goods can be imported into the country.
Ways of controlling smuggling.
❖ By enforcing laws against smuggling.
❖ Reducing on taxes paid on goods.
❖ By employing honest revenue officers.
❖ By supporting the work of the Special Revenue Protection Services (SRPS).
BUDGETING.
A Budget is an estimate of income and expesonditure for a given time.
A National budget is a country’s estimat e of expected income and expenditure for
a financial year.
A financial year is a planning year for the government.
URA Tower located at Nakawa
Page 32
In Uganda, a financial year begins on 1 st July and ends on 30 th June the following
year.
The Ministry of Finance, Planning and Economic development is responsible for
preparing a National budget in Uganda.
Parts of a budget.
▪ Income. This is the amount of money earned..
▪ Expenditure. This is the amount of money spent.
Importance of making a National budget.
❖ It helps the government to identify the sources of income.
❖ It helps the government to cater for priorities.
❖ It helps the government to avoid unplanned expenditure.
❖ It promotes proper planning.
❖ It promotes accountability.
Types of budgets.
▪ Surplus budget
▪ Balanced budget
▪ Deficit budget.
(i) Surplus budget.
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
