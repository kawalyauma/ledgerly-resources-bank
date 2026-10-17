# Job ltsk_2d60dcfa816d435c8e912f50a076e91f-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 6 lesson(s) below of week 4 of the Science scheme for Primary Six 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P6: one 40-minute lesson: 3–6 sections; about 16–32 points; worked examples and exam-style points; 6–8 activities.

lessonId=lles_5c06de1d9a4a403a8a397d909cb7f3cb: lesson 19, Monday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: Fainting — Fainting.
  Objectives: Describe or demonstrate fainting.

lessonId=lles_7628bee787e94a36ba1c12b4319bfaf0: lesson 20, Tuesday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: Causes of fainting — Causes of fainting.
  Objectives: Describe or demonstrate causes of fainting.

lessonId=lles_1201aa5ff6b443b880ce109213cc41dc: lesson 21, Wednesday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: First aid for fainting — First aid for fainting.
  Objectives: Describe or demonstrate first aid for fainting.

lessonId=lles_ff036d84a9cb49bc8ca781b70629ff2f: lesson 22, Thursday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: Foreign bodies in passages — Foreign bodies in passages.
  Objectives: Describe or demonstrate foreign bodies in passages.

lessonId=lles_4d23c227825f4863bbf45b71a94a9fab: lesson 23, Friday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: Safety precautions — Safety precautions.
  Objectives: Describe or demonstrate safety precautions.

lessonId=lles_331c9addf778416baa91a4ef1865b00e: lesson 24, Friday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: Practical first aid — Practical first aid.
  Objectives: Describe or demonstrate practical first aid.

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

<passage id="lchk_b3ba2ada9d144186bfd0378008d26191" source="NCDC P6 Set One Sept book – Integrated Science" part="3">
may not have been planned but indicate how the learner is progressing.

Besides continuous assessment, end of term and end of year assessment
shall be carried out. Records of learners’ achievements in the daily
learning activities should be documented to provide records of continuous
assessments.

Learning Outcomes
When learners go through this syllabus, they will be able to:
• survey, identify and distinguish the attributes of plants, animals,
other objects and conditions in the environment.
• use characteristics to compare and classify animals, plants and
other objects in the environment.
• identify the features and describe the functions of different parts
of the human body.
• take care of the different parts of their bodies and practice good
health habits.
• keep safe and avoid accidents.
• understand the conditions for proper growth of living things.

Primary 6 Curriculum

• apply correct scientific processes in investigations of various
phenomena.
• show knowledge of and take care of the environment for its
sustainable use.
Specific Competences
This Integrated Science Syllabus desires to develop a learner who:
1. | identifies and distinguishes the attributes of plants, animals,
other objects and conditions in the environment by making trips
and excursions to:
– | observe
– | collect
– | group/classify
– | record
– | report

2. | uses characteristics to compare and classify animals, plants and
other objects in the environment by:
– | collecting specimens of plants and animals.
– | observing plants and animals grow.
– | grouping/classifying plants and animals (kingdoms).
– | comparing plants and animals.
– | recording observations.
– | reporting findings.
– | caring for animals and plants.

3. | identifies the characteristics and functions of different parts of
the human body by:
– | identifying and naming the different parts.
– | describing functions of each part.
– | caring for the different parts of the body.
– | relating the different parts of the body to human activities.

4. | takes care of the different parts of the human body and practice
good health habits by:
– | identifying the different parts of the body.

National Curriculum Development Center

– | naming different activities done to keep the body clean.
– | caring for the different parts of the body.
– | keeping healthy and practicing good health habits.
– | having self-awareness, confidence and self-esteem.

5. | keeps safe and avoids diseases and accidents by:
– | identifying ways of keeping safe from diseases and accidents
at home and in the community.
– | identifying common accidents and first aid given for each
accident injury.
– | identifying dangers in the environment and taking
precautions.
– | practicing safety precautions.

6. | understands the conditions for proper growth of living things
by:
– | identifying the different conditions for proper growth.
– | experimenting and exploring the different conditions for
proper growth.
– | recording growth progress of plants and animals.
– | reporting on findings of simple investigations

7. | applies correct scientific processes in investigations of various
phenomena by:
– | identifying problems.
– | designing and practicing scientific investigation processes.
– | examining the evidence useful in inferences.
– | demonstrating the skills of observation, classification,
accurate measurement and recording.
– | making predictions and | formulating hypothesis for
evidence.
</passage>

<passage id="lchk_1cb269502f7d45bea6b7796be593a232" source="P6 sci notes Batch Watermark" part="54">
 If the person is not breathing lie the casualty on his back with the
head tilted
 Perform mouth to mouth breathing (kiss of life)
Fainting. GOT FROM EDUFLIX APP
Page 170
Fainting is the brief loss of consciousness.
Causes of fainting
 Shortage of enough oxygenated blood flowing to the brain
 Prolonged hunger
 Standing in sunshine for a long period of time
 Extreme sorrow or anger
 Extreme pain
 Shocking news
 Too much excitement
 Vigorous/strenuous exercises
 Illness
