# Job ltsk_07ee47bd1de34af0a8caf41adea176e3-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: draft the OUTLINE of a scheme of work for Christian Religious Education, Primary Seven 2026, Term 3.
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

REQUIRED NCDC topics/themes for Primary Seven 2026, Term 3 (from the NCDC curriculum, in this order). Every one MUST have at least one unit whose title or theme names it, with about this many teaching/practice lessons:
  8. Strengthened by the Spirit we: about 6 lessons
  9. Praying in the Spirit: about 6 lessons
  10. Growing in the Spirit: about 8 lessons
Keep to these evidence-based shares. A broad topic may take substantially more lessons than a small topic when its NCDC scope, competences and subtopics justify it.
Do NOT write lesson content yet. Each unit and lesson must cite the passage ids it comes from in sourcePassageIds.

Reply shape:
{"title":string,"summary":string,"units":[{"title":string,"theme":string|null,"weekFrom":int|null,"weekTo":int|null,"competences":string|null,"sourcePassageIds":[string],"lessons":[{"title":string,"subtopic":string|null,"kind":"teach"|"practice","objectives":[string],"sourcePassageIds":[string]}]}],"gaps":[string]}

<passages>
<passage id="lchk_0d7438cad8924bbe9a8d510e64c4f5c7" source="NCDC PRIMARY SEVEN SET ONE – Religious Education" part="1">
Religious Education Syllabus

Primary Seven Curriculum

Background
Religious Education (RE) is part of the whole educational experience.
It deals with the religious and moral beliefs and values that underpin
personal choices and behaviour such as relationships, health and
practices in life. RE is an important subject on the school curriculum
because it impacts on the morality of individuals and the society at
large by developing values like love, peace and justice. Therefore, RE is
necessary for the development of moral and spiritual values as well as
life skills. Christianity and Islam are the two major religions in Uganda.
These religions have a lot in common.

Importance of RE to the Learner
Religious Education enables the learner to:-
• gain knowledge about God and the world.
• develop self discipline, integrity, tolerance and human
fellowship.
• develop spiritually.
• develop personal discipline and good manners.
• make sense of themselves, their own experiences and the world
in which they live.
• learn about communities of faith, the foundations of given
religions, religious practices and festivals, rituals and holy
days, marriage customs, as well as regulating the interpersonal
behaviour.
• become a well balanced and mature young citizen who makes
informed choices about beliefs.
• behave positively in society.
• grow into an all-round, balanced, responsible and mature
member of the society.
Given its nature as a comprehensive discipline covering all aspects of
life, other subjects such as singing religious songs, making models and
pictures in RE and dramatising religious stories are integrated during the
Religious Education teaching and learning process.

National Curriculum Development Centre

The Primary Seven Religious Education syllabus comprises of two
alternative parts:
(i) | Christian Religious Education (CRE)
(ii) Islamic Religious Education (IRE)
Each part provides the topic outline to be covered in a year. It is up to the
individual school to decide which part they want to teach. They may opt
to teach CRE or IRE depending on the available resources, the foundation
bodies, and other stakeholders.

Part I: Christian Religious
Education

National Curriculum Development Centre

Introduction
The P7 Christian Religious Education syllabus has one theme “Christians
and the Holy Spirit” which is broken down into topics that are taught
throughout the year. An attempt has been made to create a bond between
Christians and the Holy Spirit in all aspects of their lives. This includes
living, service, enjoyment, growing up, praying, using gifts, loving and
freedom.

Rationale
The manifestation of the Holy Spirit in Christians is done through
appreciating richness in the Spirit, ancestors, ourselves and the Spirit
being enriched by other nations and religions, service to others in the
spirit, living in the spirit of love, freedom, enjoyment in the spirit, being
helped by the spirit, enjoyment of the gift of life, being strengthened by
the spirit to accept the events of life, praying in the spirit, and growing up
in the spirit.

Organisation of the Syllabus
A background for each topic has been provided. It gives an overview of
the topic, thus giving the teacher an insight into the topic.

Learning Outcomes
Learning outcomes have been stipulated for each topic. Learning outcomes
define the overall direction of the teaching and learning process. It is
what the learner understands, knows and is able to do. They are achieved
</passage>

<passage id="lchk_b76cec0204e74a49aa88162e63a31fb0" source="NCDC PRIMARY SEVEN SET ONE – Religious Education" part="2">
through competences.

