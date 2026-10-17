# Job ltsk_5f4590f5075e47c0af572dab533b629f-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 3 lesson(s) below of week 4 of the Christian Religious Education scheme for Primary Five 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P5: one 40-minute lesson: 3–5 sections; about 14–28 points (meaning, examples, reasons, problems and solutions as the passages give); 5–8 activities.

lessonId=lles_a93d5133ea7a4bfdb2769cf70d316a62: lesson 10, Tuesday, 1 period(s), 40 minutes.
  Unit: Relationship with God (theme: Christian witness, discipleship and hope). Lesson: God the Father — God the Father.
  Objectives: Explain the Christian teaching concerning God the Father.

lessonId=lles_35d7dbaf06aa455db2f46a37bc03c0f0: lesson 11, Thursday, 1 period(s), 40 minutes.
  Unit: Relationship with God (theme: Christian witness, discipleship and hope). Lesson: God the Son — God the Son.
  Objectives: Explain the Christian teaching concerning God the Son.

lessonId=lles_b9f1d59a391444809b4d48cd5b9f7b7a: lesson 12, Friday, 1 period(s), 40 minutes.
  Unit: Relationship with God (theme: Christian witness, discipleship and hope). Lesson: Week 4 review — Relationship with God.
  Objectives: Review this week's lessons: God the Father; God the Son
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
<passage id="lchk_ca727a4838654f60bf1fdd1287c7b8a8" source="P 5 Religious Education Scheme OF Work P5 Term III" part="2">
Identifyin
g the
disciples
(Apostles
of Jesus)
• Critical
thinking.
• Friendsh
ip
formatio
n.
A chart
showing
Jesus’
Apostle
s
Bible
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
apostles of
Jesus
Resurrect
ion
correctly.
• Jesus’
teaching
Mark 1:16-
20,
Mathew
4:23-25
Our
Response
• Discussing
about
Jesus’
Apostles.
5 1 &
2
Disc
iple
ship
and
its
Rew
ard
Teachin
g of
Jesus
on
disciple
ship
The learner:
• Explains
Jesus’
teachings
on
discipleshi
p.
The
learner:
Pronounce
s, reads
and spells
words e.g.
Our
experienc
e
• Discussing
different
ways of
talking to
our
parents
when we
• Class
discussio
n.
• Explanati
on
Identifyin
g different
examples
of
disciplesh
ip
• Friendsh
ip
formatio
n
n,
• Critical
thinking
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
• States the
meaning
of prayer.
• Mentions
types of
prayer.
Discipleshi
p, Prayer,
Intercessio
n,
Thanksgivi
ng,
Trespasse
s.
are in
need.
God’s
message
• Examples
of
discipleshi
p.
• Spiritual
uprightnes
s.
• Comfort in
sorrow.
• Being
humble.
• Being pure
in heart,
working
for peace,
courage in
persecutio
n
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
Lk 12:19-
29
Our
Response
Learners
mention
different
examples
of
discipleshi
p.
6 1 &
2
Rel
atio
nshi
p
with
God
The
Holy
Trinity
The learner
• States the
meaning
of the Holy
Trinity.
• Mentions
the three
persons
that make
up the
The
learner:
Pronounc
es, spells
the words
e.g.
Holy
Our
experienc
e
• Discussing
different
roles
played by
family
members.
• Whole
class
discussio
n.
• Explanati
on.
• Singing
the song
of the
Trinity.
• Memorizi
ng the
Bible
verses
on
Trinity.
• Friendsh
ip
formatio
n
• Critical
thinking
Bible
Poem
about
Trinity.
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
Holy
Trinity and
their
duties.
Trinity,
The Holy
Sprit.
God’s
message
God the
Father 1Jn
3:1
God the
Son
Jn 15: 9-10
God The
Holy Spirit
Romans
5:5
7 1 &
2
Hop
e
Teachin
g of the
Testam
ent on
the
Hope
that
The learner:
• States the
meaning
of Hope.
• Mentions
the
The
learner;
Pronoun
ces,
reads
and
spells the
Our
experienc
e:
Examples
of situations
when
someone is
• Role play.
• Whole
class
discussio
n
Discussing
Bible tests
• Coping
with
emotions
.
• Decision
making
PIASCY
material
s
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
God
gives.
importanc
e of Hope.
new
words
e.g.
Hope,
Messiah
in trouble
and later
succeed.
Gods
message
• Psalms of
hope
Psalms
31:24,
33:20.
• Hope in
Trouble.
• Jeremiah
6:22-23.
• Hope for
the
Messiah.
Isaiah
11:1-10.
Our
Response
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
</passage>

