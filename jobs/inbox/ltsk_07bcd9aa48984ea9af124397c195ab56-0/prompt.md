# Job ltsk_07bcd9aa48984ea9af124397c195ab56-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 3 lesson(s) below of week 1 of the Christian Religious Education scheme for Primary Six 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P6: one 40-minute lesson: 3–6 sections; about 16–32 points; worked examples and exam-style points; 6–8 activities.

lessonId=lles_295d0ae4699b4d04bfbdb212b91bad90: lesson 1, Tuesday, 1 period(s), 40 minutes.
  Unit: Friends on the Way (theme: Christians on the way). Lesson: Meaning and importance of friendship — Meaning and importance of friendship.
  Objectives: Explain the meaning and importance of friendship.

lessonId=lles_e724a765760b4e309f617c1fc029f218: lesson 2, Thursday, 1 period(s), 40 minutes.
  Unit: Friends on the Way (theme: Christians on the way). Lesson: Qualities of true friends — Qualities of true friends.
  Objectives: Identify qualities of true friends.

lessonId=lles_511ff109100642efb2d175ad244085b3: lesson 3, Friday, 1 period(s), 40 minutes.
  Unit: Friends on the Way (theme: Christians on the way). Lesson: Week 1 review — Friends on the Way.
  Objectives: Review this week's lessons: Meaning and importance of friendship; Qualities of true friends
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

<passage id="lchk_352756f3359c4065bddf3735cad81ad3" source="p.6 R.E Scheme term III 2019" part="1">
P.6 R.E SCHEME OF WORK TERM THREE 2019
WK
PD
THEME
SUB-THEME
UNIT
COMPETENCES
CONTENT
LEARNER’S ACTIVITIES
T/L AIDS
REF
RE
1
1
Christians on the way
Friends on the way
Friendship
Meaning and importance of friendship
SUBJECTS
The learner:-
-Explains the meaning of friendship
-Describes the importance of friendship
LANGUAGE
The learner
reads, pronounces, writes, spells and uses the following words correctly
-Friend
-Friendship
-Relate
-Relationship
-Advice
-Crisis
-Marriage
WHO IS A FRIEND?
A friend is a person with whom you relate freely.
He/she is a person you can tell about your feelings and secrets.
Importance of friendship
Friends give us good advice and encouragement
Friends provide us with practical support.
How Jesus showed true friendship to his apostles and other people.
Jesus’ friendship was selfless he spent much time serving others
He also died for our sins.
Jesus spent most of his time with the outcasts in society eg. the sick, blind/ disabled
Humility – Jesus had a lot of humility- Jesus was humble and respected other people beyond himself
Servant hood – Jesus’ life was an example of servant hood
Group work discussion about the meaning of friendship
Bible reading about Jonathan and David Isam : 20: 1 –ff.
The Bible
MK.R.E
Bk.6
Pg 103
109
1
2
Christians on the way
Friends on the way
Qualities of a good friend
SUBJECT
The learner;
-Explains Jesus’ example of friendship (John, 5:12-15)
-Describes from the gospel how Jesus showed friendship to his apostles and other people.
-Describe Jesus’ qualities as a good friend
LANGUAGE
The learner
reads, pronounces, writes, spells and uses the following words correctly
- Friend
- Friendship
- Relate
- Relationship
- Advice
- Crisis
-Marriage
Jesus’ example of friendship
-Jesus commanded us to love one another as he loved us.
-He used the His own example of dying for us on the cross “Creator love has no one than this, that he lay down his life for his friends”
-If we act as Jesus did he does not call us servants but friends for he teaches us the will of his father.
Qualities of a Jesus as a good friend
-Selflessness- the act of wanting to please others more than yourself.
Jesus gave his life for us (John 15:13)
-Humility refers to humbles when you are humble, you cannot start to think that you are more important than others. You treat others the some way you want them to treat you.
-Servant hood – a good friend should have a spirit of servant hood.
Jesus always served others and wanted to please his father in heaven
-Understanding
This is a friend who is not quick to judge other people’s mistakes but to them listens first.
Jesus had many people provoke him with questions but he answered back with understanding he never intended to annoy anyone
Forgiving
True love
Mutual respect
Patience and tolerance
Loyalty, openness and trust
-Bible reading John 15,12-15.
-Discussions about qualities of a good friend
-Sharing experiences when they were good or when someone was good to them.
The Bible
MK.RE
Pg
103.104,105
1
3
Christians on the way
Friends on
the way
How to distinguish between good and bad advice
Subject
The learner;
Explains the importance of advice
Distinguishes between good and bad advice in friendship
Give examples of good advice and bad advice.
Identifies qualities
States the importance of advice
LANGUAGE
-learners should be able to read, pronounce and use the following words in sentences.
-Advice
-Godly
-Marriage
-Respect
-Mutual love
-Companionship
ADVICE
</passage>