Competences
Competences describe the specific abilities of the learner. It is what the
learner can demonstrate, show and do as a result of being exposed to
the given RE content. The syllabus stipulates subject and language
competences to be developed in each topic. These competences focus on
knowledge, comprehension, application and attitude change. Language
competences have been emphasised to enhance literacy skills.

Life Skills and Values

Primary Seven Curriculum

Life skills are personal and social skills that enable young people to
function confidently and competently with others. The curriculum
emphasises the development of life skills and values across all subjects.
This will create awareness among the learners and enable them practice
what is acceptable in society. Life skills and values must be on your finger
tips so that you stress and apply them as you teach.

Life skills help learners to:
– | make informed decisions.
– | practice healthy behaviours.
– | avoid risky situations.
– | change attitudes.
– | become good citizens.
– | be active and constructive in life.
– | solve problems encountered in different situations.
– | cope with stress and control their emotions.
– | communicate effectively.
Below are the suggested life skills and values you need to develop and
refer to during scheming and teaching/learning.

Life skills and their indicators
Skills of Living with Oneself
Effective | Friendship Formation | Self-Esteem
Communication | • Sharing | • Expressing likes and
• Fluency | • Playing with others | dislikes
• Audibility | • Working in groups | • Self-appreciation
• Meaningfulness | • Using polite | • Talking about self
• Confidence | language
• Articulation | • Love
• Accuracy | • Concern
• Logical flow of ideas | • Care
• Verbal | • Trustworthiness
• Non-verbal | • Faithfulness
• Responsibility

National Curriculum Development Centre

Assertiveness | Self-Awareness
• Being open | • Self identification
• Listening and | • Self evaluation
valuing what others | • Talking about one’s
say | potential, feelings
• Expressing one’s | and emotions
point of view | • Talking about one’s
• Volunteering | culture e.g. tribe,
• Giving reasons for | home, religion
actions taken | • Knowing one’s
• Standing up for | position and
one’s rights | responsibility
• Responding to | • Making choices
questions | • Caring for oneself
Skills of Making Informed Decisions
Creative Thinking | Decision-Making | Critical Thinking
• Logical reasoning | • Acceptance | • Responding to
• Initiating new ideas | • Refusal | questions appropriately
• Innovativeness | • Making questions | • Selecting and
• Finding different | • Asking questions | evaluating information
ways of doing | • Giving instructions | • Analysing statements
things | • Telling | • Giving reasons for
consequences of | action taken
decisions made | • Making a decision
• Making the best use of
the information you
have

Primary Seven Curriculum

Problem-Solving | Interpersonal | Coping with Stress
• Taking a decision | Relationship | • Being patient
• Making choice | • Forgiving others | • Forgiving others
• Evaluating facts | • Interacting freely | • Accepting advice
• Finding different | with others | • Talking about personal
ways of doing | • Caring for others | problems
things | • Sharing with others | • Narrating past
• Knowing how | experiences
Empathy
to be with
• Supporting others
different people
• Caring
under different
• Guiding others
circumstances
</passage>

<passage id="lchk_86310d98cff1405a854548de477e0a10" source="NCDC PRIMARY SEVEN SET ONE – Religious Education" part="3">
• Using appropriate
• Working together
language (etiquette)
• Respecting others’
• Listening to others
opinions
• Comforting
• Reacting
appropriately
• Respecting other
people’s property,
cultures, and so on
• Appreciating
individual
differences
Skills of Living with Others
Negotiation | Non-Violent Conflict | Coping with Emotion
• Using persuasive | Resolution | • Recognising emotions
language | • Resolving issues | • Identifying other
• Using appropriate | without fighting | people’s emotions and
body language | • Negotiating | feelings
• Temper control | • Using appropriate | • Being sensitive about
• Responding | language | other people’s feelings
appropriately | • Assisting others | • Recognising causes for
• Apologising | to come to an | different emotions
• Requesting | understanding | • Making critical
• Thanking | • Coping with stress | decisions for different
• Accepting defeat | emotions
Peer Resistance
• Knowing when to | • Not letting your
• Standing for one’s
give in | emotions affect your
values and beliefs
decisions
• Defending one’s
decisions
• Standing by one’s
principles

National Curriculum Development Centre

Values
These are the desired standards of behaviour acceptable in society.
Values need to be developed during and after the teaching and learning
process. Examples of values include cooperation, sharing, appreciation,
endurance, patience, responsibility, care, respect, trustworthiness, love,
togetherness, honesty, joy, concern, privacy, independence, self-reliance.
It is important to note that you need to observe the learners to see whether
they are practising what they learn.

