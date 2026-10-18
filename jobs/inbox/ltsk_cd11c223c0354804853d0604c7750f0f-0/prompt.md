# Job ltsk_cd11c223c0354804853d0604c7750f0f-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 3 lesson(s) below of week 1 of the Islamic Religious Education scheme for Primary Four 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P4: one 40-minute lesson: 2–4 sections; about 12–24 points; meanings, examples and uses; 5–7 activities.

lessonId=lles_7a2654c9ae9a47a39cf72aff4dc20eae: lesson 1, Tuesday, 1 period(s), 40 minutes.
  Unit: Fiqh — Congregational Prayer and Conduct of Prayer (theme: Congregational Prayer and Conduct of Prayer). Lesson: Requirements for congregational prayer — Congregational Prayer and Conduct of Prayer.
  Objectives: By the end of the lesson, learners should be able to give the meaning and requirements of congregational prayer.

lessonId=lles_a4218f25160941c5b89d8e6a5273ac5f: lesson 2, Thursday, 1 period(s), 40 minutes.
  Unit: Fiqh — Congregational Prayer and Conduct of Prayer (theme: Congregational Prayer and Conduct of Prayer). Lesson: Conduct of congregational prayer — Congregational Prayer and Conduct of Prayer.
  Objectives: By the end of the lesson, learners should be able to identify the roles of the Imam and Ma-amuum in prayer.

lessonId=lles_f8795eb3b58f42a4b741868f61322ed0: lesson 3, Friday, 1 period(s), 40 minutes.
  Unit: Fiqh — Congregational Prayer and Conduct of Prayer (theme: Congregational Prayer and Conduct of Prayer). Lesson: Week 1 review — Fiqh — Congregational Prayer and Conduct of Prayer.
  Objectives: Review this week's lessons: Requirements for congregational prayer; Conduct of congregational prayer
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
<passage id="lchk_1599c0a6def246809643a0f88e540244" source="P4 IRE" part="2">
The content covered has been carefully written covering the
different topics in the syllabus. This is an addition to what you had
learnt before schools were closed due to outbreak of COVID-19.
The content is arranged using simple steps for your understanding.
The activities provided in each topic are organised in such a way
that they will enable you to relate with your local environment.
The content is organised into lessons. Each lesson has activities
and summary notes that help you to understand the concepts.
Some lessons have projects that you need to carry out at home
during this period. You are encouraged to work individually as you
do the practical and interactive activities.
Feel free to try out all the activities in this material.
Enjoy learning
1 SELF-STUDY LEARNING
Introductory page
This book has been designed as a self-study material so that you may learn the subject
matter at your own pace. You should work through the material at a time best suited
to yourself while at home. Therefore you need to have time for learning.
General Instructions:
• Get a quiet place for your self-study.
• Have a personal time table.
• Consult with your peers, friends, parents and guardians.
• Get assistance from a nearby teacher/ resource person in case you need help.
• In the materials there are Illustrations, Qur’an Quotations and Hadith.
• While learning, use them to benefit from your learning.
Please enjoy this Self Study material
2 ISLAMIC RELIGIOUS EDUCATION SELF | PRIMARY FOUR
THEME: FIQH
SUB- THEME; Congregational Prayer and Conduct of Prayer.
Lesson: Requirements for Prayer
LEARNING COMPETENCES;
During this lesson you should:
• Give the meaning of “a congregational prayer”
• Give the requirements for the group prayer.
• Pronounce, read, spell, write and use the words related to the lesson.
• Appreciate praying in a group.
Resources you need:
Water in a small jerry can, prayer mat, decent dress, Kanzu, Hijab, a veil, trousers, a
sister or brother.
Key Words:
- Congregation/ group prayer; prayer performed by more than one person led by an
imam
.
Qibla- The direction where Muslims face while in prayer .
Wudhu/ablution- Cleaning some parts of the body before prayer
INTRODUCTION
At home there is work which we do in a group. Can you mention different activities
which you do in groups at home?
Compare your answers with mine
i.e. fetching water, washing utensils, gardening, eating, playing and praying. It is good
to pray at home, can you mention the five daily prayers? In this lesson you are going
to learn about:
i- How prayer in a group is carried out.
ii- Things you need to do for your prayer to be accepted.
ALLAH’S MESSAGE
Prophet Muhammad (P.B.U.H) said: “A congregational prayer is better than individu-
al prayer by twenty seven (27) times”. Another name for a congregational prayer is a
group prayer.
Examples of congregational prayers: Juma prayer, Tarawiih, Idd prayer, funeral prayer
etc. Even the five daily prayers can be performed in a group.
Like other prayers, before performing a congregational prayer, there are things you
3 SELF-STUDY LEARNING
must do so that it is accepted by Allah. These include; be sane, having the rightinten-
tion, performing ablution, clean dress, dressing decently and facing the Qibla.
FOLLOW UP ACTIVITY
Exercise:
a- Write ‘true’ or ‘false’ for a congregational prayer
i- Tarawiih prayer (………..)ii- Juma prayer(………..) iii-Idd prayer(………..) iv-
Five daily prayer
</passage>