<passage id="lchk_4e61ef831c6a48ac964838bbb3f44a11" source="P 5 R E Lesson Notes Term III" part="3">
4. Use the following words in the sentences to show that you know their meanings.
a) Glory
b) divine
c) trinity
5. Who is the head of the Holy Trinity?
6. According to the Holy Trinity who is God the son?
7. Name one person in the Holy Trinity who is always among believers.
Date Class L. Area No. of children Time
P.5 R.E
THEME : Our Relationship with God
SUBTHEME : The Holy Trinity
INTRODUCTION : The lesson will be introduced by reviewing the previous lesson.
7
CONTENT : Common Duties of the three Persons
Spellings
- Eternal
- Eternity
- Guides
- Strengthen
- Suffered
God the father. (1 John 3:1) (Luke 12:29 – 30)
He created all living things and non – living things.
 He provides us with all our needs.
 He protects us from all dangers.
 He sent his son to save us.
God the son (John 15:9 – 10) (John 8:19)
 He saved us from sin.
 He showed us God the father
 He gives us eternal life.
 He sent the holy spirit to us.
God the Holy Spirit (Romans 5:5, 8:11 – 17)
 He teaches us about the son.
 He guides us in our life as Christians.
 He helps us during prayer.
 He gives us Jesus to proclaim Jesus.
 He strengthens our faith in God.
The love of the Three persons of Trinity for us:
God the Father
 He for gives us our sins.
 He provides us with our needs.
 He set his only son Jesus to earth.
God the son
 He accepted to become a human being like us.
 He healed, fed the hungry and preached.
8
 He suffered on our behalf.
 He died on the cross for our sins.
God the Holy Spirit
 He enables us to share the suffering and the glory of Jesus. He gives us blessing.
 He makes us God’s children.
 He makes us God’s children.
 He helps us to overcome our sin full nature.
 He gives us courage to call God our father.
Exercise
1. State one roles of God the father.
2. How is God the Holy Spirit important to Christians?
3. What important role did God the son offer to us?
4. Explain the love of the three person of the trinity for us.
5. Which of the three persons of the trinity gives us eternal life?
6. Write down any two ways you can benefit from God the Holy Spirit.
Date Class L. Area No. of children Time
P.5 R.E
THEME : Our relationship with God
SUBTHEME : God the Holy Spirit
INTRODUCTION : The lesson will be introduced by reviewing the previous lesson.
Language competence: Constructing sentences using three persons of holy trinity
CONTENT : The coming of the Holy Spirit
The disciples received the Holy Spirit on the Pentecost day. It took forty days for the disciples to
receive the Holy Spirit.
Signs which showed the disciples had received the Holy Spirit
 Strong wind came from the sky.
 The apostles spoke different languages.
 The flames of fire appeared on their heads.
 The disciples spoke different languages.
9
Symbols of the Holy Spirit
 Strong wind
 Fire
 Dove
The Two Great Commandments (Matthew 7:12) - Bible reading
 A commandment is order from God. Moses received the Ten Commandments from Mt.
Sinai. God gave the Israelites these commandments because they had began behaving
badly.
The first great commandment
 “Love the Lord your God with all your heart, with all your soul, with all your strength
and with all your mind.
 Four commandments deal with our relationship with our God. These commandments.
forbid us from:-
 Worshipping other gods.
 Making any object for worship.
 Using God’s name falsely.
 Keeping his day unholy.
The second great commandment (Matthew 5:43 – 44)
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

<passage id="lchk_c86a32aa12604f768607232ce603074a" source="NCDC P5 Curriculum – Religious Education" part="10">
topic gives examples of Christians who to their best, lived and practiced love of God and love of fellow human beings. The topic
challenges the learner to respond to that divine love by emulating the examples of some famous Christians.

The suggested methods will include singing, reading the Bible and discussions.

Learning Outcome
The learner is able to study and articulate the roles played by the three persons: God the FATHER, God the SON and God the HOLY
SPIRIT.

    |   |  |   |  
• | The learner: | The learner: | Trinity | • | Memorizing the Bible | • | Bible
Describes the | • Writes the roles | • God the Father | verses on the Trinity.
role of the three | of the three | Ǧ 1 John 3:1 | • | Discussion of the
persons of the | persons of the | Ǧ Luke 12:29-30 | verses
Trinity. | Trinity. | Ǧ 1 John 4:8-10 | • | Guided discovery on
• Writes a simple | • God the Son John 15:9- | the roles of each
• | Identifies the | poem about the | 10 | person.
three persons | trinity | Ǧ John 8:19
which make the | • God the Holy Spirit | • | Singing a song of the
Trinity | Ǧ Romans 5:5, 8:9-17 | Trinity.
• Concept of the Trinity
• | Explains the
Ǧ Mathew 3:16-17 | • | Creative writing
role of each
Ǧ Mathew 2:28:19
person
Ǧ 1Peterϭ͗Ϯ

