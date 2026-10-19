# Job ltsk_47ee2b40223e43a785eb371dd62e928d-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 6 lesson(s) below of week 2 of the English scheme for Primary Four 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P4: one 40-minute lesson: 2–4 sections; about 12–24 points; meanings, examples and uses; 5–7 activities.

lessonId=lles_a1389d206da249cebbb742b03b620d79: lesson 7, Monday, 1 period(s), 40 minutes.
  Unit: Time and expression of the future — week 2 (theme: Expression of the future and Time). Lesson: Using for — Using for.
  Objectives: By the end of the lesson, learners should be able to use for to express duration.

lessonId=lles_ef97d1dc02904f08a4e724c4aa5f279a: lesson 8, Tuesday, 1 period(s), 40 minutes.
  Unit: Time and expression of the future — week 2 (theme: Expression of the future and Time). Lesson: Using before — Using before.
  Objectives: By the end of the lesson, learners should be able to use before to order actions.

lessonId=lles_7a85983cf8674af9b5f7fb617bc50a6b: lesson 9, Wednesday, 1 period(s), 40 minutes.
  Unit: Time and expression of the future — week 2 (theme: Expression of the future and Time). Lesson: Using after — Using after.
  Objectives: By the end of the lesson, learners should be able to join actions using after.

lessonId=lles_6d6d944a939e4dd992274981c5b43b9c: lesson 10, Thursday, 1 period(s), 40 minutes.
  Unit: Time and expression of the future — week 2 (theme: Expression of the future and Time). Lesson: Reading: Namata’s work plan — Reading: Namata’s work plan.
  Objectives: By the end of the lesson, learners should be able to interpret a weekly work plan and answer in full sentences.

lessonId=lles_f159b2f7f0bc40f9861254e99aa84c88: lesson 11, Friday, 1 period(s), 40 minutes.
  Unit: Time and expression of the future — week 2 (theme: Expression of the future and Time). Lesson: Reading: Amanya’s diary — Reading: Amanya’s diary.
  Objectives: By the end of the lesson, learners should be able to read a diary and identify dates and events.

lessonId=lles_89ae109bbfd045b882c32a6ab644f787: lesson 12, Friday, 1 period(s), 40 minutes.
  Unit: Time and expression of the future — week 2 (theme: Expression of the future and Time). Lesson: Reading: Mukaga’s daily plan — Reading: Mukaga’s daily plan.
  Objectives: By the end of the lesson, learners should be able to read a timed plan and answer questions.

