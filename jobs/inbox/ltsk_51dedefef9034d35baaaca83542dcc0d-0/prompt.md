# Job ltsk_51dedefef9034d35baaaca83542dcc0d-0

You are the curriculum engine of Ledgerly AI for a Ugandan school.
Work from the passages, page images and records given in this prompt. Do not invent facts, topics, notes, examples, activities, questions, answers or names: every one of them is taken from the passages. You choose, order, tidy and format the material; you never make it up.
If the material does not cover something, leave it out or set the field to null and say so in "gaps". Never fill gaps from memory.
Do not run commands, open files or browse. Everything you need is in this prompt.
Reply with ONE JSON object only, exactly matching the requested shape. No prose before or after it.

Task: write ALL 3 lesson(s) below of week 1 of the Christian Religious Education scheme for Primary Four 2026, Term 3, in ONE reply: for each lesson its chalkboard notes AND its lesson plan.
Return exactly one entry per lessonId, keeping each lessonId exactly. Write the lessons in order so they build on each other; a practice or review lesson works from the lessons before it in this week.
Class-depth rule: P4: one 40-minute lesson: 2–4 sections; about 12–24 points; meanings, examples and uses; 5–7 activities.

lessonId=lles_650e6c904c8b4c088467eb413216f238: lesson 1, Tuesday, 1 period(s), 40 minutes.
  Unit: Reconciliation. Lesson: Christian ways of reconciling with God — Christian ways of reconciling with God.
  Objectives: State Christian ways of reconciling with God.

lessonId=lles_deee5b4da9214571aa5cd7019dd3f359: lesson 2, Thursday, 1 period(s), 40 minutes.
  Unit: Reconciliation. Lesson: Practice: Christian ways of reconciling with God — Christian ways of reconciling with God.
  Objectives: Write any two Christian ways of reconciling with God.
  This is a PART B lesson: it continues the subtopic taught in the lesson before it. notes = '### Remember' with the key points ('- ' points, 4–8 lines); in Mathematics, English and Reading then NEW '### Example' sections not used in Part A; then '### Exercise' with NEW numbered activities learners copy and answer. All of it is taken from other passages (other notes, workbooks, past papers), never invented. Oral work, drawing and group activities go in methods. activities = those exercises.

lessonId=lles_c0d9b3b73acf4dc389cca26dcf3e875e: lesson 3, Friday, 1 period(s), 40 minutes.
  Unit: Reconciliation. Lesson: Week 1 review — Reconciliation.
  Objectives: Review this week's lessons: Christian ways of reconciling with God; Practice: Christian ways of reconciling with God
  This is the FRIDAY REVIEW of this week's lessons (listed in the objectives). notes = a '### Summary' heading per lesson with its key points ('- ' points), then '### Exercise' with review questions taken from the passages. activities = those questions.

Write, using ONLY the passages below. Passages from "NCDC" documents are the official base for what to teach; NCDC lower-primary thematic curricula put every learning area in columns separated by " | ": use only the Christian Religious Education column.
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

<passage id="lchk_cdbacdc842ea4cada3b1ac35cb7fcf34" source="P 4 R E Lesson Notes Term III" part="3">
4. Why was King David not happy with Nabal.
Date Class L. Area No. of children Time
P.4 R.E
TOPIC : Peace
SUB TOPIC : Different ways of making peace in the bible.
INTRODUCTION : The lesson will introduced by reviewing the previous lesson.
CONTENT : LEVITICUS (26 – 3 – 20 )
God promised peace to those who believe in him. In order to have peace of God, we must have
faith in Him and His son Jesus Christ.
God tells us that if we live according to his commandments, He would do the following,
 Make us live safely in our land.
 Give us peace in our land.
 Enable us sleep without being afraid of any one.
 Stop all wars.
 Make us prosperous
Jesus made the following suggesting towards peace making
 Do not revenge on some one who wrongs you.
 When somebody asks for something, give it to him or her when someone wants to borrow
