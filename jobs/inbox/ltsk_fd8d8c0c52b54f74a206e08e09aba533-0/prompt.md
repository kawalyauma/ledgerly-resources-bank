# Job ltsk_fd8d8c0c52b54f74a206e08e09aba533-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for Islamic Religious Education, Primary Six 2026, Term 3.
The term has 10 teaching weeks and this subject has 3 periods per week. Every lesson is ONE 40-minute period, so keep each lesson small enough to teach in 40 minutes.
Ledgerly reserves the last lesson of each week for a review of that week.
Give at most 20 teaching/practice lesson entries in teaching order (the last lesson of the term is the end of term assessment).
Each lesson has a kind: "teach" (new content) or "practice" (the same subtopic as the teaching lesson just before it: exercises, oral work, drawing, matching, filling in blanks, ALL taken from the passages).
When the material is thin (common in lower primary), follow each teaching lesson with a practice lesson. Split big subtopics over several teaching lessons.
Never pad with content the passages do not have: if they cannot fill the term, return fewer lessons and list what is missing in gaps. Ledgerly fills the remaining weeks with revision.
You are composing the SCHOOL'S OWN scheme. The passages below (the official NCDC curriculum and guides, plus schemes of work, lesson plans, notes and past papers from the school e-library) are reference material:
The school's SCHEMES OF WORK for this class and term ("P.6 R.E scheme term 3", "p.6 R.E Scheme term III 2019") are the BASE: follow the topics, subtopics and week-by-week order they agree on. Every topic they list for this term MUST become a unit, in their order, and their subtopics become the lessons, with about the pacing they give. Cite their passages in sourcePassageIds of every lesson that follows them.
The NCDC documents (titles starting "NCDC") only FILL GAPS: a topic NCDC lists for this term that the schemes lack gets its own unit where it fits best. Never drop or rename a schemes-of-work topic to fit NCDC. NCDC lower-primary thematic curricula list every learning area side by side in table columns separated by " | ": take only the Islamic Religious Education column.
Combine them in this authority order: the school's schemes of work for topics, sequence and pacing; NCDC for anything they miss; the strongest detailed notes for accurate teaching depth; past papers for expected applications and activities.
Use this term's part of the material (Term 3) when the passages cover several terms.

NCDC topics for Primary Six 2026, Term 3 that must ALSO be covered. Each needs at least one unit whose title or theme names it; the school's schemes of work decide where it goes and how many lessons it gets:
  9. Christian Involvement
  10. Happiness on the Way
Do NOT write lesson content yet. Each unit and lesson must cite the passage ids it comes from in sourcePassageIds.

Reply shape:
{"title":string,"summary":string,"units":[{"title":string,"theme":string|null,"weekFrom":int|null,"weekTo":int|null,"competences":string|null,"sourcePassageIds":[string],"lessons":[{"title":string,"subtopic":string|null,"kind":"teach"|"practice","objectives":[string],"sourcePassageIds":[string]}]}],"gaps":[string]}

<passages>
<passage id="lchk_f0f2f487715b434fa6ab5c94d63932cc" source="NCDC P6 Set One Sept book – Religious Education" part="1">
Religious Education Syllabus

Introduction to the Primary Six Religious
Education Syllabus

General Background

Rationale
One of the stated national aims of Education is to “inculcate moral,
ethical and spiritual integrity, tolerance and human fellowship”. It is
in fulfilment of this national broad aim that this Religious Education
Syllabus has been prepared. Religious Education forms an integral part
of the P6 Curriculum which has been designed to enable the learner to
develop ethically, morally and spiritually. This will bring out a balanced,
responsible and mature person to fit in the community.

Religious Education blends well with other subjects for example the
content of the music lesson may include religious songs, models and
pictures for RE lessons can be made during the CAPE3 lessons, a Science
lesson on hygiene will relate well with the Religious Education teaching
on hygiene in the P6 IRE Syllabus.

