# Job ltsk_7da26a3c412645e79c3d5cc64cec0984-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 3 lesson(s) below of week 4 of the Christian Religious Education scheme for Primary Six 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P6: one 40-minute lesson: 3–6 sections; about 16–32 points; worked examples and exam-style points; 6–8 activities.

lessonId=lles_5ca97a41dd4a4da1bc842f3c9d6683b5: lesson 10, Tuesday, 1 period(s), 40 minutes.
  Unit: Christian Involvement in the World (theme: Christians on the way). Lesson: Christian voluntary organisations — Christian voluntary organisations.
  Objectives: Identify Christian voluntary organisations.

lessonId=lles_dcff9f2158bc41cab581ab57c4cdad40: lesson 11, Thursday, 1 period(s), 40 minutes.
  Unit: Christian Involvement in the World (theme: Christians on the way). Lesson: Role of Christian organisations — Role of Christian organisations.
  Objectives: Describe roles of Christian voluntary organisations.

lessonId=lles_4e7217eaf3b64e0289f96f873c5bf050: lesson 12, Friday, 1 period(s), 40 minutes.
  Unit: Christian Involvement in the World (theme: Christians on the way). Lesson: Week 4 review — Christian Involvement in the World.
  Objectives: Review this week's lessons: Christian voluntary organisations; Role of Christian organisations
  This is the FRIDAY REVIEW of this week's lessons (listed in the objectives). notes = a '### Summary' heading per lesson with its key points ('- ' points), then '### Exercise' with review questions taken from the passages. activities = those questions.

Write, using ONLY the passages below. Passages from "NCDC" documents are the official base for what to teach; NCDC lower-primary thematic curricula put every learning area in columns separated by " | ": use only the Christian Religious Education column.
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
<passage id="lchk_62622d06b00c4698b1f540bbf5ba9278" source="P.6 R.E scheme term 3" part="1">
GENERAL TOPICS GENERAL COMPETENCES
SUBJECT : RELIGIOUS EDUCATION i) Friends on the way i) ……………………………………...
CLASS: PRIMARY SIX ii) Christian involvement in the world. ii) ………………………………………
TERM: THREE iii) Happiness on the way and travel iii) ………………………………………
YEAR: 2016 iv) …………………………………… iv) …………………………………...……
WK
PD
Theme
Topic
Sub-topic
Competence
Content
Method
L/Skills ind.
Activities
T/L AID
REF
REM
Subject
Language
1
1
&
2
Christians on the way
Friends on the way
Qualities of true friends
States qualities if true friendship learnt from Jesus Christ
Reads, spells and writes selflessness, humility , servant hood
The qualities of a true friend
Selfleness
Humility
Servant hood
Understanding
Forgiving
Respect
True love
Patience
Loyalty
Guided discovery
Role play
Discussion
Sharing
Love
Friendship
Stating qualities of a true friendship
Reading
Board
New prim six curri pg 226 – 233
Mk standard R.E pg 103 - 105
2
1
How to distinguish between good and bad advice
States qualities of a good advice
Spells promote , respect , true
Qualities of good pieces of advice.
Should be Godly
Should promote respect for others.
Should promote peace.
Guided discovery
Role play
Discussion
Brain storming
Effective communication
Sharing
Critical thinking
Spelling, reading and writing.
Sharing
Board
Mk standard R.E 106 – 110
New prim six curr pg 226 - 233
2
Importance of true friends
The value of true friends.
Encourages
Doesn’t give up
Shows true love
Stands in hard times with you.
3
1
&
2
Christians on the way
Friends on the way
The need to co-operate in order to make the world a better place.
States importance of working together.
Mentions ways of co-operation.
Spells, reads and writes
Co-operation , leadership, obedience, voluntary
Importance of working together.
Possible ways of co-operation
Through good leadership
Through concern for the welfare of our people.
Being open
Through obedience to God
Through working hard
Guided discovery
Brain storming
Discussion
Effective communication
Sharing
Love
Stating importance of working together
Mentioning ways of working together
Board
New prim.six curr.pg 226 – 223
Mk stand.R.E bk 6 pg 118 - 119
4
1
&
2
Christian organization in developing the world
Mentions voluntary organization
Describes the roles of the voluntary organization
Spells , reads and writes , relief , fund , compassion , agency , development
Christian voluntary organizations.
Christian children’s fund (CCF)
World Vision International
Adventists Development Relief Agency (ADRA)
Compassion international
Mothers Union
YWCA
Catholic Women’s Guild
Scripture Union
Roles of Christian Voluntary Organization
Brain storming
Guided discovery
Discussion
Sharing
Appreciation
Critical thinking
Mentioning voluntary organizations.
Spelling , reading and writing
Board
New Pri. Six curr, pg 226 – 233
Mk stand. R.E bk 6 pg 121
5
1
Christians on the way
Contributions of science technology and education
States the meaning of technology.
States the effects of technology.
Spells and reads words e.g. Technology , communication
Technology
Application of technology
In transport and communication
In building
In farming
In food preservation
In entertainment
In power production.
Bad effects of technology.
Pollution of air and water
Increased employment
Destruction of culture
Increased death rate
Inquiry
Question and answer
Guided discovery
Sharing
Love
Reading
Stating the contributions of technology towards x-tian development
Board
Primary six curriculum.
2
National laws and rules
</passage>

