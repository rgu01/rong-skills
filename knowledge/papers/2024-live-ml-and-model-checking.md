---
id: gu2024live-ml-and-model-checking
title: "Integrating the Power of Machine Learning and Model Checking in Safety-Critical Systems"
authors:
  - Rong Gu
affiliation: Mälardalen University, Västerås, Sweden
year: 2024
venue: LiVe'24
venue_source: author's publications page (the PDF does not name the venue)
doi: null
document_type: short position paper (extended abstract)
pages_in_pdf: 2
pdf_url: https://drive.google.com/file/d/1_HqnmYyZhPLC_y08KSmeYdLPVus5p2_l/view?usp=sharing
listing_url: https://sites.google.com/view/ronggu/publications
author_keywords: []
topics: [machine learning, model checking, safety-critical systems, controller synthesis, reinforcement learning, autonomous systems, security, timing requirements, requirement ambiguity, large language models]
formalisms: [timed automata, Markov decision process, Timed Rebeca]
tools: [UPPAAL, TAMAA, MCRL, MoCReL, Timed Rebeca]
algorithms: [reinforcement learning, Guess-and-then-Check, strategy compression]
application: autonomous agents with reach-avoid missions; timing requirements of real-time systems
abbreviations: {MC: model checking, ML: machine learning, TAMAA: UPPAAL-based Mission Planning for Autonomous Agents, MCRL: Model Checking + Reinforcement Learning, MoCReL: Model-checked Compressed Reinforcement Learning, TRebeca: Timed Reactive Objects Language, MDP: Markov decision process, LLM: large language model}
funding: null
---

# Integrating the Power of Machine Learning and Model Checking in Safety-Critical Systems (Gu, LiVe 2024)

## At a glance

This 2-page paper by Rong Gu, from 2024, argues that machine learning (ML)
can remove barriers to model checking (MC) in safety-critical systems,
such as poor scalability and hard formalisms. It summarises a line of the
author's work on controller synthesis: TAMAA, MCRL, MoCReL, and a
Guess-and-then-Check algorithm on Timed Rebeca. It also describes a
conceptual framework, still under development, that uses an LLM to find
ambiguities in timing requirements and MC to find inconsistencies. The
paper has no new experiments.

Page references `[p. N]` point to the 2-page PDF.

## Key facts

Each fact is a claim from the paper unless it is marked otherwise.

- The ML-and-MC paper names scalability and the difficulty of learning
  formalisms as barriers to industrial use of model checking. [p. 1]
- TAMAA uses UPPAAL model checking to generate controllers that satisfy a
  reach-avoid property in an environment with only static obstacles. [p. 1]
- With more than five agents, UPPAAL runs out of memory on the TAMAA model,
  because the state space is too large. [p. 1]
- MCRL learns a controller by reinforcement learning without a correctness
  guarantee. It then model-checks the result and repeats until the
  reach-avoid property holds. [p. 1]
- MoCReL also compresses the learned controller, so it needs much less
  memory and still satisfies the reach-avoid property. [p. 1]
- The Guess-and-then-Check algorithm models the system as a Markov decision
  process in Timed Rebeca and synthesises a controller in three phases.
  [p. 1–2]
- Guess-and-then-Check gives a controller that is safe after phase II and
  secure after phase III. [p. 2]
- The proposed requirements framework uses an LLM to detect ambiguity in
  textual requirements and MC to find counterexamples for inconsistent
  timing requirements. [p. 2]
- The author states that the requirements framework is under development
  with industrial partners. [p. 2]

## Questions this paper answers

**Why combine ML and MC?** MC gives rigorous analysis but scales badly and
is hard to learn. ML solves complex single-domain problems well, so it can
help with these barriers. [p. 1]

**How does learning keep a correctness guarantee?** Learning proposes a
controller, and model checking verifies it. The learned controller limits
the state space, so the check scales better. [p. 1–2]

**Where does an LLM come in?** In the planned requirements framework. The
LLM finds ambiguities, generates formal models from template-based text,
explains counterexamples, and proposes better requirement text. [p. 2]

## Scope: what this paper does not do

- It reports no new experiments, numbers, or case studies. The only result
  it states is the five-agent memory limit of TAMAA, from earlier work.
  [p. 1]