It is important to note that Religious Education is not meant to indoctrinate
learners but give them the knowledge needed to develop a whole person.
The teachers therefore have to teach objectively.

The Primary Six Religious Education Syllabus is composed of alternative
two parts:
i) | Christian Religious Education
ii) | Islamic Religious Education

It is up to the school to teach either Part I or Part II depending on their
religions population, the facilities available and the school foundation
bodies.

Part I: Christian Religious
Education

Background
This is the P6 Christian Religious Education (CRE) Syllabus. The syllabus
has one theme “Christians on the Way” for the whole year.

The P6 CRE Syllabus was mainly revised to provide learners with
knowledge, values, life skills and attitudes. The following topics will
help us to achieve the above:
• God Created Me
• Evil and Suffering
• God Calls His People
• Christ is the Answer
• Christ’s Gift for the Journey
• How to Behave on the Way
• People on the Way
• Friends on the Way
• Christian Involvement in the World
• Happiness on the Way to Arrival

There are some changes that have taken place in this new P6 Syllabus. It
is spirally arranged. Ideas and concepts that may have been covered in
the previous years and others repeated in the succeeding year have been
treated in greater depth and breadth or from a different view point.
i) | Language competences have been included in order to enforce
literacy skills and the teacher is expected to use English as a
medium of instruction. For that matter, the teacher must put
emphasis on giving a chance to children to practice spellings,
pronunciation, structure, etc of key words.

Primary 6 Curriculum

ii) | Specific objectives have been replaced by subject and language
competences which focus on knowledge, comprehension and
application.
iii) The general objectives for each topic have been replaced by the
learning outcome.
iv) A background to introduce each of the topic is provided and
gives an insight on how to handle each topic.
v) | Content on Child-labour, Adolescent Sexual and Reproductive
Health, Life Planning Skills, Voter Education and Animal
Welfare Education has been added by infusing in the relevant
topics existing in the syllabus.

Suggested Assessment Guidelines
Continuous assessment is the most recommended and should be based
on the suggested competences for each topic. In addition to continuous
assessment, you are supposed to carry out end of term and end of year
assessments.

General Methodology
</passage>

<passage id="lchk_577ecd092626472c9c45af1d422a6a74" source="NCDC P6 Set One Sept book – Religious Education" part="2">
You are advised to use child-centred methods which put the learner at
the centre of the teaching/learning process. Some of the methods are
suggested in the suggested activities for each topic that will help learners
exhibit the suggested competences.

General Learning Outcomes
The learner;
• | discovers his strengths and weaknesses, develops responsible
behaviour as a youth and displays a positive attitude to working
alone and with others using the God-given talents.
• discovers the true meaning of evil and suffering and develops
the ability to accept and cope with suffering.

National Curriculum Development Center

• explores how God revealed His promise of a redeemer through
various messengers and develops an appreciation of God’s
messenger and messages.
• explores the importance of repentance and forgiveness and
discovers the need for a good relationship between themselves
and Jesus Christ.
• explores and develops a deep understanding of the sacraments
of baptism and Holy Communion and develops the confidence
that in all they do God never forsakes them.
• develops appreciation for consideration, love for others, and
promote unity, co-operation, justice and responsibility in
society.
• appreciates interacting and living with the different groups of
people they meet in life.
• develops skills of forming and keeping true friendships and
acknowledges that friendship is a gift that should be cherished.
• explores events and circumstances where Christians have
contributed towards the development of the world and develop
skills that will enable them become better citizens.
• explores Christian beliefs that are the source of happiness, hope
and perseverance in his/her Christian journey in faith.

Guidance to the Teacher
• You should use relevant books of the old curriculum and any
other related material. You should, however, be mindful of the
novelties and modifications introduced in the syllabus which
may require new information.
• You should know that the key words that appear in the column
of language competences matrix represent the conceptual
framework in which the topic should fit, so due attention must
be paid to them.

