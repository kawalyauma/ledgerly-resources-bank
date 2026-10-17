# Job ltsk_cb3075d67fee4bf3b2cf9ef9a70fdc96-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 6 lesson(s) below of week 3 of the Science scheme for Primary Six 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P6: one 40-minute lesson: 3–6 sections; about 16–32 points; worked examples and exam-style points; 6–8 activities.

lessonId=lles_80e57e204f724e928c9958d6d03cb11d: lesson 13, Monday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: First aid for burns — First aid for burns.
  Objectives: Describe or demonstrate first aid for burns.

lessonId=lles_d63e261f107e4043bc4914755961fe30: lesson 14, Tuesday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: Fever and convulsions — Fever and convulsions.
  Objectives: Describe or demonstrate fever and convulsions.

lessonId=lles_de89385225d14487af0153ba9c894e7a: lesson 15, Wednesday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: Causes of fever — Causes of fever.
  Objectives: Describe or demonstrate causes of fever.

lessonId=lles_42446ce24b364adf8ffa5b8aa2f75333: lesson 16, Thursday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: First aid for fever — First aid for fever.
  Objectives: Describe or demonstrate first aid for fever.

lessonId=lles_43e47cb05c67473da0dc9ee29cc8b9c5: lesson 17, Friday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: Near drowning — Near drowning.
  Objectives: Describe or demonstrate near drowning.

lessonId=lles_5a30bef06f864e4091441d10fea09e91: lesson 18, Friday, 1 period(s), 40 minutes.
  Unit: Accidents and First Aid (theme: Human Health). Lesson: First aid for near drowning — First aid for near drowning.
  Objectives: Describe or demonstrate first aid for near drowning.

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

<passage id="lchk_0f111e68199d4db394440b790dbd919d" source="P6 sci notes Batch Watermark" part="53">
 If the blister is not broken, leave it to prevent infection of the wound.
 If the blister is broken, wash the area with soap and clean water and
then cover the skin with cloth to prevent flies bringing germs
First aid for a third degree burn
 First put the burnt area in cold water then cover with a clean cloth.
 Encourage the burnt casualty to drink a lot of fluids like ORS because
victims of second and third degree buns lose a lot of water from their
bodies through the burnt skin by evaporation.
SCALDS
What is a scald?
A scald is an injury caused by wet heat.
Or
A scald is an injury caused by hot liquids.
Causes of scalds
 Through body contact with hot water
 Through body contact with hot water, hot tea, hot milk, hot soup, hot
porridge etc.
First aid of scalds
 Put the injured part in cold water for at least 10 – 15 minutes
Reasons for putting injured part in cold water GOT FROM EDUFLIX APP
Page 168
 To cool the temperature of injured part
 To prevent further damage of the underlying body cells
NOTE: If the injured part cannot be put in cold water, pour cold water
on the injured part
Prevention of scalds and burns
 Keep hot objects far from children’s reach.
 Cook food in raised fire places
 Prevent children from playing near fire places
 Avoid children from playing with hot liquids and metals
 Keep away inflammable liquids such as petrol from the living house.
 Construct fire guards around places where cooking is done
 People should use poor conductors of heat when lifting hot objects
from the fire
 People should avoid using appliances with un – insulated electric
wires.
Fever and convulsions
Fever: Is a condition of the body when the temperature goes beyond the
normal.
Note: Fever is not a disease but a symptom of many diseases.
Convulsions: Are sudden violent body movements which cannot be
controlled
Or
Convulsions: Is when the body shakes or jerks involuntarily.
Causes of fever and convulsions
 Diseases/illness like malaria, measles, meningitis, typhoid etc
 Epilepsy (Fits)
 Exposure of the body to high temperature
 Poisoning
Note: high fever causes convulsions
First aid for fever
 Remove most of the persons clothes
 Perform tepid sponging
 Encourage the person to drink more cold fluids than normal
First aid for convulsions
 Make the person get enough air supply GOT FROM EDUFLIX APP
