# Job ltsk_b511cbcfda6d4dbab176b2ed1ecf1ef2-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 3 lesson(s) below of week 2 of the Islamic Religious Education scheme for Primary One 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P1: one 40-minute lesson: 1–2 small ideas; about 6–14 short points; very short words; concrete/local examples; 3–5 oral, matching, tracing or picture-led activities.

lessonId=lles_8528dd637201429eb213bf26d2965c0f: lesson 4, Tuesday, 1 period(s), 40 minutes.
  Unit: Reading from the Qur'an — Surat An-Nas (theme: Our Transport (general P1 theme 9)). Lesson: Meaning of Surat An-Nas — Surat An-Nas.
  Objectives: By the end of this lesson, the learner should be able to tell the meaning of Surat An-Nas.

lessonId=lles_4a597d6cf504416f9ce0cc4ea8e3e647: lesson 5, Thursday, 1 period(s), 40 minutes.
  Unit: Reading from the Qur'an — Surat An-Nas (theme: Our Transport (general P1 theme 9)). Lesson: Importance of Surat An-Nas — Surat An-Nas.
  Objectives: By the end of this lesson, the learner should be able to state the importance of Surat An-Nas.

lessonId=lles_a7449ff64db240acbbbc144b75371025: lesson 6, Friday, 1 period(s), 40 minutes.
  Unit: Reading from the Qur'an — Surat An-Nas (theme: Our Transport (general P1 theme 9)). Lesson: Week 2 review — Reading from the Qur'an — Surat An-Nas.
  Objectives: Review this week's lessons: Meaning of Surat An-Nas; Importance of Surat An-Nas
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
<passage id="lchk_d75bf64ba9b746b4883980badae1a50e" source="NCDC P1 Curriculum" part="39">
Content | Competences | Life Skills | Values
Attributes of God |  | Mentioning some of the attributes |  | Creative thinking |  | Respect
of God (Allah) |  | Decision-making |  | Appreciation
 | Telling their meaning |  | Critical thinking |  | Care
 | Responsibility
Pillars of Faith (Imaan) |  | Defining Imaan |  | Coping with |  | Respect
 | Telling the meaning of the pillars | emotions |  | Care
of Imaan |  | Empathy |  | Loyalty
 | Giving the numbers and names |  | Critical thinking |  | Appreciation
of Imaan |  | Interpersonal |  | Sympathy
relationships |  | Responsibility

Assessment Guidelines for Theme 6
 Mention at least 4 attributes of Allah
 Define Imaan
 Tell meaning of the pillars of Imaan
 Give the numbers and names of Imaan

TERM 2
Theme 7: Moral and Spiritual Teaching (Hadith)

Weeks 7-9

Learning Outcome: The learner is able to understand and appreciate the value of respect.
Content | Competences | Life Skills | Values
 | Ways of showing |  | Identifying how people in our |  | Interpersonal |  | Loyalty
respect in | society show respect; kneeling, | relationships |  | Obedience
different societies | bowing, helping |  | Friendship formation |  | Respect
 | People who |  | Telling the categories of people |  | Empathy |  | Responsibility
should be | respected in each society e.g. |  | Care
respected in | mothers, fathers
different societies

Assessment Guidelines for Theme 7
 Tell at least 3 categories of people who should be respected
 Demonstrate at least 3 ways of showing respect

TERM 2
Theme 8: The History of Islam

Weeks 10-12

Learning Outcome: | The learner is able to know and appreciate the life of Prophet Mohammed
(P.B.U.H).
Content | Competences | Life skills | Values
Muhammad as a youth |  | Telling the tribe and clan of |  | Coping with emotion |  | care
 His clan | Prophet Muhammad |  | Creative thinking |  | Appreciation
 His tribe |  | Talking about the character of |  | Friendship formation |  | Togetherness
 His characters | the Prophet and telling those |  | Interpersonal |  | Respect
 His works | which should be emulated. | relationship |  | Obedience
 | Identifying the character that |  | Coping with stress |  | Tolerance
