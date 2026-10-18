# Job ltsk_988d5408142a4a2ca36b984662fca70c-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 7 lesson(s) below of week 1 of the English scheme for Primary One 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P1: one 40-minute lesson: 1–2 small ideas; about 6–14 short points; very short words; concrete/local examples; 3–5 oral, matching, tracing or picture-led activities.

lessonId=lles_75af7826e3ce4ebc92311ed8512d3133: lesson 1, Monday, 1 period(s), 40 minutes.
  Unit: Our Transport (theme: Our Transport). Lesson: Plurals taking s — Types and means of transport: plurals taking s.
  Objectives: Read and spell the supplied singular and plural words correctly.

lessonId=lles_56bdc1dc46244fe9b831f42cf46bb780: lesson 2, Tuesday, 1 period(s), 40 minutes.
  Unit: Our Transport (theme: Our Transport). Lesson: Reading and writing plurals taking s — Types and means of transport: plurals taking s.
  Objectives: Write the supplied plural words correctly.
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points ('- ' points, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

lessonId=lles_8708966783c14930a38fb6ac8cfdacd1: lesson 3, Wednesday, 1 period(s), 40 minutes.
  Unit: Our Transport (theme: Our Transport). Lesson: The Traffic Light — Rhyme in relation to transport.
  Objectives: Read and recite the rhyme correctly.

lessonId=lles_0ef1d8e54dc94bfe9af56bc2bb29cde4: lesson 4, Wednesday, 1 period(s), 40 minutes.
  Unit: Our Transport (theme: Our Transport). Lesson: Reciting and writing The Traffic Light — Rhyme in relation to transport.
  Objectives: Recite and write the rhyme correctly.
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points ('- ' points, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

lessonId=lles_fb7a1094a27344c2a2062d59b5448a0b: lesson 5, Thursday, 1 period(s), 40 minutes.
  Unit: Our Transport (theme: Our Transport). Lesson: My Father — A story related to transport.
  Objectives: Read the supplied story carefully.; Identify missing words from the supplied list.

lessonId=lles_55b3efb097af412e93ec2519a1091173: lesson 6, Friday, 1 period(s), 40 minutes.
  Unit: Our Transport (theme: Our Transport). Lesson: Completing My Father — A story related to transport.
  Objectives: Fill the visible blanks using suitable words from the supplied list.
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points ('- ' points, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

lessonId=lles_fc41225201764b98b5fa9751f64e84a4: lesson 7, Friday, 1 period(s), 40 minutes.
  Unit: Our Transport (theme: Our Transport). Lesson: Week 1 review — Our Transport.
  Objectives: Review this week's lessons: Plurals taking s; Reading and writing plurals taking s; The Traffic Light; Reciting and writing The Traffic Light; My Father; Completing My Father
  This is the FRIDAY REVIEW of this week's lessons (listed in the objectives). notes = a '### Summary' heading per lesson with its key points ('- ' points), then '### Exercise' with review questions taken from the passages. activities = those questions.

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
<passage id="lchk_b4d3b58a64c44079b56622075ebfe9d9" source="P I English Grammar , Composition & Comprehension Scheme OF Work Term III" part="1">
1
TERM III – PRIMARY ONE ENGLISH
SCHEME OF WORK
2
GRAMMAR SCHEME OF WORK FOR PRIMARY ONE TERM III
W
K
D
P
THEME SUB-
THEME
CONTENT COMPETENCES METHODS ACTIVITIES L/AIDS REF REMARK
S
1 Our
transport
Types &
means of
transpor
t
Plurals
Plural means many
Nouns with letter ( s)
Examples
car – cars
road – roads
bicycle – bicycles
boat – boats
train – trains
ship – ships
pencil – pencils
pen – pens
ball – balls
bag – bags
pot – pots
toy – toys
doll – dolls
basket – baskets
- Reading the words
correctly
- Spelling and
writing answers
and the words
correctly
- Reading the words
correctly
- Spelling and
writing the words
correctly.
- Question
and
answer
- Reading
- Spelling
- Writing
- Answering
- A chart
showing
plurals
which take
(s)
- Effecti
ve
commu
nicatio
n
- Critical
thinkin
g
-
2 Plurals
Nouns which take ( es)
bus – buses
mango – mangoes
bench – benches
church – churches
- Reading the words
correctly
- Spelling and
writing the words
correctly
- Question
and
answer
- Reading
- Spelling
- Writing
- answering
- A chart
showing
plurals
which
takes (es)
- Effecti
ve
commu
nicatio
n
- Critical
thinkin
g
-
3
3 Plurals
Nouns which take ( ies)
Examples
lorry – lorries
baby – babies
lady – ladies
body – bodies
- - Look and
say
- Question
and
answer
- Reading
- Spelling
- Writing
- answering
- a chart
showing
plurals
ehich
takes (ies)
- critical
thinkin
g
- effectiv
e
commu
nicatio
n
-
1
Plurals
Nouns which take ( ves)
Examples
knife – knives
leaf – leaves
loaf – loaves
Plurals which change vowels
Examples
man – men
woman – women
tooth – teeth
foot – feet
goose – geese
- Reading the words
correctly.
- Spelling and
writing the words
correctly.
- Differentiating the
nouns which
change completely
- Look, say
and use
- Question
and
answer
- Reading
- Spelling
- Writing
- Answering
- A chart
showing
these
nouns
which take
( ves) and
those
which
change
completel
y
- Creativ
e
thinkin
g
- Effecti
ve
commu
nicatio
n
- Critical
thinkin
g
-
4
2 Nouns
Nouns which remain the same in
singular ( one) and plural (
many)
One many
sheep sheep
furniture furniture
luggage luggage
money money
firewood firewood
- - - - - -
3 Pronouns
A pronoun is a word used instead
of a noun .
Examples
He is used for (male)
Boy and man
She is used for (female)
Woman and girl
Anita is a girl.
She is a girl.
Deo is a boy
He is a boy.
Other pronouns like
We, they, I, it etc
- Reads the words
and sentences
correctly
- Identifies the
pronouns correctly
- Answers correctly
the given activity
- Guided
discussio
n
- Explanati
on
- Chalk board
- illustration
- reading
- writing
- self
awaren
ess
- effectiv
e
commu
nicatio
n
- critical
thinkin
g
-
5
1 Our
transport
Means of
transport
Tenses
Everyday tense
We add S, ies to the verb
when we are in singular but
the verb remains when we are
in plural.
e.g
- She goes to school
everyday. (go)
- Sarah washes her uniform
everyday. (wash)
- They eat food everyday.
(eat)
Children play good games
everyday.(play)
- Reading sentences
correctly
- Changing the verbs
correctly
- Guided
discovery
- Reading
- Spelling
- Writing
- A chart
showing
everyday
tense
- -
2 Yesterday tense ( past tense )
Verb yesterday tense
pray prayed
play played
read read
stop stopped
give gave
write wrote
take took
- Reads the words
correctly
- Changes the given
verbs into yesterday
tense correctly
- Attempts the given
activity correctly
- Guided
discussio
n
- Explanati
on
- Whole
word
- A chart
showing the
yesterday
tense
- Reading
- Spelling
- Writing
- Effecti
ve
commu
nicatio
</passage>

<passage id="lchk_ff7da0e0a6d4466fab01a6c633e4ad9a" source="P 1 English Comprehension Scheme Of Work Term III" part="1">
ENGLISH COMPREHENSION SCHEME OF WORK FOR P.1 THIRD TERM
W
K
P
D
THEM
E
SUB
THEME
CONTENT COMPETENCES METHODS/
TECHNIQU
ES
L/ACTIVITY IND. OF
L.SKILLS &
VALUES
L/AIDS REF RE
M
1 1 OUR
TRANS
PORT
Rhyme
in
relation
to
transpor
t
The Traffic Light
Stop says the red light.
Go says the green.
Get set the amber one.
Blinking in between.
That’s what they say.
And that’s what they mean.
All must obey them.
Even the queen
The learner;
- reads and writes the
rhyme correctly.
- answers oral and written
questions.
discussion
explanation
recitation
reciting the
rhyme
answering
oral and
written
question
fluency
articulation
effective
communica
tion
Chalkb
oard
illustrati
on
Monitor
English
Course
book 1
page 68
2 A story
related
to
transpor
t
MY FATHER
My father was driving a…… As he
was driving, we saw a-----moving
on rails. The bus by passed us
driving very fast. My father drove
up to Airport. (train, driver car,
Entebbe)
The learner;
- reads the story carefully.
- tells the missing words
according to given list.
- fills in the missing words
to complete a meaningful
story.
observation
explanation
question
and answer
reading the
story
filling the
missing
words in the
story
effective
communica
tion
fluency
self esteem
Chalkb
oard
illustrati
on
Teachers
collection
2 1 OUR
TRANS
PORT
Speech
exercise
and
tongue
twister
Travellers travelling to Toronto
travelled with travellers travelling
to different countries.
Mark the carpenter parked his car
at the far car park.
The learner;
-makes different sounds
imitating the teacher and
animal sounds.
-pronounces words
correctly.
imitation
recitation
story telling
explanation
telling
stories
reciting
tongue
twisters
fluency
articulation
self esteem
Chalkb
oard
illustrati
on
Mk
Precise
page 80
-recites tongue twisters
correctly.
question and
answer
2 A story
related
to
measure
s and
transpor
t
MY HOME
My home is near Mbale town.
There is a big tree near my home.
I go to study at Aloi Primary
School. My home is far away from
my school. I use a lorry to go to
school. It is very fast. It takes me a
few minutes to reach school.
The learner;
- reads the story correctly.
- explains new words in
the story correctly.
- answers oral and written
questions about the story.
explanation
discussion
question
and answer
story telling
reading the
story
answering
oral and
written
question
articulation
verbal and
non verbal
logical
thinking
Chalkb
oard
illustrati
on
Thematic
curriculum
Trs guide
page 357
3 1 OUR
TRANS
PORT
A
substitut
ion table
about
past
tense
A substitution table about the past
tense
The learner;
- reads the words
correctly.
- constructs oral and
written sentences in past
tense.
discussion
explanation
reading the
words
correctly
makes good
sentences
from the
table
articulation
creative
and critical
thinking
Chalkb
oard
illustrati
on
MK Pupils
book
standard 2
page 133
2 A
dialogue
about
measure
s
A dialogue
Nathan: Good morning Susan.
Suzan: Good morning Nathan.
Nathan: Where do you live?
Suzan: I live at Gayaza.
Nathan: What do you use when
coming to school?
Suzan: I use a car.
Nathan : I like using a motor cycle
because I stay near the school.
Suzan: Oh! That is good.
The learner;
- reads the dialogue.
- answers oral and written
questions.
discussion
explanation
question
and answer
answering
the
questions
acting the
dialogue
articulation
fluency
self esteem
Chalkb
oard
illustrati
on
Teachers
collection
4 1 OUR
TRANS
PORT
A rhyme
about
travellin
g
Rhyme
Travelling is good
by road by air
by water by rail
</passage>

<passage id="lchk_774e31304802474db0b62f3d614c8ff9" source="P 1 English Comprehension Term Three" part="1">
ENGLISH COMPREHENSION SCHEME OF WORK FOR P.1 THIRD TERM
W
K
P
D
THEM
E
SUB
THEME
CONTENT COMPETENCES METHODS/
TECHNIQU
ES
L/ACTIVITY IND. OF
L.SKILLS &
VALUES
L/AIDS REF RE
M
1 1 OUR
TRANS
PORT
Rhyme
in
relation
to
transpor
t
The Traffic Light
Stop says the red light.
Go says the green.
Get set the amber one.
Blinking in between.
That’s what they say.
And that’s what they mean.
All must obey them.
Even the queen
The learner;
- reads and writes the
rhyme correctly.
- answers oral and written
questions.
discussion
explanation
recitation
reciting the
rhyme
answering
oral and
written
question
fluency
articulation
effective
communica
tion
Chalkb
oard
illustrati
on
Monitor
English
Course
book 1
page 68
2 A story
related
to
transpor
t
MY FATHER
My father was driving a…… As he
was driving, we saw a-----moving
on rails. The bus by passed us
driving very fast. My father drove
up to Airport. (train, driver car,
Entebbe)
The learner;
- reads the story carefully.
- tells the missing words
according to given list.
- fills in the missing words
to complete a meaningful
story.
observation
explanation
question
and answer
reading the
story
filling the
missing
words in the
story
effective
communica
tion
fluency
self esteem
Chalkb
oard
illustrati
on
Teachers
collection
2 1 OUR
TRANS
PORT
Speech
exercise
and
tongue
twister
Travellers travelling to Toronto
travelled with travellers travelling
to different countries.
Mark the carpenter parked his car
at the far car park.
The learner;
-makes different sounds
imitating the teacher and
animal sounds.
-pronounces words
correctly.
imitation
recitation
story telling
explanation
telling
stories
reciting
tongue
twisters
fluency
articulation
self esteem
Chalkb
oard
illustrati
on
Mk
Precise
page 80
-recites tongue twisters
correctly.
question and
answer
2 A story
related
to
measure
s and
transpor
t
MY HOME
My home is near Mbale town.
There is a big tree near my home.
I go to study at Aloi Primary
School. My home is far away from
my school. I use a lorry to go to
school. It is very fast. It takes me a
few minutes to reach school.
The learner;
- reads the story correctly.
- explains new words in
the story correctly.
- answers oral and written
questions about the story.
explanation
discussion
question
and answer
story telling
reading the
story
answering
oral and
written
question
articulation
verbal and
non verbal
logical
thinking
Chalkb
oard
illustrati
on
Thematic
curriculum
Trs guide
page 357
3 1 OUR
TRANS
PORT
A
substitut
ion table
about
past
tense
A substitution table about the past
tense
The learner;
- reads the words
correctly.
- constructs oral and
written sentences in past
tense.
discussion
explanation
reading the
words
correctly
makes good
sentences
from the
table
articulation
creative
and critical
thinking
Chalkb
oard
illustrati
on
MK Pupils
book
standard 2
page 133
2 A
dialogue
about
measure
s
A dialogue
Nathan: Good morning Susan.
Suzan: Good morning Nathan.
Nathan: Where do you live?
Suzan: I live at Gayaza.
Nathan: What do you use when
coming to school?
Suzan: I use a car.
Nathan : I like using a motor cycle
because I stay near the school.
Suzan: Oh! That is good.
The learner;
- reads the dialogue.
- answers oral and written
questions.
discussion
explanation
question
and answer
answering
the
questions
acting the
dialogue
articulation
fluency
self esteem
Chalkb
oard
illustrati
on
Teachers
collection
4 1 OUR
TRANS
PORT
A rhyme
about
travellin
g
Rhyme
Travelling is good
by road by air
by water by rail
</passage>

<passage id="lchk_0f5e18c52938474c801f964c09e9e235" source="P I English Grammar , Composition & Comprehension Scheme OF Work Term III" part="3">
These two words are normally
used in every day tense
whereby do is used in plural
and does is used in singular
part from I
Examples
He They
She does we do
have children
It peter
Cat
Peter
Mary
- - - - - -
11
1
Peace and security
Use of was and were
These two words are normally
used in yesterday tense.
Was is used in singular and
were is used ion plural
- He was not with me
- She was present yesterday.
- Joan was here last week.
- They were together in the
store
- Children were happy
yesterday
- Reading the
pronouns and
sentences correctly
- Constructing
meaningful
sentences
- Guided
discovery
- Reading
- Writing
- Chalkboar
d
illustration
- -
COMPOSITION SCHEME OF WORK FOR PRIMARY ONE TERM III 201
W
K
DP THEME SUB-
THEME
CONTENT
1
Our
transpor
t
Types of transport
Vocabulary
Road, railway, water, animal,
air, transport
2 Means of
transport
Vocabulary
Motor cycle, trailer, pick up,
bus, car, ship, donkey, lorry,
bicycle, boat, train, horse,
aeroplane, ferry, yatch, horse,
canoe
Structures
What is this / that?
This is a ………..
That is a …….
COMPOSITION SCHEME OF WORK FOR PRIMARY ONE TERM III 2019
COMPETENCES METHOD
S
ACTIVITIES L/AIDS
Road, railway, water, animal,
- Reads, spells and
writes the new words.
- Pronounces the words
correctly.
- Whole
word
listen
say and
use
- Reading
- Spelling
- Writing
- Pronouncing
the words
correctly
- Completing
the
structures
correctly
- Using the
structures
correctly
-
-
-
Motor cycle, trailer, pick up,
bus, car, ship, donkey, lorry,
bicycle, boat, train, horse,
aeroplane, ferry, yatch, horse,
This is a ………..
That is a …….
- Reads, spells
pronounces and
writes the words
correctly.
- Writes and completes
the structure
correctly.
- Uses the structures
correctly.
- Identifies different
means of transport for
different types
- Explanat
ion
- Whole
sentence
s
- -
12
L/AIDS REF REMARK
S
- Flash
cards
- Wall
charts
- Sentence
cards
- Sharing
- Confid
e
- Audibil
ity
- Confid
ence
- Fluenc
y
- Curr
Bk
Pg 43
trs
guide
pg
334
- - - Mk
Bk
pg
109
- 110
3 Structures
What are these / those?
These are ……..
These are ………..
1
Means of transport
Picture composition
Picture 1 __________
Picture 2 __________
Picture 3 _________
Picture 4 __________
Free composition writing
Write a free composition about
transport. Talk about the types
and means of transport.
Tell us the means of transport
you commonly use
These are ……..
These are ………..
-
-
-
- Studies the pictures
- Make correct
sentences for the
pictures
- Explanation
- Reading
- Spelling
- Writing
Free composition writing
Write a free composition about
transport. Talk about the types
Tell us the means of transport
- Read
- Writes the story
correctly
- Story telling
- Explanation
- Chalk board
13
-
- -
-
- -
- Decision making
- Effective
communiaction
- -
1
Measures related to transport
Vocabulary
Tall, short, longer, heavy,
near, far, bigger, bus, ship,
smaller, lorry, bicycle, train
Structures
a) What is the school?
Is it far or near?
b) Is the …. Long or short
Yes, it is/ No it is not
c) Which is bigger
d) Which is longer
e) Which is smaller?
2 Things
we
make
Things
we make
at home
and
school
Vocabulary
Mats, baskets, pots, dolls, toys,
balls, ropes, hats, winnowers
Structures
What is that / what is this?
Tall, short, longer, heavy,
far, bigger, bus, ship,
smaller, lorry, bicycle, train
What is the school?
Is the …. Long or short
Yes, it is/ No it is not
Which is smaller?
- Reads the words
correctly
- Spells and writes the
words correctly
- Compares the given
</passage>

