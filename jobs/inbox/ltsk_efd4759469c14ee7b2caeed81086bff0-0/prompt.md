# Job ltsk_efd4759469c14ee7b2caeed81086bff0-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 3 lesson(s) below of week 1 of the Christian Religious Education scheme for Primary Five 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P5: one 40-minute lesson: 3–5 sections; about 14–28 points (meaning, examples, reasons, problems and solutions as the passages give); 5–8 activities.

lessonId=lles_0a9008c0d4a047e299ce7fa955d8e95a: lesson 1, Tuesday, 1 period(s), 40 minutes.
  Unit: Witness: Christ the Light (theme: Christian witness, discipleship and hope). Lesson: Christ as the light of the world — Christ as the light of the world.
  Objectives: Explain how Christ is seen as the light of the world.

lessonId=lles_8940941320e64253b1738c546e46726d: lesson 2, Thursday, 1 period(s), 40 minutes.
  Unit: Witness: Christ the Light (theme: Christian witness, discipleship and hope). Lesson: Christ's light seen in people — Christ's light seen in people.
  Objectives: Identify ways Christians witness Christ's light.

lessonId=lles_a12ec3037d564816b1bf7db410ddeb62: lesson 3, Friday, 1 period(s), 40 minutes.
  Unit: Witness: Christ the Light (theme: Christian witness, discipleship and hope). Lesson: Week 1 review — Witness: Christ the Light.
  Objectives: Review this week's lessons: Christ as the light of the world; Christ's light seen in people
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
<passage id="lchk_af0983e9dd8d42c9818cd1d9093d8fb2" source="CRE Notes P 5 ALL Terms" part="15">
3. Who is the head of the church?
4. Why should a Christian pray? Give 2 reasons.
5. What is baptism?
6. What sacrament identifies us with Jesus?
7. What does the water used during baptism symbolize?
8. List down any two benefits of Baptism.
9. What is confirmation?
10. Why do Christians receive the sacrament of confirmation?
11. State any two benefits of confirmation.
12. List down any two characteristics of Christians as members of one universal
church.
13. What three persons do Christians believe in?
14. What will happen on the day f Judgment?
15. What life is there after death?
16. Who is a saint?
17. Name any three common sacraments.
18. Identify any three types of prayers.
19. Why d Christians pray? (Give three reasons)
20. When do Christians pray? (Give two cases)
21. List down any three church activities.
22. Who taught the Lord’s Prayer?
23. Mention any three requests Christians make in the Lord’s Pray er.
24. State any two ways how Jesus acted like a light to us.
For more lesson notes, please visit www.freshteacheruganda.com
CHRISTIAN RELIGIOUS EDUCATION - LESSON NOTES
FOR PRIMARY FIVE
TERM THREE
WITNESS
Christ is the light
According to John the coming of Jesus removed all darkness and sin from the hearts of
many. (John 8:12-20)
What John means by Jesus as the light.
➢ Jesus is the light that gives life.
➢ Christians should follow him since He is the source of life and light.
➢ God the father sent Him into the world to give life to all.
➢ His light is the source of everlasting.
➢ It is only through Him that people can see God.
Ways Jesus was the light of the world.
➢ He trained his disciples to be ready to serve others.
➢ He told the disciples to receive the kingdom of God humbly like little children.
➢ He loved Lazarus so much that wept at his death.
➢ Jesus was loyal to his father throughout His mission.
➢ He healed the sick.
➢ He fed the hungry.
In Mathew 5:14 -16, Jesus says that if people are to remain as salt and light of the
world, we should show the following.
➢ As salt of the earth we should remain tasty and never lose taste.
➢ We should come out in open and shine for others.
➢ We should be the source of light for the sinners.
For more lesson notes, please visit www.freshteacheruganda.com
The healing of a blind beggar. (Luk 18:35-43)
➢ As light, Jesus brought life to the beggar.
➢ The beggar gained vision. This was new life that he had no had since birth.
➢ The beggar increased in faith. He started proclaiming Jesus name.
➢ Those with faith behave the way the beggar did.
The birth of John the Baptist announced.
Luke 1 : 10 – 17
Zechariah was a man who had strong faith in the coming of the Messiah.
He served God well in the temple and one time during his daily work.
Angel Gabriel appeared to him with Good News.
The News was that his wife Elizabeth would bear a child and his name would be John.
The Nature of the child (John the Baptist)
➢ Be filled with the Holy Spirit from birth.
➢ Change the hearts of many for God.
➢ Act as a bearer of Good News for many people.
➢ Come as messenger before the appearance of the messiah.
➢ Live a simple life and eating simple things
➢ Lead the type of life Elijah lived.
The resurrection of Lazarus.
</passage>