Page 169
 Remove all the tight clothes and loosen others
 Clear the space where the victim is convulsing from
 Put an object between the teeth to prevent the victim from biting the
tongue.
Near drowning and drowning.
Near drowning: Is a condition when a person stops breathing due to
having a lot of water in lungs but not yet dead.
Drowning: Means dying as a result of the lungs being filled with
water.
Causes of near drowning and drowning
 Swimming pools
 Bathe tubs
 Ponds
 Basins full of water
 Ditches
 Lakes and rivers
 Seas and oceans
Prevention of near drowning
 People should not swim in deep waters without life savers
 People sailing on water should wear life jackets
 People should acquire swimming skills.
 Swimming pools should be fenced
 Septic tanks and other sewerage systems should be covered
 Children should not go near big water sources without grown up
people
 Bath tabs should not be left with water
 Containers filled with water should be kept out of reach of children.
First aid for near drowning
 Yell for help
 Remove the person from water as soon as possible
</passage>

<passage id="lchk_96b8a9c35810499cad9f14f103777116" source="P 6 Primary SIX SCI Notes Teacher AC (0)" part="44">
Sugar should not be put on the burn because it attracts houseflies which bring germs to the wound.
The victim of the second degree burns should be given plenty of fluids to drink.
Third degree burns
There are burns which cause deep burning of the skin.
The skin is burnt deeply and it appears shinny white.
a) The skin is burnt deeply
FIRST AID
Put the burn areas in cool water.
Encourage the casuality to drink a lot of fluids.
NB: Patients of second and third degree burns should be given a lot of fluids to drink.
Why?
They lose a lot of fluids through the burnt skin by evaporation
Prevention of burns and scalds
• Use heat insulators to handle hot objects.
• Cooking from raised places
• Keep petroleum products out of reach of children.
• Do not allow young children to cook.
• Refill lanterns or lamps after putting them off.
• Teach children the dangers of burns
• Tell children to play away from fire places.
Fever and convulsions
Fever is the condition of the body when its temperature goes beyond the normal.
The normal body temperature is 37 o C or 98.4 o F.
Fever is not an illness but a symptom of many illnesses such as malaria, typhoid, measles, etc
Page 152
Effect of fever
It can lead to convulsions
Convulsions
These are uncontrollable jerky movements of the body.
Convulsions can be stopped if the disease causing them is treated.
First aid for convulsions
• Remove all tight clothes from the body of the victim.
• Put an object in the mouth of the victim to stop him from biting the tongue.
• Give the victim plenty of cold drinks after recovery.
• Take the patient to hospital
First aid for fever
Carry out tepid sponging (cold compress).
A wet cloth is put on the forehead or chest of a victim.
Caution
Do not use very cold water because it leads to convulsions.
Fainting
It is the loss of consciousness for a short time
Main cause of fainting
Reduced supply of blood rich in oxygen and food to the brain.
Conditions that can lead to fainting
• Anxiety
• Heavy body exercises
• Extreme sorrow (sad news)
fear
• Prolonged hunger
Page 153
FIRST AID
• Put the victim in open air.
• Remove tight clothings around the neck and chest to enable the victim get enough oxygen.
• Raise the legs of the victim higher than the head.
Why?
To allow blood flow faster to the brain.
Don’t allow the victim to be over crowded
DROWNING
This means dying as a result of having lungs filled water.
Drowning has no first aid since the victim dies.
Near drowning
It is temporary loss of breath due to having one’s lungs filled with water.
A person who has nearly drowned has only four minutes to live therefore a first aider must be very fast to save his life.
First Aid
Remove the victim quickly from water
Shout for help
Lie the person on his back.
Carry out mouth to mouth breathing (kiss of life)
How to carry out mouth to mouth respiration
• Make the victim to lie on his back
• Tilt the head backwards and keep his mouth opened
• Remove any object stuck in the mouth
• Press the victim’s nostrils with your fingers to close them
• Put your mouth directly into the mouth so that the chest rises.
• Stop a bit to let the air out and blow again
• Repeat this many times (about 15 times in a minute)
• Continue the steps until the victim can breathe again by himself.
• Place the heels of your hands between the navel and the ribs of the victim
• Make a quick strong push forward into the ribcage.
Page 154
How to prevent near drowning
• Acquire swimming skills
• Always empty bath tubs
</passage>

