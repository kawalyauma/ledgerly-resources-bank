# Job ltsk_959b79e586ec420d9b9b817451bf497a-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 5 lesson(s) below of week 1 of the Social Studies scheme for Primary Five 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P5: one 40-minute lesson: 3–5 sections; about 14–28 points (meaning, examples, reasons, problems and solutions as the passages give); 5–8 activities.

lessonId=lles_ea27eef39bc04f1b80544b7836e833a8: lesson 1, Monday, 1 period(s), 40 minutes.
  Unit: Uganda as an independent nation (theme: Living together in Uganda). Lesson: Independence — Meaning of independence and characteristics of an independent nation.
  Objectives: Define independence; State the characteristics of an independent nation

lessonId=lles_4ffc3c8c5282426c8fd1dd71d712a007: lesson 2, Tuesday, 1 period(s), 40 minutes.
  Unit: Uganda as an independent nation (theme: Living together in Uganda). Lesson: The national flag — Symbols of a nation: the national flag.
  Objectives: Name the symbols of a nation; Describe the colours of the national flag and what they stand for

lessonId=lles_982fb9e85e004d528bb9517124377890: lesson 3, Wednesday, 1 period(s), 40 minutes.
  Unit: Uganda as an independent nation (theme: Living together in Uganda). Lesson: The national anthem — Symbols of a nation: the national anthem.
  Objectives: Name the composer of the national anthem; State occasions when the national anthem is sung

lessonId=lles_4430a2b499fc4a4b9ca9dc331eb0da41: lesson 4, Thursday, 1 period(s), 40 minutes.
  Unit: Uganda as an independent nation (theme: Living together in Uganda). Lesson: The national coat of arms — Features of the coat of arms.
  Objectives: Draw the coat of arms; Name the features of the coat of arms