<passage id="lchk_c88531d4f76242c99535794efb92e708" source="All P 4 To P 7 Religious Education Notes All Terms Copy" part="28">
- Avoid desires of the flesh
- Read the word of God often
- Imitate Jesus Christ in His way of life while He was on earth
- Pray all the time
CHRISTIAN RELIGIOUS EDUCATION
TOPICAL QUESTIONS SET 1
www.freshteacheruganda.com For more lesson notes, please visit
FRIENDS ON THE WAY: TERM III
1 (a) Name the greatest commandment Jesus gave to his followers.
(b) How can people know that Christians are followers of Jesus Christ?
2 (a) In which two ways did Jesus show his love to man-kind.
(b) How useful are pieces of advice given to us by our elders?
3 (a) Give any two characteristics of bad advice
(b) Identify any two groups of people that need guidance and counseling.
4 State any two qualities of a good marriage partner according to Christian teaching
5 Which type of marriage is practiced in the church?
6 Identify any two problems facing families today
7 How useful is a stable peaceful family to children?
8 Identify any two causes of street children today.
9 name any two Christian organizations that cater for the needs of people in our
community.
1o why do Christians give offertories
www.freshteacheruganda.com For more lesson notes, please visit
CHRISTIAN RELIGIOUS EDUCATION
TOPICAL QUESTION SET 2 TERM III
1. (a) What does the word happiness mean?
(b) In which two ways can man achieve happiness?
2. (a) Give any two benefits of sharing and giving
(b)Why are some people in our community selfish?
3. What is the biblical teaching on life and death?
4. What are the values of suffering (Give two)
5. What does the Bible teach about heaven?
6. Which religion was in Africa before the coming of Europeans?
7. Name any three religions in Uganda.
8. What is the meaning of death in African tradition?
9. Name three causes of death in traditional Africa beliefs
1o. State any three causes of death today
www.freshteacheruganda.com For more lesson notes, please visit
WK PD S/THEME CONTENT SUBJECT
COMPETENCES
LANGUAGE
COMPETENCES
METHODS ACTIVITIES SKILLS AND
VALUES
LEARNING
AIDS
REF REM
1 1 Friends on
the way
Friendship
- Meaning
- Importance
- Jesus example of
friendship
- John 15:12-15
- Qualities of a good
friend
- Jesus’ friendship
from the gospel to
the apostles and
other people
The learner:-
- Explains the
meaning of
friendship
- Identifies the
importance of
friendship
- Explains Jesus’’
example of
friendship
- Points our qualities
of a good friend.
- Describes Jesus’
friendship
according to the
gospel
The learner:-
- Pronounces, spells
and uses words
correctly
- Generous
- Friendship
- relate
- guided
- discovery
- brainstorming
- demonstration
- role play
- guided discussion
- Bible reading
- Discussion
- Role playing
Skills
- Self esteem
- Self awareness
- Creative thinking
Values
- Awareness
- Appreciation
- Love
- The holy
Bible
- Text books
The holy Bible
John 15:12-15
Fountain
CRE
128-133.
2 Importance of advice
- Characteristics of
bad advise
- Crisis and how
friends offer help
in time of crisis
Proverbs 17:17-18
The learner:
- Explains the
value of good
advise
- Explains the
meaning of crisis
- Explains how
friends offer help
in times of a
crisis
The learners:-
- Pronounces,
spells and uses
words
- Crisis
- Emergency
- Will dishonesty
- Biases
- - - - - Fountain
- CRE
- 133-138
-
3 Marriage
- Meaning
- Types
- Reasons why
people marry
- Qualities of a
marriage partner
The learner:-
- Explains the
meaning of
marriage
- Identifies types
of marriage
- Explains qualities
of a marriage
partner
- The learner:-
- Pronounces,
spells and uses
</passage>