<passage id="lchk_2256b09f74a442eca1dd4d536a3baa98" source="p.6 R.E Scheme term III 2019" part="3">
These promises are called vows.
They promise to love one another till death separates them.
These vows are made before a priest, pastor or reverend in the witness of their members and relatives.
Questions
What is marriage?
List down any four characteristics of a happy marriage
Identify one example of situations in marriage with which people need to be patient
How many the failure to produce children create as unhappy marriage.
Give any one example of a …….. duty
The bible
1 Cor. 13: 4---
MK
Standard Christian Religious education pupils’ book 6 page 117
2
3
Christians on the way
Christian’s involvement in the world
-Using our talents to improve the world
SUBJECT
The learner;
-Defines a talent
-Describe the talents he/she posseses
-Describes how he/ she can use the stated God given talents to develop the world.
-Reads the parable of the 3 servants / talents and draw important lessons.
LANGUAGE
The learner reads, pronounces, writes, spells and uses the e.g words correctly:-
-Talents
-Co-operation
-Science
-Technology
-Duties
-Responsibilities
-Biodiversity
-Contribution
-Communication
-Values
Talents are Natural gifts given to us by God they can also be referred to as special abilities
Examples of talents include
Singing
Playing musical instruments
Jumping (High)
Playing foot ball
Running fast
Dancing
How one can use his/ her talents
-Christians should use their talents to develop the world and to develop themselves.
-Jesus referred to us as salt and light of the world because of our talents and their usefulness in the development of the world we live in.
- Jesus encouraged his followers not to neglect their talents through the different parables he taught:
a) The parable of the three servants
Mt 25:14-27 (Read the story)
Lesson learnt
- All Christians should use their talents for the benefit of themselves and others
Every xtn. Will one day have to give an account of how he used his / her talents
-Those who will have used their talents properly will get rewards and those who will have failed will be punished.
How the above stated talents can benefit the world if used well.
-They are a source of -entertainment
- They send teaching or advisory messages to people
- They are a source of income for individuals who can get a livelihood
- They are a source of income for the government through taxation.
- Discussing about their own talents
- Bible reading on the parable of the 3 tenants
-The Bible
-Picture showing
Examples of related people in the world
MK
Bk 6
Pg
3
1
Christian on the way
Christian involvement in the world
The role of Christians in development
SUBJECTS
-Define the term voluntary work.
-Give examples of voluntary organizations in Uganda.
-Explains the role of Christian organizations in development
LANGUAGE
The learners reads, pronounces, writes, spells, and uses the following words correctly.
-Contribution
-Organizations
-Role
-Voluntary
-There are so many Christian organizations that offer free services to people/ communities some promote welfare of orphans, some help the government to fight poverty among people some promote good health, others drill bore holes for communities and provide safe water sources. Christian Organizations have helped to support street children, refugees the disabled.
-Most of the work is voluntary in nature it is done for free.
Examples of Christians voluntary organizations in Uganda and the roles they play
</passage>