136 | P5 Set One Syllabus, National Curriculum Development Centre

    |   |  |   |  
• | Identifies the | • | Reads the | Two great | • | Studying Bible
two great | Bible verses. | commandments | references and
commandments | • Jesus teaching John | discovering the role
•  Writes the two | 15:9-12 | God the Father Son
Jesus taught.
great | Mathew 7:12 | and the Holy Spirit
Mathew 5:43-44. | plays.
• | Responds to | commandments.
• Examples of | • | Memorizing the great
God’s love by | • Talks about | commandments taught
Christians who | Christians Who loved
obeying His | by Jesus.
showed love | without
commandments
to others. | discrimination
and loving | • | Dramatizing ways
• Reciting the two | • Our response
others | they can show Gods
great
love to others.
commandments.

TOPIC 10: HOPE
Background to the Topic
This topic aims at equipping learners with knowledge and skills that will encourage them never to give up. It explains to the learners how
people waited for a Saviour right from the Old Testament times. The learners will be exposed to the messages of hope in Psalms,
Jeremiah and Isaiah.

The topic of hope will also be applied in the learners’ daily lives. The methods of instruction will include reading the Bible, discussion,
singing, creative writing and role playing.

P5 Set One Syllabus, National Curriculum Development Centre | 137

Learning Outcome
The learner is able to:
• Appreciate the fact that God is the source of hope in all circumstances.
• Develop skills that enable him/her to keep going on even under difficult circumstances.

Life skills
• Coping with emotions
• Decision-making

Values
• Faith
• Hope

    |   |  |   |  
The learner: | The learner, | Psalms of Hope | • | Bible
• Explains | • Reads Luke 2:42 | Psalms 31:24 | • | Memorizing Psalms
Psalms of hope | • Psalms of hope. | 33:20, 33:22 | of Hope.
as reflected in | 34:17-18, 42:5
71:5 – 7 | • | Discussing of the
the Bible.
• God give strength. | message in the
• God gives | Psalms.
protection.
• | Writes how hope | • God listens. | • | Writing a prayer
</passage>

<passage id="lchk_b7a765d26a7d4b2a803fec3f9aa4ef7f" source="P 5 R E Lesson Notes Term III" part="1">
1
P.5 R.E LESSON NOTES FOR TERM III
Date Class L. Area No. of children Time
P.5 R.E
THEME : Discipleship and its rewards
SUBTHEME : Teaching of Jesus on discipleship
INTRODUCTION : The lesson will be introduced by reviewing who a disciple is.
Language competence: Pronounces and gives the meaning of new words e.g
- Disciple
- Discipleship
- Happiness
- Persecution
- Pure
- Merciful
CONTENT : Teaching of Jesus on discipleship
A disciple is a closest follower of Jesus Christ.
Discipleship is copying Jesus’ examples.
Copying Jesus’ life style.
Examples of discipleship
 Spiritual uprightness
 Being humble
 Working for peace.
 Courage during persecution
 Obedience
 Forgiveness
Jesus’ teaching about discipleship
 This is what Jesus taught about discipleship. (Matthew 5:1 – 11) – Bible teaching
Finding happiness
 Happy are those who know they are spiritually poor; the kingdom of heaven belongs to
them.
 Happy are those who mourn, God will comfort them.
 Happy are those who are humble, God will give them what he has promised.
 Happy are those who are merciful to others, God will be merciful to them.
 Happy are those whose greatest desire is to do what God requires.
 God will satisfy them fully
2
 Happy are those who are persecuted because they do what God requires, the kingdom of
heaven belongs to them.
Exercise
1. Who is a disciple?
2. What is a discipleship?
3. State two examples of discipleship. .
4. How will people benefit from being humble?
5. Outline any three Jesus teaching on discipleship.
6. How will God reward the following:-
a. The spiritually poor?
b. The mourners?
c. Those who are merciful?
d. Those who are persecuted?
7. According to Jesus’ teaching, which four groups of people are to be happy?
Date Class L. Area No. of children Time
P.5 R.E
THEME : Discipleship and its rewards
SUBTHEME : Lives of people who fulfilled Jesus’ teaching on discipleship.
INTRODUCTION : The lesson will be introduced by reviewing the previous lesson.
Language competence: Constructing sentences using names of people who fulfilled Jesus’
teaching
Text book teaching
CONTENT : Khama
 He was born in South Africa. He spread the word of God to the people of his tribe.
 Some of his tribe mates hated him and even tried to kill him.
 He preached against murder, polygamy and witch craft.
Nicky Cruz
 He was a drug addict who lived in New Yolk in the United States of America.
3
 He was a member of gang of spoiled youth.
 One day, Nicky Cruz gave his life to Jesus when he was preached to by a servant of God
