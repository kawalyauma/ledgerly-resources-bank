# Job ltsk_c63decc85b3949f3afeeda75362ddd28-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 5 lesson(s) below of week 2 of the Social Studies scheme for Primary Five 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P5: one 40-minute lesson: 3–5 sections; about 14–28 points (meaning, examples, reasons, problems and solutions as the passages give); 5–8 activities.

lessonId=lles_831d3e35d6084faba037b1ed09260a0e: lesson 6, Monday, 1 period(s), 40 minutes.
  Unit: Uganda as an independent nation (theme: Living together in Uganda). Lesson: The national emblem — Symbols of a nation: the crested crane.
  Objectives: Name the national emblem; Give reasons why the crested crane was chosen

lessonId=lles_e56bd80763154dfaa05ad7b74ee19fc4: lesson 7, Tuesday, 1 period(s), 40 minutes.
  Unit: Uganda as an independent nation (theme: Living together in Uganda). Lesson: The national language — National and official language.
  Objectives: Name Uganda's official language; Give reasons why Uganda has no national language

lessonId=lles_d4eb7099e7af4befa05c9ce95976389d: lesson 8, Wednesday, 1 period(s), 40 minutes.
  Unit: Uganda as an independent nation (theme: Living together in Uganda). Lesson: The capital city — Symbols of a nation: the capital city.
  Objectives: Name the capital city of Uganda; State the importance of a capital city

lessonId=lles_03d523830f3641daa4b8a090f1e3e387: lesson 9, Thursday, 1 period(s), 40 minutes.
  Unit: Uganda as an independent nation (theme: Living together in Uganda). Lesson: The national currency — Uganda's currency and financial institutions.
  Objectives: Name Uganda's currency and its denominations; State the roles of the Bank of Uganda

lessonId=lles_f72c6211677f44ea828a1c7da3bdcc08: lesson 10, Friday, 1 period(s), 40 minutes.
  Unit: Uganda as an independent nation (theme: Living together in Uganda). Lesson: Democracy — Meaning, importance and challenges of democracy.
  Objectives: Define democracy; State the importance and challenges of democracy

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
<passage id="lchk_a51d4f1ab8634588a6770df9da1b613d" source="P.5 SST SCHEME TERM III 2019" part="2">
-Identify the importance of the National language.
-name the official language and why its used in Uganda
-Pronounce , read, spell and write words related to language.
National language.
-Language
-National language
-Importance
-Official language
-Reasons
-Reasons why Uganda is not having a national language.
-Role play
-Questions and answer
-Explanation
-Appreciation
-Critical thinking
-Love
-Respect
-naming different languages
-Learn the meaning of words from different languages
-Text books
-Resource
Persons
-A chart showing different words in different languages.
Functional SST bk 5
Page 172
3
Symbols of a nation (Capital city)
-Naming the capital city
- Identifying the importance of a capital city.
-Naming the towns which were once capital cities and years
-Pronounce , read and write words related to capital cities.
The National Capital
-The capital city of Uganda.
-Importance of a capital city.
-Towns that were once capital cities and years.
-Discussion
-Discovery
-Explanation
-Question and answer
-Love
-Respect
-Critical thinking
-Caring
-Identifying the importance of a capital city.
-Naming the towns that were once capital cities.
-Chalk board illustrations
-Text books
Mk std
Bk 5
Page 129
2
4
LIVING TOGETHER IN UGANDA
Uganda as an independent nation
National currency
-identifying Uganda’s currency and importance.
-Naming financial institutions and their roles.
-Pronounce, read and write words related to currencies.
National currency
-Uganda’s national currency.
-Denominations.
-Importance of currency.
-Financial institutions eg
BOU and roles
Commercial banks and roles.
-Question and answer
-Discovery
-Explanation
-Self awareness
-Love
-Appreciation
-Critical thinking
-Identifying Uganda’s currency and its importance.
-naming the financial institutions and their roles.
-Text books
-Papers having printed roles of currencies.
5
Democracy
-Explaining democracy
-Discussing the importance of democracy
-spells, reads , pronounces and writes words related to democracy
Democracy
-Definition
-Importance of democracy, functions
-Challenges of democracy
-Ways how democracy is practiced
-Explanation
-Discussion
-Discovery
-Question and answer
-Description
-Critical thinking
-Effective communication
-Explaining democracy.
-Discussing the importance of democracy
-Text books
-Chalk board illustration
3
1
Citizenship
-Explaining a citizen
The new words are challenges, election , citizen , conduct
Citizen ship
-Defining a citizen
-Ways in which one play can become a citizen.
-Ways how one can loose his/her citizenship.
-Roles of a citizen in practicing demoncracy
-Role play
-Role playing elections
MK stdbk 5 page 142-143
3
2
LIVING TOGETHER IN UGANDA
Uganda as an independent nation
Pronounces, spells, reads and writes words of bad practices
Bad practices during elections.
-before voting
-during voting
-after voting
3
Elections
-Explaining elections and its importances
-spells, read, pronounce and write words related to elections
Elections
-Definition
-Types of elections
Ballot paper elections
Lining elections
Appointing elections
-How elections are conducted
-Role play
-Explanation
-Discussion
-Critical thinking
-Respect
-Effective communication
-Inquiry
-Naming the different elections
-Role playing elections
-Drawing different elections materials
-Text books
4
Terms used in elections
-Explaining terms used in elections
Terms used in elections.
-polling station
-Bullot box etc
-Polling Assistant
-Polling officer etc
-Importances of elections
</passage>

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

