# Job ltsk_9e8f8f73b860400fb45a3b163422108f-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for Social Studies, Primary Seven 2026, Term 3.
The term has 10 teaching weeks and this subject has 5 periods per week. Every lesson is ONE 40-minute period, so keep each lesson small enough to teach in 40 minutes.
There are no weekly review lessons: the subject has a lot of content, so every period teaches or practises.
Give at most 49 teaching/practice lesson entries in teaching order (the last lesson of the term is the end of term assessment).
Each lesson has a kind: "teach" (new content) or "practice" (the same subtopic as the teaching lesson just before it: exercises, oral work, drawing, matching, filling in blanks, ALL taken from the passages).
When the material is thin (common in lower primary), follow each teaching lesson with a practice lesson. Split big subtopics over several teaching lessons.
Never pad with content the passages do not have: if they cannot fill the term, return fewer lessons and list what is missing in gaps. Ledgerly fills the remaining weeks with revision.
You are composing the SCHOOL'S OWN scheme. The passages below (the official NCDC curriculum and guides, plus schemes of work, lesson plans, notes and past papers from the school e-library) are reference material:
The NCDC documents (titles starting "NCDC") are the BASE: their topics, competences and order for this class and term are what the scheme must cover. NCDC lower-primary thematic curricula list every learning area side by side in table columns separated by " | ": take only the Social Studies column.
Every topic the NCDC curriculum lists for this class and term MUST become a unit, in the NCDC order. Share the weeks between ALL of them according to their NCDC periods, competences, content and subtopics. Large topics should receive more lessons than small topics.
combine them in this authority order: curriculum for required coverage; all relevant schemes for sequence and pacing; the strongest detailed notes for accurate teaching depth; past papers for expected applications and activities. Do not copy one reference scheme blindly.
Use this term's part of the material (Term 3) when the passages cover several terms.

REQUIRED NCDC topics/themes for Primary Seven 2026, Term 3 (from the NCDC curriculum, in this order). Every one MUST have at least one unit whose title or theme names it, with about this many teaching/practice lessons:
  9. Economic Developments in: about 25 lessons
  10. Major World Organisations: about 24 lessons
Keep to these evidence-based shares. A broad topic may take substantially more lessons than a small topic when its NCDC scope, competences and subtopics justify it.
Do NOT write lesson content yet. Each unit and lesson must cite the passage ids it comes from in sourcePassageIds.

Reply shape:
{"title":string,"summary":string,"units":[{"title":string,"theme":string|null,"weekFrom":int|null,"weekTo":int|null,"competences":string|null,"sourcePassageIds":[string],"lessons":[{"title":string,"subtopic":string|null,"kind":"teach"|"practice","objectives":[string],"sourcePassageIds":[string]}]}],"gaps":[string]}

<passages>
<passage id="lchk_c8e10e5097074644ad353ff3556c7e2b" source="NCDC PRIMARY SEVEN SET ONE – Social Studies" part="1">
Social Studies Syllabus

Primary Seven Curriculum

Background
The P7 learner has gone through a variety of experiences on the physical
and social environments. By this time, the learner has been exposed to
living together in an expanding environment, starting with the familiar
ones such as a home, school, neighbourhood, sub-county, municipality,
district, Uganda and East Africa. The learner will now be exposed to the
rest of Africa, under the theme “Living together in Africa”.

A number of physical, social, political and economic aspects have been
covered to enhance the learners’ knowledge and skills on how human
beings interact with other living things to survive in different types of
environments.

Rationale
Social Studies (SST) is designed to equip the learners with knowledge,
skills, values and desired attitudes which are required to prepare them
for living in a physical, social, political and economic environment as
knowledgeable and as participating citizens of society. Primary Seven
SST competences are intended to prepare learners in their final year of
primary school education to higher academic levels. Learners will use
the knowledge, skills and values to interact with others from various
communities and backgrounds and this is why they should be exposed to
the wider community for a harmonious living.

Social Studies can provide learners with the skills for productive
problem-solving and decision-making, as well as for assessing issues
and making thoughtful value judgements. Above all, Social Studies helps
learners to integrate these skills and understandings into a framework for
responsible citizen participation, whether in their play group, the school,
the community or the world.

