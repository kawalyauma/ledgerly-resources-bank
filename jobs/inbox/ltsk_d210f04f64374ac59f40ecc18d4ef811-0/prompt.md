# Job ltsk_d210f04f64374ac59f40ecc18d4ef811-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for Christian Religious Education, Primary Four 2026, Term 3.
The term has 10 teaching weeks and this subject has 3 periods per week. Every lesson is ONE 40-minute period, so keep each lesson small enough to teach in 40 minutes.
Ledgerly reserves the last lesson of each week for a review of that week.
Give at most 20 teaching/practice lesson entries in teaching order (the last lesson of the term is the end of term assessment).
Each lesson has a kind: "teach" (new content) or "practice" (the same subtopic as the teaching lesson just before it: exercises, oral work, drawing, matching, filling in blanks, ALL taken from the passages).
When the material is thin (common in lower primary), follow each teaching lesson with a practice lesson. Split big subtopics over several teaching lessons.
Never pad with content the passages do not have: if they cannot fill the term, return fewer lessons and list what is missing in gaps. Ledgerly fills the remaining weeks with revision.
You are composing the SCHOOL'S OWN scheme. The passages below (the official NCDC curriculum and guides, plus schemes of work, lesson plans, notes and past papers from the school e-library) are reference material:
The NCDC documents (titles starting "NCDC") are the BASE: their topics, competences and order for this class and term are what the scheme must cover. NCDC lower-primary thematic curricula list every learning area side by side in table columns separated by " | ": take only the Christian Religious Education column.
Every topic the NCDC curriculum lists for this class and term MUST become a unit, in the NCDC order. Share the weeks between ALL of them according to their NCDC periods, competences, content and subtopics. Large topics should receive more lessons than small topics.
combine them in this authority order: curriculum for required coverage; all relevant schemes for sequence and pacing; the strongest detailed notes for accurate teaching depth; past papers for expected applications and activities. Do not copy one reference scheme blindly.
Use this term's part of the material (Term 3) when the passages cover several terms.
Theme-only references (P 4 R E Scheme Term III): general thematic schemes covering every learning area. Use them ONLY for the term's theme name and week order; ignore their content for other learning areas (reading, spelling, drawing, literacy, songs). Every lesson must be Christian Religious Education content.

Do NOT write lesson content yet. Each unit and lesson must cite the passage ids it comes from in sourcePassageIds.

Reply shape:
{"title":string,"summary":string,"units":[{"title":string,"theme":string|null,"weekFrom":int|null,"weekTo":int|null,"competences":string|null,"sourcePassageIds":[string],"lessons":[{"title":string,"subtopic":string|null,"kind":"teach"|"practice","objectives":[string],"sourcePassageIds":[string]}]}],"gaps":[string]}