Write, using ONLY the passages below. Passages from "NCDC" documents are the official base for what to teach; NCDC lower-primary thematic curricula put every learning area in columns separated by " | ": use only the English column.
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
<passage id="lchk_52d32128a6914ca8ae03917f25c7b78f" source="P 4 Grammar Scheme Term III" part="1">
P.4 ENGLISH SCHEME (GRAMMAR) TERM III
WK PD TOPIC ASPECT SKILLS CONTENT COMPETENCE METHODS ACTIVITIES T/L AIDS REF. REM
1 1 Expression of
the future
Grammar Listening
Speaking
Reading
Writing
Use of “if” and “unless”
If and unless are called conditional
clauses because a certain condition
is supposed or imagined to be fulfilled
in order for an action to take place.
We commonly use a future simple
tense in the main clause and the
present simple tense in the If clause.
Examples
If I get money, I will buy a new radio
Mother will punish us if we don’t
complete the work.
The learner;
Reads the given
sentences
correctly
Uses if and
unless in
sentences
correctly
Explanation
Guided
discovery
Discussion
Reading the
sentences
Using the
words in the
sentences
Answering the
questions
correctly
Chalk board
illustration
2 Expression of
the future
Grammar Listening
Speaking
Reading
Writing
Use of “unless”
Examples
If it shines, the crops will dry
Unless it shines, the crops will dry.
Unless he listens to his teacher, he
won’t learn.
The learner;
Reads the given
sentences
correctly
Uses if and
unless in
sentences
correctly
Explanation
Guided
discovery
Discussion
Reading the
sentences
Using the
words in the
sentences
Answering the
questions
correctly
Chalk board
illustration
3 Expression of
the future
Grammar Listening
Speaking
Reading
Writing
Since and for
Since is used when a point of time
from which an action began is given.
The present perfect continuous
tense is always used when an action
is still existing
Examples
The boy has been crying since
9:00am
The baby has cried for an hour.
The pupils
Read the given
sentences
correctly
Use “since” in
sentences
correctly
Explanation
Discussion
Guided
discovery
Reading the
given
sentences
Constructing
sentences
using since
Chalkboard
illustration
Chalkboard illustration
MK. Precise English Grammar page
125 and detailed English Grammar
2 1
Expression of
the future
Grammar Listening
Speaking
Reading
Writing
Using “for”
For is used when the length of time
(duration) an action has spent or
spent in existence is shown
Examples
They have played for four hours
I have not seen my mother for two
years.
Joseph has sat there for five hours
The pupil,
Reads the
sentence
correctly
Uses “for’ in
meaningful
sentences
Discussion
Explanation
Question and
answer
Reading the
sentences
Using “for” in
sentences
Chalk bard
illustration
Detailed English Grammar book 2 pages 68 – 70
2 Before and after using “before”
Examples
I wash my hands before eating food
She will do her homework before
going to play
Before going to pray, Musa will tale
breakfast
The pupil;
Reads the
sentences
correctly
Uses “before” in
meaningful
sentences
3 Using “after”
This is used when one action has
happened after the other
Note
Use past perfect for 1 st action
Past simple for 2 nd action
Examples
Tom finished his homework. He went
to sleep
After Tom had finished his
homework, he went to sleep.
Tom went to sleep after he had
finished his homework
The pupil;
Reads the
sentences
correctly
Uses “before” in
meaningful
sentences
Discussion
Explanation
Question and
answer
Reading the
sentences
Using “for” in
sentences
Chalk board
illustration
Detailed English Grammar book 2 pages 68 – 70
3 1 Active and
passive voice
Grammar Listening
Speaking
Reading
Writing
The present simple tense
When changing from active to
passive voice we use
Object + (is, are, am) + (past
participle of the main parts)
The pupil;
Reads the
sentences
correctly
Changes
sentences from
</passage>

<passage id="lchk_f716af72c8cc4a5a82acd048b8952822" source="P 4 Composition AND Comprehension Scheme Term III" part="1">
P.4 ENGLISH SCHEME COMPO AND COMPRE TERM III
WK PD TOPIC ASPECT SKILLS CONTENT COMPETENCE METHODS ACTIVITIES L/SKILLS AIDS T/AID REF REM
1 1 Time
Composition
Listening
Speaking
Reading
Writing
Vocabulary
Learning the meaning of these words
tomorrow
next day
next week
shall not
will not
arrive
reach
library
lend
borrow
The learner;
Pronounces,
reads the
words, spells
the new words
and uses the
new words in
sentences
Guided
discussion
Question and
answer
Brain
storming
Pronouncin
g, reading
and
spelling the
new words
Using given
words in
sentences
Effective
communication
Self esteem
Co-operation
Effective
communication
Dictionary , chart esteem, co-operation and effective communication
St. Bernard’s English book 4 page 125
2 Time
Composition
Listening
Speaking
Reading
Writing
Structures
Using will / shall .......
Examples
Jane will go to school tomorrow
We shall not go to the market next
week
The learner;
Reads given
sentences,
forms own
sentences
using the given
structures ,
joins the given
sentences
using the given
structures
Guided
discussion
Question and
answer
Brain
storming
Reading
given
sentences
Forming
own
sentences
Joining
sentences
Effective
communication
Self esteem
Co-operation
Effective
communication
3 Time
Composition
Listening
Speaking
Reading
Writing
Conversation
We shall miss / Mr. Guma
Read the conversation and
answer the questions in full
sentences
The learner;
Reads the
passage
correctly and
answer
questions
about it in full
sentences
Guided
discussion
Question and
answer
Brain
storming
Reading
the
conversatio
n correctly
Answering
the
questions
about the
conversatio
n
Effective
communication
Self esteem
Co-operation
Effective
communication
2 1 Time
Comprehension
Listening
Speaking
Reading
Writing
Passage
My family
Read the passage and answer
questions in full sentences
The learner;
Reads the
passage
correctly and
answers
questions
about it in full
sentences
Guided
discussion
Question and
answer
Brain
storming
Reading
the
passage
correctly
Answering
questions
about the
passage in
full
sentences
Effective
communication
Self esteem
Co-operation
Effective
communication
Dictionary , chart esteem, co-operation and
effective communication
St. Bernard’s English book 4 page 125
2 Time
Comprehension
Listening
Speaking
Reading
Writing
Keeping a diary
Study Amanya’s Diary and answer
the questions in full sentences
The learner;
Studies the
diary carefully
and answer
the questions
about it in full
sentences
Questions
and answer
Guided
discussion
Brain
storming
Question and
answer
technique
Studying
the diary
answering
questions
in full
sentences
Self esteem,
Pull out
St. Bernard English book 4 page 133
3 Time
Comprehension
Listening
Speaking
Reading
Writing
Class time table for P.4
Study the time table and answer the
given written questions
The learner;
Studies the
time table
carefully and
answers the
questions in
full sentences
Questions
and answer
Guided
discussion
Brain
storming
Question and
answer
technique
Studying
the time
table
Answering
the
questions
Effect
communication
Text book and class time table
The Winner English book 4 page 102
3 1 Time
Comprehension
Listening
Speaking
Reading
Writing
Keeping a diary
Vocabulary
diary, read, months, text book, day,
year, date, borrow, lend, revise, time
table
The learner;
Reads, spells
and
pronounces
words
correctly,
forms
sentences
correctly and
use the words
in sentences
correctly
Questions
and answer
Guided
discussion
Brain
storming
Question and
answer
technique
Reading
spelling
</passage>

