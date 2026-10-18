# Job ltsk_abd869d0b5dc4c10b398b10a72635aec-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 3 lesson(s) below of week 1 of the Christian Religious Education scheme for Primary Three 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P3: one 40-minute lesson: 2–3 ideas; about 10–20 points; simple meanings and worked examples; 4–6 activities.

lessonId=lles_99f3857335d24c87b7c7d8b415a1cb90: lesson 1, Tuesday, 1 period(s), 40 minutes.
  Unit: Forgiveness and Acceptance (theme: Christians Grow in Jesus). Lesson: Meaning of forgiveness — Forgiveness and acceptance.
  Objectives: By the end of the lesson, the learner should be able to explain the meaning of forgiveness and identify words used to seek forgiveness.

lessonId=lles_33a4ff57d0324262a7b7546c0a0a8ea6: lesson 2, Thursday, 1 period(s), 40 minutes.
  Unit: Forgiveness and Acceptance (theme: Christians Grow in Jesus). Lesson: Traditional ways of encouraging forgiveness — Forgiveness and acceptance.
  Objectives: By the end of the lesson, the learner should be able to name traditional ways of encouraging forgiveness, including apologising and reconciliation.

lessonId=lles_499d79b6714f4f6db4f12a1307ebeab5: lesson 3, Friday, 1 period(s), 40 minutes.
  Unit: Forgiveness and Acceptance (theme: Christians Grow in Jesus). Lesson: Week 1 review — Forgiveness and Acceptance.
  Objectives: Review this week's lessons: Meaning of forgiveness; Traditional ways of encouraging forgiveness
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
<passage id="lchk_8a908ba4886e4d62ac30811dbe54f9e4" source="NCDC P3 Thematic Curr 21 November" part="50">
• | Jesus’ example of prayer and | • | Identifying different situations which require | • | Interpersonal relationship | • | Appreciation
teaching | prayer and teaching | • | Effective communication | • | Forgiveness
• | When, where and how to pray | • | Talking about different occasions on which | • | Creative thinking | • | Faithfulness
• | The Lord’s prayer | Jesus prayed and taught | • | Critical thinking | • | Unity
• | Praying for others | • | Talking about when, where and how to pray | • | Problem-solving | • | Cooperation

Mark 1: 35 | • | Reciting the Lord’s Prayer | • | Obedience
Mathew 6: 9-13 | • | Asking and answering questions
Luke 22: 32 | • | Singing songs about prayer and teaching
John 17: 20-21

Assessment Guidelines (Weeks 10-12)
• Talk about the importance of different personal abilities.
• Sing songs about different personal abilities.
• Talk about the different ways in which family members resemble.
• Talk about different occasions on which Jesus prayed and taught.
• Recite the Lord’s Prayer.

TERM III
Theme: | Christians Grow in Jesus Weeks 1-3:
Learning Outcome: The child appreciates and practices the value of tolerance and forgiveness for maintaining good relationship with others in society.
Sub-theme | Content | Competences | Life skills | Values
Forgiveness and | • Traditional ways of encouraging | • Talking about traditional ways of encouraging | • Critical thinking | • Care
Acceptance | forgiveness | forgiveness | • Creative thinking | • Acceptance
Mathew 18: 15-16 | • Talking about the importance of forgiveness | • Friendship formation | • Tolerance
Luke 17: 23 | • Telling and retelling stories | • Effective communication | • Kindness
• Ways of forgiveness | • Asking and answering questions | • Problem-solving | • Responsibility
- wrong doings that required | • Singing songs about forgiveness | • Non-violent conflict
forgiveness | • Reciting the gospel message Luke 17: 23 | resolution

• | Resolving differences without | • | Identifying wrong doings which require forgiveness | • | Friendship formation | • | Acceptance
violence | • | Talking about how to resolve differences without | • | Empathy | • | Tolerance
• | Desire for forgiveness | violence | • | Self-awareness | • | Unity
Genesis 27: 30-36 | • | Telling and retelling stories | • | Non-violent conflict | • | Concern
Genesis 33: 1-11 | • | Asking and answering questions | resolution | • | Friendliness
Mathew 18: 15-35 | • | Role-playing forgives | • | Coping with stress | • | Responsibility
Genesis 37: 25-28 | • | Reciting a memory verse | • | Coping with emotions
Luke 15: 11-24 | Numbers 5:7
Mathew 6: 12
Mathew 5: 38-42
• | Acceptance | • | Identifying causes of conflicts | • | Critical thinking | • | Acceptance
- need to accept others | • | Telling and retelling the story of Joseph and his | • | Coping with emotions | • | Forgiveness
- the joy of good relationship | brothers | • | Coping with stress | • | Tolerance
- the help of the Holy Spirit in | • | Talking about ways of accepting and being tolerant | • | Creative thinking | • | Friendliness
forgiving others | of others differences | • | Love
• | Asking and answering questions | • | Concern

