# Job ltsk_ff64a6e1de8b415eade24a8bce369fd0-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 5 lesson(s) below of week 9 of the Social Studies scheme for Primary Five 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P5: one 40-minute lesson: 3–5 sections; about 14–28 points (meaning, examples, reasons, problems and solutions as the passages give); 5–8 activities.

lessonId=lles_18f4bea3ecac4c18aad6b5bd4737a766: lesson 41, Monday, 1 period(s), 40 minutes.
  Unit: Population, Size and Distribution (theme: Living together in Uganda). Lesson: Hazards that check population growth — Natural and man-made hazards.
  Objectives: Name natural hazards that check population growth; Name man-made hazards that check population growth

lessonId=lles_f5c63946b6f14a26804d4d3021a38cc6: lesson 42, Tuesday, 1 period(s), 40 minutes.
  Unit: Population, Size and Distribution (theme: Living together in Uganda). Lesson: Population terms — Summary of population terms.
  Objectives: Explain population terms such as over population and under population; Use population terms correctly

lessonId=lles_d4a41884dbc6431fa7db7963bca08462: lesson 43, Wednesday, 1 period(s), 40 minutes.
  Unit: Uganda as an independent nation (theme: Living together in Uganda). Lesson: Revision: Uganda as an independent nation — Revision and practice.
  Objectives: Revise and practise the main points of Uganda as an independent nation
  This is a REVISION lesson for the unit. notes = the unit's key points under ### headings ('- ' points), then '### Exercise' with practice questions taken from the passages. activities = those questions.

lessonId=lles_29608edb52284b84815abca6d9204b78: lesson 44, Thursday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: Revision: The Government of Uganda — Revision and practice.
  Objectives: Revise and practise the main points of The Government of Uganda
  This is a REVISION lesson for the unit. notes = the unit's key points under ### headings ('- ' points), then '### Exercise' with practice questions taken from the passages. activities = those questions.

lessonId=lles_14aa97868f904a259dfd0b60a9577f64: lesson 45, Friday, 1 period(s), 40 minutes.
  Unit: Population, Size and Distribution (theme: Living together in Uganda). Lesson: Revision: Population, Size and Distribution — Revision and practice.
  Objectives: Revise and practise the main points of Population, Size and Distribution
  This is a REVISION lesson for the unit. notes = the unit's key points under ### headings ('- ' points), then '### Exercise' with practice questions taken from the passages. activities = those questions.

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

<passage id="lchk_3b379eae4956473980abd2ec5698fb8d" source="Excel P 5 SST Term III" part="16">
❖ It guides the government when making national policies.
❖ It promotes good governance.
Relationships between the constitution and elections.
❖ The constitution defines the duration for conducting elections.
❖ It sets conditions for aspiring candidates.
❖ It sets conditions to participate in elections.
❖ It states the functions of the electoral commission.
COMMUNICATION.
Commulnication is the sending and receiving of messages.
Traditional ways of communication.
▪ Use of drums
▪ Ululation
▪ Clapping hands
▪ Use of horns
▪ Use of smoke signals
▪ Whistling
▪ Sending special messengers
Modern ways of communication.
▪ Radio
▪ Television
▪ Billboards
▪ Telephones
▪ Magazines
▪ Newspapers
▪ Letters
Note.
✓ Mass media is the sending of messages to many people at the same time.
✓ Means of mass media communication include; radios, televisions, newspapers
✓ All media services are regulated by the Uganda Communications
Commission ( UCC) .
Barriers to effective communication in Uganda.
▪ High taxes imposed on the
communication companies.
▪ Illiteracy among the people.
▪ Arrests and torture of journalists.
▪ Poverty among people.
▪ Communication barrier.
▪ Poor network coverage.
▪ Poor transport network.
▪ High cost of communication means.
Page 29
Possible solutions to the barriers of communication.
❖ By introducing a national language.
❖ By providing free education for all Ugandans.
❖ By lowering the cost of communication means.
❖ By charging low taxes on communication companies.
❖ By constructing and maintaining good transport network.
❖ By regulating the work of communication companies.
Importance of communication.
❖ It promotes trade.
❖ It promotes national unity.
❖ It promotes peace in the country.
SOURCES OF GOVERNMENT REVENUE.
Government revenue means government’s income.
Government’s income is all the money earned by the government in a given time.
The main source of revenue of the government of Uganda is taxation.
Sources of government revenue.
▪ Taxation.
▪ Grants.
▪ Loans.
▪ Donations.
▪ Sale of electricity
▪ Tourism.
▪ Court fines and traffic fines.
▪ Licences.
▪ Sale of minerals.
▪ Agricultural exports.
▪ Sale of parastatal bodies.
Note:
✓ Grant is a sum of money given to the government to solve particular problems and to
be paid back without interest.
✓ Loan is the money a country borrows from another country or international financial
body and is paid back with interest.
✓ Donation is the foreign aid given to a country according to its needs eg.materials,
finances, equipment. Donations are not paid back.
✓ Fine is themonhey charged from people who have been found guilty for breaking the
law.
✓ Licence is an official document which gives permission for one or an organisation to
carry out business.
TAXATION.
Taxation is the system of imposing taxes on people.
Taxes is all money paid to government by the people and their business or
organisations in order to provide public services.
It is the charge against a person, property or activity for the support of
government.
Types of taxes paid in Uganda.
▪ Direct tax
▪ Indirect tax.
Page 30
(a) Direct tax
This is the tax collected directly from the person who pays it.
Examples of direct taxes.
(i) Property tax.
➢ This is the tax paid by the people on the commercial buildings they own.
(ii) Income tax.
➢ This is the type of tax paid by people according to how much they earn. The
salary earners (workers) pay this tax every month using a method of Pay As
You Earn (PAYE).
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