<passage id="lchk_7685308ccbde482cb6da1bdbb89736ea" source="P 4 ENG & SST Lesson Notes Term III 2023" part="1">
Page | 1
PRIMARY FOUR ENGLISH LESSON NOTES FOR
TERM THREE
WEEK ONE
TOPIC 1: EXPRESSION OF THE FUTURE
Topic 1 a: Expression of the Future
Vocabulary
1. tomorrow 5. shall not
2. next week 6. will not
3. next month 7. shan’t
4. next year 8. won’t
Activity 2
Use the vocabulary above to construct meaningful sentences.
Activity 3.
Look at the table below and write five sentences.
I
We
She
They
shall
shall not
will
will not
play with my friends.
go with him.
go on holiday.
swim in the lake.
disturb you today.
For example.
(a) We shall not play with him.
(b) We shall go with him
Activity 4.
Read the passage and answer the questions about it in full sentences
AKOT’S PLAN TO GO TO THE ZOO
Next Sunday,my sister Joyce and I will visit the Zoo. We shall see many
animals and birds.We shall see lions,chimpanzees and monkeys.But we shall
not see the elephants because they are not in the Zoo.
On our way to the zoo,we shall eat some pancakes and drink soda. We shall
take some bananas for chimpanzees and the monkeys.
Page | 2
We shall come back home in the evening when we are very tired.We shall bathe
with warm water.After that, we shall go to bed to rest.We shall then be able to
wake up early and go to school the next day.
Questions
1.When will Akot go to the zoo?
2.With whom will Akot go to the zoo?
3.What will they eat on their way to the zoo?
4.Why will they not see the elephants at the zoo?
5.What will they take for the chimpanzees and the monkeys?
6.Will they see lions at the zoo?
7.How many people will go to the zoo next Sunday?
Activity 5 Written Work.
Study Namata’s work plan for next week and answer questions that follow
in full.
Sunday  She will go to church.
 She will feed the rabbits at 10:00 a.m.
Monday  She will clean the kennel.
Tuesday  She will read a novel.
Wednesday  She will go for P.E at school.
Thursday  She will visit aunt Suzan after school.
 She will wash her P.E uniform.