<passage id="lchk_0a3e241529644f8281bf332325d73f12" source="P 5 Religious Education Scheme OF Work P5 Term III" part="1">
For more schemes of work, visit www.uganda.madpath.com
RELIGIOUS EDUCATION SCHEME OF WORK P5 TERM III
WK PD TO
PIC
SUB-
TOPIC
COMPETENCE
CONTENT METHOD
S
SUGGES
TED
ACTIVITI
ES
LIFE
SKILLS/
VALUES
TEAC
HING/
LEAR
NING
AIDS
REF
R
M
KS SUBJECT LANGUA
GE
1 1 &
2
Witn
ess
Christ
the
Light
The learner:
• Explains
how
Jesus is
the light
of world.
The
Learner:
Reads,
pronounc
es new
words
e.g.
Our
experienc
e:
• Local story
of some
one who
tried to
• Story
telling.
• Dramatiz
ation
• Group
work
• Singing
songs
about the
light of
the
world.
• Appreciat
ion
• Love
• Bible.
• Pictur
es of
Christ
Good
News
Bible.
For more schemes of work, visit www.uganda.madpath.com
WK PD TO
PIC
SUB-
TOPIC
COMPETENCE
CONTENT METHOD
S
SUGGES
TED
ACTIVITI
ES
LIFE
SKILLS/
VALUES
TEAC
HING/
LEAR
NING
AIDS
REF
R
M
KS SUBJECT LANGUA
GE
• Writes
ways in
which
Christ is
seen as
a light in
us and in
the
world.
Light,
Christ,
Witness.
save
another
person out
of danger.
Gods
message
• How
Christ is
the light.
• John 8:12-
20.
• How
Christ’s
light can
be seen in
us
Lk 18:35-
43
Lk1:10-17
• Discussi
ng ways
in which
Christ is
seen as
the light
in us in
the
world.
2 1 &
2
Witnessi
ng for
the
church
Describes
different
ways of
The
leaner:
• Reads,
pronounc
Our
experienc
e
• Story
telling.
• Group
work.
• Discussin
g ways of
witnessin
• Apprecia
tion.
• Love
Bible Good
News
Bible
For more schemes of work, visit www.uganda.madpath.com
WK PD TO
PIC
SUB-
TOPIC
COMPETENCE
CONTENT METHOD
S
SUGGES
TED
ACTIVITI
ES
LIFE
SKILLS/
VALUES
TEAC
HING/
LEAR
NING
AIDS
REF
R
M
KS SUBJECT LANGUA
GE
witnessing
for Christ
es and
writes
the new
words
correctly
e.g.
Witness,
Christ,
Mathew
• Learners
mention
different
activities
done by
Christians.
Gods
Message
Witnessing
for Christ
• Living as a
witness for
Christ.
Mathew
5:14-16.
• Spreading
the word
Mat 28:19-
20. Eph
4:11-12.
Ways of
witnessing
for Christ:
• Explanati
on.
g for
Christ.
• Discussio
n in
groups
different
Christians
in history
who have
witnessed
for Christ.
For more schemes of work, visit www.uganda.madpath.com
WK PD TO
PIC
SUB-
TOPIC
COMPETENCE
CONTENT METHOD
S
SUGGES
TED
ACTIVITI
ES
LIFE
SKILLS/
VALUES
TEAC
HING/
LEAR
NING
AIDS
REF
R
M
KS SUBJECT LANGUA
GE
Ephesians
4:7
Kivebulay
a, Mother
Tereza,
Nelson
Mandela,
Julius
Nyerere
3 1 &
2
Witn
ess
Voluntar
y
Organiz
ations
The learner:
• Mentions
examples
of
voluntary
work.
• States the
meaning
of a
voluntary
service
and a
voluntary
The
learner:
Pronounce
s the new
words
correctly
e.g.
Voluntary,
Service,
Our
experienc
e
• Learners
mention
the duties
of the Red
Cross
Society in
school.
Gods
message
• Story
telling.
• Dramatiza
tion.
• Class
discussio
n.
• Dramatizi
ng the
story of
the Good
Samarita
n
• Love.
• Apprecia
tion.
• Self
awarene
ss.
• Problem
solving
A chart
showin
g a
picture
of a
Good
Samarit
an
Bible.
Good
News
Bible
For more schemes of work, visit www.uganda.madpath.com
WK PD TO
PIC
SUB-
TOPIC
COMPETENCE
CONTENT METHOD
S
SUGGES
TED
ACTIVITI
ES
LIFE
SKILLS/
VALUES
TEAC
HING/
LEAR
NING
AIDS
REF
R
M
KS SUBJECT LANGUA
GE
organizati
on
Organizati
on.
• The story
of the
Good
Samaritan.
Our
response
• Dramatize
the story
of the
Good
Samaritan.
4 1 &
2
Disc
iple
ship
and
its
rew
ard
Disciple
s of
Jesus
(Apostle
s of
Jesus)
The learner:
• Gives the
difference
between
apostles
and
disciples.
• Mentions
the 12
The
learner:
Spells
and
reads the
words
Apostles,
Disciples,
Our
experienc
e:
• Mentionin
g the roles
of the
Church
leaders
God’s
message
• Explanati
on.
• Story
telling
</passage>

