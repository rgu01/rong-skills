---
id: backeman2023aisola-formal-models-chatgpt
title: "Studying Formal Models Using ChatGPT"
authors:
  - Peter Backeman
  - Rong Gu
  - Florian Lorber
affiliation:
  - Mälardalen University, Sweden (Backeman, Gu)
  - Silicon Austria Labs, Austria (Lorber)
year: 2023
venue: AISoLA'23
venue_source: author's publications page (the PDF does not name the venue)
doi: null
document_type: conference paper
pages_in_pdf: 19
pdf_url: https://drive.google.com/file/d/1jGrIsesQzMG_E_j7MpM3PfCpQBxgOa_-/view?usp=sharing
listing_url: https://sites.google.com/view/ronggu/publications
author_keywords: [LLM, ChatGPT, formal models]
topics: [large language models, formal methods, model explanation, model checking, SMT, interactive theorem proving, formal methods education, prompt engineering, LLM evaluation]
formalisms: [timed automata, TCTL, SMT-LIB, Coq proofs]
tools: [ChatGPT 3.5, Copilot, UPPAAL, UPPAAL 5.0, Z3, Coq]
llms: [ChatGPT 3.5, Copilot (version not stated)]
application: explaining and building formal models; teaching UPPAAL to master students
abbreviations: {LLM: large language model, GPT: generative pre-trained transformer, SMT: satisfiability modulo theories, UTA: UPPAAL timed automata, TA: timed automata, QF_LIA: quantifier-free linear integer arithmetic, NL: natural language, RQ: research question}
funding: Vinnova Advanced digitalization programme, project D-RODS (ID 2023-00244); Swedish Knowledge Foundation, PerFlex project, grant 20220033; Swedish Knowledge Foundation, synergy project ACICS, grant 20190038
---

# Studying Formal Models Using ChatGPT (Backeman, Gu, and Lorber, AISoLA 2023)

## At a glance

This 2023 paper by Backeman, Gu, and Lorber asks whether large language
models (LLMs) can explain existing formal models and help to build new
ones. It tests ChatGPT 3.5 on four small models: a UPPAAL train-gate model,
a new UPPAAL vending machine, an SMT pigeonhole benchmark, and a Coq proof.
It also asks ChatGPT 3.5 and Copilot for SMT-LIB formulas for 16 simple
properties. Copilot gives far better formulas than ChatGPT. A class
experiment with master students shows that ChatGPT helps with syntax,
simple queries, and model structure, but not with complex behaviour. Its
answers are inconsistent. The authors call all results "very preliminary".

Page references `[p. N]` point to the 19-page PDF.

## Key facts

Each fact is a claim from the paper unless it is marked otherwise.

- The ChatGPT formal-models paper uses ChatGPT version 3.5 and Copilot. It
  does not state the Copilot version. [p. 2–3]
- The ChatGPT formal-models paper asks four research questions:
  interpretation, modelling assistance, generalisation, and building
  blocks. [p. 6–7]
- On the UPPAAL train-gate model (about 400 lines), ChatGPT 3.5 correctly
  calls the train-crossing query a liveness property and explains its
  intent well. [p. 7–8]
- On a new vending-machine model that is not on the Internet, ChatGPT 3.5
  finds the purpose of the model. With extra help, it finds a flaw in the
  payment logic and a fix. [p. 8–9]
- On the vending machine, ChatGPT 3.5 writes one correct UPPAAL query. Its
  more complex queries are wrong and not even syntactically valid. [p. 9]
- On the SMT pigeonhole benchmark (about 350 lines), ChatGPT 3.5 explains
  the constraints and says "unsat" correctly. It states the grid size as
  11x11 instead of 11 rows and 10 columns. [p. 9–10]
- ChatGPT 3.5 rewrites a Coq proof that negation is involutive into short
  plain mathematics after the follow-up prompt "A bit shorter please."
  [p. 10]
- For 16 SMT-LIB building-block queries, Copilot with the simple prompt
  scores 12 of 16 perfect on semantics. ChatGPT 3.5 with the simple prompt
  scores 4 of 16. [p. 12]
- With the simple prompt, ChatGPT 3.5 gives a completely wrong semantic
  answer, or no formula, for 5 of 16 queries. Copilot gives none. [p. 12]
- A longer "extended" prompt does not help Copilot and sometimes makes its
  answers worse. For ChatGPT 3.5 it helps overall. [p. 13–14]
- One Copilot error is a declared linear logic for a nonlinear formula. The
  paper says this gives an erroneous formula "which can provide false
  answers". [p. 13]