forced Hadijah to propose
marriage to Muhammad

Assessment Guidelines for Theme 8
 Tell the tribe of Prophet Muhammad
 Tell the clan of Prophet Mohammad
 Tell the character of the Prophet to be emulated

TERM 3

TERM 3
Theme 9: Reading from the Quran

Weeks 1-3

Learning Outcome: The learner is able to recite Surat Annas and understand the message contained
in the Surah.
Content | Competences | Life skills | Values
Surat Annas |  | Reciting the Surat |  | Effective |  | Appreciation
 | Telling the meaning of the Surat | communication |  | Loyalty
 | Telling the importance of the Surat |  | Creative thinking |  | Acceptance
i.e. Islamic teaching about diseases |  | Critical thinking |  | Responsibility
e.g. It cures Ginns |  | Problem solving |  | Sympathy
 | Narrating the incidents that led to |  | Empathy
the revelation of the Surat

Assessment Guidelines for Theme 9
 Recite the Surat
 Tell the meaning of Surat
 Tell the importance of the Surat

TERM 3
Theme 10: Tawhiid (Faith)

Weeks 4-6

Learning Outcome: | Thelearner is able to understand the principle of Tawhiid.
Content | Competences | Life skills | Values
</passage>

<passage id="lchk_1c39d6f24103439aa9a783db81b14e33" source="NCDC IRE P.1 TEACHERS RESOURCE BOOK" part="55">
 Do not give the Holy Qur’an to learners but use the quotations given from
the various parts of Holy Qur’an

LESSON 2: Meaning of Surat An-Nas
Reference: Holy Qur’an, Juzu, Islamic
Key message: | Competences:
I know the meaning | The learner:
of Surat An-Nas. |  recites/signs Surat An-Nas
 gives the meaning of Surat An-Nas

Life Skills | Indicators | Values
 Effective |  Audibility, meaningfulness, |  Acceptance,
communication | confidence, verbal and non- verbal | responsibility
expression
 Critical thinking |  Responding to questions

ISLAMIC RELIGIOUS EDUCATION

Life Skills | Indicators | Values
appropriately, analysing statements,
taking decision
 Creative |  Logical reasoning
thinking

Instructional Strategies: Recitation, guided discussion
Instructional Resources: Holy Qur’an, CD containing the meaning of Surat
Annas

Teacher’s Activities | Learners’ Activities
 Lead learners to recite/sign Surat An- |  Recite/ sign Surat An-Nas (1-6
Nas from the Quran | verses) from the Qur’an
 Share with the learners the meaning of |  Tell/ sign the meaning of Surat An-
the Surah (chapter) (1-6 verses) guided | Nas (1-6 verses) as observed from
discussion | the film on the CD
 Guide the learners to recite/ and |  Recite/ sign and discuss the
discuss the meaning of the key | meaning of the key message “I
message | know the meaning of Surat An-
Nas”

Guidance on Assessment
 Assess as the learner gives the meaning of the following verses–
 Assess as the learner recites/signs Surat An-Nas (1-6 verses)

Sample activity: Reciting Surat An-Nas (1-6 verses)
1. Qul a'oozu birabbin naas - Say: I seek refuge with the Lord And
Cherisher of Mankind
2. Malikin naas - The King (or Ruler) Of Mankind
3. Ilaahin naas - The God (or Judge) Of Mankind,
4. Min sharril waswaasil khannaas - From the mischief
Of the Whisperer (Of Evil) who withdraws (After his whisper)
5. Allazee yuwaswisu fee sudoorin naas - (The same) who whispers into
the hearts of Mankind
6. Minal jinnati wannaas - Among Jinns and among Men

PRIMARY ONE | TEACHERS’ RESOURCE BOOK

Hint for the Teacher
 Prepare a chart showing the meaning of the Surah (chapter) An-Nas and
display it in class from verses 1-6
 Guide the learners to recite as a class, group, in pairs and individually for