<passage id="lchk_fa1f49fe122d49d393c248950fd55631" source="NCDC P1 Curriculum TG" part="176">
Preparation
• Collect materials for the shopping corners
• Make a clock face
• Prepare flashcard for reading

News
• | Learners tell news of their choice in turns
• | Learners discuss side effects of accidents.

Literacy 1
• Learners tell stories about travelling
• Learners role play on speed and distance e.g. three learners, one an imaginary motor-cycle, one
to walk on foot, one an imaginary bicycle.
• Learners read words related to different types from flashcards e.g. motor cycle, bicycle.
• Learners talk about different types of transport.
Which transport is fastest? | Which is slower/est
Which one is faster | Which is more comfortable
Which transport is fast?

Literacy II
• Learners write letter patterns ara taha
• Learners write words they have read in their exercise books/slates e.g. motorcycle, bicycle, bus.
• Learners spell the words they have written orally. Copy sentences.
• Learners fill in missing letters in words.

Mathematics
• Learners count up to 90.
• They practise subtracting in groups, pairs and individually.

English
• Revise the vocabulary for Monday and Tuesday.
• Let learners look at the different vehicles in the picture and get them to ask and answer these
questions.
- Look at the car. | Which one is fast, | Which one is big.
- Look at the bicycle | That one is fast. | This one is big,
• Learners ask a variety of questions related to transport using the same structures

