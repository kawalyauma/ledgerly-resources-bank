# Job ltsk_2e6488baae014bac97494970e8e6b92e-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 6 lesson(s) below of week 1 of the Science scheme for Primary Six 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P6: one 40-minute lesson: 3–6 sections; about 16–32 points; worked examples and exam-style points; 6–8 activities.

lessonId=lles_d05728906d2b44f1a6821687fbb85097: lesson 1, Monday, 1 period(s), 40 minutes.
  Unit: Science at Home and in Our Community (theme: Science in Human Activities and Occupations). Lesson: Safe drinking water — Safe drinking water.
  Objectives: Describe or demonstrate safe drinking water.

lessonId=lles_487f493cee954c7c968c6958b83f6469: lesson 2, Tuesday, 1 period(s), 40 minutes.
  Unit: Science at Home and in Our Community (theme: Science in Human Activities and Occupations). Lesson: Water impurities — Water impurities.
  Objectives: Describe or demonstrate water impurities.

lessonId=lles_b65189aea11848329da9daf3871c0a06: lesson 3, Wednesday, 1 period(s), 40 minutes.
  Unit: Science at Home and in Our Community (theme: Science in Human Activities and Occupations). Lesson: Boiling water — Boiling water.
  Objectives: Describe or demonstrate boiling water.

lessonId=lles_e52ce5f2126b425fa858c3df16286e98: lesson 4, Thursday, 1 period(s), 40 minutes.
  Unit: Science at Home and in Our Community (theme: Science in Human Activities and Occupations). Lesson: Filtering water — Filtering water.
  Objectives: Describe or demonstrate filtering water.

lessonId=lles_7fe1d23bcb78465fa793028bdf830a67: lesson 5, Friday, 1 period(s), 40 minutes.
  Unit: Science at Home and in Our Community (theme: Science in Human Activities and Occupations). Lesson: Treating water — Treating water.
  Objectives: Describe or demonstrate treating water.

lessonId=lles_bd74e013218c4843b3003456e5b101d9: lesson 6, Friday, 1 period(s), 40 minutes.
  Unit: Science at Home and in Our Community (theme: Science in Human Activities and Occupations). Lesson: Distilling water — Distilling water.
  Objectives: Describe or demonstrate distilling water.

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

<passage id="lchk_3992e00e9502482f9c49407a8d400893" source="P 6 Primary SIX SCI Notes Teacher AC (0)" part="42">
• Diaphragm and intercostals muscles contracts.
• Ribs move upwards and outwards.
• The lungs increase in volume
What happens during expiration /exhalation?
• The volume of the chest and lungs decreases.
• The diaphragm and intercostals muscles relax.
• Ribs move downwards and inwards.
• The lungs decreases in volume.
Diseases that attack the breathing/respiratory system.
Tuberculosis Bronchitis
Influenza Asthma
Diphtheria Pneumonia
Emphysema Whooping Cough
Habits that improve the working of the respiratory system
• Avoiding smoking
• Having regular physical exercises.
• Good feeding/nutrition
• Eat food with low and fat
• Keep away from dusty places etc.
Disorders of the respiratory system
Choking
Hiccup
Sneezing etc
RESPIRATION IN RELATION TO FOOD AND OXYGEN
- Respiration is the chemical burning of food in the presence of oxygen in order to release ( produce ) energy
- Water and carbondioxide are released as by products.
Page 145
- Respiration takes place in the body cells
- Food + oxygen carbondioxide + water + energy (ATP)
(Starch )
Types of respiration
Aerobic respiration
Is respiration which uses oxygen.
Anaerobic respiration
It is a type of respiration which takes place in absence of oxygen and in which food substances are only partly broken down. It
produces lactic acid in animals and alcohol in parts. It occurs in muscles during exercise.
Page 146
SCIENCE PRIMARY SIX TERM III
SCIENCE AT HOME AND COMMUNITY
WATER
Water is a colourless liquid substance made up of hydrogen and oxygen gases. These gases are in the ratio of 2:1 (H 2 O)
Sources of water
• Rain water
• Artesian wells
• Hot springs
• Streams, lakes, rivers, swamps, ponds, oceans, and seas.
Properties of pure water
• It is colourless
• It is without suspended matter like germs.
• It has no smell
• Pure water is tasteless
• Pure water boils at 100 o C (212 o F) and freezes at 0 o C (32 o F) at sea level.
• Pure water forms lather (foam) very easily) with soap.
Uses of water to the body
• Water makes up part of blood as plasma
• Helps to dissolve the digested food for easy absorption in the body.
• Maintains the shape of body cells.
• Cools the body in form of sweat when it evaporates.
• Helps in formation of body fluids such as tears, saliva, urine, sweat etc.
Other uses of water
• For domestic use e.g. cooking, washing etc
• For drinking by man, mammals, and birds
Page 147
• For irrigation in agriculture
• Used in industries for cooling, washing machines and raw materials.
• Used to generate hydro-electricity
• Used by plants for photosynthesis
Preparation of safe water for drinking
i. Boiling
When water is heated, it boils, to a temperature of 100 o C (212 o F) this temperature kills germs.
ii. Filtering
This is the process by which a clean or sterilized piece of cloth or local water filter.
Examples of solid impurities filtered are dirt, soil, stones, leaves, animals wastes etc.
NB: Filtered water is not safe for drinking because it may be containing some germs.
iii. Treatment of water
Treatment of water is when chemicals are added to kill germs in it.
Examples of chemicals used to treat water are; chlorine, water guard and aquasafe.
Advantages of chemicals used in water treatment
The chemicals kill germs in water
Disadvantages of using chemicals
• They are expensive
• They do not make water clear
• They add some smell and taste to water.
DECANTING
Decanting is a method of removing large particles of objects from water.
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

