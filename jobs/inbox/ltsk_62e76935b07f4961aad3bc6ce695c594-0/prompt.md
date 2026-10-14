# Job ltsk_62e76935b07f4961aad3bc6ce695c594-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 5 lesson(s) below of week 1 of the Social Studies scheme for Primary Five 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P5: one 40-minute lesson: 3–5 sections; about 14–28 points (meaning, examples, reasons, problems and solutions as the passages give); 5–8 activities.

lessonId=lles_d4b23f847dcb46fd8d7b35e8bacaa14b: lesson 1, Monday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: The Government of Uganda). Lesson: Role of government — Role of government.
  Objectives: Identify and explain role of government.

lessonId=lles_e76cdbef459a4e03976d03c735db66d9: lesson 2, Tuesday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: The Government of Uganda). Lesson: Three organs of government — Three organs of government.
  Objectives: Identify and explain three organs of government.

lessonId=lles_f49747ae5e484198b6546fdf3600c03f: lesson 3, Wednesday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: The Government of Uganda). Lesson: The executive — The executive.
  Objectives: Identify and explain the executive.

lessonId=lles_24a1d72879b3407291fadaa6ce0af730: lesson 4, Thursday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: The Government of Uganda). Lesson: The legislature — The legislature.
  Objectives: Identify and explain the legislature.

lessonId=lles_b067ec80ecac491a86ebea898aaf6632: lesson 5, Friday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: The Government of Uganda). Lesson: The judiciary — The judiciary.
  Objectives: Identify and explain the judiciary.

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

<passage id="lchk_853d95d8ec1549f28a6ca4fadcc6f022" source="Excel P 5 SST Term III" part="21">
2. State any two difference between the Central government and Local government.
3. Name the body that is responsible for building major roads in Uganda.
4. What title is given to a political head of a sub-county?
5. Give one way a government is important to a country.
6. Mention the three arms of a democratioc government.
7. State any three duties performed by the executive organ of the government.
8. Complete the table below correctly.
Government organ Headed by Composition
(i) ------------- ------------------- -civil servants -ministers
(ii) ------------- Chief justice -------------- --------------
(iii) ------------- ------------------- -Constituency MPs -Ex-officios
9. State any two roles performed by the president of Uganda.
10. Mention any three instruments of power given to the president on the swearing in ceremony.
Page 39
11. What title is given to the;
(i) Political head of a ministry?
(ii) Highest civil servant in a ministry?
(iii) Highest civil servant in a district?
12. How does the chief justice help the president to attain leadership powers?
13. Mention any two examples of civil servants.
14. State tany three ways the legislature in a democratic government.
15. How is the work of the parliament similar to that of the defunct LEGCO?
16. Give one way one can become a member of parliament in Uganda.
17. How does the Legislature help the Judiciary to perform its work?
18. Mention any three special groups of people represented in the par5liament of Uganda.
19. How is a Bill different from an Act?
20. State one role performed by the following people in the parliament of Uganda.
(i) Speaker of parliament.
(ii) Clerk
(iii) Sergeant at arms
21. When does a bill become a law?
22. Give any two ways law brakers are punished by the Judiciary.
23. Apart from punishing law breakers, give any two other ways the Judiciary is important to a
country.
24. State any three roles performed by the government.
25. State any three problems the government faces when performing iots duties.
26. Name the government ministry that is responsible for fighting againsty corruptio n in the
country.
27. What are Social services?
28. Mention any three social services provided by the government to its citizens.
29. Give the meaning of each of the following;
(i) A constitution
(ii) By-laws
30. Which constitution made Uganda become a republic?
31. How did the 1967 constitution affect cultural institutions in Uganda?
32. Why is 8 th October, 1995 remembered in the history of Uganda?
33. State any two ways a national constitution is important to acountry.
34. Give the meaning of Mass media.
35. Name the body that is responsible for regulatinmg media services in Uganda.
36. State any two challenges hindering effective communication in Uganda.
37. How does communication promote trade in an area?
38. Mention any four sources of government revenue.
39. Give any two ways the government spends its revenue.
40. Name the type of tax charged on;
(i) Locally manufactured goods.
(ii) Imported goods.
41. Mention the two types of taxes.
42. Name the body that is responsible for collecting taxes in Uganda.
43. State any three problems the above body faces when carrying out its work.
44. Give the meaning of the term Smuggling.
45. Name the body under URA that is responsible for controlling smuggling in Uganda.
46. Give two any two ways smuggling affects the development of the country.
47. Give the meaning of the following;
Page 40
(i) A Budget
(ii) A National budget
</passage>

