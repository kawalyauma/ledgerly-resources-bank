# Job ltsk_f7056364fa1f4da2b9308681019344f4-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 5 lesson(s) below of week 4 of the Social Studies scheme for Primary Five 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P5: one 40-minute lesson: 3–5 sections; about 14–28 points (meaning, examples, reasons, problems and solutions as the passages give); 5–8 activities.

lessonId=lles_2174eb576b9642eaa0c1519cbe035323: lesson 16, Monday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: The government of Uganda — Meaning of government and its organs.
  Objectives: Define government; Name the three organs of government

lessonId=lles_f9c24cda432a4823884b2ed2f9ed6c39: lesson 17, Tuesday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: The legislature — Parliament: duties, officers and qualifications of a Member of Parliament.
  Objectives: State the duties of Parliament; Name the main officers of Parliament

lessonId=lles_e5c32cc9fdbf457987e60b21c1dcbb43: lesson 18, Wednesday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: The executive — The President, ministers and civil servants.
  Objectives: Name the components of the executive; State the functions of the executive

lessonId=lles_c7da3fb37ec14fd1958700d3693863f6: lesson 19, Thursday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: The judiciary — Composition and roles of the judiciary.
  Objectives: Name the courts and officers of the judiciary; State the roles of the judiciary

lessonId=lles_30e71760d56a46fb99ee7edbd41c0d81: lesson 20, Friday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: Organs of government Part B — The legislature, executive and judiciary.
  Objectives: Compare the work of the three organs of government; Explain the separation of powers
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points ('- ' points, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

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
<passage id="lchk_a068c36f55a64155a9a2517aace9832f" source="P.5 Social Studies Lesson Notes Term 3" part="4">
 To provide clean water to people
 To implement the laws
 To protect people and their property.
ARMS / ORGANS OF A DEMOCRATIC GOVERNMENT.
Government has many responsibilities. It carries them out through organs.
- The executive
- The legislature
- The judiciary.
Duties of the executive
 To implement the law
 To plan for the country
DIVINE EDUCATION CENTRE:0784540287/0751565742 Page 11
 To rule the country
 To protect people and their property.
The executive organ does the work of government.
Composition of the executive.
- The president (head)
- Cabinet ministers
- Civil servants (government workers)
Duties of the Legislature
 To discuss and pass laws.
 To give advice to the executive
 To approve the national budget
 To approve (vet) newly appointed minister and other senior government officials.
 To protect the national constitution
Legislature is headed by the speaker of parliament.
Important personalities in parliament.
- The speaker of parliament
- Sergeant at arms
- Clerk to parliament
Note: Roles of the speaker
 The speaker chairs parliamentary meetings
 The sergeant at arms keeps law and order in parliament.
 The clerk to parliament records minutes in parliament.
 Recorded minutes of parliament are called hansards
 Give the present speaker (and the deputy speaker) of parliament.
Composition of parliament.
- Constituency representatives.
- Special groups / interest groups representatives.
Special groups representatives:
 The army
 The youth
 Women
DIVINE EDUCATION CENTRE:0784540287/0751565742 Page 12
 People with disabilities.
Teacher should revise the work on Legco
- Give similarities of Legco and today’s parliament
- Differences between members of Legco and members of parliament.
Duties of the judiciary
 To interpret the law
 To decide if the law has been broken or not.
 To settle disputes
 To punish law breakers.
Composition of the judiciary
- Judges
- Magistrates
- Court clerks
- Lawyers
The judiciary is headed by the chief justice.
Teacher should give the similarities of the judiciary and local councils and the judiciary
with prefects.
CONSTITUTIONALISM AND THE RULE OF LAW
A national constitution is a set of laws used to rule a country.
A constitution is a set of laws used to govern a company, a society or an organization.
Functions of a national constitution
 To unite people
 To promote peace and security
 To guide leaders
 To help change government peacefully
 To promote good governance
 To promote human rights.
The constitutions Uganda has ever had.
1961 constitution
1962 constitution
1966 constitution
1967 constitution
1995 constitution
DIVINE EDUCATION CENTRE:0784540287/0751565742 Page 13
The 1961 constitution
This constitution was made in London between 18 th September. This constitution was
made in London between 18 th September to 9 th October 1961.
It was mainly made to enable Uganda get self government.
Lord Munster Commission
- This was a committee appointed in July 1961 to make a report about the kingdoms
interests mainly those which refused to send representatives to Legco.
- It was chaired by Lord Earl Munster.
Recommendations:
 Buganda was to remain part of Uganda.
 Buganda was to send 21 members to the national assembly.
Contributions of the Munster Commission
 It led to the Lancaster Conference which granted Uganda independence.
The Lancaster Conference of September 1961
This conference was held in Lancaster house in London.
It granted Uganda independence.
</passage>

<passage id="lchk_613d1868da5840e4844b343f10260aa2" source="Primary 5 Social Studies Scheme of Work – Term 3" part="3">
-Examples of
Ugandan
president since
1962 up to the
present leader
Idi Amin Dada
1971-79
Yesufu Kilonde
Lule 1979
-self
awareness
-talking
about one’s
potential
feeling and
emotions
-Observation
-Talk and a
chalk board
illustration
-Identify
presidents
who ruled
Uganda
Text books MK
SST
Bk
5
Pg
122
For more schemes of work, visit www.uganda.madpath.com
presidents
who ruled
Uganda
-Pronounces
words
correctly
Geoffrey
Rukongwa
Brinaisa 1979-80
-making
choices
The learner is able to understand the organs of the government, the constitution and duties of citizens, explain the sources of revenue and expenditure by
government and understand the rights and responsibilities of the citizens of Uganda.
5 -The
government
-Types of
governme
nts
-A learner
defines the
two types of
governments
-A learner
pronounces
vocabulary
words
correctly
-Writes
words
correctly
Writes
words in
correct
spelling
-Definition of a
government
-Listing types of a
government and
their functions
-Ways in which
government were
formed
-Creative
thinking
-initiating
new ideas
-friendship
formation
-working in
groups
-Observation
-Talk and a
chalk board
illustration
-Identifying
types of
government
s
Text
books
MK
SST
Book 5
pg 131
6 The
government
of Uganda
Organs of
the
governme
nt
-A learner
lists down
three organs
of the
government
-States the
functions of
the
executive
organ of the
government
-A learner
spells words
of the lesson
correctly
-Writes
words in
good
spelling
-Pronounces
words
correctly
-Mentioning the
three organs of
the government
-Functions of the
executive organ
-Planning for the
country
-Ensuring peace
in the country
Empathy
-supporting
others
-caring for
others
guiding
others
-guided
discussion
-inquiry
-talk and
chalk
Stating the
organs of
the
government
Answering
questions
Text
books
MK
SST Bk
5 Pg
133
7 The
Legislatio
n
-A learner
Identifies
the la
making
body during
colonial days
-A learner
Write all
words rightly
-Spells
words
correctly
-Pronounce
vocabulary
-The main work
of legislation
-The head of
legislation
-Functions of
legislation
-creative
thinking
-logical
reasoning
-initiating
new ideas
-inquiry
-guided
discussion
-Stating the
function of
the
legislation
-Answering
questions
Text
books
MK
SST Bk
5 Pg
133
For more schemes of work, visit www.uganda.madpath.com
words
correctly
-Finding
different
ways of
doing things
3 1 ORGANS
OF THE
GOVERNM
ENT
THE
JUDICIA
RY
-A learner
Defines the
term
judiciary
states the
three
categories of
people in
judiciary
-Names the
heads of the
judiciary
-A learner
spells lesson
vocabulary
correctly
-Writes
lesson notes
and exercise
rightly
-Group of people
who make up
judiciary
-The judges,
lawyers,
legislature,
antoneys, justice
-Functions of the
judiciary
-The head of
judiciary
empathy
-caring for
others
listening to
others
-critical
thinking
-reasoning
-explanation
-inquiry
-guided
discussion
Identify
what form
of judiciary
organ of
government
Text
books
MK
SST Bk
5 pg
134
2 The
constituti
on
A learner
defines
constitution
A learner
Spells
difficult
words
correctly
-Definition of the
term constitution
-The four
constitutions
Uganda has ever
had since
independence.
-Independence
constitution 1962
-Pigeon hole
constitution of
1966 etc
-problem
solving
-taking
decision
-taking
decisions
-making
choices
-decision
making
giving
instructions
-Inquiry
Guided
discussion
-Explanation
-Chalk and
talk
Look and say
Discussing
functions of
the
constitution
Text
books
Mk
SST Bk
5 pg
135
3 Function
of a
national
constituti
</passage>

<passage id="lchk_b1f295b60e564889b04f04231149793d" source="Primary 5 Social Studies Scheme of Work, Term III" part="3">
The learner pronounces, reads,
spells and writes words correctly.
e.g. executive, Cabinet, Public
service, Permanent secretary
Group work
Guided discussion
Answering oral and
written activities
Effective
communication
Co-operation
Patriotism
Photos
of
cabinet
and
state
ministers
MK pupils book 5 page 161
2
The Government
The legislature / parliament
Head of the legislature
Members who make up legislature
Duties of the parliament
Parliamentary staff
Qualifications for members of
parliament
Parliamentary business
- Bills
- Laws
- Hansands
- Mace
- Sergeant –at-arms
- Special groups represented
in the parliament
Subject
The learner
Gives the meaning of the new words
like parliament, bills / acts and
Hansards
States the duties of parliament
Language
The learner pronounces, reads,
spells and writes the words
connected to the parliament
correctly
Parliament, bills, acts, Hansaids,
Parliamentary , Chamber
Guided discovery
Inquiry
Story telling
Giving the meaning of
new terms
Stating the duties of
the parliament both
orally and written
Critical thinking
Responsibility
Patriotism
Photos
parliame
nt in the
text
book/
new MK
page
162 of
the
Comp. SST pupils book 5 pages 177 – 179
3
The Government
The Judiciary Organ
Head of judiciary
Components of judiciary
Duties of judiciary
Roles of the members in judiciary like
Chief Justice, Lawyers and
magistrates, Judicial Courts in
Uganda.
Functions of Judicial service
commission
Subject
The learner
Names the title given to the head of
Judiciary
Mentions members who makes up
the Judiciary organ.
Language
The learner pronounces, reads,
spells and writes words correctly
related to Judiciary like Lawyer,
magistrate, Court, Judiciary
Guided discovery
Inquiry
Story telling
Stating the functions
of judiciary
Answering questions
orally and written
activities
Critical thinking
Effective
communication
Leadership
Pictures
of
judges in
the
courts of
law
Comp. SST book 5 pages 177 - 179 and
New MK pupils book 5 page 134
4
&
5
The Government
The constitution
Meaning of a constitution
Types of a constitution i.e. written and
unwritten constitution
The four constitutions Uganda has
ever had since independence.
The constitution making process
The draft constitution
Functions of a national constitution
Subject
The leaner,
Gives the meaning of the word
constitution
Outlines the constitutions Uganda
has so far had since independence
Language
The learner
Pronounces, reads, spells and
writes words related to the
constitution correctly e.g.
Amend, craft, constitution, decrees,
pigeon hole
Story telling
Guided discussion
Describing the term
constitution
Critical thinking
Effective
communication
Leadership
Text
books
A copy
of a
national
4 1
The Government
Democracy
Meaning of democracy
Signs or indicators of democracy
Roles of citizens in promoting
democracy
Ways how democracy is exercised
Ways how democracy is misused in
Uganda
Ways of overcoming the above
problems
Origin of democracy
Advantages of democracy in the
modern society
Subject
The learner
Describes the term democracy,
human rights, human right violation
and children’s rights
Language
The learner pronounces, spells,
reads and writes the words correctly
like indicators, democracy,
violation, human rights, abuse
Guided discussion
Inquiry
Giving the meaning of
the word democracy
Stating the roles of
citizens in promoting
democracy
Critical thinking
Effective
communication
Text
book
reading
MK SST pupils book 5 page 137
2
The Government
Human rights
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

<passage id="lchk_daea287472e2407897fac9dadc140318" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="8">
3. What title given to the political head of a district?
4. Which ministry runs the affairs of local government?
5. Who is the current minister of local government?
19
Decentralization
Decentralization is the transfer of some powers from the central government to the district level.
Under what ministry is decentralization?
The ministry of local government
Advantages of Decentralization
 Brings social services nearer to the people
 Creates employment to people.
 For easy administration.
Disadvantages of Decentralization
 Promotes corruption.
 Embezzlement of government funds.
 Promotes tribalism
Reasons why the government of Uganda creating many districts?
 For easy administration.
 To create employment to the people.
 For easy provision of social services.
The National / central government
 This is the government that bears all the major responsibilities towards the people in a
country.
Differences between the central government and local government
Central government Local government
 It is one government.
 It controls all armed forces.
 It cares for the development of the whole nation.
 Runs the major hospitals.
 Builds and maintains major roads.
 There are many local governments.
 It controls the local defence forces.
 Cares only for their localities.
 Controls dispensaries and health centres.
 Builds and mains feeder roads.
Activity
1. Write short notes on the following?
a) A government
b) Decentralization
c) Bye laws
2. Mention the types of government in Uganda.
3. Give the ministry that is responsible for the development of the district localities.
20
4. What is the major reasons for the promotion of decentralization programme?
5. Why is the government of Uganda dividing the country into many districts?
6. Give two differences in the activities run by the central and local government.
7. Who heads the district council?
8. State any two advantages of decentralization.
9. Give two disadvantages of decentralization
Activity
1. What is the ruling body of government called?
2. Under which organ of government do the police belong?
3. Who is the current president of Uganda?
4. Who is the local of all ministers in government?
5. What role do civil servants play in government?
6. Who is the current vice president of Uganda?
7. State one function of the executive arm of government.
8. Why should a country have laws?
Date Class Subject No. of pupils Time
P.5
TOPIC: The Government of Uganda
SUB –TOPIC: The organs of Government and their functions
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic: Executive , legislature, judiciary,
cabinet, civil servants, parliament, ministers
Content : Arms or organs of the government
 Executive
 Legislature
 Judiciary
