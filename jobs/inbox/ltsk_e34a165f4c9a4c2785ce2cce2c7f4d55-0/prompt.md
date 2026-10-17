# Job ltsk_e34a165f4c9a4c2785ce2cce2c7f4d55-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 6 lesson(s) below of week 2 of the Science scheme for Primary Six 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P6: one 40-minute lesson: 3–6 sections; about 16–32 points; worked examples and exam-style points; 6–8 activities.

lessonId=lles_b9b0d17f5a564685a597818bc49a5dfe: lesson 7, Monday, 1 period(s), 40 minutes.
  Unit: Science at Home and in Our Community (theme: Science in Human Activities and Occupations). Lesson: Decanting water — Decanting water.
  Objectives: Describe or demonstrate decanting water.

lessonId=lles_dcb19853f6794ca0a36df0ffc52d4c2a: lesson 8, Tuesday, 1 period(s), 40 minutes.
  Unit: Science at Home and in Our Community (theme: Science in Human Activities and Occupations). Lesson: Sorting and soaking clothes — Sorting and soaking clothes.
  Objectives: Describe or demonstrate sorting and soaking clothes.

lessonId=lles_c813876e026e42cb87042c460b39c742: lesson 9, Wednesday, 1 period(s), 40 minutes.
  Unit: Science at Home and in Our Community (theme: Science in Human Activities and Occupations). Lesson: Washing and rinsing clothes — Washing and rinsing clothes.
  Objectives: Describe or demonstrate washing and rinsing clothes.

lessonId=lles_b157a20810f745258dafc0bbb128453f: lesson 10, Thursday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: Accidents and first aid — Accidents and first aid.
  Objectives: Describe or demonstrate accidents and first aid.

lessonId=lles_cd29e28062e2488ea00c91695522017a: lesson 11, Friday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: Burns and scalds — Burns and scalds.
  Objectives: Describe or demonstrate burns and scalds.

lessonId=lles_716e46e8601a436983fca63419294cc5: lesson 12, Friday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: Preventing burns — Preventing burns.
  Objectives: Describe or demonstrate preventing burns.

Write, using ONLY the passages below. Passages from "NCDC" documents are the official base for what to teach; NCDC lower-primary thematic curricula put every learning area in columns separated by " | ": use only the Science column.
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
<passage id="lchk_423533289cce49e2ad444f1ac034ec9e" source="NCDC P6 Set One Sept book – Integrated Science" part="15">
Subject | Language | Suggested
Content
Competences | Competences | Activities

The learner; | The learner; | • Preparation | • Carrying out
• describes | • names ways | of Clean and | experiments
ways of | of preparing | Safe Water | on different
preparing | clean and | for Drinking | ways of
clean and | safe water | and Washing: | preparing
safe water | for drinking | clean and
– boiling
for drinking | and washing. | safe water
and washing. • reads words,  – filtering | for drinking
– treating | and washing.
• discusses | sentences
ways of | and stories | – distilling | • Discussing
cleaning | about | – decanting | ways of
clothes in a | preparation  • Water | cleaning
home. | of clean and | inpurities | clothes in a
• participates | safe water | home.
– human
in preparing | for drinking
wastes | • Preparing
clean and | and washing.
– animal | clean and
safe water | • recites | wastes | safe water
for drinking | poems about | for drinking
– pollutants
and washing. | cleaning | and washing.
from farm
clothes in a
chemical | • Discuss what
home.
– silt from | makes water
erosion | unsafe
• Cleaning | • Words and
Clothes in a | sentences
Home | about getting
– sorting | local salt
from ash.
– soaking
– washing
– rinsing

National Curriculum Development Center

Subject | Language | Suggested
Content
Competences | Competences | Activities
• Constructs a | • reads | – wringing | • Preparing
simple water | words and | – drying | clean and
purifying | sentences | – ironing | safe water
system. | about getting | for drinking.
local salt | • Constructing
from ash. | a simple
• Writes down | water
clear steps in | purifying
the process | system.
of preparing
clean water
for drinking
and washing.

Guidance to the Teacher
• Set up practical experiment to clean water from different
impurities.
• With your learners set up an experiment with a water filter
constructed by the class.
• You should encourage the learners to practically demonstrate
the steps people should follow to clean clothes.
• Clearly outline steps that are followed when making salt from
ash.
Suggested Competences for Assessment
The learner;
• describes what safe drinking water is.
• outlines ways of preparing clean and safe water for drinking
and washing.
• describes the steps people should follow to clean clothes in a
home.
• carries out a science oriented activity on preparation of clean
and safe water during science show.