lessonId=lles_fcaf265518c64dde8444330b8da2a508: lesson 5, Friday, 1 period(s), 40 minutes.
  Unit: Uganda as an independent nation (theme: Living together in Uganda). Lesson: The national motto and the coat of arms — Significance of the coat of arms and its features.
  Objectives: State the national motto; Give the significance of the features of the coat of arms
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points ('- ' points, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

Write, using ONLY the passages below. Passages from "NCDC" documents are the official base for what to teach; NCDC lower-primary thematic curricula put every learning area in columns separated by " | ": use only the Social Studies column.
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
<passage id="lchk_1162553670784949a6a5f4ead61c3374" source="P.5 SST SCHEME TERM III 2019" part="1">
SCHEME OF WORK:
SUBJECT: SOCIAL STUDIES CLASS: P.5 SUBJECT TEACHER ………………………………………………….. TERM THREE YEAR ………………….
WK
PD
Theme
Topic
Sub-Topic
Competence
Content
Methods and Techniques
Life skills and values
( Indicators)
Suggested activities
Teaching / learning aids
Ref
Re
Subject
Language
1
1
LIVING TOGETHER IN UGANDA
Uganda as an independent nation
Independence
-Explain the
word political
-Independence
-Independent
-Pronounce, spell, write , read words to independence
Independence
-definition – is the state of being free from foreign control or rule.
Characteristics of an independent nation
-Territory of land.
-Government
-Constitution
-Parliament
-Judiciary
-Freedom
-Police to keep law and order
-Citizens
-Control its affairs
-Explanation
-Discussion
-Brain storming
-Question and answer
-Self esteem
-Negotiation
-Problem solving
-Define and explain the word independence.
-Discuss the characteristics of an independence nation
-Dramatizing
-Text books
-Children’s properties
-Functional SST book 5 page 165
MK Standard page 117
2
Symbols of a nation (The national flag)
-Identify national symbols and explain their significances
Spells , reads, pronounces and writes words and sentences related to symbols of the nation.
The symbols of the nation.
-The National flag.
-National Anthem
-Coat of Arms
-Emblem
-language (English)
-The constitution (supreme law)
National flag
-Concept
-The designer
(Grace Nsingira)
-The colours of the flag
-Areas where it can be flown.
-How and when its flown.
-Signifance of the national flag.
-Explanation
-Discussion
-Question and answer
-Self discovery
-Effective communication
-Appreciation
-Self awareness
-observation
-Respect
-love
-caring
-Drawing and shading
-Practice how to raise fly the national flag.
-national flag
-Pictures of the national flag.
-Text book
Mk std
\bk 5
Pg 12506
Teachers guid
Pg 222
1
3
LIVING TOGETHER IN UGANDA
Uganda as an independent nation
Symbols of a nation (The National Anthem
-Identify and explain the National Anthem. (stanza) and the coat of Arms
-Reads, spell, pronounce and write words found in the Anthem and Coat of Arms
National Anthem
-Concept (3 stanzas)
-The composer (George William Kakoma)
-Occasions when its sung.
(British National Anthem) was sung before Independence.
-Significances.
-Discussion
-Discovery
-Explanation
-Appreciation
-Self awareness
-Effective communication
-Observation
-Analyse
-Respect
-Singing and practicing the Anthem
-Papers having the National Anthem
MK stdbk 5 pg 123-4
4
&
5
The national coat of Arm
National Coat of Arms.
-Concepts
-Features of the coat of Arms.
-The National Motto
-Significance of The Coat of Arms.
-Significances of the features of the coat of Arms.
-Discussion
-Question and answer
-Drawing
-Patriotism
-Respect
-Drawing and indicating the features of he coat of Arms
-Coat of Arms.
-Chart showing the coat of Arms
MK stdbk 5 page 126-127
2
1
LIVING TOGETHER IN UGANDA
Uganda as an independent nation
Symbols of a nation (The Emblem)
-Name and identify the emblem and give its significances
-Spell, read, pronounce the words related to the National emblem
Emblem
-Concepts (crested crane)
-Reasons why it was chosen as the emblem.
-Documents where its found.
-Significances.
-Discussion
-Explanation
-Discovery
-Appreciation
-Description
-Inquiry
-Drawing
-Critical thinking
-Love
-Caring
-Respect
-Drawing the emblem and shading
-Pictures of the emblem
Mk stdbk 5 page 128
2
The National Language
-Name the Local languages.
</passage>

<passage id="lchk_6816a0521efb434a8d222966ed00fd03" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="6">
 The national coat of arms is a symbol by which our nation if identified.
Features on the coat of arms
i) The crested crane
 It is the emblem of Uganda
 The crested crane stands on one leg to show that Uganda is going forward, interms of
development.
14
ii) The sun
 It shows that Uganda is found along the Equator.
 It shows that Uganda receives sunshine throughout the year it has good climate.
iii) The Kob
 It represents the rich wildlife of Uganda and the beautiful animals that earn Uganda foreign
exchange by attracting tourists.
iv) Coffee and Cotton
 These show that Uganda is an agricultural country.
 They are the chief export cash crops of Uganda.
v) Blue stripes of water entering the shield from the bottom
 These represent the source of River Nile which is found in Uganda.
vi) The drum
 It represents Uganda’s culture.
 It represents traditional means of communication
 It represents traditional musical instrument for entertainment.
vii) Shield and spears
 They represent the traditional weapons used by Ugandans for defence.
 They show that Uganda is ready to defend herself against her enemies.
viii) Uganda motto (for God and my country)
 It represents the spirit of nationalism.
 It shows that Ugandans are God fearing
ix) Blue stripes of water at the top of the shield
 These stripes represent the great lakes and rivers of Uganda.
x) The black colour
 This represents the black skinned people of Uganda.
xi) Landscape with green colour
 It represents the abundant green vegetation of Uganda
xii) Green hills
 These symbolize the many physical features of the country.
Uses of coat of arms
 The Uganda coat of arms is used on national paper currency and coins to distinguish them
from those countries.
15
 It is hung up in government places such as courts and offices to symbolize power and
authority
 It is printed on letter heads and official documents for government official use.
 It is used on the government seal for endorsement of documents.
 It is put/ mounted on the president’s car as a number plate
