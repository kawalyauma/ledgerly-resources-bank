# Job ltsk_e8226b4415b04d02a7458a0e9aad1398-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 5 lesson(s) below of week 5 of the Social Studies scheme for Primary Four 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P4: one 40-minute lesson: 2–4 sections; about 12–24 points; meanings, examples and uses; 5–7 activities.

lessonId=lles_99b759036f1d4367bb22a107dd1e1d41: lesson 21, Monday, 1 period(s), 40 minutes.
  Unit: OUR LEADERS IN THE DISTRICT (theme: Living together in our district). Lesson: Responsibilities of district residents — Responsibilities of district residents.
  Objectives: Explain responsibilities in a district.

lessonId=lles_c37a88405d224f95b1ba9d77c77d4ccf: lesson 22, Tuesday, 1 period(s), 40 minutes.
  Unit: OUR LEADERS IN THE DISTRICT (theme: Living together in our district). Lesson: Responsibilities of district residents — Part B — Responsibilities of district residents.
  Objectives: Practise identifying and explaining responsibilities of district residents.
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points ('- ' points, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

lessonId=lles_5485662790874b70b5873378efd66cd3: lesson 23, Wednesday, 1 period(s), 40 minutes.
  Unit: OUR LEADERS IN THE DISTRICT (theme: Living together in our district). Lesson: Community leadership elections — Community leadership elections.
  Objectives: Describe how elections are used to choose leaders.

lessonId=lles_a506ac98c3a947ee857f66f2ce3b2481: lesson 24, Thursday, 1 period(s), 40 minutes.
  Unit: OUR LEADERS IN THE DISTRICT (theme: Living together in our district). Lesson: Community leadership elections — Part B — Community leadership elections.
  Objectives: Practise identifying and explaining community leadership elections.
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points ('- ' points, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

lessonId=lles_95c4ee21de8b494f80336d17ae393abe: lesson 25, Friday, 1 period(s), 40 minutes.
  Unit: OUR LEADERS IN THE DISTRICT (theme: Living together in our district). Lesson: District administrative structures — District administrative structures.
  Objectives: Identify political and civic administrative structures.

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
<passage id="lchk_806c25b3901545fc9f5f7aa6e76b5e29" source="P 4 Primary Four SST Scheme OF Work Teacher AC" part="6">
commercial centres.
Importance of social
activities.
- They keep different
families together.
- They promote
culture e.g. feeding,
dressing, language.
- Unite people.
- They promote
acceptable
behavior.
- Promote working
together.
- Strengthen family,
clan norms.
Factors contributing to
people’s way of life.
- Work
- Availability of food
- Mentioning the
importance of
social
activities.
- Naming factors
contributing to
people’s way of
life.
- Stating factors
contributing to
people’s way of
life.
- Defining
commercial
Page 17
- Security
- Education
- Diseases
- Un employment
- Poverty
- Trade
- Transport
- Communication
- Commercial
centres.
These are places where
most economic activities
take places.
Examples of commercial
centres.
- Big markets
- Banks
- Hospital schools
- Industries etc.
centres.
- Giving different
examples of
commercial
centres.
PRIMARY FOUR SOCIAL STUDIES SCHEME OF WORK TERM 3
WK PD THEME TOPIC COMPETENCES CONTENT ACTIVITIES T/L AIDS REF REM
1 1
&
5
OUR
LEADERS
IN THE
DISTRICT
DISTRICT
LEADERSHIP
 Learners defined
decentralisation.
 Define by – laws.
 Tell who heads a district both
civic and political.
 Give the types of leaders and
their examples.
 State the members that make
up the district council.
 Outline the different heads of
departments and their roles.
 Give the qualities of a good
leader.
 Outline ways people acquire
leadership.
 Mention the people’s
responsibilities in our district.
- Division of power
between the central
and local
government.
- By- laws: These
are laws made and
passed by the local
government.
- The political heads
is the chairperson
LCV.
- Civic head – is the
chief administrative
officer (C.A.O).
- Define terms.
- Give types of
leaders.
- Give the
members
that make
up the
district
council.
- Group leaders
in our
district.
- Describe and
draw the
political and
civic
administrati
ve
structures.
- A chart
showing the
a map of
your district
SST syllabus pg.
2
Fountain s.s.t Mk
ppls bk 4 pg. 2
Trs. SST bk. 4
Atlas.
Page 18
TYPES OF LEADERS.
- Appointed leaders.
- Elected leaders.
- Cultural leaders.
- Religious leaders.
- Voluntary leaders
(appointed by the
district service
commission)
Members that make up
the district local council
- Chair person.
- Sub-country
councilors.
- 2 youth councilors
- 2 councilors for the
disabled.
Different departments
and their roles.
- District chairperson
(LCV)
- District speaker.
- CEO
- DDE
- DVO
- DPC
- RDC
- DFO
Qualities of a good
leader.
- Ability
- Kindness.
- Approachable
- Tolerant
- Understanding
- Operative
- Confident
- Responsible
- Careful
How people acquire
leadership
- Role play L.C.I
meeting.
- Identify names
of leaders in
the district.
- Role playing
election
- Singing
patriotic
songs.
- Drawing
election
- Modeling of
ballot
papers.
- Demonstrate
campaignin
g by
prefects.
- Give qualities
of a good
leader.
- Give people’s
rights in a
district
- Suggesting
people’s
responsibiliti
es in the
district.
Page 19
- By appointment
- Through
inheritance
- By voluntarism
People’s rights in a
district
- Aright to food.
- A right to
education.
- Aright to security
- Aright to medical
care.
- Aright to privacy
- Aright to get
information
- A right to
movement
- Aright to
association
- Aright to work
- Aright to fair
judgment etc.
Responsibilities of
people in our district.
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
</passage>

<passage id="lchk_4f1813f648d140cd892a0f18ac07c8c5" source="Primary 4 Social Studies Scheme of Work, Term 3, 2022" part="1">
~s

IBANDA DISTRICT LOCAL GOVERNMENT
P.4 SOCIAL STUDIES SCHEMES OF WORK TERM THREE 2022

SUBTOPIC = [CONTENT COMPETENCES [METHODS LEARNING LIFE SKILLS AND VJINSTRUCTIONAL REFERENCE REMARI
[SUBJECT. LANGUAGE ACTIVITIES MATERILS I;
Types of leaders TheTear The learner Group discussioy .{dentifying types ¢.Cooperation __|.€ lection posters ;MK Standard SST
four district |.Political leaders Defines a leader |.pronounces and spells th Question and an|leaders in our disty .Classifying -Pictures of leaders In pug BK4 pg66
.Civic leaders: Identifies types of | related to theleadership |.Role play Giving examples of Respect books Primary Four SST
Religious leaders leaders district. political leaders |.Critlcal thinking CUrriculum pgi6
Cultural leaders :Glves example sof —_|.Constructs sentences using the a
.Voluntary leaders political leaders |words related to political leaders,
POLITICAL LEADERS ac:
Definition of a political leader.
Examples of political
leaders
a|LIVING TOGETHER LOCAL COUNCIL 2 Listing the titles given
IN OUR DISTRICT EXECUTIVE COMMITTEE MEMBERS. to executive committee .
~ | Roles@FEC E xecutive The learner; The learner; -Role play members. -Responsibility _|.Chalkboard Illustrations |MK Standard SST
F Intenance of sanitation .ldentifies duties of | ,pronounces, reads and |.Demonstration |,|déntifying the LC|,Appreciation _|Pictures in puplls'books |BK 4 pg67
Settling disputes played by each LC juses the words related chairpersons In th¢ Self-esteem Primary 4 calliculum
.Implementing government lexecutive memberS _|local council committee. areas, ™ pBiG
policies Names the executivé members a a :
-keeping peace and seurity lof LC 1. 6 .
F = promotion of development F 3 4
LIVING TOGETHER ,pomotion of food security $
IN i L
;RESIDENT DISTRICT COMMISSIO The learner; The learner; “Discussion idertifyin g the du|.critical thinking’ |.Resourceful person __ [Mk Standard SST bk 4
3 .\dentifiesaive duties ind spellsthe | Question and anjof the ROC In a dj.inquiry ” pe 68
|. Duties per formed lof the ROC'snd the DIS(words related to the dutl{.Dramatisation |.Locating the RDC! pattecys communication
DISO -Nameg the ROC of euytimRDC offices inourarea, —*
| Dutles ofDISO tra @istrict district.
THE DISTRICT CHAIRPERSON — |The learner; The learner; Inquiry |Mentloning the di.Honesty A chart showing.LC structures:
People who elect the chalrpersq.outlines the duties of |.reads,spells-and.pronour.lilustration of the chalrperson| Cooperation Cmprehensive sst
d fe " ,Dutles perfomed the LCV chairperson |the words related to the {Discision :Responsibility bk4 ps8
i THE STRUCTURE OF LCV Identifies the compositchalrperson LC v. MK Standard SST bk4
- Its composition of the LGW structure pp 70
—
CIVIC LEADERS IN OUR DISFAICT |The learner ; “|The learner; Group discussior/Listing examples o|.Self-awareness [A chart showing civic lead Comprehensive SST
k How they attain thelr positions _|./dentifles examples of | uses the words related tq.Demonstration |leaders In.our: critical thinking |structures, book 4 pg 59
4.The body that appoints them [civic leaders + |the topic in structures _|.Question and an|Naming the body t].Appreclation -MK Standard SST bk
| Examples of gic leaders |.names-the body that. |.pronounces and spells the leppoints civic leaders In ge M4 pg 70
3 lappoints civic leaders il words related to the topic Jour district,
district.
</passage>

<passage id="lchk_a6c1d3301a7743d3a21b117783ccf339" source="Primary Four Social Studies Schemes of Work, Terms 1–3" part="6">
DISTRICT Social activities
 Factors contributing to
people’s way of life.
 Outline the importance of
social activities.
 States factors contributing to
people’s way of life.
 Defining commercial centres.
 States examples of
commercial centres.
Importance of social
activities.
- They keep different
families together.
- They promote
culture e.g. feeding,
dressing, language.
- Unite people.
- They promote
acceptable
behavior.
- Promote working
together.
- Strengthen family,
clan norms.
Factors contributing to
people’s way of life.
- Work
- Availability of food
- Security
- Education
- Diseases
- Un employment
- Poverty
- Trade
- Transport
- Communication
- Commercial
centres.
These are places where
most economic activities
take places.
Examples of commercial
centres.
- Big markets
- Banks
- Hospital schools
- Industries etc.
- Mentioning the
importance of
social
activities.
- Naming factors
contributing to
people’s way of
life.
- Stating factors
contributing to
people’s way of
life.
- Defining
commercial
centres.
- Giving different
examples of
commercial
centres.
0754895241/0783298434 Page 17
TERM III
WK PD THEME TOPIC COMPETENCES CONTENT ACTIVITIES T/L AIDS REF REM
1 1
&
5
OUR
LEADERS
IN THE
DISTRICT
DISTRICT
LEADERSHIP
 Learners defined
decentralization.
 Define by – laws.
 Tell who heads a district both
civic and political.
 Give the types of leaders and
their examples.
 State the members that make
up the district council.
 Outline the different heads of
departments and their roles.
 Give the qualities of a good
leader.
 Outline ways people acquire
leadership.
 Mention the people’s
responsibilities in our district.
- Division of power
between the central
and local
government.
- By- laws: These
are laws made and
passed by the local
government.
- The political heads
is the chairperson
LCV.
- Civic head – is the
chief administrative
officer (C.A.O).
TYPES OF LEADERS.
- Appointed leaders.
- Elected leaders.
- Cultural leaders.
- Religious leaders.
- Voluntary leaders
(appointed by the
district service
commission)
Members that make up
the district local council
- Chair person.
- Sub-country
councilors.
- 2 youth councilors
- 2 councilors for the
disabled.
Different departments
and their roles.
- District chairperson
(LCV)
- Define terms.
- Give types of
leaders.
- Give the
members
that make
up the
district
council.
- Group leaders
in our
district.
- Describe and
draw the
political and
civic
administrati
ve
structures.
- Role play L.C.I
meeting.
- Identify names
of leaders in
the district.
- Role playing
election
- Singing
patriotic
songs.
- Drawing
election
- Modeling of
ballot
papers.
- Demonstrate
campaignin
g by
prefects.
- Give qualities
of a good
leader.
- Give people’s
- A chart
showing the
a map of
your district
s.s.t syllabus pg 2
Fountain s.s.t Mk
ppsbk 4 pg 2
rs.s.tbk 4 Atlas.
0754895241/0783298434 Page 18
- District speaker.
- CEO
- DDE
- DVO
- DPC
- RDC
- DFO
Qualities of a good
leader.
- Ability
- Kindness.
- Approachable
- Tolerant
- Understanding
- Operative
- Confident
- Responsible
- Careful
How people acquire
leadership
- By appointment
- Through
inheritance
- By voluntarism
People’s rights in a
district
- Aright to food.
- A right to
education.
- Aright to security
- Aright to medical
care.
- Aright to privacy
- Aright to get
information
- A right to
movement
- Aright to
association
- Aright to work
- Aright to fair
judgment etc.
Responsibilities of
people in our district.
rights in a
district
- Suggesting
</passage>

<passage id="lchk_ebd7903d943347949b1dbbda763df810" source="NCDC Primary Four Social Studies Syllabus Book" part="14">
National Curriculum Development Centre 2010 | 15 | 15




Subject Competence | Language Competence | Content | Suggested Activities
The Learner; |  Pronounces, reads, writes | Types of leaders in our |  Grouping leaders in our district.
 Identifies different | and practices structures | district. | Describing and drawing the
groups of leaders in | related to different groups | Political leaders: | political and civic administrative
the district | of leaders in the district. | LC1 – LC 5, RDC, | structures.
District Internal |  Role playing an L.C I meeting
Security Officer |  Identifying names of leaders in
(DISO) | our district.
 Civic leaders: |  Role playing election
CAO, District | procedures.
Health Officer, |  Singing patriotic songs.
District |  Drawing election posters.
Agricultural |  Modeling a ballot paper.
Officer, |  Demonstrating campaigning to
Magistrates, | be prefects.
District Police
Commander.
 Religious
Leaders: Bishops,
Priests,
Reverends,
Sheiks, Pastors
and Khadis.
 Voluntary leaders:
Scouts, Guides, All
leaders of NGOs.,
UWESO, TASO, The Red
Cross etc
 Describes how leaders |  | 
How leaders are
are chosen in the
chosen n Our district
district.
- By election
- By appointment
- Through inheritance.

16 | National Curriculum Development Centre 2010 | 16



Subject Competence | Language Competence | Content | Suggested Activities
- By volunteering
 Identifies qualities of a |  Pronounces, reads, writes | Qualities of a good leader |  Brainstorming on qualities of a good
good leader and roles | and practices structures | - Ability/able | leader.
of different leaders in | related to qualities of a | - Kindness |  Telling a story on how she helped
the district. | good leader | - Respectful | someone in a problem.
- Knowledgeable |  Discussing the roles of different
- Approachable | leaders.
- Responsible |  Role – play an L.C V Council meeting.
- Tolerant |  Listening to a resource person on
- Obedient
roles of cultural leaders, Civic and
- Careful
political
- Hardworking
- Cooperative |  Listing down roles of different
- Exemplary | leaders in the district.
- Confident |  Matching the leaders with their
correct roles.
 Identifies the rights and |  Pronounces, reads, writes |  Rights and |  Listing children’s rights.
responsibilities of the | and practices structures | responsibilities of people |  Identifying people who provide
people in our district | related to peoples rights | in our district: | services related to these rights.
and responsibilities. | Rights of the people in our |  Singing songs of appreciation to the
District. | people who provide these rights.
- Life, food, Education, |  Making posters of people who abuse
security | their rights and display their work in
- Right to medical care. | class and compound
 Making campaign against people
(ii) Responsibilities of | who abuse peoples’ rights in the
people in our | school and neighborhood.
district: |  Discussing in groups the
Obeying laws | responsibilities people do in their
Participating in | localities to provide the basic needs.
community work, Doing |  Reporting the discussed
Productive activities, | responsibilities to class
Caring for the sick,, |  Writing class rules for them to follow.
going to school.

National Curriculum Development Centre 2010 | 17 | 17



Subject Competence | Language Competence | Content | Suggested Activities
- Participating in making
laws.
- Maintaining proper
sanitation.
</passage>

<passage id="lchk_0c5ec1b888e3496a801febd087ddb64b" source="Primary 4 Social Studies Notes: Living Together in Our District" part="26">
Contact: 0754895241/0783298434
Email: tekule@tekartlearning.com
Website: www.tekartlearning.com 3) Introduction ceremony
4) Circumcision
5) Graduation party
6) Baptism party
7) Birthday party
Importance of social activities
✓ They promote unity
✓ They promote friendship
✓ They promote culture
✓ They promote development
✓ They promote love
Marriage
Marriage is the legal union between a man and a woman as husband and wife.
Types of marriage
1) Religious marriage
2) Cultural/traditional marriage
3) Civil marriage
Reasons why people marry
- To bear children
- To promote love
- To promote unity
CULTURE
Culture and customs and beliefs of people in a society
Examples of culture practices
✓ Naming children
✓ Circumcision
✓ Burial
✓ Dressing style
✓ Dancing style
✓ Types of food
✓ Initiation
✓ Marriage
Examples of tribes that circumcise
✓ Bagisu (male circumcision)
92
Contact: 0754895241/0783298434
Email: tekule@tekartlearning.com
Website: www.tekartlearning.com ✓ Bakonjo (male circumcision)
✓ Sabiny (female genital mutilation)
Importance of culture
✓ It promotes unity
✓ It promotes identify
✓ It promotes good morals
✓ It promotes hard work
TERM THREE
LIVING TOGETHER IN OUR DISTRICT
OUR LEADERS IN THE DISTRICT
What is leadership?
Leadership is the way of guiding and directing other people
93
Contact: 0754895241/0783298434
Email: tekule@tekartlearning.com
Website: www.tekartlearning.com
Who is a leader?
A leader is a person who guides and directs others.
Qualities of a good leader
- Knowledgeable - responsible
- Tolerant - obedient
- Approachable - exemplary
- Cooperative - confident
- Hardworking - kind etc.
Types of leaders in our district
i) Political leaders
ii) Civic leaders
iii) Traditional leaders
iv) Religious leaders
v) Voluntary leaders
How leaders are chosen in our district
i) Through elections
ii) Through appointment
iii) Through inheritance
iv) Through volunteering
Political leaders
Political leaders are people who are elected or appointed to promote good
governance.
Examples of political leaders in our district
- Resident district commissioner (RDC)
- The District Internal Security Officer (DISO)
- Gombolola Internal Security Officer (GISO)
- Local Council Committee members
Local council
94
Contact: 0754895241/0783298434
Email: tekule@tekartlearning.com
Website: www.tekartlearning.com 1. Write LC in full - Local Council
2. Local council in Uganda are under the ministry of local government
3. The current minister of local government in Uganda (2015) Hon. Adolf
Mwesige
4. Local councils begin from LC I to LC V.
5. This is the lowest unit of local councils
6. Local council I is made up of 10 members.
Members of local council I and their duties
1. Chairperson
- Heads local council I executive committee
- Chairs all committee and council meetings
- Signs official documents and gives recommendations
- Supervises and implements all government programmes at village level
2. Vice chairperson
- Assist the chairperson in all his/her duties
- In charge of children welfare (affairs)
3. General secretary
i) Records all the minutes of council meetings
ii) Keeps official records
iii) Calls the executive and council meetings
4. Secretary for finance
- He /she is a treasurer of the council.
5. Secretary for defense
- Maintain peace and security in the area
6. Secretary for information, education and mobilization
- Passes on all the information needed by the people.
7. Secretary for youth
- Mobilizes youth to take part in development.
</passage>