Friday  She will start on her mixed exercise.
Saturday  She will go to the beach with her parents.
Questions:-
1. Who will feed the rabbits?
2. On which day will the rabbits be fed?
3. What will Namata do on Monday?
4. At what time will Namata feed the rabbits?
5. What is a kennel?
6. Write P.E in full.
7. At what time will Namata visit her aunt?
8. What is the name of Namata’s aunt?
9. On which day will Namata wash her P.E uniform?
10. What will Namata do on Friday?
11. With whom will Namata go to the beach?
TOPIC 1B: KEEPING A DIARY
Vocabulary
1. diary
2. read
3. note
4. date
5. day
6. daily
7. month
8. year
9. calendar
10. time
Page | 3
Activity 2
Read the words and use them to construct sentences.
Activity 3.
Read the words in the box and use them to fill the gaps below.
1. The …………today is Monday, 15 th August, 2011.
2. Have you seen my …………? I need to write in it.
3. I am ten now, so I shall be eleven next………….
4. It’s August now, so next……………… is September.
5. A ………………….shows you all the days of the year.
6. How many ……………….are there in a week?
diary
date
days
month
calendar
year
Monday Tuesday Wednesday Thursday Friday Saturday Sunday
1
Wrote an
invitation
card to
uncle
2 3
Sent the
invitation
card to
uncle
4 5
6 7 8 9 10 11
We went to
the village
for my
birthday
party
12 Father
bought for
me a new
party dress.
13 14
Aunt
Monica
baked
my
birthday
cake
15 16
I
celebrated
my ninth
birthday
17 18 19
20 21 22 23 24 25 26
I attended
thanks
giving
service.
27 28 29 30
We
returned
to our
home.
Page | 4
Activity 4.
</passage>

<passage id="lchk_a8b51257a7204350820a66c1c782842d" source="P 4 ENG & SST Lesson Notes Term III 2023" part="2">
Study Amanya’s Diary and answer the questions about it.
Questions:-
1. Whose diary is this?
2. On which day of the week did this month begin?
3. What did Amanya do on the first Wednesday of this month?
4. When did Amanya send the invitation card to her uncle?
5. What did Amanya’s father buy for her ?
6. Who baked Amanya’s birthday cake?
7. On which day did Amanya celebrate her birthday?
8. When did the month end?
9. When did Amanya attend thanks giving service?
10.Who bought Amanya a new dress?
Activity 5.
Written Exercise
Study Kivi’s activity plan for a whole week and answer questions that follow in
full.
October Morning Afternoon
Sunday, 13 th Prayers Ironing clothes
Monday, 14 th Reciting a poem Singing
Tuesday, 15 th Spellings and dictation Computer lessons
Wednesday, 16 th Writing a composition Drawing and painting
Thursday, 17 th Debating Swimming lessons
Friday, 18 th Attending school
assembly
Doing mixed work
Saturday, 19 th Helps mother with
domestic work
Visits his friend in Kansanga.
Questions:-
1. When will Kivi go for prayers?
2. What will Kivi do on Sunday afternoon?
3. What will Kivi do on Monday, 14 th ?
4. When will Kivi go for computer lessons ?
5. Apart from drawing, what else does Kivi do on Wednesday?
6. What does Kivi do on Thursday morning ?
7. At what time of the day will Kivi attend the school assembly?
8. Whom will Kivi help on Saturday?
9. What kind of work will Kivi help his mother?
10. Whom will Kivi visit on Saturday?
11. Where does Kivi’s friend stay?
Page | 5
TOPI 1 C: USING STUDY TIME.
Vocabulary
1. borrow 6. usually
2. lend 7. return
3. library 8. notes
4. librarian 9. notebook
5. revise 10. textbooks
Activity II
Use the vocabulary above to construct sentences.
Activity III
Use the words in the box to fill in the gaps correctly.
1. We write ………………in our exercise books.
2. It is very important to …………………for end of term exams.
3. A ………………works in a library.
4. A ………………..is a collection of books.
5. He told me to …………………….. him my jacket.
Activity IV
Study Mukaga’s plan for tomorrow and answer the questions that follow in
full sentences.
8:00 a.m Having breakfast at Doso’s restaurant.
8:30 a.m Boarding a vehicle to Entebbe with friends.
10:30 a.m Getting special hire taxi to the zoo.
11:00 a.m Looking at different animals and birds.
12:30p.m Taking photographs at the zoo.
I:00 p.m Having lunch with my friends.
2:00 p.m Swimming with my friends.
2:45 p.m Boarding a vehicle back to Jinja.
Questions
1.Where will Mukaga go tomorrow?
2.Where will he have breakfast from?
3.For how long will he have his breakfast?
4.With whom is he going to Entebbe?
5.What will Mukaga do at 11:00 a.m?
6.What will he do after looking at the animals?
librarian
lend
library
notes
revise
Page | 6
7.At what time will he have lunch?
8.What means of transport will he use to go to the zoo?
9.Where does Mukaga stay?
10.Write in full:
(a) a.m
(b)p.m
Written Exercise
Study Nanono’s timetable and answer questions that follow in full.
9:00a.
10.00a.m
10:00a.m
11:00a.m
11:00a.m
12:00p.m
12:00p.m
1:00p.m
1:00p.m
2:00p.m
2:00p.m
3:00p.m
3:00p.m
4:00p.m
Math English Art L S.S.T Science
Sci Maths S.ST Eng Music
Maths Reading
and
Writing
Sci P.E R.E
Eng Maths Computers Debate S.ST
Assembly S.ST Eng Swimming Sci
Questions
1. Whose timetable is written above?
2. What subject is taught after maths on Monday?
3. What subject is taught on Tuesday after break?
4. At what time does Nanono go for break?
5. On which day is music taught?
</passage>

