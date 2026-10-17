# Job ltsk_6134f81b91644e9c9c1e2e7edc966262-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for Science, Primary Six 2026, Term 3.
The term has 10 teaching weeks and this subject has 6 periods per week. Every lesson is ONE 40-minute period, so keep each lesson small enough to teach in 40 minutes.
There are no weekly review lessons: the subject has a lot of content, so every period teaches or practises.
Give at most 59 teaching/practice lesson entries in teaching order (the last lesson of the term is the end of term assessment).
Each lesson has a kind: "teach" (new content) or "practice" (the same subtopic as the teaching lesson just before it: exercises, oral work, drawing, matching, filling in blanks, ALL taken from the passages).
When the material is thin (common in lower primary), follow each teaching lesson with a practice lesson. Split big subtopics over several teaching lessons.
Never pad with content the passages do not have: if they cannot fill the term, return fewer lessons and list what is missing in gaps. Ledgerly fills the remaining weeks with revision.
You are composing the SCHOOL'S OWN scheme. The passages below (the official NCDC curriculum and guides, plus schemes of work, lesson plans, notes and past papers from the school e-library) are reference material:
The NCDC documents (titles starting "NCDC") are the BASE: their topics, competences and order for this class and term are what the scheme must cover. NCDC lower-primary thematic curricula list every learning area side by side in table columns separated by " | ": take only the Science column.
Every topic the NCDC curriculum lists for this class and term MUST become a unit, in the NCDC order. Share the weeks between ALL of them according to their NCDC periods, competences, content and subtopics. Large topics should receive more lessons than small topics.
combine them in this authority order: curriculum for required coverage; all relevant schemes for sequence and pacing; the strongest detailed notes for accurate teaching depth; past papers for expected applications and activities. Do not copy one reference scheme blindly.
Use this term's part of the material (Term 3) when the passages cover several terms.

REQUIRED NCDC topics/themes for Primary Six 2026, Term 3 (from the NCDC curriculum, in this order). Every one MUST have at least one unit whose title or theme names it, with about this many teaching/practice lessons:
  10. Accidents and First Aid: about 19 lessons
  11. Sanitation: about 19 lessons
  12. The Reproductive System: about 21 lessons
Keep to these evidence-based shares. A broad topic may take substantially more lessons than a small topic when its NCDC scope, competences and subtopics justify it.
Do NOT write lesson content yet. Each unit and lesson must cite the passage ids it comes from in sourcePassageIds.

Reply shape:
{"title":string,"summary":string,"units":[{"title":string,"theme":string|null,"weekFrom":int|null,"weekTo":int|null,"competences":string|null,"sourcePassageIds":[string],"lessons":[{"title":string,"subtopic":string|null,"kind":"teach"|"practice","objectives":[string],"sourcePassageIds":[string]}]}],"gaps":[string]}

<passages>
<passage id="lchk_f16b9ab2a13f457884791c7d5abfca5a" source="NCDC P6 Set One Sept book – Integrated Science" part="1">
Integrated Science Syllabus

Introduction to the Primary Six Integrated Science Syllabus

Background
This is the Primary Six Integrated Science Syllabus. From Primary One
to Three (P1-3), learning was based on themes, learning outcomes and
competences. Most of the science-related competences are covered under
the literacy strands of the Thematic Curriculum. From P4-7, learning
is based on subjects. The science syllabus outlines learning outcomes,
content and language competences.

Learners in P6 are expected to have developed basic literacy skills in
English language, therefore you are expected to use English as the medium
of instruction. You are required to assess from time to time if learners
understand the concepts correctly and are able to consolidate what was
acquired in earlier classes. As a teacher, you need to know that some of the
learners in your class are exceptional; therefore, it is your duty to arrange
activities basing on each learner’s needs. Accommodating all learners’
individual needs should be addressed and if necessary adaptations should
be made in the areas of methodology, content, environment, teaching
steps and learning materials.

This Integrated Science Syllabus brings together content of Biology,
Physics, Chemistry, Health, Agriculture and Environment. The scientific
knowledge and skills from these aspects must be presented to the learners
in a practical integrated and an interesting manner.

The instructional process will follow what was in the old syllabus and you
will be required to use the old instructional materials such as textbooks,
charts and so on.

Rationale
This revised P6 Integrated Science Syllabus has been designed to
consolidate the basic literacy and numeracy skills acquired during the
Thematic Curriculum, the P4 Transition Year and P5. It will further
develop learners’ language competences.

It is also intended to provide learners with knowledge, skills, attitudes,
practices and values on basic science, health, agriculture and environment

National Curriculum Development Center

that are important to prepare learners for the final assessment of the
primary cycle and self-reliance.