The Executive arm of the government
 This is the ruling organ of the government
 It is the organ of the government which is responsible for the day today running of the affairs
of the country.
21
 It is headed by the president.
The roles of the executive arm of the government
 To plan for the country
 To ensure that there is development in the country.
 It ensures that there is peace in the country.
 It implements government policies.
 It implements laws.
Groups of people that make up the executive organ
 The president
 The ministers
 The civil servants
The roles of the president
 The president is the chief executive officer in Uganda.
 He takes care of all the citizens of Uganda.
</passage>

<passage id="lchk_f3a20646343545bf90e63ce171b6cf0e" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="10">
 Ministers without constituencies (Ex. officials)
Special groups of people represented in the parliament
 The youth
 The workers
 The women
 The army
 The disabled
Duties of the parliament
 To make or set laws.
 To approve the national budget.
 To approve persons appointed in high public offices such as vice president, prime minister
etc.
 To check on how the government spends public funds .
 To amend the constitution when need arises.
 Disciplines unruly ministers and civil servants.
 The parliament passes a vote of no confidence or censure on the president, ministers and
other public officers if they are found corrupt or out of order.
Main officers of parliament
a) The speaker of the parliament
 The speaker is the chairperson of parliament.
 He/ she chairs all the debates in parliament.
b) The clerk to parliament
 He is the administrative head of parliament who keeps records and property of