<passage id="lchk_ff3b51efe44c4cfe8922d9a49d70971f" source="P 4 SST Lesson Notes Term III" part="7">
 Leader
 Administration
 Decentralization
 Disability
CONTENT: LEADERS
A leader is a person who manages and controls something/ person given authority to control / direct
others.
Administration is the act of managing and controlling an organization.
Decentralization is the transfer of power from central government to local government.
Types of leaders in our district
 Political leaders
 These are leaders of areas.
Examples of leaders
 LCI – LC5
 RDC – Resident District Commissioner
 LC – Local Council
Local Council V system
 The district council is made up of the following
 Chair person
 Councilors elected to represent district sub-county / divisions and towns
 Two councilors elected to represent the youth
 Two councilors with disabilities
The Local Council Structure
 LCV – District
 LC IV – County/ Municipality
 LC III – Sub – County / division
 LC II – Parish Executive
 LC I – Village executive
Exercise
8. Who is a leader?
9. Mention any two types of leaders.
10. Give any three examples of political leaders
11. State the political heads of the following areas
a. Country
b. District
c. Country
12. How are leaders important in a community?
13. How do civic leaders came into power?
14. Write LC in full.
Date Class Subject No. of pupils Time
P.4
TOPIC: Leaders in our district
SUB –TOPIC: Members of the LC Executive
INTRODUCTION: The lesson will be introduced by
COMPETENCES: Learners should be able to read, write, and spell correctly.
 Resident
 Chairperson
 Commissioner
 Disabilities
 Finance