Social Studies content integrates knowledge, skills and attitudes within
and across disciplines. This helps learners to view and relate the concepts
of physical, social, political and economic factors which will enable them
cope with multiple perspectives in the dynamic world.

It is important for learners to begin to understand, appreciate and apply
knowledge, skills and values in other academic disciplines as a way of

National Curriculum Development Centre

disciplinary integration. Such interdisciplinary-based learning draws
simultaneously from several disciplines in clarifying specific concepts.
Social Studies addresses the contemporary conditions of real life and
academic scholarship.

Learning Outcomes
The following are the expected learning outcomes of the P7 SST learning
and teaching process:
1. | Promotes an appreciation of Africa as a continent, where our
own country exists.
2. | Demonstrates the usage of lines of latitudes and longitudes to
locate Africa, its regions and member countries.
3. | Explores, identifies and appreciates the value of one’s
immediate and distant environment for better and harmonious
living.
4. | Identifies and appreciates the importance of climate and how it
determines and supports human, animals and plant life.
5. | Appreciates the value of vegetation and endeavours to care for
it for better and harmonious living.
6. | Demonstrates and promotes values, social practices in the
society and shows respect for his/her own and other cultures.
7. | Identifies the importance of interdependence of nations and
continents.
8. | Demonstrates and explains the use of map reading skills,
interpretation and analysis of data.
9. | Demonstrates knowledge and appreciates the rights of
</passage>

<passage id="lchk_411e092405944d91882777f9ec80cdd7" source="NCDC PRIMARY SEVEN SET ONE – Social Studies" part="2">
individuals in society and recognises and practises collective
responsibility in bringing order, social justice, and political
growth.
10. Identifies and appreciates the values of being in an independent
state and appreciates the events that led to independence.
11. Identifies and examines natural resources and their importance
in the development of Africa.
12. Explores and understands the challenges African states face and
highlights strategies to overcome them.

Primary Seven Curriculum

13. Appreciates the inter-dependence among nations and the
contribution made by United Nations agencies.
14. Appreciates the role-played by the Commonwealth in the
development of member countries.
Methodology
Teaching Social Studies calls for the application of various methods which
support the development of literacy, numeracy, positive behaviour,
desired attitudes, values and application of life and study skills. Therefore,
the following generic methods are recommended for use:
• | Group discussion
• | Project method
• | Dramatisation
• | Exhibition
• | Construction
• | Inquiry
• | Discovery method
• | Problem-solving method
You are encouraged to explore and use various teaching methods.

Method | Techniques
Discussion | • Brainstorming, question and answer, debate,
resource person, storytelling, arguments, experiment,
observation, illustration, interview and field visits

Projection | • Audio-visual, video recording, slides, films, trips and
method | audio-recording

Dramatisation | • role-play, drama, conversations, dialogue or
monologue and simulation
Exhibition | • Display, interest corner/centre, picture essays,
demonstration, ground and wall maps and real objects
Representation | • Drawing, painting, sculpture, modelling, use of
diagrams, charts, photographs, posters and so on
Group method | • Grouping, reporting, brainstorming and display

Problem- | • Sorting, competitions, initiations, note making, puzzles,
solving | quizzes and debates

National Curriculum Development Centre

Inquiry or | • Project assignment, research, field visits, excursion,
discovery | questions, resource persons, observations, recording
and interviews

Life Skills
A life skill is the ability to cope with any emerging situation both in
happiness and difficulty. For effective teaching of SST, you are advised
to develop life skills in the learner. Life skills and values should be
incorporated in your scheme of work and lesson plan. Life skills cannot
be developed in a single lesson. It takes time.

Life skills are grouped into three categories:
1. Skills for living and knowing oneself
a) | Self-awareness: knowing one’s strengths and weaknesses.
b) | Self esteem: having confidence in oneself.
c) | Coping with emotions: one’s ability to manage or deal
effectively with situations or problems such as fear, love, anger,
shyness, disgust and the desire to be accepted by others.
d) | Coping with stress: overcoming physical, psychological and
emotional tension arising out of difficult situations.
e) | Assertiveness: expressing one’s feelings, needs or desires
openly and specifically in a respectful manner.
2. Skills of knowing and living with others
a) | Interpersonal relationships: ability to relate freely with others.
b) | Friendship formation: the ability to build/make meaningful
and healthy associations with people.
c) | Empathy: the ability to understand and address other people’s
circumstances/problems and finding ways of helping them
make the right decisions.
</passage>