mastery
 Instruct learners to practise the recitation of the Surah (chapter) An-Nas and
its meaning on a daily basis

LESSON 3: Read Surat Annas in Arabic (verses 1-6)
Reference: Holy Qur’an, Juzu
Key message: | Competences:
I can read Surat An- | The learner:
Nas. |  The learner reads the transliteration of the Surat
correctly (1-6) verses correctly.

Life Skill | Indicators | Values
 Effective |  Fluency, accuracy, |  Appreciation,
communication | audibility, clarity, verbal | responsibility,
and non-verbal | respect
expression

Instructional Strategies: Recitation, I do, we do, and you do
Instructional Resources: Holy Qur’an, Surat An-Nas written on a chart.

Teacher’s Activities | Learners’ Activities
 Guide learners to recite/ sign Surat |  Recite/sign Surat Annas in the
Annas (1-6 verses) by using the | Holy Qur’an
Holy Qur’an |  Read/ braille the Surah
 Guide learners to read the | (chapter) from the displayed
transliteration of Surat Annas (1-6) | chart as a class, in groups and
verses several times | individually
 Guide learners to recite/ sign and |  Recite/ sign and discuss the
discuss the meaning of the key | meaning of the key message
message. | “I can read Surat An-Nas”.
</passage>

<passage id="lchk_8e901e6e75984837a9b4f858f11ed702" source="NCDC IRE P.1 TEACHERS RESOURCE BOOK" part="56">
ISLAMIC RELIGIOUS EDUCATION

Guidance on Assessment
Assess as the learner reads Surat Annas with confidence and correct
articulation of words
Sample activity: Reading Surat An-Nas

Hint for the Teacher
Display the transliteration of Surat An-Nas as below;
Bismillaahir Rahmaanir Raheem
1. Qul a'oozu birabbin naas
2. Malikin naas
3. Ilaahin naas
4. Min sharril waswaasil khannaas
5. Allazee yuwaswisu fee sudoorin naas
6. Minal jinnati wannaas
 Guide learners to practise reading the transliteration of the Surah (chapter)
 Leave the chart displayed in the class and make learners practice reading the
Suarh on a daily basis
 You may even make flash cards and ask learners to re-arrange in order the
verses (1-6).

PRIMARY ONE | TEACHERS’ RESOURCE BOOK

Week 2
LESSON 1: Read Surat An-Nas in the Language of Instruction (verses 1-6)
Reference: Holy Qur’an, an explanation of the last tenth of the Noble Holy
Qur’an, Juzu
Key message: | Competences:
I can read Surat An- | The learner:
Nas in my language. |  The learner reads Surat An-Nas with correct
pronunciation

Life Skill | Indicators | Values
 Effective |  Accuracy, audibility, |  Appreciation,
communication | fluency, verbal and non- | respect, love
verbal expression

Instructional Strategies: Demonstration, recitation
Instructional Resources: Holy Qur’an

Teacher’s Activities | Learners’ Activities
 Guide learners to recite/sign Surat |  Recite/sign Surat An-Nas from the
An-Nas (1-6 verses) from the Holy | Holy Qur’an
Qur’an | Read/braille the Surah (chapter)
 Using demonstration, guide learners | after the teacher
to read/braille Surat An-Nas (1-6) |  Recite/sign and discuss the
verses in the language of instruction | meaning of the key message “I can
through demonstration | read Surat An-Nas in my language”
 Guide learners to recite/sign and
discuss the meaning of the key
message

Guidance on Assessment
 | Assess as the learner recites/signs Surat An-Nas
 | Observe and assess as the learner reads Surat An-Nas in the language of
instruction

ISLAMIC RELIGIOUS EDUCATION

Sample activity: Reading Surat An-Nas