CONTENT: MEMBERS OF LC EXECUTIVE
Chairperson – He chairs meetings
Vice chairperson – Helps the chairperson
He is in charge of children
General Secretary – Records minutes
Secretary for defence – Responsible for security matters
Secretary for finance – In charge of money
Secretary for information – In charge of delivering messages / mobilization
Secretary for production and environment – To care for the environment
Secretary for youth – Responsible for youth affairs.
Secretary for women affairs – Responsible for women
Secretary for disabilities – Responsible for the disabled
There are ten members who make the LCI executive
RDC
RDC in full is Resident District Commissioner
Roles of the RDC
 He heads a district.
 He is appointed by the president
 He advises the chairperson.
 He carries out any other function assigned by the president.
CIVIL LEADERS
Civil leaders are
Example of civil leaders
 DEO
 DFO
Exercise
7. Write LC in full.
8. How many members make up LC committee?
9. Who is responsible for children affairs in LC
10. Write RDC in full.
11. Outline any three roles of RDC in a district.
12. Mention any one role of the CAO in a district.
Date Class Subject No. of pupils Time
P.4
TOPIC: Leaders in our district
SUB –TOPIC: The duties of the district leaders
INTRODUCTION:
COMPETENCES: Learners should be able to read, write, and spell correctly.
 Co-ordinates
 Marriage
 Agriculture
 Commander