<passage id="lchk_3f56d32c757948a687e50291e63ce909" source="NCDC P5 Curriculum – Religious Education" part="9">
witnessing for | different Christians in
Christ. | history who have
Ǧ | Ephesians 4:7 | witnessed for Christ.
Ǧ | Kivebulaya
Ǧ | Mother Tereza
Ǧ | Nelson Mandela
Ǧ | Nyerere
Ǧ | 1Timothy 3:1 – 2
Ǧ | Mathew 5:14-16

P5 Set One Syllabus, National Curriculum Development Centre | 133

    |   |  |   |  
•  Demonstrates | • | Talks about how | How to reflect the | •  Discussing the | • | Voter
the Christian | to reflect the light | light of Christ to | values that | Educations
service to the | of Christ to other | other people | promote good | Manual
community as a | people. | Ǧ Values that share | • behaviour.
witness to | good behaviour.
Christ. | Ǧ Avoiding moral
• Explains how to | degeneration in
form healthy | society.
relationships. | Ǧ The role of a returning
officer, presiding
officer, polling
assistant, constable,
etc.

TOPIC 8: | Discipleship and its Rewards
Background to the Topic
This topic presents the idea of discipleship to the learner as well as the teaching of Jesus about discipleship. It further gives knowledge to
the learners about the qualities and examples of discipleship. It also gives examples of famous Christians who emulated the discipleship
as understood and taught by Jesus.

This topic teaches learners about relationships, qualities of a good friend and Jesus as a good friend. It also gives some knowledge on
the polling process as seen in the roles of election observers and election monitors. The teacher can use group discussion, explanation,
question and answer, and role-play in teaching this topic.

Learning Outcome:
The learner is able to understand and explain the concept of discipleship and describe Jesus’ teaching about discipleship.
134 | P5 Set One Syllabus, National Curriculum Development Centre

Life skills
• Friendship formation.
• Critical thinking.

Values
Ǧ Cooperation | Ǧ Respect
Ǧ Love | Ǧ Patience

    |   |  |   |  