parliament.
 He acts as the secretary to the parliament.
 He records all the parliamentary proceedings. (Hansard)
c) The sergeant at arms
 He is in charge of security in the parliament.
 He ensures that there is discipline in the parliament.
 He alerts members of the parliament when the speaker is about to enter.
 He makes sure that no person disrupts the members of parliament during their meetings.
Terms connected to the Parliament
25
A bill
 A bill is a proposed law in the parliament
A law or an act
 A law or an act is a bill that has been signed by the president
Hansard
 Hansard are the recorded proceedings of the parliament.
A mace
 A mace is a symbol of authority that represents the power of the speaker and parliament
Qualifications for one to become a member of parliament
 He or she should be a citizen of Uganda.
 Should be a registered voter.
 Should be eighteen years old or above.
 Should have completed a minimum level of formal education of senior six or equivalent.
Activity
1. What is legislature?
2. State one duty of the legislature arm of the government.
3. Who heads the legislature?
4. What title is given to the chief administrative head of the parliament?
5. Give the roles of the following officers in the parliament.
a) The speaker of parliament
b) Sergeant at arms
c) Clerk to parliament
Date Class Subject No. of pupils Time
P.5
TOPIC: The Government of Uganda
SUB –TOPIC: The Judiciary arm of the government
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic: justice, judge, magistrates,
attorneys , lawyers, supreme
Content : The Judiciary arm of government
 The judiciary arm of the government is the custodian of the law.