Theme: Human Health | 15 Periods

Topic 10: | Accidents and First Aid
Background
Learners began to learn about accidents and first aid in P4. You should
build on the work they did then. In our day to day activities, we may get
involved in accidents whose victims require assistance in form of first
aid. Guide learners on how to administer first aid to victims of accidents.
Practical demonstration is important to make learning real. Help the
learners to acquire knowledge and skills that can help them to avoid
accidents. This topic has been retained in the same P6 term.

Learning Outcomes
The learner;
• becomes increasingly aware of accidents in places where they live.
• develops the necessary skills and knowledge for applying first aid.

Life Skills | Values
• Problem-solving | • Care
• Critical thinking | • Concern
• Creative thinking | • Sympathy
• Effective communication | • Fluency
• Decision-making | • Responsibility
• Empathy | • Patience
• Coping with stress | • Acceptance
• Coping with emotions | • Negotiating
• Non-violent conflict | • Working together
</passage>

<passage id="lchk_a99260574eee4dc4be7def09f7890d7a" source="NCDC P6 Set One Sept book – Integrated Science" part="16">
resolution
• Apologising
• Negotiation

National Curriculum Development Center

Subject | Language | Suggested
Content
Competences | Competences | Activities

The learner; | The learner; | • Burns and | • Talking from
• describes burns | • describes | Scalds | a resource
and scalds | different | person (first
• Fever and
• discusses | types of | Aider) about
Convulsions:
the causes | accidents. | the different
– what they | types of
prevention and | • reads
are | accidents.
treatment of | words,
fever. | sentences | – causes, | • Discussing
and stories | prevention | the causes,
• describes near | and first
drowning. | about | prevention
accidents | aid | and first aid
• mentions | and first | • Near- | for fever
causes, | aid. | Drowning: | different types
prevention and | of accidents.
– what it is
first aid for near • writes
drowning. | words, | – causes, | • Discuss
sentences | prevention | different
• describes | and stories | and first | safety
causes of | about | aid | precautions.
fainting, and | accidents
how to give | and first
first aid. | aid.

Primary 6 Curriculum

Subject | Language | Suggested
Content
Competences | Competences | Activities

• acts out | • Fainting:
• identifies | • Describing
foreign bodies | dialogues | – causes, | fainting,
in the passages. | and plays | conditions | causes and
about | and first | first aid.
• participates | accidents | aid
in activities | and first | • Identifying
which prevent | • Foreign | foreign
aid. | Bodies in
accidents. | bodies in the
• Write down | Passages | passages.
• gives effective | clear steps | (mouth,
first aid to | of giving | nose, ears, | • Writing steps
burns, fevers, | first aid | anus, eyes, | for first aid
fainting and | to victims | throat and | to different
removal of | of various | vagina): | accident
foreign body. | accidents. | victims.
– First Aid
Guidance to the Teacher
• Arrange for a resource person to talk about various aspects of
accidents injuries, first Aid, and prcautions for safety.
• Work with your learners to make practical demonstration on
first aid to the different accidents. You can do this with help of
a resource person.
• Help the learners to clearly differentiate between:
– | causes of fainting and conditions that lead to fainting.
– | burns and scalds.

Suggested Competences for Assessment
The learner;
• identifies passages where foreign bodies can get stuck.
• outlines the causes of fever and convulsions.
• describes the first aid for fainting and near drowning.
• uses the new words leant to describe how to handle the various
forms of accidents.

Theme: Human Health | 15 Periods

Topic 11: | Sanitation

Background
Our activities and the way we live may make our environment dirty
and unhealthy. Guide learners on how to keep clean and healthy where
they live and how to use toilets and latrines properly. This will help to
prevent the spread of diseases especially diarrhoeal diseases. You may
invite a health worker to talk to the pupils about proper sanitation and
hygiene of a toilet / latrine. Involve your learners to participate in the
maintance of sanitation. In earlier classes learners were taught how to
wash hands before eating and after visiting the latrine/toilet. Ensure that
they demonstrate this as an example to younger pupils. This topic has
been retained in P6, Term III.

Learning Outcome
The learner acquires scientific skills and knowledge of keeping proper
sanitation for a healthy living.
Life Skills | Values
</passage>

<passage id="lchk_6154a6908c2f47359d652823839e039b" source="P6 sci notes Batch Watermark" part="52">
 Heavy floods destroy man’s crops and cause a lot of damage to
