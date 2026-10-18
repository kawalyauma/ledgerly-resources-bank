# Job ltsk_4a676e1899d740719b7c8970c2aeb0e4-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 3 lesson(s) below of week 1 of the Islamic Religious Education scheme for Primary Three 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P3: one 40-minute lesson: 2–3 ideas; about 10–20 points; simple meanings and worked examples; 4–6 activities.

lessonId=lles_0a25e2d98b64493ca819be8cbfd3828c: lesson 1, Tuesday, 1 period(s), 40 minutes.
  Unit: History of Islam — Khadijah and the Revelation (theme: Khadijah and the Revelation). Lesson: Events immediately after the first revelation — Khadijah and the Revelation.
  Objectives: By the end of the lesson, learners should be able to tell what happened immediately after the first revelation.

lessonId=lles_fcb5eb50daf5425ea1b5a38eb0e8aa21: lesson 2, Thursday, 1 period(s), 40 minutes.
  Unit: History of Islam — Khadijah and the Revelation (theme: Khadijah and the Revelation). Lesson: Khadijah's reaction to the first revelation — Khadijah and the Revelation.
  Objectives: By the end of the lesson, learners should be able to describe how Khadijah responded to the first revelation.

lessonId=lles_7dbbe9215f904a0f97a904bbea56c5ad: lesson 3, Friday, 1 period(s), 40 minutes.
  Unit: History of Islam — Khadijah and the Revelation (theme: Khadijah and the Revelation). Lesson: Week 1 review — History of Islam — Khadijah and the Revelation.
  Objectives: Review this week's lessons: Events immediately after the first revelation; Khadijah's reaction to the first revelation
  This is the FRIDAY REVIEW of this week's lessons (listed in the objectives). notes = a '### Summary' heading per lesson with its key points ('- ' points), then '### Exercise' with review questions taken from the passages. activities = those questions.

Write, using ONLY the passages below. Passages from "NCDC" documents are the official base for what to teach; NCDC lower-primary thematic curricula put every learning area in columns separated by " | ": use only the Islamic Religious Education column.
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
<passage id="lchk_0483f0e20f2044b2bcdd9445a9aef8ca" source="NCDC P3 Thematic Curr 21 November" part="57">
Weeks 10-12
Theme: | Moral and Spiritual Teachings | Sub-theme: | Laws
Learning outcome: The child appreciates and applies the moral and spiritual teachings about divine laws in various situations for a peaceful living.
Content | Competences | Life skills | Values
• Law | • Identifying different laws | • Critical thinking | • Care
- definition of law | • Talking about categories of laws | • Creative thinking | • Unity
- categories of law e.g. man-made laws, | • Asking and answering questions | • Interpersonal relationship | • Obedience
laws by God | • Respect
• Responsibility
• | Types of laws | • | Naming the types of man-made laws | • | Coping with emotions | • Sharing
- laws of the state, family, school, divine | • | Discussing the importance of laws | • | Coping with stress | • Loyalty

law | • | Role-playing.

• | Purpose of laws | • | Identifying other types of man-made laws | • | Critical thinking | • | Responsibility
- orderliness | • | Talking about the reasons why laws should be respected | • | Creative thinking | • | Respect
- equity | • | Talking about what happens / would happen if laws are violated | • | Coping with emotions | • | Obedience
- protection of the weak | • | Asking and answering questions | • | Coping with stress | • | Unity
- promotion of state policy | • | Loyalty
- control selfish tendencies

Assessment Guidelines (Weeks 10-12)
• Identify the different laws.
• Name the types of man made laws.
• Talk about the reasons why laws should be respected.

Term III
Weeks 1-3
Theme: | History Of Islam | Sub-theme: | Khadijah and the Revelation
Learning outcome: The child understands and appreciates the important of continuous revelation occurrences right from the time of the prophet (PBUH) to the present-
day religious experiences.
Content | Competences | Life skills | Values
• Events which occurred immediately after the | • Talking about the first revelation | • Critical thinking | • Sharing
revelation | • Talking about the first revelation to Hadijah’s responses | • Effective communication | • Care
• Khadijah’s reactions | • Talking about Naufal’s reactions and how Hadijah helped Muhamad | • Interpersonal relationship | • Sympathy
• The role of Naufal | • Asking and answering questions | • Creative thinking | • Cooperation
• Coping with stress | • Love
• Coping with emotions | • Respect
• Obedience