- It gives no evaluation of the LLM-based requirements framework. [p. 2]
- It does not define the safety or the security properties formally.
- It names no DOI and no venue inside the PDF.

## Line of work summarised

| Work | Method | Guarantee | Reference in the paper |
|---|---|---|---|
| TAMAA | UPPAAL model checking generates reach-avoid controllers; static obstacles only | Exhaustive model checking; memory runs out above five agents | [1] SAC 2020 |
| MCRL | Reinforcement learning, then model checking of the result, in a loop | Reach-avoid holds after the check passes | [2] FMICS 2020 |
| MoCReL | Like MCRL, plus compression of the learned controller | Reach-avoid kept after compression | [3] Science of Computer Programming 2022 |
| Guess-and-then-Check | MDP in Timed Rebeca; guided exploration, then two checks | Safety and security | [4] technical report, January 2024 |

Source: Section 2 and the reference list. [p. 1–2]

## Guess-and-then-Check algorithm

The algorithm splits the state-space exploration into three phases. [p. 2]

1. **Guess.** Explore all system transitions, so that no valid system
   action is missed. Explore environment transitions selectively, by an
   accumulated reward. A high reward leads fast to a state that ends the
   exploration, for example a state that violates safety.
2. **Check safety.** Check the guessed controller against a safety property
   with exhaustive exploration of the environment transitions. The guessed
   controller already restricts the state space, so this phase does not
   necessarily explode.
3. **Check security.** Check the safe controller against a security
   property. Prune the transitions that can reveal information to
   unauthorised intruders.

The author claims two benefits: the split alleviates state-space explosion,
and learning stops exploration early on branches that are "doomed to
fail". [p. 2]

## Planned framework for timing requirements

- **Ambiguity** means that one requirement has several interpretations.
  [p. 2]
- **Consistency** means that a model exists that satisfies all timing
  requirements. [p. 2]
- The LLM detects ambiguities in textual requirements. [p. 2]
- MC finds counterexamples that cause inconsistencies. [p. 2]
- The requirements follow templates. The author expects that, "given a
  proper amount of prompting", the LLM can generate formal models from the
  text directly. [p. 2]
- The LLM can also explain counterexamples and propose improved requirement
  text. [p. 2]

## Reviewer notes

These notes are a reading of the paper, not claims from it.

- **Position paper.** The paper is a summary of earlier work plus a plan.
  Its claims about the LLM framework, for example that it "would be
  state-of-the-art", are expectations, not results. [p. 2]
- **Guarantee pattern.** In MCRL, MoCReL, and Guess-and-then-Check, the
  learner only proposes and the model checker decides. The guarantee is
  therefore as strong as the model and the checked property, not stronger.
- **Requirement fidelity.** In the planned framework, an LLM writes the
  formal model from text. Nothing in the paper says how the generated model
  is checked against the intent of the text. That step decides whether a
  later consistency result means anything.
- **Phase I completeness.** Phase I explores the environment selectively.
  Phase II then checks the environment exhaustively, so the safety result
  does not depend on the guess being complete.
- **AI aspect.** Two kinds of AI appear: reinforcement learning to guide
  state-space search, and an LLM for requirements text. Only the first has
  published results behind it in the references.

## Terms

| Term | Meaning in this paper |
|---|---|
| Model checking (MC) | Exhaustive exploration of a model's states to check a property |
| Reach-avoid property | The system reaches the destination within a time frame and avoids obstacles |
| Reinforcement learning | Learning a policy from rewards over simulated runs |
| State-space explosion | Fast growth of the number of states with model size, which exhausts memory |
| Markov decision process (MDP) | A model with choices and probabilistic outcomes |
| Timed Rebeca (TRebeca) | A modelling language for timed reactive objects; the paper expands it as "Timed Reactive Objects Language" |
| Controller compression | Removal of unneeded state-action pairs from a learned controller |
| Ambiguity | One requirement with several interpretations |
| Consistency | A model exists that satisfies all timing requirements |
| Counterexample | A run that shows why a property fails |

## Citation

Rong Gu. "Integrating the Power of Machine Learning and Model Checking in
Safety-Critical Systems." LiVe'24, 2024.