- In the student experiment, 21 of 30 students finished the UPPAAL
  assignment and 6 of them used ChatGPT. [p. 15]
- The assignment finishing rate rose from 65% to 70% against earlier
  semesters. The authors say the link to ChatGPT use is not clear. [p. 15]
- All 6 ChatGPT users needed more than the 1 to 4 prompts that the authors
  expected before they got meaningful answers. [p. 16]
- The students rated ChatGPT 3 to 6 for model building and 7 to 10 for
  query writing, out of 10. [p. 16]
- The authors conclude that ChatGPT is not a good learning tool, because
  its answers are not consistent. It only assists people who already know
  the modelling tool. [p. 16–17]
- The authors asked each query only once. They name LLM non-determinism and
  tool updates as threats to validity. [p. 18]

## Questions this paper answers

**Can ChatGPT explain a formal model?** For the general idea and the
syntax, yes, in these small cases. For deeper semantics, such as whether a
system can deadlock, no. [p. 17]

**Does it work on a model that it has never seen?** Yes, when the variable
names are descriptive. When all transitions have single-letter labels, it
gives only syntactic information. [p. 17]

**Can it help to change a model?** It finds and fixes small logical
inconsistencies and makes small changes, such as a new drink. Larger
changes fail and are sometimes not even syntactically correct. [p. 17]

**Can it write SMT formulas?** Copilot often gives formulas that can be
used directly. ChatGPT 3.5 is much weaker and sometimes gives no formula.
[p. 13–14, p. 18]

**Does a longer prompt with background help?** Not for Copilot. For ChatGPT
3.5, sometimes better and sometimes worse, with a better result overall.
[p. 13–14]

**Does ChatGPT help students learn UPPAAL?** It helps with basic mistakes,
simple queries, and the template structure. It does not help with complex
behaviour, such as message loss. [p. 16]

## Scope: what this paper does not do

- It does not use GPT-4. The experiments use ChatGPT 3.5 and Copilot only.
  [p. 2–3]
- It does not train or fine-tune an LLM on formal models. The authors name
  that as future work. [p. 6]
- It does not repeat any query, so it measures no variance. [p. 18]
- It does not run the generated SMT formulas in a solver in the reported
  text. The scores are the authors' grades.
- It does not compare the students who used ChatGPT with the control group
  on grades or on time.
- It does not interview the students. [p. 16]
- It does not test the semantically equivalent transformations (renamed
  variables, moved sections) that it proposes for RQ3. That is future work.
  [p. 7, p. 18]
- It names no DOI and no venue inside the PDF.

## Research questions

| RQ | Name | Question as stated on p. 6–7 |
|---|---|---|
| RQ1 | Interpretation and explanation | To what extent can LLMs interpret and explain formal models of different verification techniques in natural language? |
| RQ2 | Assistance for modelling | Can LLMs help to develop a formal model by modifying existing parts or adding new parts? |
| RQ3 | Generalisation | How do LLMs perform on models that are not in the training data? |
| RQ4 | Bottom-up assistance | Can LLMs give building blocks for formal models, with syntactically and semantically correct formulas for simple properties? |

The paper names four scenarios that motivate model explanation: legacy
systems with poor documentation, new team members, fast documentation in
agile work, and third-party testers. [p. 6]

## Formal methods in the study

| Branch | Tool or format | Model used |
|---|---|---|
| Model checking | UPPAAL timed automata (XML file) | Train gate from UPPAAL 5.0; a handcrafted vending machine |
| SMT solving | SMT-LIB, for example for Z3 | Pigeonhole benchmark `QF_LIA/pidgeons/pigeon-hole-10.smt2`; 16 building-block queries |
| Interactive theorem proving | Coq | Proof of `negb_involutive` |

Source: Sections 2.2 and 4. [p. 3–5, p. 7–10]

The authors expect ChatGPT 3.5 to read formal models at the syntactic level
but not to understand their full semantics. They note that UPPAAL XML files
contain comments, which may help. [p. 4]

## Use cases: explaining existing models (RQ1 to RQ3)

### Train gate (UPPAAL)

- **Input.** The whole train-gate model, about 400 lines. [p. 7]
- **Prompts.** "What does this model do?", then "Could you explain this
  query in more depth?" about the query that an approaching train
  eventually crosses the bridge. [p. 7]