<passage id="lchk_f40b92e904a047848ab2874de1234e64" source="P 6 Primary SIX SCI Notes Teacher AC (0)" part="46">
• Teach children not to put seeds, coins, stones, and soil in their eyes, nose, ears, and mouth.
Poisoning
Poison is any substance once taken into the body damages body organs or causes death.
Ways poison can be introduced into the body
• Through food
• Through air
• Through animal bites (snakes, rapid dogs)
• Through injections
• Through swallowing (orally)
Common house hold poisons
Paraffin herbicides
Root poison Jik
Petrol Insecticides
Wormcides Diesel
Acaricides Drugs (Aspirin/ chloriqune)
Signs of poisoning
• Rapid breathing
• Fever and sweating
• Feeling thirsty
• Mental confusion
Page 158
• Comma
• Vomiting
• Loss of balance
First Aid
Give the casuality a lot of fluids (fresh milk).
Why?
To dilute poison in the stomach
Make the person vomit in case its non-corrosive poison.
How to make the person to vomit
• Placing the finger in the mouth or throat.
• Give the victim water mixed with soap
• Rush the victim to the hospital
NB: If the causality has taken paraffin, petrol, or bleach (Jik), do not make him vomit.
Why?
It causes more damage to the stomach and gullet.
Preventing poisoning
• Keep petrol, paraffin out of reach of children
• Keep drugs out of reach of children
• Follow the doctor’s prescription
• Buy drugs from recommended pharmacies
• Dispose expired drugs.
• Avoid drugs misuse
The ABC technique followed before giving first AID
A- Air way
B- Breathing
Page 159
C- Circulation
TOPICAL QUESTIONS
1. Mention the main reason for giving first aid
2. Distinguish burns and scald.
3. How is the cause of burns similar to that of scalds?
4. Why should a burnt hand of a victim be dipped in cool running water?
5. Why is it not advisable to break blisters on the skin?
6. How do heat insulators prevent burns and scalds?
7. Define fever.
8. List down the main effect of fever.
9. Explain the first aid you can give a person who has fever.
10. How would you help a person who has convulsion?
11. What is fainting?
12. State the main cause of fainting?
13. How does drowning differ from near drowning?
14. Why should patients of second and third degree burns be given a lot of drinks?
15. Give one difference between first degree burns and third degree burns.
16. Why is it not good to make the victim who is nose bleeding to face up.
Page 160
17. How does a foreign body in the throat cause choking?
18. Why would you give plenty of drinks to a person who has taken poison?
19. Why is it dangerous to make a person who has drunk paraffin to vomit?
20. Mention one way of preventing poisoning at home.
SANITATION
Definition:
Sanitation is the general cleanliness of a place where we live.
Ways of maintaining sanitation
• Construction of latrines or toilets for proper disposal of wastes.
• Digging rubbish pits and providing dust bins for proper disposal of house hold refuse.
• Slashing bushes around the homes.
• Draining away all stagnant water to deny mosquitoes breeding and protecting water sources.
Constructing a latrine or toilet
A latrine is pit dug in the ground where human excreta is deposited.
Uses of latrines
They keep faeces and urine where vectors cannot bring them to our food.
Types of latrines
i) Pit latrine
ii) Toilets
iii) Potties
Pit Latrines
Qualities of a well built latrine
• It should be 5 to 7 metres deep
Page 161
• The floor should be strong enough to stand on and smooth to sweep and clean.
• It should have a hole big enough to allow faeces and urine to pass and small enough to prevent children from falling inside.
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