PE | Experience with body and space (Refer to Curriculum)

Free activity
Prepare enough materials for learners to use.

Primary School Curriculum , Teacher’s Guide- Primary 1

9.3. Measures Related to Transport

Materials
A simple map
Word and sentence cards
Money (coins)
A chart of the National a n d Schools Anthem

Preparation
• Prepare a simple map showing home, school, church, clinic with varying distances.
• Prepare a rhyme related to measures
• Prepare word and sentence cards

PE
Experience with body and space (Refer to Curriculum)

Literacy 1
• Learners talk about the distance and time they take to come to school
• They talk about the means of transport and how.
• Learners recite a rhyme related to measures
• Learners read the words and sentences from the word/sentence cards

Literacy II
• Learners write patterns; iri ira tera, letters i, r, a, e
• They write words and short sentences.
• Learners fill in the missing letters.

Mathematics
• Display the simple map for the whole class to see
• Learners tell the distances between places using far and near, short and long.
• Learners draw simple maps of their homes, school and clinic
• Learners talk about their maps

English
• Using a situational game teach the following words and structures e.g. light, heavy, big,
small, long and short Structures
- What are they/those? | These/those are ...
- Is this (big) ...? | It is ...
- Is the (long) ... | No it is short.

News
• Learners tell news about any means of transport they have seen
• Learners imitate coming to school using different means of transport.
• Learners recite rhymes