The learner: | The learner, | Discipleship | • | Brainstorming on | • | Bible
• Describes | • Tell Jesus | • Describe discipleship | Jesus’ teachings on
discipleship | teaching on | • Jesus teaching | discipleship.
Discipleship. | Ǧ Mark 1:16-20
• Ǧ Mathew 4:23-25
• | Explains Jesus’ | • | Writes some | Examples of | • | Discussing what
teaching on | examples of | discipleship | Jesus taught about
discipleship | discipleship | • Spiritual uprightness | discipleship.
• Comfort in sorrow.
• Being humble. | • | Identifying different
• Being pure in heart. | examples of
• Working for peace. | discipleship.
• Courage in
persecution.
Ǧ Mathew 5:1 – 10
Ǧ Luke 12: 29 – 31
• | Lists some | • | Reads the lives of | Some famous Christians | • | Profiles of
famous | some famous | who lived a life of | famous
Christians who | Christians who | discipleship | Christians like
Ǧ St. Francis of Assisi
lived a life of | lived a life of | St. Francis of
Ǧ St. Clare
discipleship. | discipleship. | Ǧ St. Augustine | Assisi

P5 Set One Syllabus, National Curriculum Development Centre | 135

TOPIC 9: | RELATIONSHIP WITH GOD
Background to the Topic
This topic helps the learner to explore the concept of the Trinity: the “three persons in one”. It helps the learner to explore the roles of
each personality in the Trinity.

The relationship between the Trinity reflects love, it is the same love that should exist and guide the relations of God’s creatures. This
</passage>

<passage id="lchk_cbaf0568f9c24ebbb333e51a1dc51891" source="P 5 R E Lesson Notes Term III" part="4">
 According to Luke 10:27, the second great commandment is:-
 “Love your neighbour as you love yourself”
 According to this commandment, a neighbour is any person.
This commandment requires us to treat other people as we would like to be treated.
Each one of us would like to be treated in the following ways:-
 Loved
 respected
 accepted as we are
 Praised wherever necessary.
 Comforted when we are sad
 Thanked when we do something good.
 Provided with needs.
10
Note:
 A neighbor is a person who helps you when in need/ in trouble.
 Give ways of showing good neighborhood in a community.
Exercise
1. How is the Pentecost day important to Christians?
2. Outline any three symbols of the Holy Spirit.
3. State the two great commandments.
4. Outline any four ways you as a Christian would like to be treated.
5. As a Christian how can you treat your neighbour?
6. Write down the 10 commandments God gave to Moses.
Date
Class L. Area No. of children Time
P.5 R.E
THEME : Our relationship with God
SUBTHEME : Christians who showed love for God and other people
Language competence:
1. Gives the meaning of new words i.e
- Justice
- Injustice
- Pentacost day
2. Spells the names of personalities. E.g. Martin Luther, Damien
INTRODUCTION : The lesson will be introduced by reviewing the previous lesson.
CONTENT : Christians who showed love for God and other people
Martin Luther King:
 He fought against injustice between the black Americans and whites.
 He wrote magazines about racial discrimination in America.
11
Civil rights activists
 Demanded for equal rights through peaceful means and civil disobedience
Father Damien:-
 He went to the island of Molokai in Belgium to preach the word of God to the lepers. he
also died of leprosy.
 He treated people who were suffering from Leprosy
Topical test
1. What does the term trinity mean?
2. Name the three persons who make up one God.
3. State the role of God the father.
4. Why did God send his only son Jesus Christ to earth?
5. State two duties of the Holy Spirit.
6. In which ways does the Holy Spirit help Christians today?
7. As a Christian, explain four ways through which you would treat your neighbour.
8. How is the Pentecost day important to Christians?
9. Give four fruits of the Holy Spirit.
10. Outline three gifts of the Holy Spirit.
11. State the greatest commandments.
12. Why is mountain Sinai important to Christians
13. Give one reason why Moses was given the Ten Commandments by God.
14. What does the term eternal life mean?
15. What does God tell us to do in order to get eternal life?
16. State any two people who showed love for God and other people.
17. Why is Martin Luther king still remembered in the history of America?
18. Outline any two roles of God the son.
19. Which of the three persons of the trinity is responsible for sanctification?
20. State any three things the first great commandment forbids us to do.
12
Date Class L. Area No. of children Time
P.5 R.E
THEME : Hope
SUBTHEME : Psalms of Hope
INTRODUCTION : The lesson will be introduced by discussing what hope is
CONTENT : Psalms of Hope
Hope
Hope is living with an expectation of something better yet to happen. To expect that something
will happen.
Importance of hope
Helps people to withstand suffering.
Helps people to be patient.
It makes us have meaning for life.
Hope is expectation of something better to happen.
- Effects of living without hope (hopelessness)
- People may not withstand hard times e.g. suffering, death
</passage>

