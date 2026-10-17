# Job ltsk_77f34ee07c6d444d93366bdaf8ece7f6-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 5 lesson(s) below of week 3 of the Social Studies scheme for Primary Five 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P5: one 40-minute lesson: 3–5 sections; about 14–28 points (meaning, examples, reasons, problems and solutions as the passages give); 5–8 activities.

lessonId=lles_283f96e109404be3aad963bee9808d7a: lesson 11, Monday, 1 period(s), 40 minutes.
  Unit: Uganda as an independent nation (theme: Living together in Uganda). Lesson: Citizenship — Ways of becoming a citizen of Uganda.
  Objectives: Define a citizen; State ways of becoming a citizen of Uganda

lessonId=lles_cd7c7c03f17b41adb2245b352c3b3c1c: lesson 12, Tuesday, 1 period(s), 40 minutes.
  Unit: Uganda as an independent nation (theme: Living together in Uganda). Lesson: Elections — Meaning and types of elections.
  Objectives: Define elections; Name the types of elections

lessonId=lles_d65048524b0941b99e21c41ea99910bc: lesson 13, Wednesday, 1 period(s), 40 minutes.
  Unit: Uganda as an independent nation (theme: Living together in Uganda). Lesson: Terms used in elections — Election terms and the importance of elections.
  Objectives: Explain terms used in elections; State the importance of elections

lessonId=lles_c93a1de7ede84717927d7171c796140f: lesson 14, Thursday, 1 period(s), 40 minutes.
  Unit: Uganda as an independent nation (theme: Living together in Uganda). Lesson: Bad practices during elections — Bad practices before, during and after voting.
  Objectives: Identify bad practices during elections; Suggest ways of avoiding bad practices in elections

lessonId=lles_01cc42c43fd84d91adeba440f1882f67: lesson 15, Friday, 1 period(s), 40 minutes.
  Unit: Uganda as an independent nation (theme: Living together in Uganda). Lesson: The Electoral Commission — Roles and challenges of the Electoral Commission.
  Objectives: State the roles of the Electoral Commission; Name challenges faced by the Electoral Commission

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
<passage id="lchk_c4cae182343748ec9eda6c629cf41c35" source="Primary 5 Social Studies Scheme of Work – Term 3" part="6">
standar
d SST
for
upper
classes
pg 141
5 Long
term
solutions
to deficit
budget
A learner
outlines the
long term
solutions to
deficit
budget
A learner
reads, spells,
writes and
pronounces
words
correctly
-Diversifying the
economy
-Widening the
tax base
-Privatization of
the economy
-taking
decisions
-making
choices
Inquiry
Guided
discussion
Explanation
Discussing
the
solutions
deficit
budget
Text
books
Mk
standar
d SST
for
upper
classes
pg 111
6 The
government
of Uganda
Elections A learner
defines
elections
commission
A learner
spells, reads,
pronounces
words of the
topic
correctly
-Meaning of
elections
-Importance of
elections
-nonviolent
conflict
resolution
-resolving
issues
Inquiry
Guided
discussion
Look and say
Discussing
elections in
Uganda
Text
book
Mk
SST Bk
5 pg
144
For more schemes of work, visit www.uganda.madpath.com
States roles
of electoral
commission
-The body that
conducts
elections
-The electoral
commission
without
fighting
-negotiating
7 The
Electoral
commissi
on
A learner
Defines
electoral
commission
States roles
of electoral
commission
States roles
of electoral
commission
A learner
spells, reads,
pronounces
words of
topic
correctly
-Meaning of
electoral
commission
-Duties of
electoral
commission
-nonviolent
conflict
resolution
-resolving
issues
without
fighting
-negotiating
Inquiry
Guided
discussion
Look and say
Discussing
elections in
Uganda,
Text
book
Mk
SST Bk
5 pg
144
6 1 Types of
elections
A leaner
identifies the
types of
elections
A learner
spells,
writes,
pronounces
words and
sentences
related to
the topic
-Types o
elections.
-General
elections
Bye elections
-Why bye
elections are
carried out
-Local elections
Referendum
-Problem
solving
-accepting
defeat
Inquiry
Guided
discussion
Explanation
Discussing
types of
elections
Text
books
MkSST
Bk 5 Pg
143
2 Bad
practices
during
elections
A learner
outlines the
bad
practices
during
election
exercise
A learner
spells, reads,
writes words
or sentences
related to
the topic
Bad practices in
elections include:
-Rigging
-Ballot staffing
-decision
making
-accepting
refusal
Guided
discussion
Explanation
Discussing
the bad
practices
during
elections
Text
bks
Mk std
SST for
upper
classes
Pg 80,
81
3 Election
exercise
The
electoral
systems
Secret
ballot
system
A learner
explains a
ballot system
Tells the
advs of a
A learner
spells, reads,
writes words
or sentences
related to
the topic
-The secret ballot
system
Advs & disadvs
of a secret ballot
system
-decision
making
-accepting
refusal
Guided
discussion
Explanation
Discussing
the secret
ballot
system and
the advs of
it
Text
bks
Mk std
SST for
upper
classes
Pg 80,
For more schemes of work, visit www.uganda.madpath.com
secret ballot
system
States the
disadvs of a
ballot system
-critical
thinking
-love
-problem
solving
4 The open
election
A learner
defines open
elections
Tells advs
and disadvs
of open
elections
A learner
spells, reads,
writes words
or sentences
related to
the topic
-Meaning of
open elections
-Advs open
elections
-Disadvs of open
elections
Love
Problem
solving
taking
decision
Guided
discussion
Explanation
Discussing
the secret
ballot
system and
the advs of
it
Text
bks
Mk std
SST for
upper
classes
Pg 80,
5 Organizat
ion of
elections
A learner
outlines all
officials of
election
exercise
A learner
spells, reads,
pronounces
and writes
words
related to
the topic
correctly
-Electoral
commission
-Returning
officers
-Presiding
officers
-Polling assistants
-Polling
constables
self-
awareness
knowing
one’s
responsibilit
y
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