Hint for the Teacher
Guide the learners to read the Surah (chapter) verse by verse in the language of
instruction
1. Say: I seek refuge with the Lord and Cherisher of Mankind
2. The King (or Ruler) Of Mankind,
3. The God (or Judge) Of Mankind, —
4. From the mischief of the Whisperer (Of Evil) who withdraws (After his
whisper)
5. (The same) who whispers into the hearts of Mankind
6. Among Jinns and among Men

LESSON 2: Importance of Surat An-Nas
Reference: Holy Qur’an, Islamic books e.g., Bukhari, Islamic website e.g.,
www.tafseer.info
Key message: | Competences:
Surat An-Nas | The learner:
protects me against |  recites/signs the Surah (chapter) with correct
evil. | pronunciation.
 gives the importance of Surat An-Nas.

Life Skills | Indicators | Values
 Effective |  Fluency, confidence, audibility,  Appreciation
communication | verbal and non- verbal
expression, articulation
 Creative making |  Logical reasoning
 Critical thinking |  Responding to questions
appropriately, giving reasons
for actions taken
Instructional Strategies: Recitation, guided discovery
Instructional Resources: Holy Qur’an, Islamic CD about the importance of the
Surah.

PRIMARY ONE | TEACHERS’ RESOURCE BOOK

Teacher’s Activities | Learners’ Activities
 Lead learners to recite/sign Surat An-  Recite/sign Surat An-Nas with
Nas (1-6 verses) from the Holy | correct pronunciation (1-6
</passage>

<passage id="lchk_87ccf675cc344e278f61c86a178d8e51" source="NCDC IRE P.1 TEACHERS RESOURCE BOOK" part="57">
Qur’an | verses) from the Holy Qur’an
 Through guided discovery, share the  Tell/sign the importance of the
importance of the Surah (chapter) | Surah (chapter)
with the learners as they listen to the  Read/braille Surat An-Nas as a
Islamic CD | class, in groups and individually
 Guide the learners to read/braille |  Recite/sign and discuss the
Surat An-Nas | meaning of the key message
 Guide the learners recite/sign and | “Surat An-Nas protects me
discuss the meaning of the key | against evil”.
message.

Guidance on Assessment
 | Assess as the learners recite/sign Surat Annas (1-6 verses)
 | Listen and assess as the learners give the importance of Surat An-Nas This
should be done using the language of instruction.
Sample activity: Reciting Surat Annas

Hint for the Teacher
Importance of Surat An-Nas:
 It helps to get Allah’s protection against evil
 It shows the power of Allah over Satan
 It is used as a dua.

LESSON 3: Memorising Surat An-Nas
Reference: Holy Qur’an, Juzu, Islamic Books
Key message: | Competences:
I can recite Surat An- | The learner:
Nas by heart |  memorises the Holy Qur’an.
 states advantages of memorizing the Holy Qur’an.

ISLAMIC RELIGIOUS EDUCATION

Life Skills | Indicators | Values
 Effective |  Audibility, Fluency, Accuracy, |  Responsibility,
communication | Verbal and non-verbal | appreciation
expression
 | Decision making |  Acceptance, telling
consequences of decisions
made

Instructional Strategies: Demonstration, recitation
Instructional Resources: Holy Qur’an
Teacher’s Activities | Learners’ Activities
 Lead learners to recite/ sign a known |  Recite/sign a dua
dua |  Recite/ sign Surat Annas slowly
 Demonstrate to the learners | from the Qur’an
reciting/signing Surat An-Nnas from |  Recite/ sign the Surah (chapter)
memory slowly as learners listen (1-6 | verse by verse (1-6 verses) from
verses) from the Qur’an | memory after the teacher
 Guide the learners to recite/ sign the |  Recite/ sign as a class, in groups
Surah (chapter) from memory verse | and individually
by verse several times (1-6 verses) |  Recite/sign and discuss the
 Guide the learners to recite/sign and | meaning of the key message “I
discuss the meaning of the key | can recite Surat Annas by heart”
message.

Guidance on Assessment
 | Assess as the learner memorises Surat Annas (1-6 verses) with confidence
and correct articulation of words

Sample activity: Practising memorizing Surat Annas