Primary 6 Curriculum

• You are expected to relate the topic to daily life. As far as
possible, you should avoid using hypothetical examples which
normally begin with “suppose” or “imagine”.
• The methods you choose should contribute to the achievement
of competences, learning outcomes and eventually lead to the
achievements of aims and objectives of primary education.
They should be interactive in order to make the learning process
interesting.
• You should be gender sensitive, and mindful of learners with
special needs.
• You should not be the director of the learning process, instead
you should allow learners to make contributions at every stage
of lesson development and discussion.
• Take note of peculiar words, difficult terminology, words used
frequently, or misconceptions and stereotypes.

Topic Outline
No. of
Theme | Term | Topic | Sub-topics | Periods

Christians | I | 1. | Understanding and
on the | appreciating myself
Way | as a unique person
2. | How to relate
1. God
with others with
Created Me
consideration and | 7
respect
3. | Definition and value
of work

1. Suffering
2. Jesus’ example
of sharing in the
2. Evil and | suffering with others
Suffering | 3. How to share in the | 11
suffering of others
4. Our response to
suffering

1. Restoration of broken
relationships
2. Bible characters who
</passage>

<passage id="lchk_f783a4974c2e4f76b77225c60d3c7d51" source="NCDC P6 Set One Sept book – Religious Education" part="31">
• Let the learners say the effects of wars on society.
• Be mindful of the learners with special needs.
• Effects of religious wars:
– political parties
– Democratic Party (DP) for Catholics
– Uganda People’s Congress (UPC) for Protestants
– Kabaka Yekka (KY) for Protestants and Muslims
• Use a history book to get facts about religious wars and their
effects on society.
Suggested Competences for Assessment
• describes the role of Muteesa I in the spread of Islam.
• explains “The golden era of Islam”, Muteesa’s reign.
• gives the causes and effects of religious wars in Buganda.

Allocation of Periods
• Role of Muteesa I (2 periods)
• Golden age of Islam (2 periods)
• Causes of religion wars (2 periods)
• Effects of religions wars (2 periods)

Primary 6 Curriculum

Word List

Flights of birds, baked clay, invade, mischief,
transgressor, evil, Al-Hamdu Lillah, Inna Lillahi wa Inna
TERM I | ilaihi Raji’un, Qadha, Qadar, divine decree, pre-destination,
Zakah, Sadaqah, charity, settlement, migration, coast,
circumstances, century, courtier, Kabaka, Arab

Nature, natural laws, ordinance, Ayat Al-Kursi, Kufr, Shirk,
minor Shirk, Riya, needy, poor, wa-farer, heavily depted,
TERM II | cause of God, those whose hearts should be reconciled,
hygiene, faith, cleanliness, personal hygiene, public
hygiene, colonial policy, spread, impact

Al Kafirun, freedom of worship, compromise, reconciliation,
worship, Ibada, Bismillah, master, servant, Niyya, Nisaab,
TERM III | ratio, percentage, calculate, uprightness, adolescence,
elders, juniors, authority, loyalty, Muteesa I, role, spread,
religious wars, effects, causes.
</passage>