<passage id="lchk_c38cad29997d407d9ec1ae000f1bcd99" source="P4 IRE" part="3">
b- This prayer can be performed alone or in a group(√) or (x).
i- Juma prayer(…) ii- Subuhi(...) iii- Magharib(…) iv- Idd prayer. (…)
Activity:
i- With your peers/ friends, performwudhu, dress decently for prayers, get one
person to act as an Imaam and perform a congregational prayer.
THEME: FIQH
SUB- THEME: Congregational Prayer and Conduct of Prayer.
Lesson: Conduct of the congregational prayer
LEARNING COMPETENCES;
During this lesson you should:-
• Demonstrate a congregational prayer.
• Pronounce, read, spell, write and use the words related to the lesson.
• Appreciate praying in a group.
Resources you need:
Prayer mat. decent dress, a veil, trousers, , sisters or brothers.
Key Words:
Imaam– the person who leads Muslims in prayer.
Ma-amuum– One who follows the Imam in a prayer.
Tak-biiratul – Ihram - Saying Allah - Akbar while beginning a prayer.(first Takbiir at
the start of prayer)
Rakah– Swalatround. Or unit of prayer
Sujuud - putting your head on the ground while in prayer (prostration)
INTRODUCTION
It is good for every Muslim to pray in a group (congregation).Mention all prayers per-
formed in a group. Allah the Almighty gives more rewards to those who pray in a group
than those who pray alone. Give reasons why work done in a group is better than work
done by one person. Compare your answers with mine.
Shows equality before Allah, make friends, share ideas, you learn more about your re-
4 ISLAMIC RELIGIOUS EDUCATION SELF | PRIMARY FOUR
ligion, showing respect to one another, solutions about your problem can easily be got,
it has more rewards.
ALLAH’S MESSAGE
In a congregational prayer, ImamLeads and then Ma-amuum follows strictly the ac-
tions of the Imam. Among congregational prayers we have: Jumaprayer (two rakahs),
Idd- Al-fitr (2 rakahs) and Idd- Al-Adhuha prayer (2 rakahs), Tarawiih (11 rakahs),
Swalaatul- Janazah (Funeral prayer/ prayer for the dead), five daily prayers (Subuhi,
Zuhri, Asr, Magharib and Isha’i)
Do you go to the Mosque for Juma prayers?
Give what takes place in a Mosque during Juma prayers.(Discuss with your friends/
peers / parents)
FOLLOW UP ACTIVITY
Exercise:
1. Choose from the brackets the correctnumber ofRakahs (units) for each prayer.
i- Idd…………………………………………….(2, 3,4)
ii- Juma…………………………………………… ….(2, 3,4)
iii-
2. Write the correct answer in the space provided
i- The prayer performed when someone is dead………………………………….
ii- The prayer performed after the completion of Ramadhan………………………
iii- The prayer performed after Isha-i during Ramadhan…………………………..
iv- A congregational prayer performed on Friday…………………………………….
3. Which prayer is performed at the following time?
i- Early in the morning……………………………………
ii- After noon from 4:00p.m to sunset.
iii- At 8:00pm
Activity:
1-Organise your friends, let one of you act as an Imaam and perform a group prayer.
(Invite your parents/ guardian to witness)
Summary :
I have learnt that group prayers are better than an individual prayer. I have learnt
that Allah loves people who pray/ work in a group. I will encourage my friends to al-
ways pray and work in a group.
5 SELF-STUDY LEARNING
THEME: HADITH
SUB- THEME: Impurities
Lesson: Readingand writing a hadith on impurities
LEARNING COMPETENCES;
During this lesson you should:
• Read a Hadith on impurities in Arabic or in transliterated form.
• Write a Hadith on impurities.
• Pronounce, read, spell, write and use the words related to the lesson.
• Appreciate the Hadith on impurities.
Resources you need:
</passage>