Assessment Guidelines (Weeks 1-3)
• Talk about the first revelation.
• Talk about Naufals reactions and how Hadija helped Mohammed.
• Talk about the Divine nature of the Qur’an.
• Identify the rites performed before reciting the Qur’an.
• Write translated Arabic words.

Weeks 1-3
Theme: | Reading of the Qur’an | Sub-theme: | Rites of the Qur’an
Learning outcome: The child understands recognises and practices the performance of the required religious rites in the day today interaction with the Qur’an.
Content | Competences | Life skills | Values
• Rites | • Talking about the divine nature of the Qur’an | • Effective communication | • Respect
- definition of rites | • Identifying the rites performed before reciting the Qur’an | • Creative thinking | • Responsibility
- rites performed before reading the | • Asking and answering questions | • Coping with stress | • Care
Qur’an | • Role-playing the rites | • Coping with emotions | • Sharing
a) Wudhu | • Interpersonal relationship
b) Saying Istidha and Bismallah
</passage>

<passage id="lchk_f1810b7b39dd4e0a98bd9bdf9cd7a817" source="NCDC IRE P.3 TEACHERS RESOURCE BOOK" part="55">
- | Loving each other

Methods
Guided discovery, recitation

Instructional materials
A chart showing punishments given to people who break the law, newspapers

Teacher’s Activities | Learner’s Activities
 Guiding learners to share experiences |  Sharing experiences of people
about people who broke the law in | who broke the law and what
their community | happened to them
 Telling a situation where people do not |  Answering questions related to
obey the law and what happened to | the situation told by the teacher
them |  Telling the dangers of not
 Guiding learners to tell the danger of | keeping the law
not keeping the laws in society |  Mentioning punishment given to
 Guiding learners to name the | people who do not keep the law
punishment given to people who do |  Sharing lessons learnt from the
not keep the law | situations told by the teacher
 Guiding learners to share the lessons |  Saying a prayer asking God to
learnt from the situation shared | help them obey the law
 Guiding learners to say a prayer asking |  Reciting the verse of the week
God to help them obey the laws | (Qur’an 5: 47)
 Letting them recite the verse of the
week

PRIMARY THREE | TEACHERS’ RESOURCE BOOK

Verse of the week: Qur’an 5: 47’ “And whoever doesn’t judge by the Qurán such
people are rebellious or disobedient to Allah”. “Wamalam yahkum bimaa
anzala Allaahu fa.ula-ika hum li-faasi quun”

Guidance on Assessment
Assess the learner’s
i) logical reasoning as he/she tells the dangers of breaking the laws of the
state.
ii) concern as he/she mentions punishments given to people who break the
laws in the state.

Sample Activity
Organise learners to role play where some people kidnap children and they are
arrested, imprisoned or punished in public. The role play should bring out
repentance and promise to change.

Hint for the Teacher
Note some of the dangers:
 Creates conflicts in the society
 People are being exploited
 Insecurity i.e., kidnapping children, killing people
 Sending away people from their land
 Being arrested
 Getting imprisoned
 Being killed
 Getting burnt

ISLAMIC RELIGIOUS EDUCATION

TERM 3
WEEK 1
THEME: HISTORY OF ISLAM
SUB-THEME: Khadijah and the Revelation

Learning Outcome
The learner should be able to understand and appreciate the importance of the
continuous revelation occurrences right from the time of the Prophet (PBUH)
to the present-day religious experience.

Lesson 1: Events which Occurred Immediately after the First
Revelation

Reference
Qur’an 96: 1-5

Key message
Allah is happy when I appreciate the message revealed to Prophet
Muhammad.

Key term | Competences
 events - happenings | The learner
i) identifies the messages of the first revelation.
ii) tells the events that happened after the first
revelation.

PRIMARY THREE | TEACHERS’ RESOURCE BOOK

Life Skills Indicators
i) | Empathy | - | Caring; supporting others; comforting
others
ii) Problem-solving | - | Taking a decision, making choices
iii) Critical thinking | - | Responding | to | questions
appropriately

Values
- | Sharing
- | Love
- | Appreciation
- | Cooperation
- | Respect
- | Obedience

Methods
Guided discussion, story telling

Instructional materials
A chart showing the first five verses of Iqrah

Teacher’s Activities | Learner’s Activities
 Guiding learners to recite surah |  Reciting surah related to the
