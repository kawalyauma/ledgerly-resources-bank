# Job ltsk_be5254648795450a989bf1207326194a-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 5 lesson(s) below of week 6 of the Social Studies scheme for Primary Four 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P4: one 40-minute lesson: 2–4 sections; about 12–24 points; meanings, examples and uses; 5–7 activities.

lessonId=lles_f7473e5aeca249a29b9120d43232284d: lesson 26, Monday, 1 period(s), 40 minutes.
  Unit: HOW TO MEET PEOPLE’S NEEDS IN OUR DISTRICT (theme: Living together in our district). Lesson: Basic needs and luxuries — Basic needs and luxuries.
  Objectives: Distinguish basic needs from luxuries.

lessonId=lles_85d0f55e7eb24e209bd552b1c40a8f2d: lesson 27, Tuesday, 1 period(s), 40 minutes.
  Unit: HOW TO MEET PEOPLE’S NEEDS IN OUR DISTRICT (theme: Living together in our district). Lesson: Basic needs and luxuries — Part B — Basic needs and luxuries.
  Objectives: Practise identifying and explaining basic needs and luxuries.
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points ('- ' points, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

lessonId=lles_75486637a1f34805a5f612a83d4d4eeb: lesson 28, Wednesday, 1 period(s), 40 minutes.
  Unit: HOW TO MEET PEOPLE’S NEEDS IN OUR DISTRICT (theme: Living together in our district). Lesson: Social services in our district — Social services in our district.
  Objectives: Explain social services and name examples.

lessonId=lles_1008a1552ac24872b570c66debf0d242: lesson 29, Thursday, 1 period(s), 40 minutes.
  Unit: HOW TO MEET PEOPLE’S NEEDS IN OUR DISTRICT (theme: Living together in our district). Lesson: Social services in our district — Part B — Social services in our district.
  Objectives: Practise identifying and explaining social services in our district.
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points ('- ' points, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

lessonId=lles_0c880aa4f417485288d096b30f2e1aa3: lesson 30, Friday, 1 period(s), 40 minutes.
  Unit: HOW TO MEET PEOPLE’S NEEDS IN OUR DISTRICT (theme: Living together in our district). Lesson: Social service centres — Social service centres.
  Objectives: Explain the meaning of social service centres.

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
<passage id="lchk_fc0c8851ffe548008fa7de367dfd1f6e" source="P 4 SST Scheme3" part="1">
1
PRIMARY FOUR S.ST SCHEME OF WORK FOR TERM III 2023
W
K
P
D
TOPI
C
S/
TOP
IC
COMPETENCES CONTENT METHODS
/
TECHNIQU
ES
ACTIVI
TIES
LIFE
SKILLS
&
VALUES
T/L
AIDS
REF R
E
M
.
SUBJE
CT
LANGUA
GE
1 GOING THROUGH HOLIDAY WORK
2 1 HOW
TO
MEE
T
PEO
PLE’
S
NEE
DS
IN
OUR
DIST
RICT
Soci
al
serv
ices
in
our
distr
ict
The
learner
;
-
differe
ntiates
betwee
n basic
needs
and
luxurie
s.
-
explain
s the
meanin
g of
social
service
s.
The
learner
writes,
pronounc
es and
uses the
following
terms;
- Needs
services.
-
Veterinar
y doctors.
- teachers
- farmers
- bankers
-
carpenter
s
Social
services in
our district
- learning
the new
words/term
s
Differentiati
ng basic
needs from
luxuries
-Giving the
meaning of
social
services.
- Giving
examples of
social
services in
our district.
- Whole
class
discussion
-
brainstormi
ng
- guided
discovery
-
Answer
ing oral
questio
ns
-
writing
structu
red
notes.
- clear
pronunci
ation of
terms
- proper
utilizatio
n of
available
resource
s
-
creativity
-Chalk
board
illustrat
ion
-Text
books
Compr
ehensi
ve
Social
Studie
s,
Pupils
book 4
Pg
141-
152.
2
-gives
exampl
es of
social
service
s
-
treatment
-
governme
nt
2 Soci
al
serv
ice
cent
ers
in
our
distr
ict
The
learner
;
-
explain
s the
meanin
g of
social
service
s
centres
- gives
exampl
es of
social
service
centre
in our
district
-
mentio
The
learner
writes,
uses and
pronounc
es the
following
terms;
- hospital
- petrol
station
- Police
post
-
responsib
ility
- service
Social
service
centres in
our
district.
- meaning
of social
services
centres
Examples of
social
service
centres
- Service
providers at
different
social
service
centres.
- group
discussion
- guided
discovery
-
brainstormi
ng
-
drawin
g social
service
s
centres
-
taking
structu
red
notes.
-
visiting
the
sick-
bay.
- drawing
and
colouring
-
appreciat
ion
- care
and love
- chalk
board
illustrat
ion
- sick
bay
Compr
ehensi
ve
Social
Studie
s,
Pupils
Bk 4.
Pgs
161-
170.
3
ns the
differe
nt
groups
who
work in
differe
nt
social
centres
.
Edu
cati
on
serv
ices
The
learner
;
-
mentio
ns the
two
types
of
educati
on
- states
the
meanin
g of
each
type of
The
learner
writes,
pronounc
es and
uses the
terms
- informal
education
- Formal
education
-
discipline
-
carpentry
- conduct
Education
services
- Types of
education
- meaning
of each type
of
education
- what
was/is
taught in
informal
and formal
education.
-
brainstormi
ng
- story
telling
- guided
discovery
- class
discuss
ion
about
the
history
of
educati
on
-
taking
structu
red
notes.
-
appreciat
ion
- care
and love
- Proper
utilizatio
n of
available
resource
s.
-
chalkbo
ard
illustrat
ion
- text
books
Compr
ehensi
ve
Social
Studie
s book
4, pg
141-
142
4
educati
on.
-
outline
s what
is
empha
sized
during
inform
al and
formal
educati
on.
-
constructi
on
Imp
orta
nce
of
educ
atio
n
The
learner
;
- states
the
import
ance of
educati
on.
-
explain
s why
UPE
was
The
learner
writes,
pronounc
es and
uses the
terms.
-
universal
- illiteracy
-
secondary
- hygiene
-
education
Importanc
e of
education
- stating
reasons for
introductio
n of UPE
- Problems
facing
schools
under UPE
policy with
their
solutions.
- whole
class
discussion
-
brainstormi
ng
- guided
discovery
-
answer
ing oral
questio
ns
-
writing
structu
red
notes
-
appreciat
ion
- care
and love
-
responsi
bility
- text
books
-
chalkbo
ard
illustrat
ion
Compr
ehensi
ve
Social
Studie
s bk 4,
pg
141-
142
5
introdu
ced
-
identifi
es
proble
ms of
UPE
schools
and
their
solutio
ns.
-
sanitation
- skills
Tran
spor
t
serv
ices
</passage>

<passage id="lchk_5697e9d412874540b9ba874686bebc18" source="P 4 SST Lesson Notes Term 3" part="1">
1
HOW TO MEET PEOPLE’S NEEDS IN OUR DISTRICT
SOCIAL SERVICES IN OUR DISTRICT
Lesson one
New words
- Needs/services
- Social services
- Veterinary doctors
- Doctor
- Teacher
- Farmer
- Banker
- Carpenter
- Treatment
- Communication
- Transport
1. What are needs?
These are things we should get in order to live a better life.
These are two different types of needs and these are:
a) Basic needs
b) Luxuries
a) What are basic needs?
These are things that we cannot live without e.g. food, water, education, clothing, shelter,
medical care
Reasons why some homes lack basic needs
i) poverty iii) unemployment
ii) laziness iv)disasters
v) big number of people in a home
Activity
2
1.Where do people get the following?
i) food ii)water
2. Give two reasons why some families lack enough food.
i)……………………………………………………….
ii)……………………………………………………….
3.Which crop provides a raw material for making clothes?
4.Give two reasons why people build houses
i)…………………………………………
ii)………………………………………….
5.Give two examples of natural disasters and man-made disasters
Natural disasters Man-made disasters
a)………………………………
b)………………………………
a)…………………………………
b)…………………………………
Lesson two
Luxury items
b) What are luxuries/non basic needs?
These are things that people can live without e.g. Television, cars, play station, etc
c) Make a list of the needs in;
i) Your family
ii) Your school
iii) Your local area.
Activity-2
3
1. Give any three examples of basic needs.
i……………………………………….
ii………………………………………
iii……………………………………..
2. Why is a car not a basic need?
……………………………………….
3. Mention any three things we can live without.
i………………………………………..
ii……………………………………….
iii………………………………………
Lessons 3
Social services
2. What are social services?
These are needs provided by government to improve people’s welfare / make people’s lives
better.
3. Examples of social services in our district
i. Education services
ii. Medical services
iii. Security services
iv. Transport services
v. Communication services
vi. Banking services
vii. Insurance services
viii. Housing services
ix. Water supply services
x. Electricity services
xi.
Activity 3
1. What are social services?
…………………………………………………………………….
2. Apart from keeping money safe, give three other importance of banks.
i……………………………………………………………………….
ii………………………………………………………………………
iii………………………………………………………………………
3.Apart from education, name other four social services provided in your district.
4
i)………………………………………………………………………
ii)……………………………………………………………………...
iii)……………………………………………………………………..
iv)……………………………………………………………………..
4 State any three problems faced by the government when providing social services.
i……………………………………………………….
ii………………………………………………………
iii………………………………………………………
Lesson 4
4. What are social service centers?
These are places from which social services are provided to the people.
5. Examples of social service centers in our district
• Schools
• Hospitals
• Police stations/ police posts
• Banks
• Water sources
• Petrol stations
• Post offices
Activity
Identify any two groups of people who work in each of the social service centres given
1.a) School
i) ……………………
ii) …………………..
b) Hospital
i) _____________
ii) _____________
2.List any four service providers in our district.
i)………………….
ii)…………………
5
iii)………………..
iv)………………..
Lesson 5
EDUCATION SERVICES
These are two types of education and these include;
a) Formal education
b) Informal education
Informal Education
Informal education is the type of education which is mainly got from home and it doesn’t involve
</passage>