<passage id="lchk_9736199ab4a342ea936fa6d345b01be4" source="P 4 ENG Grammar Scheme 2023" part="1">
P.4 ENGLISH GRAMMAR SCHEME OF WORK FOR
TERM III 2023.
WK PD TOPIC SUB-TOPIC SKILLS ASPEC
T
COMPE
TENCE
S
CONTE
NT
METH
ODS
ACTIVITIES
1 1
to
3
GOING
THROUG
H
HOLIDAY
WORK
HOLIDAY
WORK
Reading
&
listening
Speaking
Writing
- Reading
- Answering orally
- Writing corrections
2 - Writing and completing e
1 EXPRESSION
OF THE
FUTURE
EXPRESSION
OF THE
FUTURE
Listening
Speaking
Reading
Writing
The
future
simple
tense.
Vocabu
lary
“will”
and
“shall”
They
should
be able
to
• U
se the
future
simple
tense
correctl
y
• U
se will
• T
he
tense
used
when
thinkin
g or
imagini
ng an
action
or
event
that
• Expla
nation
s
• Guide
d
disco
very
• Whol
e
class
discu
ssion
Reading words and senten
future simple tense
Writing and completing s
exercise
and
shall in
senten
ces
correctl
y
• P
unctuat
e
joined
senten
ces
correctl
y
• W
rite
and
comple
tely
senten
ces
correctl
y. With
“will”
and
“shall”.
will
take
place
in
future.
• H
elping
verbs,
used
“will” &
“shall”
He
She
+
will
They
It
I + shall
We
2
EXPRESSION OF THE FUTURE
EXPRESSION OF THE FUTURE
Listening
Speaking
Reading
writing
Comple
ting
senten
ces
with
“will”
and
“shall:
with
given
verbs.
• Compl
ete
senten
ces
with
either
“will”
or
“shall”
with
given
verbs
correct
ly
• Compl
eting
sentenc
es with
will and
shall,
and
given
verbs.
• Exam
ples
Julian –
a prize
next
year –
(get)
Julian
will get
a prize
next
year
• Expl
anati
on
• Guid
ed
disco
very
Reading sentence
Writing and completing sent
3 The
future
continu
ous
tense
• Use
the
futur
e
conti
nuo
us
tens
e
corr
• Used
when
sayin
g or
talkin
g
about
an
event
that is
-do-
ectly
.
• Writ
e
and
com
plet
e
sent
enc
es in
the
futur
e
conti
nuo
us
tens
e
corr
ectly
taking
place
for a
perio
d of
time
in the
future
• Helpi
ng
verb
s
Will be
+verb
Shall be
ending
In- ing
3 1
EXPRESSION OF THE FUTURE
The
Passiv
e in
the
future
simple
Vocab
ulary
Expressing
“self” and
others in the
future simple
tense correctly.
Change the
given
sentences from
the active to
passive voice
in the future
simple tense
correctly
Re-write the
given
sentences
correctly.
The passive
voice in the
future simple
is used in the
order below.
Will be
past
Shall be
participle
Form of the
verb.
Examples:
The woman
will dig the
garden
tomorrow
(active)
The garden
will be dug by
the woman.
(passive)
Guided
discove
ry
Discuss
ion
Whole
class
discussi
on
Reading
the
given
sentenc
es
Re-
writing
the
given
sentenc
es in the
passive
of the
future
simple
tense
Effective
communi
cation
(Accurac
y, verbal
expressio
n)
Values
Honesty
Concern
Cooperat
ion
Hando
uts
MK
Precis
e Eng.
Gram,
pgs
92-
101
2
DEMOCRACY
Electio
ns
Listen
ing
Spea
king
Readi
ng
writin
g
Relativ
e
prono
uns.
Using
appropriate
language in
convincing
others.
Use relative
pronouns
correctly.
Completing
sentences
choosing the
correct relative
pronoun.
Joining
sentences
correctly using
relative
pronouns
Definition of a
relative
pronoun
Examples:
Who, whom,
that, which,
whose etc.
Guided
discove
ry
Whole
class
discussi
on
Construc
ting
sentenc
es using
relative
pronoun
s
Joining
sentenc
es
Writing a
filling in
exercise
Values
Cooperat
ion
Joy
Enduranc
e
Appreciat
ion
Life
skills
Self
Esteem
Assertive
ness
Volunteer
ing
Peer
resistanc
e
Textbo
oks
Hando
uts
Revisi
on
Englis
h by
Ronal
d
Forest
, pgs
91-92
MK
Precis
e Eng.
Gram.
Pgs
32-34
High
school
Eng.
Gram,
pgs
56-57.
3 Interro
gative
prono
uns
Use
interrogative
pronouns in
asking
questions
correctly.
Use suitable
pronouns to
complete the
given exercise.
Interrogative
pronouns are
</passage>

