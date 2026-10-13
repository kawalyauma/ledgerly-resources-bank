# Job ltsk_c0bf12d677f2456ea1c23ac2725378bf-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 5 lesson(s) below of week 3 of the Social Studies scheme for Primary Five 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P5: one 40-minute lesson: 3–4 ideas; 300–500 words; connected explanations and application; 5–8 activities.

lessonId=lles_7fe2ec8e39724938b51744fc0f9a99f3: lesson 11, Monday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: The constitution: meaning and Uganda's constitutions since independence — The constitution.
  Objectives: Give the meaning of a constitution and of by-laws.; Name the constitutions Uganda has had since independence.; State the results of the 1967 constitution.

lessonId=lles_63209098de7544f6a9de80687b356a20: lesson 12, Tuesday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: The 1995 constitution, functions of a constitution and its relationship with elections — The constitution.
  Objectives: Name the people who took part in making the 1995 constitution and their roles.; State the functions and importance of a constitution.; Explain the relationship between the constitution and elections.

lessonId=lles_e861344ca4ac4ba085bf41aa50160c52: lesson 13, Wednesday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: Practice: the constitution — The constitution.
  Objectives: Answer exercise questions on the constitution.
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points (numbered, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

lessonId=lles_e4e0ebfa6c044cbdba337f0a55e0481e: lesson 14, Thursday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: Duties of the government and social services — Duties of the government.
  Objectives: State the duties of the government to its citizens.; Explain what social services are and name those the government provides.; State problems the government faces when providing social services and their solutions.

lessonId=lles_80fbb03bed604c68980bb6fad198d9fd: lesson 15, Friday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: Communication — Duties of the government: communication.
  Objectives: Give the meaning of communication and mass media.; Name traditional and modern ways of communication.; State the importance of communication, barriers to communication and their solutions.

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

<passage id="lchk_db3ff097ff99464aba2332c9d68a600d" source="P.5 SST SCHEME TERM III 2019" part="3">
-Description
-Observation
-Discussing importance of electing leaders.
3
5
LIVING TOGETHER IN UGANDA
Uganda as an independent nation
Elections commission
-Explain the meaning of the word elections
Spell, reads , pronounces and writes words related to elections.
The Electoral commission
-Roles of the electoral commission.
-Challenges of the electoral commission.
-Respect for democracy and elections
-Discovery
-Discussion
-Explanation
-Question and answer
-Critical thinking
-Effective communication
-Inquiry
-Suggesting two things people who get the least votes should do after elections.
-Role playing voting exercise.
-Discussion importances of electing leaders
-Text books
4
1
&
2
LIVING TOGETHER IN UGANDA
The government of Uganda
The arms of the government (Legislature)
-Explaining the government.
-Naming the organs of the government.
-Identifying the components of the legislature.
-Stating the duties of the Legislature
-Spells, reads, pronounce the words related to the gov’t .
-Legislature
-Read, spell, pronounce words related to
-speaker
-Clerk to the parliament
-Sergeant at Arms.
-Parliament
The Government
-Meaning
-Organs of the government
Executive
Legislature
Judiciary
Legislature
(Parliament )
-Meaning
-Duties of the parliament
-Main officers of the parliament
Clerk to the parliament
Sergeant of Arms
-Qualifications of a MP
-Explanation
-Discussion
-Role play
-Cooperation
-Respect
-Observation
-Listening
-Critical thinking
-Debate
-Reading and spelling words related to the government
-Photographs of a parliament in session
MK stdbk 5 pg 131-133
4
3
LIVING TOGETHER IN UGANDA
The government of Uganda
Executive
Explaining executive and give components of the executive .
-Giving the functions of the executive
-Executive
-President
-Minister
-Civil servants
Executive
-Meaning
-Components of the executive
President
Ministers
-Functions of the executive
-Description
-Guided discovery
-Explanation
-Respect
-Appreciation
-Listening
-Critical thinking
-Discussing the roles of the executive government
A chart showing the executive government
Mk std BK 5 PAGE 132-133
4
Judiciary
-Explaining and composition of the Judiciary.
-Discussing the roles of the Judiciary
-spells, reads and pronounces words related to Judiciary.
Judiciary
Chief Justice
Judges
Attorneys
Lawyers
Supreme Court
Judiciary
-Meaning
-Composition of Judiciary
Chief justice
Principal judge
Judges
Justices
Attorneys
Lawyers
Magistrates
Supreme court
Roles of the Judiciary
Roles of a chief Justice
-Explanation
-Discussion
-Role play
-Observation
-Analysing
-Sharing
-Reporting
-Explaining the necessity of the separation of legislative and Judiciary
-Pictures of judges
-Resource person
-Pictures of High Court building
Mk std
Bk 5
Page 134
5
1
&
2
LIVING TOGETHER IN UGANDA
The government of Uganda
Roles of the government
-Explaining the roles of the government.
-State the types of the gov’t and their roles.
-spell, read and pronounce and use words like roles.
Roles of the gov’t
-Types of the gov’t
-Central government (National)
-Local government
-Role of the central government.
-Roles of the local government.
-Question and answer
-Discussion
-Explanation
-Role play
-Respect
-Co-operation
-Critical thinking
-Discussing the roles of the government.
-Discussing how different types of the government carry out their duties
-Pictures connected to the activities of the gov’t
Mk stdbk 5
Page 131
Functional bk 5
Pg 179
3
&
4
LIVING TOGETHER IN UGANDA
The government of Uganda
The Constitution
</passage>

<passage id="lchk_8565a70475344911b9db098cef933069" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="12">
 Officials that were elected in 1994 to debate the 1995 constitution.
29
iii) Mr. Stephen Akabway
 He was the chairperson of the Interim Electoral commission which organized the