something, lend it to him/ her.
7
 Love your enemies and pray for them.
 According to St, Paul, she has three suggestions for peace, these are:- (Corinthians 13:13)
 faith
 hope
 love
St. Paul says love is the key to peace
The bible gives us the following ways of having peace.
 To obey God’s commandment.
 To help some one who asks for something.
 Not to be offended by people’s acts.
 To be patient by people who demand things from us.
 To love one another.
Exercise
1. Whom did God promise peace.
2. What should we do in order to be with peace from God?
3. State what God will do if we live according to his commandments.
4. What are the three suggestions of St. Paul for peace?
5. Outline the ways of having peace according to the bible.
6. List any two Jesus’ suggestions towards peace making.
Date Class L. Area No. of children Time
P.4 R.E
TOPIC : Peace
SUB TOPIC : The promotion of peace through communication and
Reconciliation
INTRODUCTION : The lesson will introduced by reviewing the previous lesson.
CONTENT : The story of Kato and His neighbour
There lived a man called Kato in Bigadda in Rakai district. He was richer than all his neighbours.
He had a car, a nice house and a number of goats and cattle.
One day, Kato’s cattle went and ate the neighbour’s crops. During the meeting, the neighbour
was angry, he explained the cause of the anger.
Kato stood up and apologized to the neighbour.
8
He bought some drinks and eats to the people.
Kato and the neighbour had reconciled.
In order to have peace, there must be good communication.
If somebody has annoyed you, you need to talk to him/ her about it.
When peace is brought back through proper communication, we call that reconciliation.
In Luke 22: 39 – 46, we read about how Jesus reconciled us with God.
Exercise
1. What is reconciliation?
2. What had Kato done to the neighbour?
3. Why was Kato’s neighbour not happy?
4. What did Kato do after the neighbour explained why he was annoyed?
Date Class L. Area No. of children Time
P.4 R.E
TOPIC : The birth of Jesus
SUB TOPIC : Problems that disturb peace
INTRODUCTION : The lesson will introduced by discussing the problems that
disturb peace.
CONTENT : Problems that disturb peace.
 Unforgiveness
 Hatred
 Injustice
 Tribalism greed
 Greed
Results of lack of peace
 Wars cause death
 They lead to hatred and destruction of property
 It leads to lack of trust to one another.
The suffering of Israelites in Egypt (Exodus 7)
 The Israelites lived in Egypt for a period of 430 years.
 Their ancestors went to Egypt because of famine in their land.
 The king who welcomed them died.
</passage>

<passage id="lchk_17bbbfa0c681404fa8df11cf6d361f88" source="P 4 R E Lesson Notes Term III" part="5">
 No person can ever get peace unless he is reconciled with God.
 Through acceptance of Christ’s salvation, we become daughters and sons of God. As
Christians, we must always seek peace with others and God.
 When we have problems, we must seek for God’s comfort and peace.
 Luke 12:22 – 33, Jesus assures us that God will always solve our problems because he knows
them.
 Jesus told his disciples that he had left them with peace when he was going to heaven.
Exercise
1. Name the person who held Jesus in his hands in the temple.
2. State Simeon’s message at the temple.
3. How was God’s promised peace achieved?
4. How do we become sons and daughters of God?
5. According to Luke 12: 22 – 33, what does Jesus assures us?
6. What did Jesus leave with his disciples?
Date Class L. Area No. of children Time
P.4 R.E
TOPIC : Making our Decisions as Christians
SUB TOPIC : Good decisions in the Bible
INTRODUCTION : The lesson will introduced by discussing what decision making
is. Giving examples of good and bad decisions in the Bible.
12
CONTENT : Examples of people who made good decisions in the Bible
John the Baptist
 He accepted to Baptize Jesus in river Jordan.
 He also preached about repentance to prepare for the coming of Jesus
 The mother of John the Baptist was Elizabeth
 John the Baptists met his death after being beheaded