<passage id="lchk_1898e987748f4805af88515286c6bdb9" source="P.6 CRE NOTES TERM 3" part="6">
4 State any two qualities of a good marriage partner according to Christian teaching
5 Which type of marriage is practiced in the church?
6 Identify any two problems facing families today
7 How useful is a stable peaceful family to children?
8 Identify any two causes of street children today.
9 name any two Christian organizations that cater for the needs of people in our
community.
1o why do Christians give offertories
www.freshteacheruganda.com For more lesson notes, please visit
CHRISTIAN RELIGIOUS EDUCATION
TOPICAL QUESTION SET 2 TERM III
1. (a) What does the word happiness mean?
(b) In which two ways can man achieve happiness?
2. (a) Give any two benefits of sharing and giving
(b)Why are some people in our community selfish?
3. What is the biblical teaching on life and death?
4. What are the values of suffering (Give two)
5. What does the Bible teach about heaven?
6. Which religion was in Africa before the coming of Europeans?
7. Name any three religions in Uganda.
8. What is the meaning of death in African tradition?
9. Name three causes of death in traditional Africa beliefs
1o. State any three causes of death today
www.freshteacheruganda.com For more lesson notes, please visit
WK PD S/THEME CONTENT SUBJECT
COMPETENCES
LANGUAGE
COMPETENCES
METHODS ACTIVITIES SKILLS AND
VALUES
LEARNING
AIDS
REF REM
1 1 Friends on
the way
Friendship
- Meaning
- Importance
- Jesus example of
friendship
- John 15:12-15
- Qualities of a good
friend
- Jesus’ friendship
from the gospel to
the apostles and
other people
The learner:-
- Explains the
meaning of
friendship
- Identifies the
importance of
friendship
- Explains Jesus’’
example of
friendship
- Points our qualities
of a good friend.
- Describes Jesus’
friendship
according to the
gospel
The learner:-
- Pronounces, spells
and uses words
correctly
- Generous
- Friendship
- relate
- guided
- discovery
- brainstorming
- demonstration
- role play
- guided discussion
- Bible reading
- Discussion
- Role playing
Skills
- Self esteem
- Self awareness
- Creative thinking
Values
- Awareness
- Appreciation
- Love
- The holy
Bible
- Text books
The holy Bible
John 15:12-15
Fountain
CRE
128-133.
2 Importance of advice
- Characteristics of
bad advise
- Crisis and how
friends offer help
in time of crisis
Proverbs 17:17-18
The learner:
- Explains the
value of good
advise
- Explains the
meaning of crisis
- Explains how
friends offer help
in times of a
crisis
The learners:-
- Pronounces,
spells and uses
words
- Crisis
- Emergency
- Will dishonesty
- Biases
- - - - - Fountain
- CRE
- 133-138
-
3 Marriage
- Meaning
- Types
- Reasons why
people marry
- Qualities of a
marriage partner
The learner:-
- Explains the
meaning of
marriage
- Identifies types
of marriage
- Explains qualities
of a marriage
partner
- The learner:-
- Pronounces,
spells and uses
words correctly
- Morals
- Healthy
- Wealth
- Jealousy
- Companionship
- - - - - Fountain
- CRE
- 138-143
-
2 1 Roles of Christian
organization in the
development.
- Definition of
organization
- Examples of
Christian
organizations
- Contributions of
Christian
organizations.
The learner:-
- Defines
“organization”
- Identifies
examples of
Christian
organizations
- Explains the
contributions of
Christian
organizations
The learner:-
- Pronounces,
spells and uses
words correctly
- Organization
- - - - - -
2and
3
Friends on
the way
- Roles of science
and technology in
development
- The learner
- Defines terms
- Technology
- Science
- The learner
pronounces ,
spells and uses
</passage>