26
 It is headed by the chief justice.
 The chief justice is assisted by the principal judge.
Officials/ people who make up the judiciary
 The judges
 The justices
 The attorneys
 The lawyers
 The magistrates
The duties of the judiciary arm of government
 Punishes law breakers
 Settles disputes and conflicts in courts of laws.
 It makes sure that laws are observed and maintained in the country. .
 Interprets laws to the public.
 It protects the rights of every citizen by giving free and fair trial in courts of law.
Duties of the chief justice
 He/ she guides the judges and magistrates in the way they should carry out their work.
 He/ she is responsible for the swearing in of the important political people the president
and vice president.
 He is the head of the Supreme Court.
What is the highest court in Uganda called?
 The Supreme Court
</passage>

<passage id="lchk_d3d9ba3578dc423c98bad9300623680e" source="Primary Five Social Studies Notes 2020" part="53">
 A minister is the political head of a ministry.
 Town clerk is the highest civil servant in a municipality and responsible
for paying civil servants.
Types of government
1. Democratic government
It is a government where leaders are elected by people.
2. Dictatorial government
It is the government where leader’s words are final and not answerable.
3. Monarchy government
A government ruled by a king or queen
4. Military government.
This is a type of government which come into power through force
/violence
System of government
i) Single party system
ii) Multi-party system
iii) Federal system
Single party system
 This is the system where one political party operates in a country