Moses
 He accepted to rescue the Israelites from slavery in Egypt.
 Moses led the Israelites out of Egypt but he never reached the Promised Land.
 He also accepted to receive the ten commandments on Mt. Sinai
Joshua
 He accepted to lead the Israelites to the promised land of Canaan. he succeeded Moses.
Abraham
 He accepted to sacrifice his son Isaac.
 The mother of Isaac was Sarah
 Abraham also accepted to leave Haraan to Canaan.
Jesus :
 He accepted to be born like other human beings.
 He also accepted to be sacrificed for our sins.
 Jesus showed us love through the miracles he performed.
Exercise
1. List any three people in the Bible who made good decisions.
2. Mention the major message John the Baptist preached.
3. From which mountain did Moses receive the Ten Commandments?
4. Name the wife of Abraham.
5. State the promised land where the Israelites.
6. Why did God tell Moses to rescue the Israelites?
7. Which good decision did Abraham make?
8. Give two ways Jesus showed love to us.
13
9. State the reasons why Jesus died on the cross.
10. Mention Abrahams’ son he wanted to sacrifice.
Date Class L. Area No. of children Time
P.4 R.E
TOPIC : Making our decisions as Christians
SUB TOPIC : Bad decisions in the bible
INTRODUCTION : The lesson will introduced by reviewing some examples of
people who made bad decisions in the Bible.
CONTENT : Examples of people who made bad decisions in the bible.
Simon Peter
 He denied Jesus three times and after the cock crawled
Pontius Pilate
 He sentenced Jesus to death
Adam and Eve;
 They disobeyed God and ate the forbidden fruit.
Cain :
 He killed his brother Abel due to jealousy.
Jonah
 He disobeyed God by refusing to go to the people of Nineveh and instead went to Spain.
 He was swallowed by a fish
King Darius
 He ordered his officials to throw Daniel in the den of lions
Judas Iscariot
 He betrayed Jesus
 He hanged himself.
Exercise
1. How many times did Simon Peter deny Jesus?
2. Apart from Simon Peter, name any other three people in the bible whop made bad
decisions
3. State the bad decision which Adam and eve made.
4. Name the third born of Adam and Eve.
</passage>

<passage id="lchk_c47cbc2258984d10a0b923448576c6b0" source="P 4 R E Lesson Notes Term III" part="1">
1
P.4 R.E LESSON NOTES FOR TERM III
Date Class L. Area No. of children Time
P.4 R.E
TOPIC : Making our decisions as Christians
SUB TOPIC : Examples of Good and Bad Decisions
INTRODUCTION : The lesson will introduced by discussing the good and bad
decisions
CONTENT : Examples of Good and bad decisions
Decision making is identifying and selecting a certain action in order to deal with a certain
problem. Decision can either be good or bad.
A decision is a choice taken by a person.
Examples of good decisions
 Helping your parents
 Going to church on Sundays.
 Forgiving
 Being honest
 Not stealing
 Not taking alcohol
Examples of bad decisions
 Not going to church on Sundays
 Stealing
 Taking alcohol
 Refusing to study
 Refusing to help your parents
Note :
The decision we make affect what we are and what we shall be in future.
Effects of bad decisions
 They make God unhappy.
 They annoy other people.
 They put us to shame.
Importance of making good decisions
 They make God happy.
 They make our parents happy.
 They do not bring conflicts.
2
 Good decisions do not lead us to the bad future.
 They create friendship.
 They promote order.