<passage id="lchk_527b2d4028b540489573908c47f7a593" source="NCDC PRIMARY SEVEN SET ONE – Social Studies" part="3">
d) | Peer pressure resistance: overcoming misleading influence from
friends.
e) | Negotiation: ability to come up with agreed positions.
f) | Non-violent conflict resolution: ability to handle hostile
situations or friction calmly and peacefully.

Primary Seven Curriculum

g) | Effective communication: ability to express oneself clearly and
appropriately.
3. Skills of making effective decisions
a) | Critical thinking: ability to explore possibilities of solving
problems.
b) | Creative thinking: ability of coming up with new ways of doing
things, ideas, arrangements or organisations.
c) | Decision-making: ability to make the right choice from
alternatives.
d) | Problem-solving: ability to identify, cope with and find
solutions to difficult or challenging situations.
Social Studies Skills
The skills that are primary to Social Studies are those related to maps and
globes, such as understanding and using locational and directional terms.
These SST skills are categorised as study and manipulative skills.

Study skills
A study skill is the ability to collect, analyse and use information during the
teaching/learning process. Some examples of study skills are: listening,
observing, investigating, reading, writing, grouping/classifying,
analysing, experimenting, collecting and recording information.

Manipulative skills
A manipulative skill is the ability to express knowledge by the use of
hands and other body parts. Some of these skills are displaying, drawing,
painting, modelling, making cut-outs and all activities done using hands.

Values and Attitudes
Values are things we believe in and support openly such as orderliness,
honesty, love, carefulness, respect, faithfulness, obedience, kindness and
trustworthiness.

Attitudes are inner feelings manifested by actions like appreciation,
cooperation, patience, tolerance, empathy and sympathy.

National Curriculum Development Centre

Instructional Materials
The following instructional materials may be used to support the
teaching/learning process of the subject.
• Reference books
• Textbooks
• Wall maps
• Charts
• Globes
• Flash cards
• Models
• Radios
• Televisions
• Other audio/visual aids
Above all, you are encouraged to use the environment. This is a major
source of teaching and learning aids. The things provided by the
environment are plants, animals, physical features, houses, factories,
household property, social service centres such as schools, health centres,
hospitals and police stations.

Instructional materials are very important in the teaching/learning
process because they make teaching and learning real and enjoyable. They
reinforce learning and also attract learners’ attention and motivation.

Instructional materials are clear, bold, representative, attractive and can
make teaching and learning effective. Learners must be involved in the
making or collecting of instructional materials. As you select instructional
materials, you are encouraged to consider the special needs learners as
well.

Assessment
Assessment of learning is a very important aspect of the teaching/learning
process. You should assess the learner’s progress in terms of attainment
of the set competences. The syllabus also suggests competences to be
assessed at the end of every topic. However, summative assessment
should be carried out at the end of a specified period.

Primary Seven Curriculum

The three domains, cognitive, psychomotor and affective, should be
</passage>

<passage id="lchk_d2861670341541fc82e4b0a679a47bf0" source="NCDC PRIMARY SEVEN SET ONE – Social Studies" part="15">
• gives reasons why foreigners came to Africa.
• mentions groups of foreigners who came into Africa.
• names European countries that colonised Africa.
• draws the map of Africa showing sphere of influence.
• discusses problems faced by explorers.
• identifies the effects of European explorers.
• explains the causes of the Great Trek.
• discusses the effects of the Great Trek.
• discuses methods used by colonialists to acquire colonies.
• describes the methods used by colonialists to administer colonies.

Topic 7: Nationalism and the Road to
Independence of Africa
20 Periods

Background
In the previous topic, the learner was introduced to how foreigners came
to Africa, reasons for their coming, how they introduced colonial rule
and how the people reacted to colonial rule. They also learnt about how
the people of Uganda, Tanzania, Rwanda and Burundi and Kenya got
independence. In this topic, bring out the meaning of the terms “Pan-
Africanism” and “nationalism”.

Pan-Africanism is a feeling of uniting and promoting political, economic
and social interests of Africa. Nationalism is a deep love and pride for
one’s country. These movements spearheaded the struggle for Africa’s
independence.