Assessment Guidelines (Weeks 1-3)
• Talk about traditional ways of encouraging forgiveness.
• Talk about the importance of forgiveness.
• Talk about how to resolve conflict without violence.
• Role play forgiveness.
• Identify causes of conflicts.
</passage>

<passage id="lchk_62708a3a375147ff995bcb0b55044f5c" source="P 3 C R E Term Three" part="1">
For more lesson notes, visit www.freshteacheruganda.com
PRIMARY THREE
RELIGIOUS EDUCATION
LESSON NOTES
TERM III
WEEK1 : Lesson 1
FORGIVENESS AND ACCEPTANCE
1. What is forgiveness?
Forgiveness means stopping being angry with some body for something he/she has done
wrong.
For more lesson notes, visit www.freshteacheruganda.com
2. If you want somebody to stop being angry with you, say, “please forgive me” or “please, am
sorry.”
3. Traditional ways of encouraging forgiveness
• Paying a fine i.e. a cock, goat etc.
• Sharing a meal.
• Saying sorry to a person wronged.
• Using another person (mediator) to reconcile the two people friends again.
• Re-accepting the offender into the family.
4. Draw, name and colour any one traditional way of encouraging forgiveness
WEEK1 : Lesson 2
1. Reasons why we need to forgive
We need to forgive others because:
• God also forgives us
• Everybody makes mistakes
• Forgiveness helps us to live and work together happily
• Forgiveness prevents bad out comes like hatred, fighting etc.
• It serves as a lesson to the person forgiven to also forgive others who wrong him/her.
• Jesus showed us an example when he forgave those who hated him.
2. Examples of people who forgave one another in the Bible
• Jacob and Esau(Genesis33:1-11)
• Joseph and his brothers(Genesis45:1-5)
For more lesson notes, visit www.freshteacheruganda.com
• King Darius and Daniel(Daniel 6:13-23)
• The prodigal son and his father(Luke 15:11-31)
WEEK2 : Lesson 1
Resolving misunderstanding without violence
1. To resolve means to find a solution or an answer to a problem.
2. The word violence means an act of using physical force e.g. fighting.
3. How Jesus teaches about resolving misunderstanding without violence
( Matthew 18:15-16)
Steps :
• Solve it in private with a person who has wronged you.
• If the person does not listen, take/call other two people.
• If he/she does not listen to the two, take it to the church (group).
• If he/she does not listen to the church (group) take the case to LC or court.
WEEK2 : Lesson 2
1. Causes of misunderstandings/violence
• Physical differences e.g. height, colour and body shape.
• Religious differences e.g. some are Catholics, Protestants, Pentecostals etc.
• Cultural differences e.g. Buganda, Acholi, Karamajong.
• Racial differences e.g. the black and white.
• Home differences e.g. the rich and the poor.
• Differences in education.
2. We are all God’s children regardless of our differences.
3. We should accept and be tolerant to other peoples’ differences to live peacefully.
For more lesson notes, visit www.freshteacheruganda.com
4. Ways of accepting and tolera ting other peoples’ differences
• Loving and caring for one another.
• Over looking our differences
• Praying together
• Sharing time of sorrow and joy
• Knowing that we are all God’s children
WEEK3 : Lesson 1
TOPICAL TEST
1. What should you do after annoying a friend?
2. Name any two traditional ways of encouraging forgiveness.
3. Give two reasons why we should forgive others.
4. What lesson do we learn from the parable of the lost son?
5. Name one group of people who forgave one another.
6. Mention any two differences that exist among people.
7. Which prophet was thrown in the lion’s den?
WEEK3 : Lesson 2
TREATING OTHERS FAIRLY
1. Being fair means treating each person equally.
2. Unfairness is the opposite of fairness.
For more lesson notes, visit www.freshteacheruganda.com
2. Common examples of fair behaviour
</passage>