related to the first revelation to | first revelation
Prophet Muhammad |  Listening to the story and
</passage>

<passage id="lchk_0bae47a91d89494f859251372186e83c" source="NCDC IRE P.3 TEACHERS RESOURCE BOOK" part="56">
 Telling a story related to what | answering questions
happened in the cave immediately |  Mentioning what is in the first
after the revelation | five verses of Iqrah
 Sharing the first five verses of Iqrah |  Practicing the reading of
 Instructing learners to practice | verses of Iqrah
reading of the verses |  Reciting the verse of the week.
 Guiding learners to recite the verse | (Surat Al-Iqrah 96: 1)
of the week

Verse of the week: “In the name of your Lord who has created all that exists.
Surat Al-Iqrah 96: 1“I qra-u bismi rabbika llazii khalaq”

ISLAMIC RELIGIOUS EDUCATION

Guidance on Assessment
Assess the learner’s
 confidence in sharing information as he/she tells what happened after the
first revelation.
 ability to support other learners as he/ she re-tells the story of what
happened in the cave.
 audibility as he/she recites the first five verses of Surah Iqrah.

Sample Activity
Guide learners in pairs and individually to recite Surah Iqrah Q 96:1-5 below:
Igra’bismi Rabbikal-lazee khalaq
Read! In the name of your lord who has created all that exists
Khalaqal- insaana min alaq
He created man from a clot
Iqra” wa Rabbukal- Akram.
Read! And your lord is the most generous
Allazee allama bilqalam
Who has taught the writing by the pen.
Allamal- insaana maa lam ya’lam
He has taught man that which he knew not.

Hint for the Teacher
 Prepare a chart showing the first five verses of Surah Iqrah.
 Let individual learners practice reciting the first five verses of Surah Iqrah.

Lesson 2: Khadijah’s Reactions

References
Qur’an, Hadith

Key message
Allah is happy when I accept His message.

PRIMARY THREE | TEACHERS’ RESOURCE BOOK

Key term | Competences
 reactions - responses | The learner
i) identifies what Khadijah did when the
Prophet approached her.
ii) describes Khadijah’s response after being
told the message.

Life Skills Indicators
i) Empathy | - | Listening to others
ii) Problem-solving | - | Taking a decision
iii) Coping with stress | - | Accepting advice; narrating personal
experience

Values
- | Sharing the experiences
- | Cooperating with one another
- | Loving the Prophet who brings Allah’s message

Methods
Storytelling, guided discovery, guided discussion

Instructional materials
Chart, markers

Teacher’s Activities | Learner’s Activities
 Guiding learners to recite the first five |  Reciting the first five verses of
verses of Iqrah | Surah Iqrah
 Telling a story about Khadijah’s |  Listening | and | answering
experience | questions about the story
 Sharing Khadijah’s reaction as told in |  Mentioning Khadijah’s reactions
the story |  Sharing lessons learnt
 Guiding learners to share lessons learnt |  Reciting the verse of the week. (Q
 Guiding learners to recite the verse of | 96: 1)
the week

ISLAMIC RELIGIOUS EDUCATION

Verse of the week: “In the name of your Lord who has created all that exists -
Q 96: 1 “I qra-u bismi rabbika llazii khalaq”

Guidance on Assessment
Assess the learner’s
i) confidence as he/she mentions Khadijah’s reaction towards the 1st
revelation.
ii) articulation as he/ she gives the lessons learnt from Khadijah’s reaction.

Sample Activity
Guide learners in groups of three to role play a situation when one is sick,
feeling cold, shivering and goes back to parents! What happens?

Hint for the Teacher
Khadija’s reactions to Prophet Muhammad (PBUH);
 She received the message wholeheartedly.
 She accepted everything that was said by the Prophet as was revealed.
</passage>

<passage id="lchk_286d5562262a47209e989a508d8802d2" source="NCDC IRE P.3 TEACHERS RESOURCE BOOK" part="71">
Wa rizqan tayyibba | - | Knowledge that benefits
Waamalan mutaqabbalah | - | I ask you

Hint for the Teacher
Emphasise correct pronunciation and spelling.

Lesson 3: Role Playing the Dua Practices (dua related to
knowledge)

Reference
Qur’an 2: 269

Key message
Allah helps me to spread His words through prayers.