elections of the CADS.
iv) Hon James Wapakhabulo
 He was the chairperson of the Constituent Assembly.
v) Professor Victoria Mwaka (Hon)
 She was the deputy chairperson of the Constituent Assembly.
A draft constitution
 A constitution where the views of citizens were represented.
 The Constituent Assembly debated and finalized the 1995 constitution.
 It took a period of sixteen months.
 On the 8 th October 1995, the 1995 – constitution was promulgated at the constitutional
square formerly known as city square.
Functions of a national constitution
 It protects the rights of the citizens.
 It guides the nation systematically in a particular direction of governance.
 It provides the means through which conflicts can be solved peacefully.
 It promotes national unity.
 It provides a peaceful transition of leadership.
The constitution promotes democracy in a country.
Activity
1. What is a national constitution
2. Write down any two constitutions that Uganda has had since independence.
3. What contribution was made by Godfrey Lukongwa Binaisa and Kofi Crable in 1967?
4. Why is a constitution important in a democratic country like Uganda?
5. Write short notes on the people below.
a) Stephen Akabway
b) Hon. James Wapakhabulo
6. Why is 8 th October 1995 politically important?
30
7. Mention the way, the 1967 constitution was unfriendly to the kingdoms in Uganda.
8. Write CADs in full.
9. What contribution was made by the constituent Assembly in 1994?
Date Class Subject No. of pupils Time
P.5
TOPIC: The Government of Uganda
SUB –TOPIC: Democracy
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic: freedom, democracy, human rights
, press
Content : Democracy
 What is democracy?
 Democracy is a system of governance which gives people freedom of speech, worship
and participation in politics
Or
 Democracy is the government of the people by the people and for the people.
 Democracy was first introduced and practiced by the Greeks in the city of Athens in
Greece.
Signs of modern democracy in a democratic country
 Elected political leaders.
 Elected parliament
 Freedom of speech
 There is freedom of the press.
 There is freedom of movement
 There is freedom of worship.
 Freedom to carry out business.
 Observance of human rights.
 Constitutional rule.
 Competitive politics.
Roles of citizens in promoting democracy
 Obeying the law.
31
 Respecting other people’s rights.
 Reporting wrong doers to the police.
 Participating in elections.
Ways through which Democracy is exercised in Uganda today
 Through elections by giving people freedom of speech
 By giving people freedom of press.
 Through freedom of worship
Ways how democracy is practiced in schools
 By electing prefects.
 By giving children freedom of expression.
 Through freedom of worship.
Activity
1. Define democracy
2. In which city was democracy first practiced?
3. State one way democracy is practiced in Uganda today.
4. How is democracy important in a country like Uganda?
5. Give two roles of citizens in the promotion of democracy in a country.
Date Class Subject No. of pupils Time
P.5
TOPIC: The Government of Uganda
SUB –TOPIC: Human rights in Uganda
LANGUAGE COMPETENCE :
</passage>