<passage id="lchk_9e957d59f08b43d1b70e97ab9a55ec26" source="P.3 R.E TERM II1 NOTES" part="1">
PRIMARY THREE
RELIGIOUS
EDUCATION
LESSON NOTES
FOR
TERM 3
1
WEEK 2 : Lesson 1
spellings
1. Nazareth
2. Jordan
3. Ararat
4. Red sea
5. Canaan
FORGIVENESS AND ACCEPTANCE
1. What is forgiveness?
Forgiveness is to stop being angry with some body for
something he/she has done wrong.
2. To ask for forgiveness we say, “Please forgive me” or “please,
am sorry.”
3. We should forgive one another and also ask God to forgive us.
4. Traditional ways of encouraging forgiveness
 Paying a fine i.e. a cock, goat etc.
 Sharing a meal.
 Saying sorry to a person wronged.
 Using a middleman (mediator) to reconcile the two people.
Activity
1. Explain the meaning of the word forgiveness.
2. Emma poured Suzan’s juice accidentally. What should these
two do to become friends again?
a.Emma_____________________________
b.Suzan______________________________
3. Draw, name and colour any one way traditional way of
forgiveness.
WEEK 2 : Lesson 2
spellings
1. forgiveness
2
2. traditional
3. sorry
4. reconcile
5. angry
1. Reasons why we need to forgive
We need to forgive others because:
 God also forgives us.
 Everybody makes mistakes.
 It helps us to live and work together happily.
 It prevents bad out comes like hatred, fighting etc.
 It acts as a lesson to those forgiven to also forgive others.
2. Jesus showed us an example when he forgave those who hated
him.
3. People who forgave one another in the Bible
 Jacob and Esau(Genesis33:1-11)
 Joseph and his brothers(Genesis45:1-5)
 King Darius and Daniel(Daniel 6:13-23)
 The prodigal son and his father(Luke 15:11-31)
Activity
1. Give two reasons why we should forgive one another.
2. What is sin?
3. Name any two examples of sin.
4. What should we do when we sin?
5. State any two dangers of sin.
6. Which parable teaches us to forgive one another?
WEEK 3 : Lesson 1
spellings
1. forgive
2. repent
3. mistake
4. hate
3
5. hatred
Resolving misunderstanding without violence
1. To resolve means to find a solution or an answer to a problem.
2. Violence means the use of physical force e.g. fighting.
3. Jesus’ teachings about resolving misunderstandings.
Matthew 18:15-16
Steps :
 Solve case privately with your bother/sister.
 If the he/she does not listen, take/call other two people.
 If he/she does not listen to the two, take it to the church
(group).
 If he/she does not listen to the church (group), take the case
to LC or court.
Activity
1. Define the term violence.
2. What should you do after annoying a friend?
3. What should you do if somebody does wrong to you but
doesn’t apologize?
WEEK 3 : Lesson 2
spellings
1. violence
2. misunderstanding
3. resolve
4. annoy
5. friend
1. Causes of misunderstandings/violence
a) Physical differences
-That is in height, colour and body shape.
b) Religious differences
-Some are Catholics, Protestants etc.
c) Cultural differences
-Some are Baganda, Acholi, Karamajong etc.
4
d) Racial differences
- Some are black, white coloured etc.
e) Home differences
- Some are rich and others are poor.
f) Differences in education .
- The educated and uneducated.
2. We are all God’s children regardless of our differences.
3. We should accept our differences to live peacefully.
4. Ways of accepting and tolerating our differences
 Loving and caring for one another.
 Over looking our differences.
 Praying together.
 Sharing times of sorrow and joy.
 Knowing that we are all God’s children.
Activity
1. Mention any two differences that exist among people.
</passage>

<passage id="lchk_c2868e5b48194f86bef866f029d1d96f" source="NCDC P.3 teachers guide Book" part="13">
recording until the end of term. Learners can now use the recorded data for the first three weeks to come up with a
picture graph.

As in P1 and P2, a child-centred approach should include opportunities for:
x exposition by the teacher;
x discussion between teacher and learners and between learners themselves;
x appropriate practical work and recording;
x consolidation and practice of fundamental skills;
x problem-solving, including the application of Mathematical skills to everyday situations.

Exposition by the teacher
This means explanation by the teacher – often using the chalkboard. This is a fundamental part of most
Mathematics lessons. However, it is important that it does not dominate your lessons. You should allow the
learners to participate in the other activities given below. Make sure your explanation is clear, delivered in a lively
way and that you use effective body language.

Discussion
Learners must be given opportunities to talk about Mathematics – to explain and discuss their results. They should
feel confident in using their own language to discuss with you and with their peers. Let them discuss the
challenges that they find when solving mathematical problems. Encourage them to ask questions.