Hint for the Teacher
Observe as learners memorise… (what?) Use easier steps such as:
Learners recite/sign Ayahs/verses one by one until they complete the Surah
(chapter).

PRIMARY ONE | TEACHERS’ RESOURCE BOOK

Week 3
LESSON 1: Incidents that led to the revelation of Surat An-Nas
Reference: Holy Qur’an, Islamic Books i.e. Bukhari
Key message: | Competences:
I hate evil. | The learner:
 names incidents that led to the revelation of the
Surat Annas

Life Skills | Indicators | Values
 Effective |  Fluency, confidence, audibility, |  Appreciation,
communication | verbal and non- verbal expression | respect,
 Creative |  Logical reasoning | concern,
thinking | responsibility
 Decision making |  Acceptance, asking questions

Instructional Strategies: Storytelling, recitation, memorize
Instructional Resources: Holy Qur’an, Learner’s book
Teacher’s Activities | Learners’ Activities
 Recite/sign Surat An-Nas together |  Recite/ sign the Surah (chapter)
with the learners (1-6 verses) from | (1-6 verses) from the memory
</passage>

<passage id="lchk_7bc4fd2bd1b14712a8cb85dfd8e5e3f4" source="NCDC P1 Curriculum TG" part="170">
Sub-theme 9.1: Types and Means of Transport

Materials
Wall chart showing types and means of transport
Counters
Word cards
Number cards

Preparation
Prepare rhymes and songs for the day's lessons

News
• | Ask learners to tell you their news. Discuss what transport they use when coming to school.
• | Recite a known rhyme

Literacy I
• Identify and describe types of transport
• Reading words related to transport
• Matching words to pictures
• Asking and answering questions

Literacy II
• Prepare learners for writing through finger exercises.
• Learners write patterns and letters h, a ha ha
• Learners write words: water, road, air, and railway.
• They recite a known rhyme.
• Write short sentences.

Mathematics
• Learners count round the class from 1 to 90.
• Continue then from 81-90.
• Learners count in 10s together - 10, 20, 30, 40 etc to 90.
• Learners write number symbols 71-80.
• End with a known counting song.

English
• Teach them new vocabulary "road, water, railway" using the following structures
- What is this? This/That is a . . .
- Where is the . . . . . . ? Here is the . . . . . .

PE
Experience with body and space awareness (Refer to Curriculum)

RE
IRE: | Reading the Quran: Surat Annas (Refer to Curriculum)
Reciting the Surat
CRE: | Plow??? Jesus expressed friendship among people e.g. lonely

Creative Performing Arts (Music)
• Teach a song related to types of transport.
• As learners sing let them move according to the rhythm of the song.

Primary School Curriculum , Teacher’s Guide- Primary 1

9.1. | Types and Means of Transport

Materials
Wall chart showing different means of transport
Number chart
Picture cards
Musical instruments
Abacus
Word cards
Calendar

Preparation
Prepare all the materials above beforehand e.g. picture of cars with number plates.

PE
Experiences with body and space (Refer to Curriculum).

Mathematics
• Learners count 1-90
• Learners name the months of the year
• Using a calendar let learners tell the days of each month, January to June
• They write the month of the year (ordinal numbers e.g. 1st, 2nd, 3rd).

Literacy 1
• Learners name common places related to types and means of transport e.g. bus park, taxi park, bus
stop. Identify where these are if they are near the school and where they can catch a bus, taxi or
bicycle, (borda borda)
• Using a wallchart learners identify means of transport related to common places.
• Learners read words from word cards related to common places and means of transport

Literacy II
• Learners write patterns and letters aha | aha and letters ah, a.
• Learners write words and sentences.

English
• Revise the vocabulary for the previous English lesson (road, water, railway)
• Using a wall chart teach the new vocabulary (i.e. car, bus, and bicycle) | using the following
structures:
- What is this/that? | This is/that is a ...
- What are these/those? | These/those are ...