<passage id="lchk_8565a70475344911b9db098cef933069" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="12">
 Officials that were elected in 1994 to debate the 1995 constitution.
29
iii) Mr. Stephen Akabway
 He was the chairperson of the Interim Electoral commission which organized the
elections of the CADS.
iv) Hon James Wapakhabulo
 He was the chairperson of the Constituent Assembly.
v) Professor Victoria Mwaka (Hon)
 She was the deputy chairperson of the Constituent Assembly.
A draft constitution
 A constitution where the views of citizens were represented.
 The Constituent Assembly debated and finalized the 1995 constitution.
 It took a period of sixteen months.
 On the 8 th October 1995, the 1995 – constitution was promulgated at the constitutional
square formerly known as city square.
Functions of a national constitution
 It protects the rights of the citizens.
 It guides the nation systematically in a particular direction of governance.
 It provides the means through which conflicts can be solved peacefully.
 It promotes national unity.
 It provides a peaceful transition of leadership.
The constitution promotes democracy in a country.
Activity
1. What is a national constitution
2. Write down any two constitutions that Uganda has had since independence.
3. What contribution was made by Godfrey Lukongwa Binaisa and Kofi Crable in 1967?
4. Why is a constitution important in a democratic country like Uganda?
5. Write short notes on the people below.
a) Stephen Akabway
b) Hon. James Wapakhabulo
6. Why is 8 th October 1995 politically important?
30
7. Mention the way, the 1967 constitution was unfriendly to the kingdoms in Uganda.
8. Write CADs in full.
9. What contribution was made by the constituent Assembly in 1994?
Date Class Subject No. of pupils Time
P.5
TOPIC: The Government of Uganda
SUB –TOPIC: Democracy
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic: freedom, democracy, human rights
, press
Content : Democracy
 What is democracy?
 Democracy is a system of governance which gives people freedom of speech, worship
and participation in politics
Or
 Democracy is the government of the people by the people and for the people.
 Democracy was first introduced and practiced by the Greeks in the city of Athens in
Greece.
Signs of modern democracy in a democratic country
 Elected political leaders.
 Elected parliament
 Freedom of speech
 There is freedom of the press.
 There is freedom of movement
 There is freedom of worship.
 Freedom to carry out business.
 Observance of human rights.
 Constitutional rule.
 Competitive politics.
Roles of citizens in promoting democracy
 Obeying the law.
31
 Respecting other people’s rights.
 Reporting wrong doers to the police.
 Participating in elections.
Ways through which Democracy is exercised in Uganda today
 Through elections by giving people freedom of speech
 By giving people freedom of press.
 Through freedom of worship
Ways how democracy is practiced in schools
 By electing prefects.
 By giving children freedom of expression.
 Through freedom of worship.
Activity
1. Define democracy
2. In which city was democracy first practiced?
3. State one way democracy is practiced in Uganda today.
4. How is democracy important in a country like Uganda?
5. Give two roles of citizens in the promotion of democracy in a country.
Date Class Subject No. of pupils Time
P.5
TOPIC: The Government of Uganda
SUB –TOPIC: Human rights in Uganda
LANGUAGE COMPETENCE :
</passage>

<passage id="lchk_048ba2ce490e4899bc75b49b2fa571ad" source="P.5 Social Studies Lesson Notes Term III: Uganda as an Independent Nation" part="7">
 A capital city of a nation serves as the centre of all the major activities of a country.
 The capital city of Uganda is Kampala
Which was the capital city of the colonial government?
 It was Entebbe
Importance of a capital city in a country
 It serves as an administrative centre
 It serves as a commercial centre
 It is a communication centre.
 It is an educational centre