<passage id="lchk_a51d4f1ab8634588a6770df9da1b613d" source="P.5 SST SCHEME TERM III 2019" part="2">
-Identify the importance of the National language.
-name the official language and why its used in Uganda
-Pronounce , read, spell and write words related to language.
National language.
-Language
-National language
-Importance
-Official language
-Reasons
-Reasons why Uganda is not having a national language.
-Role play
-Questions and answer
-Explanation
-Appreciation
-Critical thinking
-Love
-Respect
-naming different languages
-Learn the meaning of words from different languages
-Text books
-Resource
Persons
-A chart showing different words in different languages.
Functional SST bk 5
Page 172
3
Symbols of a nation (Capital city)
-Naming the capital city
- Identifying the importance of a capital city.
-Naming the towns which were once capital cities and years
-Pronounce , read and write words related to capital cities.
The National Capital
-The capital city of Uganda.
-Importance of a capital city.
-Towns that were once capital cities and years.
-Discussion
-Discovery
-Explanation
-Question and answer
-Love
-Respect
-Critical thinking
-Caring
-Identifying the importance of a capital city.
-Naming the towns that were once capital cities.
-Chalk board illustrations
-Text books
Mk std
Bk 5
Page 129
2
4
LIVING TOGETHER IN UGANDA
Uganda as an independent nation
National currency
-identifying Uganda’s currency and importance.
-Naming financial institutions and their roles.
-Pronounce, read and write words related to currencies.
National currency
-Uganda’s national currency.
-Denominations.
-Importance of currency.
-Financial institutions eg
BOU and roles
Commercial banks and roles.
-Question and answer
-Discovery
-Explanation
-Self awareness
-Love
-Appreciation
-Critical thinking
-Identifying Uganda’s currency and its importance.
-naming the financial institutions and their roles.
-Text books
-Papers having printed roles of currencies.
5
Democracy
-Explaining democracy
-Discussing the importance of democracy
-spells, reads , pronounces and writes words related to democracy
Democracy
-Definition
-Importance of democracy, functions
-Challenges of democracy
-Ways how democracy is practiced
-Explanation
-Discussion
-Discovery
-Question and answer
-Description
-Critical thinking
-Effective communication
-Explaining democracy.
-Discussing the importance of democracy
-Text books
-Chalk board illustration
3
1
Citizenship
-Explaining a citizen
The new words are challenges, election , citizen , conduct
Citizen ship
-Defining a citizen
-Ways in which one play can become a citizen.
-Ways how one can loose his/her citizenship.
-Roles of a citizen in practicing demoncracy
-Role play
-Role playing elections
MK stdbk 5 page 142-143
3
2
LIVING TOGETHER IN UGANDA
Uganda as an independent nation
Pronounces, spells, reads and writes words of bad practices
Bad practices during elections.
-before voting
-during voting
-after voting
3
Elections
-Explaining elections and its importances
-spells, read, pronounce and write words related to elections
Elections
-Definition
-Types of elections
Ballot paper elections
Lining elections
Appointing elections
-How elections are conducted
-Role play
-Explanation
-Discussion
-Critical thinking
-Respect
-Effective communication
-Inquiry
-Naming the different elections
-Role playing elections
-Drawing different elections materials
-Text books
4
Terms used in elections
-Explaining terms used in elections
Terms used in elections.
-polling station
-Bullot box etc
-Polling Assistant
-Polling officer etc
-Importances of elections
</passage>

