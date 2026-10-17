# Job ltsk_82d464096efa40a39fb5f8f9c5529db6-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 5 lesson(s) below of week 10 of the Social Studies scheme for Primary Five 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P5: one 40-minute lesson: 3–5 sections; about 14–28 points (meaning, examples, reasons, problems and solutions as the passages give); 5–8 activities.

lessonId=lles_9a2753bbd95b4d9e84313391e5ec4506: lesson 46, Monday, 1 period(s), 40 minutes.
  Unit: Uganda as an independent nation (theme: Living together in Uganda). Lesson: Term revision 1: Uganda as an independent nation, The Government of Uganda, Population, Size and Distribution — Mixed revision of the term.
  Objectives: Revise and practise questions from all the term's units
  This is a REVISION lesson for the unit. notes = the unit's key points under ### headings ('- ' points), then '### Exercise' with practice questions taken from the passages. activities = those questions.

lessonId=lles_3a53301040464ad29d62b25c2651c542: lesson 47, Tuesday, 1 period(s), 40 minutes.
  Unit: The Government of Uganda (theme: Living together in Uganda). Lesson: Term revision 2: Uganda as an independent nation, The Government of Uganda, Population, Size and Distribution — Mixed revision of the term.
  Objectives: Revise and practise questions from all the term's units
  This is a REVISION lesson for the unit. notes = the unit's key points under ### headings ('- ' points), then '### Exercise' with practice questions taken from the passages. activities = those questions.

lessonId=lles_922160d51b92469a8ec82d95a6fb54c8: lesson 48, Wednesday, 1 period(s), 40 minutes.
  Unit: Population, Size and Distribution (theme: Living together in Uganda). Lesson: Term revision 3: Uganda as an independent nation, The Government of Uganda, Population, Size and Distribution — Mixed revision of the term.
  Objectives: Revise and practise questions from all the term's units
  This is a REVISION lesson for the unit. notes = the unit's key points under ### headings ('- ' points), then '### Exercise' with practice questions taken from the passages. activities = those questions.

lessonId=lles_310fae2b123445f093a410f2e64e3b27: lesson 49, Thursday, 1 period(s), 40 minutes.
  Unit: Uganda as an independent nation (theme: Living together in Uganda). Lesson: Term revision 4: Uganda as an independent nation, The Government of Uganda, Population, Size and Distribution — Mixed revision of the term.
  Objectives: Revise and practise questions from all the term's units
  This is a REVISION lesson for the unit. notes = the unit's key points under ### headings ('- ' points), then '### Exercise' with practice questions taken from the passages. activities = those questions.

lessonId=lles_381da0be0dc64895b0bade512779b38f: lesson 50, Friday, 1 period(s), 40 minutes.
  Unit: Uganda as an independent nation (theme: Living together in Uganda). Lesson: End of term assessment — Uganda as an independent nation, The Government of Uganda, Population, Size and Distribution.
  Objectives: Assess what learners have learnt this term
  This is the END OF TERM ASSESSMENT. notes = an assessment paper of 15–25 questions from the passages covering the term's units, numbered, with a marking guide (answers) at the end where the passages give them. activities = the questions.

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

<passage id="lchk_a068c36f55a64155a9a2517aace9832f" source="P.5 Social Studies Lesson Notes Term 3" part="4">
 To provide clean water to people
 To implement the laws
 To protect people and their property.
ARMS / ORGANS OF A DEMOCRATIC GOVERNMENT.
Government has many responsibilities. It carries them out through organs.
- The executive
- The legislature
- The judiciary.
Duties of the executive
 To implement the law
 To plan for the country
DIVINE EDUCATION CENTRE:0784540287/0751565742 Page 11
 To rule the country
 To protect people and their property.
The executive organ does the work of government.
Composition of the executive.
- The president (head)
- Cabinet ministers
- Civil servants (government workers)
Duties of the Legislature
 To discuss and pass laws.
 To give advice to the executive
 To approve the national budget
 To approve (vet) newly appointed minister and other senior government officials.
 To protect the national constitution
Legislature is headed by the speaker of parliament.
Important personalities in parliament.
- The speaker of parliament
- Sergeant at arms
- Clerk to parliament
Note: Roles of the speaker
 The speaker chairs parliamentary meetings
 The sergeant at arms keeps law and order in parliament.
 The clerk to parliament records minutes in parliament.
 Recorded minutes of parliament are called hansards
 Give the present speaker (and the deputy speaker) of parliament.
Composition of parliament.
- Constituency representatives.
- Special groups / interest groups representatives.
Special groups representatives:
 The army
 The youth
 Women
DIVINE EDUCATION CENTRE:0784540287/0751565742 Page 12
 People with disabilities.
Teacher should revise the work on Legco
- Give similarities of Legco and today’s parliament
- Differences between members of Legco and members of parliament.
Duties of the judiciary
 To interpret the law
 To decide if the law has been broken or not.
 To settle disputes
 To punish law breakers.
