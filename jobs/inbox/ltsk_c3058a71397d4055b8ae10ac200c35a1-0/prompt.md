# Job ltsk_c3058a71397d4055b8ae10ac200c35a1-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 6 lesson(s) below of week 1 of the English scheme for Primary Four 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P4: one 40-minute lesson: 2–4 sections; about 12–24 points; meanings, examples and uses; 5–7 activities.

lessonId=lles_ab709c243769477f9d5dc2457c5186ff: lesson 1, Monday, 1 period(s), 40 minutes.
  Unit: Time and expression of the future — week 1 (theme: Expression of the future and Time). Lesson: Using if — Using if.
  Objectives: By the end of the lesson, learners should be able to use if to express a condition and punctuate a conditional sentence.

lessonId=lles_d82dbb9eddac46a5aedebb8cbba94210: lesson 2, Tuesday, 1 period(s), 40 minutes.
  Unit: Time and expression of the future — week 1 (theme: Expression of the future and Time). Lesson: Using unless — Using unless.
  Objectives: By the end of the lesson, learners should be able to use unless to express a negative condition.

lessonId=lles_158a41b592ad4482a3e12f50d5b2571d: lesson 3, Wednesday, 1 period(s), 40 minutes.
  Unit: Time and expression of the future — week 1 (theme: Expression of the future and Time). Lesson: Using since — Using since.
  Objectives: By the end of the lesson, learners should be able to use since with a starting point in time.

lessonId=lles_d8040a8a9b59412a8235b83012670960: lesson 4, Thursday, 1 period(s), 40 minutes.
  Unit: Time and expression of the future — week 1 (theme: Expression of the future and Time). Lesson: Future-time vocabulary — Future-time vocabulary.
  Objectives: By the end of the lesson, learners should be able to read and spell future-time words.

lessonId=lles_80e2c6fa87b046f099f6f57f37931828: lesson 5, Friday, 1 period(s), 40 minutes.
  Unit: Time and expression of the future — week 1 (theme: Expression of the future and Time). Lesson: Using will and shall — Using will and shall.
  Objectives: By the end of the lesson, learners should be able to form affirmative and negative future sentences.

lessonId=lles_ef59331003f94be28160c04dfdb1ac62: lesson 6, Friday, 1 period(s), 40 minutes.
  Unit: Time and expression of the future — week 1 (theme: Expression of the future and Time). Lesson: Reading: Akot’s plan to go to the zoo — Reading: Akot’s plan to go to the zoo.
  Objectives: By the end of the lesson, learners should be able to read a future-time passage and answer comprehension questions.

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