231
Advantages of single party system
 It is easy to make decisions
 There are less conflicts
 Leadership is respected
 It promotes national unity
 There are less election petitions
 There are less vote rigging
Disadvantages of single party system
 It promotes dictatorship
 New ideas are not accepted
 It promotes abuse for human rights
 Wrong decisions can be made to lack of opposition
Multi-party system
 This is when many political parties are allowed to operate in a country.
Advantages of multi-party system.
i) It promotes respect for human
ii) It provides peaceful change of leaders
iii) It develops government organs
v) It helps the ruling government to check on its self
Disadvantages of multiparty system
 There are many election petition
 It promotes corruption
 Decision making is difficult
 It promotes injustice
 It promotes vote rigging
 It promotes division of peoplebasing on ethnicity.
232
N:B Multiparty system is the one followed in Uganda today.
Roles of political parties
 To conduct political campaigns
 To nominate candidates to represent their views
Organ of government
 The executive
 The legislature
 The judiciary
THE EXECUTIVE
 This is the administrative organ of the government
 This organ is head by the president
 It is the top most organ of the government in a country
Duties of the executive
 To plan and govern the country
 To implement government policies
 To enforce laws
 To promote development
 To maintain peace and security in a country
 To pay civil servants
 To provide social services
People who belongs to the Executive
 The president
 The vice president
 Cabinet ministries
 Civil servants
Examples of civil of civil servants
 Police
 Permanent secretaries
 Attorney general
 Teachers
233
 Health workers
 Chief administrative officers(CAO)