<passage id="lchk_d3587800f56c42258e6f0667ea447b16" source="Primary Four Social Studies Schemes of Work, Terms 1–3" part="7">
people’s
responsibiliti
es in the
district.
0754895241/0783298434 Page 19
- Obeying laws.
- Participating in
community work.
- Reporting wrong
doers.
- Participating in
making laws.
- Maintaining proper
activities.
- Involving in proper
activities.
- Helping and caring
for others.
- Caring for the sick
etc.
2 1
to
5 How law and
order is kept
in our district
- Give the group that provides
security.
- State the name of Uganda’s
Army.
- Mention departments of the
police and their duties.
- The head of the police force
in Uganda.
- Give the ministry in which
the police and Army belong.
- State functions of the police.
- Give the functions of the
prisons.
Groups that provide
security
 Police
 Army
 Private security
guards.
 Prisons
 Local council
 Uganda’s army in
Uganda.
 People defence
forces.
Departments of the
police
 CID
 Anti-Riot police.
 Radio and signal
section.
 Passport section.
 Dog section.
 Fire brigade.
 General Duty
Section.
 Patrol section.
 Traffic police
 Police Anti-terrorism
unit.
 Head of the police is
lieutenant general
Kale Kayihura.
(Inspector General of
- Give the
security organs
in our district.
- Demonstrate
duties of the
police
departments.
- Mention the
leaders of
police force
and prisons.
- Give the
functions of the
police and
prisons
- Give the
ministry that
takes the
police, prisons
and the Army.
Mk
standare
d s.s.t
book 4
pg 63.
0754895241/0783298434 Page 20
police)
 The police is under