ISLAMIC RELIGIOUS EDUCATION

Key terms | Competences
 enjoy | The learner
 spreading | i) recites the dua related to knowledge.
 prayers | ii) role plays the dua related to knowledge.

Life Skills Indicators
i) Effective communication | - Fluency, audibility, confidence,
articulation, accuracy
ii) Creative thinking | - Logical reasoning, initiating ideas

Values
- Sharing new ideas with others
- Respecting other pupils’ ideas
Methods
Rote method, guided discussion, demonstration, recitation
Instructional materials
Costumes
Teacher’s Activities | Learner’s Activities
 Guiding learners to recite the dua |  Reciting the dua
 Telling a story about the dua |  Listening to the story and
 Organising learners for role play the | answering questions
dua to bring out the meaning |  Role playing the dua
 Guiding learners to recite the verse |  Reciting the verse of the week
of the week Qur’an 2:269 | Qur’an 2: 269

Reciting the dua: Asi-aluka ilman naafi-aa wa rizqan rwayyibaawa amala
mmutaqabbalaa” – “O Allah I ask you for good knowledge, good provisions and
deeds which are accepted and pleasing you”.

Guidance on Assessment
Assess the learner’s audibility as he/she recites the dua related to knowledge.

Sample Activity
Prepare learners to role play the dua.

PRIMARY THREE | TEACHERS’ RESOURCE BOOK

WEEK 10
THEME: HISTORY OF ISLAM
Sub-theme: The Call

Learning outcome
The learner should be able to understand and appreciate the call and mission of
Prophet Muhammad (PBUH), in order to enrich the daily religious experiences in
different life situations.

Lesson 1: The Beginning of the Call

Reference
Qur’an, 96:1-5

Key message
It is good to accept the message given to Prophet Muhammad (PBUH).

Key term | Competences
 Ramadhan - 9th | The learner
month on the | i) tells when the first call was made to Prophet
lunar calendar | Muhammad.
ii) names the place where the first call was received
from.
iii) mentions what happened when Prophet received
the first call.

Life Skills Indicators
i) Creative thinking | - Logical reasoning, initiating ideas, Innovativeness
ii) Critical thinking | - Responding to questions appropriately
iii) Empathy | - Guiding others, listening to others, comforting
others

ISLAMIC RELIGIOUS EDUCATION

Values
- Appreciating the message revealed
- Being patient like the Prophet (PBUH)

Methods
Storytelling, guided discussion

Instructional materials
Documentary

Teacher’s Activities | Learner’s Activities
 Guiding learners to tell when the first call  Telling when the first call was
was made to Prophet Muhammad | made | to | Prophet
 Helping learners to name the place where | Muhammad
the first call was received from |  Naming the place where the
 Guiding learners to mention what | first call was received from
happened when Prophet received the  Mentioning what happened
first call (through telling the story of how | when Prophet received the
Prophet Muhammad (PBUH) received the | first call
first message from Allah) |  Reciting the first five verses
 Guiding learners to recite the first five | of Surat Iqrah. Qur’an 96:1-5
verses of Surat Iqrah. Qur’an 96:1-5

Guidance on Assessment
</passage>

<passage id="lchk_057e00aab4e44d66aa9549782d5bacd2" source="NCDC IRE P.3 TEACHERS RESOURCE BOOK" part="57">
 She accepted Islam.

Lesson 3: The role of Waraqa bin Nawfal

References
Qur’an, Hadith

Key message
Allah is happy when I help those in need.

Key term | Competences
 Waraqa bin Nawfal - He was | The learner
an old man who was an | i) shares the story about Waraqa bin
expert in translating the | Nawufal experience.
ii) tells lessons learnt from Waraqa bin
scriptures.
Nawfal’s experience.

PRIMARY THREE | TEACHERS’ RESOURCE BOOK

Life Skills Indicators
i) Friendship formation: | - | Sharing; working with others; love;
concern; trustworthiness; coping
with stress
ii) Coping with stress: | - | Being patient, accepting advice
iii) Effective communication: | - | Confidence, logical flow of ideas

Values
- | Sharing the experience of Waraqa bin Nawufal with others
- | Caring for others
- | Cooperating with others

Methods
Storytelling, rote method

Instructional materials
A chart showing people in need, resource person

Teacher’s Activities | Learner’s Activities
 Guiding | learners | to | share |  Sharing experiences about