Important buildings found in Kampala
 Parliamentary buildings
 Television stations
 The state house
 International conference centre
 Bank of Uganda
The National Emblem
 The crested crane was chosen as the national Emblem of Uganda.
 It was chosen because of its good characteristics which were observed by Ugandans.
The good characteristics of the crested crane
 It is gentle
 It is peaceful
 It is a gracious bird
 It has all the three colours of the Uganda flag.
Areas where the crested crane symbol is used
 It is used on any government official documents
 It is found on the national flag.
 It is used on the parliamentary building.
 It is used on national currencies.
 It is used on the hats of police, prisons and army officials.
17
Activity
1. Why should a nation have a national capital city?
2. How does a national language promote trade in a country?
3. Who called Uganda the pearl of Africa?
4. Why was Uganda called the pearl of Africa?
5. Why does Uganda use English as the official language?
6. Why was the crested crane chosen as the Uganda’s emblem. Give any three reasons.
7. Why has Uganda taken long to adopt a national language?
Topical tests on Uganda as an independent nation
1. What is an independent nation?
2. Why was it important for Uganda to fight for her independence?
3. Quote the date, month and year when Uganda attained her political independence.\
4. Why is it important for a country to have national attributes?
5. Who was the first directly elected president of Uganda?
6. a) What is an election?
b) Why are periodical general elections important in Uganda?
7. Which feature on the Uganda coat of arms shows that Ugandans are God fearing people?
8. Give two occasions at which the Uganda Anthem is sung.
9. What were the contributions of the following towards Uganda independence;
a. George William Kakoma
b. Grace Ibingira
c. Mzee Paul Mukasa
10. Mention two places where the Uganda flag is hoisted.
Date Class Subject No. of pupils Time
P.5
TOPIC: The Government of Uganda
SUB –TOPIC: The organs of Government and their functions
18
LANGUAGE COMPETENCE :
The learner:- Spells and uses words related to the sub -topic: government, central government,
by laws, decentralization, president, council
General importance of national symbols
- For identification
- They promote national unity, nationalism e.t.c
Content : Meaning of a Government
A government is a group of people who exercise power in a particular country.
Or
A government is an established authority that runs the affairs of a country on behalf of her
people.
Types of Government
i) The National (central) government.
ii) Local government
The local government
This is the government that begins at the district level.
Levels of the local government
Rural settings. Urban settings
 The District level LC V District LC V
 The county level LC IV Municipality LC IV
 Sub county level LC III Division LC III
 Local council II Parish Ward LC II
 Local council I Village Cell LC I
They are all under the National government.
1. Name the laws that are used at local government.
2. What are bye laws?
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

<passage id="lchk_1d0a00b334ac4c53bc15fad9593b34fd" source="Primary Five Social Studies Notes 2020" part="50">
Qn: What title is given to the political head of capital city authority ?
 Lord Mayor.
Qn; What title is given to the head of civil servants in a city /municipality ?
 Town clerk
218
Duties of KCCA
i) To clean the city
ii) To put lights on streets
iii) To collect taxes in the city
iv) To construct and maintain roads in the city
v) It sets ordinances in the city.
Importance of Kampala as a city .
i) It serves as the main administrative centre
ii) It serves as the main trading centre
Problems faced by people in Kampala.
i) High crime rates
ii) Traffic jam during rush hours
iii) Poor sanitation
iv) Unemployment
What is slum ?
 A slum is an area congested with unplanned houses.
DEMOCRACY
 Democracy is a type of government that allows citizens to use their
power and authority.
Or
 This is a type of government that allows citizens to exercise their rights.
Signs /indicators of democracy
219
i) Freedom of speech
ii) Freedomof worship
iii) Freedom of movement
iv) Freedom of expression
v) Freedom of association.
Name the town where democracy started .
 Athens of Greece.
Ways democracy is practiced in Uganda .
i) Through freedom of worship
ii) Through freedom of expression
iii) Through freedom of association
iv) Through freedom of press
v) Through freedom of speech
vi) Through freedom of movement
Ways democracy is practiced in schools .
i) Through freedom of worship
ii) Through freedom of expression
iii) Through freedom of association
iv) Through electing prefects
Qn: How is democracy exercised in the following ways.
a) Association
i) By attending political rallies.
ii) By forming clubs.
b) Freedom of press
220
 People are free to write articles in newspapers.
c) Freedom of movement
 People are free to move to any part of the country
d) Freedom of worship
 People are free to pray from any where
Importance of democracy .
 It promotes peaceful transition of leaders.
 It promotes unity among people.
 It promotes human rights.
 It helps people to choose their ownleaders.