<passage id="lchk_6af4f52db25643a8b54c687e3cd2a4fe" source="p.6 r.e lesson notes term III" part="5">
With which servant did the master get annoyed?
What lesson do we learn from the parable of the three servants?
DATE
CLASS
SUBJECT
NO OF PUPILS
TIME
THEME: CHRISTIANS ON THE WAY
SUB THEME: CHRISTIAN INVOLVEMENT IN THE WORLD
CONTENT: THE ROLE OF CHRISTIAN ORGANISATION IN DEVELOPING THE WORLD
Spelling practice
Services
Political affairs
Livelihood
Advisory
Religious
Fund
Relief
Voluntary
organization
New words to define
A company formed for a particular purpose
The act of causing something to grow / become larger / more advanced.
T
There are many Christian organization that offer free services to people / communities
Some promote the welfare of orphans .some help the government to fight poverty among people
Some promote good health others still drill boredom for communities
EXAMPLES OF CHRISTIAN’ VOLUNTARY ORGANSISATIONS IN UGANDA / THE ROLES THEY PLAY
CHRISTIAN CHILDREN’S FUND ; sponsors needy children in their education and provide health care to such children
WORLD VISION INTERNATIONAL: provide / support orphans promote the welfare of peasants, build schools and clinics and provide safe water sources.
ADVENTIST DEVELOPMENT RELEIF AGENCY (ADRA)
Builds and facilitates schools
Caters for people hit by disasters e.g earth quake e.t.c
COMPASSION INTERNATIONAL
Caters for orphans
Gives clothes and other necessities to the needy children
Pays school fees for ready children
YOUNG WOMEN’S CHRISTIAN ASSOCIATION (YWCA)
Provides education and sponsors students
Provides counseling services
MOTHER’S UNION
Promotes women’s projects for development
Offers counseling to the married women and those seeking marriage
CATHOLIC WOMEN’S GUILD – promotes women’s project
SCRIPTURE AND CHRISTIAN UNION OF UGANDA
Promotes the teaching of the word of God in schools and institutions
The above institutions promote
Health among communities
Care for the disadvantaged people
They provide services and items like food,clothers,medicine,shelter,opharnage centers e.t.c
Exercise
What does C.F stand for?
Give any one of world vision international
What is ADRA in full?
What is the role of Y.W.C.A
Why do we need Christian voluntary organization?
Mention any two Christian organization which help women only
DATE
CLASS
SUBJECT
NO OF PUPILS
TIME
THEME: Christians on the way
SUB THEME: Christian involvement in the world
CONTENT: THE ROLE OF SCIENCE AND TECHNOLOGY AND DUCATION TO THE DEVELOPMENT OF THE WORLD
Spelling practice
Involvement
Standards
Yields
Interferences
Invention
Skills
Words to define
Science – the study of the natural world based on facts learned through experiments and observation
Technology
Education – knowledge, skill, understanding you get from attending school.
Development
Invention - This refers to productive imagination
Technology is the practical way of using science to solve some of the day to day problems.
Technology and education have improved greatly on people’s standards of living
There are a number of scientific discoveries which have contributed to the development of the world.
Ways through which science and technology has led to development
Technology has improved the transport and communication through construction of better roads, speedy motor boats, aero planes to cover longer distances faster, electronic means of communication i.e emails, telephone, radios, television.
Technology has improved building today better buildings or houses are constructed due to modern technology
</passage>

<passage id="lchk_127f56d74e9f4b1099783d9ef777672d" source="NCDC P6 Set One Sept book – Religious Education" part="13">
The learner;
• describes the importance of friendship.
• explains how Jesus showed friendship to his apostles and other
people.
• outlines the qualities of a good friend.
• Lists the qualities of a marriage partner.
• explains how a friend should behave.

Topic 9: Christian Involvement
in the World | 11 Periods

Background
Christians should not leave world affairs to non-Christians alone. They
have a duty to participate in the affairs of the world at all times. This
includes religious, social, economic and political affairs. They thus have
to make a contribution to the world they live in. This in the end makes the
world a better place for people to live in. The role of science and technology
is discussed and how it has developed and affected the world. The topic
further brings out the role of Christian organisations in developing the
world.

It brings out the fact that the Christians should also fulfil their duties and
responsibilities in the community and country at large. The Christians
are also urged to be law abiding citizens.