<passage id="lchk_f3cec8ceab1a4b79933fc5a2d872dad2" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="15">
 To compile and update voters’ registers
 To carry out civic education.
 To register voters.
Electoral terms
a) Constituency
 A constituency is an area demarcated by the electoral commission for a candidate to stand
as a member of parliament.
b) Polling station
 A polling station is a place where elections are held.
c) Polling day
 A polling day is a special day organized by the electoral commission when election takes
place.
d) Ballot paper
 Is a special paper designed for voters to use during voting
e) Ballot box
A ballot box is a special box designed by the electoral commission where votes are cast and
kept
f) Voters’ register
 A voters’ register is a book designed by the electoral commission where all legible voters
are enrolled.
g) Polling assistants
 The se are officials that help the presiding officer in a given polling station
h) Presiding officer
38
 This is an officer appointed by the electoral commission to be in charge of the polling
station.
i) Polling agent
 This is the person who represents a candidate at a polling station.
j) Returning officer
 This is the officer in charge of elections in a district
k) Voting by Proxy
 This is when a person who is absent gives authority to another person to vote for him.
l) A proxy
 Proxy is the person who chose to vote for you
Activity
1- What is a constituency?
2- What is the main work of the electoral commission?
3- When is a by-election held?
4- In which way do elections promote human rights?
5- What is the best method of forming a government?
6- Give any three officials involved in an election at the polling station.
7- What is voting by proxy?
8- Name the current chairperson of the Electoral commission in Uganda.
Date Class Subject No. of pupils Time
P.5
TOPIC: The Government of Uganda
SUB –TOPIC: Electoral systems
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic: secret, president, electoral college
Content: Electoral systems
 This is way elections are conducted or carried out.
Examples of electoral system
39
 Secret ballot system
 Open elections
 Electoral college
Secret ballot system
 This is a system where ballot papers are used during the voting process by the voters.
Advantages of the secret ballot system
 The voter is free from interference when casting his / her vote.
 To the voters, the system is time saving.
 It can easily be monitored by computers.
Disadvantages of the secret ballot system
 It is difficult to voters who cannot read and write.
 It is expensive to conduct since it requires buying ballot papers, ballot boxes, and
transporting theme.
 The elections can easily be rigged.
Open elections
 This is where elections are done by either lining up of voters behind a candidates
(queuing) or by raising up hands.
 The elections are held when everybody is seeing each step.
 The system is common with LC elections at the lower levels.
Advantages of an open electoral system
 Results of the elections cannot be easily rigged.
 It is cheap to carryout in developing countries.
 It is simple to people who cannot read and write.
Disadvantages of an open electoral system
 It is tiresome since voters must be counted in person.
 It is not free since on lookers can easily affect the voter’s final decision.
 It cannot be easily computerized.
 It can promote enemity.
Qn. Under what ministry is the electoral commission?
 Ministry of Justice and constitutional affairs
40
Electoral college
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

<passage id="lchk_f99c684c29f64207a407b1bd185ea3cd" source="Primary Five Social Studies Notes 2020" part="51">
This is an election held to decide on an important issue in a country
Qn: When was the first referendum held in Uganda?
 In 1964.
Why
To decide whether Bunyoro should be given its two lost countries.
Qn: Give the meaning of the following terms
1. Ballot paper
 A ballot paper is a piece of paper on which voter marks candidate
of his or her choice.
Or
 A piece of paper with a candidate name and photo used during
an election.
2. Ballot box
 This is a special box where voters cast their votes.
3. Polling station
 This is a place where an election is held.
4. Presiding officer
 This is a person who heads all election activities of a polling station.
Polling agent
 This is a representative of a candidate at a polling station.
5. Polling assistant
 This is a person who helps the presiding officer.
6. Returning officer
 This is a person who is in charge of election in a district.
223
7. Electrol college
 This is a group of people chosen to represent others in an election.
8. Voting by proxy
 This is when a person voters on behalf of another.
9. Universal adult suffrage
 This is when a person votes on behalf of another.
10. Election petition
 This is a way of challenging election results in courts of law.
Qualities of a voter in Uganda.
 A voter should be a citizen of Uganda
 A voter should be eighteen years and above
 A voter should be registered
Qn: Which body organizes national elections in Uganda ?
 Electoral commission
Qn: Under what ministry is the electoral commission?
 Ministry of justice and constitutional affairs.
Qn: What title is given to the head of the electoral commission in
Uganda?
 Chairperson electoral commission.
Qn: Who is the current chairperson electoral commission?
 Justice Simon Byabakama.
Systems of elections
i) Open elections
ii) Secret ballot
Qn: What is an open election?
224
 This is a system of voting by lining behind orraising hands.