<passages>
<passage id="lchk_b730228824d64941842793fd8df2914e" source="P4 IRE" part="1">
P
R
I
M
A
R
Y
4
A u g u s t 2 0 2 0
Ministry of Education
and Sports
HOME-STUDY
Published 2020
This material has been developed as a home-study intervention for schools during the
lockdown caused by the COVID-19 pandemic to support continuity of learning.
Therefore, this material is restricted from being reproduced for any commercial gains.
National Curriculum Development Centre
P.O. Box 7002,
Kampala- Uganda
www.ncdc. g o.ug
FOREWORD
Following the Outbreak of the CoVID-19 Pandemic, Government of Uganda
closed all schools and other educational institutions to minimize the spread
of the coronavirus. This has affected more than 36,314 primary schools, 3129
secondary schools, 430,778 teachers and 12,777,390 learners.
The COVID-19 outbreak and subsequent closure of all has had drastically
impacted on learning especially curriculum coverage, loss of interest in education
and learner readiness in case schools open. This could result in massive rates of
learner dropouts due to unwanted pregnancies and lack of school fees among
others.
To mitigate the impact of the pandemic on the education system in Uganda, the
Ministry of Education and Sports (MoES) constituted a Sector Response Taskforce
(SRT) to strengthen the sector’s preparedness and response measures. The SRT
and National Curriculum Development Centre developed print Home- Study
Materials, radio and television scripts for some selected subjects for all learners
from Pre-Primary to Advanced level. The materials will enhance continued
learning and learning for progression during this period of the lockdown, and will
still be relevant when schools resume.
The materials focused on critical competences in all subjects in the curricula to
enable the learners to achieve without the teachers’ guidance. Therefore effort
should be made for all learners to access and use these materials during the
lockdown. Similarly, teachers are advised to get these materials in order to plan
appropriately for further learning when schools resume, while parents/guardians
need to ensure that their children access copies of these materials and use them
appropriately.
I recognise the effort of National Curriculum Development Centre in responding
to this emergency through appropriate guidance and the timely development of
these home study materials. I recommend them for use by all learners during the
lockdown.
Alex Kakooza
Permanent Secretary
Ministry of EDUCATION AND SPORTS
ACKNOWLEDGEMENTS
National Curriculum Development Centre (NCDC) would like to express its
appreciation to all those who worked tirelessly towards the production of
home–study materials for Pre-Primary, Primary and Secondary Levels of
Education during the COVID-19 lockdown in Uganda.
The Centre appreciates the contribution from all those who guided
the development of these materials to make sure they are of quality;
Development partners - SESIL, Save the Children and UNICEF; all the
Panel members of the various subjects; sister institutions - UNEB and DES
for their valuable contributions.
NCDC takes the responsibility for any shortcomings that might be
The comments and suggestions may be communicated to NCDC through
P.O. Box 7002 Kampala or email admin@ncdc.go.ug or by visiting our
website at http://ncdc.go.ug/node/13.
Grace K. Baguma
Director,
National Curriculum Development Centre
ABOUT THIS BOOKLET
Dear learner, welcome to this home-study material which has been
prepared for you. The material covers content for term 1, II and
III.
</passage>

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

<passage id="lchk_7909450e802b4d1abfe19884cbbe0a0d" source="P4 IRE" part="15">
i. Cleanliness is one of the conditions for prayer to be accepted by Allah.
(…………………)
ii. Dirtiness is a good practice.(…………………)
iii. Allah does not accept Swadaqah from stolen things.(…………………)
iv. Theft is good in Islam.(…………………)
Activity:
1. With your friend demonstrate to your parent how ablution is performed.
National Curriculum
Development Centre,
P.O. Box 7002,
Kampala.
www.ncdc.go.ug
</passage>

<passage id="lchk_512fa51e25c14ad1b7a1e0998f162db1" source="P 4 R E Scheme Term III" part="3">
Guided
discussion
Question and
answer
Dramatization
Listing
problems
faced by
Israelites
during
Exodus
Problem
solving
Creative
thinking
Critical
thinking
Self
awareness
Audio
visual aid
of Moses
and Aaron
God and us book 4 page 146
5 1
Peace
Gods promised peace
The learner;
Mentions signs of peace God
promised
Discusses the birth of Jesus prince of
peace
Discusses Simeon’s message towards
the birth of Jesus
The learners
Pronounces and spells new
words e.g. Bethlehem,
Kraal, Simeon, forbidden
Signs of peace God
promised
Birth of Jesus prince
of peace
Simeon’s message
Brain
storming
Guided
discussion
Dramatizing
Discussing
the birth of
Jesus Christ
Self
awareness
Problem
solving
Chalkboard
illustrations
Chart
showing
the family
life of
Jesus
God and us book 4 page 150
</passage>