CONTENT: Duties of the District leaders
District chairperson
 He is the political head of the district.
 He is directly elected by adults.
Roles of a chairperson
 He monitors the general administration of the district.
 He co-ordinates the activities of the local government.
 He supervise the work of all other officers in the district.
Chief Administrative Officer (CAO)
 He is the chief accounting officer of the district.
Duties of CAO
 He is the highest civil servant in the district.
</passage>

<passage id="lchk_0b5f3048fe934b8c8fc3e9b936a54917" source="Sipro P4 Beginning Of Term 3 By Kalulu Brian 0755518221" part="1">
a

|

I

| SUBJECT : SOCIAL STUDIES WITH RELIGIOUS EDUCATION
| icLASS : PRIMARY FOUR

| IQURATION : 2 hours 15 minutes

READ THE FOLLOWING INSTRUCTIONS
CAREFULLY:

_ This paper has two sections: A and B.
Section A has 40 questions (40 Marks).

_ Section B has 15 questions (60 Marks).

_ Attempt ail questions in both sections. All
answers to both sections A and B must be
written in the spaces provided.

All answers must be written in blue or
black ball point pens or ink. Only diagrams
and graph work must be done in pencil.

_ Unnecessary alteration of work will lead to
loss of marks.

. Any han¢writing that cannot be easily read
may lead to loss of marks.