Activity
1. Who designed the Uganda Coat of Arms?
2. State one event that took place on Independence Day.
3. Name the personalities that held the following positions on independence.
4. Prime minister
5. President
6. What are national symbols?
7. Name one place where we find the coat of arms
8. Which political party led Uganda to independence?
9. Mention one document on which the coat of arms is printed
10. State Uganda’s national motto.
11. What feature on the coat of arms symbolize that Uganda is an agricultural coutry?
12. What do the Blue stripes on the Uganda Coat of Arms symbolize?
Date Class Subject No. of pupils Time
P.5
TOPIC: Uganda as an Independent nation
SUB –TOPIC: The National language
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic:- coat of arms, bottom, kob, shield,
CONTENT: THE NATIONAL LANGUAGE
 A national language is any one common language which is widely spoken by the majority of
the people in a country and is officially adopted for that purpose.
 Uganda doesn’t have a national language but it has English as her official language.
Importance of having a national language in a country
 It promotes unity among people in the country.
 It ensures easy communication in the country.
16
Why has Uganda failed to get her national language?
 It has got many traditional languages
The National Capital City
</passage>

<passage id="lchk_3dedebb31c1e4c9783852eb0a4fc6cfb" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="5">
How does the red colour in our national flag foster unity among Ugandan?
 It shows that all people regardless of race, colour, language , religion, cultural and social
back grown have same colour of blood.
 It emphasizes international brother hood.
THE UGANDA NATIONAL FLAG
THE CRESTED CRANE
 This is Uganda’s national emblem
 It is the visible symbol that represents a nation
Why does a crested crane stand on one leg?
 It shows that Uganda is moving forward in terms of development.
Reasons why the crested crane was chosen as Uganda’s Emblem
 The crested crane has the three colours of the national flag.
 It is a gentle bird.
 It is graceful
 It is a beautiful bird.
What does the crested crane represent?
 It represents gracefulness, beauty and peacefulness of the people of Uganda.
 It represents the gentility of the people of Uganda.
12
Why is a national flag important to our country?
 The national flag promotes national unity.
 It is for identification.
Ways through which the National Flag is used
 The national flag should be raised early in the morning on public buildings and in places
where national or official duties/ activities are taking place and lowered late in the evening.
 The flag must be flown with the Crested Crane facing the flag pole.
 The flag is raised at a half mast when an important person died or there is a national disaster.
 Some people match following bands like school band, Army, Police etc to demonstrate a
cause of national interest bands carry flags and should be held in front of those maching.
 The national flag is flown on president’s car, ministers and judges’ cars when these officers
are travelling.
Taking care of the National flag
 Our national flag must always be respected.
 The flag should never be allowed to touch and anything below it such as ground or water.
 It should never have anything placed upon it or pinned on to it.
 The flag should never be used for commercial advertising.
 The flag is not supposed to be used as clothing.
 When it is raised or brought down the people near the flag pole should stop moving until the
flag is up or held by the person in charge.
Examples of places where the national flag is flown
 The parliament
 Official car of the president while traveling and other government officers.
 Government departments/ offices
 The office of the resident district commissioners.
 Institutions of learning, such as schools.
 Individuals can also hand the nationals flag in their offices, in class or on their tables
Activity
1. What is the name of the bird in the middle of the Uganda flag?
2. Of what importance is a flag pole?
3. Give one way the National flag is respected.
4. How does the red colour of the Uganda promote unity world wide?
13
5. Identify the last colour of the Uganda National flag.
6. Give two importance of A national flag.
7. Which school attribute is similar to the school national flag?
8. Why should the crested crane on the Uganda flag face the flag pole when raised?
9. Why does the crested crane on the Uganda flag stand on one leg?
Date Class Subject No. of pupils Time
P.5
TOPIC: Uganda as an Independent nation
SUB –TOPIC: The National Coat of Arms
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic:- coat of arms, bottom, kob, shield,
motto, nationalism, documents, agricultural
Content: THE NATIONAL COAT OF ARMS
Importance / significance
- Power and authority
- National heritage
</passage>

<passage id="lchk_b297e6921590437280a1192ded841240" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="4">
How many stanzas has the Uganda national anthem?
 There three stanzas of the Uganda national anthem.