<passage id="lchk_33701deccaae42a8a951c8e4f63437bb" source="P 5 R E Lesson Notes Term III" part="5">
- It leads to impatience among people
- It makes people lose meaning for life.
- It brings fear and shame.
Acts of hopeless people
- Committing suicide
- Some resign jobs
- Theft
- Corruption
- Bribery
Examples of Psalm of Hope
Psalms 42:5
 Why am I so sad?
 Why am I so troubled?
 I will put my hope in God and once again I will praise him.
13
Psalms 33:20
We put our hope in the lord. He is our protector and our help. We are glad because of him. We
trust in the holy name.
May your constant love be with us.
Lord as we put our hope in you
The old testament teaching about Hope (Jer. 23: 5 – 6 , 31: 1 – 5)
 At times, we make wrong choices which bring us into trouble. We should not blame any
one else for these problems. We may be the ones to blame.
 This happened to Israelites during the time of Jeremiah. This happened never wanted to
live a holy life as God wanted them to do.
 God sent his messengers to warn and persuade the Israelites to change their ways. The
Israelites would not listen to the voice of God.
 They became even more stubborn. They were rebellious, corrupt, liars, thieves and ran
after gods. (Jeremiah 5,6)
 God decided to punish the Israelites for their sins. God allowed foreign armies to invade
Israel. Many of the Israelites were taken into exile.
 But God was sorry for what his people were going through. He promised that they would
be restored if they changed their ways.
 “I alone know the plans I have for you, plans to bring prosperity and not disaster, plans to
bring about the future you hope for” (Jeremiah 29:11 – 14)
 If we continue sinning without repenting our sins, we cannot have hope from God.
Exercise
1. How is hope important to man?
2. Why was God not happy with the Israelites according to the book of Jeremiah?
3. What should we do after sinning to God?
4. What did Prophet Jeremiah preach about?
5. Mention any four ways Israelites turned away from expectations of God.
6. Identify any four ways people in Uganda have turned away from God’s guidelines.
14
Date Class L. Area No. of children Time
P.5 R.E
THEME : Hope
SUBTHEME : Psalms of Hope
INTRODUCTION : The lesson will be introduced by reviewing the previous lesson
LESSON 1
CONTENT : The coming of Jesus the promised Messiah
How people were prepare for the coming of Jesus. God sent different prophets to inform people
about the coming of Jesus.
Examples of prophets God sent (Messianic Prophets) – talk about what each prophesized.
 Isaiah
 Zechariah
 Micah
 John the Baptist
LESSON II
 God formed a nation of God’s chosen people (Israel) in whom the messiah was born.
 People repented their sins and got baptized by John the Baptist.
 Receiving and listening to messages about the messiah.
 The mother of the messiah accepted the task.
 The coming of Jesus as the promised messiah brought the real hope.
The birth of Jesus, the promised Messiah
 After waiting for 4000 years, the Savior was born.
 His mission was to save people from their sins.
 The mother of Jesus was Mary the Virgin.
 Jesus’ father was Joseph
 Jesus was born on Christmas day.
 Jesus was born from a kraal in Bethlehem.
 Today Christians celebrate the birth of Jesus on Christmas day.
 Christians celebrate the birth of Jesus on 25 th December every year.
15
 We also have hope for the second coming of Jesus.
Some of the names of Jesus
 Christ
 Redeemer
 Messiah
 Lord
 Saviour
 Immanuel – God is with us.
Eternal life (Thessalonians 4:13 – 14)
</passage>