<passage id="lchk_1b4b35f2875a4025ab5a04cf2ff6eeff" source="P 4 Religious Education 2019" part="18">
Examples of Jihads (battles) prophets Mohammad fought with non-
believers were; Badir, Handaq and Uhudi
Activity
1. Give the meaning of the following terms in Islam
a) Ihsan
b) Hegira
c) Jihad
d) Miraj
e) Isra
2. Which word means treating people in a cruel way
3. Why did Muslims migrate to Abyssinia
4. Who was the leader of Muslims in Abyssinia
5. Why did Mohammad make a journey to Tait
6. With whom did Mohammad go to Tait
COLLECTED, PRINTED & MARKETED BY ACOSMA EDUCATIONAL SERVICES (0752614244 ) Page 45
Theme: Tawheed (faith)
Unit : the twenty-five prophets
Content
1. Adam
2. Nooh
3. Swaleh
4. Ibrahim
5. Muusa
6. Yunus
7. Zul – kife
8. Al – yasa
9. Aliyaasa
10. Ismail
11. Is – haaq
12. Yakoob
13. Yusuf
14. Daauda
15. Sulaiman
16. Zakarufs
17. Yahya
18. Shauaib
19. Ayuub
20. Haroona
21. Isa
22. Loot
23. Hood
24. Idris
25. Mohammad
Activity
Mention any ten of the prophets of Allah
Theme: Tawheed (faith)
Unit: brief notes about prophets
P.4 TERM III LESSON NOTES FOR IRE
COLLECTED, PRINTED & MARKETED BY ACOSMA EDUCATIONAL SERVICES (0752614244 ) Page 46
Content
1.Adam
He was the first prophet
His wife was Hawa
Their children were Kaabiru and Haabiir
Kaabir (his son) is said to have been the first person to commit murder
2. Nooh
He built an ark
Allah saved him and his family from the floods
Activity
1.Who was the first prophet?
2.Name the two sons of prophet Adam?
3.According to the Quran, who was the first person to commit murder?
4.Who built an ark?
5.Draw Noah being saved from the flood
Theme: Tawheed (Faith)
Unit: Brief notes about prophets
3.Musa
He was a son of Imran
He received the Taurat
He delivered his people from Slavery
4.Isa
Born without a father
His mother was Mariam
He received the Injir
5. Ibrahim
His father was Azan and idol worshippers
Ibrahim rejected idol worship
Ibrahim’s wives were; Sarah and Hajara
Activity
Write two things about lack at the following prophets
Musa
Isa
Ibrahim
Theme: Tawheed (faith)
COLLECTED, PRINTED & MARKETED BY ACOSMA EDUCATIONAL SERVICES (0752614244 ) Page 47
Unit: Holy books
Content
Holy books prophet
Quran Mohammad
Injir Isa
Tauret Muusa
Zabur Daauda
Activity
Complete correctly
Prophet holy book
……………………. Zabur
Musa ……………………….
……………………. Injir
Mohammad …………………………
Theme: Fiqh
Unit: organization for prayers
Content
Before prayers are said the following must be observed
Performing ablution
Observing the right time
Observing a proper dress code
Facing the Kibla
Ablution
During ablution, the following body parts are cleaned
Palms
Mouth
Face
Hands
Legs
Head
Ears
Nose
COLLECTED, PRINTED & MARKETED BY ACOSMA EDUCATIONAL SERVICES (0752614244 ) Page 48
Theme: History of Islam (siira)
Unit: Reasons why most Meccans first rejected Islam
Content:
They considered idol worshipping
They feared to be punished (Islam has harsh punishments for sinners)
e.g.
A fornicator is supposed to be given on hundred strokes of cane
An adulterous person is supposed to be killed by stoning
A thief’s palm is supposed to be chopped off
A murderer is supposed to be killed
They feared to loose respect
They were interested in slavery which Islam rejected
Activity
1. Identify two reasons why the Meccans rebelled against Prophet
Muhammad
2. Define the term sin
3. Name the first convert in Islam
4. Name the city where Prophet Mohammad was born
Theme: fiqh
Unit: prayers
Content
A Muslim must pray five times a day. The prayers are
Fajr or subuhi
Zhuri
Asri
Magribi
Ishaari
An Imam leads Muslims in prayers while a Muazin calls Muslims for
</passage>