- **What worked.** ChatGPT 3.5 calls the query a liveness property. It
  explains that every `Train(i).Appr` leads to `Train(i).Cross`, so no
  train stays stuck in the approach state. The authors call this "a very
  good explanation" of the intuition. [p. 8]
- **Caveat.** The model ships with UPPAAL and is likely in the training
  data. [p. 7]

### Vending machine (UPPAAL, new model)

- **Input.** A small handcrafted model that sells drinks at different
  prices, paid in cash or by card. The model is not on the Internet. The
  paper links one shared conversation. [p. 8–9]
- **Prompts.** Questions about syntax, semantics, and improvements. The
  paper does not print them. [p. 9]
- **What worked.** ChatGPT 3.5 finds the purpose of the model. With extra
  help, it finds a flaw in the payment system and a fix. The conclusion says
  that the flaw was a drink price that differed between an update and a
  guard. It also adds a new drink correctly. [p. 9, p. 17]
- **What failed.** It writes one correct query. More complex queries are
  wrong and do not match the UPPAAL query syntax. Larger modifications
  fail. [p. 9, p. 17]
- **Naming effect.** With single-letter transition labels, it gives only
  syntactic information. [p. 17]

### Pigeonhole (SMT-LIB)

- **Input.** The SMT-LIB benchmark asks whether a grid of 11 rows and 10
  columns can have at least one pigeon per row and at most one per column.
  The answer is no. The instance has about 350 lines. [p. 9]
- **Prompts.** "Can you explain the intuition behind the following SMT
  formula: ...", then "Do you think it is satisfiable?" [p. 9]
- **What worked.** It describes the row and column constraints correctly
  and concludes "unsat". [p. 9–10]
- **What failed.** It calls the grid "11x11". The authors say that this
  mistake makes the whole reasoning "confusing and faulty". [p. 9–10]

### Negation is involutive (Coq)

- **Input.** The lemma `negb_involutive : forall b:bool, negb (negb b) = b`
  and its proof. [p. 5, p. 10]
- **Prompts.** "Can you explain the provided proof using standard
  mathematical notation?", then "A bit shorter please." [p. 10]
- **What worked.** The answer is a short case analysis on `true` and
  `false`, with no Coq syntax left. The authors find it easy to understand.
  [p. 10]

## Building blocks: SMT formulas (RQ4)

### Prompts

Each query starts with "Give me an SMT formula which is true if ...". Each
query runs in a new conversation, in two forms. [p. 11–12]

- **Simple:** "Give me an SMT formula which is true if x is a prime
  number."
- **Extended:** a fixed background paragraph first. It explains SMT, says
  that the formula must be in SMT-lib syntax, and says that an integer must
  be called `x`. Then the same final sentence. [p. 12]

The authors tried the extended form because, in preliminary tests, more
background sometimes gave better answers, although it adds no real
information. [p. 11–12]

### The 16 queries

| Category | Query | Property ("... true if ...") |
|---|---|---|
| Numbers | prime | x is a prime number |
| | square | an integer is a perfect square number |
| | positive | `f(x) = x*x - x + x` is always positive |
| | trianglenum | a number is a triangle number |
| Geometry | overlap | one rectangle overlaps another rectangle |
| | area | a rectangle has an area larger than its circumference |
| | rightangle | a triangle has a right angle |
| | point | a given point lies within a given circle |
| Lists | largest | a given integer is the largest integer in a list |
| | sorted | a list is sorted |
| | equallists | two lists contain the same elements |
| | notcontain | a list does not contain a given integer |
| Strings | palindrome | a string is a palindrome |
| | even-a | a string contains an even number of occurrences of the letter a |
| | lex-between | one string is lexicographically between two other strings |
| | regex | a string matches the regular expression `(ab)*` |

Source: Table 3 of the paper. [p. 11]

### Grading scale

| Points | Grade | Meaning |
|---|---|---|
| 0 | None | No formula, or very wrong |
| 1 | A bit | Has some fundamental structure; at least in the correct domain |
| 2 | Almost | Close to fully correct, for example a typo or `<` instead of `>` |
| 3 | Perfect | Fully correct; usable with no change |

Each answer gets three grades: semantics (does it express the property),
syntax (can it be used by copy and paste), and explanation (comments and
text). Source: Table 2 and p. 11. [p. 11]

### Results per query

Sem. = semantics, Syn. = syntax, Expl. = explanation.