<passage id="lchk_f249775bfab9472fbaa5b06e03fb5230" source="P 5 SST Scheme Term III 2019 (ecolebooks Com)" part="3">
related to
elections
Elections
-Definition
-Types of elections
✓ Ballot paper
elections
✓ Lining
elections
✓ Appointing
elections
-How elections are
conducted
-Role play
-Explanation
-Discussion
-Critical
thinking
-Respect
-Effective
communicatio
n
-Inquiry
-Naming the
different
elections
-Role playing
elections
-Drawing
different
elections
materials
-Text books
Ecolebooks.com
DOWNLOAD MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
4
Terms used in elections
-Explaining
terms used in
elections
Terms used in
elections.
-polling station
-Bullot box etc
-Polling Assistant
-Polling officer etc
-Importances of
elections
-Description
-Observation
-Discussing
importance of
electing
leaders.
3 5
LIVING TOGETHER IN UGANDA
Uganda as an independent nation
Elections commission
-Explain the
meaning of
the word
elections
Spell, reads ,
pronounces
and writes
words
related to
elections.
The Electoral
commission
-Roles of the
electoral
commission.
-Challenges of the
electoral
commission.
-Respect for
democracy and
elections
-Discovery
-Discussion
-Explanation
-Question
and answer
-Critical
thinking
-Effective
communicatio
n
-Inquiry
-Suggesting
two things
people who get
the least votes
should do after
elections.
-Role playing
voting exercise.
-Discussion
importances of
electing
leaders
-Text books
Ecolebooks.com
DOWNLOAD MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
4 1
&
2
LIVING TOGETHER IN UGANDA
The government of Uganda
The arms of the government (Legislature)
-Explaining
the
government.
-Naming the
organs of
the
government.
-Identifying
the
components
of the
legislature.
-Stating the
duties of the
Legislature
-Spells,
reads,
pronounce
the words
related to
the gov’t .
-Legislature
-Read, spell,
pronounce
words
related to
-speaker
-Clerk to the
parliament
-Sergeant at
Arms.
-Parliament
The Government
-Meaning
-Organs of the
government
❖ Executive
❖ Legislature
❖ Judiciary
Legislature
(Parliament )
-Meaning
-Duties of the
parliament
-Main officers of the
parliament
❖ Clerk to the
parliament
❖ Sergeant of
Arms
-Qualifications of a
MP
-Explanation
-Discussion
-Role play
-Cooperation
-Respect
-Observation
-Listening
-Critical
thinking
-Debate
-Reading and
spelling words
related to the
government
-
Photograph
s of a
parliament
in session
MK
stdbk 5
pg 131-
133
Ecolebooks.com
DOWNLOAD MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
4 3
LIVING TOGETHER IN UGANDA
The government of Uganda
Executive
Explaining
executive
and give
components
of the
executive .
-Giving the
functions of
the executive
-Executive
-President
-Minister
-Civil
servants
Executive
-Meaning
-Components of the
executive
❖ President
❖ Ministers
-Functions of the
executive
-Description
-Guided
discovery
-Explanation
-Respect
-Appreciation
-Listening
-Critical
thinking
-Discussing the
roles of the
executive
government
A chart
showing the
executive
government
Mk std
BK 5
PAGE
132-133
Ecolebooks.com
DOWNLOAD MORE RESOURCES LIKE THIS ON ECOLEBOOKS.COM
4
Judiciary
-Explaining
and
composition
of the
Judiciary.
-Discussing
the roles of
the Judiciary
-spells, reads
and
pronounces
words
related to
Judiciary.
❖ Judiciary
❖ Chief
Justice
❖ Judges
❖ Attorney
s
❖ Lawyers
❖ Supreme
Court
Judiciary
-Meaning
-Composition of
Judiciary
❖ Chief justice
❖ Principal judge
❖ Judges
❖ Justices
❖ Attorneys
❖ Lawyers
❖ Magistrates
❖ Supreme court
❖ Roles of the
Judiciary
❖ Roles of a chief
Justice
-Explanation
-Discussion
-Role play
-Observation
-Analysing
-Sharing
-Reporting
-Explaining the
necessity of
the separation
</passage>

<passage id="lchk_461170f297794aa1b58cec46e2ae28f2" source="NCDC P5 Merged – Social Studies" part="19">
- Identify the systems of election.
- Outline the duties of the Electoral Commission.
Materials you will need:
A pen, note book, P. 5 text book (if possible)
Introduction:
In the previous lesson you learnt about democracy. Now in this lesson you
are going to study about elections in Uganda.
Step I
i) Election is the action of choosing leaders. To elect means to select.
ii) In Uganda, there are different kinds of elections exercised for exam-
ple; elections for the president, elections for Members of Parliament, local

SELF-STUDY LEARNING

council elections, By – elections and referendum.
Step II
Let us find out the materials used during elections. Write them in your
note book.
Step III
In Uganda, elections are organised by a body called The Independent
Electoral Commission (I.E.C). It carries out different duties. below are
some of its duties;
- To register voters.
-To print ballot papers
- Displat voter’s registers
-To organize and supervise elections.
Activity
In my village, ____________ where carried out at a _____________.
People cast their votes in the ___________. After voting, the
_____________ were counted for each candidate. The _____________
announced the election results.

Polling station, presiding officer, elections, votes, ballot box

SOCIAL STUDIES | PRIMARY FIVE

TOPIC: THE GOVERNMENT OF UGANDA
Lesson 1: Organs of government
You will be able to;
- Give the meaning of government.
- State the importance of government.
- Mention the three organs of government.

Materials you will need:
Pens, Pencils, note book, P. 5 SST text book (If possible)
Instructions:
Get ready with your books. Today you are going to study about the or-
gans of government.