Exercise
1. What is decision making?
2. Give two examples of good decisions.
3. State two examples of bad decisions.
4. Outline three importance of making good decisions
Date Class L. Area No. of children Time
P.4 R.E
TOPIC : Making our decisions as Christians
SUB TOPIC : Some biblical examples of decisions and their effects.
INTRODUCTION : The lesson will introduced by reviewing the previous lesson.
CONTENT : Good decisions in the Bible
Mary – mother of Jesus
She decided to accept the responsibility of being the mother of Jesus the Saviour.
Daniel
He decided to worship God despite the law which had been put. God saved him from the lions in
which he had been thrown to eat him.
Bad decisions made by people in the bible.
The story of the sons of Eli. (1 Samuel 2:12 – 17)
Eli was a high priest in Israel. He had two sons Hophni and Phinehas. They made wrong
decisions for disobeying God by:-
 Taking meat from the worshipers by force.
 Sleeping with women who worked in the temple.
 God punished them and died in the war.
Judas Iscariot
 The following were some of the wrong decisions made by Judas Iscariot:-
Judas Iscariot:-
 He used to steal Jesus’ money in his money purse.
 He wanted to sell the oil Mary Magdalene had brought for Jesus.
 He betrayed Jesus Christ.
3
 He hanged himself
Herod the great
 He wanted to kill baby Jesus because he thought he would take his kingship.
Exercise
1. List any two people in the bible who made good decisions.
2. According to the Bible, who was thrown in the den of lions?
3. State any two people who made bad decisions in the bible.
4. Why should people make God decisions?
Date Class L. Area No. of children Time
P.4 R.E
TOPIC : Making our decisions as Christians
SUB TOPIC : How to make good decisions
INTRODUCTION : The lesson will introduced by reviewing the previous lesson
CONTENT : How to Make Good Decisions
We should not be quick or slow to make decisions. We need to think about these points before
making decisions.
 Never be quick to make decisions .
 Good decisions produce good results.
 Bad decisions produce bad results.
 Whenever possible, make sure that your decisions are based on the right facts.
 Consider how your decisions can affect you and others
 Always ask God to help you to make right decisions
</passage>

<passage id="lchk_38144eec07264e72b6e465b40f73e2d6" source="P 4 R E Lesson Notes Term III" part="4">
 The Israelites were forced to do hard work without payment.
 God used Moses to go and deliver Israelites from Egypt.
9
 The Israelites were suffering due to slavery.
 The Pharaoh first refused and God gave them punishments like:-
 frogs
 heavy rains
 death of first born
 boils
 Moses died on the way and Joshua led the Israelites to the Promised Land.
Israel at war with Syria
 Nations used to be at war in the Old Testament. Through wars, nations would expand.
 The king of Syria made plans to attack Israel.
 God had revealed the plans to the Israelites to the king through King Elisha.
 This annoyed the king of Syria.
 He thought that one of his people was revealing his secrets. Later he knew Elisha was
revealing his plans.
 The king of Israel wanted to kill them but Elisha effused.
Exercise
1. List two problems which disturb peace.
2. Outline any two results of war in an area.
3. List two punishments God gave top the Israelites for not realizing the Israelites.
4. State the work of Elisha.
5. What was Exodus?
Date Class L. Area No. of children Time
P.4 R.E
TOPIC : Peace
SUB TOPIC : God’s promised peace and how it comes.
INTRODUCTION : The lesson will introduced by reviewing the previous lesson.
CONTENT : God’s promised peace and how it comes
Adam and Eve lived in joy and peace in the Garden of Eden.
When they ate the forbidden fruit, they lost the peace.
Due to God’s abundant love, he planed to bring peace again through his son Jesus Christ.
10
Examples of peace God promised
 Rainfall
 Plenty of food.
 Safety in land
 Isaiah promised to bring peace to the world through the messiah.
 God’s son would be called Immanuel and prince of peace.
 God’s son would set his rule which bring peace.
The birth of Jesus – the prince of peace
 The Israelites lived under the Roman rule for a long time. The Romans were harsh and
oppressed the Israelites.
 The Israelites had hope in coming of the messiah.
 An angle called Gabriel announced to her that she would be pregnant by the power of the
holy spirit
 By then Mary was not yet married but engaged to Joseph, the carpenter.
 The savior was born in the town of Bethlehem in a kraal when Joseph and Mary had gone