experiences about people they | people they have ever helped
have ever helped |  Listening to the story about
 Telling the story about Waraqa bin | Waraqa bin Nawfal and
Nawfal’s experience to learners | answering questions
 Guiding learners to share lessons |  Sharing lessons learnt from the
learnt from the story | story
 Guiding learners to recite the verse |  Reciting the verse of the week.
of the week | (Q 96: 1)

Verse of the week: “In the name of your Lord who has created all that exists.
Q 96: 1 “I qra-u bismi rabbika llazii khalaq”

ISLAMIC RELIGIOUS EDUCATION

Guidance on Assessment
Assess the learner’s
i) articulation as he/ she mentions Waraqa bin Nawufal’s reaction.
ii) concern for other people as he/ she tells how Khadijah helped Prophet
Muhammad (PBUH).

Sample Activity
Ask learners to:
1. Give at least 2 good things done by the following people/angels.
a) Khadijah
b) Waraqa-bin-Nawufal

2. Recite a rhyme about helping those in need.
Help, help, help
Help the sick
Help the poor
Help the sick
Help the orphans
Help the widow
Help, help, help
Allah will reward you

PRIMARY THREE | TEACHERS’ RESOURCE BOOK

WEEK 2
THEME: READING OF THE QUR’AN
SUB-THEME: Rites of the Qur’an

Learning Outcome
The learner should be able to understand, recognise and practise the
performance of the required religious rites in the day-to-day use of the Qur’an.

Lesson 1: Rites

Reference
Qur’an 16: 98, 4: 43, 5: 6

Key message
I should respect the Holy Qur’an.

Key term | Competences
 rites - religious customs | The learner
i) gives the meaning of the word “rites”.
ii) names the rites performed before reciting
the Qur’an.

Life Skills Indicators
i) | Effective | - Accuracy, meaningfulness, articulation
communication
ii) Critical thinking | - Responding to questions appropriately
iii) Assertiveness | - Being open

ISLAMIC RELIGIOUS EDUCATION

Values
- | Respecting the Holy Books
- | Responsibility towards protecting the Holy Books
- | Caring for the Holy Books

Methods
Guided discussion, demonstration, recitation

Instructional Materials
A chart showing a person reading the Qur’an

Teacher’s Activities | Learner’s Activities
 Guiding learners to recite a surah |  Reciting a surah related to the
related to the Qur’an | Qur’an
 Sharing the meaning of rites with |  Telling the meaning of rites
the learners |  Naming rites performed before
 Sharing with learners the rites | reciting the Qur’an
</passage>

<passage id="lchk_9a3a8c1962714cc289d9a9885bc70608" source="NCDC P3 Thematic Curr 21 November" part="59">
b) Zukinfalimanoh | • Reciting the Duas | • Coping emotions | • Respect
• Asking and answering questions | • Effective communication | • Sharing
(Lord advance me in knowledge and grant me | • Coping with emotions | •
wisdom) | • Coping with stress
• Interpersonal relationship
• Critical thinking
• | Dua | • | Talking about the importance of seeking knowledge | • Effective communication | • | Respect
- importance of seeking knowledge to a | • | Reciting the Duas | • Coping with emotions. | • | Obedience
Moslem | • | Asking and answering questions | • Coping with stress | • | Care
• Interpersonal relationship | • | Sharing

• | Critical thinking | • | Responsibility

Assessment Guidelines (Weeks 7-9)
• Recite Duas related to knowledge.
• Ask and answer questions.
• Talk about each Dua.
• Talk about the importance of seeking knowledge.

Weeks 10 – 12
Theme: | History of Islam, | Sub-Theme: | The Call
Learning outcome: The child understands and appreciates the call and mission of Prophet Muhammad (PBUH) in order to enrich the daily religious experiences in
different life situations
Content | Competences | Life skills | Values
• The call | • Talking about revelation | • Effective communication | • Tolerance
- the beginning of the call | • Talking about Mohammad’s plans for calling people | • Critical thinking | • Respect
- the first people who received his call | • Explaining how Mohammad’s close companions reacted | • Creative thinking | • Endurance
- the approach Mohammad (PBUH) used | • Asking and answering questions | • Coping with stress | • Responsibility
to preach his words | • Telling and retelling stories | • Coping with emotions
• | The reactions | • Identifying the first converts | • Effective communication | • | Tolerance
- how other people reacted to his call | • Talking about how Mohammad called people outside his family | • Critical thinking | • | Responsibility
and how they reacted | • Creative thinking | • | Respect
• Asking and answering questions | • Coping with emotions | • | Endurance
• Telling and retelling stories | • Coping with stress
• | Problems | • Identifying problems Mohammad faced | • Coping with stress | • | Obedience
- immediate problems Mohammad | • Talking about the problems Mohammad faced | • Coping with emotions | • | Respect
(PBUH) faced | • Telling and retelling stories | • Interpersonal relationship | • | Tolerance
• Asking and answering questions | • Effective communication | • | Perseverance