<passage id="lchk_62622d06b00c4698b1f540bbf5ba9278" source="P.6 R.E scheme term 3" part="1">
GENERAL TOPICS GENERAL COMPETENCES
SUBJECT : RELIGIOUS EDUCATION i) Friends on the way i) ……………………………………...
CLASS: PRIMARY SIX ii) Christian involvement in the world. ii) ………………………………………
TERM: THREE iii) Happiness on the way and travel iii) ………………………………………
YEAR: 2016 iv) …………………………………… iv) …………………………………...……
WK
PD
Theme
Topic
Sub-topic
Competence
Content
Method
L/Skills ind.
Activities
T/L AID
REF
REM
Subject
Language
1
1
&
2
Christians on the way
Friends on the way
Qualities of true friends
States qualities if true friendship learnt from Jesus Christ
Reads, spells and writes selflessness, humility , servant hood
The qualities of a true friend
Selfleness
Humility
Servant hood
Understanding
Forgiving
Respect
True love
Patience
Loyalty
Guided discovery
Role play
Discussion
Sharing
Love
Friendship
Stating qualities of a true friendship
Reading
Board
New prim six curri pg 226 – 233
Mk standard R.E pg 103 - 105
2
1
How to distinguish between good and bad advice
States qualities of a good advice
Spells promote , respect , true
Qualities of good pieces of advice.
Should be Godly
Should promote respect for others.
Should promote peace.
Guided discovery
Role play
Discussion
Brain storming
Effective communication
Sharing
Critical thinking
Spelling, reading and writing.
Sharing
Board
Mk standard R.E 106 – 110
New prim six curr pg 226 - 233
2
Importance of true friends
The value of true friends.
Encourages
Doesn’t give up
Shows true love
Stands in hard times with you.
3
1
&
2
Christians on the way
Friends on the way
The need to co-operate in order to make the world a better place.
States importance of working together.
Mentions ways of co-operation.
Spells, reads and writes
Co-operation , leadership, obedience, voluntary
Importance of working together.
Possible ways of co-operation
Through good leadership
Through concern for the welfare of our people.
Being open
Through obedience to God
Through working hard
Guided discovery
Brain storming
Discussion
Effective communication
Sharing
Love
Stating importance of working together
Mentioning ways of working together
Board
New prim.six curr.pg 226 – 223
Mk stand.R.E bk 6 pg 118 - 119
4
1
&
2
Christian organization in developing the world
Mentions voluntary organization
Describes the roles of the voluntary organization
Spells , reads and writes , relief , fund , compassion , agency , development
Christian voluntary organizations.
Christian children’s fund (CCF)
World Vision International
Adventists Development Relief Agency (ADRA)
Compassion international
Mothers Union
YWCA
Catholic Women’s Guild
Scripture Union
Roles of Christian Voluntary Organization
Brain storming
Guided discovery
Discussion
Sharing
Appreciation
Critical thinking
Mentioning voluntary organizations.
Spelling , reading and writing
Board
New Pri. Six curr, pg 226 – 233
Mk stand. R.E bk 6 pg 121
5
1
Christians on the way
Contributions of science technology and education
States the meaning of technology.
States the effects of technology.
Spells and reads words e.g. Technology , communication
Technology
Application of technology
In transport and communication
In building
In farming
In food preservation
In entertainment
In power production.
Bad effects of technology.
Pollution of air and water
Increased employment
Destruction of culture
Increased death rate
Inquiry
Question and answer
Guided discovery
Sharing
Love
Reading
Stating the contributions of technology towards x-tian development
Board
Primary six curriculum.
2
National laws and rules
</passage>

<passage id="lchk_103d74844b1745b4a3b7fe2a24e04ded" source="P.6 R.E scheme term 3" part="3">
Question and answer
Guided discovery
Inquiry
Sharing
Love
Stating ways of doing God’s work.
Board illustration
Primary Six curr.
2
How giving and receiving brings happiness
True source of happiness.
Living right with God.
A good relationship with God.
Doing God’s work.
- Sharing with the needy
Giving
- Appreciating
- Receiving gifts from friends
- Receiving the needy.
</passage>