Composition of the judiciary
- Judges
- Magistrates
- Court clerks
- Lawyers
The judiciary is headed by the chief justice.
Teacher should give the similarities of the judiciary and local councils and the judiciary
with prefects.
CONSTITUTIONALISM AND THE RULE OF LAW
A national constitution is a set of laws used to rule a country.
A constitution is a set of laws used to govern a company, a society or an organization.
Functions of a national constitution
 To unite people
 To promote peace and security
 To guide leaders
 To help change government peacefully
 To promote good governance
 To promote human rights.
The constitutions Uganda has ever had.
1961 constitution
1962 constitution
1966 constitution
1967 constitution
1995 constitution
DIVINE EDUCATION CENTRE:0784540287/0751565742 Page 13
The 1961 constitution
This constitution was made in London between 18 th September. This constitution was
made in London between 18 th September to 9 th October 1961.
It was mainly made to enable Uganda get self government.
Lord Munster Commission
- This was a committee appointed in July 1961 to make a report about the kingdoms
interests mainly those which refused to send representatives to Legco.
- It was chaired by Lord Earl Munster.
Recommendations:
 Buganda was to remain part of Uganda.
 Buganda was to send 21 members to the national assembly.
Contributions of the Munster Commission
 It led to the Lancaster Conference which granted Uganda independence.
The Lancaster Conference of September 1961
This conference was held in Lancaster house in London.
It granted Uganda independence.
</passage>

<passage id="lchk_613d1868da5840e4844b343f10260aa2" source="Primary 5 Social Studies Scheme of Work – Term 3" part="3">
-Examples of
Ugandan
president since
1962 up to the
present leader
Idi Amin Dada
1971-79
Yesufu Kilonde
Lule 1979
-self
awareness
-talking
about one’s
potential
feeling and
emotions
-Observation
-Talk and a
chalk board
illustration
-Identify
presidents
who ruled
Uganda
Text books MK
SST
Bk
5
Pg
122
For more schemes of work, visit www.uganda.madpath.com
presidents
who ruled
Uganda
-Pronounces
words
correctly
Geoffrey
Rukongwa
Brinaisa 1979-80
-making
choices
The learner is able to understand the organs of the government, the constitution and duties of citizens, explain the sources of revenue and expenditure by
government and understand the rights and responsibilities of the citizens of Uganda.
5 -The
government
-Types of
governme
nts
-A learner
defines the
two types of
governments
-A learner
pronounces
vocabulary
words
correctly
-Writes
words
correctly
Writes
words in
correct
spelling
-Definition of a
government
-Listing types of a
government and
their functions
-Ways in which
government were
formed
-Creative
thinking
-initiating
new ideas
-friendship
formation
-working in
groups
-Observation
-Talk and a
chalk board
illustration
-Identifying
types of
government
s
Text
books
MK
SST
Book 5
pg 131
6 The
government
of Uganda
Organs of
the
governme
nt
-A learner
lists down
three organs
of the
government
-States the
functions of
the
executive
organ of the
government
-A learner
spells words
of the lesson
correctly
-Writes
words in
good
spelling
-Pronounces
words
correctly
-Mentioning the
three organs of
the government
-Functions of the
executive organ
-Planning for the
country
-Ensuring peace
in the country
Empathy
-supporting
others
-caring for
others
guiding
others
-guided
discussion
-inquiry
-talk and
chalk
Stating the
organs of
the
government
Answering
questions
Text
books
MK
SST Bk
5 Pg
133
7 The
Legislatio
n
-A learner
Identifies
the la
making
body during
colonial days
-A learner
Write all
words rightly
-Spells
words
correctly
-Pronounce
vocabulary
-The main work
of legislation
-The head of
legislation
-Functions of
legislation
-creative
thinking
-logical
reasoning
-initiating
new ideas
-inquiry
-guided
discussion
-Stating the
function of
the
legislation
-Answering
questions
Text
books
MK
SST Bk
5 Pg
133
For more schemes of work, visit www.uganda.madpath.com
words
correctly
-Finding
different
ways of
doing things
3 1 ORGANS
OF THE
GOVERNM
ENT
THE
JUDICIA
RY
-A learner
Defines the
term
judiciary
states the
three
categories of
people in
judiciary
-Names the
heads of the
judiciary
-A learner
spells lesson
vocabulary
correctly
-Writes
lesson notes
and exercise
rightly
-Group of people
who make up
judiciary
-The judges,
lawyers,
legislature,
antoneys, justice
-Functions of the
judiciary
-The head of
judiciary
empathy
-caring for
others
listening to
others
-critical
thinking
-reasoning
-explanation
-inquiry
-guided
discussion
Identify
what form
of judiciary
organ of
government
Text
books
MK
SST Bk
5 pg
134
2 The
constituti
on
A learner
defines
constitution
A learner
Spells
difficult
words
correctly
-Definition of the
term constitution
-The four
constitutions
Uganda has ever
had since
independence.
-Independence
constitution 1962
-Pigeon hole
constitution of
1966 etc
-problem
solving
-taking
decision
-taking
decisions
-making
choices
-decision
making
giving
instructions
-Inquiry
Guided
discussion
-Explanation
-Chalk and
talk
Look and say
Discussing
functions of
the
constitution
Text
books
Mk
SST Bk
5 pg
135
3 Function
of a
national
constituti
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
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