Assessment Guidelines (Weeks 10-12)
• Talk about Mohammed’s plans for calling people.
• Identify the first converts.
• Tell and re-tell stories.
• Identify problems Mohammed faced.
• Ask and answer questions.

PHYSICAL EDUCATION (PRIMARY 3)

1.0 | INTRODUCTION
Physical Education (PE) is the field of learning which aims at the development of the following;
• Knowledge;
• understanding positive social behaviour;
• attitudes concerning human movement;
• body skills and capabilities;
• practical activities in sports and games as well as their application to physical fitness;
• healthy lifestyle and social interaction within safe and structured play through physical and mental
exercise;
• the mastery of the movement patterns and the development of body stamina to maintain health
through movement, agilities, games and sports.

Physical Education (PE) in the Thematic Curriculum is to be taught as an independent learning area (subject)
</passage>

<passage id="lchk_2333a86171bb440d83a3be4b4f4b196b" source="NCDC IRE P.3 TEACHERS RESOURCE BOOK" part="72">
Assess the learner’s
i) logical reasoning as he/she answers at least three questions about the
story.
ii) articulation as he/she recites Qur’an 96: 1-5.

Sample Activity
Let learners answer questions about the first revelation.
1. Who received the message?
2. Where was the message received from?
3. Who brought the message?
4. What was the response of Prophet Muhammad?

PRIMARY THREE | TEACHERS’ RESOURCE BOOK

Hint for the Teacher
The story on the first revelation was handled in Term 1. Therefore;
 tell the story to remind learners about what they learnt.
 emphasise key questions about the story.

Lesson 2: The First People Who Received the Prophet’s Call

Reference
Qur’an, 73: 1-3

Key message
I should appreciate those who received and believed in the first
message.

Key term | Competences
 believe – have faith | The learner
i) identifies the people who received the first call
ii) identifies people he/she trusts at home.
iii) gives reasons why he/she trusts those people.

Life Skills Indicators
i) Problem solving | - Making a choice, evaluating facts, taking
a decision
ii) Creative thinking | - Logical reasoning
iii) Empathy | - Supporting others, listening to others,
comforting others

Values
- | Appreciating people who received the first message
- | Respecting other people

ISLAMIC RELIGIOUS EDUCATION

Methods
Storytelling, guided discussion

Instructional materials
A chart showing names of people who first believed the Prophet’s message

Teacher’s Activities | Learner’s Activities
 Sharing with learners through story |  Naming the first people
telling the first people who received the | received the first call of
first call of Prophet’s message | Prophet’s message
 Guiding learners through discussion to |  Identifying people, they
identify peoplehe/she trust at home | trust at home
 Helping learners to give reasons why |  Giving reasons why he/she
he/she trusts those people | trusts those people
 Guiding learners to recite the verse Q73: |  Reciting the verse Q73: 1-3
1-3

Guidance on Assessment
Assess the learner’s sharing of information as he/she names the people who
received the first message from Prophet Muhammad.

Sample Activity
Let learners answer questions about the story from Qur’an, 73: 1-3
1. Who received the message from Angel Jibril?
2. Who was the first person to believe in Prophet’s message?
3. Give other 3 people who received the first message.

Hint for the Teacher
Below are the people who received the first call.
 Khadijah: first woman
 Abubakar: first man
 Ali bin Abu Twalib: first among the children
 Zaid Harith: first slave and writer of the Qura’n

PRIMARY THREE | TEACHERS’ RESOURCE BOOK

Lesson 3: The Approach Prophet Muhammad (PBUH) used to
preach his Words

Reference
Qur’an 73: 1-3

Key message
I believe in Prophet Muhammad’s (PBUH) message.