Challenges /problems faced by democracy.
 Corrupt political leaders
 Dictatorship
 Vote rigging
 Ignorance of citizen about their rights
 Bribing voters.
 Threatening voters.
Roles of citizens in democracy.
 Participating in elections
 Promoting human rights
 Promoting peace, security and unity
ELECTIONS
 An election is a democratic way of choosing leaders.
Qn: What is the minimum age in which one can participate in elections
in Uganda?
 18 Years
221
Qn: Why are children not allowed to vote in an election?
 They cannot make their own decision
 They are taken to be young according to the constitution of Uganda
Types of elections
 Parliamentary elections
 By elections
 Presidential elections
 By elections
 Referendum
 By elections
 This is an election held to fill a vacant political post
Causes of a by election
 When an elected political leader dies.
 When an elected political leader runs insane.
 When an elected political leader resigns.
 When an elected political leader has rigged voters
 When an elected political leader has been exiled.
Qn: What does the electoral commission do when election results have
been nullified by the courts of law?
 It organizes a by – election
Examples of leaders who acquire offices through elections.
i) President
ii) Members of parliament
iii) Local council chairperson
iv) Youth council representatives
v) District councilors
222
Qn: What is referendum ?
</passage>

<passage id="lchk_868bb787b248475a9303e07ee616b3c3" source="Primary Five Social Studies Notes 2020" part="49">
 Busoga College Mwiri
214
Importance of the national motto
 It promotes love for one’s country
 It promotes national identify
 It promotes unity among citizens
 It symbolizes that Uganda’s are God fearing people
Uganda national Emblem
Uganda national emblem is the crested crane.
Qn: Why was the crested crane chosen as the Uganda national emblem?
 It is a gentile bird
 It is a peaceful bird
 It is a graceful bird
 It is a humble bird
Qn: What does the crested crane symbolizes?
 It symbolizes that Ugandans are peace loving people
Qn: Why is the crested crane drawn standing on one leg?
 It shows that Uganda is moving forward to development.
Government official objects where the crested crane appear.
 National flag
 Security flag
 Number plates
 Bank of Uganda buildings
 Parliamentary currency
 National coat of arms
 Huts of prison, police and army officials
Qn: Why is it wrong for a Ugandan to kill a crested crane?
 It is Uganda’s national emblem.
NATIONAL LANGUAGE.
215
1. What is a national language?
 This is a local language spoken and under stood by most citizens in a
country.
2. Give two reasons why Uganda does not have a national language.
 It has many tribes.
3. What is Uganda’s official language?
 English.
4. Why does Uganda use English as the official language?
 It was colonized by Britain.
5. What is an official language?
 This is a language used in government offices.
Advantages of having a national language.
 It promotes national unity
 It promotes trade
 It brings a sense of belonging
 It promotes easy communication
Uganda national currency
 The Uganda shillings is the national currency
 Uganda currency is in both paper and coins
Qn:What is the Uganda legal lender?
Uganda shillings.
Types of money
 Paper notes
 Coins
Features found on different denominations of Uganda shillings
Denominations Unique feature
216
50/= Head of antelope
100/= cow
200/= fish
500/= Head of a crested crane
1000/= Antelope
2000/ fish
5000/= nest,bird
10,000/= banana plant
20,000/= cow
50,000/= mountain gorilla
Examples of foreign currency commonly used in Uganda
Us Dollar
The central bank .
 The central bank in Uganda is called Bank of Uganda .
 It is head by the Governor.
Duties of the central bank
 It prints new money
 It controls money incirculation.
 It gives licences to commercial banks
 It gives loans to commercial banks
 It controls forex bureaus
 It manages public debts
 It buys valuable minerals like gold.
Commercial banks
 These are banks where people keep their money safe.
Examples of commercial banks
i) Stanbic bank
ii) Centenary bank
iiI) Tropical bank
iv) DFCU bank
217
V) Absa bank
vi) Diamond Trust bank
vii) Equity bank
importance of commercial banks
 They create employment /jobs
 They keep people’s money safe
 They give loans to people
 They give financial advice to people
Why people keep their money in banks
 To get interest
 To get loans
 For their money to be safe
 It keeps government important documents
 It keeps money for commercial banks
NATIONAL CAPITAL CITY
 A national capital city is the main administrative centre in the country.
 Kampala is the capital city of Uganda.
 Entebbe was the colonial capital city of Uganda.
Qn: Why was the capital city of Uganda transferred from Entebbe
toKampala?
 Kampala is centrally located.
Qn: Name the body that governs Kampala city .
 Kampala Capital city Authority. (KCCA)
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