News
• | Learners tell news related to means of transport.
• | Learners draw their news
• | Learners display and talk about their work.

RE
IRE: Reading the Quran: Annas (Refer to Curriculum)
Importance of Surat Al-Lahab
CRE: What each member of the family contributes to the home.

Creative Performing Arts (Music)
• Learners sing a known song.
• Learners play instruments to accompany the song.
• Learners dance according to the rhythm of the song.

National Curriculum Development Centre

9.1. Types and Means of Transport

Materials
A wall chart showing types of transport
Number cards
Word cards
</passage>

<passage id="lchk_e6dd2d7cb62042abb60b1f95a71f60fa" source="NCDC IRE P.1 TEACHERS RESOURCE BOOK" part="59">
 Decision-making |  Acceptance, making choice |  Appreciation,
 Effective |  Fluency, confidence, | responsibility
communication | audibility, verbal and non-
verbal expression

Instructional Strategies: Recitation, demonstration
Instructional Resources: Holy Qur’an
Teacher’s Activities | Learner’s Activities
 Lead learners to recite/sign any dua |  Recite/sign a known dua
they know |  Recite/sign a dua after the
 Demonstrate reciting a dua using | teacher using Surat An-Nas.
Surat An-Nas |  Practice reciting a dua using
 Guide the learners to recite/sign | Surat An-Nas on their own
Surat An-Nas as a dua on their own |  Recite/sign and discuss the
 Lead learners to recite/sign and | meaning of the key message
discuss the meaning of the key | “Allah gives me protection”.
message.
Guidance on Assessment
 | Assess as the learner recites/ signs a dua using Surat Annas

Sample activity: Practising reciting a dua using Surat An-Nas

Hint for the Teacher
 | Let learners know that when you use Surat An-Nas as a dua, Allah gives you
protection.

PRIMARY ONE | TEACHERS’ RESOURCE BOOK

WEEK 4: THEME 2: Tawhiid (Faith)
SUB-THEME: Allah and His Creation
Learning outcome: The learner is able to understand the principle of Tawhiid

LESSON 1: Belief in the existence of Allah
Reference: Holy Qur’an, Hadith Books -Bukhari, Islamic Website, Islamic Books
e.g. Let us Learn Islam

Key message: | Competences:
Allah is near me | The learner:
 identifies things that show Allah’s existence.
 tells/signs who Allah is.

Life Skills | Indicators | Values
 Effective |  Audibility, fluency, confidence, |  Love,
communication | verbal and non- verbal expression | respect,
 Critical thinking |  Responding to questions | obedience
appropriately,
 | Creative thinking |  Logical reasoning

Instructional Strategies: Guided discovery, recitation.
Instructional Resources: Chart showing different things in the environment

Teacher’s Activities | Learners’ Activities
 Guide learners to say a prayer |  Say a prayer thanking Allah
thanking Allah |  Mention things from the
 Guide the learners to mention things | environment that show the
in the environment that show the | existence of Allah
existence of Allah |  identifying some of the things
 Guide the learners to identify some of | from the chart that show Allah’s
the things from the chart | existence
 Share with the learners who Allah is |  Explain who Allah is.
 Guide learners to recite/ sign a rhyme |  Recite/sign the rhyme about

ISLAMIC RELIGIOUS EDUCATION

Teacher’s Activities | Learners’ Activities
about Allah | Allah
 Guide the learners to recite/sign and |  Recite/sign and discuss the
discuss the meaning of the key | meaning the key message “Allah
message. | is near me.”

Guidance on Assessment
 | Assess as the learner tells/signs who Allah is
 | Listen and assess as the learner identifies at least four things in the
environment that show Allah’s existence.

Sample activity:
A rhyme
Allah, Allah Allah
Created this world
Oh oh oh
He created the people
He created all things
Oh oh oh

Hint for the Teacher
 | Before the lesson, read chapter 59: 22-24 to get information about Allah’s