Methodology
You are expected to use child-centred methods which put the learner
at the centre of the teaching and learning process. Some of the methods
to be used during the teaching and learning process include project
work, discussion, role-play, brainstorming, storytelling, excursion,
dramatisation, demonstration and debating.

Instructional Materials
Instructional materials are very important in lesson delivery. Use
instructional materials and get learners involved in the teaching and
learning process as this will help learners get more interested in their work.
Use a wide range of instructional materials. Examples of instructional
materials include textbooks, bible, money, clock, pictures, charts,
poster of major world religions, magazines, life skills manual, Young
Talk (newspaper), human rights documents and electoral commission
materials.

Assessment
Continuous assessment is recommended and should be based on the
suggested competences for each topic. Assessment should be carried
out during and after the teaching and learning process, at the end of the
topic, at the end of the term and at the end of the year. Keep records
of the assessment. Christian Religious Education should be assessed
using two basic attainment targets, knowledge and practice. Learners are
expected to gain knowledge of/about the religious beliefs and practice
what is taught and learnt in class. They should transfer that knowledge
to practical situations in the daily life.

Primary Seven Curriculum

Guidance to the Teacher
• You are free to use relevant books of the old curriculum and
any other materials related to the content. However you should
be mindful of the novelties and modifications introduced in the
syllabus which may require new information.
• The key words that appear in the column of language
</passage>

<passage id="lchk_6fbb76e4226043a4b69e2930bcaf1e7f" source="NCDC PRIMARY SEVEN SET ONE – Religious Education" part="4">
competences represented in each topic will enable you develop
literacy skills.
• You are expected to relate the content to daily life situations. As
far as possible you should avoid using hypothetical examples
which normally begin with “suppose” or “imagine”.
• When teaching Religious Education, you should relate God’s
message/word to real life experiences. Put emphasis on
practising what is learnt.
• You are expected to be a role model and should be knowledgeable
about the content of learner’s discipline. In case of any difficulties,
it is advisable to seek assistance from resource persons.
• The methods you choose to use should be those which contribute
to the achievement of the expected learning outcomes,
competences, and eventually lead to the achievements of the
aims and objectives of Primary Education. They should be
interactive in order to make the learning process interesting.
• You should not be the director of the learning process; instead
you should allow learners to make contributions at every stage
of lesson development and discussion.
• You should be gender sensitive, and mindful of learners with
special needs.
• You should take note of peculiar words and difficult terminology
frequently used.
• Avoid hurting the feelings of the learners who may not
agree with you. Do not take sides on issues where Christian
denominations differ.
• Use pictures as much as possible in the teaching and learning
process. Some RE concepts become easier to understand when
presented pictorially.
• Read the bible commentaries for more information.
• Observe learners in and outside the class to see whether they
are practising what they learnt to ensure change of attitudes.

Topic Outline
THEME: | CHRISTIANS AND THE HOLY SPIRIT | No. of
periods
TERM I
Topic 1: | Enriched in the Spirit | 7
Topic 2: | Ancestors, Ourselves and the Spirit | 7
Topic 3: | Enriched by other Nations and Religions | 7
Term II
Topic 4: | Serving others in the Spirit | 6
Topic 5: | Living in the Spirit of Love | 9
Topic 6: | The Spirit Makes us Free | 6
Topic 7: | The Spirit Helps us to Use His Gifts | 6

TERM III
Topic 8: | Strengthened by the Spirit we Accept the | 6
Events of Life
Topic 9: | Praying in the Spirit | 7
Topic 10: | Growing in the Spirit | 7

Term I

Theme: Christians and the Holy Spirit

Topic 1: Enriched in the Spirit | 7 Periods

Background
God’s Holy Spirit in us, as Christians, is our greatest gift. When we receive
the gift of the Holy Spirit we receive the gift and the giver, because the
gift is the giver.

At the time of creation, man was created in God’s image. The image of
God in man is the Spirit. The Spirit is expected to help man fulfil his God-
given responsibility of being accountable for his entire creation including
animals. This topic will expose the learner to discover the richness of the
Spirit and how it helped bridge the gap between God and the people of
the New Testament. It will also help the learner to discover that the Spirit
that helped Jesus in his work is the very Spirit that guides us today.