Introduction:
At home, the mother prepares food on three cooking stones or a charcoal
stove with also three stands. Find out what happens when one stone or
stand is removed. In the same way the government is is made up of three
organs or arms.

Procedure:
Step I: Give the meaning of government
A government is a ruling body of a country.
In Uganda, there are two levels under which people are governed. These
include; Central government which manages the national affairs and the
Local government which runs the district affairs.
Step II:
The government plays many roles to its citizens as listed below;
- keeping law and order.
-Building schools.
-Building hospitals.
-Defending the country from external attacks.

SELF-STUDY LEARNING

- Constructing roads

Step III
Now write the three organs of government relating to the cooking stones
or stands of a charcoal stove at home.
They are Executive, Legislature and Judiciary.

Activity
1. Name the three organs of government.
2. What name is given to a group of people who govern a country?
3. Mention the two levels of the government.
4. State the importance of government to its people.

Lesson 2: The Executive
You will be able to;
- Mention the groups of people who form the Executive.
- State the functions of the Executive.
- Identify the duties of the President.
Materials you will need:
Pens, Pencils, note book, P. 5 SST text book (If possible).
Introduction:
In this lesson, you are going to learn about the Executive, groups of peo-
ple who form the Executive, functions of the Executive and duties of the
President.

Step I:
The Executive.
i. This is the ruling organ of the government.
It is headed by the President. It is made up of; the president, the
cabinet and civil servants.

SOCIAL STUDIES | PRIMARY FIVE
</passage>

<passage id="lchk_eca2cbe9906942cfad946678f2edb234" source="NCDC P5 Merged – Social Studies" part="21">
The Courts of law under the Judiciary.

Level | Head
Supreme Court | Chief Justice
Court of Appeal | Deputy Chief Justice
High Court | Principal judge
Chief Magistrate’s Court | Chief magistrate
Resident Magistrate’s Court | Magistrate
Activity
1. Name the Chief Justice Of Uganda.
2. Name the highest court of the judiciary.
3. What title is given to head of Judiciary?
4. State the duties of the Judiciary.
Lesson 5:
The Constitution
You will be able to;
- Give the meaning of a Constitution.
- List the examples of Constitutions.
- Identify the importance of a Constitution.
Materials you will need:
A Pen, pencil, note book, P. 5 S.ST text book (if possible)

SOCIAL STUDIES | PRIMARY FIVE

Introduction:
Do you have some rules at home that were set by your parents? List some
of them. Also as a country, there are laws which the citizens must follow.
These laws make up what we call a Constitution.
Step I:
The Constitution.
i) A Constitution is a set of laws that govern a country.
ii) The Constitution of the Republic of Uganda was written in 1995.
iii) It is called the 1995 Constitution.

Step II:
Examples of constitutions in Uganda since independence.
i) 1962 Constitution/Independence Constitution.
ii) 1966 Constitution/Pigeon hole Constitution.
iii) 1967 Constitution/Republican Constitution.
v) 1995 Constitution/The people’s Constitution.
Note: The 1995 constitution was made public on 8th October, 1995 at the
Constitutional Square, formerly known as City Square

Step III:
a) The functions of the Constitution.
i) It creates order in a country.
ii) It protects people from unfair laws.
iii) It protects people’s rights.
b) Importance of the constitution.
i) It promotes human rights.
ii) It promotes democracy.
iii) It promotes good governance.
iv) It helps to change leadership peacefully.
Activity

SELF-STUDY LEARNING

1. ____________ is a set of laws governing a country.
2. Why should every school have rules and regulations?
3. Give the importance of a constitution.

Lesson 6:
Sources of Revenue and Expenditure by the government.
You will be able to;
- Mention the sources of government revenue.
- State the ways the government spends its money.
- Identify the services on which government spends its revenue.

Materials you will need:
A pen, pencil, note book, P. 5 S.ST text book (if possible)

Introduction:
In this lesson you are now going to learn about the government revenue,
ways the government spends its money and services on which govern-
ment spends money.
Step I:
Find out the type of work that your parent or guardians do to get money.
List them. Write down the things on which your parents spend money on.
Step II:
The sources of government revenue.
i) Revenue is the money government gets or earns.
ii) Expenditure is the money government spends or uses.
iii) List the sources of government revenue. Check your list with these be-
low; taxes, loans, donations, court fines, tourism, grants, licenses.
Step III:
a) Ways government spends its money.
-Building of schools. | -Buying security equipments.

SOCIAL STUDIES | PRIMARY FIVE

-Paying civil servants. | -Building of hospitals.
-Constructing and maintaining roads,
-Paying loans . | -Providing safe and clean water.
b) Services on which the government spends its money.
-Education services. | -Security services.
-Transport services. | -Health services.
Communication services.

Activity
1. Give the meaning of revenue.
2. Mention the sources of government revenue.
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