<passage id="lchk_a8d263adf25145d9b9a94e0acaa20555" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="1">
1
P.5 SST LESSON NOTES FOR TERM III
Date Class Subject No. of pupils Time
P.5
TOPIC: Uganda as an Independent nation
SUB –TOPIC: The Independence of Uganda
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic:- Nation, independence, state,
Freedom, foreign
Content: Independence
The independence of Uganda
a) The meaning of independence
 Independence is when a country is free from foreign political, social and economic
influence.
 It is when the highest power in a country is transferred into the hands of the citizens.
When did Uganda get her independence?
 Uganda got her independence on Monday 9 th October 1962.
What conference was the climax of all Uganda’s struggle for independence?
 It was the London constitutional conference.
Who was the first prime minister of independent Uganda?
 Apollo Milton obote
Who was the first president of Uganda in 1963?
 Sir Edward Muteesa II
Who was the first non executive president of Uganda?
 Sir Edward Muteesa II
Name the first vice president of the non executive Uganda?
 He was Wilberforce Nadiope
Who had power to appoint ministers in Uganda in 1964?
 The prime minister had power to appoint ministers in Uganda in 1964
A nation
The meaning of a nation
 A nation is a large community of people united by common aspiration/ aims which
makes them to want to be under one government.
 A group of people with the same history, culture and language under one government.
2
Type of a nation
 Heterogenous nation
 Monolithic nation
Heterogenous nation
 These are nations composed of different groups of people with different culture, origin
and languages but share the same territory.
Examples of Heterogenous nations
 Uganda
 Kenya
 Tanzania
 Nigeria
Monolithic nations
 These are nations with a common origin, langauge, history, and cultural institutions.
 These are nations made up of people of the same ethnic group.
Examples of monolithic nations
 Rwanda
 Burundi
 Swaziland
 Lesotho
 Saudi Arabia
Characteristics of a nation
 It has a common culture.
 It has a common language
 It shares a common ethnicity or heritage
 Has a common desire.
A STATE
What is a state?
 A state refers to a country considered as an organized political community controlled by
one government.
Characteristics of a state
 It has a national leader.
 It is not controlled by any other country
3
 It has clearly marked boundaries
 Its citizens should have a sense of belonging
 It has its own citizen.
 It has control over all its territorial areas.
Uganda becomes a republic
What is a republic?
 A republic is the country governed by its own laws with a president as the head of state.
Name the president who abolished kingdoms in Uganda in 1967?
 Apollo Milton Obote
In which year was Uganda declared as a republic
 It was in 1967
Activity
1. What is political independence?
2. How did World War II contribute towards Uganda’s independence? Give three ways.
3. When did Uganda get her independence?
4. How did Ben Kiwanuka became Uganda’s first chief minister?
5. What was Kabaka crisis?
6. What failed Ben Kiwanuka from becoming the first Prime minister of independent
Uganda?
7. What enabled Obote to become the first Executive Prime Minister of Uganda?
8. Who was the first Republican president of Uganda?
9. What political even took place in Uganda in 1967?
10. Give two characteristics of monolithic nations.
11. Why is Uganda regarded as a heterogeneous nation?
</passage>