The National Anthem
1. Oh Uganda! May God uphold thee,
We lay our future in thy hand,
United free for liberty,
Together we’ll always stand.
2. Oh Uganda! The land of freedom,
Our love and labour we give,
And with neighbours all,
At our country’s call,
In peace and friendship we’ll live.
3. Oh Uganda! The land that feeds us,
9
By sun and fertile soil grown,
For our own dear land
We shall always stand
When and how the stanzas of the national anthem are sung?
 At the opening of any function of national importance.
Messages of the National Anthem
 Belief in one God.
 Determination to remain free from foreign control.
 Desire to live at peace with our neighbours.
 To remind people about the fertile soil and favorable climate of Uganda.
Respect for the National Anthem
 When the national anthem is being sung all the people should stand still or at attention and
remain in one place until it is completed.
Reasons why we should respect the National Anthem when it is being sung
 To pray to God for our nation
 To respect our nation, which is more important than all other things in the country
 To remind us f our national duties
 It shows national unity
The importance of the national anthem during national anthem occasions
 To express the national beliefs of the nation
 To show national identify
 To remember the rich environment of Uganda
 To promote unity among the people
Activity
1. Why is Late. George William Kakoma remembered in the history of Uganda.
2. Give two reasons why Ugandans sing the national anthem
3. Apart from the national anthem, outline two other attributes of a nation.
4. When was the national anthem played for the first time in Uganda?
10
5. Give one way school children express the spirit of nationalism when on assemblies.
6. In which stanza of the Uganda National Anthem is the statement;
a. At our country’s call?
b. United free for Liberty?
c. By sun and fertile soil grown?
7. How is the National Anthem respected when its being sung?
Date Class Subject No. of pupils Time
P.5
TOPIC: Uganda as an Independent nation
SUB –TOPIC: The Uganda national flag
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic:- black, yellow, red, flag, crested
crane
Content: The Uganda national flag – Signifies unity among Ugandans
 Before getting independence. Uganda used the British flag known as the union jack
How was the union jack treated on 9 th October 1962?
 The Union Jack was lowered and Uganda national flag was raised.
Who was responsible for the ceremony of lowering the union jack and raising our flag?
 He was major Kanuti Akorimo
When was the Uganda National flag first raised?
 The Uganda National flag was first raised on Monday 9 th October 1962?
Who designed the Uganda national flag?
 Grace Ibingira assisted by Paul Mukasa
The colours of the Uganda national flag
 The Uganda national flag has three colours. Namely;
 Black
 Yellow
 Red
Meaning of each colour
A: THE BLACK COLOUR
 The black shows Uganda as a black African country.
 It signifies that Ugandans are dark skinned people / Africans
11
B: THE YELLOW COLOUR
 What does the yellow colour symbolize?
 The yellow colour symbolizes sun shine.
 It shows that the Equator passes through Uganda and therefore country enjoys sunshine
throughout the year.
C: THE RED COLOUR
 The Red colour signifies international brother hood.
</passage>

<passage id="lchk_a8d263adf25145d9b9a94e0acaa20555" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="1">
1
P.5 SST LESSON NOTES FOR TERM III
Date Class Subject No. of pupils Time
P.5
TOPIC: Uganda as an Independent nation
SUB –TOPIC: The Independence of Uganda
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic:- Nation, independence, state,
Freedom, foreign
Content: Independence
The independence of Uganda
a) The meaning of independence
 Independence is when a country is free from foreign political, social and economic
influence.
 It is when the highest power in a country is transferred into the hands of the citizens.
When did Uganda get her independence?
 Uganda got her independence on Monday 9 th October 1962.
What conference was the climax of all Uganda’s struggle for independence?
 It was the London constitutional conference.
Who was the first prime minister of independent Uganda?
 Apollo Milton obote
Who was the first president of Uganda in 1963?
 Sir Edward Muteesa II
Who was the first non executive president of Uganda?
 Sir Edward Muteesa II
Name the first vice president of the non executive Uganda?
 He was Wilberforce Nadiope
Who had power to appoint ministers in Uganda in 1964?
 The prime minister had power to appoint ministers in Uganda in 1964
A nation
The meaning of a nation
 A nation is a large community of people united by common aspiration/ aims which
makes them to want to be under one government.
 A group of people with the same history, culture and language under one government.
2
Type of a nation
 Heterogenous nation
 Monolithic nation
