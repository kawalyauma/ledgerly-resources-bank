# Job ltsk_e060fdfce508402eaed4da760d9c140f-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 3 lesson(s) below of week 3 of the Christian Religious Education scheme for Primary Six 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P6: one 40-minute lesson: 3–6 sections; about 16–32 points; worked examples and exam-style points; 6–8 activities.

lessonId=lles_57098df4ab9c415792163a76db374e02: lesson 7, Tuesday, 1 period(s), 40 minutes.
  Unit: Christian Involvement in the World (theme: Christians on the way). Lesson: Importance of working together — Importance of working together.
  Objectives: Explain the importance of cooperation.

lessonId=lles_c1a7e553104f493db056ef00f73f924e: lesson 8, Thursday, 1 period(s), 40 minutes.
  Unit: Christian Involvement in the World (theme: Christians on the way). Lesson: Ways of cooperation — Ways of cooperation.
  Objectives: Describe possible ways of cooperation.

lessonId=lles_6a378a58b6be49bd903c7fc90ec01b11: lesson 9, Friday, 1 period(s), 40 minutes.
  Unit: Christian Involvement in the World (theme: Christians on the way). Lesson: Week 3 review — Christian Involvement in the World.
  Objectives: Review this week's lessons: Importance of working together; Ways of cooperation
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

<passage id="lchk_48579250e06e49c3945066f2fdf59bf0" source="P.6 CRE NOTES TERM 3" part="2">
i) It recognizes marriage
ii) It creates a bond between the family of the bride groom and the bride.
iii) It is a way of thanking the parents of the bride for having kept their daughter.
Biblical teaching on marriage (1 Cori 7:1-16)
i) It encourages monogamy
ii) A man should fulfill his duty as a husband and a woman should fulfill her duties as
wife.
iii) A husband is a master to his wife’s body
Common marriage problems
i) Quarrels
ii) Fights
iii) Lack of respect
iv) Neglect of children
v) Lack of trust etc
Lesson 1: wk 2
Subtheme: Christian organization in development
Cooperation
Cooperation means working together to achieve a desired goal
Possible ways of cooperation
i) Through good leadership
ii) Through democratic laws and rules
iii) Through concern of welfare of other people
iv) Through working hard
v) Through provision of freedom and security
Voluntary organization
www.freshteacheruganda.com For more lesson notes, please visit
These are organizations that offer free services to people
Importance of voluntary organization
i) It promotes the welfare of vulnerable people
ii) They help to fight poverty
iii) They help to drill bore holes and provides water sources
iv) They offer guidance and counseling services
Examples of Christian organizations
Organization Function /role
- Christian children’s’
fund (CCF)
- Sponsors needy children in education
- Provides health care for needy children
- World vision
international
- Supports orphans
- Promotes welfare of the peasants
- Builds schools, clinic and safe water sources
- Adventist development
relief agency (ADRA)
- Builds and facilitates schools
- Helps people affected y diseases e.g. earth quakes
- Builds schools, clinics and provides water sources
- Compassion
international
- Caters for orphans gives clothes and other necessities to
the needy children
- YMC /YWCA - Provides education, counseling and sponsorships to
students
- Mothers union - Promotes women’s projects
- Offers counseling to married women and those seeking for
marriage
- Catholic women’s guild - Promotes women’s projects
- Scripture and Christian
union
- Promotes the teaching of the word of God in schools and
institutions
Lesson 2 and 3 wk 2
Roles of science teaching lody and education in development
Science
This is the study of physical or world of material things and natural environment
Technology
This is the making and uses of tools and machines to do work
Education
Roles of science in development
- Discovery of medicine to cure diseases
www.freshteacheruganda.com For more lesson notes, please visit
- Knowledge of how the body function
- Control and prevention of killer epidemics
- Better nutrition
- Improvement of agriculture
- Control and better care of the natural environment
Roles of technology
- Improve on transport
- Improve communication
- Discover the sources of power to run industries
- Improve on medical services
- Build complicated infrastructure
- Invent recreation facilities
- Promotes peace and security
Disadvantage of technology
- It causes air and water pollution
- It increases the rate of unemployment
- Interferes with our culture
- Increases high rate of deaths
Roles of education
- Acquisition of knowledge
- Promotes literacy
- Learning of knew language
- Learning of knew faith e.g. Christianity , Islam and etc
Importance of laws in society
- Guide people how to treat others
- It makes people fear crime
- Guides leaders on how to govern their people
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