National Curriculum Development Centre

RE
IRE: Reciting Surat Annas | (Refer to Curriculum)
Reading the Quran: Importance of Surat
CRE: Songs of Praise

Creative Performing Arts (Music)
• Revise the first stanza of the National Anthem

Primary School Curriculum , Teacher’s Guide- Primary 1

9.3. Measures Related to Transport

Materials
Real objects of different sizes
A chart showing days of the week
Word cards
</passage>

<passage id="lchk_1f4c2a6cc0b5478a9bd4b57f8954a527" source="NCDC P1 Curriculum TG" part="173">
-  What is she doing? | She is ... (riding a bicycle).
• Learners say the vocabulary in plural form
• Learners draw and label pictures.

PE
Experience with body and space (Refer to Curriculum)

RE
IRE: Reading the Quran: Meaning of the Surat Annas (Refer to Curriculum)
CRE: Doing what is right at all times

Creative Performing Arts (Music)
• Recite any known rhyme
• Give the background of the song to be taught
• Learners learn the new song
• Learners sing the song and dance to the rhyme.

National Curriculum Development Centre

9.2. Importance of Transport

Materials
Counters,
Wall chart
Flashcards
Toys

Preparation
Prepare materials for the day's lessons

PE
Experiences with body and space (Refer to Curriculum)