<passage id="lchk_526fa31e33c048179dbdaa358f860e49" source="P 5 R E Term I, II, III #creative Printers" part="9">
P.5 CRE LESSON NOTES FOR TERM: III- 2023.
THE TEACHING OF JESUS ON DISCIPLESHIP.
A disciple is a follower of Jesus.
Discipleship means imitating the work of Jesus as a teacher.
We must be able to suffer for the sake of Christ and give up our own interests. (Luke
14: 25-27)
The teaching of Jesus about discipleship.
i. Happy are those who know that they are spiritually poor! The kingdom of
heaven belongs to them (Mathew 3:5)
ii. Happy are those who mourn! God will comfort them. (Mathew 3: 4)
iii. Happy are those who are humble; they will receive what God has promised
them.
iv. (Mathew 3: 5)
v. Happy are those whose greatest desire is to do what God requires! God will
satisfy them fully. (Mathew 3: 6)
vi. Happy are those who are merciful to others! God will be merciful to them.
(Mathew 3: 7)
vii. Happy are those who are pure in heart! They will see God. (Mathew 3: 8).
viii. Happy are those who work for peace! God will call them his children.
(Mathew 3: 9)
ix. Happy are those who are persecuted because they do what God requires!
The kingdom of God belongs to them. (Mathew 3: 10)
Lives of people who fulfilled Jesus’ teaching of discipleship.
These are the people who acted as good examples to us
St. Francis.
He lived from 1182 – 1226 in Assisi in Italy.
He was born in a rich family but his heart changed to God.
He gave up his property to the poor. He started living a simple life by teaching the
message of Jesus Christ.
He started living a poor life but never regretted.
He continued to serve God till death.
Before his death, he had founded the Franciscans order, which is still serving in
different parts of the world.
Khama.
He lived in South Africa.
He became so popular after converting to Christianity.
He preached against murder, polygamy and witchcraft.
He became a chief of his clan and changed many of his tribe mates to Christian
teaching.
19 #CREATIVE PRINTERS 0703745068
Nicky Cruz.
He was a drug addict who lived in New York City of USA.
He was a member of a gang who fought police and killed many people.
One day he turned to God. His former group wanted to kill him but trusted Jesus and
won them to Christianity.
Uganda martyrs.
For example Mbaga Tuzinde, Charles Lwanga, Noah Mawaggali, etc.
Characteristics for Christian’s life.
All Christians should live in a life which is pleasing God. He/she should serve as an
example for the rest.
The way they talk and dress.
Seeking God’s guidance.
Desire to serve others.
Contentment.
OUR RELATION WITH GOD.
The Holy Trinity.
The word trinity comes from the Latin word called Trinitas, meaning three ness.
This is the existence of three persons in one God i.e.
I. God the father.
II. God the son.
III. God the Holy Spirit.
God the father .
Created all living and non-living things.
Provides us with our needs.
Protects us from danger.
Sent his son to save us.
God the son.
Saved us from sin.
Show us God the father
Gives internal life.
Sent the Holy Spirit.
God the Holy Spirit .
Teaches about the son.
Helps us during prayer
Guides us in our lives as Christians.
Jesus teaches about prayer:
Jesus taught His followers the Lord’s Prayer.
20 #CREATIVE PRINTERS 0703745068
Requests made in the Lord’s Prayer.
i. To give us food (our daily bread).
ii. To forgive our sins.
iii. Not to take us to temptation (protect us from evil).
iv. To deliver us from sin (guide us).
v. God’s will be done.
vi. God’s kingdom to come.
MARRIAGE:
Marriage is a legal union/agreement/relationship between a man and a woman as
</passage>