<passage id="lchk_b9d0ddbf1787408da1f2d108c6cdca35" source="All P 4 To P 7 Religious Education Notes All Terms Copy" part="24">
In bad and good times, poverty and riches, sickness and healthy, only death that will
separate us
What the couple does in the church
i) Vows
ii) Signing marriage certificates
iii) Exchange of rings
Types of marriages
i) Religious marriage
ii) Customary marriage
iii) Civil marriage
Religious marriage
This is a type of marriage officiated by a religious leader
www.freshteacheruganda.com For more lesson notes, please visit
Customary marriage
This is a type of marriage officiated by both the parents of the bride and the bride groom
Civil marriage
This is a type of marriage officiated by government official like CAO
Bride price /dowry
This is the money and property in some societies that the bride groom must pay to the
bride’s family.
i) It recognizes marriage
ii) It creates a bond between the family of the bride groom and the bride.
iii) It is a way of thanking the parents of the bride for having kept their daughter.
Biblical teaching on marriage (1 Cori 7:1-16)
i) It encourages monogamy
ii) A man should fulfill his duty as a husband and a woman should fulfill her duties as
wife.
iii) A husband is a master to his wife’s body
Common marriage problems
i) Quarrels
ii) Fights
iii) Lack of respect
iv) Neglect of children
v) Lack of trust etc
Lesson 1: wk 2
Subtheme: Christian organization in development
Cooperation
Cooperation means working together to achieve a desired goal
Possible ways of cooperation
i) Through good leadership
ii) Through democratic laws and rules
iii) Through concern of welfare of other people
iv) Through working hard
v) Through provision of freedom and security
Voluntary organization
www.freshteacheruganda.com For more lesson notes, please visit
These are organizations that offer free services to people
Importance of voluntary organization
i) It promotes the welfare of vulnerable people
ii) They help to fight poverty
iii) They help to drill bore holes and provides water sources
iv) They offer guidance and counseling services
Examples of Christian organizations
Organization Function /role
- Christian children’s’
fund (CCF)
- Sponsors needy children in education
- Provides health care for needy children
- World vision
international
- Supports orphans
- Promotes welfare of the peasants
- Builds schools, clinic and safe water sources
- Adventist development
relief agency (ADRA)
- Builds and facilitates schools
- Helps people affected y diseases e.g. earth quakes
- Builds schools, clinics and provides water sources
- Compassion
international
- Caters for orphans gives clothes and other necessities to
the needy children
- YMC /YWCA - Provides education, counseling and sponsorships to
students
- Mothers union - Promotes women’s projects
- Offers counseling to married women and those seeking for
marriage
- Catholic women’s guild - Promotes women’s projects
- Scripture and Christian
union
- Promotes the teaching of the word of God in schools and
institutions
Lesson 2 and 3 wk 2
Roles of science teaching lody and education in development
Science
This is the study of physical or world of material things and natural environment
Technology
This is the making and uses of tools and machines to do work
Education
Roles of science in development
- Discovery of medicine to cure diseases
www.freshteacheruganda.com For more lesson notes, please visit
- Knowledge of how the body function
- Control and prevention of killer epidemics
- Better nutrition
- Improvement of agriculture
- Control and better care of the natural environment
</passage>