<passage id="lchk_c32feb9dafbd4e66afc10350032c1887" source="All P 4 To P 7 Religious Education Notes All Terms Copy" part="65">
(d) Holy communion - is the sacrament through which we receive the blood and body of Christ.
Makes Christians soldiers of Christ.
QN: What does bread and wine represent during the Holy Communion?
(i) Bread - the body of Christ
(ii) Wine - the blood of Christ
(e) Penance - the sacrament through which we confess and repent to God.
(f) Holy ordination - the sacrament through which a Christian receives priestship.
1
RELIGIOUS EDUCATION LESSON NOTES FOR UPPER PRIMARY (P.4 – P.7)
CREATION
Order of God’s creation
1 st day: light
2 nd day: sky
3 rd day: vegetation
4 th day: sun, moon and stars
5 th day: animals
6 th day: man (Adam)
NOTE: The universe had already been made even before creation began. (Gen 1: 1-2)
Guiding questions about creation.
1- Name the place where Adam and Eve were made to live.
2- What did God make as a summit of his creation.
3- How was Adam special from other creatures?
4- Why did God create man last?
5- Why did God make Sabbath a day of resting?
6- How did man break off his relationship with God?
7- How did God complete his plan of salvation?
8- Which creature is blamed for the fall of man?
9- Give the meaning of Genesis and exodus.
10- Why did God create Eve?
God’s punishments to Adam and Eve.
- They were sent out of the Garden of Eden.
- Man was to sweat for al that to eat.
- Woman was to undergo a lot of labour pains.
- The snake had to bite man.
- They had to die
The creature blamed for the fall of man was the snake / serpent / Satan / devil.
Consequences / results of sin in the world.
• suffering • hatred • worries
2
• envy
• misery
• jealousy
• unhappiness
• wars
• death
• fear etc
God completed his plan of salvation by sending his only son Jesus Christ to come and die for
mankind.
The son of Adam who killed the brother was Cain.
Possible causes of Abel’s murder by Cain.
• Envy
• jealousy
• hatred
• dislike
• intrigue etc
God punished a murderer by becoming a wonderer / homeless he was cursed.
Other bad things happening in our communities.
❖ robbery
❖ thuggery
❖ killing others
❖ Sex abuse i.e rape, defilement, abortion, prostitution etc.
❖ kidnapping
❖ abduction
❖ Homo sexuality. etc.
Things that can be done for the good of the community.
➢ Take part in self help projects.
➢ Help those in need.
➢ Respect elders as well as young ones.
➢ Forgive those who wrong us.
➢ be obedient to community members
➢ Do voluntary work.
➢ Keep law and order.
How I can show love to my fellow pupils.
✓ By forgiving them.
✓ By respecting them.
✓ By sharing with them.
✓ By helping them.
✓ By obeying them.
✓ By advising them.
✓ By associating with them.
Guiding questions:
3
1- What was the symbol of God’s covenant with Noah?
2- Give the meaning of these names (i) Abraham (ii) Sarah
3- Which covenant did God make with Abraham?
4- Which responsibility did God give Noah?
5- Why did God give that responsibility to Noah?
6- Why did God ask Abraham to sacrifice his son Isaac?
7- Name the two sons of Isaac and his wife Rebecca.
8- Which son of Isaac is said to be the founder of Israel?
9- Name two of the twelve sons of Jacob.
10- Which son was sold to Egypt by his brothers?
THE EXODUS
Exodus was the movement of the Israelites from slavery in Egypt to the Promised Land.
(Canaan)
God called Moses on mountain Sinai in order to send him to Egypt to rescue the Israelites
from slavery.
Moses asked for a helper because he was not a good speaker (stamerer)
Moses led the Jews across Red sea. Joshua succeeded Moses and led the Jews across the
</passage>