Heterogenous nation
 These are nations composed of different groups of people with different culture, origin
and languages but share the same territory.
Examples of Heterogenous nations
 Uganda
 Kenya
 Tanzania
 Nigeria
Monolithic nations
 These are nations with a common origin, langauge, history, and cultural institutions.
 These are nations made up of people of the same ethnic group.
Examples of monolithic nations
 Rwanda
 Burundi
 Swaziland
 Lesotho
 Saudi Arabia
Characteristics of a nation
 It has a common culture.
 It has a common language
 It shares a common ethnicity or heritage
 Has a common desire.
A STATE
What is a state?
 A state refers to a country considered as an organized political community controlled by
one government.
Characteristics of a state
 It has a national leader.
 It is not controlled by any other country
3
 It has clearly marked boundaries
 Its citizens should have a sense of belonging
 It has its own citizen.
 It has control over all its territorial areas.
Uganda becomes a republic
What is a republic?
 A republic is the country governed by its own laws with a president as the head of state.
Name the president who abolished kingdoms in Uganda in 1967?
 Apollo Milton Obote
In which year was Uganda declared as a republic
 It was in 1967
Activity
1. What is political independence?
2. How did World War II contribute towards Uganda’s independence? Give three ways.
3. When did Uganda get her independence?
4. How did Ben Kiwanuka became Uganda’s first chief minister?
5. What was Kabaka crisis?
6. What failed Ben Kiwanuka from becoming the first Prime minister of independent
Uganda?
7. What enabled Obote to become the first Executive Prime Minister of Uganda?
8. Who was the first Republican president of Uganda?
9. What political even took place in Uganda in 1967?
10. Give two characteristics of monolithic nations.
11. Why is Uganda regarded as a heterogeneous nation?
</passage>

<passage id="lchk_b6ebfff8d01745efa6141743d019e6df" source="Primary Five Social Studies Notes 2020" part="46">
 To promote democracy
Examples of political parties before independence
 Uganda National Congress (UNC)
 Democratic party (DP)
 United Congress party (UCP)
 Uganda people’s congress (UPC)
 Uganda People’s Union(UPU)
 KabakaYekka(K.Y)
Qn: How did political parties help to fight for independence?
 They united people
 They mobilized people
Political parties and their founders
Political party founder year of formation
U.N.C Ignatius
KangaveMusaazi
1952
D.P Joseph Kasolo 1954
U.P.C Dr. Apollo Milton Obote 1960
K.Y Augustine Kamya
Masembe.S.
1961
203
Qn: What was the first political party to be formed in Uganda?
 UNC(Uganda National Congress)
Qn: Name the two political parties that joined to form U.P.C
 U.N.C (Uganda National Congress)
 U.P.C (Uganda People’s Union)
Qn: How did united Congress Party come into existence?
 After the splitting of U.N.C
Note: It was led by David Lubega
Aims of Democratic Party
 To demand for Uganda’s independence.
 To protect the rights of Catholics in government.
Qn: Which political party won the 1961 general elections ?
 D.p (Democratic Party)
Qn: Who won the 1961 general elections ?
 Benedicto Kiwanuka
Qn: Who was the first chief minister of Uganda ?
 Benedicto Kiwanuka
Qn: What title was given to the leader of government in1961 ?
 Chief Minister
Qn: Which title was given to the leader of government in1962 – 1966?
 Executive Prime Minister
Aims of K.Y
 To protect interests of Buganda
 To secure a favorable political position for Kabaka in the independent
Uganda.
204
Qn: Why did UPC form an alliance with KY IN 1961?
 To win the 1962 general elections
 To destroy the support and influence of democratic party.
Ways how political parties struggled for Uganda’s independence
 By writing news articles against colonialism
 They united people
 They mobilized people
 They organized demonstrations and boycotts
Problems political parties faced in the struggle for independence
 Shortage of funds
 Some leaders were imprisoned
 Disunity among political leaders
 Illiteracy amongpeople.
Qn: What was the aim of the Lancaster conference?
 To plan for Uganda’s independence