The changes that have been made in this P6 syllabus include:
• topic overflows from P5 that were moved to P.6 that is;
Circulatory System and Respiratory System.
• overlaps found in P5, P6 and P7 that were merged in P6
include:
a) “Essential drugs” and “Drugs of Dependency,” “Smoking and
Drugs,” and “Alcohol in Society”;
b) “Respiration and Respiratory System”
c) “Sexually Transmitted Diseases to the Reproductive System.
• The background of each topic will remind you from which class
the topic was shifted.
• by merging topics, content has been reduced in order to keep
learning experiences lighter and simpler than before.
Other changes emphasised include:
– | the scope and sequencing of content has been based on progression
of outcomes and competences.
– | literacy skills and language competences have been included in
each topic to clarify concepts.
– | possible life skills which can be developed have been suggested
in each topic.
– | subject competences and language competences have been
included to replace objectives. These competences are arranged
in order of cognitive levels namely knowledge, comprehension
and application.
– | language competences have been included especially to reinforce
literacy skills and to help clarify concepts.
– | general outcomes instead of aims and objectives have been
</passage>

<passage id="lchk_ca94afec6f3d42c2b4519c1b710833bd" source="NCDC P6 Set One Sept book – Integrated Science" part="2">
provided for each topic.
– | the background for each topic has been given together with other
necessary guidance to the teacher.
– | key words for each topic have been included in order to enrich
the learner’s vocabulary and mastery of concepts. A word list is
given at the end of this science syllabus.

Primary 6 Curriculum

– | the suggested number of periods vary because some topics have
more aspects for you to cover while others are being finalised in
this class.
– | this syllabus provides guidance to the teacher. There is no
separate teachers’ guide.

General Methodology
During the teaching/learning process, you are expected to enhance
learning through the most effective learner-centred methods and activities.
You will be expected to facilitate learning as the learners do the activities.
The active verbs used in expressing the learning competences are all
directed to the learner. As a result of the teaching/learning process, the
learner should exhibit these competences.

You are expected to use a variety of existing books and charts to prepare
the correct content on the topics. You should use the environment as
much as possible to help the learners relate science to real life situations
and experiences. Often you will be required to let the learners carry
out experiments, exhibitions, projects, field trips and excursions. You
should encourage the learners to record and report on their findings.
You should also use examples that will provide the learner with
opportunities to explore, and acquire knowledge, concepts, skills, values
and competences.

Your classroom should possess different, attractive, incidental reading
materials in form of related science pictures, nature corner, word cards,
educational charts, and many other materials that can boost learning. Use
those materials that are relevant and learner-friendly.

Task analysis is another important approach, that is breaking down the
available content or activity to be taught into simpler manageable steps
that can be accommodated easily at the pace of every individual learner.

Assessment Guidelines
Continuous Assessment is recommended and should be based on the
summarised competences provided at the end of each topic and learning
competences given in the syllabus. Assessment should be included as
part of each lesson activity, must be purposeful originating from a specific

National Curriculum Development Center

learning achievement you want to observe in a learner as a result of the
lesson. Therefore, it must be included as part of every lesson plan in which
specific individual learners with learning challenges are being assessed.
When you teach, you are teaching a class of individual learners. In order
to help them learn, you need to know their weaknesses and strengths on a
continuous basis. This will help you to structure any follow-up strategies
and what to focus on for assessing each learner.

One of the principles of the new primary curriculum is its emphasis
on developing competences. The P6 curriculum covers both subject
and language competences. This aims at mastering various skills with
understanding rather than memorising content.

Like it was done in P4 and P5, in P6, assessment guidelines are provided
to guide you in carrying it out, managing and keeping records on each
individual learner, class progress and end of term performance. You are
therefore encouraged to record innovative products of the learner that
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

<passage id="lchk_fba7daf4aac04826b9e9b847d448b677" source="Tekart Primary Six Science 2024" part="1">
Science
Tekule Musa
TEKART LEARNING
First Edition
Primary Six
www.tekartlearning.com
Based on the
National Curriculum
1
Topic 1: classification of animals
Characteristics of living things
➢ They feed
Nutrition is the taking in of food (materials) for energy, growth and
development. Plants require sunlight, carbon dioxide and water. Animals
need food and water.
➢ They grow
Growth is a permanent increase in size and dry mass by an increase in cell
number, cell size or both. Even bacteria and single-celled organisms show
an increase in size. Multicellular organisms like humans increase the
number of cells in their bodies, become more complicated and change their
shape as well as increasing in size.
➢ They reproduce
Reproduction is the process by which organisms produce young ones
similar to themselves. Single-celled organisms and bacteria may simply
keep dividing into two (Binary fission). Multicellular plants and animals may
reproduce sexually or asexually.
➢ They respond to stimuli
Sensitivity is the ability to detect or sense stimuli in the internal or external
environment and to make appropriate responses.
➢ They move
Movement is an action by an organism or part of an organism causing a
change of position or place. Most single-celled creatures and animals move
about as a whole. Fungi and plants may make movements with parts of their
bodies.
➢ They excrete
Excretion is the removal of waste products from organisms. Toxic materials
and substances in excess have to be removed from the body. Excretion
prevents damage of body organs due to accumulation of wastes.
➢ They respire
Respiration describes the chemical reactions in cells that break down
glucose and release energy for body processes. Most organisms need oxygen
for this.
Living things are divided into five kingdoms namely;
• Animal Kingdom
• Plant Kingdom
• Prokaryote (Bacteria Kingdom)
• Protoctista (single celled organisms)
• Fungi Kingdom
2
Animal Kingdom
Animals are multicellular organisms whose cells have no cell walls or
chloroplasts. Most animals ingest solid food and digest it internally.
Animals are classified into two groups
• Vertebrates
• Invertebrates
Vertebrates
Vertebrates are animals with a back bone /vertebral column (spine)
Groups of vertebrates
Vertebrates are classified into five classes;
• M ammals
• B irds
• R eptiles
• F ish
• A mphibians
For remembering ( A ll M y B est F riends R epresent Vertebrates!).
Vertebrates are grouped into two major groups;
i. Warm blooded (homoeothermic)
ii. Cold blooded (poikilothermic)
Warm blooded
These are animals that can maintain a constant body temperature.
i) Mammals
ii) Birds
Cold blooded
These are animals that cannot maintain a constant body temperature.
i) Fish
ii) Reptiles
iii) Amphibians
Mammals
Mammals are vertebrates which have mammary glands. All female mammals have
mammary glands, which secrete milk to nourish their young ones. Mammalian
teeth are differentiated into incisors, canines, premolars, and molars and the
middle ear contains three sound-conducting ear ossicles.
Characteristics of mammals
• Mammals are warm blooded.
• They have fur on their bodies.
• Most of them give birth to living young ones.
• They feed their young ones on breast milk.
• They breathe through the lungs.
3
• Their hearts are divided into four chambers. The four-chambered heart
enables complete separation of oxygenated and deoxygenated blood.
Groups of mammals
• Primates (most advanced /fingered mammals)
• Ungulates (hoofed mammals)
</passage>