the ministry of
internal affairs.
 The Army is under
the ministry of
defence.
Functions of the police
 It investigates on
crimes.
 Stops riots.
 Puts out fire
 Locates lost and
crushed planes.
 Arrest wrong does
 Protects people and
their property.
Functions of the
prisons.
 They transform law
breakers in to law
abiding citizens.
 They keep law
breakers away from
the public.
 They teach prisoners
skills e.g. carpentry.
 The commissioner of
prisons in Uganda is
Mr. Johnson
Byabashaija.
 The prisons are
under the ministry of
internal affairs.
3 1
to
5
How to
meet
people’s
needs
Social services  Explain what social services
are.
 Give examples of social
services.
 Outline problems people
faces in trying to satisfy their
needs.
 Mention solutions to the
problems.
 Explain what social services
Social services.
- These are benefits
given to people to
live a good life.
Groups of people who
provide social services.
- Define social
services.
- Give examples
of social
services
- Mention groups
of people who
Text books social
services centres
in our
environment
Monitor s.s.t
pupils bk 4 pg 50
– 59
Fountain S.S.T bk
4
0754895241/0783298434 Page 21
are.
 State ways of caring for social
services.
- Government
- Local leaders
- Doctors / medical
workers
- Teachers.
- Veterinary officers.
- Farmers.
- Bankers.
- Carpenters.
- Security organs.
- Parents.
- Shop keepers.
Examples of social
services.
- Education services.
- Medical services.
- Security services
- Transport services.
- Water services.
- Banking services
- Road maintenance
- Postal and
communication
services.
Problems faced by
people in meeting their
needs.
- Embezzlement
- Poverty
- bad weather
- Shortage of food.
- Theft
- Corruption
- Irresponsibility
- Laziness
- Over population
- Accidents
- Diseases
provided social
services.
- Draw different
social services
centres.
- Visiting some
social services
centres.
- Matching social
service.
- Discussing
ways and
means of
reducing
poverty
- Visiting any
nearly services
centre
observes and
</passage>