The roles of the president
 To plan and rule the country
 To defend the country
 To approve parliamentary bills
 To control the armed forces
 To appoint cabinets ministers
 To provide social service to the citizens
Uganda’s armed forces
 The army
 The police
 The prisons
Note
 The main duty of the executive is to implement government policies
/programmes.
 The civil servants carryout day today work of the government
departments.
THE LEGISLATURE.
 Legislature is the national assembly of a country.
 Legislature is the law-making body in Uganda.
 Before Uganda became independent, the assembly was called the
legislature council
 It is headed by the parliamentary speaker.
People who belongs to the legislature
 Speaker of parliament
 Deputy speaker
 The sergeant at arms
 The clerk to parliament
234
 Members of parliament
 Ex-officios.
Examples of special interest groups in parliament.
 National army
 Workers/civil servants
 Youths
 Women
</passage>

<passage id="lchk_4fda346b6242448383e30fe61e55cb53" source="Primary Five Social Studies Notes 2020" part="54">
 People with disabilities
ADMINISTRATORS IN PARLIAMENT
1. The speaker of parliament
 He /she is the head of parliament
 He /she chairs parliamentary debates
 He/she presides over functions of parliament
2. Deputy speaker
 Chairs parliamentary debates in the absence of the speaker.
3. Clerk to parliament
 He /she records parliamentary minutes
 He/she is the chief accounting officer of parliament
Define Hansard.
 These are the written proceedings in parliament
Sergeant at arms
 He or she is in charge of security in parliament
 He/she alerts members of parliament when the speaker is about to
enter
 He or she carries a mace
Qn: Who is a constituent?
 This is a person who lives and can vote in a constituency
235
Function of the legislature
i) To make and amend laws
ii) To approve the national budget
iii) To monitor government expenditure
iv) To approve public officials appointed by the president
v) To fight against misuse of government’s fund
vi) To pass information to the public about government plans
vii) To discipline unruly ministers and civil servants
viii) To pass a vote of no confidence on the president, ministers and other
government officials
Qn: How does one become a member of parliament?
 Through elections
 Through appointment
Qn: Define the term bill
 A bill is a proposed law in parliament
Qn: What is an act?
 An act is abill which have been approved and signed by the president
Qn: What is an ordinance?
 This is a law made by an urban council.
Qn: What is a by law?
 This is a law made by local council.
Qn: What is a shadow cabinet?
 This is the government formed by the side of opposition in parliament.
Qn: Who was the first parliamentary speaker of Uganda?
 John Bowers Griffin
236
THE JUDICIARY
It is headed by the chief justice
People who compose the judiciary
i) The chief justice
ii) Deputy chief justice
iii) The principle judge
iv) Judge
V) Magistrates
vi) Lawyers
Duties of the chief justice
i) Heads the supreme court
ii) He disciplines the jusges
iii) He is responsible for the swearing in the president
IV) He heads the judiciary
v) He guides and supervises the judges
N;B Judicial service commission is the body that appoints judges in Uganda
Duties of judiciary
i) To interpret the low to the people(main)
ii) To settle cases in courts of law
iii) To punish lawbreakers
iv) To settle disputes
v) To pass judgement
vi) To protect the rights of the citizens
237
Note
Supreme court is the highest court in Uganda
People who are not satisfied with the way their cases handled in the lower
courts appeals to the supreme courts
Qn: Where do each of the following organs sit
i) Executive - state house
ii) Legislature - parliament
iii) Judiciary – court
Importance of a court in the community
 Settles disputes in the community
 It protects human rights
THE CONSTITUTION
 A Constitution is a set of laws governing an real organization
 A national constitution is a set of laws by which a country is governed
Functions of a constitution
 It promotes national unity
 It promotes peaceful transition of leadership
 It promotes the rights of the citizens
 It states duties of each organ of government
 Promotes good governance
 Used to settle disputes in courts of law
Types of constitution
Relationship between constitution and elections
i) Constitution sets the duration for conducting general elections
ii) Constitution sets conditions to participate in general elections
238
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