<passage id="lchk_438d837d307c4a5cb9df5094c4aabb2a" source="Tekart Primary Six Science 2024" part="2">
• Carnivorous mammals (flesh eaters)
• Rodents (gnawing mammals)
• Insectivorous (insect eaters)
• Pouched mammals (marsupials)
• Flying mammals (chiropteran)
• Egg laying mammals (monotremes)
• Sea mammals (cetaceans)
• Lagomorpha
Primates
These are the most advanced group of mammals. Their brain, particularly the
cerebrum, is relatively large and well developed, accounting for the intelligence
and quick reactions of these mammals.
Characteristics of primates
• They have well developed brain.
• They use front limbs for holding and hind limbs for walking.
• They have five fingers on each hand and five toes on each foot.
• They are omnivorous i.e. they feed on both flesh and vegetables.
• They have well developed set of all the four types of teeth i.e. incisors, canines,
premolars and molars (32 teeth)
Examples of primates
Humans, monkeys, gorillas, baboon, bush baby, chimpanzee, orangutan.
Humans Gorilla Bush baby
4
Baboon Chimpanzee Orangutan
Monkeys Lemur Tarsier
Ungulates (hoofed mammals)
These are herbivorous mammals with hoofed feet. All mammals in this group are
herbivorous i.e. they feed on vegetation.
Ungulates are divided into two sub-groups
i) Even toed ungulates
ii) Odd toed ungulates
Even toed Odd toed
Even toed ungulates
These have hooves arranged in even form and have the third and fourth digits
equally developed and bear the weight of the body. They include; Deer, pigs,
cattle, giraffe, sheep, antelopes, hippopotamus.
Even toed ungulates are subdivided into two;
i) Ruminants
5
ii) Non-ruminants
Ruminants
These are ungulates with four stomach chambers and chew cuds. Swallowed food
passes from the first chamber, the reticulum , to the rumen , where food is
digested by cellulase and other enzymes that live in the rumen. Some products of
digestion are absorbed in the rumen; the remaining partly digested food is
regurgitated (to bring back what has been swallowed) and chewed to a pulp – the
process known as ‘chewing the cud’. This food mass is then swallowed and passes
from the reticulum to the third chamber, the omasum , where water and some
nutrients are absorbed; and finally, to the abomasum , in which further digestion
takes place.
Stomach of a ruminant
Examples of ruminants
• Cattle
• Goats
• Sheep
• Camel
• Antelope
Cow Goat Sheep
6
Non-ruminants
• These are ungulates which do not chew cud but have a complete dentition.
• They have well developed canines which they use for protection
Examples of non-ruminants
Pigs, hippopotamus, warthog
Pig Hippo Warthog
Odd toed ungulates
The number of toes is always odd e.g. one in horse, donkey, zebra and three in
elephant and rhino.
Rhino Elephant Donkey
Carnivorous mammals
A group of mainly flesh-eating mammals. Carnivores typically have very keen
sight, smell, and hearing. The hinge joint between the lower jaw and skull is very
tight, allowing no lateral movement of the lower jaw. This – together with the
arrangement of jaw muscles – enables a very powerful bite. The teeth are
specialized for stabbing and tearing flesh: canines are large and pointed.
Characteristics of carnivorous animals.
o They are strong mammals
o They have well developed canine teeth for tearing flesh of their prey.
o They have sharp claws for holding, killing and tearing their prey.
o They have a very good speed, good sense of smell, keen eye sight and good
hearing.
o This is why they even hunt at night.
7
o Their feet have soft pads therefore thus can ran after their prey without
making noise.
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
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