Learning Outcome
The learner discovers events and circumstances where Christians have
contributed towards the development of the world and develops skills to
enable him/her become a better citizen.
Resources | Methods
• The Bible | • Dramatisation
• Pictures | • Pole play
• Textbooks | • Discussion
• Voter Education Manual | • Debate
Life Skills | Values
• Self-awareness | • Responsibility
• Effective communication | • Support
• Decision-making | • Love

National Curriculum Development Center

Subject | Language | Suggested
Content
Competences | Competences | Activities

The learner; | The learner
• describes the  reads, |  Our talents | • Discussing
talents he/she pronounces, | – Meaning of | about
writes, spells | talents. | talents.
possesses. | and uses the
following | – Using God- | • Bible
• uses God- | given talents
given talents  words correctly: | reading of
to improve the
to improve the – talents | world we live
texts which
world. | – co-operation | reflect
in - Mathew | talents.
– science
• explains | 25: 14-30.
– technology | • Debating.
the role of | – Using talents
Christian | – contribution
in cooperation | • Role playing
organisations | – duties | about God
with others - 1
in | – responsibility | Corinthians | given talents
development. | 3:5 – 10, | • Bible
• explains how | Genesis. 2:15 | reading and
science and | • The role of | discussions.
technology | Christians in
• Discussing
contributes to | development.
about
development | • The role | participating
of education. | of science, | in an
• describes a | technology, | electoral
good citizen. | and | process.
• relates | education in
• Role playing
Christianity | development
about good
to good | and Christian
citizenship.
citizenship | and the law.
like | Deuteronomy.
participating | 5: 16-21, Mark
in an election | 12: 13-17
process.
• mentions
qualities of a
good citizen.

Primary 6 Curriculum

Subject | Language | Suggested
Content
Competences | Competences | Activities

• Participating
in an electoral
process:
– voting
– rights and
freedoms of
voters
– duties of the
Electoral
Commission
• Demonstrating
good
citizenship

Guidance to the Teacher
• This topic is expected to cover 11 periods.
• Help the learners to identify their God-given talents by
mentioning them and demonstrating where it is applicable.
• Discuss with them the importance of talents and how they are
useful in developing the community.
</passage>

<passage id="lchk_1d61423169f3452f95af9dcaf32ccab4" source="NCDC P6 Set One Sept book – Religious Education" part="14">
• Guide them into realising the value of cooperation.
• The learners should point out the Christian organisations they
know and discuss their contribution to the communities in
which they operate.
• Debate about the role of science and technology in
development.
• Have class discussions on the reasons why they are expected as
Christians to obey rules and regulations.
• Discuss the rules and laws the learners have collected.
• Guide learners towards discovering the importance of obeying
laws as Christians.
• Help the learners develop an understanding that the Electoral
Commission performs a vital role in the world affairs.

National Curriculum Development Center

• In groups, the learners discuss the functions of the Electoral
Commission.
• Use the teacher’s resource book for voter education to get more
information.
• Devise methods which cater for learners with special needs

Suggested Competences for Assessment
The learner;
• identifies talents that can be used as a contribution to creating
a better world.
• explains the role of a Christian in developing the world.
• explains how science and technology contribute to the
development of the world.
• describes some aspects of a good citizen.

Topic 10: Happiness on the Way
to Arrival | 12 Periods

Background
This topic brings out the aspect of happiness and the different ways
in which we can achieve it. The topic emphasises the fact that a good
relationship with God is the most important source of happiness. Giving
and receiving are also presented as a source of happiness.

It further brings out to the learners the Biblical aspects and understanding
of the life hereafter and the concept of Heaven. The topic also discusses
suffering and the skills needed to endure and persevere in order to achieve
happiness.

Learning Outcome
The learner discovers Christian beliefs that are the source of happiness
and hope and develops a persevering spirit/attitude in her/his Christian
journey of faith.
Resources | Methods
• The Bible | • Discussion
• Textbooks | • Debate
• Guided discovery
• Sharing of experiences

Life Skills | Values
• Effective communication | • Appreciation
• Friendship formation | • Endurance
• Coping with stress
• Interpersonal
relationships

National Curriculum Development Center