<passage id="lchk_352756f3359c4065bddf3735cad81ad3" source="p.6 R.E Scheme term III 2019" part="1">
P.6 R.E SCHEME OF WORK TERM THREE 2019
WK
PD
THEME
SUB-THEME
UNIT
COMPETENCES
CONTENT
LEARNER’S ACTIVITIES
T/L AIDS
REF
RE
1
1
Christians on the way
Friends on the way
Friendship
Meaning and importance of friendship
SUBJECTS
The learner:-
-Explains the meaning of friendship
-Describes the importance of friendship
LANGUAGE
The learner
reads, pronounces, writes, spells and uses the following words correctly
-Friend
-Friendship
-Relate
-Relationship
-Advice
-Crisis
-Marriage
WHO IS A FRIEND?
A friend is a person with whom you relate freely.
He/she is a person you can tell about your feelings and secrets.
Importance of friendship
Friends give us good advice and encouragement
Friends provide us with practical support.
How Jesus showed true friendship to his apostles and other people.
Jesus’ friendship was selfless he spent much time serving others
He also died for our sins.
Jesus spent most of his time with the outcasts in society eg. the sick, blind/ disabled
Humility – Jesus had a lot of humility- Jesus was humble and respected other people beyond himself
Servant hood – Jesus’ life was an example of servant hood
Group work discussion about the meaning of friendship
Bible reading about Jonathan and David Isam : 20: 1 –ff.
The Bible
MK.R.E
Bk.6
Pg 103
109
1
2
Christians on the way
Friends on the way
Qualities of a good friend
SUBJECT
The learner;
-Explains Jesus’ example of friendship (John, 5:12-15)
-Describes from the gospel how Jesus showed friendship to his apostles and other people.
-Describe Jesus’ qualities as a good friend
LANGUAGE
The learner
reads, pronounces, writes, spells and uses the following words correctly
- Friend
- Friendship
- Relate
- Relationship
- Advice
- Crisis
-Marriage
Jesus’ example of friendship
-Jesus commanded us to love one another as he loved us.
-He used the His own example of dying for us on the cross “Creator love has no one than this, that he lay down his life for his friends”
-If we act as Jesus did he does not call us servants but friends for he teaches us the will of his father.
Qualities of a Jesus as a good friend
-Selflessness- the act of wanting to please others more than yourself.
Jesus gave his life for us (John 15:13)
-Humility refers to humbles when you are humble, you cannot start to think that you are more important than others. You treat others the some way you want them to treat you.
-Servant hood – a good friend should have a spirit of servant hood.
Jesus always served others and wanted to please his father in heaven
-Understanding
This is a friend who is not quick to judge other people’s mistakes but to them listens first.
Jesus had many people provoke him with questions but he answered back with understanding he never intended to annoy anyone
Forgiving
True love
Mutual respect
Patience and tolerance
Loyalty, openness and trust
-Bible reading John 15,12-15.
-Discussions about qualities of a good friend
-Sharing experiences when they were good or when someone was good to them.
The Bible
MK.RE
Pg
103.104,105
1
3
Christians on the way
Friends on
the way
How to distinguish between good and bad advice
Subject
The learner;
Explains the importance of advice
Distinguishes between good and bad advice in friendship
Give examples of good advice and bad advice.
Identifies qualities
States the importance of advice
LANGUAGE
-learners should be able to read, pronounce and use the following words in sentences.
-Advice
-Godly
-Marriage
-Respect
-Mutual love
-Companionship
ADVICE
</passage>

<passage id="lchk_d6bba15e192f4643bb63d6960deda0cf" source="p.6 R.E Scheme term III 2019" part="8">
-Christians are called to lead a life of purity before their God.
-Jesus set a good example for us that even when he had no sin he was crucified for our sins but still remained pure
Ways through which we can purify ourselves.
As human beings we are not perfect although we are called to be God wants us to continually purify ourselves sin prevents us from going to heaven some of the ways we can purify ourselves on a daily basis are:-
- Repenting
- Forgiving others
- Having courage as we seek God
- Praying to God
- Reading the Bible
- Reading Christian literature
- Attending fellowships at church
- Showing love to others in what we do and say.
- How remaining pure helps us to go to heaven
- The hope of going to heaven results from our ability to remain pure in our doing living
The parable of the ten virgins
- Through this parable, Jesus teaches us to remain pure
-The five were wise and the five were foolish
-The foolish girls never reserved oil for their lamps by the time the bridegroom came, they were not prepared
-Only the five wise girls were prepared to receive the groom and to participate in the wedding
-Likewise believers who are not purified may fail to go to heaven (Math.25:1-13)
Lessons learnt from the parable
-To keep ourselves pure at all times.
-To wait on God no matter the challenges.
-To put our hope in God at all times
Discuss ways of keeping yourself pure
The Bible
MK
R.E
Bk 6
Pg
147-148
</passage>