<passage id="lchk_cbb1a62bd4a54a3c86239988d6bcd251" source="P4 Islamic Religious Education Notes for Terms 1–3" part="5">
Theme: history of Islam (siira)
Unit : Reasons why most Meccans first rejected Islam
Content:
They considered idol worshipping
They feared to be punished (Islam has harsh punishments for sinners) e.g.
A fornicator is supposed to be given on hundred strokes of cane
An adulterous person is supposed to be killed by stoning
A thief’s palm is supposed to be chopped off
A murderer is supposed to be killed
They feared to lose respect
They were interested in slavery which Islam rejected
Activity
1. Identify two reasons why the Meccans rebelled against Prophet Muhammad
2. Define the term sin
3. Name the first convert in Islam
4. Name the city where Prophet Mohammad was born
Theme: fiqh
Unit: prayers
© Email: tekule@tekartlearning.com Website: www.tekartlearning.com
Page 11
Content
A Muslim must pray five times a day. The prayers are
Fajr or subuhi
Zhuri
Asri
Magribi
Ishaari
An Imam leads Muslims in prayers while a Muazin calls Muslims for prayers ma – amuunaa are the followers of the Imam
Activity
1. Name the five daily prayers performed by Muslims
2. What is the role of these people?
a) Muazeen
b) Imam
c) Ma-amuuna
Theme: history of Islam
Unit : Migration of early Muslims
Content
When Prophet Mohammad saw the Muslims being persecuted, he ordered them to migrate to other areas. Persecution is to
treat a person in an unfriendly way
Prophet Mohammad first went to Tait for safety before he finally went to Medina
Mohammad’s journey from Mecca to Medina
Activity
1. Briefly define “persecution”
2. Name the neighbouring town where Prophet Mohammad went to before going to Mecca
3. Why did Prophet Mohammad go to Tait?
4. What is Hejira?
Theme: Hejira
Unit: Problems met during Hejira
Content
Shortage of enough food
Lack of accommodation
Scorching sunshine
Long journey distance
Being looked for by idol worshippers
Shortage of fresh water
Causes of Hejira
Persecution of new converts
Non believer warned to kill Muslim converts
Command from Allah
Activity
1. Identify the problem met during Hejira
2. Point out any three of the causes of Hejira
</passage>