<passage id="lchk_ffbd8d2a243242b78590b9329650b56a" source="P 4 Composition Scheme" part="1">
ENGLISH SCHEME OF WORK; CLASS: P.4
SUBJECT: COMPOSITION TERM: THREE, YEAR:2023
W
K
PD TOPIC ASPECT COMPETENCES METHO
DS
SKILLS L/AIDS ACTIVITIE
S
VALUES LIFE SKILLS REF
1 1&
2
Express
ion of
the
Future
-
Vocabulary:
tomorrow,
shall, will,
next,
-construct
sentences
using the
above
words.
- Punctuation
capital
letters.
- Jumbled
ideas.
-Guided
composition
swimming
gala
-Free
composition.
The learner :
-spells &
pronounces the
words correctly.
-uses the new
words correctly.
-punctuates
correctly
-rearranges to
form correct
sentences.
-fills in with
correct words.
-Writes a
descriptive
composition.
Class
and
group
discussio
ns
-
listening
.
-
speakin
g.
-
reading
-writing.
-handouts
-
chalkboar
d
-
textbooks
-reading
-spelling
-making
sentences
-
rearrangin
g ideas
-filling in
correctly
-story
writing.
-
cooperatio
n
-
appreciati
on
-effective
communicat
ion
-decision
making
St.
Bernard
Bk4
page
152.
Model
compositi
ons.
Essential
English
workboo
k.
Trs.
Collectio
n.
Christmas Dictionar
y
2 1&
2
Keepin
g a
Diary
-Vocabulary
practice
diary, date,
time, note.
-matching
words to
their
meanings
- Structures
What / very.
-Jumbled
ideas.
The learner :
-spells &
pronounces the
words correctly.
-matches the
words to their
meanings
correctly.
-punctuates
correctly
-rearranges to
Class
and
group
discussio
ns
-
listening
.
-
speakin
g.
-
reading
-writing.
-handouts
-
chalkboar
d
-
textbooks
-a diary
-reading
-spelling
-making
sentences
-
rearrangin
g
sentences.
-filling in
correctly.
-values
-co-
operation
-
appreciati
on
-effective
communicat
ion
-decision
making
St.
Bernard
Bk4
page
160.
Model
compositi
ons.
Essential
English
- Revision
( opposites)
- Guided
composition.
(Kenya’s
Diary)
form good
stories.
-gives opposites
of words.
-fills in with the
correct words.
-forming
opposite
words
workboo
k.
Trs.
Collectio
n.
Dictionar
y
3 1&
2
Using
study
time.
- Vocabulary
practice:
library,
borrow, lend,
notes.
- Structures
.. usually..
..sometimes..
- Jumbled
ideas.
-
Revision (usin
g correct
forms)
-Jumbled
composition:
(Our time
table).
The learner :
-spells &
pronounces the
words correctly.
-uses the new
words correctly.
-punctuates
correctly.
-rearranges to
form good
stories.
-uses correct
forms of words.
-Makes a good
composition
from the
jumbled ideas.
Class
and
group
discussio
ns
-
listening
.
-
speakin
g.
-
reading
-writing.
-handouts
-
chalkboar
d
-
textbooks
- copies
of the
class
timetable
reading
-spelling
-making
sentences
-
completing
sentences.
-arranging
-filling in
correctly.
-values
-co-
operation
-
appreciati
on
-effective
communicat
ion
-decision
making
St.
Bernard
Bk4
page
169.
Model
compositi
ons.
Essential
English
workboo
k.
Trs.
Collectio
n.
Dictionar
y
4 1&
2
Games
and
Sports.
- Vocabulary
practice:
run, jump,
skip, throw.
- Structures
but /
although
- Punctuation
- Jumbled
ideas.
- Revision
…so….that
…
- Free
composition.
(Sports
Bonanza.)
The learner :
-spells &
pronounces the
words correctly.
-uses the new
words correctly.
-punctuates
correctly
-rearranges to
form good
stories.
-writes a
narrative
composition.
Class
and
group
discussio
ns
-
listening
.
-
speakin
g.
-
reading
-writing
-handouts
-
chalkboar
d
-
textbooks
-pictures
reading
-spelling
-making
sentences
-arranging
-filling in
correctly.
-
cooperatio
n
-
appreciati
on
-
endurance
-joy
-patience
-honesty
-love
-self
esteem
-
assertivene
ss
-conflict
resolution
-empathy
St.
Bernard
Bk4
page
176.
Model
compositi
ons.
Essential
English
workboo
k.
Trs.
Collectio
n.
</passage>