<passage id="lchk_4ea67a5f999d4f529b497430a09bf6a2" source="P.5 Social Studies with RE End of Term III Examination 2022" part="3">
………………..……………………………….…..………………………………………….
7 Turn Over
46. (a) Name the person who represented Eastern Uganda on LEGCO in
1945.
…………………………………………………………………….…………………………….
(b) Give two reasons why LEGCO was formed in Uganda.
(i) ………………………………………….…..………………………………………..….
(ii) ……………………………………………………………………………………………..
(c) Write LEGCO in full.
……………………………………………………………………………………………….
47. Study the sketch map of Uganda below and then answer the questions
that follow.
(a) Name the game park marked M on the map above.
……………………………………………………………………………………………
(b) How is river P important to the people of Northern Uganda?
…………………………………………………………………..……………………….
(c) Give two characteristics of lake marked K .
(i) ………………………………………………………………………………………
(ii) ………………………………………………………………………………………
8
K
M
P
50K
M
0
48. (a) What are human rights?
………………………………………………………………………………………………
(b) Give two examples of human rights.
(i) ………………………………………….…..………………………………………….
(ii) …………………………………………………………………………………………..
(c) How does the government promote human rights in Uganda?
……………………………………………………………………………………………
49. (a) What is the main duty of Uganda Police Force?
……………………………………………………………………………………………
(b) State three problems faced by Uganda Police Force when
carrying out its duties.
(i) ………………………………………….………………………………………………
(ii) ………………………………………………………………………………………….
(c) Name the department of police that controls road accidents.
……………………………………………………………………………………………..
50. Below is List A showing different bodies in Uganda with their
roles in List B but in wrong order. Match them correctly.
(i) NFA …………………………………………………………………………………
(ii) URA ………………………………………………………………………………
(iii) UHRC ………………………………………………………………………………
(iv) UBOS …………………………………………………………………………………
LIST A LIST B
NFA – protects human rights.
URA – conducts National population census.
UHRC – conserves forests.
UBOS – collects revenue.
9 Turn Over
For each of the questions 51 to 55 , answer EITHER Christian OR Islamic
questions but not both. No mark will be awarded to a candidate who
attempts both alternatives in a particular number .
51. EITHER:
(a) Give two ways in which Christians sin against God.
(i) ………………………….………………….…..……………………………………
(ii) ………………………………………………………………………………………..
(b) State one reason why some Christians sin against God.
…………………..…….…………………….…..………………………………………….
(c) Mention one thing Christians do after sinning against God .
…………………..…….…………………….…..………………………………………….
OR:
(a) Give two ways in which Muslims sin against Allah.
(i) ………………………….………………….…..……………………………………
(ii) ………………………………………………………………………………………..
(b) State one reason why some Muslims sin against Allah.
…………………..…….…………………….…..………………………………………….
(c) Mention one thing Muslims do after sinning against Allah .
…………………..…….…………………….…..………………………………………….
52. EITHER:
(a) What is meant by the term talents?
……………………………………………………………………………………………
(b) Write down the three talents Christians use to serve others.
(i) ……………………………………..…………………………………………………
(ii) ………….……………….…………..……………….………………………………
(iii) …………………………………………………………………………………………
10
OR:
(a) What is meant by the term talents?
……….………………………….….………………………………….…………………...
………………………………………………………………………………………………..
(b) Give three talents Muslims use to serve others.
(i) …………..………….……………………………………………….……………………
(ii) ……………………………………………………………………………………………..
(iii) ……………………………………………………………………………………………..
53. FOR BOTH:
(a) Give any one good act children always do at school.
……………………………………………………………………………………………….
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