| Query | Copilot simple (Sem/Syn/Expl) | Copilot extended | ChatGPT simple | ChatGPT extended |
|---|---|---|---|---|
| prime | 3/3/3 | 3/3/3 | 3/1/3 | 1/1/2 |
| square | 3/3/3 | 2/3/3 | 0/0/1 | 3/3/3 |
| positive | 3/3/2 | 2/3/3 | 1/3/1 | 1/3/3 |
| trianglenum | 3/3/3 | 2/2/3 | 0/0/0 | 3/2/3 |
| overlap | 3/3/3 | 3/3/3 | 3/3/3 | 1/3/1 |
| area | 3/3/3 | 3/2/3 | 3/0/3 | 3/3/3 |
| rightangle | 3/3/3 | 3/2/3 | 2/3/2 | 1/3/2 |
| point | 3/2/3 | 3/3/3 | 0/0/1 | 3/3/3 |
| largest | 1/3/3 | 3/3/3 | 1/1/1 | 1/2/3 |
| sorted | 3/3/3 | 3/3/3 | 3/3/3 | 3/2/2 |
| equallists | 3/3/1 | 3/3/3 | 1/3/2 | 1/3/2 |
| notcontain | 2/2/3 | 3/3/3 | 1/1/2 | 3/3/3 |
| palindrome | 1/3/3 | 1/3/3 | 0/2/1 | 3/2/3 |
| even-a | 2/2/3 | 1/2/1 | 1/3/1 | 1/1/3 |
| lex-between | 3/3/3 | 3/3/3 | 0/0/0 | 1/3/1 |
| regex | 3/3/3 | 3/2/3 | 1/1/1 | 0/0/0 |

Source: Table 4 of the paper. [p. 12]

### Grade counts (out of 16 queries)

| Grade | Copilot simple (Sem/Syn/Expl) | Copilot extended | ChatGPT simple | ChatGPT extended |
|---|---|---|---|---|
| Perfect | 12/13/14 | 11/11/15 | 4/6/4 | 7/9/9 |
| Almost | 2/3/1 | 3/5/0 | 1/1/3 | 0/4/4 |
| A bit | 2/0/1 | 2/0/1 | 6/4/7 | 8/2/2 |
| None | 0/0/0 | 0/0/0 | 5/5/2 | 1/1/1 |

Source: the "Sum" rows of Table 4. [p. 12]

### What worked and what failed

- **Copilot, trianglenum.** It defines `isTriangle` with an existential
  `n >= 0` and `x = n(n+1)/2`. [p. 13]
- **Copilot, rightangle.** It declares three positive reals and asserts the
  Pythagorean theorem, with clear comments. [p. 13]
- **Copilot errors with the extended prompt.** [p. 13]
  - It is confused that an integer must be part of the answer.
  - It renames a variable to `x` in the declaration but not in the formula.
  - It adds a `set-logic` line for linear arithmetic in square and
    positive, although the formula is nonlinear. The formula is then wrong
    and "can provide false answers".
- **ChatGPT, missing formulas.** For trianglenum and regex, it sometimes
  gives no SMT formula at all. [p. 14]
- **ChatGPT, palindrome (extended).** The recursive function is correct,
  but it uses `define-fun` where SMT-LIB needs `define-fun-rec`. Otherwise
  the paper calls the answer perfect. [p. 14]
- **Copilot, palindrome.** With the simple prompt, it says that the task is
  impossible and gives an answer for strings of length four only. With the
  extended prompt, it uses `str.reverse`, which is not in SMT-LIB. [p. 14]
- **Summary by the authors.** Copilot gives a perfect answer in 9 of 16
  cases and an almost perfect answer in 14 of 16 cases. [p. 14]

### Error types seen in the LLM outputs

This list collects the error types that the paper reports. [p. 9–10,
p. 13–14, p. 16]