property.
Hard and soft water
 Hard water is water that contains certain mineral salts dissolved in it.
 Hard water does not form scum with soap easily
 Soft water is water that forms scum easily with soap
Ways of removing hardness from water
 Adding chemicals to hard water e.g chlorine and water guard
 Boiling water
Cleaning clothes in a home
 Sorting: This is the practice of identifying dirty clothes which have
been used.
 Soaking: This is the act of sinking clothes in water and soap for easy
removal of dirt and other spots on a cloth
 Washing: This is the act of squeezing of the cloth together with soap
 Rinsing : Is the act of dipping soapy clothes in clean water to remove
soap solution
Types of washing clothes GOT FROM EDUFLIX APP
Page 164
 Hand washing
 Machine washing
Activities after washing clothes
 Drying clothes
 Ironing clothes
Reasons for ironing clothes
 To kill parasites like lice, itch mites etc
 To kill germs
Items used to clean clothes
 Clean water
 Detergents
 Soap
 Basin GOT FROM EDUFLIX APP
Page 165
THEME 2: HUMAN HEALTH
TOPIC: ACCIDENTS AND FIRST AID:
What is an accident?
An accident is a sudden happening that causes harm to the body.
Mention some injuries to the body:
 Fainting
 Animal bites
 Nose bleeding
 Bruises
 Choking
 Food poisoning
 Burns
 Scalds
 Cuts
 Foreign bodies in natural opening
What is first aid?
First aid is the immediate help given to a casualty before he/she is taken to
the nearest health centre.
Who is a casualty?
A casualty is a person who has been involved in an accident and needs
assistance of first aid.
Mention five reasons for giving first aid
 First aid saves life
 First aid promotes quick recovery
 First aid stops bleeding
 It reduces pain
 It prevents further injuries
What is a first aid kit?
A first aid kit is a set of equipment used when giving first aid for a certain
type of an accident
What items are found in a first aid kit
 Cotton wool
 Plaster GOT FROM EDUFLIX APP
Page 166
 Razor blade
 Bandage
 Pain killers
 A pair of scissors
Who is a first aider?
A first aider is any person who gives first help to a casualty.
Or
A first aider is any person who gives assistance to a casualty.
Mention four qualities of a good first aider
 He/she should be quick in giving first aid.
 He/she should be knowledgeable enough
 He/she should have skills
 He/she should be clean
BURNS:
What is a burn?
A burn is an injury on the skin caused by dry heat. Or
A burn is an injury caused by a hot object
Causes of burns include;
 Through body contact with hot plates, cookers, hot burning charcoal.
 Through body contact with un-insulated electric wires carrying
current
 Through body contact with chemicals like acids
 Through body contacts with fire
Degree of burns
Degree of burns is a term used to describe how severe the burn is.
Degrees of burns include;
 First degree burn
 Second degree burn
 Third degree burn
First degree burn.
A first degree burn is a minor burn in which there are no blisters formed.
What is a blister?
A blister is a raised skin with some liquid underneath. GOT FROM EDUFLIX APP
Page 167
Second degree burn.
A second degree burn is a severe burn in which blisters are formed on the
skin at the site of the injury.
Third degree burn
This is the most severe burn in which the skin is burnt deeply and appears
shinny white.
First aid for second degree burn
</passage>

<passage id="lchk_fb87e8874d7541f4ba18ae85b06eddc6" source="SCIENCE LESSON NOTES FOR P6 2019(1)" part="44">
Preparation of safe water for drinking
i. Boiling
When water is heated, it boils, to a temperature of 100 o C (212 o F) this temperature kills germs.
ii. Filtering
This is the process by which a clean or sterilized piece of cloth or local water filter.
Examples of solid impurities filtered are dirt, soil, stones, leaves, animals wastes etc.
(c) P6 SCIENCE LESSON NOTES 2016Page 141
NB: Filtered water is not safe for drinking because it may be containing some germs.
iii. Treatment of water
Treatment of water is when chemicals are added to kill germs in it.
Examples of chemicals used to treat water are; chlorine, water guard and aquasafe.
Advantages of chemicals used in water treatment
The chemicals kill germs in water
Disadvantages of using chemicals
 They are expensive
 They do not make water clear
 They add some smell and taste to water.