Guide them to understand that Mathematics is a precise and accurate subject. In Mathematics there is no place for
the words “perhaps” or “probably”. For this reason, it is important that children are encouraged to use
mathematical language as often as possible. Encourage learners to work in groups and report back. This gives the
learner an opportunity to share with others.
Practical work
There should be frequent opportunities for appropriate practical work. In many of the themes in P3, examples of
practical activities are suggested.

Practice
Every child needs to practice the skills they have recently learned and to consolidate the ones they already have.
The amount of practice that is needed will depend on the child and you must be aware of the different needs of

your learners. While some things in Mathematics certainly need to be learned by heart, it should never be
necessary to commit things to memory without seeking to develop a proper understanding of the mathematical
concepts to which they relate.

Problem-solving
The ability to solve problems is at the heart of Mathematics. You need to help children understand and apply the
concepts and skills they have learned and to know when and how to use them to solve problems. It is of no use for
a child being able to recite their multiplication tables but not knowing when and how to use them.

“If I had known it was an addition sum I could have done it,” is a common remark heard in primary classes. If you
hear it, you should concentrate on developing problem-solving skills.

A problem is usually stated in words, given orally or written down. To solve it, the child will first have to
understand what it means Mathematically, i.e. translate it into a Mathematics sum. Then the Mathematics sum has
to be solved. Finally the child has to interpret the answer.

Original | Î translate | Î | Mathematics
Problem | sum

Ð

Solve

Ð

Answer to | Í interpret | Í | answer to sum
Original
Problem

NB
x | Original problem is always in words.
x | SUM this is simple mathematical problem that involves calculating the problem.
x | Mathematics and sum means problems that involve calculations.
</passage>

<passage id="lchk_63fa3d33432a432f86fa345f56da871d" source="NCDC CRE P.3 TEACHERS RESOURCE BOOK" part="61">
loss of love, etc.
 | Talk about the need to avoid wrongdoing.

PRIMARY THREE | TEACHERS’ RESOURCE BOOK

WEEK 2

LESSON 1: Ways of Seeking Forgiveness
Reference: Bible—Luke 15:11-21
Key message: God wants me to ask for forgiveness when I do wrong.
Key terms: Forgiveness – pardon

COMPETENCES
The learner:
i) | identifies ways in which he/she should be forgiven.
ii) | tells ways in which Jesus Christ wants him/her to forgive others.

Life skills | Indicators
Non-violent conflict | - | Using appropriate language
resolution | - | Assisting others to understand the problem
- | Resolving issues without fighting
- | Being a peacemaker/moderator/intermediator
- | Accepting defeat
- | Coping with stress
Problem solving | - | Taking the right decision
- | Finding different ways of solving problems
without using violence

Values
 Appreciating the need to forgive others
 Being honest
 Being concerned
 Being a peacemaker
Methods: Storytelling, recitation
Instructional materials: Bible, a chart showing the prodigal son

CHRISTIAN RELIGIOUS EDUCATION

Suggested Teacher’s Activities | Suggested Learner’s Activities
 | Guiding the learners to share |  | Sharing experience of what he/she did
experiences of what they did | after doing something wrong.
after doing something wrong |  | Listening to the story and answering
 | Telling the learners, a Bible | questions
story in Luke 15:11-21, and |  | Mentioning ways of seeking forgiveness
asking questions | following the story of the lost son
 | Asking the learners to mention |  | Reciting Luke 15: 21; “Father I have
ways of seeking forgiveness | sinned against God and against you. I am
 | Asking learners to recite Luke | no longer fit to be called your son.”
15:21

Guidance on Assessment
Assess the learner on:
 telling what he/she does after doing something wrong.
 mentioning the lessons learnt from the story of the lost son.
Sample Activity
Saying a prayer asking God to help him/her to always ask for forgiveness when in the
wrong.
Notes for the Teacher
 How did the lost son seek forgiveness from his father?
- accepted his mistake
- went back to the father whom he had wronged
- asked for forgiveness
- humbled himself before his father
 Encourage the learners to ask for forgives when they do something wrong.
 Share with the learners how they can forgive someone who has wronged them.
- Telling them that you have forgiven them
- Sharing with him/her
- Embracing the offended person
- Giving gifts
 If time allows, let the learners role-play the prodigal son.

PRIMARY THREE | TEACHERS’ RESOURCE BOOK

LESSON 2: Importance of Forgiveness

Reference: Bible—Luke 15:21-32
Key message: I need to forgive others so that God can bless me.
Key term: Prodigal – a person who spends money in a recklessly extravagant way