_ Do not fil’ anything in the boxes indicated:

“FOR EXAMINER’S USE ONLY”

Please turn over

ITHE §|PRO BEGINNING OF TERM III EXAMINATIONS - 2023!

'
1
!
1
i]
1
1
1
1
\ 1
1
1
1
{
1
1

eer ne ee er ee : “a 7 —

'
i]
1
i)
1
i)
'
'
i)
'
i)
4
t
1
i
4
i
t


OCU TVs mark eaci!.
Questions 1 to 40 carly one is all about.

the map
“1. Name the element of a map that tells what

— e identified.
2. Give any one way parents help their children to b :

d.
where meals are prepare

3. Write the important place at school

in their homes.
4. Give any one way people can control trespass in th

; i W.
5. Mention the feature represented in the diagram belo
NUN 73

6. Why do people rear cows in their homes?

7. Mention any one group of people who care for patients in the hospital.

8. State any one reason why deforestation is bad.

9. How is a drum useful in church?

10. Who is the political head of a district?

—_.11.How is a barometer useful at a weather station?

12 State any one importance of lakes and rivers to people.

13. Write any one member found in an extended family.

14. How areflowers important to people?

15. Give any one way people care for roads.

16. Mention any one type of holidays.

17. State any one local way of locating places. -

18. Give any one use of a cupboard in a home. z