<passage id="lchk_ac900ec3a1984e52b584e352e119d4ab" source="NCDC P4 ENGLISH SYLLABUS" part="15">
• | Reads texts related to future activities and study time
• | Writes personal diary and study timetable.
• | Writes texts in the future tense.
• | Uses a personal diary and study time table.

TOPIC 8: DEMOCRACY
General background
This topic will enable learners to develop vocabulary and structures related to democratic activities. This will enable learners to express
themselves using appropriate language in different situations. The teacher should use demonstrations, discussions, dialogues and story
telling to develop the required competences.

Learning Outcome Learners will be able to use appropriate language to express themselves accurately and fluently when expressing
appreciation, making comments, noting main points and answering questions in order to live harmoniously in society.

Life skills and indicators.
Self esteem
Ǧ | Appreciating oneself.

Assertiveness
Ǧ | Being open
Ǧ | Listening to and valuing what others say
Ǧ | Volunteering
Ǧ | Standing for one’s right
Ǧ | Giving reasons for actions taken.
Ǧ | Peer resistance
Ǧ | Defending one’s decisions

ϮϭNational Curriculum Development Centre
P4 English Syllabus, | 21

Non – violent conflict resolution
• Negotiating
• Accepting defeat
• Use of appropriate body language

Empathy
• Supporting others
• Listening to others

Values
• | Co-operation | • | Honesty
• | Appreciation | • | Love
• | Endurance | • | Joy
• | Patience

SUB-TOPIC 8.1: GAMES AND SPORTS

Subject competences | Content | Suggested activities
• Using vocabulary and structures to construct
The learner: | Vocabulary | meaningful statements.
• Identifies games and sports | run, jump, play, football, netball, skip, race, throw | • Role playing different games and sports
played | high, long, kick, player, lose, win, happy. clap, shout, | events.
• Uses appropriate vocabulary | game, support, slow, ordinal numbers, fast, quickly | • Conducting simple conversations on games
and structures when | and sports.
volleyball, watch, coach, umpire, referee.
describing games and sports. | • Listening to and answering questions about
• Gives and follows simple | radio sports programmes.
Grammar
instructions in a given game | • Reading stories related to sports
and sport | • Use of adjectives
• Reading simple articles and adverts on games
• Sustains simple | and sports.
Language Structures
conversations | • Reading and interpreting information on a
• Reads simple articles on | • | What will …. do? | score board.
sports and games | • Writing guided compositions.
• | e.g. what will Akello do?
• Reads and interprets points | • Writing simple instructions
• | … will …
22 | ϮϮNational Curriculum Development Centre
P4 English Syllabus,