Subject | Language | Suggested
Content
Competences | Competences | Activities
The learner; | The learner
• explains how | reads, | • Developing a | • Discussing
God is the | pronounces, | relationship with | about ways
writes, spells
source of | and uses the | God: | through
happiness. | following | – Happiness - | which God
• relates | words correctly: | meaning. Giving | brings
– happiness | happiness to
happiness | and receiving
and God. | – suffering | as a source of | men.
– endure | happiness - John | • Debating.
• describes
– heaven | 13: 14–14.
giving and | • Sharing of
– interpersonal  – Good
receiving as | experiences
a source of | – relationship | relationship | about cases
happiness. | with God as | where they
a source of | received
• explains the | happiness,
concepts | and became
Psalm 1: 1–3, | happy.
of life and | Psalm112:4-7
death. | • Life and death - | • Bible
• describes | John 11:1 – 44 | reading
what | of cases of
– The Biblical | happiness in
Christians | teaching about
believe about | the Bible.
death - 1
heaven. | Corinthians | • Group
• mentions | 15:55 – 57. | discussions
the cause of | about the
• Suffering: causes
suffering. | Biblical texts
and how to
read about
</passage>

<passage id="lchk_2fb7f3526b2948ab9b25f475235d0794" source="P.6 C.R.E TERM III LESSON NOTES, 2022" part="3">
e) They groom future leaders e.g. team captains.
f) They donate to the poor.
4. How can we develop talents among people?
8
i) Having regular practice.
ii) By identifying and training.
iii) Organizing competitions.
iv) By encouraging and rewarding good performance.
5. How do people benefit from their talents?
i) They get jobs.
ii) They get fame.
iii) They get friends.
iv) They get wealth.
v) They get exposure to foreign lands.
vi) They use talents to kill boredom.
The roles and cooperation of different people in making the world a
better place.
There is a need to cooperate and work together as a team in order to be
successful in any project.
Different ways we can cooperate in making the world a better place.
a. By working together as a team / collective responsibility.
b. By having proper care for God’s creation.
c. By ensuring peace and freedom for all people.
d. Through leaders being open and transparent.
e. Through concern and welfare of other people.
Why do we need to co-operate with each other?
a. It helps us to overcome challenges.
b. It builds strength (United we stand and divided we fall).
c. We get new ideas from other people.
The role of Christian organizations in developing the world
9
There are many Christian organizations in Uganda which serve people and some
of these include:-
I. Young Women’s Christian Association (YWCA).
II. The Bible Society.
III. World Vision International
IV. Mother’s Union
V. Christian Children’s Fund (C.C.F)
VI. Adventist Development Relief Agency (A.D.R.A)
VII. Inter Religious Council (IRC)
VIII . Uganda Joint Christian Council (U.J.C.C)
CHRISTIAN VOLUNTARY ORGANISATION IN UGANDA
1. What are voluntary organizations?
o These are groups of people who work willingly and without payment.
o These are organizations that do charity work.
o These are organizations that offer free services.
2. Give examples of voluntary organizations Uganda.
a) Mothers’ Union.
b) Fathers’ Union.
c) Adventist Development Relief Agency (ADRA)
d) World Vision International
f) Scripture Union.
Other Non-Government Organizations / Non-Religious organizations.
a) The AIDS Support Organization (TASO)
b) The Uganda Women’s Effort to Save Orphans (UWESO)
c) United Nations International Children’s Emergency Fund (UNICEF)
d) Kulika Uganda
e) World Food Programme (WFP)
10
f) World Health Organization (WHO).
g) Uganda Red Cross Society.
h) Cooperative for Assistance and Relief Everywhere (CARE).
3. State the roles of each of the following voluntary organizations in
Uganda.
Uganda Red Cross Society
a) Gives medicine to wounded and displaced people.
b) Facilitates the donation of blood.
c) Traces displaced people.
d) Provides food and clothing to displaced people.
e) Resettles people who are displaced during the war.
Babies’ homes / orphanages
a) Cater for infants without parents and who have been neglected.
b) They provide them with food, shelter, medical care and clothing.
Bible society
Provides the teaching and spread of the Word of God.
World Vision International
a) Builds and facilitates schools.
b) Caters for people hit by the disasters like earthquakes.
c) Provides safe water sources.
Compassion International
a) Caters for orphans.
b) Give clothes and other necessities to needy children.
c) Pays school fees for needy children.
Christian Children’s Fund (C.C.F)
a) Sponsors needy children in their education.
11
b) Also provides health care for such children.
Mothers’ Union
a) Gives counseling services to women with special problems.
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