Recommendations of the Lancaster conference
i) The leader of Uganda’s government was to be prime minister.
ii) Buganda was to remain part of Uganda.
Note: After the Lancaster conference different kingdoms and chiefdoms
Joined to form Uganda.
TERM THREE
UGANDA AS AN INDEPENDENT NATION
Qn: What is an independent nation ?
205
 This is a country which is free from colonial rule
The independence of Uganda
Questions
1. When did Uganda get her independence ?
 9 th October 1962
2. Which political party led Uganda to her independence ?
 Uganda People’s Congress
3. Who led Uganda to independence ?
 Dr. Apollo Milton Obote
Note: Apollo Milton Obote got instruments of power from Duke of Kent.
4. Name the first executive prime minister of Uganda.
 Dr. Apollo Milton Obote
5. What title was given to the leader of Uganda after independence
 Prime Minister
6. Why did UPC make an alliance with KY in 1962 ?
 To win the independence election
 To reduce the support of DPin Uganda
7. How was the union treated on the Independence day ?
 It was lowered.
Instruments of power Obote got from Duke of Kent .
 Dummy Key
 Uganda flag
 Uganda coat of arms
 Uganda Constitution
206
8. What is a republic ?
 A republic is a country ruled by an elected president
9. Which constitution granted Uganda independence ?
 The 1962 constitution
</passage>

<passage id="lchk_0f400a3753174ca4964cfae5fee9eca7" source="Excel P 5 SST Term III" part="6">
Oh Uganda! the land that feeds us
By sun and fertile soil grown.
For our own dear land,
We'll always stand:
The Pearl of Africa's Crown.
➢ “Oh Uganda,land of beauty” is the country’s official
song. It was composed by George Wilberforce
Kakoma.
➢ George W.Kakoma was assisted by Peter G.Wingard.
➢ It was first officially sung on independence day on
9 th October 1962 by Makerere college school choir,
conducted by a student Catherine Mwandha.
➢ The Uganda national anthem is sung and played
during official functions.It symbolises the country’s
principles, hopes and goals.
➢ The Uganda national anthem has three stanzas . All
the three stanzas are sung to open and close official
and important functions.
NOTE:
✓ If there are other anthems or prayers during a
function, the national anthem is sung first, followed
by other anthems and then a prayer. At the end of the
function, other anthems are sung first and the
national anthem is sung last to close the function.
Occasions where Uganda national anthem is sung
▪ On school assemblies
▪ During parliamentary sessions.
▪ Opening of sports activities.
▪ Opening of school debates.
▪ At official ceremonies
▪ Start of public functions.
Page 11
Importance of the Uganda national anthem.
❖ It promotes national unity.
❖ It promotes nationalism and patriotism.
❖ It is a national prayer for Uganda.
❖ It promotes the fear of God amongst Ugandans.
Respect for the Uganda national anthem.
▪ When singing the national anthem, people must stand up at attention to show
respect to the nation.
▪ When one is unable to stand up, he/she should raise up the right hand.
THE UGANDA COAT OF ARMS.
➢ Uganda coat of arms is composed of a shield and
two spears on a green hill with the Uganda kob on
the left and the crested crane on the right. It is
designed using symbols that summarise important
ideas and things Uganda holds .
➢ It is found on official documents, the national
currency, parliament, the government seal and the
president’s official car.
➢ It is also hung in government institutions like
courts and offices to symbolise power and
authority.
➢ The Uganda coat of arms was designed by Paul
Mukasa.
➢ The Uganda coat of arms acts as a public seal of
Uganda.
➢ The public seal is used to signify the official nature
of government documents that bear its stamp.
Features found on the Uganda coat of arms.
▪ The Uganda Kob.
▪ The crested crane.
▪ The sun.
▪ The drum.
▪ The shield and spear.
▪ The black colour of the shield.
▪ Coffee and cotton.
▪ The Green land scape.
▪ The National Motto.
▪ Blue stripes on top of the shield.
▪ Blue stripes entering the shield at the bottom.
Meaning of features found on the Uganda coat of arms.
❖ The spears and shield represents the traditional means of defence.
❖ The blue stripes at the top represents the water bodies in Uganda.
❖ The blue stripes at the bottom entering the shield represent the source of River
Nile found in Uganda.
❖ The sun represents the abundant sunshine received in Uganda or warm climate
experienced in Uganda.
❖ The drum represents the traditional means of communication.
It also represents the culture of the people of Uganda.
❖ The black colour on the shield symbolises the African race of Ugandans.
❖ The kob represents the rich/abundant wildlife in Uganda.
Page 12
❖ The crested crane represents the gentleness and peaceful nature of the people of
Uganda.
❖ Coffee and cotton on the green hill show the traditional cash crops grown in
Uganda.
</passage>