Literacy 1
• Learners revise different types and means of transport.
• Learners talk about the most common type of transport.
• They talk about the safest transport and why.
• Learners read words and sentences related to different types and means of transport
• Learners build words learnt using individual letters (word building).

Literacy II
• Learners write patterns aka, akoa
• They write letters o, a, k.
• Learners write words built from the letters.
• Learners write short sentences.

Mathematics
• Learners count 1-90.
• They write number names 31-40.

English
• Learners revise the vocabulary from last week using the singular.
- "What is this/that is?
- This/that is . . .
• Learners learn the plural form of bicycle, horse, aeroplane using the following structures
- How many ... are there?
- There are ...
• Learners practice using the structures learnt
• Learners practise the question and answer:
- How do you come to school? | I walk to school.
- How does she come to school | She comes to school by bus '
• If necessary, they can imitate how they come to school.

News
• | Learners tell / sign news about the means of transport they saw on their way to school
• | Learners tell their news
• | Learners draw their news

RE
IRE: | Reciting Surat Annas (Refer to Curriculum)
Reading the Quran: Meaning of the Surat
CRE: | Doing what is right at all times

Creative Performing Arts (Music)
• Learners sing any known song
• Talk about the song intended to be taught
• Teach a new song and accompany it with simple percussion instruments.