<passage id="lchk_a0d15756a3524e7faf3e5317149d5de5" source="Lower I R E Notes" part="1">
ISLAMIC RELIGIOUE EDUCATION
(IRE)
PRIMARY LEVEL
BY
CREATIVE PRINTERS
0703745068/0785681207
1
ISLAM Lesson Notes
Islam
This is the total submission to the will of Allah.
Islam is obedience to commands of Allah.
Symbols of Islam
i. Qu’ran / Koran
ii. The Crescent
iii. The Mosque
iv. The Qaladi
Pillars in Islam
There are two types of pillars in Islam.
1. Pillars of Ibadat (worship)
2. Pillars of Iman (faith)
1. Pillars is Ibadat
The term Ibadat means
Worship .
Worship is to perform an act of honour of Allah.
There are three types of Ibadah (worship)
i. Worship made by saying words e.g saying good words to others , greeting others ,
etc.
ii. Worship made by doing something e.g praying, assisting a person with physical
needs, fasting, performing Ablution, etc
iii. Worship made by a person in one’s heart e.g to love Allah, to love prophet
Mohammed, to love one’s parents.
Pillars of Islam/Ibadat
i. To believe in Allah and that Prophet Muhammad is his messenger ( Shahaddah).
ii. Praying five times a day. (Salat / Swallah)
iii. Alms giving / paying Zakat.
iv. Fasting in the Holy Month of Ramadhan (Saum).
v. Making a Holy Journey to Mecca (Hijja / Hajj).
The Holy journey is also called a
Pilgrimage.
2
2. Pillars of Iman
Iman in Islam means Faith.
Pillars of Iman
i. To believe in Allah and that Prophet Mohammed is his messenger (Shahadah).
ii. To believe in Allah’s Angels.
iii. To believe in Allah’s prophets.
iv. To believe in Allah’s Holy books.
v. To believe in the Day of Judgment.
vi. To believe in Allah’s Will / Final decision.
How one becomes a Muslim?
i. After reciting the Shahadah.
ii. A baby becomes a Muslim by:
(a). Reciting the Shahadah in its right ear.
(b). Through birth by Muslim parents.
Circumcision in Islam makes one clean or pure.
i. It also enables Muslims to follow the footsteps of prophet Ibrahim.
The Holy city in Islam is Mecca or Makkah.
Months of the Islamic calendar
i. Muharram
ii. Sufur
iii. Rabil-Awal
iv. Rabil-Akhiri ( Rabil Than)
v. Jamadal -Awal
vi. Jamadal-Akhiri (Jamadal Thaan)
vii. Rajab
viii. Shaban
ix. Ramadhan
x. Shawwal
xi. Dhul Qaadah
xii. Dhul Hijja
3
The Islamic calendar started in 622 AD, when prophet Muhammad migrates from Mecca to
Medina ( Yathrib) .
Medina became the first city of Islam.
Most important months of the Islamic Calendar
i. Rabai-Awal - Month when Prophet Muhammad was born.
- Month when Prophet Muhammad died.
ii. Ramadhan - It’s the ninth month on the Islamic Calendar.
- It’s the fasting month for Muslims.
- When the Qu’ran was revealed to PBUH.
iii. Shawaal - Idd-el-Fitr is celebrated on 1 st Shawaal.
iv. Dhul Hijja - Holy pilgrimage is conducted (Hijja)
- Idd-Adhuha is celebrated.
- Sacrificing of animals takes place.
v. Rajab - Isra and Miraj took place on the 27 th Rajab.
PROPHET MUHAMMAD (PBUH)
He was born in the month of Rabil-awal on 12 th , it was a Monday in 571 AD.
His father was Abdullah and the mother was Aminah.
He was born an orphan because his father dided before he was born.
At the age of six, he became a total orphan after the death of his mother.
After his birth, he was given away to an Arabic woman called Halimah who became his
foster mother.
Halimah was so important to him in the following ways:-
1. She breast fed him.
2. She taught him Arabic cultures.
Prophet Muhammad belonged to the Hashim clan and Quraish tribe.
Prophet Muhammad under the care of his grandfather.
His grandfather was Abu Muttalib.
He was the leader of the Hashim Clan.
</passage>