DECANTING
Decanting is a method of removing large particles of objects from water.
Decanting is done by pouring water slowly from one container to another so that heavily particles are left
behind. In this method, the three pot system is used to purify the water.
WATER IMPURITIES
Impurities are contaminants or foreign objects in water. Water impurities make it unsafe for use.
Impurities may be soluble or insoluble organic.
Inorganic impurities
It consists of dissolved mineral salts which make water unsafe to use.
Organic impurities
These include bacteria , fungi and protozoa others may be dead plant materials such as leaves and grass.
Examples of water impurities
- Human wastes
- Animal wastes like urine , dung
- Herbicides
- Insecticides
- Silt from erosion
(c) P6 SCIENCE LESSON NOTES 2016Page 142
CLEANING CLOTHES AT HOME
One main use of water at home is to wash clothes. This also called laundry
Step used in cleaning clothes at home
Sorting
- It involves selecting and putting clothes together according to colour , intensity of dirt, nature of
the fabric , use of clothes etc.
Soaking
It is the putting clothes in soapy water for some time.
Importance of soaking clothes
- It helps to loosen dirt and dissolve stains
- It saves time during washing as it a little effort to remove it.
- It saves against tear and wear due to constant rubbing while washings.
Washing
It is the removal of dirt using water and detergent
Rinsing
Clothes are put in clean water. It helps to remove all soapy water from the clothes.
Wringing
It involves squeezing excess water out of the clothes
NOTE : Woolen clothes should be dried without wringing because it may loosen the fabric and makes
them to lose their shape.
Drying
Some clothes can be dried out completely under the sun.
Ironing
It helps to remove creases from the washed clothes and bring them to their original form
ACCIDENTS AND FIRST AID
What is an accident?
An accident is a sudden happening that cause harm to the body.
Accidents can take place anywhere.
They may happen at home, school, place of work, where we go for prayers, on the pitch etc.
(c) P6 SCIENCE LESSON NOTES 2016Page 143
First aid
This is the first help given to a casuality before he/she is taken to hospital. a casuality is a person who
has got an accident.
Burns
These are body injuries caused by heat.
Types of burns
1. Burns
2. Scalds
Burns and scalds
Burns are injuries caused by dry heat.
Causes of burns
a. Hot metals
b. Hot flat iron
c. Acids
d. Glowing charcoal
e. Hot charcoal stove
f. Fire
Degree of burns
Burns and scalds are described using the word degree to tell how severe they are;
</passage>

<passage id="lchk_c74ecae2015e462ea18ed82fc1f55b5e" source="P 6 Primary SIX SCI Notes Teacher AC (0)" part="43">
Decanting is done by pouring water slowly from one container to another so that heavily particles are left behind. In this method, the
three pot system is used to purify the water.
WATER IMPURITIES
Page 148
Impurities are contaminants or foreign objects in water. Water impurities make it unsafe for use. Impurities may be soluble or
insoluble organic.
Inorganic impurities
It consists of dissolved mineral salts which make water unsafe to use.
Organic impurities
These include bacteria , fungi and protozoa others may be dead plant materials such as leaves and grass.
Examples of water impurities
- Human wastes
- Animal wastes like urine , dung
- Herbicides
- Insecticides
- Silt from erosion
CLEANING CLOTHES AT HOME
One main use of water at home is to wash clothes. This also called laundry
Step used in cleaning clothes at home
Sorting
- It involves selecting and putting clothes together according to colour , intensity of dirt, nature of the fabric , use of clothes etc.
Soaking
It is the putting clothes in soapy water for some time.
Importance of soaking clothes
- It helps to loosen dirt and dissolve stains
- It saves time during washing as it a little effort to remove it.
- It saves against tear and wear due to constant rubbing while washings.
Washing
It is the removal of dirt using water and detergent
Rinsing
Clothes are put in clean water. It helps to remove all soapy water from the clothes.
Wringing
It involves squeezing excess water out of the clothes
NOTE : Woolen clothes should be dried without wringing because it may loosen the fabric and makes them to lose their shape.
Page 149
Drying
Some clothes can be dried out completely under the sun.
Ironing
It helps to remove creases from the washed clothes and bring them to their original form
ACCIDENTS AND FIRST AID
What is an accident?
An accident is a sudden happening that cause harm to the body.
Accidents can take place anywhere.
They may happen at home, school, place of work, where we go for prayers, on the pitch etc.
First aid
This is the first help given to a casuality before he/she is taken to hospital. a casuality is a person who has got an accident.
Burns
These are body injuries caused by heat.
Types of burns
1. Burns
2. Scalds
Burns and scalds
Burns are injuries caused by dry heat.
Causes of burns
a. Hot metals
b. Hot flat iron
c. Acids
d. Glowing charcoal
e. Hot charcoal stove
f. Fire
Page 150
Degree of burns
Burns and scalds are described using the word degree to tell how severe they are;
There are three types of degrees of burns. These are;
a) First degree burns
b) Second degree burns
c) Third degree burns
First degree burns
These are minor burns which do not form blisters.
A blister is a raised skin with a liquid under neath.
The skin is tender for several days
The skin is unbroken.
First aid
Put the burnt area in cool water immediately after the accident.
Why?
To reduce the temperature of the burnt part.
N.B; First degree burns need no dressing.
Second degree burns
These are burns which form blisters.
They are severe than first degree burns.
Signs of second degree burns
a) Blister are formed
b) Unbroken blisters
FIRST AID
If the blister is broken, wash the area with clean water and soap.
Cover the skin with a bandage or clean cloth.
Page 151
NB; It is not good to break the blister because it may lead to infection of the wound by germs. Fats, oil, coffee, herbs or dung should
never be put on the burn because they can cause infection.
</passage>