Learning Outcomes
The learner demonstrates knowledge and appreciates the rights of an
individual, society and collective responsibility in bringing social justice,
and political order.

Life Skills
• Effective communication
• Self-awareness
• Self-esteem
• Assertiveness
SST Skills
• Reading
• Writing
• Analysing

Primary Seven Curriculum

Values
• Cooperation
• Love
• Respect
• Appreciation
Subject | Language | Content | Suggested
Competences | Competences | Activities
The learner: | The learner | • Meaning of pan- | • Discussing the
• discusses pan- | correctly uses the | Africanism, pan | meaning of
Africanism and | following words | – Africanists, | pan-Africanist,
nationalism. | related to the | nationalism, | nationalist,
• explains the | topic: | nationalists, | patriotism and
work of pan- | – nationalism | patriotism | nationalism.
Africanisists | – pan- | • The work of pan- | • Debating the
and nationalists. | Africanism | Africanists and | work of pan-
• identifies | – patriotism | nationalists | Africanists and
countries | – independence | • African countries that | why nationalists
that were not | – freedom | were not colonised: | succeeded
colonised in | – detention | Ethiopia and Liberia | in their
Africa. | • Reasons for | movements
• discusses | maintaining their | • Discussing
the reasons | independence | problems pan-
why Ethiopia | Africanists and
and Liberia | nationalists met
maintained | in their struggle
their
• Discussing
independence.
reasons why
Ethiopia and
Liberia were not
colonised
• discusses | The learner |  Reasons for | • Stating reasons
reasons why | correctly uses the | independence such | why Africans
Africans | following words | as to: | wanted
wanted | related to the | – control of national | independence
independence. | topic: | resources
– discrimination | – revive African | • Drawing a
– resources | culture/ | map of Africa
– oppression | independence | showing African
– equality | – stop exploitation by | independent
– dignity | former colonial rulers | countries and
– freedom | – regain land from | their former
European settlers | colonial masters

National Curriculum Development Centre

Subject | Language | Content | Suggested
Competences | Competences | Activities
– stop oppression
– desire for social
</passage>

<passage id="lchk_7b75c9e4203840aea59fb098eb0e285f" source="NCDC PRIMARY SEVEN SET ONE – Social Studies" part="16">
freedom and their
rights
– regain African
dignity and self-
respect
– ensure human
equality
– end racial
discrimination
• identifies key | The learner | • Leading | • Mentioning key
personalities | correctly uses the | personalities who | personalities
who fought | following words | fought for Africa’s | who fought
for Africa’s | related to the | independence: | for Africa’s
independence. | topic: | – Marcus Garvey – | independence
• identifies | – pan-Africanist | Jamaica | • Explaining the
the leading | – nationalist | – William Du Bois – | methods they
nationalists | – ideology | America | used to attain
who fought for | – law | – Booker T. | independence
independence. | – imprisonment | Washington –
• discusses | – trade union | America
the methods | – Henry Sylvester
used to gain | Williams – Trinidad
independence. | – J.E.K. Aggrey – | • Listing leading
• identifies the | Ghana | nationalists
problems | – Leopold Senghor – | in Africa who
encountered | Senegal | fought for
on the road to | – Kwame Nkrumah - | independence in
independence. | Ghana | their countries
– Edward Blyden –
Liberia
• Leading nationalists
who fought for
independence of their
countries examples
– Kwame Nkrumah -
Ghana
– N’Amdi Azikiwe –
Nigeria
– Hastings Kamuzu
Banda –Malawi
– Nelson Mandela -
South Africa

Primary Seven Curriculum

Subject | Language | Content | Suggested
Competences | Competences | Activities
– Patrice Lumumba –
Zaire (Democratic
Republic of Congo)
– Abdul Nasser –
Egypt
– Samora Machel –
Mozambique
– Haile Selassie -
Ethiopia
 Methods use by pan-
Africanists in their
struggle
- Meetings/
conferences
- Media

• Discussing
the methods
used to gain
independence
 Methods used by the • Discussing
nationalists in their  the problems
struggle: | faced by pan-
– Formation of trade | Africanists and
unions | nationalists
– Formation of political during their
parties | struggle for
– Formation of | independence
nationalistic
associations
– Armed struggle
 Problems pan-