<passage id="lchk_6e3eb72efd854bd7bd7c1d830367e9d9" source="P 4 Comprehension Lesson Notes Term III" part="1">
1
GRAMMAR AND COMPREHENSION FOR P.4 TERM III
Expression of the future
Use of if or unless
If and unless are called conditional clauses because a certain condition is supposed or imagined to
be fulfilled in order for an action to take place.
We commonly use a future simple tense in the main clauses and the present simple tense in the if
clauses and the present simple tense in the if clauses ( If + PST + FT)
Examples
1. If I get money, I will buy a new radio.
2. If I get time, I will go to Nairobi.
3. If Juma comes, we shall go together.
4. If it rains, Tom will not come to school.
Exercise
Re-write these sentences using
( If : …………………..)
(…………….if …………..)
Use of unless
( will …… will not)
Examples
If it shines, the crops will dry.
Unless it shines, the crop won’t dry.
Unless you first show me the book, I will not pay you
Exercise
Use of Hope ……….will …………
Hope is followed by a verb in the future tense when we use hope, it means there are chances of the
action of the verb to happen.
Hope is used with a future simple (present) using will or shall.
Examples
I hope I will arrive at school early morning.
Exercise
Detailed book 2 page 72.
Looking forward to …………
2
Examples
1. We shall do our P.L.E in November.
2. We are looking forward to doing or P.L.E in November.
3. Ntambi will visit his relatives next month.
4. Ntambi is looking forward to visiting his relatives next month.
Exercise
Using since and far
Since
Since is used when a point f time fun which an action began is given (starting point of time)
The present perfect tense is always used when an action is still existing
Examples
1. They have played netball since morning
2. I have not seen her since last week.
3. Joseph has not eaten anything since last night.
Exercise
Mk. Precise English Grammar for upper page 125
For
For is always used when the length of time an action has spent or spent in existence is indicated
(duration)
Examples
1. They have played for two hours
2. I have not seen him for three days
3. Joseph has not eaten for eight hours
Exercise
MK. Precise English Grammar for upper page 125 task 35.
Compound Nouns
A compound noun is made up of more than one word
Examples
3
 brother – in – law
 guest – of honour
 head – of – state
 mother – in – law
 commander – in – law
 bye – law
 passer – by
 foot – path
 side path
 a pair of scissors
 mater – on – duty
 x – ray
 spoonfuls
 step – son
 mouse – trap
 girl – guide
 cob – plant
 egg – plant
 post – office
 head – of department
Date Class Subject No. of pupils Time
P.4 Grammar
TOPIC: Conjunctions
SUB – TOPIC: Using conjunctions in sentences
SKILLS: Listening, Speaking, Reading, Writing
Using: “Neither …nor”
“Neither ...nor “ are used with negative sentences. They are used to replace “not”
When the clauses to be joined have two subjects, neither is put at the beginning. And if only one
subject, we use “neither” in the middle.
Examples
4
1. Peter will not bring my books. James will not bring my books.
Neither Peter nor James will bring my books.
2. I shall not drink safi. My brother will not drink safi.
Neither my brother no I shall drink safi.
3. Ali doesn’t eat meat daily. Ali doesn’t eat fish daily.
Ali neither eats meat nor fish daily.
Exercise
Join the following sentence using “neither”
1. Mary will not marry Alex. Annet will not marry Alex.
2. The pupils didn’t eat posho. The pupils didn’t eat beans.
3. The lady was not bought a dress. The lady has not bought blouse.
</passage>

<passage id="lchk_da2a32cf3b084a5fabeebdf9c15b9b42" source="P 4 R E Notes Tem Iii" part="4">
i) By offering sacrifices.
ii) Through the use of arbitrators.
iii) By paying fines.
iv) By sharing eats and drinks.
CHRISTIAN WAYS OF PROMOTING RECONCILIATION
i) By involving other people to settle the cases.
ii) By asking for forgiveness.
iii) By fasting.
iv) By paying fines.
HOW JESUS RECONCILED MANKIND WITH GOD
He died on the cross for our sins.
How is good communication important in peace keeping? (Gen. 45:1-25)
Enables one to ask for forgiveness
THINGS THAT GOD PROMISED US IF WE LIVE ACCORDING TO HIS COMMANDMENTS
-To make us live safely in our land.
-To give us peace in our land
-Make us prosperous.
Activity:
1. Define the term reconciliation.
……………………………………………………………………………………..
2. Mention any two importances of reconciliation.
i)…………………………………….
ii)……………………………………
3.List any two promises God made to people if they lived according to his commandments.
i)…………………………………………………………………
ii)……………………………………………………………...
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