<passage id="lchk_f3b4d2d129c2446088a6dc2dec98a843" source="All P 4 To P 7 Religious Education Notes All Terms Copy" part="23">
The birth of John the Baptist announced.
Luke 1 : 10 – 17
Zechariah was a man who had strong faith in the coming of the Messiah.
He served God well in the temple and one time during his daily work.
Angel Gabriel appeared to him with Good News.
The News was that his wife Elizabeth would bear a child and his name would be John.
The Nature of the child (John the Baptist)
➢ Be filled with the Holy Spirit from birth.
➢ Change the hearts of many for God.
➢ Act as a bearer of Good News for many people.
➢ Come as messenger before the appearance of the messiah.
➢ Live a simple life and eating simple things
➢ Lead the type of life Elijah lived.
The resurrection of Lazarus.
www.freshteacheruganda.com For more lesson notes, please visit
TERM THREE
P.6 LESSON NOTES
RELIGIOUS EDUCATION
LESSON 1: WK 1
SUBTHEME: FRIENDS ON THE WAY
Friendship is relationship between people who love or like each other.
Friend is a person whom you can relate freely.
Importance of friendship
- It makes one feel secure
- Enable one to have someone to share and secrets
- Brings joy
- Gives individual self confidence
- Gives one a sense of belonging
- Brings opportunities to others.
Jesus’ examples of friendship (John 15:12 -15) love the life of God
This commandment urges people to love one another as Jesus loved them.
Qualities of a good friend
- Honest
- Respectful
- Trustworthy
- Peaceful
- Generous
- Humble
- Loving
- Kind
- Faithfulness
How Jesus expressed His love to mankind?
- He revealed to His disciples the secrets of the kingdom of heaven
www.freshteacheruganda.com For more lesson notes, please visit
- He was merciful to sinners
- He was considerate
- He had compassion and fed the hungry
- He consoled the sorrowful Mary and Martha
- He called children to Him and showed them love
- He taught His disciples the skills of love
Lesson 2 Wk 1
Advice
This is an opinion or suggestion about what somebody should do in a particular situation
Importance of advice (Sam 2:12)
- May save someone from danger
- Promotes peace and harmony
- It promotes unity
- It promotes friendship
- Encourages development (2 Sam 1:12) difficult mission of prophet Nathan)
Characteristics of bad advice
- It encourages evil
- It encourages biasness
- It is dishonest
- It is not corrective
Crisis and how friends offer support in times of crisis
Meaning of crisis
Crisis is a time of trouble in which a quick solution should be given (Proverb 17:17-18)
A friend is always a friend at all times in happiness or in sorrow.
Lesson 3: wk 1
Marriage
Meaning of marriage
Marriage is a legal love union between man and a woman as a husband and wife
Qualities of a good marriage partner according to the Christian teaching
- Age
- Beauty
- Character
- Dignity
- Education
- Family background
www.freshteacheruganda.com For more lesson notes, please visit
- Godliness
- HIV/AIDS
- Status
Reasons why people marry
i. To have children
ii. For companionship
iii. To express love
iv. For sexual desires
v. For security
vi. For prestige
Signs of marriage
i. Mutual love
ii. Patience
iii. Trust
iv. Openness
v. Faith fullness
vi. Bearing children
vii. Fulfillment of marital duties
viii. Showing sympathy to each other
Marriage as a social institution
It is the society concern because it involves all members of the community such as wedding
preparations, witnessing the marriage ceremonies.
It unites different families, clans, tribes and races
Marriage vows
</passage>