| Error type | Example from the paper |
|---|---|
| No formula at all | ChatGPT on trianglenum and regex |
| Wrong fact inside correct reasoning | Pigeonhole grid "11x11" instead of 11 by 10 |
| Invented function | `str.reverse` (Copilot) |
| Wrong keyword | `define-fun` for a recursive function (ChatGPT) |
| Wrong logic declaration | Linear logic declared for a nonlinear formula (Copilot) |
| Inconsistent renaming | Variable renamed to `x` in the declaration only (Copilot) |
| Over-restriction | Palindrome only for length four (Copilot) |
| Invalid query syntax | Complex UPPAAL queries for the vending machine (ChatGPT) |
| Inconsistent names | Variable names differ inside one answer (students' report on ChatGPT) |

## Student experiment and survey

### Design

- **Participants.** Master students in computer science in the course
  Embedded Systems II at Mälardalen University. They know UML and
  programming but no formal methods except discrete mathematics. [p. 14–15]
- **Task.** Build a UPPAAL timed-automata model of data communication and
  write (timed) CTL properties, for example absence of deadlock. [p. 15]
- **Preparation.** A four-hour lecture on modelling real-time systems as
  timed automata in UPPAAL. [p. 15]
- **Groups.** A control group without ChatGPT, and an experimental group
  that may use ChatGPT as much as it wants. [p. 15]
- **Hypothesis.** ChatGPT helps the students to some extent but cannot give
  them the correct answers directly. [p. 15]
- **Prompt aid.** The assignment text gave an example prompt. The authors
  tried it and expected 1 to 4 prompts to be enough for ChatGPT to learn
  the UPPAAL format. [p. 16]

### Survey questions

| ID | Question | Answer type |
|---|---|---|
| A | How much did you know UPPAAL before the lecture? | 0–10 |
| B | After the lecture, how would you evaluate your knowledge about UPPAAL? | 0–10 |
| C | What is your biggest question about UPPAAL before doing the assignment? | Text |
| D | Has your biggest question been answered by ChatGPT? | Options |
| E | How many prompts have you used to tune your ChatGPT? | Options |
| F | How many questions have you asked ChatGPT? | Options |
| G | Give an example of a helpful answer from ChatGPT. | Text |
| H | Give an example of a useless/wrong answer from ChatGPT. | Text |
| I | How would you evaluate ChatGPT's answers for building the model? | 0–10 |
| J | How would you evaluate ChatGPT's answers for formulating the temporal logic properties? | 0–10 |
| K | What else experience would you like to share about using ChatGPT for modelling? | Text |

Source: Table 5 of the paper. [p. 15]

### Results

| Item | Result |
|---|---|
| Students in the course | 30 [p. 15] |
| Students who finished | 21 [p. 15] |
| Students who used ChatGPT | 6 [p. 15] |
| Finishing rate | 65% in earlier semesters, 70% now; link to ChatGPT not clear [p. 15] |
| Q A (before lecture) | 5 students rated 0, 1 student rated 1 [p. 16] |
| Q B (after lecture) | 5 students rated 3–6, 1 student rated 8 [p. 16] |
| Q C and D | Most questions were about modelling, one about queries; 3 students got answers from ChatGPT [p. 16] |
| Q E (prompts) | 2 used 3–5, 2 used 6–9, 2 used more than 10 [p. 16] |
| Q F (questions) | 2 asked 4–6, 4 asked more than 10 [p. 16] |
| Q I (model building) | Mostly 3–6 [p. 16] |
| Q J (queries) | 7–10 [p. 16] |

- **Helpful answers (Q G).** The number of templates, removal of syntax
  errors, and simple model-independent queries such as `A[] not deadlock`.
  [p. 16]
- **Useless answers (Q H).** Details of modelling, such as how to model
  message loss in a network protocol. Students had to read the UPPAAL
  manual and design the model themselves. [p. 16]
- **Why queries scored higher.** One required query, `A[] not deadlock`,
  does not depend on the model, and queries are much shorter than models.
  [p. 16]
- **Free text (Q K).** ChatGPT is good at the structure of a model, such as
  the split into templates, but it is not a reliable source. Variable names
  change from place to place in the same answer. [p. 16]

## Answers to the research questions, as stated by the authors

| RQ | Answer [p. 17–18] |
|---|---|
| RQ1 | ChatGPT shows "surprising potential" for the general idea and the syntactic elements of a model. Deeper questions, such as deadlock, are "naturally out of its scope". |
| RQ2 | It detects and fixes some logical inconsistencies and makes small correct changes. Larger changes fail and sometimes lack correct syntax. |
| RQ3 | It explains new models when the names are descriptive. With single-letter labels, it gives only syntactic information. |
| RQ4 | LLMs give simple SMT parts, sometimes perfect. Copilot is stronger and more consistent than ChatGPT 3.5. More than half of the experiments give a formula that can be used directly. |

## Threats to validity stated by the authors

- Each query ran once. Generative AI can give a different answer each time.
  [p. 18]
- The tools change over time, which can change the results. [p. 18]
- An LLM can learn from repeated questions about the same model, which
  makes repeated tests hard to compare. [p. 18]

## Future work stated by the authors

- RQ1: a systematic study with more models. [p. 18]
- RQ2: ask for extensions and modifications of the models. [p. 18]
- RQ3: apply semantically equivalent syntactic transformations and compare
  the explanations. [p. 18]
- RQ4: study the consistency of the tools. [p. 18]
- Train LLMs specifically on formal models. [p. 6]
- Interview the students about their prompt counts. [p. 16]

## Related work, as the paper positions itself

- Earlier work uses LLMs to generate formal models from natural language,
  such as temporal logic (NL2LTL, NL2TL) and automata. [p. 1]
- This paper looks in the opposite direction: from an existing formal model
  to an explanation, and to flaw detection. The authors say few studies do
  this. [p. 2]
- Most work on machine learning and formal methods targets either
  guarantees for ML or ML-based generation. The paper targets the knowledge
  gap between practitioners and researchers. [p. 6]

## Reviewer notes

These notes are a reading of the paper, not claims from it.

- **Scale.** Four explanation cases and 16 one-shot SMT queries per
  configuration. The evidence is anecdotal, as the authors also say ("very
  preliminary"). [p. 17]
- **Grading.** The authors grade semantics by hand. The paper does not say
  that the formulas ran in a solver, and it does not report how many
  graders took part.
- **Training-data contamination.** The train gate ships with UPPAAL, the
  pigeonhole file is a public benchmark, and the Coq proof is a standard
  Coq example (p. 10). Only the vending machine is new. RQ3 rests on that
  one model.
- **Semantic risk of "Almost".** An "Almost" answer can be one operator
  wrong. An SMT formula with a wrong operator still runs and gives a
  confident wrong answer. The Copilot logic-declaration error shows this
  risk. For requirement fidelity, a near-correct formula is not safe to use
  without review.
- **Copilot summary.** "9 of 16 perfect" matches the Copilot simple column
  (all three grades 3). "14 of 16 almost perfect" matches the Copilot
  extended column (all grades 2 or more), not the simple column, which
  gives 13. The text does not say which column it means. (Counts by the
  reviewer from Table 4.)
- **"A single instance".** The text says ChatGPT scores higher than Copilot
  only once (palindrome). Table 4 also shows ChatGPT simple with syntax 3
  on even-a, against 2 for both Copilot columns. [p. 12, p. 14]
- **Inconsistencies.** The abstract says three research questions; the
  paper defines four (p. 1, p. 6–7). The conclusion says "three use case
  studies"; Section 4 has four (p. 7–10, p. 17). The RQ3 text differs
  between p. 7 and p. 17. Table 1 says GPT-3, while the text says GPT-3.5
  (p. 7). The weights in Table 1 add up to 101%.
- **Student experiment.** Only 6 students used ChatGPT, and the paper
  reports no comparison with the control group. The 65% to 70% change uses
  different cohorts. 21 of 30 is 70%, so the rate counts all students.
- **What "explains" means.** The good explanations restate the query and
  the names in the model. The paper reports no case where ChatGPT explains
  state-space behaviour that the text of the model does not show.
- **AI aspect.** The paper is an early (2023) look at LLMs as explainers
  of formal artefacts. Its main lessons are that names in a model drive the
  quality of the explanation, that answers are not consistent between runs,
  and that a code-tuned assistant (Copilot) writes better formulas than a
  general chat model (ChatGPT 3.5).

## Terms

| Term | Meaning in this paper |
|---|---|
| LLM | Large language model, a neural model trained on large text data that generates text |
| ChatGPT 3.5 | OpenAI's chat model based on GPT-3.5, used in all explanation tests |
| Copilot | An AI assistant used only in the SMT building-block test; the paper does not give its version |
| Prompt | The text input to the LLM; it can hold a whole model and earlier turns |
| Simple / extended prompt | One-sentence request / the same request after a fixed background paragraph |
| Building block | A small formula for one property that can go into a larger model |
| UPPAAL | A model checker for networks of timed automata; models are XML files |
| Timed automata | State machines with real-valued clocks |
| Liveness property | A property that something good eventually happens |
| SMT | Satisfiability modulo theories: decide if a formula over typed variables has a model |
| SMT-LIB | The standard input format for SMT solvers |
| QF_LIA | Quantifier-free linear integer arithmetic, an SMT-LIB logic |
| `define-fun-rec` | The SMT-LIB command for a recursive function definition |
| Coq | An interactive theorem prover that checks proofs |
| Involutive | Applying the function twice gives the input back |
| Pigeonhole principle | If n items go into m containers and n > m, one container has two items |

## Citation

Peter Backeman, Rong Gu, and Florian Lorber. "Studying Formal Models Using
ChatGPT." AISoLA'23, 2023.