<passage id="lchk_8e9d431e9d6b47f498cca1284b751ed0" source="P6 sci notes Batch Watermark" part="51">
 Water exerts pressure
 Water finds its own level
 Water is a good solvent
 Water can dissolve gases
Diagrams showing the properties of water
Water exerts pressure
Water finds its own level
Water can dissolve gases
Uses of water in the body GOT FROM EDUFLIX APP
Page 160
 Water makes up part of blood as plasma
 Water helps to dissolve digested food for easy digestion
 Water maintains the shape of the body cells
 Water takes part in changes that must occur in the body such as
cooling as sweat.
 Water is a medium where chemical changes takes place in the body.
Domestic uses of water
 Water is used for cooking food
 It is used for washing clothes
 Water is used for bathing our bodies
 Water is used for washing utensils
 Water is provided to animals to drink
Industrial uses of water
 Water is used for generating electricity
 Water is used for recreation like swimming and boating
 Water is used for cooling machines in industries
 Water is used to clean machines in industries
Preparation of clean water
Methods of obtaining clean water from dirty water include:
 Decantation/Decanting method
 Filtration/Filtering method
 Distillation (clean water is water that does not contain germs)
Decantation
This is the method of removing solid particles from water
Experiment to show decantation GOT FROM EDUFLIX APP
Page 161
Filtration
This is the process of separating solid particles from water
The solid particles that remain on the filter are called the filtrate
Experiment to show filtration
Distillation
This is the process which involves evaporation of the liquids and then
condensing the vapour to liquid form.
The water obtained through distillation is called distilled water
Note: Distilled water is used by doctors to mix drugs for injection.
Distilled water is not food for drinking because it does not contain
mineral salts.
Experiment to show distillation method GOT FROM EDUFLIX APP
Page 162
Preparation of safe water
Safe water is water which is free from germs
Methods of preparing safe water
 Boiling water
 Distillation
 Treating water using chemicals like chlorine, water guard, florine,
calcium chloride, potassium permanganate
Water pollution or water impurities
Water pollution is the process of making water contaminated.
Water impurities are substances added to water and change the nature of
quality of water
Examples of water impurities
 Bacteria
 Viruses
 Microscopic plants and animals like amoeba and spirogyra
 Dead plant matter
 Fine particles of mud
 Sand
Ways of polluting water
 Urinating in water sources
 Deficating in water sources
 Dumping industrial wastes in water sources
 Dumping heavy metals in water sources
 Silting
 Leakages of petroleum products into water sources
Silting
This is the deposition of soil and other materials into the water bodies by
erosion.
Examples of silts GOT FROM EDUFLIX APP
Page 163
 Soil
 Grass
 Metal scraps
 plastics
 polythene paper
Effects of silting to water bodies
 Silts reduces the depth of water bodies
 Silts leads to dryness of rivers, swamps and lakes
 Silting leads to flooding of surrounding areas
 Silts kill aquatic animals
 Silts cover the breeding ground for fish
Dangers of water
 Water carries harmful germs that cause diseases like cholera and
typhoid
 Poisonous substances from factories, human wastes, detergents are
often dumped into rivers and lakes by water.
 Flowing water causes soil erosion
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
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