for population census.
 An angel of God appeared to the shepherds and told them that the savior had been born.
 The baby boy was named Jesus which means savior.
 After some time, baby Jesus was taken to the temple in Jerusalem
 Baby Jesus was born on 25 th December which is the Christmas day
Exercise
1. Name the garden where Adam and Eve lived
2. How did God bring back peace to man.
3. Outline any three examples of peace God promised.
4. Why is Jesus referred to as the prince of peace?
5. Name the day Jesus was born.
6. State the mother of Jesus Christ.
7. Mention the heavenly father of Jesus.
8. Why was Jesus of Nazareth born from Bethlehem
11
Date Class L. Area No. of children Time
P.4 R.E
TOPIC : Peace
SUB TOPIC : Simeon’s Message
INTRODUCTION : The lesson will introduced by reviewing the previous lesson
CONTENT : Simeon’s Message
 Simeon was a God fearing man living in Jerusalem.
 Jesus and his parents found him in a temple.
 Simeon held Jesus in his hands and spoke out the message God gave him.
 “Now Lord you may let your servants go in peace” with message God gave him.
 God’s promised peace was achieved through the birth, suffering death and resurrection of
Jesus.
Seeking and promoting peace and comfort form God.
</passage>

<passage id="lchk_d5fddea82d5c431cb55939179350eeb4" source="P 4 R E Lesson Notes Term III" part="2">
 Never make decision in fear or never fear to make decision.
 Allow others to advise you but not to decide for you.
 For one to make a right decision, one must desire the right to do what is right or good.
Making unselfish decision and keeping them with God’s help.
 Selfishness is the act of caring for one’s self and not others
 With god’s help, we can make unselfish decision.
 The story of Ananias and Sapphira teaches us not to be selfish (they lied – Act 5:1 – 6).
4
Date Class L. Area No. of children Time
P.4 R.E
TOPIC : Peace
SUB TOPIC : The meaning of peace
INTRODUCTION : The lesson wills introduced by discussing what peace is
CONTENT : The meaning of peace
Peace is when there is war or suffering in a given area of country.
Peace is also a state of being in perfect joy and happiness with God and with people.
Signs which show unpeacefulness
 Pain
 disunity
 shame
 unhappiness
 fighting
 quarreling
In the story of Adam and Eve, they lived in peace in the Garden of Eden.
When they ate the forbidden fruit, they lost their peace. They started feeling pain, shame, and
unhappiness.
Peace given by Jesus
In John 14:27, Jesus says peace is what I leave with you.
It is my own peace that I give you.
 In order to get Jesus’ peace, we need to obey God’s commands.
 Uganda’s national emblem is the Crested crane. it was chosen to be the emblem because
it is humble and peaceful bird.
Traditional ways of keeping peace
Activities in the socictie4s which kept peace
 Celebrations
 Sacrifices
 Thanks giving
 Local games
 Exchanging visits
 Eating and working together.
 Child naming
5
 Circumcision
 Wedding parties
Exercise
1. Mention one sign which show unpeacefulness
2. Name the garden where Adam and Eve lived.
3. How did Adam and Eve disobey God?
4. What was the result of Adam and Eve’s disobedience to God?
5. Give any four traditional ways of keeping peace.
6. According to John 14:27, what does Jesus leave his disciples with?
Date Class L. Area No. of children Time
P.4 R.E
TOPIC : Peace
SUB TOPIC : Traditional ways f keeping peace
INTRODUCTION : The lesson will introduced by reviewing the previous lesson
CONTENT : Traditional ways of keeping peace
 By praying to God for him to keep peace.
 By keeping god’s commandments
 By keeping national laws.
 Listening to each other.
 Loving every body in the community.
The story of David and Abigail (1 Samuel 25:1 – 36)
 David sent a message and greetings to a man called Nabal.
 Nabal was mean and unfriendly. The wife of Nabal was Abigail.
 David sent his servants to tell Nabal that his shepherd and sheep were at David’s place.