on a score board. | • | Akello will play football. | • Writing simple articles on games and sports.
• Writes simple descriptions on | • | Who was the ……. (first, second)? | •  Writing descriptions of selected games and
a given game or sport. | • | …. was …. the ……. | sports.

Subject competences | Content | Suggested activities
• | Writes simple articles | • | E..g. who was the first? | • Rearranging sentences related to sports
related to games and | • | E.g. Opendu was the first | and games events in a logical flow.
sports. | Why was …… the ……..
• E.g. why was Delia the last?
• ….. was the ……. because…………
• E.g. Delia was the last because she was slow
• ……want(s) to …… when …….
• I want to play volley ball when I join Primary Five

SUB – TOPIC 8.2: MUSIC, DANCE AND DRAMA
</passage>

<passage id="lchk_43d1a5388030467d8aa5d3bd64890a2a" source="NCDC P4 ENGLISH SYLLABUS" part="14">
The learner: | Vocabulary | and structures in
• Talks about future | • tomorrow, next Monday next week, next month, next year, shall not, | meaningful statements.
events | will not, arrive,
• | Acting dialogues
• Explains what will | Grammar: | /conservations related to
happen | • Use shall and will when expressing the future. | future events
• Responds to questions | • NB. I/we are used with shall | • | Asking and answering
appropriately. | • You/she/he/they used with will. | questions in the future
• Narrates events related | • Use of ‘will not’ | tense.
to future happenings. | • | Talking about events
Language Structures
• Read plans written by | related to the future
• I/we shall … You/she/he/they will …
their peers. | • … will…. | events.
• Writes personal plans. | • E.g. Alice will go to school tomorrow. | • | Reading simple texts
• … shall … | describing future events
• E.g. I shall eat a mango tomorrow | • | Reading plans of other
• … shall not … | learners.
• We shall not go to school next Monday. Shall we ……. tomorrow/next | • | Writing sentences and
week? | short texts in the future
• Yes, we shall …… No, we shall not … | tense.
• … will not …. | • | Formulating sentences
• E.g. Masaba will not come for the meeting tomorrow. | from substitution tables.
• Will …? | • | Writing guided composition.
• E.g. Will Masaba/he/she …… tomorrow? Yes, /she/Masaba will…….. | • | Writing personal plans.
• No, he/she will not………

ϭϵNational Curriculum Development Centre
P4 English Syllabus, | 19

Sub-topic 7.B: Keeping a diary

Subject competences | Content | Suggested activities
• Using vocabulary and
The learner: | Vocabulary | structures related to keeping
• Talks about activities in a • | diary, read, note, date, day, month, year, calendar time | a diary.
diary | • Acting dialogues related to
• Reads events in a diary | Language Structures
keeping a diary.
• Records events in a diary | • …… will …. on ….
• Reading and interpreting
• e.g. Miriam will visit her grandmother on 25th August. Revise then,
• Keeps a personal diary | information in a diary.
where and what time. Will … ?
• No… will … Yes … will …. | • Recording events in a
• e.g. Will Apio go to the market on Monday? | personal diary.
Ǧ No, she will not | • Keeping a class diary.
Ǧ No, she will go to the market on Sunday Yes she will go to the market
on Monday Yes,
• she will.

Sub-topic 7.C: Using study time

Subject competences | Content | Suggested activities
• Using given vocabulary and structures
The learner: | Vocabulary | correctly to construct sentences.
• Explains activities done | • borrow, lend, library, revise, note(s), notebook. | • Studying and answering questions about
during study time. | textbook. | a study time table.
• Reads a study timetable | • Formulating sentences using a study
Grammar | timetable.
• Writes a personal study
• Use of “usually”, “sometimes” | • Telling activities done during study time.
timetable.
• Language structures. | • Reading and interpreting a study time
• Uses the study time | • ….. “usually”…… | table.
effectively | • e.g. The teacher usually lends us books to read at | • Writing compositions about study time.
• Follows a study time | home | • Writing and acting conversations about
table. | • … “sometimes”…… | study time.
• e.g. I sometimes write down notes after reading a textbook.