<passage id="lchk_c4c6d466acb549fa9c4bba1246eb74f8" source="P.6 PRIMARY SIX SCI NOTES TEACHER.AC Copy (2)" part="41">
Pure water is tasteless
Pure water boils at 100oC (212oF) and freezes at 0oC (32oF) at sea level.
Pure water forms lather (foam) very easily) with soap.
Uses of water to the body
Water makes up part of blood as plasma
Helps to dissolve the digested food for easy absorption in the body.
Maintains the shape of body cells.
Cools the body in form of sweat when it evaporates.
Helps in formation of body fluids such as tears, saliva, urine, sweat etc.
Other uses of water
For domestic use e.g. cooking, washing etc
For drinking by man, mammals, and birds
For irrigation in agriculture
Used in industries for cooling, washing machines and raw materials.
Used to generate hydro-electricity
Used by plants for photosynthesis
Preparation of safe water for drinking
Boiling
When water is heated, it boils, to a temperature of 100oC (212oF) this temperature kills germs.
Filtering
This is the process by which a clean or sterilized piece of cloth or local water filter.
Examples of solid impurities filtered are dirt, soil, stones, leaves, animals wastes etc.
NB: Filtered water is not safe for drinking because it may be containing some germs.
Treatment of water
Treatment of water is when chemicals are added to kill germs in it.
Examples of chemicals used to treat water are; chlorine, water guard and aquasafe.
Advantages of chemicals used in water treatment
The chemicals kill germs in water
Disadvantages of using chemicals
They are expensive
They do not make water clear
They add some smell and taste to water.
DECANTING
Decanting is a method of removing large particles of objects from water.
Decanting is done by pouring water slowly from one container to another so that heavily particles are left behind. In this method, the three pot system is used to purify the water.
WATER IMPURITIES
Impurities are contaminants or foreign objects in water. Water impurities make it unsafe for use. Impurities may be soluble or insoluble organic.
Inorganic impurities
It consists of dissolved mineral salts which make water unsafe to use.
Organic impurities
These include bacteria , fungi and protozoa others may be dead plant materials such as leaves and grass.
Examples of water impurities
Human wastes
Animal wastes like urine , dung
Herbicides
Insecticides
Silt from erosion
CLEANING CLOTHES AT HOME
One main use of water at home is to wash clothes. This also called laundry
Step used in cleaning clothes at home
Sorting
It involves selecting and putting clothes together according to colour , intensity of dirt, nature of the fabric , use of clothes etc.
Soaking
It is the putting clothes in soapy water for some time.
Importance of soaking clothes
It helps to loosen dirt and dissolve stains
It saves time during washing as it a little effort to remove it.
It saves against tear and wear due to constant rubbing while washings.
Washing
It is the removal of dirt using water and detergent
Rinsing
Clothes are put in clean water. It helps to remove all soapy water from the clothes.
Wringing
It involves squeezing excess water out of the clothes
NOTE : Woolen clothes should be dried without wringing because it may loosen the fabric and makes them to lose their shape.
Drying
Some clothes can be dried out completely under the sun.
Ironing
It helps to remove creases from the washed clothes and bring them to their original form
ACCIDENTS AND FIRST AID
What is an accident?
An accident is a sudden happening that cause harm to the body.
Accidents can take place anywhere.
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