Primary School Curriculum , Teacher’s Guide- Primary 1

9.2. Importance of Transport

Materials
Counters
Word cards
Wall chart, picture cards, number chart, sentence cards

Preparation
Find an appropriate story, songs for the day's lessons.

News
• | Learners tell their news about types of transport they like and why.
• | They draw their news in their workbooks/slates.

Literacy 1
• Read a story to learners while they listen
• Ask questions about the story
• Learners answer orally.
• Let learners talk about the safest type of transport
• Learners read the key words from the story.

Literacy II
• Learners write patterns kata tak. Get learners to find words that use those letters.
• Learners write letters a, k, t.
• Write simple sentences and get learners to copy and punctuate them using capital letters and full stops.

Mathematics
• Learners count 1 - 9 0
• They match number symbols to number names 1 — 40.

English
• Revise the vocabulary learnt previously and structure i.e. bicycle and horse "How many ... are
there?", "There are ..."
• Teach new vocabulary motor cycle, ship and helicopter using following the structures in
singular and plural: -
- "What is this/that?"
- it's a ...
- What are these?
</passage>

<passage id="lchk_f9d2f349ddfe41e1b4aed39dc6119737" source="P 1 English Term 3 Notes" part="3">
6. as black as charcoal
7. as slow as snail
8. as fat as a pig.
9. as busy as a bee.
10. as easy as ABC
Exercise
Complete these sentences
1. This water is as cold as
2. The tea is as hot as
3. She walks as slow as
4. Her blouse is as white as
5. Our friend is as as a pig.
Animals, bunch, bar, fruits, pair
For more lesson notes, visit www.freshteacheruganda.com
Theme: Transport and communication
For more lesson notes, visit www.freshteacheruganda.com
Sub-theme: Types and means of transport.
Content: Vocabulary - opposites
Examples of words.
Far - near heavy - light
Long - short fat - thin
Tall - short bigger - smaller
Big - small shorter- smaller
Exercise
Give the opposites of the underlined words in the sentences.
1. A bus is bigger than a taxi.
2. An elephant is a fat animal.
3. Maria is carrying heavy books.
4. Musa is a short boy.
5. Our home is near the school.
Choose the correct word from the brackets.
1. The girl is carrying a basket. (fat, big)
2. My home is from the school. (far, short)
3. A cow is than a goat. (smaller, bigger)
4. My father is than me. (taller, longer)
Theme: Transport and communication
Sub-theme: Types and means of transport.
Content: Joining sentences using “but”
Examples;
1. Musa went to the airport. He did not see the aeroplane. Musa went to the airport
but he did not see the aeroplane.
2. My brother went to the stage. He missed the bus. My brother went to the stage but
he missed the bus.
Exercise:
1. Sarah has a taxi. She doen’t know how to ride it.
2. Tim fell off his motorcycle. He did not get hurt.
For more lesson notes, visit www.freshteacheruganda.com
3. They went to the bus park. The bus had gone.
4. Sandra is ill. She does not want medicine.
For more lesson notes, visit www.freshteacheruganda.com
5. The fox chased a rabbit. It did not catch it.
Theme: Transport and communication
Content: Conjunction: Joining sentences using “and”
Examples
1. Ali is going to the lorry. Ann is going to the lorry.
Ali and Ann are going to the lorry.
2. The bird is flying in the air. The aeroplane is flying in the air.
The bird and the aeroplane are flying in the air.
Exercise
1. Musa drove the car very fast. Paul drove the car very fast.
2. Henry drove the car. He went home.
3. Tom is a fat boy. Peter is a fat boy.
4. The baby is eating food. The baby is drinking milk.
5. My father has a car. My mother has a car.
Sub-theme: Types and means of transport
Content: Vocabulary;
Road, water, air, railway, car, bus, lorry, bicycle, motorcycle, donkey,
camel, horse, boat, ship, train, aeroplane.
Exercise:
Make good sentences
For more lesson notes, visit www.freshteacheruganda.com
Read and draw.
1. I can see a bus.
2. A boy is riding a bicycle.
3. A man is driving a car.
4. This is a ship.
</passage>