20 | ϮϬNational Curriculum Development Centre
P4 English Syllabus,

Suggested Assessment Competences
• | Talks about future events
</passage>

<passage id="lchk_11d1b263ed194f0dbe2283cd505309d9" source="P4 English End Of Term III 2023" part="1">
STANDARD KOLFRAM P4 ENGLISH END OF TERM III EXAMINATION 2023
A product of Kolfram Educational Services Kampala 0777886622/ 0784044408/ 0756821512/0786941943/ 0777292922
For the best and improved holistic learning, always use Kolfram Educational Services products
END OF TERM III EXAMINATION 2023
PRIMARY FOUR
ENGLISH
Time allowed: 2 hours 15 minutes
Index Number :
Candidate’s Name : ………………………………………………………………………………….
Candidate’s Signature: ………………………………………………………………….……....
School Name: ………………………………………………………………………………………….
District Name: …………………………………………………………………………………………
DO NOT OPEN THIS BOOKLET UNLESS YOU ARE TOLD TO DO SO
QN.
NUMBER
MARKS EXAMINER’S
INITIAL
1 - 10
11 - 20
21 - 30
31 - 40
41 - 43
44 - 46
47 - 49
50 - 52
53 - 55
TOTAL
Admission Number Personal Number
A PRODUCT OF KOLFRAM EDUCATIONAL SERVICES KAMPALA
A leading publisher and distributor of Kolfram standard premium workbooks, companion books, Kolfram textbooks for all
classes, Topical revision workbooks, assessments, Past PLE Question Banks, PLE Revision workbooks and holiday packages
1. This paper has two sections: A and B .
Section A has 50 questions (50 marks) and
section B has 5 questions (50 marks). The
paper has 8 printed pages.
2. Answer all questions. All answers to both
sections A and B must be shown in the
spaces provided.
3. All answers must be written using a blue or
black ball point pen or ink. Any answer
written in pencils other than on graphs and
diagrams will not be marked.
4. No calculators or written materials are
allowed in the examination room.
5. Unnecessary changes in your work and
handwriting that cannot easily be read may
lead to loss of marks .
6. Do not fill anything in the table indicated:
" FOR EXAMINERS' USE ONLY " and boxes
inside the question paper.
FOR EXAMINER’S USE ONLY
Turn Over
STANDARD KOLFRAM P4 ENGLISH END OF TERM III EXAMINATION 2023
A product of Kolfram Educational Services Kampala 0777886622/ 0784044408/ 0756821512/0786941943/ 0777292922
For the best and improved holistic learning, always use Kolfram Educational Services products
SECTION A
( Questions 1 to 50 carry one mark each )
SUB-SECTION I
In each of the questions 1 to 5, fill the blank space with a suitable word.
1. There is …………………………………… new teacher in our class.
2. All the …………………………………… were stolen from the kraal.
3. I remember the boy …………………………………… took away my pencil.
4. There isn’t …………………………………… child at the play centre.
5. The …………………………………… is selling very good meat today.
In each of the questions 6 to 15, use the correct form of the word in
brackets to complete the sentence
6. Jackie succeeded due to …………………………………… hard work. (she)
7. The baby …………………………………… every night. (cry)
8. Most of the …………………………………… were late for the burial. (mourn)
9. Brenda is …………………………………… of her new dress. (pride)
10. Otim’s …………………………………… to do his homework was good. (decide)
11. A bag of cement is ………………………………… than a bag of maize flour. (heavy)
12. When it started raining, Mom was …………………………………… matooke. (peel)
13. What a …………………………………… day it was! (cloud)
14. All players were …………………………………… dressed during the match. (smart)
15. Akello ran quite fast and she was the ……………………………… in the race. (one)
In questions 16 and 17, arrange the given words in alphabetical order.
16. Soroti, Kampala, Gulu, Mbale
………………………………………………………………………………..……………………………….
17. pull, pineapple, pears, pawpaw
………………………………………………………………………………..……………………………….
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