<passage id="lchk_73c563984d8649a993877d865e8eb60c" source="P 4 Comprehension Lesson Notes Term III" part="6">
TOPIC: Expression of the future
SUB – TOPIC: Expression of the future
SKILLS: Listening, Speaking, Reading, Writing
Vocabulary
Tomorrow, next day, next week, next month, shall not, will not, arrive, reach, borrow, lend, library,
note book, text book.
Activity one
Use the words in the brackets to complete these sentences
1. The ________ of the king surprised everybody. (arrive)
2. We ________ story books from the library yesterday (borrow)
3. How may ________ do you have at your school. (library)
4. Tom ________ Jane five thousand shillings last Saturday . (lend)
5. At what time did you ________ school yesterday. (to reach)
Use the most suitable word to complete the sentences correctly
6. We arrived ________ the park very late.
7. The children borrowed some novels ________ the library.
8. The president arrived ________ Entebbe at night.
Write the following in full
9. shan’t
10. won’t
11. arr.
12. dep.
13. e.g.
Give the plural forms of these words
14. library
15. text book
16. notebook
Re-write the following sentences giving one word for the underlined group of words
18
17. Stephen has gone to a place where books are kept for reading purpose.
18. My uncle is the man who takes charge of the library at our school.
Use the words below in sentences to show that you know the difference in their meaning
19. Reach
20. Rich
21. Arrive
22. Alive
Re-write the following sentences as instructed in the brackets
23. The barbers arrived at the barber’s very late. (Rewrite using ...............reach...............)
24. The carpenter arrived at 9:00pm. (Use...................reached ....................)
25. The pupils borrowed a book from the librarian. (Use...........lent.....................)
26. The head teacher lent me ten thousand shillings. (Use..........borrowed.................)
27. Scovia lent a text book to Bob. (Use ..............borrowed.................)
28. We are going to Kampala now. (Re-write and end .....................tomorrow.)
Date Class Subject No. of pupils Time
P.4 Grammar
TOPIC: Expression of the future
SUB – TOPIC: Expression of the future
SKILLS: Listening, Speaking, Reading, Writing
Lesson two
Use of “will” and “shall”
Here, shall and will are used when expressing the future.
N.B:
a) I / we are used with “shall”
b) You/ she / he / they are used with “will”
Note that the short form of shall not is shan’t and the short form of will not is won’t.
Change the following sentences from affirmative to negative and interrogative
Examples
1. I shall go to school tomorrow
I shall not go to school tomorrow
Shall I go to school tomorrow?
No, I shan’t.
2. Alice will go to Kampala next week
Alice will not go to Kampala next week
19
Will Alice go to Kampala next week?
Yes, she will.
Activity
Use “shall” / “will” to complete the following sentences
1. I __________ feed the baby next Sunday.
2. They __________ weave a mat ext Saturday
3. We __________ watch football tomorrow.
4. He __________ not make a call to him next week.
5. __________ we travel to Nairobi next week.
Make 5 correct sentences from the table below
He
I
Fiona
We
You
They
will
shall
will not
shall not
weave a mat
travel to Nairobi
visit the dentist
borrow the book
watch football
feed the baby
make a call to him
withdraw all the money
next week
next Thursday
tomorrow
next month
next Sunday
Re-write the following sentences as instructed in the brackets
1. We shall not go to school next Monday, shall we? (Re-write ending.................. shan’t we?
</passage>

<passage id="lchk_2e672c4992c84ee99d428530f09345ea" source="P4 IRE" part="14">
1. Fill the gaps in the following hadith concerning cleanliness.
Abdullah the son of Umar reported that Prophet Muhammad (P.B.U.H) said, “Allah
does not accept a………… that was not performed in the state of ……….. nor does He
accept ………. from what has been ………….”
ACTIVITY
2. Read a hadith concerning cleanliness
29 SELF-STUDY LEARNING
THEME: HADITH
SUB-THEME: A hadith concerning cleanliness.
Lesson: Meaning of a hadith concerning cleanliness.
LEARNING COMPETENCES;
During this lesson you should:-
• Give the meaning of a hadith concerning cleanliness.
• Pronounce, read, spell, write and use the words related to the lesson correctly.
Resources you need:
Time, Qur’an, learning notes, an Exercise book and pen.
Key Words:
Sadaqah: Charity
INTRODUCTION:
You are welcome to this lesson. You are going to learn the meaning of the Hadith con-
cerning cleanliness.You have known how prayers cannot be accepted without ablution.
A person who is dirty is disliked in the community. Therefore you have to be thankful
to the teachings of Islam on cleanliness. What steps do you take to brush your teeth?
Compare your answer with mine
Get a tooth brush, water, puttoothpaste on your tooth brush, but first brush your
teeth with a toothbrush without tooth paste to remove foodparticles in the teeth. Then
use tooth paste andclean allparts of the teeth including the tongue. Then rinse the
mouth,. Share this with your family member.
ALLAH’S MESSAGE
The Hadith on cleanliness was narrated by Abdullah bin Umar said, “He heard the Proph-
et saying that people’s prayer (Swalat) are not accepted by Allah unless when someone
is clean.
He further tells us that Allah does not accept any Sadaqah from money or something
which is stolen.
Some people perform prayers while they don’t have ablution. Others go for prayers
while putting on clothes which are not clean. Therefore a Muslim is advised to check
him/ herself before going to perform any Swalat. Charity is not only giving out money.
Allah does not accept any charity from what has been stolen.
FOLLOW UP ACTIVITY
Exercise:
1- Give the meaning of the hadith concerning cleanliness.
Activity :
1- Tell your friends the importance of keeping your body and clothes clean.
30 ISLAMIC RELIGIOUS EDUCATION SELF | PRIMARY FOUR
THEME: HADITH
SUB-THEME: Meaning of Hadith Concerning Cleanliness
Lesson: Lessons learnt from Hadith concerning cleanliness.
LEARNING COMPETENCES;
During this lesson you should:-
• Give the lessons learnt from Hadith concerning cleanliness.
• Pronounce, read, spell, write and use the words related to the lesson correctly.
Resources you need:
, Qur’an, learning notes, an Exercise book and pen.
Key Words:
Purity: cleanliness
INTRODUCTION
A person who is clean appears good, liked by many people and gets rewards from Al-
lah. How do you fill when a dirty person sits near you? You should always stay clean if
you want respect from people.
ALLAH’S MESSAGE
Abdullah the son of Umar reported that Prophet Muhammad (P.B.U.H) said, “Allah
does not accept a prayer that was not performed in the state of purity nor does He
accept charity from what has been stolen”
- Cleanliness is one of the conditions for prayer to be accepted by Allah.
- Dirtiness is a bad practice.
- Allah does not accept Sadaqah from stolen things.
- Theft is against the teaching of Islam.
FOLLOW UP ACTIVITY
Exercise
1. Give three lessons learnt from the Hadith concerning cleanliness.
2. Write ‘correct’ or ‘wrong’ in the following gaps.
</passage>

<passage id="lchk_7098142dafa44329a70e46a15474e5b4" source="P 4 Religious Education 2019" part="19">
prayers ma – amuunaa are the followers of the Imam
Activity.
1. Name the five daily prayers performed by Muslims
2. What is the role of these people?
a) Muazeen
b) Imam
c) Ma-amuuna
COLLECTED, PRINTED & MARKETED BY ACOSMA EDUCATIONAL SERVICES (0752614244 ) Page 49
Theme: history of Islam
Unit: Migration of early Muslims
Content
When Prophet Mohammad saw the Muslims being persecuted, he
ordered them to migrate to other areas. Persecution is to treat a
person in an unfriendly way
Prophet Mohammad first went to Tait for safety before he finally went
to Medina
Mohammad’s journey fro m Mecca to Medina
Activity.
1. Briefly define “persecution”
2. Name the neighbouring town where Prophet Mohammad went to
before going to Mecca
3. Why did Prophet Mohammad go to Tait?
4. What is Hejira?
Theme: Hejira
Unit: Problems met during Hejira
Content
Shortage of enough food
Lack of accommodation
Scorching sunshine
Long journey distance
Being looked for by idol worshippers
Shortage of fresh water
Causes of Hejira
Persecution of new converts
Non-believer warned to kill Muslim converts
Command from Allah
Activity
1. Identify the problem met during Hejira
2. Point out any three of the causes of Hejira
COLLECTED, PRINTED & MARKETED BY ACOSMA EDUCATIONAL SERVICES (0752614244 ) Page 50
</passage>