<passage id="lchk_070218ba35a74b91a8fcdd3abd96bf35" source="Primary Five Tekart Revision R E" part="36">
_________________________________________________________________________
________________
c) Matthew;
__________________________________________________________________
TEKART LEARNING REVISION SERIES 68
d) John;
_________________________________________________________________________
________________
Or: How were the following people related to prophet Muhammad ?
a) Abdallah ;
_________________________________________________________________
b) Amina;
__________________________________________________________________
c) Halima;
_________________________________________________________________________
________________
d) Hadijah;
_________________________________________________________________________
________________
31. Either:
a) Who led Jesus into the wilderness ?
____________________________________________________________________
b) Mention three temptations the devil gave to Jesus Christ.
Or:
a) How did the first muslim martyr meet her death ?
____________________________________________________________________
b) Name the place of worship for muslims.
____________________________________________________________________
c) State two reasons why we should forgive others.
Both:
32. a) What is trinity ?
b) mention the three persons that form the Holy trinity.
TEKART LEARNING REVISION SERIES 69
33. a) What is sin ?
__________________________________________________________________
b) Mention any one cause of sin.
__________________________________________________________________
c) Give two results of sin.
34. a) What is a miracle ?
__________________________________________________________________
b) Give any two miracles performed by Jesus.
c) Why did Jesus perform miracles in His ministry ?
____________________________________________________________________
35. a) Give two similarities between Christianity and Islam.
b) State two differences between Christianity and Islam.
TEKART LEARNING REVISION SERIES 70
PAPER EIGHT
SECTION A:
In this paper answer either Christianity or Islam but not both.
1. Either : In which book of the Bible do we read the story of creation.
_________________________________________________________________
Or : In which city did Miraj take place?
_________________________________________________________________
2. Either : Who is a prophet?
_________________________________________________________________
_________________________________________________________________
Or : Who is a messenger in Islam?
_________________________________________________________________
_________________________________________________________________
3. Either : Why did God send His only son, Jesus Christ into the world?
_________________________________________________________________
Or : Why did Allah send prophets to His people?
_________________________________________________________________
4. Either : What name was given to the short stories Jesus used to teach His disciples?
_________________________________________________________________
Or : What name is given to the teachings, sayings or acts of prophet Muhammad?
_________________________________________________________________
5. Either : State one way Abraham showed his faith in God.
_________________________________________________________________
Or : State one way prophet Ibrahim showed his faith in Allah.
_________________________________________________________________
_________________________________________________________________
</passage>

<passage id="lchk_affb83d4494649f8b4852147b51b41e6" source="Primary Five Tekart Revision R E" part="8">
11. Either : What did God create on the second day?
______________________________________________________________________
Or : Mention one item from which the idols were made during prophet Ibrahim’s time.
______________________________________________________________________
12. Either : What should a Christian do after sinning?
_____________________________________________________________________
Or : What should a Muslim do after disobeying Allah?
______________________________________________________________________
13. Either : What is meant by the term Lent in Christianity?
______________________________________________________________________
Or : What is meant by the term ‘Adhan’ in Islam?
______________________________________________________________________
14. Either : Name the person who led the Israelites to the Promised Land.
______________________________________________________________________
Or : Name the prophet Allah sent to the people before He sent the floods.
______________________________________________________________________
15. Either : What lesson do Christians learn from the story of the Good Samaritan?
______________________________________________________________________
Or : What lesson do Muslims learn from the life style of prophet Muhammad?
______________________________________________________________________
16. Either : According to the book of Genesis, who committed the first murder?
______________________________________________________________________
Or : According to Islam, who was the last prophet in Islam.
TEKART LEARNING REVISION SERIES 14
______________________________________________________________________
17. Either : Why is river Jordan an important place in the Christian faith?
______________________________________________________________________
Or : Why is Madina an important place in Islam?
______________________________________________________________________
18. Either : A part from Joshua, name any other Israelite leader who reached the Promised Land from
Egypt
______________________________________________________________________
Or : A part from Fatuma, name any other daughter of prophet Muhammad.
______________________________________________________________________
19. Either : Give one way Jesus showed his love for man kind.
______________________________________________________________________
Or : Give one way prophet Muhammad showed his love to his followers.
______________________________________________________________________
20. Either : Mention the last book in the Bible.
______________________________________________________________________
Or : Mention the last divine book in Islam.
______________________________________________________________________
SECTION B.
21. Either : (a) On which day do Christians celebrate the resurrection of Jesus Christ?
______________________________________________________________________
(b) Mention three things that happened when Jesus died on the cross.
(i) ______________________________________________________________________
(ii) ______________________________________________________________________
(iii) ______________________________________________________________________
Or : (a) Which celebration marks the end of the month of Ramadhan?
______________________________________________________________________
(b) Mention three ways Moslems are supposed to behave in the month of Ramadhan.
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