19. Write any one example of fish caught from wetlands,

- ————
EN eS ervices Tel: 0414668050/ 0755-274911/077¢.;

Kh) op SOCIAL STUDIES WITH RELIGIOUS EDUCATION aeG NING OF Toa

MM 2023


20. Name any one place where people get food.

21. Mention the member of Local Council | committee in charge of sanitation.

22. Give any one way people use a house.

23. State any one reason why rural areas have few people.

24.Name any one item needed to set up a project.

25. How does a school signpost help people in an area?

26. Mention any one modern method of preserving fish in Uganda.

--27.State any one danger of insecurity at home.

28. Give one way people of long ago used shadows.

29. Name any one group of people.who help school children to cross busy roads.

30, Draw a map of a table in the space below.

31. How de people benefit from vegetation?

32. Name any one buiiding material got from a quarry.

33. Give any one way people choose leaders in the community.

- 525% Fxonatonal Services % Sa On asos0se OTSSaTASTIOTIET AT $
7S Avie STUDIES WITH RELIGIOUS EDUCATION BEGINNING OF TERM ttt - 2023 cs a

b=) CamScanner

at gcnool.
ated at 6
34. State any one way friendship can be prom

re rennnennnnnean ive in , valley’ me
35. Write any one problem faced by people wiv I

ristian OR Islarn-
marks will be
cular number.

— ch
in each of the questions 36 to 40, answer EITHER a ay
question but not both questions on the same num arth
awarded to a pupil who attempts both questions inaP
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