<passage id="lchk_72408bf80d91438bbf3bb3f312247c94" source="CRE NOTES & SCHEMES P.6" part="16">
Qualities of a good friend
Honest
Respectful
Trustworthy
Peaceful
Generous
Humble
Loving
Kind
Faithfulness
How Jesus expressed His love to mankind?
He revealed to His disciples the secrets of the kingdom of heaven
He was merciful to sinners
He was considerate
He had compassion and fed the hungry
He consoled the sorrowful Mary and Martha
He called children and showed them love
He taught His disciples the skills of love
Lesson 2 Wk 1
Advice
This is an opinion or suggestion about what somebody should do in a particular situation
Importance of advice (Sam 2:12)
May save someone from danger
Promotes peace and harmony
It promotes unity
It promotes friendship
Encourages development (2 Sam 1:12) difficult mission of prophet Nathan)
Characteristics of bad advice
It encourages evil
It encourages biasness
It is dishonest
It is not corrective
Crisis and how friends offer support in times of crisis
Meaning of crisis
Crisis is a time of trouble in which a quick solution should be given (Proverb 17:17-18)
A friend is always a friend at all times in happiness or in sorrow.
Lesson 3: wk 1
Marriage
Meaning of marriage
Marriage is a legal love union between man and a woman as a husband and wife
Qualities of a good marriage partner according to the Christian teaching
Age
Character
Dignity
Education
Family background
Godliness
HIV/AIDS free
Status
Reasons why people marry
To have children
For companionship
To express love
For sexual desires
For security
For prestige
Signs of marriage
Mutual love
Patience
Trust
Openness
Faith fullness
Bearing children
Fulfillment of marital duties
Showing sympathy to each other
Marriage as a social institution
It is the society concern because it involves all members of the community such as wedding preparations, witnessing the marriage ceremonies.
It unites different families, clans, tribes and races
Marriage vows
In bad and good times, poverty and riches, sickness and healthy, only death that will separate us
What the couple does in the church
Vows
Signing marriage certificates
Exchange of rings
Types of marriages
Religious marriage
Customary marriage
Civil marriage
Religious marriage
This is a type of marriage officiated by a religious leader
Customary marriage
This is a type of marriage officiated by both the parents of the bride and the bride groom
Civil marriage
This is a type of marriage officiated by government official like CAO
Bride price /dowry
This is the money and property in some societies that the bride groom must pay to the bride’s family.
It recognizes marriage
It creates a bond between the family of the bride groom and the bride.
It is a way of thanking the parents of the bride for having kept their daughter.
Biblical teaching on marriage (1 Cori 7:1-16)
It encourages monogamy
A man should fulfill his duty as a husband and a woman should fulfill her duties as wife.
A husband is a master to his wife’s body
Common marriage problems
Quarrels
Fights
Lack of respect
Neglect of children
Lack of trust etc
Lesson 1: wk 2
Subtheme: Christian organization in development
Cooperation
Cooperation means working together to achieve a desired goal
Possible ways of cooperation
Through good leadership
Through democratic laws and rules
Through concern of welfare of other people
Through working hard
Through provision of freedom and security
Voluntary organization
These are organizations that offer free services to people
Importance of voluntary organization
It promotes the welfare of vulnerable people
</passage>

<passage id="lchk_3c9035cd159b4d149db8993f7019f1e8" source="p.6 R.E Scheme term III 2019" part="4">
-Children’s fund (CF)– sponsors needy children in their education and provides health care for such children
-World vision international – supports orphans, promotes the welfare of the peasants, builds schools, clinics and provides safe water sources.
-Adventist development relief agency (ADRA) – Builds and facilitates
Schools, cater for people hit by disasters eg. Earthquakes etc others
Others include
Compassion international
Y WCA
Mother’s union
Catholic women’s guild
Scripture union Uganda etc
Identifying and explaining
some Christian organization and the impact these have made on our local communities
A chart showing a t8able of xtn organizations and their work
MK
Pupil’s
Bk 6
Pg
121 and
122
3
2
Christians on the way
Christians involvement in the world
The role of science Technology and Education to the development of the world
SUBJECT
-Defines science and Technology
-Defines Education
-Explains how Science and Technology contributes to development of Education
LANGUAGE
The leaner reads, spells, pronounces the following words correctly
-Technology
-Science
-Education
-Development
DEFINITION
Technology is the practical way of using science to solve some of the day to day problems
-Technology has improved people’s standards of living greatly in uses equipment, machinery and tools to make it
easier in many ways
Ways through which science and technology has led to development
- Technology has improved transport and communication through construction of better roads, speedy motorboats, aeroplanes to cover long distances faster etc
-Technology has improved on building- today better building/ houses are early constructed due to modern technology
-Technology has improved farming. It has led to an increase in food productions due to better farming methods and tools used, use of fertilizers etc.
-Technology has improved Education through easy publication of books, typing and printing out materials etc.
-It has improved power production
-It has improved entertainment etc.
Effects of technology on development
-Much as modern technology is good, it has bad effects too as seen below
- It has caused Air and water pollution these are effects from the machines used in industries, motor vehicle exhausts, releasing poisonous gasses into man’s environment
-It has increased the rate of unemployment . Machines do work at a very high speed which doesn’t necessitate use of human being who slow production hence high rates of unemployment
-A lot of cultural interferences have been infiltrated through movies watched by people bringing in a lot of different cultures from different parts of the world.
-Increased death rates-through regular accidents from the transport industry, fire or electric accidents, wars from use of modern weapons etc.
Exercise
What is the meaning of the Term “Technology”?
Explain how technology has improved the way of construction.
How do farmers benefit from existing technology?
What is the Advantage of preserving food?
Discussing the different ways science and technology has led to development in different sectors ie Education Health Transport etc.
MK
R.E
Bk 6
Pg
3
3
Christians on the way
Christians involvement in the world
Christians and the law
Deut 5:16-21
Mk 12:13-17
SUBJECTS
-Describes a good citizen
-Relates Christianity to good citizenship like participating in an election process
-Mentions qualities of a good citizen
LANGUAGE
-Citizenship
-Citizen
-Electoral
-Election
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