<passage id="lchk_82338bd42ca14803a283a044275dc225" source="Kesk P4 RE Workbook" part="1">
Standard Kolfram in Use; Abridged Curriculum P4 Christian Religious Education Workbook
A product of Kolfram Educational Services Kampala 0777886622/ 0784044408/ 0756821512/0786941943 1
For the best and improved academic performance, always use Kolfram Educational Service products
Standard Kolfram in Use; Abridged Curriculum P4 Christian Religious Education Workbook
A product of Kolfram Educational Services Kampala 0777886622/ 0784044408/ 0756821512/0786941943 2
For the best and improved academic performance, always use Kolfram Educational Service products
FOREWORD AND RECOMMENDATION
COVID 19 pandemic caused a disruption in our education system and made learners missed
schooling for two years of 2020 to 2021 schooling period. This has created a need to rethink
what and how learners will be taught when schools open.
The Kolfram Educational Services Kampala has developed a series of teaching
materials for pre-primary, primary and secondary schools in Uganda. These materials are
prepared in accordance to the abridged curriculums right from primary two up to senior six.
“ Special thanks go to the board of directors, managers and staff of Kolfram
Educational Services Kampala for the great work done .’’
Congratulations
This material presents a selection of priority learning competences and concepts, along with
psychological support, which should be focus of instruction in the 2022 school year in order
to achieve learning recovery.
This material is not a departure from the existing old curricula for this level but is a
modification of the same with a purpose of recovering the lost learning time with maximum
learning loss. They have been packed for all primary and secondary classes in Uganda
including pre- primary , primary one , senior one and senior five that are still using the
old standard curriculums.
I therefore, recommend this material and ask all stake holders, educational fraternity to
support its implementation as a strategic intervention towards the mitigation of the effects of
COVID 19 pandemic on the education system. The effective implementation of this material
by the implementers will be a great milestone towards the recovery of lost learning time and
giving hope and confidence to learners and teachers.
HON. Janet K. Museveni
First Lady and Minister for Education and Sports
Standard Kolfram in Use; Abridged Curriculum P4 Christian Religious Education Workbook
A product of Kolfram Educational Services Kampala 0777886622/ 0784044408/ 0756821512/0786941943 3
For the best and improved academic performance, always use Kolfram Educational Service products
ACKNOWLEDGEMENT
• I’m very grateful to the Almighty God the Most High who enabled us to accomplish the
mission and publish this book.
• Similarly, we wish to express and convey our gratitude to all those who contributed to
the production and reproduction of this book, materially, spiritually and professionally.
Thank you very much.
• Lastly we do sincerely regret any error, mistakes or incorrect writing in a paragraph
which may be found in this book; it could have cropped up unknowingly.
• All rights to photocopy, print, reproduce or duplicate this material found herein are
strictly reserved.
Special thanks to:
1. Mr. Makumbi Diriisa Wasswa,(headteacher Kitagobwa UMEA primary school- Butambala)
2. Mr. Okol Charles (Head teacher Acuta Primary School- Oyam)
3. Mr. Ggoobi Ramathan ( Permanent Secretary , Ministry of Finance)
</passage>

<passage id="lchk_7086752e78844cd2b356c8a499198a7d" source="Kesk P4 RE Workbook 1" part="61">
7. Conflicting members are asked to forgive one another.
8. Sharing meal to celebrate new relationship.
Christian ways of reconciling with God
1. Believing in Jesus Christ.
2. Accepting Jesus as a personal saviour.
3. Repenting for our sins.
4. Asking for forgiveness
5. Christian ways of reconciling with one another.
6. Apologizing/asking for forgiveness.
7. Using gifts.
8. Visiting each other.
9. Using mediators
10. ACTIVITY
1. State any two traditional ways of reconciliation.
i)_______________________________________________________________________________
ii) ______________________________________________________________________________
2. Mention any one traditional way of reconciling with God.
_________________________________________________________________________
_________________________________________________________________________
3. State any two process involved in traditional reconciliation.
i)_______________________________________________________________________________
ii) ______________________________________________________________________________
4. Write any two Christian ways of reconciling with God.
i)_______________________________________________________________________________
ii) ______________________________________________________________________________
STANDARD KOLFRAM IN USE: ABRIDGED CURRICULUM P.4 CHRISTIAN RELIGIOUS EDUCATION WORKBOOK
A product of Kolfram Educational Services Kampala 0777886622/ 0786941943/ 0756821512/ 0784044408 84
For quality and improved learning materials, always use Kolfram Educational Services products
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