called David Wilkerson.
 Life became harder for Cruz when he became a Christian because even his gangsters
started to hate him and wanted to kill him.
Mbaga Tuzinde
 He was born to Katamiza and Bukuwa of Buyonga in Busiro County.
 Tuzinde’s father was a great friend to Mukajanga who later became the chief executioner
of Mwanga.
 Mbaga Tuzinde was one of the Uganda martyrs who were killed at Namugongo.
Rose velt
 Sat
 Stood
 Walking
St. Francis of Assisi (Italian)
 Was born of a rich family
 Lived a lyxurious life
 Had great passion for the poor.
 Gave up all his property to the poor.
 Started living a simple life
 Started the francisian order
Martin Luther King
 Fought for the rights of the black Americans
 Equal rights
 Civil rights activists
 Peaceful means and Civil disobedience
St. Clare of Assis
 She was a follower of St. Francis of Assisi
 She was put in Benedictine nun’s coverts
</passage>

<passage id="lchk_22f2378359f84747b73366e55bae3282" source="P 5 R E Term I, II, III #creative Printers" part="12">
v. The mother of the messiah accepted the task.
NB. Hope should not be put entirely on earthly things e.g. money, houses, good cars and
education. Such things can never bring true happiness and hope.
Jesus was given many names i.e. Messiah, Saviour, Lord, Emmanuel etc because he gave
people hope and set them free from oppression.
“A promise is a debt”.
How God gives hope for internal life.
There is life after death. This is evidenced when Jesus died and resurrected. (Thessalonians
4: 13-14)
25 #CREATIVE PRINTERS 0703745068
The Lord's Prayer
(Traditional)
Our Father, who art in heaven,
Hallowed be thy name;
Thy kingdom come;
Thy will be done;
On earth as it is in heaven.
Give us this day our daily bread.
And forgive us our trespasses,
As we forgive those who trespass
against us.
And lead us not into temptation;
But deliver us from the evil one.
For thine is the kingdom,
The power and the glory,
For ever and ever. Amen.
The Lord's Prayer
(Contemporary)
Our Father in heaven,
Hallowed be your name,
Your kingdom come,
Your will be done,
On earth as in heaven.
Give us today our daily bread.
Forgive us our sins
As we forgive those who sin against
us.
Lead us not into temptation
But deliver us from evil.
For the kingdom, the power,
And the glory is yours
Now and forever. Amen.
</passage>

<passage id="lchk_6f2918a39f984de4839bf0b19bb4b31c" source="Primary Five Tekart Revision R E" part="19">
________________________________________________________________________
Or: Which group of people suffered slavery in Msiri?
________________________________________________________________________
13. Both: How can a good father show love to his children?
________________________________________________________________________
14. Either: Who is the earthly and foster father of Jesus Christ?
________________________________________________________________________
Or: Which prophet was born in Saudi Arabia?
________________________________________________________________________
15. Either: How did Jesus show love to His people?
TEKART LEARNING REVISION SERIES 34
________________________________________________________________________
Or: How did Prophet Muhammad show love to His people?
________________________________________________________________________
16. Either: Why is 3 rd June remembered in Uganda every year?
________________________________________________________________________
Or: Which event marks the end of Saum in Islam?
________________________________________________________________________
17. Either: What lesson do Christians learn from the life of Abraham?
________________________________________________________________________
Or: What lesson do Muslims learn from the life of prophet Ibrahim?
________________________________________________________________________
18. Either: Why did Cain kill Abel?
________________________________________________________________________
Or: Why did Adam’s son kill his brother?
________________________________________________________________________
19. Either: Write the second greatest commandment according to Jesus.
________________________________________________________________________
Or: Write down the greatest pillar in Islam.
________________________________________________________________________
20. Both: How is the judgment day important to human beings?
________________________________________________________________________
SECTION B
21. Either: (a) What do you understand by the term Trinity?
________________________________________________________________________
(b) How are the following persons important in Christianity:
(i) God the father? _____________________________________________________
________________________________________________________________________
(ii) God the son? _______________________________________________________
________________________________________________________________________
TEKART LEARNING REVISION SERIES 35
(iii) God the Holy Spirit? _________________________________________________
________________________________________________________________________
Or: (a) What is Islam? _________________________________________________
________________________________________________________________________
(b) Mention any three pillars of Islam.
(i)______________________________________________________________________
(ii)_____________________________________________________________________
(iii) ____________________________________________________________________
22. Either: (a) How were these people related to Abraham according to the Bible:
(i) Sarah? ____________________________________________________________
(ii) Isaac? _____________________________________________________________
(b) State any two ways in which Abraham showed faith to God.
(i)______________________________________________________________________
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