<passage id="lchk_b297e6921590437280a1192ded841240" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="4">
How many stanzas has the Uganda national anthem?
 There three stanzas of the Uganda national anthem.
The National Anthem
1. Oh Uganda! May God uphold thee,
We lay our future in thy hand,
United free for liberty,
Together we’ll always stand.
2. Oh Uganda! The land of freedom,
Our love and labour we give,
And with neighbours all,
At our country’s call,
In peace and friendship we’ll live.
3. Oh Uganda! The land that feeds us,
9
By sun and fertile soil grown,
For our own dear land
We shall always stand
When and how the stanzas of the national anthem are sung?
 At the opening of any function of national importance.
Messages of the National Anthem
 Belief in one God.
 Determination to remain free from foreign control.
 Desire to live at peace with our neighbours.
 To remind people about the fertile soil and favorable climate of Uganda.
Respect for the National Anthem
 When the national anthem is being sung all the people should stand still or at attention and
remain in one place until it is completed.
Reasons why we should respect the National Anthem when it is being sung
 To pray to God for our nation
 To respect our nation, which is more important than all other things in the country
 To remind us f our national duties
 It shows national unity
The importance of the national anthem during national anthem occasions
 To express the national beliefs of the nation
 To show national identify
 To remember the rich environment of Uganda
 To promote unity among the people
Activity
1. Why is Late. George William Kakoma remembered in the history of Uganda.
2. Give two reasons why Ugandans sing the national anthem
3. Apart from the national anthem, outline two other attributes of a nation.
4. When was the national anthem played for the first time in Uganda?
10
5. Give one way school children express the spirit of nationalism when on assemblies.
6. In which stanza of the Uganda National Anthem is the statement;
a. At our country’s call?
b. United free for Liberty?
c. By sun and fertile soil grown?
7. How is the National Anthem respected when its being sung?
Date Class Subject No. of pupils Time
P.5
TOPIC: Uganda as an Independent nation
SUB –TOPIC: The Uganda national flag
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic:- black, yellow, red, flag, crested
crane
Content: The Uganda national flag – Signifies unity among Ugandans
 Before getting independence. Uganda used the British flag known as the union jack
How was the union jack treated on 9 th October 1962?
 The Union Jack was lowered and Uganda national flag was raised.
Who was responsible for the ceremony of lowering the union jack and raising our flag?
 He was major Kanuti Akorimo
When was the Uganda National flag first raised?
 The Uganda National flag was first raised on Monday 9 th October 1962?
Who designed the Uganda national flag?
 Grace Ibingira assisted by Paul Mukasa
The colours of the Uganda national flag
 The Uganda national flag has three colours. Namely;
 Black
 Yellow
 Red
Meaning of each colour
A: THE BLACK COLOUR
 The black shows Uganda as a black African country.
 It signifies that Ugandans are dark skinned people / Africans
11
B: THE YELLOW COLOUR
 What does the yellow colour symbolize?
 The yellow colour symbolizes sun shine.
 It shows that the Equator passes through Uganda and therefore country enjoys sunshine
throughout the year.
C: THE RED COLOUR
 The Red colour signifies international brother hood.
</passage>

<passage id="lchk_3dedebb31c1e4c9783852eb0a4fc6cfb" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="5">
How does the red colour in our national flag foster unity among Ugandan?
 It shows that all people regardless of race, colour, language , religion, cultural and social
back grown have same colour of blood.
 It emphasizes international brother hood.
THE UGANDA NATIONAL FLAG
THE CRESTED CRANE
 This is Uganda’s national emblem
 It is the visible symbol that represents a nation
Why does a crested crane stand on one leg?
 It shows that Uganda is moving forward in terms of development.
Reasons why the crested crane was chosen as Uganda’s Emblem
 The crested crane has the three colours of the national flag.
 It is a gentle bird.
 It is graceful
 It is a beautiful bird.
What does the crested crane represent?
 It represents gracefulness, beauty and peacefulness of the people of Uganda.
 It represents the gentility of the people of Uganda.
12
Why is a national flag important to our country?
 The national flag promotes national unity.
 It is for identification.
Ways through which the National Flag is used
 The national flag should be raised early in the morning on public buildings and in places
where national or official duties/ activities are taking place and lowered late in the evening.
 The flag must be flown with the Crested Crane facing the flag pole.
 The flag is raised at a half mast when an important person died or there is a national disaster.
 Some people match following bands like school band, Army, Police etc to demonstrate a
cause of national interest bands carry flags and should be held in front of those maching.
 The national flag is flown on president’s car, ministers and judges’ cars when these officers