<passage id="lchk_06504faf2f8f433abe8cc6c23eca9acf" source="CRE NOTES & SCHEMES P.6" part="20">
Holly living
Purity of the heart
The heart controlled by the Holy Spirit produces the following fruits:-
Love
Generosity
Mercy
Kindness
Honesty
Charity
Modesty – Not talking in a proud way
Chastity – when one lives without having sex
Peace
Integrity
Truth fullness
Loyalty
Hope
Faithfulness
Impurity of the heart
The heart that is controlled by Satan produces the following:-
Hatred
Desire to commit adultery
Evil ambitions
Murder
Anger
Desire to fornicate
Evil thoughts
Permissiveness
How to live a life of purity to enter Heaven
Keep all the commandments without breaking even one
Respect and honour God and its house of worship
Avoid desires of the flesh
Read the word of God often
Imitate Jesus Christ in His way of life while He was on earth
Pray all the time
CHRISTIAN RELIGIOUS EDUCATION
TOPICAL QUESTIONS SET 1
FRIENDS ON THE WAY: TERM III
1 (a) Name the greatest commandment Jesus gave to his followers.
(b) How can people know that Christians are followers of Jesus Christ?
2 (a) In which two ways did Jesus show his love to man-kind.
(b) How useful are pieces of advice given to us by our elders?
3 (a) Give any two characteristics of bad advice
(b) Identify any two groups of people that need guidance and counseling.
4 State any two qualities of a good marriage partner according to Christian teaching
5 Which type of marriage is practiced in the church?
6 Identify any two problems facing families today
7 How useful is a stable peaceful family to children?
8 Identify any two causes of street children today.
9 name any two Christian organizations that cater for the needs of people in our community.
1o why do Christians give offertories
TOPICAL QUESTION SET 2 TERM III
(a) What does the word happiness mean?
(b) In which two ways can man achieve happiness?
2. (a) Give any two benefits of sharing and giving
(b)Why are some people in our community selfish?
3. What is the biblical teaching on life and death?
4. What are the values of suffering (Give two)
5. What does the Bible teach about heaven?
6. Which religion was in Africa before the coming of Europeans?
7. Name any three religions in Uganda.
8. What is the meaning of death in African tradition?
9. Name three causes of death in traditional Africa beliefs
1o. State any three causes of death today
WK
PD
S/THEME
CONTENT
SUBJECT COMPETENCES
LANGUAGE COMPETENCES
METHODS
ACTIVITIES
SKILLS AND VALUES
LEARNING AIDS
REF
REM
1
1
Friends on the way
Friendship
Meaning
Importance
Jesus example of friendship
John 15:12-15
Qualities of a good friend
Jesus’ friendship from the gospel to the apostles and other people
The learner:-
Explains the meaning of friendship
Identifies the importance of friendship
Explains Jesus’’ example of friendship
Points our qualities of a good friend.
Describes Jesus’ friendship according to the gospel
The learner:-
Pronounces, spells and uses words correctly
Generous
Friendship
relate
guided
discovery
brainstorming
demonstration
role play
guided discussion
Bible reading
Discussion
Role playing
Skills
Self esteem
Self awareness
Creative thinking
Values
Awareness
Appreciation
Love
The holy Bible
Text books
The holy Bible
John 15:12-15
Fountain
CRE
128-133.
2
Importance of advice
Characteristics of bad advise
Crisis and how friends offer help in time of crisis
Proverbs 17:17-18
The learner:
Explains the value of good advise
Explains the meaning of crisis
Explains how friends offer help in times of a crisis
The learners:-
Pronounces, spells and uses words
Crisis
Emergency
</passage>

<passage id="lchk_d550af44cf5a46598f6688a3f04c4c49" source="All P 4 To P 7 Religious Education Notes All Terms Copy" part="29">
words correctly
- Morals
- Healthy
- Wealth
- Jealousy
- Companionship
- - - - - Fountain
- CRE
- 138-143
-
2 1 Roles of Christian
organization in the
development.
- Definition of
organization
- Examples of
Christian
organizations
- Contributions of
Christian
organizations.
The learner:-
- Defines
“organization”
- Identifies
examples of
Christian
organizations
- Explains the
contributions of
Christian
organizations
The learner:-
- Pronounces,
spells and uses
words correctly
- Organization
- - - - - -
2and
3
Friends on
the way
- Roles of science
and technology in
development
- The learner
- Defines terms
- Technology
- Science
- The learner
pronounces ,
spells and uses
words correctly
- Guided
discussion
- Demonstration
- Role play
- Bible reading
- Story telling
- Role playing
- Discussing
- Self esteem
- Creative
thinking
- The Holy
Bible
- Text
books
- Fountain CRE
Bk 6
-
www.freshteacheruganda.com For more lesson notes, please visit
- Definitions of
technology and
science
- Roles of education
- Roles of science,
technology and
education
- Importance of law
in society
- The ten
commandments
- Education
- Points out roles
of technology,
science and
education in
development
- Explains the
importance of
law
- Technology
science
- Development
- Education
- Law
- Guided
discovery
- Story telling
- Friendship
formation
- Appreciation
- Awareness
- Love
3 1
and
2
Good citizenship
- Meaning of
citizenship
- Roles qualities of
citizenship
- Requirements for
participating in
general elections
- Rights freedoms
of votes
- Election
malpractices
The learner
- Explains the
meaning of
citizenship
- Identifies roles of
citizens
- Identifies
requirements for
participating in
national election
The learner
- Pronounces,
spells and uses
words correctly
- Mal-practice
- Citizen
- Elections
- Voting
- Rights
- Requirements
- witness
- - - - Fountain CRE
pg 154 to 162
-
3 Happiness
on the
way to
arrival
Happiness
- Meaning
- Signs of happiness
of a person.
- God as a source of
happiness
- Giving and
receiving
- Values of giving
and receiving
John 13:14
The learner
- Explains the
meaning of
happiness
- Identify signs of
a happy person
- Explains how
God is a source
of happiness
- Explains the
values of giving
and receiving
- The learner
- Pronounces,
spells and uses
words correctly
- Happiness
- Giving
- Receiving
- - - - MkStandard CRE
Pg 136-139
-
4 1 Happiness
on the
way to
arrival
- Life and death
- Meaning of life
and death
- Causes of death
- Biblical teaching
about life and
Death
The learner
- Explains the
meaning of life
and death
- Mentions causes
of death
- Explains the
Biblical teaching
about life and
death
The learner
- Pronounces,
spells and uses
words correctly
- Death
- Life
- Heaven
- Destination
- Judgment
- Bible reading
- Demonstration
- Guided discussion
- Guided discovery
- Story telling
Skills
- Self esteem
- Creative
thinking
Value
- Awareness
- Application
- The holy
Bible
- Text
books
- Fountain CRE
- Pg 169-170
-
2 Suffering and
perseverance
- Meaning
- Causes of
suffering
- Values/benefits
of suffering
The learner
- Explains
suffering and
endurance
- Identifies causes
of suffering
The learner
- Pronounces,
spells and uses
words correctly
- Faith
- Perseverance
- Selfishness
- - - - - Fountain CRE
- Pg 171-174
-
www.freshteacheruganda.com For more lesson notes, please visit
- Ways of enduring
- Suffering of
people who
endured suffering
in the Bible
- Points out values
of suffering
- Mentions ways of
persevering
- Identifies people
</passage>