David had not harmed any of them. David had sent Nabal for some eats
 However, Nabal just sent away the servants.
 When Abigail heard of what happened, she immediately went to David, knelt down and
apologized. She gave David lots of cakes; loaves of bread, grains and many other
presents then David forgave Abigail and her husbands.
The following were some of the traditional ways of bringing back peace.
6
 Paying fines.
 Asking for forgiveness
 Reconciliation
 Cleansing through sacrifices
 Handshaking / hugging in friendship.
 Discussing the causes and solutions of the misunderstandings.
 Sharing meals or drinks.
 Taking herbal medicine.
 Moving from the unpeaceful place to a peaceful one.
Exercise
1. State any three ways of keeping peace.
2. List any four ways of restoring peace.
3. What lesson do you learn from the story of King David and Abigail?
</passage>

<passage id="lchk_6282ae3b28cf40adb49220b546f28b53" source="P 4 Religious Education 2019" part="12">
Lesson 3
Unit : peace
Lesson content: Traditional ways of bring (restoring) peace
Paying fines
Asking for forgiveness
Reconciliation
Cleaning through sacrifices
Hand shaking and hugging in friendship
Sharing a meal or drink
Taking herbal medicine
Moving from unpeaceful to peaceful places
Our response
We can’t have development unless there is peace
COLLECTED, PRINTED & MARKETED BY ACOSMA EDUCATIONAL SERVICES (0752614244 ) Page 28
Therefore, we should all try to keep peace
Verse to remember: “Do everything possible on your part to live in
peace with everybody” Romans 12:8
Activity
Suggest any four traditional ways of restoring peace
Lesson 4
Unit : peace
Lesson content: Peacemaking in the bible
God promised peace to those who believe in him. In order to have
peace of God we must have faith in him and his son Jesus Christ
The bible names many ways of making peace with God e.g. in Leviticus
2:3 – 20 God gave us several promises
God tells us that if we live according to his laws and commandments he
would do the following
1. Make us live safely in our land
2. Give us peace in our land
3. Enable us worship without being afraid of anyone
4. Stop all wars
5. Make us prosperous
Jesus make the following suggestions towards peace making
a) Do not revenge one someone who does wrong to you
b) When someone asks for something from you, give it to him
c) Love your enemies and pray for them
d) Also St. Paul in his letter to the Corinthians 13:13 says that we
need faith hope and love
Prayer: “Help me lord to use the different ways of making peace
basing on the bible Amen
Activity
1. To whom did God promise peace
2. What did God promise to those who love according to his laws
3. Mention four different groups of people who keep peace in a
community
4. Mention four different ways how good Christians help police to
keep law , peace and order in a community
5. Give four ways how police keep law and order in a community
COLLECTED, PRINTED & MARKETED BY ACOSMA EDUCATIONAL SERVICES (0752614244 ) Page 29
Lesson 5
Unit : peace
Lesson content ” Different ways of having peace in the bible
The bible gives us the following ways of having peace
To obey God’s commandments
To help the needy
To be patient with people who demand things from us
To love one another
Not to be offended by people’s acts
Verse to remember: “Love never gives up and its faith, hope and
patience never fails (Corinthians 13:7
Response to God’s message
“I will make every effort to make peace with my neighbor
Activity
1. What is the greatest thing one should have in order to have peace
2. State any three-peaceful way of solving problems
Lesson 6
Unit : the birth of the prince of peace
Lesson content: Problems that disturbed peace
Jesus Christ the son of God came to bring peace in the world
There are many things that can disturb peace
There are many wars between nations even before the coming of Jesus
Christ and after his coming
Problems of war
Wars can cause death
Wars can cause destruction of property and hatred
There are also other problems that always disturb peace in our society
e.g. unselfishness, hatred, injustice, tribalism, greed, malice
Where there is no peace, people cannot trust one another
Activity
1. How do you promote peace at your school?
2. What are some of the things that disturb peace
COLLECTED, PRINTED & MARKETED BY ACOSMA EDUCATIONAL SERVICES (0752614244 ) Page 30
Lesson 7
Unit : The birth of Jesus the prince of peace
Lesson content: God’s promised peace and how it comes about
</passage>

<passage id="lchk_63c6785e0506463cb16d106bdc5e9e45" source="Kesk P4 RE Workbook" part="61">
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

<passage id="lchk_3c95ad41c97e4b73a30793648397ab72" source="Kesk P4 RE Workbook 1" part="60">
A product of Kolfram Educational Services Kampala 0777886622/ 0786941943/ 0756821512/ 0784044408 82
For quality and improved learning materials, always use Kolfram Educational Services products
In Luke 12:22 – 23 Jesus Assured us that God will always solve our problems because he
know them.
In Psalms 40:12 – 17 the writer asks God to help him overcome his problems with faith
Verse to remember: “Instead look for the kingdom and he will provide you with these
things Luke 12:31
Prayer: “Oh God help us at all times to seek and promote peace and comfort from you
Amen”
Response to the message
“I will seek peace from God”
ACTIVITY
1. Ho w can we look for God’s peace ?
i)_______________________________________________________________________________
ii) ______________________________________________________________________________
2. What did Jesus leave his disciples with?
i)_______________________________________________________________________________
ii) ______________________________________________________________________________
3. What can we do in order to promote peace?
i)_______________________________________________________________________________
ii) ______________________________________________________________________________
LESSON
Reconciliation
Reconciliation is the restoration of broken relationship between two or more disagreeing
parties.
Reconciling means bringing back a broken relationship
Causes of misunderstandings
1. Adultery
2. Back biting
3. Greed
4. False accusation
5. Suspicion of witchcraft.
Importance of reconciliation
1. It restores friendship and love
2. It restores personal communications.
3. Prevents bitterness and revenge.
4. Working together is restored.
5. Misunderstandings are easily corrected
6. Promotes peace and harmony
ACTIVITY
1. Define the term reconciliation.
_________________________________________________________________________
_________________________________________________________________________
2. State any two causes of misunderstandings.
i)_______________________________________________________________________________
ii) ______________________________________________________________________________
3. Suggest any two ways of reconciling among people.
i)_______________________________________________________________________________
ii) ______________________________________________________________________________
4. Mention any two importance of reconciliation.
i)_______________________________________________________________________________
ii) ______________________________________________________________________________
LESSON
STANDARD KOLFRAM IN USE: ABRIDGED CURRICULUM P.4 CHRISTIAN RELIGIOUS EDUCATION WORKBOOK
A product of Kolfram Educational Services Kampala 0777886622/ 0786941943/ 0756821512/ 0784044408 83
For quality and improved learning materials, always use Kolfram Educational Services products
Traditional ways of reconciliation
1. Arbitration
2. Using mediators like elders, chiefs and clan heads.
3. Shaking hands
4. Paying fines
5. Apologizing
6. Sharing meals.
Traditional ways of reconciling with God
Sacrificing animals to God
Process/steps involved in traditional reconciliation
1. Identifying a conflict.
2. Informing elders in the community.
3. Elders talk to people involved the conflict.
4. Asking people who know anything about the conflict.
5. Giving people in the conflict to explain.
6. Members present may give advice or ask questions.
</passage>
</passages>

---

## Answer format (Ledgerly Resources Bank)

Ignore the 'Reply with ONE JSON object' and 'Reply shape' lines above: answer as a FOLDER in `jobs/outbox/<job>/`,
exactly as `AGENT.md` and `README.md` describe (notes `.md`, plan and activities `.json`, `figures/`, `meta.json`),
then run `python3 tools/check.py <job>`. The field meanings above still apply. Nothing may be invented: every
note section, example, activity and classroom activity cites a passage with an exact quote.