This topic aims at equipping the learner with knowledge about creation
and the position of human beings in creation. It also shows the learner
man’s failure to live up to God’s standards and how God’s plan bridged
the gap.
Life Skills
• Critical thinking
– analysing statements
– making the best use of information
• Decision-making
– telling consequences of their decisions
• Self-awareness
– knowing one’s position and responsibility
</passage>

<passage id="lchk_b0147db8650c4ac78a3b68a71ebb998e" source="NCDC PRIMARY SEVEN SET ONE – Religious Education" part="14">
daily life.
• uses own talents responsibly.

Term III

Topic 8: Strengthened by the Spirit we
Accept the Events of Life
6 Periods

Background
In our daily life, we need knowledge and strength to handle different
events in life. The Holy Spirit gives us the Spirit of strength and when
we consistently work in the Spirit, we bear fruits. This topic brings to
the learners the ideas of success, failure, fear and courage. It guides the
learners on what brings about success and failure. The learners will be
equipped with skills of coping with emotions.
Life Skills
• Critical thinking
– giving reasons for action taken
– selecting and evaluating information
• Decision-making
– making choices
– telling consequences of decisions made
• Self esteem
– Self-appreciation
– talking about self
– expressing likes and dislikes
• Coping with emotions
– identifying other people’s emotions
– temper control
– apologising
• Coping with stress
– | being patient
– | accepting advice
– | talking about personal problems
– | Narrating past experiences

National Curriculum Development Centre

Values
• Confidence
• Responsibility
• Commitment
• Cooperation
• Patience
Learning Outcome
The learner develops skills to make necessary emotional adjustments to
cope with failure and fear as well as celebrate success.

Primary Seven Curriculum

Subject | Language | Content | Suggested
competences | Competences | activities
The learner | The learner | • Success and
• explains the | reads, writes, | failure | • Sharing
meaning of | spells, | – Define success | success
success and | pronounces | and failure. | stories
failure. | and uses the | (Job 1: 1-22, | • Memorising
• describes | following words | Joshua 7: 1-6, 8:1- | key verses
the causes of | related to the | 23) | from the bible
success and | topic correctly: | – Causes of success | on success
failure. | – success | and failure | and failure
• explains how | – failure | – How God helps | • Writing
God helps | – cope | people to cope | stories on
people to | – fear | with positive | failure and
cope with | – courage | and negative | success
positive and | – emotions | experiences | • Discussing
negative | – pollutants | (Luke 4: 1-13, | about fear
experiences. | – natural | Matthew 14:23- | and how to
• explains the | habitat | 31, Romans 12:3- | overcome it
causes and | – cruelty | 13) | • Discussing
value of fear. | • Fear | about causes
• explains how | – The causes of | of fear in
Jesus was | fear in human | animals
strengthened | beings | • Setting
by the Holy | – The causes of | personal
Spirit. | fear in animals | goals
• manages own | – The value of fear | individually
emotions | – Bible teaching | • Saying
• describes | on fear and | prayers
causes of fear | courage (Gen. 15: | related to
in animals. | 1, Joshua 1:5-9, | success
Isaiah 41: 10, 13, | • Sharing
Jeremiah: 1: 6 -8, | experiences
1 Peter 5:7, Mark | on how
14: 32-36) | to control
• Emotions | emotions
– Recognizing our | • Role-playing
emotions | success, fear
– Managing our | and courage
emotions
– God’s help in
managing our
emotions (Gen.
45, John 16: 33)

National Curriculum Development Centre

Guidance to the Teacher
• Guide the learners to tell what they understand by success and
failure.
• Guide learners to share experiences of failures and successes.
• Discuss the causes and effects of success and failure.
• Guide learners to role-play success, fear and courage.
• Guide the learners to read key verses about success and failure
</passage>

<passage id="lchk_1b06da28b592406a82ed54b1d8a98585" source="NCDC PRIMARY SEVEN SET ONE – Religious Education" part="35">
Masjid Qiblatayn, Masjid Quba, Cave of Hira, rights, status, afford,
expenses, Uganda Muslim Supreme Council, Uganda Muslim Education
Association
</passage>