<passage id="lchk_a82d91c6b34747f1a0a1b747994dfbef" source="NCDC P6 Set One Sept book – Religious Education" part="12">
the topic gives them guidance. The qualities and importance of good
friends are clearly discussed in this topic. The topic leads us to an even
stronger and lifetime relationship that is, marriage.

Learning Outcome
The learner develops skills of forming and keeping true friendships and
acknowledges that friendship is a gift that should be cherished.

Resources
• The Bible
• A copy of the Christian marriage vows

Methods | Life Skills
• | Group work | • | Self-awareness
• | Discussion | • | Friendship formation
• | Role play | • | Decision-making
• | Brainstorming | • | Interpersonal
relationships
Values
• | Caring
• | Love
• | Respect
• | Sharing

Primary 6 Curriculum

Subject | Language | Suggested
Content
Competences | Competences | Activities

The learner; | The learner
• explains the | • Friendship | • Group work
reads, | discussion
meaning of | – Meaning and
pronounces | about the
friendship. | importance of
writes, spells | friendship. | meaning of
• describes the | and uses the | friendship.
importance of | – Jesus’ example
following | of friendship | • Bible
friendship.
words | John 15:12 – 15. | readings and
• describes | correctly: | • Qualities of a | discussions
from the | good friend: | about
gospel how | – friend
– Importance | friendship.
Jesus showed | – friendship
of advice, | • Role playing
friendship to | – relate
2Samuel 12, | about how
his Apostles | – relationship | Mathew 19:16-
and other | Jesus showed
– advice | 22
people. | friendship to
– crisis | – Good and bad | people.
• mentions the | – marriage | advice.
qualities of a | – Crisis and how | • Creative
good friend. | friends offer | writing about
support in | qualities
• describes | of good
times of crises
Jesus’ | - Proverbs 17: | friendship.
qualities as a | 17- 18
good friend. | • Brainstorming
– Building a good
about good
• distinguishes | friendship.
friendship.
between | • Qualities
good and | people look
bad advice in | for in marriage
friendship. | partners.
• lists qualities | – Marriage is
of a marriage | a bond of
partner. | friendship
for life - 1
• describes | Corinthians 13:
how a friend | 4 – 7.
should
– Marriage vows.
behave.

National Curriculum Development Center

Guidance to the Teacher
• This topic is expected to cover 8 periods.
• Guide learners to come up with an acceptable definition of
friendship.
• In groups, tell the learners to suggest ways in which the word
friendship is used.
• In groups, guide the learners to describe relationships they have
with their best friends. They should record their discussion and
a report should be made and presented to the whole class.
• Help the learners to read the Bible texts which show Jesus as a
good friend.
• Help the learners identify the qualities of a good friend.
• You need to emphasise to the learners that not all people are
good friends because some of them are misleading and thus they
should distinguish between good and bad advice.
• Guide the learners to role play a crisis situation where friends
offer each other support.
• Lead the learners into discovering how strong friendship
between a man and a woman can lead into marriage.
• Help the learners discuss in groups the qualities one would look
for in a marriage partner. The learners should write them down
and share with the class.
• Role play a wedding ceremony.
• Brainstorm with the learners about the importance of marriage
and marriage vows.
• Be mindful of the learners with special needs.
Suggested Competences for Assessment
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