<passage id="lchk_66e2ee5447794359a38eab8dca9d1b53" source="P 4 ENG Grammar Scheme 2023" part="2">
those used
for asking
questions
Examples:
Who, whom,
whose etc.
e.g.
(1)Who are
you?
(2) Whom do
you want?
Construc
ting
sentenc
es orally
using
interroga
tive
pronoun
s.
Filling in
an
exercise
with
suitable
interroga
tive
pronoun
s.
4 1
-Do-
-Do- Listen
ing
Spea
king
Readi
ng
writin
g
Reflexi
ve
prono
uns.
Use reflexive
pronouns
correctly.
Construct
sentences
using reflexive
pronouns
correctly.
Write a filling-
in-exercise
using reflexive
pronouns
correctly
Pronouns use
“self” in
singular and
“selves” in
plural
Examples
Myself –
ourselves
Himself-
themselves
Explan
ation
Guided
Discove
ry
Look,
say and
use
(LSU)
Whole
class
discussi
on.
Reading
words
and
sentenc
es
Construc
ting
sentenc
es orally
Writing
and
completi
ng a
filling-in-
exercise.
Life
skills:
Self
Esteem
Assertive
ness
Values
Cooperat
ion
Appreciat
ion
Enduranc
e
Jot
patience
Honesty
Love.
Hando
uts
Textbo
oks
High
school
Eng.
Gram,
pgs
43-44,
MK
Precis
e
Eng.
Gram,
pgs
34-36
2
-do-
COND
ITION
AL
CLAU
SES
IF
CLAU
SE (1)
expressing
“self” and
others using “if
1” correctly
punctuate
sentences
correctly
complete
sentences
correctly using
given words
complete
sentences in
different ways
Conditional
clause
contain the
words “if” or
“unless”.
Note :
put a comma
if the “if”
clause comes
first
use a future
simple tense
in the “main
clause”; and
the present
simple tense
in the “if”
clauses.
If I pass
exams, I will
fly to London.
Reading
sentenc
es
Completi
ng
sentenc
es with
given
words.
Writing
and
completi
ng
sentenc
es in
different
ways
Jnr
Eng.
Comp
&
Gram;
pgs
37-38
MK
Englis
h
Hand
outs,
M.o.O
, PGS
56-57.
MK
Precis
e Eng.
Gram,
pgs
146-
147.
3 Listen
ing
Spea
king
Readi
ng
writin
g
Condit
ional
clause
2
If (2)
Expressing
“self” and
“others” using
If (2) correctly
Punctuate the
sentences
correctly.
Complete
sentences
using given
words
correctly.
Complete
sentences in
different ways
correctly.
Conditional
sentence or
clause (2) is
used to
express a
condition
which is
impossible
The condition
can’t be
fulfilled at all
e.g.
If I was God, I
would leave
man to live
for ever.
The past
simple tense
is used in the
if clause and
the present
tense in the
main clause.
Explan
ation
Discuss
ion
Whole
class
discussi
on
Guided
discove
ry
Reading
and
construc
ting
sentenc
es
Completi
ng
sentenc
es with
given
words
Effective
communi
cation in
fluency,
Accuracy
,
Confiden
ce
Values
Patience
Co-
operation
Appreciat
ion
Chart
Hando
uts
Jnr.
Eng.
Comp
&
Gram,
pgs
39-41
MK
Precis
e Eng.
Gram,
pgs
147-
149.
MK.
Eng.
Hand
book
for
P.5-7,
by
M.O.
O pgs
56-58.
5 1 -do- Unless Using “unless”
correctly in
sentences
Re-write
sentences with
unless
correctly.
Punctuate
sentences
correctly.
Complete
sentences in
different ways.
“Unless”
means “if not”
A comma is
needed when
unless begins
a sentences;
but it is not
required
when unless
appears in
the middle
e.g
If you don’t
go to bed
early, you will
feel tired.
Unless you
go to bed
early, you will
get tired. (1
&2) almost
have the
same
meaning).
Reading
sentenc
es
Re-write
sentenc
es
beginnin
g with
unless.
Writing
and
completi
ng
sentenc
es in
ways as
guided.
Eng.
Gram
&
exerci
ses 3,
pgs
79-81
Jnr.
Eng.
Comp
&
Gram
MK
Precis
e Eng.
Gram,
pgs
146-
147
2 NOUN
S
Listen
ing
Spea
king
Readi
ng
Writin
g
Comm
on
Nouns
Define the term
“noun”
Mention the
classes of
nouns.
Giving
examples of
common nouns
Identifying
common nouns
in given words.
Completing
sentences
selecting
common nouns
from given
words.
A noun is a
naming word;
used to name
persons,
animals,
</passage>

<passage id="lchk_502bab9a89e844fb8fffbee567c30d73" source="NCDC P4 ENGLISH SYLLABUS" part="5">
The syllabus for P.4 has been arranged in matrix. The scope and sequence has been organized in eight topics. Each topic has sub-topics
with subject competences to be developed using suggested learning activities. Each sub-topic has specific content of vocabulary and
structures.

Methodolog
The recommended teaching methodology emphasizes active participation and performance of children in their own learning. Since P.4 is a
transitional class, learners should be given more time to practice the structures learnt and vocabulary orally. Reading and writing should be
enhanced through reading texts and a variety of writing exercises. The teacher is expected to use generic methods like demonstration, role
play, creative writing and reporting.

ǀŝŝNational Curriculum Development Centre
P4 English Syllabus, | vii

Teaching Procedures
TP1: Presenting vocabulary
Steps to follow when teaching vocabulary
Step 1 | Revise any learnt words and the structure learnt that you will need to use with the new words.
Step 2 | Present the new words using objects/pictures/by demonstrating. Hold up the object/picture and say/sign the word
several times.
Step 3 | Learners repeat the word several times as you point to the object, picture, as a class, in pairs/groups or individually and
emphasize correct pronunciation and intonation.
Step 4 | Construct sentences using a known structure.
Step 5 | Learners practice constructing sentences using the learnt words in pairs or individually.
Step 6 | Learners write sentences, draw a picture, and play games using the structure and vocabulary learnt.

TP2: Presenting Structures
Steps top follow when teaching structures
Step 1 | Revise relevant previous vocabulary and any related structures(s)
Step 2 | Present the new structure using known vocabulary and illustrate the meaning by miming or in context.
Step 3 | Learners repeat the new structure with emphasis on correct pronunciation and intonation.
Step 4 | Construct sentences using the structure.
Step 5 | Learners practice asking and answering questions in groups or pairs.
Step 6 | Learners describe pictures and write sentences using the structure learnt where appropriate.