First aid for fainting
 Remove tight clothes around the neck, chest and waist
 Put the casualty in an open space with fresh air
 Make the casualty lie on the back facing up while raising the legs to
encourage enough flow of blood containing oxygen to the brain
 Fanning the casualty if the day is hot
Foreign bodies
A foreign body is any external matter that enters the body either through a
natural opening or wound.
Examples of natural openings
 Mouth
 Eye
 Ears
 Nose
 Rectum
 Vagina
Examples of foreign bodies
 Seeds
 Grains
 Small stones
 Dirt/dust
 Insects
 Soil GOT FROM EDUFLIX APP
Page 171
 Coffee berries
 Pins
 Broken glasses
 Thorns
 Small bones
 Tear gas
 Nib of a pen
First aid of foreign bodies in the eyes
 Wash the eyes with plenty of clean water
 Use a clean corner of a soft piece of cloth to wipe the foreign body out
of the eye.
Note: Never use sharp objects because they can damage the eye and
cause more pain.
If the foreign body remains in the eye, take the casualty to hospital.
First aid for foreign body in the ear
 If it is an insect, tell the victim to sit and bend the head to one side
and pour clean water.
Note: If it is not an insect, do not attempt to remove it because you can
push if further and injure the ear drum.
First aid of foreign body in the nose
 Blow the nose if it is an insect, dirt, dust or small stones.
First aid of foreign body in the throat
 Observe good eating habits
Prevention of accidents caused by foreign bodies
 Keep away objects like seeds buttons, beads, coins, bottle tops etc
from children
 Food must always be chewed properly before swallowing
 Observe good eating habits
 Advising children not to put objects in their ears, eyes and nose
Poisoning
Poisoning: Is the act of taking any harmful substance which can affect
our health. GOT FROM EDUFLIX APP
Page 172
Poison is any substance either solid, gas or liquid which when taken into
the body may damage our health or cause death.
Common poisonous substances.
 Rat poison
 Insecticides
 Agro chemicals
 Paraffin
 Petrol etc
Signs of a poisoned person
 Vomiting
 Rapid breathing
 Diarrhoea
 Loss of body balance
 The person feels thirsty
 Fever and sweating
 Bleeding internally/externally
 Mental confusion
First aid for poisoning
 Give the casualty plenty of fluids like water, juice, milk to dilute the
poison
Note: A person who has taken paraffin/jik should not be made to vomit
because it causes more damage to the lungs, throat and stomach.
Nose bleeding
Fractures
A fracture is a broken or cracked bone in the body.
Types of fractures.
 Simple fracture: This is a type of fracture where the broken or
cracked bone remains inside the flesh
 Compound fracture : This is a type fracture where the broken bone or
cracked bone comes out of the body.
 Green stick fracture: This is a type of fracture which occurs in
young children where the bone tears like a twig.
Causes of fracture
 Accidents GOT FROM EDUFLIX APP
Page 173
 Rough play/games
</passage>

<passage id="lchk_9e237a9a8a0a4170a1315a7e49aba9d0" source="P.6 PRIMARY SIX SCI NOTES TEACHER.AC Copy (2)" part="44">
Make the victim sit and bend the head to one side.
If it is an insect, pour clean water in the ear for the insect to float and come out.
Flash light at the entrance of the ear if the foreign body is an insect.
Take the victim to the hospital
Foreign body in the nose
Foreign bodies in the nose include;
Small insects
Small seeds
Small stones
First Aid
Tell the victim to blow his nose hard and fast.
Take the casuality to the health worker.
Foreign body in the throat
Foreign body in the throat are mainly large pieces of food or small bone.
Foreign body in the throat lead to choking and death.
First aid
Give the victim a number of sharp blows in the back
Wrap your arms around his waist and press the belly upwards strongly.
If the victim is unconscious, lie him on his back and make several sudden pushes on the belly using heels of your hands.
It the person does not breathe, try mouth to mouth breathing.
Take the victim to hospital
If the victim is smaller than you, turn him over your folded leg and give sharp blows at the back.
Preventing accidents caused by foreign bodies
Chew food properly
Do not talk or laugh when eating
Keep beads, button, coins, and seeds out of reach of children
Putting on glasses while moving on motorcycles and bicycles
Teach children not to put seeds, coins, stones, and soil in their eyes, nose, ears, and mouth.
Poisoning
Poison is any substance once taken into the body damages body organs or causes death.
Ways poison can be introduced into the body
Through food
Through air
Through animal bites (snakes, rapid dogs)
Through injections
Through swallowing (orally)
Common house hold poisons
Paraffin herbicides
Root poison Jik
Petrol Insecticides
Wormcides Diesel
Acaricides Drugs (Aspirin/ chloriqune)
Signs of poisoning
Rapid breathing
Fever and sweating
Feeling thirsty
Mental confusion
Comma
Vomiting
Loss of balance
First Aid
Give the casuality a lot of fluids (fresh milk).
Why?
To dilute poison in the stomach
Make the person vomit in case its non-corrosive poison.
How to make the person to vomit
Placing the finger in the mouth or throat.
Give the victim water mixed with soap
Rush the victim to the hospital
NB: If the causality has taken paraffin, petrol, or bleach (Jik), do not make him vomit.
Why?
It causes more damage to the stomach and gullet.
Preventing poisoning
Keep petrol, paraffin out of reach of children
Keep drugs out of reach of children
Follow the doctor’s prescription
Buy drugs from recommended pharmacies
Dispose expired drugs.
Avoid drugs misuse
The ABC technique followed before giving first AID
Air way
Breathing
Circulation
TOPICAL QUESTIONS
Mention the main reason for giving first aid
Distinguish burns and scald.
How is the cause of burns similar to that of scalds?
Why should a burnt hand of a victim be dipped in cool running water?
Why is it not advisable to break blisters on the skin?
How do heat insulators prevent burns and scalds?
Define fever.
List down the main effect of fever.
Explain the first aid you can give a person who has fever.
How would you help a person who has convulsion?
What is fainting?
State the main cause of fainting?
How does drowning differ from near drowning?
Why should patients of second and third degree burns be given a lot of drinks?
Give one difference between first degree burns and third degree burns.
Why is it not good to make the victim who is nose bleeding to face up.
How does a foreign body in the throat cause choking?
</passage>