<passage id="lchk_84df7429f1964088b2638ed0af98c9b9" source="Primary 4 Social Studies Scheme of Work, Term 3, 2022" part="5">
This is the violation of children's .Defines the term child|.reads and writes senteng Discussion children's rights |.Empathy Posters about child abus{.MK Standard SST bk 4
Examples of child abuse abuse related to child abuse —_| Illustration answering oral quq.Critical thinking pg8é
.defilement,battering,child sacrifiq.{dentifies examples of |.uses the structures related to . drawing pictures about
abusive language ,child labour etc/child abuse child abuse, child abuse


Medical service [The learner; [The learner; [Group discussioy.Naming health ce].Appreciation _| posters [Comprehensive SST]

Medical service centres are; _|. lists the services we gd pronounces,reads and spells the In our district. |.Care pictures in pl's bk bk 4 pg 90

dispensaries hospitals and clinics|the health centres. [words related to medical|.Demonstration |.Drawing medical4.Self-esteem —_ |comprehensive .MK Standard SST bk 4
centres. SST bk 4 pg 90. pe 98.

Medical service providers Include;
.doctors,nurses,mid-wives,tab attd,Names the people whg.constructs sentences using the

medical services in our|words related to medical services
Services we get at health centres include; correctly.
.immunisation, treating the teeth etc

LIVING TOGETHER [Security service [The learner; ‘The learner; Discussion. _|. Naming security s].Problem-solving [Pictures in comprehensiv|.MK Standard SST bk 4
IN OUR DISTRICT .providers of security .identifies the security |.reads and spells the wor.Demonstration |providers. |.Self awareness |SST book 4 pp63 99}
: people are protected from; providers In our districtrelated to security. Discovery Giving examples d Critical thinking Comprehensive SST
thleves,killers,kidnappers,conflictd identifies how security Is Insecurity in our af.Appreciation bk 4 pg91
.how security organs provide seci provided .
‘| HOW TO aa servicesTransport service, [The learner; [The learner; “Mustration __|.Practicing safe wa.critical thinking |.A chart showing means d .MK Standad SST bk 4
PEOPLE'S NBour district. |.Transport Is the movement of pet.defines the term trans| pronounces,reads and sp|.Discussion crossing roads. | Self esteem transport. pg 102
|goods from one place to another.|.ldentifies different typ words related to transport In our Discussing the Imj Appreciation Comprehensive SST
? Types of transport, Itransport, district, jof roads In our district. bk 4 pg 83.
.road transport,rallway transport,|.mentlons means of road
|and water transport. transport.
Road Tansport.
Types of roads
Means of road transport
[Advantages and disadvanta| different
types of road transport,
LIVING TOGETHER The learner; ie learner; ‘Debate ‘Comparing Giferd Assertiveness [A chart showing means d Mik Standard SST Bk
IN OUR DISTRICT .Adentifies types of tralreads and practices struct,Oiscussion _—_|oftransport, —_|.Appreciation _|rallway transport, [pgs 103-104,
land thelr advantages, |related to rallway transpa.lilustration _| Answering oral qu.Care .Comprehensive SST BK4
Types of trains(cargo trains and q.mentions the means o}.mentions the means of rallway .Matching the meg.Critical thinking pg 88.
train) water transport, transport. -|types of transport.
It's advantages and disadvatages| Debating
Water Transport.
means of water transport
Advantages and disadvantage
7] [Social servicedAlr Transport The learner; The learner; ‘Demonstration |Explaining how alr].Cooperation __|.Pictures in pupll's bk MK|.Comprehensive SST pl's
</passage>

<passage id="lchk_4fedcc40996d4868b247f194b8acdef9" source="P 4 Primary Four SST Scheme OF Work Teacher AC" part="7">
- Helping and caring
for others.
- Caring for the sick
etc.
2 1
to - Give the group that provides
security.
Groups that provide
security
- Give the
security organs
Mk
standard
SST
Page 20
5 How law and
order is kept
in our district
- State the name of Uganda’s
Army.
- Mention departments of the
police and their duties.
- The head of the police force
in Uganda.
- Give the ministry in which
the police and Army belong.
- State functions of the police.
- Give the functions of the
prisons.
 Police
 Army
 Private security
guards.
 Prisons
 Local council
 Uganda’s army in
Uganda.
 People defence
forces.
Departments of the
police
 CID
 Anti-Riot police.
 Radio and signal
section.
 Passport section.
 Dog section.
 Fire brigade.
 General Duty
Section.
 Patrol section.
 Traffic police
 Police Anti-terrorism
unit.
 Head of the police is
lieutenant general
Kale Kayihura.
(Inspector General of
police)
 The police is under
the ministry of
internal affairs.
 The Army is under
the ministry of
defence.
Functions of the police
 It investigates on
crimes.
 Stops riots.
 Puts out fire
 Locates lost and
in our district.
- Demonstrate
duties of the
police
departments.
- Mention the
leaders of
police force
and prisons.
- Give the
functions of the
police and
prisons
- Give the
ministry that
takes the
police, prisons
and the Army.
book 4
pg. 63.
Page 21
crushed planes.
 Arrest wrong does
 Protects people and
their property.
Functions of the
prisons.
 They transform law
breakers in to law
abiding citizens.
 They keep law
breakers away from
the public.
 They teach prisoners
skills e.g. carpentry.
 The commissioner of
prisons in Uganda is
Mr. Johnson
Byabashaija.
 The prisons are
under the ministry of
internal affairs.
3 1
to
5
How to
meet
people’s
needs
Social services  Explain what social services
are.
 Give examples of social
services.
 Outline problems people
faces in trying to satisfy their
needs.
 Mention solutions to the
problems.
 Explain what social services
are.
 State ways of caring for social
services.
Social services.
- These are benefits
given to people to
live a good life.
Groups of people who
provide social services.
- Government
- Local leaders
- Doctors / medical
workers
- Teachers.
- Veterinary officers.
- Farmers.
- Bankers.
- Carpenters.
- Security organs.
- Define social
services.
- Give examples
of social
services
- Mention groups
of people who
provided social
services.
- Draw different
social services
centres.
- Visiting some
social services
Text books social
services centres
in our
environment
Monitor s.s.t
pupils bk 4 Pg. 50
– 59
Fountain S.S.T bk
4
Primary s.s.t
Uganda bk 4 pg.
58
Page 22
- Parents.
- Shop keepers.
Examples of social
services.
- Education services.
- Medical services.
- Security services
- Transport services.
- Water services.
- Banking services
- Road maintenance
- Postal and
communication
services.
Problems faced by
people in meeting their
needs.
- Embezzlement
- Poverty
- bad weather
- Shortage of food.
- Theft
- Corruption
- Irresponsibility
- Laziness
- Over population
- Accidents
- Diseases
- Insecurity.
Solutions
- Creating
employment
opportunities for
young people.
centres.
- Matching social
service.
- Discussing
ways and
means of
reducing
poverty
- Visiting any
nearly services
centre observe
and record
services.
- Suggesting
things that
destroy our
social services
centres.
Page 23
- Providing education
on methods of
producing more
quality food.
- Providing medical
services.
</passage>

<passage id="lchk_a44ee0da9d9845c19b9c52d044cc3865" source="Primary 4 Social Studies Scheme of Work, Term 3, 2022" part="7">
ithe government to its people to njservices. words and structures rela.Representation {Answering oral quj.Critical reasoning Comprehensive SST
Wha are utilities? .mentions some examp|social services, Identifying types of schools bk 4 pg 92. :
These are special things which wesoclal sevices In our area, In our district.
communities to live a better life,
examples of utilities;
.water, electricity, telephone.
Examples of social services. The learner; The learner;
education service .glves examples of socly,pronounces and reads the words
Types of schools In our district services In our district. |rela ted to education service.
What the government provides fo|.identifles types of schools In our
leducation. district.
1


iz HOW PEOPLE Banking The learner; The learner; “Identifying banks |.Appreclation | banknotes MK Standard SST pl's bk4

MEET THEIR Examples of banks In our district,|. mentions the service d.pronounces,reads and w/.Discussion _—| district. pictures In pl's bk MK Sta pg 110.

NEEDS |The Central Bank(Bank of Ug: ’ank to people, the words related to the #.Demonstration |.Explaining the ser pgi10 [Comprehensive SST bk 4
Commercial banks gives examples of banks In our provided by the banks, pe 93.
Micro-finance Institutions. district.

[| Services provided by the banks.
7) Po: id communication servic Discussion _| Listening to t “Aresourceful person. [MK Standard SST p's
|.Communication Is the sending an|.Defines the term steads writes and spells the person. Appreciation A chart of means of com#bk 4 pgi10.
lof messages. communication. words related to the com|.lliustration _—|.Drawing different] Assertiveness _|,Pictures in pl's bk MK st fomprehensive SST bk 4
|Anclent methods of communicatl4 Mentions traditional methods Discovery lof communication| Self-esteem pe 91.
.drumming,horning,clapping,whis|of communication.
Modern methods of communicati].Mentions modern methods of
.using telephones, intenet,faxes,le| communication.
[Housing service The learner; ihe learner -Group discussioy.Naming groups of set esteem ‘| .Achart of houses. (MK Standard SST BK4
The role played by the district adj dentifies the types of |,pronounces,reads and sf.Discovery workers who are ertiveness —_| Pictures In gl's bk pgs 10{PG107, ra
District workers who are given Nhouses In our district. |words related to housing as aservice laccommodation, appreciation
.Bullding materials used. mentions the reasons why we .Giving reasons why we
Types of houses In our district. |sleep in houses. sleep in houses.
IVING TOGETHER People who HDoctors and other medical work The learner; The learner; “Observing picture|.Assertiveness __|,Picturesin MK bk 4 pg 14MK Standard SST Dk4
IN OUR DISTRICT. Jus to meet ou).the work of doctors enumerates people wH}.pronounces,teads and w|.Discussion .Identifying the du}.Appreciation pgiis.
needs, .the duties of nurses and other m¢help us to meet our ne¢structues related to the s| .!llustration the prisons officer{.Critical thinking
workers. . identifies the work of dproviders In our area,
Police and Prison officers. In our district.
police departments mentions the roles played by
functions of prison officers ithe prison officers.
| The learns “Listing people wh{.Love Pictures in MK bk4 pgii9|MK Standard Sst bk4 |
Roles played by groups of peopl identifies the services {.writes the structures reld.Inquiry services to people|Care pgii9
</passage>

<passage id="lchk_40b165631ac142ad9070c636563c4efc" source="P4 Social Studies Scheme of Work, Term III" part="1">
P.4 SOCIAL STUDIES SCHEME OF WORK
TERM III
WK PD TOPIC SUBTOPIC SUBJECT COMPENCES LANGUAGE COMP CONTENT METHODS ACTIVITIES SKILLS T/L AIDS REF REM
1 1 How to meet
people’s
needs in our
district
Types of
needs
The learner;
- Give the meaning of
basic needs
- Mentions the types of
basic needs
- States the examples of
basic needs
- Mentions the examples
of non- essential needs
The learner;
Pronounces, spells and
uses new words correctly
- Basic
- Needs
- Shelter
- Essential
- Clothing
Basic needs / essential needs
- Things that people cannot
do without
Types of needs
- Basic needs
- Non- essential needs
Examples of basic needs
- Food and water
- Clothing
- Shelter
Examples of non-essential
needs
- Cars
- Shoes
-Discussion
-Discovery
-Giving the importance of hospitals
-Writing
-Effective communication
-Sick bay
-Comprehensive SST book 4
WK PD TOPIC SUBTOPIC SUBJECT COMPENCES LANGUAGE COMP CONTENT METHODS ACTIVITIES SKILLS T/L AIDS REF REM
II Social
services
Education
The learner;
- States the meaning of
social services
- Gives the examples of
social services
- States the meaning of
education social service
centres
- Mentions the examples of
institutions in our district.
- States the type of
schools
- Name the types of
schools in our district
- Gives the differences
between private and
government schools.
- Gives the similarities
between private and
government schools
- Mentions the types of
education
The learner;
Pronounces, and spells
new words
- Social services
- Education
- Security
- Health
Types of schools
- Private schools
- Government schools
Differences between
private schools and
government schools
- In private schools
pupils pay school fees
while in government
do not.
- Private schools are
owned by individuals
while government
schools are owned by
government
- Private schools are
facilitated by owners
while government
schools are facilitated
by government
Types of education
- Formal education
- Informal education
Formal education
- Got from schools
- Introduced by
Missionaries
Informal education
- Got from home
- Elders are the teacher
Things taught under
informal education
- Cooking
- Hunting
- Greeting
Social services
Services provided to people by
the government and non-
governmental organizations e.g.
- Education
- Security
- Transport
Education
The process of acquiring
knowledge, skills and values
Sources of education
- Schools
- Colleges
- Institutions
Guided discovery
Discussion
Writing notes
Listing the skills acquired from informal education
Writing
Reading
Chalkboard illustration
Resource person (Tr.)
Comprehension SST Book 4
WK PD TOPIC SUBTOPIC SUBJECT COMPENCES LANGUAGE COMP CONTENT METHODS ACTIVITIES SKILLS T/L AIDS REF REM
III Health
services
The learner;
- Gives the sources of
health services
- Mentions the people who
offer health services
- State the hospitals in our
district
- Gives the biggest
hospital in Uganda
- Mentions the examples of
health services
- Gives the importance of
health services
- States the ways a
government supports
the health sector
- Gives problems
affecting the provision of
medical services
- Gives the solutions to
problems.
The learner;
Pronounces, spells and
uses new words correctly
- Health
- Healthy
- Hospital
- Dispensaries
- Clinics
Health service centres
- Hospitals
- Clinics
- Dispensaries
People who offer health
services
- Doctors treat sick people
Nurses – care for sick people
Hospitals in Uganda
- Mukono health centre IV
- Nagalama hospital
Biggest hospital in Uganda
</passage>

<passage id="lchk_dcd8cd6cfffa46a0b1e9565735b52296" source="Sipro P4 Beginning Of Term 3 By Kalulu Brian 0755518221" part="2">
36.Either:Name the mother of Jacob and Esau.

Or —: Name the mother of Prophet Muhammad (PBUH).

37.Either: State any one way Jesus Christ helped Lazarus.

Or —: Why are Muslims encouraged to pay zakat?

38.Either: State any one way the devil tempted Jesus in the wilderness.

Or _ : State any one way Prophet Muhammad (PBUH) suffered.

39.Either: Name the Christian symbol that promotes salvation.

Qr =: Name the Islamic symbol that is a source of hadith.

40.Either: How is Baptism important to Christians? a

Or — : Why ee Muslims circumcise their male children?

SECTION B: 60 MARKS
Questions 41 to 55 carry four marks each.
41.2) What term is given to the violation of children's rights?

State any teen Wye GR
b) State any theo ways children's rights are violated in your district,
-

ii)

ee

 Montion anu a. en
©) Mention any one danger of violating chidren's rights


42.Match the following informa

GatA tion correctly.
Buganda Kingdom Om
Busoga Kingdom omenge
Rwenzururu Kingdom Kabaka
Bunyoro Kingdom Kyabi i"
i) Buganda Kingdom _e
ii) Busoga Kingdom

ili) Rwenzururu Kingdom

iv) Bunyoro Kingdom

43.a) What is the main role of the school bursar?

b) State any two ways a school benefits from the community.

i)

ii)