TP4 Teaching Through a Dialogue
Steps to follow when using a dialogue
Step 1 | Revise the structure and vocabulary previously learnt. Make sure everyone understands the meaning.
Step 2 | Say the dialogue as learners listen.
Step 3 | Learners repeat after you several times.
Step 4 | Divide the class into two groups, let them say with each group take on one part.
Step 5 | Learners practice in pairs or in chain drill One or two pairs demonstrate.
Step 6 | Let pairs demonstrate to the rest of the class.

viii | ǀŝŝŝ
P4 English Syllabus, National Curriculum Development Centre

TP5: Teaching Through Games
Step 1 | Teach or revise any new words they will need in the game.
Step 2 | Explain how the game will be played. Give clear instructions in English.
Step 3 | Demonstrate the game to the children
Step 4 | Encourage volunteers who may have understood the game to demonstrate to the class.
Step 5 | Children play the game. It can be outside the class.

TP6: Teaching Through Role-play and Acting
Use the same procedures as for dialogue (TP4 above). When learners have developed more vocabulary, you will be able to use a much freer
approach to acting/role-playing.

Instructional Materials
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

<passage id="lchk_6ada0a6682ac4826817cae5ee2fc04b1" source="P4 English End Of Term III 2023" part="5">
Because my daddy died!
But she comforts me totally.
As we laugh and smile
STANDARD KOLFRAM P4 ENGLISH END OF TERM III EXAMINATION 2023
A product of Kolfram Educational Services Kampala 0777886622/ 0784044408/ 0756821512/0786941943/ 0777292922
For the best and improved holistic learning, always use Kolfram Educational Services products
53. The table below shows the election result for Benita Primary School.
Study it carefully and answer in full sentences, the questions that
follow.
Candidate’s
name
P.4 P.5 P.6 Total vote
Boys Girls Boys Girls Boys Girls Boys Girls
Tendo 13 16 20 21 10 22 43 59
Ezati 15 14 14 26 20 16 49 56
Hussein 19 19 16 09 - 03 35 31
Total number of
pupils per class 96 106 71 127 146
Questions
(a) Who won the election?
……………………………………………………………………………………………………………
……………………………………………………………………………………………………………
(b) Which class had the highest number of voters?
……………………………………………………………………………………………………………
……………………………………………………………………………………………………………
(c) Which class had the most female voters?
……………………………………………………………………………………………………………
……………………………………………………………………………………………………………
(d) How many boys voted?
……………………………………………………………………………………………………………
(e) How many candidates stood for the election?
……………………………………………………………………………………………………………
……………………………………………………………………………………………………………
(f) In whose school were the above elections conducted?
……………………………………………………………………………………………………………
……………………………………………………………………………………………………………
(g) Do you think prefects are needed in a school?
……………………………………………………………………………………………………………
……………………………………………………………………………………………………………
(h) What is the above table about?
……………………………………………………………………………………………………………
(i) Write the opposite of the following
a) Female : …………………………………………………………………………………………..
b) Above : …………………………………………………………………………………………….
55. There are two stories A and B. In each story, the sentences are not
arranged in order. Re-arrange them to make good stories.
A
a. Suddenly a swarm of bees flew out of the mango tree and attacked him.
b. On his way he saw ripe mangoes on a tree.
c. One day Okello was going home from school.
d. Okello ran fast and entered a nearby house.
e. He picked stones and started throwing at the ripe mangoes.
STANDARD KOLFRAM P4 ENGLISH END OF TERM III EXAMINATION 2023
A product of Kolfram Educational Services Kampala 0777886622/ 0784044408/ 0756821512/0786941943/ 0777292922
For the best and improved holistic learning, always use Kolfram Educational Services products
Good story
……………………………………………………………………………………………………………
……………………………………………………………………………………………………………
……………………………………………………………………………………………………………
……………………………………………………………………………………………………………
……………………………………………………………………………………………………………
……………………………………………………………………………………………………………
……………………………………………………………………………………………………………
……………………………………………………………………………………………………………
B
(a) He then joins the pieces to make good tables, beds, etc
(b) He loads his timber on a pick-up track and heads to his workshop.
(c) Mr. Sendi is a hardworking carpenter.
(d) He wakes up very early morning to buy timber.
(e) At the workshop he cuts the timber into pieces.
Good story
……………………………………………………………………………………………………………
……………………………………………………………………………………………………………
……………………………………………………………………………………………………………
……………………………………………………………………………………………………………
……………………………………………………………………………………………………………
……………………………………………………………………………………………………………
……………………………………………………………………………………………………………
……………………………………………………………………………………………………………
54. Read the composition using the given words correctly
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