<passage id="lchk_9dcb4ab681fe405a8dcdb4ec067ee3eb" source="SCIENCE LESSON NOTES FOR P6 2019(1)" part="47">
 Flash light at the entrance of the ear if the foreign body is an insect.
(c) P6 SCIENCE LESSON NOTES 2016Page 150
 Take the victim to the hospital
Foreign body in the nose
Foreign bodies in the nose include;
 Small insects
 Small seeds
 Small stones
First Aid
Tell the victim to blow his nose hard and fast.
Take the casuality to the health worker.
Foreign body in the throat
Foreign body in the throat are mainly large pieces of food or small bone.
Foreign body in the throat lead to choking and death.
First aid
 Give the victim a number of sharp blows in the back
 Wrap your arms around his waist and press the belly upwards strongly.
 If the victim is unconscious, lie him on his back and make several sudden pushes on the belly using
heels of your hands.
 It the person does not breathe, try mouth to mouth breathing.
 Take the victim to hospital
 If the victim is smaller than you, turn him over your folded leg and give sharp blows at the back.
Preventing accidents caused by foreign bodies
 Chew food properly
 Do not talk or laugh when eating
 Keep beads, button, coins, and seeds out of reach of children
 Putting on glasses while moving on motorcycles and bicycles
 Teach children not to put seeds, coins, stones, and soil in their eyes, nose, ears, and mouth.
Poisoning
Poison is any substance once taken into the body damages body organs or causes death.
(c) P6 SCIENCE LESSON NOTES 2016Page 151
Ways poison can be introduced into the body
 Through food
 Through air
 Through animal bites (snakes, rapid dogs)
 Through injections
 Through swallowing (orally)
Common house hold poisons
Paraffin herbicides
Root poison Jik
Petrol Insecticides
Wormcides Diesel
Acaricides Drugs (Aspirin/ chloriqune)
Signs of poisoning
 Rapid breathing
 Fever and sweating
 Feeling thirsty
 Mental confusion
 Comma
 Vomiting
 Loss of balance
First Aid
Give the casuality a lot of fluids (fresh milk).
Why?
To dilute poison in the stomach
Make the person vomit in case its non-corrosive poison.
How to make the person to vomit
 Placing the finger in the mouth or throat.
 Give the victim water mixed with soap
 Rush the victim to the hospital
(c) P6 SCIENCE LESSON NOTES 2016Page 152
NB: If the causality has taken paraffin, petrol, or bleach (Jik), do not make him vomit.
Why?
It causes more damage to the stomach and gullet.
Preventing poisoning
 Keep petrol, paraffin out of reach of children
 Keep drugs out of reach of children
 Follow the doctors prescription
 Buy drugs from recommended pharmacies
 Dispose expired drugs.
 Avoid drugs misuse
The ABC technique followed before giving first AID
A- Air way
B- Breathing
C- Circulation
TOPICAL QUESTIONS
1. Mention the main reason for giving first aid
2. Distinguish burns and scald.
3. How is the cause of burns similar to that of scalds?
4. Why should a burnt hand of a victim be dipped in cool running water?
5. Why is it not advisable to break blisters on the skin?
6. How do heat insulators prevent burns and scalds?
7. Define fever.
(c) P6 SCIENCE LESSON NOTES 2016Page 153
8. List down the main effect of fever.
9. Explain the first aid you can give a person who has fever.
10. How would you help a person who has convulsion?
11. What is fainting?
12. State the main cause of fainting?
13. How does drowning differ from near drowning?
14. Why should patients of second and third degree burns be given a lot of drinks?
15. Give one difference between first degree burns and third degree burns.
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
