# Job ltsk_8e12b97cb54449b9a8a2405db5e69590-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 3 lesson(s) below of week 2 of the Christian Religious Education scheme for Primary Six 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P6: one 40-minute lesson: 3–6 sections; about 16–32 points; worked examples and exam-style points; 6–8 activities.

lessonId=lles_f5811374f87141f28911e1c7a0163c05: lesson 4, Tuesday, 1 period(s), 40 minutes.
  Unit: Friends on the Way (theme: Christians on the way). Lesson: Distinguishing good and bad advice — Distinguishing good and bad advice.
  Objectives: Distinguish good advice from bad advice.

lessonId=lles_022a2fc9328148c38a2a97dc7fc00511: lesson 5, Thursday, 1 period(s), 40 minutes.
  Unit: Friends on the Way (theme: Christians on the way). Lesson: Marriage in Christian life — Marriage in Christian life.
  Objectives: Describe Christian teachings on marriage.

lessonId=lles_b5f6878d98764eb89a26a25d1e3f3808: lesson 6, Friday, 1 period(s), 40 minutes.
  Unit: Friends on the Way (theme: Christians on the way). Lesson: Week 2 review — Friends on the Way.
  Objectives: Review this week's lessons: Distinguishing good and bad advice; Marriage in Christian life
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

<passage id="lchk_ce7cf5d8d98940d2a65961808b128398" source="p.6 r.e lesson notes term III" part="4">
Love never gives up on people, it never stops trusting, it never loses hope or quit – marriage is meant to last forever.
Marriage vows
People who have committed themselves to get married make promises to each other, these promises are called vows.
A promise to love each other till death separates them.
These vows are made before a priest, pastor or reverend as witnesses before God.
Exercise
What is marriage
List down any four characteristics of a happy marriage
Identify one example of situations in marriage with which people need to be patient
How may the failure to produce children create an unhappy marriage
Give one example of marital duties
What is a marriage vow?
Write down any two vows made by the marriage partners.
End of Topic test
Who is a true friend?
Why does one need a friend?
Write down any two ways to show how Jesus showed true friendship to people.
What lessons do we learn from Jesus about true friends
Write down two qualities of a good friend.
How can one distinguish between good and bad advice?
Write down any two examples of bad advices
Define the following terms
Crisis
Advice
How does good advice promote peace?
What does the bible teach us about love in 1Cor. 13.
How can you support a friend who has failed a major examination?
What is marriage?
Write down 2 major qualities of a good marriage partner.
Why do you think marriage are breaking down today?
As a Christian how can you help in solving the above problem?
Write any two qualities of a good marriage partner.
Write down any two biblical readings on marriage from St. Paul in 1 Cor. 7.
DATE
CLASS
SUBJECT
NO OF PUPILS
TIME
THEME: CHRISTIANS ON THE WAY
SUB THEME: CHRISTIAN INVOLVEMENT IN THE WORLD
CONTENT: USING OUR TALENTS TO IMPROVE THE WORLD
Spellings
talents
Abilities
Co-operation
Science
Technology
Humility
Marital
Partners
Patience
Christians should not leave world affairs to non- Christians alone. They have a duty to participate in the affairs of the world at all times. This include; religious, social, economic and political affairs in order to make a contribution in the world we live in.
Talents are natural gifts that God gives us that can also be referred to as Special abilities
Special natural abilities / gifts given to us by God
Examples of talents include:
Singing
Playing musical instruments
Jumping (high)
Playing football
Running fast
Art – making artistic objects (through painting and drawing)
Jesus encouraged us not to neglect our talents trough the different parables he taught e.g as the parable of the talents (mt 25;14 – 27)
Read the story and learn lessons
All Christians should use their talents to benefit themselves and others
Every Christian will give an account of how he used his / her talents
Those who will have used their talents properly will get rewards and those who will have failed will be punished.
Even the little they have will be taken away.
HOW THE ABOVE TALENTS CAN BENEFIT THE WORLD IF USED WELL
They are source of income for both live hood individuals and the government through taxes paid
They are a source of entertainment for people to kill boredom
They promote unity when people come together to be entertained e.g football which binds nations and the whole world.
The educate people through sending teaching and advisory messages to people on topics like Aids, social well being.
Exercise
Why do we have different abilities?
Why did the 2 servants get profits
Why didn’t the third servant get any profit?
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