<passage id="lchk_ce94496dbd07478db4aed434f20a4a6c" source="Excel P 5 SST Term III" part="5">
➢ From 27 th Jul,1985-26 th Jan, 1986 (183days)
❖ He was born in 1914 and died on 3 June 1996.
❖ He took over power from Obote through a military coup on
27 th July, 1985.
❖ He was overthrown by H.E Yoweri K.Museveni on 26 th Jan,
1986.
H.E Yoweri K. Museveni
➢ From 26 th Jan, 1986 up to date .
❖ He was born on 15th September 1944.
❖ He started a g uerilla war against Obote II’s government in
1981.
❖ He took over power from Tito Okello on 26 th January, 1986
using the National Resistance Army (NRA)
Reforms under the NRM government.
▪ Restoration of kingdoms in 1993.
▪ Completion of the 1995 constitution
▪ Women enmpowerment.
▪ Construction of infrastructure.
Page 9
▪ Promotion of democratic elections.
▪ Introduction of UPE and USE.
▪ Ugandans of Asian origin who had been expelled by Amin
Dada were allowed to come back to Uganda.
SYMBOLS OF AN INDEPENDENT NATION.
National symbols are features/items that help one to identify a particular country.
Symbols of an independent nation include;
▪ National anthem
▪ National motto
▪ National currency
▪ National coat of arms
▪ National flag.
▪ National emblem
▪ National constitution
Symbols of Uganda as a nation.
• The Uganda national flag.
• The Uganda national anthem.
• The Uganda national coat of arms.
• The Uganda national seal.
• The Uganda national constitution.
• The Uganda national emblem.
• The Uganda national currency.
Importance of national symbols.
❖ They promote national identity.
❖ They show that a country is independent.
❖ They promote national unity.
❖ They promote the spirit of patriotism.
❖ They show the core values of a nation.
THE UGANDA NATIONAL FLAG.
❖ The Uganda national flag has three colours
ie. black, yellow and red.
❖ The flag has a white circle with a crested
crane in the middle.
❖ The crested crane is standing on one leg
meaning to show that Uganda is moving
forward in development.
❖ The Uganda national flag was designed by
Grace Ibingira.
❖ The Uganda national flag was first raised on
9 th October, 1962, replacing the Union jack.
Meaning of the colours of the Uganda National flag.
(i) Black.
➢ Shows that Uganda is a black African country.
➢ It represents the dark skinned people of Uganda.
(ii) Yellow.
➢ It represents the abundant sunshine received in Uganda.
➢ It also represents Uganda’s tropical climate.
(iii) Red.
➢ It represents the international brotherhood.
Page 10
(iv) White
➢ It stands for the peace enjoyed in Uganda.
Places where the Uganda national flag can be raised.
• Schools
• Airports
• At National radio and TV stations.
• Police stations
• Hospitals
• Government offices
• State house
• Embassies and High Commissions.
How to show respect for the Uganda National flag.
❖ By standing still when it is being raised or lowered.
❖ It is not wet by either washing or by rainfall.
❖ It is not worn as a clothing.
❖ It does not touch the ground when being lowered.
Note:
➢ The Uganda national flag shows national identity.
➢ The Uganda national flag is flown at half mast to show a national mourning.
Conditions that can make a government declare a national mourning.
➢ Death of a very important person in the government.
➢ When there is a major national calamity.
THE UGANDA NATIONAL ANTHEM.
1.
Oh Uganda! may God uphold thee,
We lay our future in thy hand.
United, free,
For liberty
Together we'll always stand.
2.
Oh Uganda! the land of freedom.
Our love and labour we give,
And with neighbours all
At our country's call
In peace and friendship we'll live.
3.
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