existence
 | Surat al-Baqarah 2: 29 “Huwa alladhii khalaqa lakum maa fil arudhwi
jamii-a”, “It is He (Allah), who created for you all that is on earth …”
 | Emphasise that Allah is the powerful God who created all that we see and
all that beyond our knowledge.

PRIMARY ONE | TEACHERS’ RESOURCE BOOK
</passage>

<passage id="lchk_7382780b2be149b78ac3b55a01fc1022" source="NCDC P1 Curriculum" part="37">
acceptance and
trust

Assessment Guidelines
 Talk about how he/she relates with others at home
 Tell the importance of being trustworthy
 Talk about how forgiveness leads to acceptance and trust
 Tell how he/she can interact well with others

THEME: DISCOVERING GOD’S GIFT TO ME

Weeks 10-12
Sub-theme | Content | Competences | Life Skills | Values
Discovering |  Revision of God‟s gifts |  Telling gifts God |  Decision |  Appreciation
more of God‟s | i.e. our bodies, people | has given her/him | making |  Love
gift to me: | and other creation |  Talking about |  Critical thinking |  Caring
 God‟s | - Mathew 9: 27-30 | ways in which |  Creative |  Responsibility
family and |  Love and care for | he/she can love | thinking |  Interdependence
his love | babies in a family | and care for a |  Empathy |  Unity
- The story of Jesus’ | baby in a family |  Problem solving |  Cooperation
birth in Bethlehem |  Narrating the |  Effective |  Sympathy
- Luke 1 and 2 | events of the birth | communication
- Things to do to | of Jesus
prepare for Christmas |  Talking about
things they do to
prepare for
Christmas

 | Role-play the birth
of Jesus

Assessment Guidelines
 Tell gifts God has given her/him
 Talk about ways in which he/she can love and care for a baby in a family
 Narrate the events of the birth of Jesus

ISLAMIC RELIGIOUS EDUCATION

TERM 1
TERM 1
THEME 1: READING FROM THE QURAN

Weeks 2-4

Learning Outcome: The learner is able to appreciate, and practise the principles and teachings of
Islam in order to have total submission to the will and laws of God.
Content | Competences | Life skills | Values
The Islamic greeting |  | Saying salaam |  | Effective |  | Respect
(Salaam) |  | Explaining the meaning of | communication |  | Loyalty
salaam |  | Interpersonal |  | Responsibility
 | Telling the importance of salaam | relationship
 | Friendship formation

Surat Al-Fatiha |  | Reciting Surat „Al-Fatiha‟ |  | Decision making |  | Responsibility
 | Telling its meaning and |  | Problem solving |  | Obedience
importance |  | Creative thinking |  | Appreciation
 | Critical thinking |  | Care
 | Loyalty

Assessment Guidelines for Theme 1
 Say salaam
 Explain its meaning and importance
 Recite Surat Al-Fatiha
 Tell the meaning and importance of the Sura

TERM 1
THEME 2: (TAWHIID) FAITH

Weeks 5-7

Learning Outcome: | The learner is able to understand the principle of Tawhiid.
Content | Competences | Life Skills | Values
Worshipping |  | Telling his/her relationship |  | Self awareness |  | Responsibility
 Who am I? | with the creator |  | Problem solving |  | Sense of belonging
 Where did I come from? |  | Appreciating his/her role |  | Creative thinking |  | Respect
 Why was I created? | with God |  | Critical thinking |  | Appreciation
 What is worshipping? |  | Telling the meaning of |  | Assertiveness |  | Confidence
 Places of worship i.e. | worship |  | Unity
mosques and homes |  | Naming the places of
worship

Assessment Guidelines for Theme 2
 Name 2 places of worship
 Tell his/her relationship to the Creator
 Tell the meaning of worship

TERM 1
THEME 3: FIQH (PRACTICES)

Weeks 8 -10

Learning Outcome: The learner is able to recognise and understand the rules and regulations of the
places of worship and the concept of physical purity.
Content | Competences | Life sSkills | Values
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
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