<passage id="lchk_f58e59c0dd6744c7ae1b7f27d254f329" source="P4 CRE" part="15">
• Exercise book
Introduction:
What are some of the things you do and they either make mummy happy or annoyed.
Compare your answers with mine here. Going to school, washing plates, refusing to
fetch water etc.
Key words
Decision is to make a choice
Step 1:
At home they have organized a birthday party for you on a school day. There is also
end of Term exams. Can you choose what to miss?
Step 2:
So in today’s lesson, you are going to learn about decision making. Decision Making
is coming up with a choice. The decision we make can either be good or bad.
The good decision will make us as Christians to be strong and happy and God will be
pleased with them.
Types of decision
1. Good decision
46 CHRISTIAN RELIGIOUS EDUCATION |PRIMARY FOUR
2. Bad decision
Examples of good decisions
Going to school
Helping parents at home etc.
Examples of bad decision
Stealing
Abusing people (mention more)
Importance of making good decision
• We achieve /get what we want in life
• You become happy in life and our parents.
Consequences of making bad/wrong decision
1. Bad decision bring sadness or misery (not being happy
- You become ashamed
- You lose Friends
- You end up suffering etc.
All in all the decision you make will direct your life so be careful when making any
decision.
Step 3:
Exercise
1. Write down any two types of decisions.
2. Give any two examples of good decisions
3. Which type of decision would you prefer to make?
Activity
Get a pen/brail machine and list down good decision you would make while at home.
Hope you can now take decision.
47 SELF-STUDY LEARNING
TOPIC: MAKING OUR DECISION AS CHRISTIANS
Sub-topic: Decision Making
Lesson: People who made good and bad decision in the Bible
Competence:
You should be able to:
• Identify the people who made good decision in the Bible
• Tell the decision they made.
Materials you will need
• Self-study material
• Pen,
• Pencil
• Exercise book
Introduction:
How you your parents and brother feel about you when you perform well in class?
Happy, excited etc.
Key words:
Step 1
In your last lesson, you learnt about making decision.
What is a decision?
Give two types of decision.
Step 2:
In our last lesson, you learnt about Good and bad decision. Do you still remember
them? Right
Your lesson today is about people who made good /bad decision e.g
Solomon made a right decision of asking for wisdom.
Mary – accepted the message from Angel Gabriel that she would be mother of Jesus.
Cain took a wrong decision of killing brother Abel. (Genesis 4:1-12)
Judas Iscariot was one of the twelve disciple of Jesus and made a wrong decision to
betray Jesus.
In conclusion, God gave us free will to choose and make our own decision. In doing so
we should try to make good decision to enable ourselves to live good and happy lives.
48 CHRISTIAN RELIGIOUS EDUCATION |PRIMARY FOUR
Step 3
Exercise
Who was the bad brother of Abel?
Which disciple betrayed Jesus...?
Name the Angel who brought the good news to Mary ………………………
Give one good decision that King Solomon made...
Mention other person who made good decision in the Bible ………………
Activity
What happens if you don’t listen to your parents today?
Which advice to you give to your friend who doesn’t want to go to school?
Hope you make a right decision now, pray to ask God for guidance.
49 SELF-STUDY LEARNING
TOPIC: Peace
Sub-topic: Peace Initiative in African Tradition.
Lesson: How peace is created.
Competence:
You should be able to:
• Give the meaning of peace
• Mention ways of initiating peace
</passage>

<passage id="lchk_3c95ad41c97e4b73a30793648397ab72" source="Kesk P4 RE Workbook 1" part="60">
A product of Kolfram Educational Services Kampala 0777886622/ 0786941943/ 0756821512/ 0784044408 82
For quality and improved learning materials, always use Kolfram Educational Services products
In Luke 12:22 – 23 Jesus Assured us that God will always solve our problems because he
know them.
In Psalms 40:12 – 17 the writer asks God to help him overcome his problems with faith
Verse to remember: “Instead look for the kingdom and he will provide you with these
things Luke 12:31
Prayer: “Oh God help us at all times to seek and promote peace and comfort from you
Amen”
Response to the message
“I will seek peace from God”
ACTIVITY
1. Ho w can we look for God’s peace ?
i)_______________________________________________________________________________
ii) ______________________________________________________________________________
2. What did Jesus leave his disciples with?
i)_______________________________________________________________________________
ii) ______________________________________________________________________________
3. What can we do in order to promote peace?
i)_______________________________________________________________________________
ii) ______________________________________________________________________________
LESSON
Reconciliation
Reconciliation is the restoration of broken relationship between two or more disagreeing
parties.
Reconciling means bringing back a broken relationship
Causes of misunderstandings
1. Adultery
2. Back biting
3. Greed
4. False accusation
5. Suspicion of witchcraft.
Importance of reconciliation
1. It restores friendship and love
2. It restores personal communications.
3. Prevents bitterness and revenge.
4. Working together is restored.
5. Misunderstandings are easily corrected
6. Promotes peace and harmony
ACTIVITY
1. Define the term reconciliation.
_________________________________________________________________________
_________________________________________________________________________
2. State any two causes of misunderstandings.
i)_______________________________________________________________________________
ii) ______________________________________________________________________________
3. Suggest any two ways of reconciling among people.
i)_______________________________________________________________________________
ii) ______________________________________________________________________________
4. Mention any two importance of reconciliation.
i)_______________________________________________________________________________
ii) ______________________________________________________________________________
LESSON
STANDARD KOLFRAM IN USE: ABRIDGED CURRICULUM P.4 CHRISTIAN RELIGIOUS EDUCATION WORKBOOK
A product of Kolfram Educational Services Kampala 0777886622/ 0786941943/ 0756821512/ 0784044408 83
For quality and improved learning materials, always use Kolfram Educational Services products
Traditional ways of reconciliation
1. Arbitration
2. Using mediators like elders, chiefs and clan heads.
3. Shaking hands
4. Paying fines
5. Apologizing
6. Sharing meals.
Traditional ways of reconciling with God
Sacrificing animals to God
Process/steps involved in traditional reconciliation
1. Identifying a conflict.
2. Informing elders in the community.
3. Elders talk to people involved the conflict.
4. Asking people who know anything about the conflict.
5. Giving people in the conflict to explain.
6. Members present may give advice or ask questions.
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