<passage id="lchk_407576c7d86e431fb64bcb8c8a691e27" source="All P 4 To P 7 Religious Education Notes All Terms Copy" part="43">
For more lesson notes, visit www.freshteacheruganda.com
• Fear is the feeling that something bad may happen.
Forms of fear
• Real fear – afraid at objects that can harm
• Imagined fear – general fear to fail
• Anxiety – state of being worried.
Causes of fear
• Being lonely
• Lack of confidence
• Death
• Embarrassment
Values of fear
• Helps us to avoid dangerous situations
• Makes us do tasks better
• Makes us respect those who can protect us
• Makes us to seek for God’s help.
Biblical teachings on fear (mark 14 : 32 – 36 Joshua 1:5 – 9 Isaiah 41: 10 – 13 / 14)
• Always pray to God for strength and courage
• Have determination, confidence and obey God’s commandments.
• Leave all our worries to God.
Emotions
• An emotion is a state of one’s mind.
Examples of emotional feelings
• Sadness, Anger, fear, cheerfulness
How to control emotions
• Being patient
• Avoiding anger
• Avoiding revenge
• Being kind
• Believing in God in all situations.
TOPIC 9 PRAYING IN THE SPIRIT
• Communication is the sending and receiving of information.
How God communicates to us
• Through the bible
• Through visions
• Through prophets
For more lesson notes, visit www.freshteacheruganda.com
• Through priests
How we communicate to God
• Through prayer
• A prayer is a special way of communicating to God.
Types of prayer
• Praise prayer
• Thanks giving prayer
• Confessional prayer
• Petition prayer
• Intercession prayer
• Liturgical prayer
Teacher to explain to learners
Importance of prayer
• Brings us closer to God
• Helps us to control our emotions
• Helps us talk to God
• Helps us find peace in times of stress and sorrow.
Reasons why people pray
• To thank God
• To praise God
• To confess our sins
• To ask for protection
Ways of praying
• Praying silently
• Praying loudly
Principles to follow during prayer
• Have faith
• Being humble before God
• Turn the whole mind to God (be focused)
• Present all your desires and needs.
When should a Christian pray
• When in need
• Any time
• During joy / sorrow
Jesus teaching on a prayer (Mathew 6:9 – 13)
• Jesus taught his disciples the Lord’s prayer.
For more lesson notes, visit www.freshteacheruganda.com
Teacher mentions what we ask for in the Lord’s prayer
Lessons learnt from the Lord’s prayer.
• To praise God
• To request God for our daily needs
• To ask God for forgiveness
• To ask God to protect us from evil
• To forgive others.
Reasons why Jesus prayed
• To get food (Luke 8:6)
• To forgive his enemies (Luke 23:33-34)
• To know God’s will (Mathew 26:42)
• To ask for strength and courage (matt. 26:39)
Places where Jesus prayed from
• Gethsemane (matt 26:39-42)
• On top of the hill (Mark 6:46)
• At the grave yard (John 11:41 – 43)
TOPIC 10 GROWING IN THE SPIRIT
• Prayer in the early church
• Arrest of Peter and John (acts 4: 1 -4)
• Release at Peter from prison (acts 12: 1 -10
• Peter resurrects Tabitha (acts 9: 36 – 41)
• Paul and Barnabas (acts 14:21 – 23)
Creeds
• Creeds are statements of Christian beliefs.
• Examples of creeds:
- apostles creeds
- Nicene creed
- Athanasius creed
sections of creed
- God the father
- God the son
- God the Holy Spirit
Sacraments
• A sacrament is a symbolic religious celebration through which Christians believe
that they receive God’s grace.
Characteristics of sacraments
• Must have a material sign e.g wine, bread.
For more lesson notes, visit www.freshteacheruganda.com
• Must have a system of giving (receiving)
• Must confirm the presence and power of Jesus.
Examples of sacraments
</passage>

<passage id="lchk_edb07a1f565d4058b8056094bebd7dd5" source="CHRISTIAN RELIGIOUS EDUCATION LESSON NOTES P 7" part="6">
• Confirmation
• Holy matrimony
• Penance
• Holy order / ordination
• Anointing of the sick
• Holy Communion / Eucharist.
Holy Spirit and prayer
• The holy spirit gives people the power to:
© 2019 Page 15
- Believe in God
- Believe in God’s teachings as written in the Bible.
- Have knowledge and wisdom
- Send our prayers to God
- Become members of God’s family through Baptism.
Holy Spirit in the church today
• A church is a group of Christian believers. The presence of the holy spirit in the
church is called New Pentecost.
• The following scriptures show the presence at the Holy Spirit in believers.
- Gal 3:14
Rom 8:9
1 Cor. 6:17
Rom 8:14 – 17.
• The New Pentecost
Roman 12:6
END
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