are travelling.
Taking care of the National flag
 Our national flag must always be respected.
 The flag should never be allowed to touch and anything below it such as ground or water.
 It should never have anything placed upon it or pinned on to it.
 The flag should never be used for commercial advertising.
 The flag is not supposed to be used as clothing.
 When it is raised or brought down the people near the flag pole should stop moving until the
flag is up or held by the person in charge.
Examples of places where the national flag is flown
 The parliament
 Official car of the president while traveling and other government officers.
 Government departments/ offices
 The office of the resident district commissioners.
 Institutions of learning, such as schools.
 Individuals can also hand the nationals flag in their offices, in class or on their tables
Activity
1. What is the name of the bird in the middle of the Uganda flag?
2. Of what importance is a flag pole?
3. Give one way the National flag is respected.
4. How does the red colour of the Uganda promote unity world wide?
13
5. Identify the last colour of the Uganda National flag.
6. Give two importance of A national flag.
7. Which school attribute is similar to the school national flag?
8. Why should the crested crane on the Uganda flag face the flag pole when raised?
9. Why does the crested crane on the Uganda flag stand on one leg?
Date Class Subject No. of pupils Time
P.5
TOPIC: Uganda as an Independent nation
SUB –TOPIC: The National Coat of Arms
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic:- coat of arms, bottom, kob, shield,
motto, nationalism, documents, agricultural
Content: THE NATIONAL COAT OF ARMS
Importance / significance
- Power and authority
- National heritage
</passage>

<passage id="lchk_6816a0521efb434a8d222966ed00fd03" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="6">
 The national coat of arms is a symbol by which our nation if identified.
Features on the coat of arms
i) The crested crane
 It is the emblem of Uganda
 The crested crane stands on one leg to show that Uganda is going forward, interms of
development.
14
ii) The sun
 It shows that Uganda is found along the Equator.
 It shows that Uganda receives sunshine throughout the year it has good climate.
iii) The Kob
 It represents the rich wildlife of Uganda and the beautiful animals that earn Uganda foreign
exchange by attracting tourists.
iv) Coffee and Cotton
 These show that Uganda is an agricultural country.
 They are the chief export cash crops of Uganda.
v) Blue stripes of water entering the shield from the bottom
 These represent the source of River Nile which is found in Uganda.
vi) The drum
 It represents Uganda’s culture.
 It represents traditional means of communication
 It represents traditional musical instrument for entertainment.
vii) Shield and spears
 They represent the traditional weapons used by Ugandans for defence.
 They show that Uganda is ready to defend herself against her enemies.
viii) Uganda motto (for God and my country)
 It represents the spirit of nationalism.
 It shows that Ugandans are God fearing
ix) Blue stripes of water at the top of the shield
 These stripes represent the great lakes and rivers of Uganda.
x) The black colour
 This represents the black skinned people of Uganda.
xi) Landscape with green colour
 It represents the abundant green vegetation of Uganda
xii) Green hills
 These symbolize the many physical features of the country.
Uses of coat of arms
 The Uganda coat of arms is used on national paper currency and coins to distinguish them
from those countries.
15
 It is hung up in government places such as courts and offices to symbolize power and
authority
 It is printed on letter heads and official documents for government official use.
 It is used on the government seal for endorsement of documents.
 It is put/ mounted on the president’s car as a number plate
Activity
1. Who designed the Uganda Coat of Arms?
2. State one event that took place on Independence Day.
3. Name the personalities that held the following positions on independence.
4. Prime minister
5. President
6. What are national symbols?
7. Name one place where we find the coat of arms
8. Which political party led Uganda to independence?
9. Mention one document on which the coat of arms is printed
10. State Uganda’s national motto.
11. What feature on the coat of arms symbolize that Uganda is an agricultural coutry?
12. What do the Blue stripes on the Uganda Coat of Arms symbolize?
Date Class Subject No. of pupils Time
P.5
TOPIC: Uganda as an Independent nation
SUB –TOPIC: The National language
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic:- coat of arms, bottom, kob, shield,
CONTENT: THE NATIONAL LANGUAGE
 A national language is any one common language which is widely spoken by the majority of
the people in a country and is officially adopted for that purpose.
 Uganda doesn’t have a national language but it has English as her official language.
Importance of having a national language in a country
 It promotes unity among people in the country.
 It ensures easy communication in the country.
16
Why has Uganda failed to get her national language?
 It has got many traditional languages
The National Capital City
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