Africanists faced:
– Lack of unity among
the Africans leaders
– Lack of enough funds
– Differences in
political ideologies

National Curriculum Development Centre

Subject | Language | Content | Suggested
Competences | Competences | Activities
 Problems nationalists
faced
- Death | • Explaining
- Imprisonment | the problems
- Harsh rules/laws | encountered in
- Loss of property | the struggle for
- Intimidation | independence
- Oppression
- Detention
Subject | Language | Content | Suggested
Competences | Competences | Activities
• discusses the | The learner | • Advantages of a | • Discussing the
advantages and | correctly uses the | multiparty system | advantages
disadvantages | following words | such as: | of multiparty
of multiparty | related to the | – there is room to | systems
and single party | topic: | choose better leaders
systems of | – there is respect of
government. | – political party | fundamental human
– multiparty | rights
– single party | – there is respect for
– human rights | hierarchy
– delegation | – there is delegation of
– hierarchy | power
– leadership | – checks and controls
– corruption | • Discussing the
leadership | disadvantages
– injustice | – government organs
– petition | of multiparty
are positively | system of
– rigging | developed
– dictatorship | governance
• Disadvantages of a | • Discussing how
– election | multiparty system
– accountability | democracy is
such as: | practiced in
– cause confusion, | their school
</passage>

<passage id="lchk_43fbd13f2d104b4eafa4f0fd7699e826" source="ALL SST NOTES P.4 TO P.7 ALL TERMS EXCEL 3" part="3">
Voluntary leaders …………………………………………………………………………………… .140
Cultural leaders ……………………………………………………………………………………… 142
How leaders are chosen in our dist rict ………………………………………………………… .143
Qualities of a good leader ………………………………………………………………………… ..143
Elections ……………………………………………………………………………………………… ..143
Rights and responsibilities of people in our district …………………………………………. 146
Citizenship …………………………………………………………………………………………….. 149
Topic 5. How to meet people’s needs in the district .
Introduction to social services ………………………………………….………………………… .151
Education service…………………………………………………………………………………… ..151
Health service ………………………………………………………………………………………… 154
Transport service …………………………………………………………………………………… ..155
Communication service …………………………………………………………………………… ..165
Secur ity service ……………………………………………………………………………………… .173
Banking service ……………………………………………………………………………………… .178
Housing service ……………………………………………………………………………………… .181
Electricity service ……………………………………………………………………………………. .182
Water supply service ………………………………………………………………………………… 183
Problems faced in meeting people’s needs ……………………………………………………… 184
Social service centres ………………………………………………………………………………. .185
Social service providers …………………………………………………………………………… ..186
Caring for social service centres ………………………………………………………………… ..186
Page 6
TOPIC 1: LOCATION OF OUR DISTRICT IN UGANDA.
MAPS AND PICTURES.
A map is a drawing/ representation of an object as seen from above.
Maps show how objects look like when viewed directly from above.
We use symbols to help us understand and interpret a map of a detailed area.
The boundary of a map determines the size and shape of the map.
A picture is a representation of an object drawn as seen from aside.
All features on a picture can be clearly seen as real objects.
Pictures are more detailed than maps.
Maps and Pictures of different objects
Object name Picture Map
a tree
a plate
a pot
a house
a chair
a cup
a hut
Page 7
a car
a table
Similarity between maps and pictures.
❖ Both are representations of objects.
Difference between a picture and a map.
❖ A picture is drawn as seen from aside while a map is drawn as seen from above.
❖ A picture is more detailed than a map.
Testing Exercise.
1. Give the meaning of each of the following;
(i) A picture
(ii) A map
2. Give one way a map is similar to a picture.
3. Why is it easier for one to understand a picture of an object than its map?
4. How is a map different from a picture?
5. Draw the maps of the following objects.
a cup a circular table a pot a tree
ELEMENTS OF A MAP.
▪ A key
▪ A scale
▪ A heading/ title
▪ A compass direction
▪ A frame.
Importance of different elements of a map.
Element Importance
❖ A compass direction ❖ It helps to show the direction of places on a map
❖ A title/ heading ❖ It helps one to know what the map is all about.
❖ A key ❖ It helps a map reader to interpret symbols used on a
map.
❖ A scale ❖ It helps a map reader to calculate the actual ground
distance on a map.
❖ A frame ❖ It shows the extent of the area represented by the
map.
Page 8
Problems a map reader may face when reading a map without the map elements.
Element missing Challenge a map reader is likely to face
▪ Without a compass
direction • Failure to know the direction of places on a map
▪ Without a title/
heading • Failure to know what the map is all about.
▪ Without a key • Failure to interpret symbols used on a map.
▪ Without a scale • Failure to calculate the actual ground distance on a map.
</passage>