<passage id="lchk_72408bf80d91438bbf3bb3f312247c94" source="CRE NOTES & SCHEMES P.6" part="16">
Qualities of a good friend
Honest
Respectful
Trustworthy
Peaceful
Generous
Humble
Loving
Kind
Faithfulness
How Jesus expressed His love to mankind?
He revealed to His disciples the secrets of the kingdom of heaven
He was merciful to sinners
He was considerate
He had compassion and fed the hungry
He consoled the sorrowful Mary and Martha
He called children and showed them love
He taught His disciples the skills of love
Lesson 2 Wk 1
Advice
This is an opinion or suggestion about what somebody should do in a particular situation
Importance of advice (Sam 2:12)
May save someone from danger
Promotes peace and harmony
It promotes unity
It promotes friendship
Encourages development (2 Sam 1:12) difficult mission of prophet Nathan)
Characteristics of bad advice
It encourages evil
It encourages biasness
It is dishonest
It is not corrective
Crisis and how friends offer support in times of crisis
Meaning of crisis
Crisis is a time of trouble in which a quick solution should be given (Proverb 17:17-18)
A friend is always a friend at all times in happiness or in sorrow.
Lesson 3: wk 1
Marriage
Meaning of marriage
Marriage is a legal love union between man and a woman as a husband and wife
Qualities of a good marriage partner according to the Christian teaching
Age
Character
Dignity
Education
Family background
Godliness
HIV/AIDS free
Status
Reasons why people marry
To have children
For companionship
To express love
For sexual desires
For security
For prestige
Signs of marriage
Mutual love
Patience
Trust
Openness
Faith fullness
Bearing children
Fulfillment of marital duties
Showing sympathy to each other
Marriage as a social institution
It is the society concern because it involves all members of the community such as wedding preparations, witnessing the marriage ceremonies.
It unites different families, clans, tribes and races
Marriage vows
In bad and good times, poverty and riches, sickness and healthy, only death that will separate us
What the couple does in the church
Vows
Signing marriage certificates
Exchange of rings
Types of marriages
Religious marriage
Customary marriage
Civil marriage
Religious marriage
This is a type of marriage officiated by a religious leader
Customary marriage
This is a type of marriage officiated by both the parents of the bride and the bride groom
Civil marriage
This is a type of marriage officiated by government official like CAO
Bride price /dowry
This is the money and property in some societies that the bride groom must pay to the bride’s family.
It recognizes marriage
It creates a bond between the family of the bride groom and the bride.
It is a way of thanking the parents of the bride for having kept their daughter.
Biblical teaching on marriage (1 Cori 7:1-16)
It encourages monogamy
A man should fulfill his duty as a husband and a woman should fulfill her duties as wife.
A husband is a master to his wife’s body
Common marriage problems
Quarrels
Fights
Lack of respect
Neglect of children
Lack of trust etc
Lesson 1: wk 2
Subtheme: Christian organization in development
Cooperation
Cooperation means working together to achieve a desired goal
Possible ways of cooperation
Through good leadership
Through democratic laws and rules
Through concern of welfare of other people
Through working hard
Through provision of freedom and security
Voluntary organization
These are organizations that offer free services to people
Importance of voluntary organization
It promotes the welfare of vulnerable people
</passage>

<passage id="lchk_e712bba159ff48b39add03bf64f3c04d" source="Islamic Studies Grade 06" part="67">
____
was called the 'prince of physicians.' 4.
5. Ar-Raazee differentiated between the diseases of _ _ _ _ _ _
_
and
---------
B. Answer the following questions.
1 . What different areas did Islam contribute to?
2. Mention Islam's contributions to various fields of mathematics.
240
3. What did the Greeks lack in spite of their advanced scientific work?
4 . Why a re the 'Arabic numerals' named a s such?
5 . How did Islam encourage Muslim contribution to astronomy and
medicine?
241
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