Key terms | Competences
 approach - method | The learner
 preach - spreading the | i) identifies the first groups of people Prophet
word of God | Muhammad preached to.
ii) explains the approaches Prophet Muhammad
used to preach his word.

Life Skills Indicators
i) Critical thinking | - Responding to questions appropriately
ii) Problem solving | - Taking a decision, making a choice
iii) Effective communication | - Fluency, audibility, confidence,
accuracy, logical flow of ideas

Values
- | Appreciating Prophet Muhammad’s (PBUH) approaches to preach to
people
- | Being honest with the message
- | Being patient in case some people reject the message
</passage>

<passage id="lchk_6f2923255c7348f981bc07db4fdd1cf1" source="NCDC IRE P.3 TEACHERS RESOURCE BOOK" part="61">
 Prepare the chart showing Arabic words formed from syllables to be used
as examples.
 Prepare cut-outs of Arabic syllables, and letters for learners to work with
to form words.
 Let this activity be done in groups and then individually.
 Let learners first form the same word as those on the chart.
 Let learners write the Arabic words formed.

PRIMARY THREE | TEACHERS’ RESOURCE BOOK

WEEK 4
THEME: TAWHIID (FAITH)
Sub-Theme: Uniqueness of the Qur’an

Learning Outcome
The learner should be able to appreciate and recognise the uniqueness of the
Qur’an for meaningful spiritual growth.

Lesson 1: Uniqueness of the Qur’an –The Miracles

Reference
Qur’an 2: 185; “The month of Ramadan in which it was revealed”

Key message
Allah guides me to believe in the holy Qur’an.

Key terms | Competences
 uniqueness – being the | The learner
only one of its kind | i) sharing the uniquiness of the Qur’an.
 miracles – wonders | ii) identifies miracles in the Qur’an which
make it unique.

Life Skills Indicators
i) | Effective | - Confidence, articulation, accuracy
communication:
ii) Creative thinking: | - Logical reasoning
iii) Critical thinking: | - Responding to questions
appropriately, selecting and
evaluating information

ISLAMIC RELIGIOUS EDUCATION

Values
- | Respecting the Qur’an
- | Appreciating the miracles in the Qur’an

Methods
Guided discovery, storytelling

Instructional materials
Qur’an, chart showing the miracles that make the Qur’an unique

Teacher’s Activities | Learner’s Activities
 Reciting a verse related to the |  Reciting the surah
Qur’an |  Mentioning things that make
 Sharing | with | learners | the | Qur’an unique
uniqueness of Qur’an |  Identifying the miracles in the
 Guiding learners to identify the | Qur’an
miracles in the Qur’an that make it |  Reciting Qur’an 2: 285
unique |  Saying a prayer thanking God
 Guiding learners to recite a verse Q | for the Holy Qur’an
2: 285
 Guiding learners to say a prayer
thanking God for the Holy Qur’an

Verse of the week: Qur’an 2: 285 “The messenger (Muhammad – PBUH)
believes in what has been sent down to him from his Lord and (so do) the
believers. Each one believes in Allah, His angles, His books and His messengers
…” “A’mana rrasuulu bimaa unzilailayhi min rrabihi wal-mu-uminuuna kullun
a’mana billaahi…”

Guidance on Assessment
Assess the learner’s
 ability to share with others as he/ she tells when the Qur’an was revealed.
 self-reliance as he/she names the miracles that make the Qur’an to be
unique.
 fluency as he/she recites the surah of the week.

PRIMARY THREE | TEACHERS’ RESOURCE BOOK

Sample Activity
Ask learners to write the miracles that make the Qur’an unique

The
miracles

Hint for the Teacher
Organise for a visit to the mosque or invite the Imam/Sheik to tell the learners
miracles that make the Qur’an unique.

Note: The Qur’an contains miracle received by the Prophet who didn’t know
how to read and write

Lesson 2: Uniqueness of the Qur’an – Universal

Reference
Qur’an

Key message
Allah guides me to believe in the Holy Qur’an.

Key term | Competences
 uniqueness – being the only | The learner
one of its kind | i) explains why the Qur’an is universal.
 universal – worldwide | ii) names people who use the Qur’an.
 genuine - true message

ISLAMIC RELIGIOUS EDUCATION

Life Skills Indicators
i) | Effective | - Confidence, articulation, accuracy
communication
ii) Creative thinking | - Logical reasoning
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