c) Mention one item a community can get from the school.

eS Mention any two groups of people who tell legends.
i

ii)

b) State any two ways legends are important to children.

i)

ii)

45.a) Name one example of tree species in natural forests.

b) State any two characteristics of natural forests.

| ae

ii)

c) How do forests promote people's health?

46.a) Draw any two means of water transport.

b) State any two uses of transport to people.

i)
ii)

al Services Tel. 0414669050/ 0755-274911/0776-274911
2.4 SOCIAL STUDIES WITH RELIGIOUS EDUCATION BEGINNING OF TERM II - 2023


47.Study the sketch map of Kitu Village below and use

it to answer the questions
that follow.

Key:
P - Police
M- Market

a) Name the feature on the road marked A and T.
iA (ii) T.
b) What is the direction of P from M?

c) Name.one basic need got from the place marked M.

. 7
48.a) Mention the type of leaders where teachers belong.

b) Give any two other types of leaders apart from (a) above.
i)
ii)

c) How is a class monitor important?

49.a) Name the town where Entebbe international airport is found.

b) Apart from airports, mention any two other important places.
i) a:
ii)

c) How is an airport important? _ 5

50.a) Mention any two examples of economic activities
i)
ui) ; e ee ae
b) State any two problems faced by people who Carry out economic activities 4
i)
ii)
Gay © Soro Ecueatonal Series Tet O41 4559050 0755-27591 VOT7ETIAGIT
AS SOCIAL STUDIES WITH RELIGIOUS EDUCATION BEGINNING OF TERM «i. 2023

CamScanner

jneach of the questions 51
C to 55
nsstions but not both 0 99, answer EITHER the Christi i
questions on th e Christian OR Islamic
Eierded to a n the same numb i
pupil who attempts both questions ina particular number,

tither:a) Name the place where God put Adam and Eve to live.

b) State any two reasons why God created people.
i)
ii)
c) How did Adam and Eve disobey God?

Or =a) Name the place where Allah put Adam and Hawah to live.

b) State any two reasons why Allah created people.
i)
ii)
c) How did Adam and Hawah disobey Allah?

32.Either:a) Which angel delivered the good news to Virgin Mary about the birth of
Jesus Christ?

: b) State anyone way angels are important in Christianity.
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