Advantages of open elections.
i) Results cannot be easily rigged
ii) It is a cheap
iii) It caters for illiterates
Disadvantages of open elections
 It is tiring
 It leads to enmity
Qn: What is secret ballot election?
 This is a system of election where voters use ballot papers to choose
leaders.
Advantages of secret ballot
 It is time saving.
 The voter is free from interference when casting voters.
Disadvantages of secret ballot
i) It is easy to rig votes
ii) It is expensive
Duties of electoral commission
i) To conduct free and fair elections
ii) It provides elections materials
iii) It registers voters
iv) To announce election results
v) To carryout civic education
Vi) To demarcate polling stations
225
Qn: Why does the elections commissions display voters register
beforeelection?
i) To eliminate non-citizens.
ii) To eliminate the dead.
iii) To enable people change polling stations.
Special groups of people represented in the parliaments
i) Women
ii) Army
iii) Youth
iv) Workers/civil servants
v) People with disabilities
Qn: What is a constituency?
 This is an area represented by amember of parliament.
Bad practices during elections
i) Vote rigging
ii) Bribing voters during elections
iii) Bribing voters during elections
iv) Ballot stuffing
v) Multiple voting
vi) Violence during elections /fighting
vii) Intimidating voters
viii) Omission of voter names.
ix) Creation of ghost polling station.
226
x) Torturing opponents
Importance of voters’ register during voting.
i) It helps to know the number of voters
ii) For identification
iii) It controls multiple voting
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

<passage id="lchk_aa85ec987f1e41cf99a1ba716ad51f70" source="Excel P 5 SST Term III" part="9">
conducting regular free and fair elections in the country.
It is under the Ministry of Justice and Constitutional affairs.
Justice Simon Byabakama is the current chairperson of the Uganda electoral
commission.
The chairperson Electoral commission is appointed by the president and approved
by the parliament.
General elections in Uganda are conducted after every five years.
Roles of the Electoral commission
❖ To register voters and candidates.
❖ To prepare election materials
❖ To train the electoral officials
❖ To count votes and release election results.
❖ To carry out civic education concerning elections/ to carry out voter education.
❖ To demarcate polling stations and constituencies.
Challenges faced by the Electoral commission in Uganda.
❖ Shortage of funds.
❖ Poor response from the voters.
Page 16
❖ Dishonest electoral officials.
❖ Delay of election materials
❖ Election malpractices.
❖ Voter bribery due to increased poverty among the electorate.
Possible solutions to the challenges facing the Electoral commission.
❖ By carrying out effective voter education. This can help to reduce the number of
invalid votes.
❖ By eradicating poverty among the electorate.
❖ By distributing election materials in time.
❖ By punishing dishonest electoral officials.
❖ By providing adequate funds to the electoral commission.
Importance of elections
❖ They promote democracy in the country
❖ They promote peaceful change/ transition of leadership.
❖ They enable people get rid of bad leaders
❖ They enable people to choose their own leaders.
❖ They promote respect for human rights.
ELECTION MALPRACTICES.
These are illegal acts done during elections.
The election malpractices are the various forms of vote rigging.
Some of these practices may lead to cancellation of election results and hence
leading to by-elections.
These practices include;
• Voter bribery.
• Multiple voting.
• Torturing of opponents.
• Campaigning on the Election Day.
Bad practices that happen during voting.
▪ Bribing voters during elections.
▪ Harassing voters of a particular candidate.
▪ Ballot stuffing (putting pre-ticked ballot papers in the ballot box before elections)
▪ Grabbing and stealing ballot papers.
▪ Campaigning on the voting day.
▪ Cheating when counting votes.
Bad practices that happen after elections.
▪ Making fun of the losers of an election.
▪ Mis-recording of election results.
▪ A candidate refusing to accept defeat.
▪ Attacking a voter who has not voted a particular candidate.
▪ Unnecessary delay to announce final results.
Page 17
THE ELECTORAL SYSTEMS.
▪ Secret ballot system
▪ Open election system
(i) Secret ballot system
This is a system where a voter is given a ballot paper and secretly selects a person
he/she wants.
This is a modern way of voting in the whole world.
Advantages of secret ballot system
❖ It promotes friendship among people.
❖ Elections can easily be monitored by computers.
❖ A voter is free from interference.
Disadvantages of secret ballot system
❖ It is very expensive to conduct.
❖ Votes can easily be rigged.
❖ It is difficult to the illiterates and the blind.
❖ Election results take long to be declared.
(ii) Open elections
These are elections held when everyone is seeing each step.
It is done by lining up behind the candidate or by putting up the hands.
This is the cheapest way of voting in many places.
This was common in the past.
Advantages of open elections
❖ They are very cheap to conduct.
❖ Results can not easily be rigged.
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