COMPETENCES
The learner:
i) | identifies the importance of forgiveness.
ii) | forgives others.

Life skills | Indicators
Coping with stress | - Forgiving others, being patient, accepting
advice
Interpersonal relationship | - Forgiving others, interacting freely with
others, sharing with others, knowing how to
relate with different people, reacting
appropriately in difficult/challenging
situations

Values: Appreciating the need to forgive others
Methods: Guided discovery, storytelling, role-play
Instructional materials: A chart showing a father welcoming the prodigal son,
costumes for the role-play

Suggested Teacher’s Activities | Suggested Learner’s activities
</passage>

<passage id="lchk_b5f341e6fe9549bdac6a266ac6c32e06" source="NCDC CRE P.3 TEACHERS RESOURCE BOOK" part="67">
b) What would you do to the brothers if you were Joseph?
- | I would forgive them/ Pray to God to forgive them.

CHRISTIAN RELIGIOUS EDUCATION

WEEK 5

SUB-THEME: Treating others fairly
Learning Outcome
The learner tells the importance of the concept of fairness and forgiveness in
different daily life situations.

LESSON 1: Importance of Fair Behaviour
Reference: Bible—Matthew 10:42 & Luke 3:10-14
Key message: God rewards me when I treat others fairly.
Key term: Importance – something of great value or significance

COMPETENCES
The learners:
i) mentions the importance of being fair to others
ii) practises being fair to others

Life Skills | Indicators
 | Friendship formation |  | Sharing with others
 | Resolving issues with fairness
 | Non-violent conflict |  | Using appropriate language
resolution |  | Assisting others to understand issues

Values
 Sharing with others
 Appreciating the importance of being fair
 Loving others
Methods: Recitation, guided discovery
Instructional material: Items to be given out

PRIMARY THREE | TEACHERS’ RESOURCE BOOK

Suggested Teacher’s Activities | Suggested Learner’s Activities
 | Guiding the learners to share |  | Sharing experiences in which he/she
experiences when they were thanked | was thanked for being fair
for being fair to others |  | Listening to the message from the
 | Sharing the message according to | Bible and answering questions
Luke 3:10-14, and asking questions |  | Sharing the lessons learnt
 | Guiding the learners to share the |  | Reciting Matthew 10:42; “You can be
lessons learnt | sure that whoever gives a drink of cold
 | Asking the learners to recite Matthew | water to one of the least of my
10:42 | followers will certainly receive a
reward”

Guidance on Assessment
Assess the learner on identifying the importance of fair behaviour.

Sample Activity
Singing a song:
Whatsoever you do to the least of my brothers that you do unto me
When I was hungry you gave me to eat
When I was thirsty you gave me to drink
Now enter into the kingdom of my father
(Ref: Christians Grow in Jesus Christ. P.3. Teacher’s Guide, Page 117)

Notes for the Teacher
 The learners share experiences of when they were fair to others and where
rewarded. For example, when they helped a sick friend and the friend’s parents
gave them eats, money and appreciated them very much.
 Ask the learners: What does Matthew 10:42 teach us?
- When we are kind to others, God rewards us.
- God blesses us when we share what we have with others.
- God loves cheerful givers.

CHRISTIAN RELIGIOUS EDUCATION

LESSON 2: Effects of Unfair Behaviour
Reference: Bible—Genesis 3:14-24
Key message: Unfair behaviour may lead me to live a painful life.
Key terms:
 Serpent – snake symbolising Satan
 Cursed – brought bad luck upon by using magic words
 Bear – to be able to accept and deal with something unpleasant
 Wanderer – one who moves from place to place without any clear purpose

COMPETENCES
The learner:
i) | explains the effect of Eve and Adam’s behaviour.
ii) | shows fairness to avoid suffering in life.

Life Skills | Indicators
 | Friendship formation |  | Sharing with others fairy
 | Playing with other fairly
 | Resolving issues with fairness
 | Decision making |  | Using appropriate language
 | Assisting others to understand issues
 | Accepting defeat

Values
 Sharing with others fairly
 Appreciating others fairly
 Loving others fairly
Methods: Storytelling, guided discovery
</passage>