<passage id="lchk_1b13c587235d4ba58fc3874a35a0180a" source="UCE English Language Paper 1 (112/1) Set H – Composition and Speech Writing" part="1">
112/1
English Language
Paper 1
2 hours
UGANDA CERTIFICATE OF EDUCATION
ENGLISH LANGUAGE
PAPER 1
TIME: 2 HOURS
Instructions to Candidates;
Attempt two questions
Section A is compulsory
SECTION A:
Use 250 – 300 WORDS
1. Your school is holding a campaign assembly. Imagine you are campaigning for the post
of Head prefect in your school. Write a speech you will give to the audience.
SECTION B:
Use 500 – 600 WORDS
Attempt one question from this section
2. Write a story ending …….if it had not been for the traitor, I would be a different person
altogether.
3. Discuss the uses of media in your country.
4. “People are deceitful” Write a composition based on the above statement.
5. Narrate an incident when you were discovered guilty.
6. Boxing is a sport that can cause death and thus it should be abolished” Write your
argument in support or rejection of the above statement.
7. Explain how your friendship with someone has helped you become a better person.
END
</passage>

<passage id="lchk_45833300cc6d4b9f98ebccea3f00d8a6" source="English Language Paper 1 (112/1) Holiday Package 1 – UCE Composition Practice" part="1">
PRACTICE MAKES PERFECT MY EFFORT MY FURURE Page 1
112/1
ENGLISH
LANGUAGE
PAPER 1
2HRS
Uganda Certificate of Education
ENGLISH LANGUAGE
PAPER 1
INSTRUCTIONS TO CANDIDATES:
 This paper has two sections: Section A and Section B.
 Answer ALL questions in all.
 Answer question one (1) in Section A (compulsory) and ALL other question
in Section B.
HOLIDAY PACKAGE 1
PRACTICE MAKES PERFECT MY EFFORT MY FURURE Page 2
SECTION A
1. You are a candidate whose guardian is severely sick of Covid-19 disease
and cannot support the family anymore. Write a letter to your nephew
who stays abroad informing him of the condition/situation at home.
You may use the following;
 Pain your guardian is going through
 Insufficient finances
 School closed
 No food
 The house helper ran away
 The home is in the road reserve
 You are scared of your security.
SECTION B
For each of the following topics and write a composition of
500 – 600words.
2. Write a story beginning “I was ushered into a pitch-dark room….”
3. “Girl –students should be allowed to wear skimpy school uniform
skirts.” Do you agree?
4. Write a story based on the saying; “Birds of a feather flock together”
5. “Co-curricular activities are essential in Schools.” Discuss.
6. Write a story ending “…. I sighed with relief when the baby came
crawling with a mobile phone.”
**** END ****
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