<passage id="lchk_37a4c60f0274410483d4443cbc745314" source="ALL SST Notes P 4 TO P 7 ALL Terms Excel Copy" part="69">
7. Apart from the chairperson, mention any three other members on the LC I executive
committee.
8. State any three problems district leaders face when carrying out their duties.
9. Mention any three roles played by the LC I council in the village.
10. What title is given to the head of the municipality?
11. State any one role played by the district speaker.
12. Match the information in list A with that given in list B correctly.
List A List B
(i) Chairperson LC III Political head of a city
(ii) RDC Records minutes during LCI council meeting.
(iii) Lord mayor Political head of a sub-county.
(iv) General secretary Chairs security meetings in the district.
13. Who is the president’s representative in the district?
14. How is the Secretary for defense useful on the Local council I committee?
15. State any three roles played by the Resident District Commissioner (RDC) in the
district.
CIVIC LEADERS
These are leaders who provide social services to people
They become leaders through appointment.
Examples of civic leaders.
❖ District Internal Security Officer (DISO)
➢ He/she is responsible for spying in the district
➢ He/she is responsible for internal security in the district
❖ External Security Organisation (ESO)
➢ He spies for the country from outside the borders of the country.
❖ Internal Security Organisation (ISO)
➢ He/she is responsible for spying with in the country.
❖ Chief Administrative Officer (CAO)
➢ He/she is the highest civil servant in the district
</passage>

<passage id="lchk_0c56539c89484eec86f795bd3b158bd7" source="Act No 1 Of 2021 Uneb1136" part="12">
Cross references
The 1995 Constitution of the Republic of Uganda
National Audit Act, 2008
Public Finance and Management Act, 2015
</passage>

<passage id="lchk_a6654d7ed3fb4ebfa3aa6f04a2666943" source="P.7 PLE UNIQUE SET SST 1" part="14">
to kill him.
c) Name any two caliphs of Prophet Muhammad.
 Abu Bakr (reigned 632–634)
 Umar (reigned 634–644)
 Uthman (reigned 644–656)
 Ali (reigned 656–661)
54. EITHER:
a) What is success?
 Success is the achievement of one’s desired goals
b) Give any one factor that can make a Christian to become
successful in life.
 Hardworking
 Being disciplined
 Helping others
 Using time properly
 Making plan
 Praying all time
 Fasting
 God fearing
 Respect for other
 Determination
 Friendship
 Faith
 Good decision making
 Peer support
 Education
 Positive mental attitude
 Seeking guidance and counseling
 Good family background
39
c) Give any two causes of failure in life of a Christian.
 Fear
 Laziness
 Disunity
 Lack of faith
 Selfishness
 Indiscipline
 Lack of confidence
 Lack of education
 Poor planning
 Poor family background
 Disrespecting others
55. EITHER:
Jesus said to them, “Come with me and I teach you to catch people.”
(Matthew: 4:19)
a) Name the two people who Jesus told the above words.
 Simon Peter  Andrew
b) What activity was being done by the two people by the time
Jesus called them?
 Fishing
c) What did Jesus mean by, “I teach you to catch people”
according to the quotation above?
 To preach the gospel
 To bring people to the kingdom of God
OR:
When the hypocrites come to you, they say, “We bear witness that you
are indeed the messenger of Allah” Allah knows that you are indeed His
messenger and Allah witness that the hypocrites are liars indeed.
(Chapter 63 Verse 1)
c) Give any two ways in which hypocrites behave according to
Islamic teachings.
 Whenever they speak, they tell lies.
 Whenever he promises, he always breaks the promise.
 If you trust him, he proves to be dishonest.
d) State any two lessons Muslims learn from the above Surah.
 To tell the truth.
 To be trustworthy.
 To be honest.
 To be faithful.
 Not to trust everyone you meet. END.
40
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