<passage id="lchk_3df8544be8d74af582c42889de42aa9d" source="A.JJEB.IRE. P 3. 2019" part="1">
P235/3
ISLAMIC
RELIGIOUS
EDUCATION
Paper 3
HISTORY OF ISLAM
AUGUST, 2019
2
½ hours
JINJA JOINT EXAMINATIONS BOARD
Uganda Advanced Certificate of Education
MOCK EXAMINATIONS – AUGUST, 2019
ISLAMIC RELIGIOUS EDUCATION
HISTORY OF ISLAM
Paper 3
2 hours 30 minutes
INSTRUCTIONS TO CANDIDATES :
Answer any FOUR
questions.
ALL questions carry equal marks.
© 2019 Jinja Joint Examinations Board
Turn Over
_________________________________________________________________________________________________
1. Examine the prevailing way of life during the pre Islamic Arabian era
that necessitated the
coming of Prophet Muhammad (p b u h). (25
marks)
2. (a) Describe the social boycott of Banu Hashim. (13
marks)
(b) Explain the role of Lady Khadija in the Prophet`s (saw) mission.
(12 marks)
3. (a) Give an account of the battle of the camel. (17
marks)
(b) What were the consequences of this battle? (7 marks)
4. (a) Why was Yazid bin Muawiyah opposed by the Muslims? (13
marks)
b) Which strategies did he use in an attempt to silence the prevailing
problems?
(12
marks)
5. Discuss the methods used by the Umayyad rulers in administration
of the Islamic state.
(25marks)
6. ( a) Examine the factors that led to the rise of internal conflicts
during Al-Ma’mun’s
reign. (13
marks)
(b) Explain the significance of Al-Ma’mun’s character and
personality in overcoming
_________________________________________________________________________________________________
© 2019 Jinja Joint Examinations Board
End
_________________________________________________________________________________________________
2
such conflicts. (12
marks)
7. Explain the contribution of the Abbasids to intellectual development
during their
existence. (25
marks)
8. How far did the vastness of the Abbasid dynasty contribute to the
collapse of the dynasty?
(25 marks)
9. Describe the political and social life in Egypt under the Fatimid rule.
(25 marks)
10. “The excellent preparation for the invasion of Egypt was primarily
responsible for the rise of
the Fatimids.’’ Discuss
11. Account for the rise of the Safavids to power. (25
marks)
12. (a) Describe the political organization of the ottoman empire.
(12 marks)
(b) Analyze
the factors behind the downfall of this empire. (12
marks)
_________________________________________________________________________________________________
© 2019 Jinja Joint Examinations Board
End
_________________________________________________________________________________________________
3
</passage>

<passage id="lchk_9c9307d24eba4110b8493160dcb29021" source="A.JJEB.IRE. P 3. 2020" part="1">
P235/3
ISLAMIC
RELIGIOUS
EDUCATION
Paper 3
HISTORY OF ISLAM
DECEMBER, 2020
2
½ hours
JINJA JOINT EXAMINATIONS BOARD
Uganda Advanced Certificate of Education
MOCK EXAMINATIONS – DECEMBER, 2020
ISLAMIC RELIGIOUS EDUCATION
HISTORY OF ISLAM
Paper 3
2 hours 30 minutes
INSTRUCTIONS TO CANDIDATES :
Answer any FOUR
questions.
ALL questions carry equal marks.
© 2020 Jinja Joint Examinations Board
Turn Over
_________________________________________________________________________________________________
1. (a) Analyse the political life of the arabs during Jahiriyya period
(b) In what ways was their political system oppressive?
2. Account Prophet Muhammad’s (PBUH) Expulsion of the Jewish clans
from Medina
3. Why did unrest emerge during Ali’s reign?.
4. Assess the Muawiyah’s contribution to the establishment of the
Ummayad dynasty.
5. “Ummayyad rulers valued the work of the military as well as religious
institutions. Assess the validity of the statement.
6. (a) Discuss the challenges faced by caliph Abu Jaffar al – Mansur.
(b) Explain the role of the military in consolidating peace during
his reign.
7. Examine the following aspects of life under the Abbasids.
(a) The political organization and
(b) Scholarship learning.
8. Account for the delay in the establishment of the Fatimid rule despite
the early development of their sect.
9. Discuss the political organization of fatimids.
(a) Explain the weakness of the Fatimid rulers.
(b) Explain the weakness of the Fatimid rulers.
10. Assess the impact of the anti-Islamic movement on the Muslim
world between the 11 th to the 13 th centuries
11. Account for the rise of the Safavids to power.
12. Examine the contributions of Sulaiman the magnificent to the
prosperity of the Ottoman Empire.
_________________________________________________________________________________________________
© 2020 Jinja Joint Examinations Board
End
_________________________________________________________________________________________________
2
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
