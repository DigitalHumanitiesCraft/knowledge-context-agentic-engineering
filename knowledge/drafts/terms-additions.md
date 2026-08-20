# Additional Terms of the Teaching Line

Research draft extending `knowledge/drafts/term-references.md`. That document anchors eleven terms of the existing matrix; this one collects the terms that the authoritative texts of the teaching line use as load-bearing concepts and that the matrix does not yet carry. Nothing here is decided, and the file touches neither `knowledge/terms.md` nor the existing reference draft.

Four texts were mined in full. The CLARIAH-AT lecture notes (`workshops/2026-09-25-clariah-at/workshop-script.md`, final and operator-confirmed), the English master script (`script/master-script-en.md`, work in progress), the German Skriptum (`script/master-script-de.md`, working version July 2026) and the master deck export (`slides/master-deck-export-2026-08-20.txt`). Terms that appear once in passing were left out. Terms that carry a definition, a distinction the argument depends on, or a recurring role across sections were taken in.

## How to read an entry

Each entry gives the English canonical name as the scripts use it, the German equivalent, a working definition grounded in the scripts rather than in general usage, the section where the term does its work, and a literature anchor where a canonical source exists. The German equivalent is attested when the German Skriptum or the deck uses that wording; where neither does, the wording is marked as a proposal. A literature anchor that the scripts themselves cite is given plainly; an anchor added here because the concept has an obvious canonical source outside the corpus is marked as a proposed anchor. Where a term overlaps an existing matrix row, the relation is stated instead of a second definition.

Source labels are abbreviated. CLARIAH means the CLARIAH-AT lecture notes, Master EN the English master script, Skriptum DE the German master script, Deck the master deck export.

## 1 Understanding Large Language Models

### Applied Generative AI

- **German.** Angewandte Generative KI (attested through the working-group name in the CLARIAH footnote).
- **Working definition.** The application and adaptation of generative AI methods and systems to problems of a specific research domain, in the tradition of applied computer science, with the focus on integrating generative models into existing research practice rather than on developing foundation models.
- **Source.** CLARIAH, "Applied Generative AI for Research Data Workflows"; Master EN, same section.
- **Literature.** No external canonical source. The scripts anchor the term to the author's own framing and to the DHd working group Angewandte Generative KI in den Digitalen Geisteswissenschaften.
- **Relation.** Names the disciplinary frame inside which all four engineering layers of the matrix sit.

### Frontier Model

- **German.** Frontier-LLM (Deck).
- **Working definition.** A currently leading general-purpose model whose combination of multimodality, reasoning, coding, tool use and agentic capability the scripts treat as qualitatively relevant for computational research, without claiming that it is the appropriate choice for every task.
- **Source.** CLARIAH, "Applied Generative AI for Research Data Workflows" and "The Current LLM Capability Landscape"; Master EN, abstract and "Which Frontier Models and AI Technologies Do You Use?".
- **Literature.** Proposed anchor, Anderljung et al., "Frontier AI Regulation. Managing Emerging Risks to Public Safety," arXiv:2307.03718, 2023, for the received definition. The scripts anchor the moving reference point to the Artificial Analysis leaderboard instead.

### Capability Frontier

- **German.** Proposal, Leistungsgrenze aktueller Modelle. Neither German source carries a rendering.
- **Working definition.** The current outer edge of measurable model capability across reasoning, coding, agentic tasks, speed and cost, located through continuously updated comparisons rather than through a single benchmark score.
- **Source.** CLARIAH, "The Current LLM Capability Landscape" and "Frontier LLMs Asymmetrically Amplify Computational Research".
- **Literature.** Artificial Analysis LLM Leaderboard, https://artificialanalysis.ai/leaderboards/models; METR, Task-Completion Time Horizons of Frontier AI Models, https://metr.org/time-horizons.

### Asymmetric Amplification

- **German.** Asymmetrische Amplifikation (Deck, "asymmetrisch amplifiziert").
- **Working definition.** The thesis that frontier models strengthen existing human capability unevenly, most strongly where relevant knowledge is externalised, research objects are digitally represented, actions can be executed through software and the environment returns meaningful feedback.
- **Source.** CLARIAH, "Frontier LLMs Asymmetrically Amplify Computational Research"; Master EN, same section; Deck, thesis slide.
- **Literature.** Pollin, "Asymmetric Amplification. Why AI Does Not Automate Research, But Disruptively Amplifies Computer-Based Research Work," Digital Humanities Craft, 2026, https://dhcraft.org/excellence/blog/Asymmetric-Amplification/.
- **Relation.** The corpus-level thesis under which the whole capability block of module 1 is organised. It has no row in the matrix.

### Task-Completion Time Horizon

- **German.** Proposal, Aufgabenhorizont.
- **Working definition.** The duration of software tasks that an agent can complete at a specified success probability, used in the scripts as one capability signal among several and explicitly qualified as no general measure of research capability.
- **Source.** CLARIAH, "Frontier LLMs Asymmetrically Amplify Computational Research" with footnote 26; Master EN, same section.
- **Literature.** Kinniment et al., "Measuring AI Ability to Complete Long Tasks," arXiv:2503.14499, 2025; METR, https://metr.org/time-horizons.

### Jagged Capability (Jagged Alien Intelligence)

- **German.** Jagged Alien Intelligence, untranslated in the Deck slide title; the Skriptum has no rendering.
- **Working definition.** The observed capability profile in which a model performs extremely difficult tasks while failing on neighbouring tasks that appear simpler to a human observer, which blocks both naive extrapolation from single successes and dismissal from conspicuous failures.
- **Source.** CLARIAH, "LLMs as Jagged Alien 'Intelligences'" and the closing paragraphs of the amplification section; Master EN, same section; Deck.
- **Literature.** Dell'Acqua et al., "Navigating the Jagged Technological Frontier," *Organization Science* 37, no. 2, 2026, DOI 10.1287/orsc.2025.21838; Gans, "A Model of Artificial Jagged Intelligence," arXiv:2601.07573, 2026; Summerfield, *These Strange New Minds*, Viking, 2025.

### Large Language Model

- **German.** Large Language Model, used untranslated; the Skriptum adds the descriptive gloss probabilistisches Textsystem.
- **Working definition.** A neural network trained on large tokenised collections to estimate a probability distribution over the next token given the tokens in its context, whose output stays probabilistic across repeated runs of the same input.
- **Source.** Master EN, "How Large Language Models Work"; Skriptum DE, §2.1.
- **Literature.** Brown et al., "Language Models are Few-Shot Learners," arXiv:2005.14165, 2020; Vaswani et al., "Attention Is All You Need," arXiv:1706.03762, 2017.

### Next Token Prediction

- **German.** Next Token Prediction, untranslated (Skriptum DE, §2.1 and footnote 1).
- **Working definition.** The training objective of autoregressive language modelling, which the scripts separate sharply from the capabilities acquired while optimising it, since the objective asks which continuation is probable rather than whether a proposition is true.
- **Source.** Master EN, "How Large Language Models Work"; Skriptum DE, §2.1 with footnote 1 marking the description as a functional simplification.
- **Literature.** Brown et al., arXiv:2005.14165, 2020. For the truth argument the scripts cite an interview with the proponent of Scientist AI, which is a spoken source rather than a citable paper.

### Transformer Architecture and Self-Attention

- **German.** Transformer-Modell (Skriptum DE, footnote 1); Transformer-Architektur is a proposal.
- **Working definition.** The layered architecture in which attention lets information at different positions of the sequence influence one another, so that a token receives a context-dependent representation rather than an isolated one.
- **Source.** Master EN, "Transformer Architecture"; Deck, context-window slide.
- **Literature.** Vaswani et al., arXiv:1706.03762, 2017.
- **Relation.** Carries the bridge the scripts need for module 3, that a prompt intervenes in the current computation because it changes the sequence the attention operates over.

### Token and Tokenization

- **German.** Token, Tokenisierung (Skriptum DE, §4.3).
- **Working definition.** The discrete units into which a tokenizer converts character sequences before they enter the network, with the consequence that context limits, input cost and output length are measured in tokens rather than in words.
- **Source.** Master EN, "Tokenization"; Skriptum DE, §4.3 in the path from file to context window.
- **Literature.** Sennrich, Haddow, Birch, "Neural Machine Translation of Rare Words with Subword Units," arXiv:1508.07909, 2016.

### Embedding and Contextual Representation

- **German.** Proposal, Embedding and kontextuelle Repräsentation. The Skriptum paraphrases as hochdimensionale numerische Repräsentationen (§3.6).
- **Working definition.** The mapping of discrete token identifiers into a high-dimensional vector space, and the repeated transformation of those initial vectors across the network into representations that depend on the surrounding tokens and the current task.
- **Source.** Master EN, "Embeddings and Contextual Representations"; Skriptum DE, §3.6.
- **Literature.** Vaswani et al., arXiv:1706.03762, 2017.
- **Relation.** Supplies the mechanism behind the claim that wording matters without assuming one fixed meaning per token, which module 2 then uses for prompt sensitivity.

### Pretraining

- **German.** Pre-Training (Skriptum DE, §2.2).
- **Working definition.** The training stage on large heterogeneous corpora that establishes broad linguistic, conceptual and procedural representations, described in the scripts as building a repertoire while noting that knowledge and capability stay entangled.
- **Source.** Master EN, "Pretraining and Posttraining" and "Training Builds and Shapes the Latent Program Space"; Skriptum DE, §2.2; CLARIAH, "Training Shapes the Latent Program Space".
- **Literature.** Brown et al., arXiv:2005.14165, 2020.

### Posttraining

- **German.** Post-Training (Skriptum DE, §2.2).
- **Working definition.** The training stages that shape how the learned repertoire is expressed in an assistant, through instruction tuning, demonstrations, preference learning, reinforcement learning and related methods, including interface capabilities such as tool calling.
- **Source.** Master EN, "Pretraining and Posttraining"; Skriptum DE, §2.2.
- **Literature.** Ouyang et al., "Training Language Models to Follow Instructions with Human Feedback," arXiv:2203.02155, 2022.

### Midtraining (Model Spec Midtraining)

- **German.** Proposal, Midtraining. Absent from both German sources.
- **Working definition.** A stage between broad pretraining and later alignment training in which a model is trained on synthetic documents discussing a Model Spec or Constitution, in order to influence how the subsequent alignment training generalises. The scripts mark it as a proposed technique rather than a standardised phase.
- **Source.** Master EN, "Training Builds and Shapes the Latent Program Space".
- **Literature.** Li, Wichers, Price, Marks, Kutasov, "Model Spec Midtraining. Improving How Alignment Training Generalizes," arXiv:2605.02087, 2026.

### Parametric Knowledge

- **German.** Proposal, parametrisches Wissen. The Skriptum describes the matter in §2.2 without naming it.
- **Working definition.** Knowledge that a model can produce because its parameters encode statistical structure from training material, which the scripts contrast with an addressable copy of a training document and therefore with any direct provenance for a generated claim.
- **Source.** Master EN, "The Shape of a Wikipedia Article About Zebras" with its three information layers of model parameters, external resources and current context; Skriptum DE, §2.2.
- **Literature.** Proposed anchor, Petroni et al., "Language Models as Knowledge Bases?," arXiv:1909.01066, 2019. The scripts use a lossy-compression analogy from a practitioner introduction and mark it explicitly as an analogy.
- **Relation.** Grounds the provenance argument that module 5 needs, since a model-produced statement carries no source reference of its own.

### In-Context Learning

- **German.** Proposal, In-Context Learning. Absent from both German sources.
- **Working definition.** The ability of a model to adapt its behaviour to instructions, examples and information supplied in the current context without any change to model parameters.
- **Source.** Master EN, "Context Engineering Shapes the Model's Working Context"; the training and inference distinction in "Pretraining and Posttraining".
- **Literature.** Brown et al., arXiv:2005.14165, 2020.
- **Relation.** The matrix already cites this paper as the mechanism anchor of the Prompt Engineering row. The term itself is missing and is what makes context a working surface at all.

### Confabulation

- **German.** Konfabulation (Deck, jagged-intelligence slide).
- **Working definition.** The production of plausible but unsupported claims, chosen in the scripts as the descriptive term for this behaviour in place of hallucination.
- **Source.** CLARIAH, "LLMs as Jagged Alien 'Intelligences'", which states the terminological choice explicitly; Deck.
- **Literature.** No canonical source for the term in this sense. Inference, the adjacent received literature runs under hallucination, for which Ji et al., "Survey of Hallucination in Natural Language Generation," DOI 10.1145/3571730, 2023, is the standard survey. A decision is needed on whether the glossary states the substitution.

### Sycophancy

- **German.** Sycophancy, untranslated with the gloss Tendenz von LLMs, Nutzer:innen zuzustimmen (Deck).
- **Working definition.** The tendency to align an answer with a belief the user has expressed even where this reduces factual accuracy, with the methodological consequence that a prompt asking for confirmation of a preferred interpretation is weak evidence.
- **Source.** CLARIAH, "LLMs as Jagged Alien 'Intelligences'" and the countermeasure in "Practical Prompting Principles"; Master EN, same two places; Deck.
- **Literature.** Sharma et al., "Towards Understanding Sycophancy in Language Models," arXiv:2310.13548, 2023.

### Vector Program

- **German.** Proposal, Vektorprogramm. The Skriptum paraphrases as gelernte Verarbeitungsroutinen (§3.6).
- **Working definition.** A learned and distributed transformation across high-dimensional representations that realises one capability or behaviour, explicitly distinguished from a discrete symbolic program stored inside the model.
- **Source.** CLARIAH, "Prompt Engineering as Search in a Latent Program Space"; Master EN, "Prompt Engineering: Finding Coordinates in a Latent Program Space"; Skriptum DE, §3.6.
- **Literature.** Chollet, "How I Think About LLM Prompt Engineering," 2023, https://fchollet.substack.com/p/how-i-think-about-llm-prompt-engineering.
- **Relation.** Belongs to the existing matrix row on latent program space. See the collision section, since the row is named with a term the scripts do not use.

### Program Query

- **German.** Proposal, Programmabfrage. Absent from both German sources.
- **Working definition.** The prompt considered as an address or search signal into the learned repertoire, where one part of a prompt steers towards a region of that repertoire and another supplies the material the selected transformation operates on.
- **Source.** CLARIAH and Master EN, the five-item terminology list of the latent-program-space sections.
- **Literature.** Chollet, 2023, as above; for the underlying mechanism, Xie, Raghunathan, Liang, Ma, "An Explanation of In-context Learning as Implicit Bayesian Inference," arXiv:2111.02080, 2022, already cited by the matrix.
- **Relation.** Direct collision with the matrix wording Program Key. Both canonical scripts say Program Query.

### Reasoning and Test-Time Compute

- **German.** Reasoning as Thinking Token (Deck); the Skriptum names Reasoning only in passing (§3.5).
- **Working definition.** The allocation of additional computation during inference before a final answer is committed, read in the scripts as a partial shift of the search burden from the user's external prompt variation into a single model invocation.
- **Source.** CLARIAH, "Reasoning and Test-Time Compute as Internal Search"; Master EN, the terminology list and the prompting principle "Use Reasoning Selectively".
- **Literature.** Snell et al., "Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Model Parameters," arXiv:2408.03314, 2024.
- **Relation.** Fifth item of the latent-program-space terminology list, so it belongs with that matrix row rather than beside it.

### Mechanistic Interpretability

- **German.** Mechanistische Interpretierbarkeit (Skriptum DE, §3.6, as Interpretierbarkeitsverfahren).
- **Working definition.** Research into the internal computations through which a model produces behaviour, which the scripts use for the limited claim that model computation is structured and input-dependent rather than as an empirical map of a latent program space.
- **Source.** CLARIAH, "Excursus: Mechanistic Interpretability"; Master EN, "Excursus: Mechanistic Interpretability and Activation Paths"; Skriptum DE, §3.6 with two figures.
- **Literature.** Lindsey et al., "On the Biology of a Large Language Model," Transformer Circuits, 2025; Sofroniew et al., "Emotion Concepts and Their Function in a Large Language Model," Transformer Circuits, 2026.

### Assistant Character

- **German.** Assistentenfigur (Skriptum DE, §2.2).
- **Working definition.** The conversational persona a provider shapes and stabilises through training, runtime instructions, policy layers and product design, which the scripts keep separate from the underlying model and from any claim about subjective experience.
- **Source.** CLARIAH, "The Assistant Is a Character Generated by the Model"; Master EN, same section; Skriptum DE, §2.2 with figure 3.
- **Literature.** Anthropic, "Claude's Character," https://www.anthropic.com/research/claude-character; Anthropic, "Claude's Constitution," 2026, https://www.anthropic.com/constitution.

### Constitution, Character Training and System Prompt

- **German.** Systeminstruktionen (Skriptum DE, §2.2); Constitution untranslated in footnote 2.
- **Working definition.** Three layers the scripts insist on separating, a training artefact such as a Constitution or Model Spec that shapes what is learned, character training and post-training that stabilise behavioural dispositions, and a system prompt that operates at runtime inside one deployment.
- **Source.** Master EN, "How Anthropic Shapes Claude's Assistant Character"; Skriptum DE, §2.2 with footnote 2 marking the ontological reading as contested.
- **Literature.** Anthropic, "Claude's New Constitution," 2026, https://www.anthropic.com/research/claude-new-constitution; Anthropic, "System Prompts," https://platform.claude.com/docs/en/release-notes/system-prompts.

### Vision-Language Model

- **German.** Proposal, Vision-Language-Modell. The Skriptum speaks of multimodaler Verarbeitung (§4.3) without the term.
- **Working definition.** A model that processes visual and linguistic information within the same task, so that a general-purpose multimodal system can transcribe a facsimile from image and instruction without being a dedicated OCR or HTR system.
- **Source.** CLARIAH, "Multimodality and Vision-Language Models"; Master EN, "Multimodality & Vision Language Models".
- **Literature.** Gemini Team, "Gemini. A Family of Highly Capable Multimodal Models," arXiv:2312.11805, 2023.

### Contextually Plausible Reading

- **German.** Proposal, kontextuell plausible Lesung. The Skriptum describes the failure in §2.1 without naming it.
- **Working definition.** The characteristic failure mode of transcription by a general multimodal model, where the generated reading fits the linguistic context while the visual evidence of the source supports a different one, so that fluency and internal coherence carry no information about source fidelity.
- **Source.** CLARIAH, "Example Result and Critical Review" and "Multimodality and Vision-Language Models"; Master EN, "Hands on 1 (Example Result)".
- **Literature.** No canonical source. This is the corpus's own name for the phenomenon and should be marked as such.
- **Relation.** The one term the CLARIAH profile names as carrying the specialisation of that instance, since the hands-on exists to expose it.

### Emergent Capability

- **German.** Emergenz (Deck, in the open question on zero-shot transcription).
- **Working definition.** A capability that appears without having been trained for separately, used in the scripts as an open question about zero-shot handwriting recognition rather than as an established classification, because model scale and training composition are not observable for proprietary systems.
- **Source.** CLARIAH, "Example Result and Critical Review", closing question; Master EN, "Multimodality & Vision Language Models".
- **Literature.** Proposed anchors, Wei et al., "Emergent Abilities of Large Language Models," arXiv:2206.07682, 2022, and the counterposition in Schaeffer, Miranda, Koyejo, "Are Emergent Abilities of Large Language Models a Mirage?," arXiv:2304.15004, 2023. Neither is cited in the scripts.

## 2 Prompt Engineering

### Prompt

- **German.** Prompt, with the definitional gloss die für einen Modellaufruf bereitgestellte Eingabesequenz (Skriptum DE, §3.1).
- **Working definition.** The input sequence supplied for one model call, which may contain a task, source material, context, requirements, constraints, examples, procedural instructions and specifications for the expected output.
- **Source.** Skriptum DE, §3.1; CLARIAH, "Prompt Engineering".
- **Literature.** Schulhoff et al., "The Prompt Report. A Systematic Survey of Prompting Techniques," DOI 10.48550/arXiv.2406.06608, 2024.
- **Relation.** The matrix defines Prompt Engineering without defining its object. The scripts define both.

### Bounded Specification

- **German.** Begrenzte Spezifikation (Skriptum DE, §3.2).
- **Working definition.** A prompt understood as a specification of a current task inside an already existing knowledge and working context, which points at persistent project rules instead of restating them and therefore stays compact without becoming vague.
- **Source.** Skriptum DE, §3.2 with the TEI example and §3.8; Master EN, "Transcribe a Facsimile with Gemini 3.7 Flash".
- **Literature.** No external source. In-house formulation of the corpus, to be marked as such.
- **Relation.** The hinge between module 2 and module 3, since the prompt can only be bounded if a maintained knowledge base exists to point at.

### Task, Context, Rules, Output

- **German.** The Skriptum gives a seven-part list instead, Ziel, Ausgangslage, Anforderungen, Einschränkungen, Vorgehen, Ausgabeform, Abschlusskriterium (§3.2).
- **Working definition.** The four-part working structure for research prompts, separating what the model should do, which source or project information it needs, which scholarly and technical constraints govern the result, and in which form the result is returned, so that the parts can be revised independently.
- **Source.** CLARIAH, "Prompt Engineering" and the two transcription prompts; Master EN, "Prompting Strategies", item Structure the Prompt.
- **Literature.** Schulhoff et al., 2024, as above; Google, "Prompt Design Strategies," https://ai.google.dev/gemini-api/docs/prompting-strategies.
- **Relation.** Divergence inside the corpus. The English texts teach four parts, the German Skriptum seven. A glossary entry has to state which list is canonical or that both are instance-dependent.

### Role Prompting

- **German.** Role Prompting (Skriptum DE, §3.3).
- **Working definition.** A brief functional assignment of a role to the model, which can influence terminology, style, perspective and level of detail while adding no factual knowledge, so that it does not reliably improve accuracy or reasoning.
- **Source.** Skriptum DE, §3.3; CLARIAH, "Prompting Is Weird"; Master EN, "Prompting Is Weird, and Keeps Changing".
- **Literature.** Basil et al., "Playing Pretend. Expert Personas Don't Improve Factual Accuracy," arXiv:2512.05858, 2025; Hu and Collier, "Quantifying the Persona Effect in LLM Simulations," DOI 10.48550/arXiv.2402.10811, 2024.

### Persona Prompting (Persona Engineering)

- **German.** Persona Prompting (Skriptum DE, §3.3); Persona Engineering on the Deck slide.
- **Working definition.** A worked-out perspective with background, experience, goals, constraints and usage situation, used as a structured viewpoint for reviewing an artefact, whose outputs are hypotheses about users rather than empirical user data.
- **Source.** Skriptum DE, §3.3 with the workshop-participant persona; Master EN, "Persona Engineering"; Deck.
- **Literature.** Hu and Collier, 2024, as above. The scripts additionally cite a practitioner field guide on synthetic personas, which is a video source.
- **Relation.** The Skriptum keeps role and persona prompting distinct and warns against equating them, which a single glossary row would flatten.

### Self-Revision

- **German.** Self-Revision (Skriptum DE, §3.4).
- **Working definition.** A staged interaction in which the model first produces a draft, then checks it against explicit criteria, then revises only the confirmed findings. The scripts state that this surfaces errors without constituting independent verification, since the same model can miss or rationalise its own assumptions.
- **Source.** Skriptum DE, §3.4; Deck, hands-on step 3; Master EN, "Generate, Compare and Reconcile" as the related principle.
- **Literature.** No canonical source cited. Proposed anchor for the limit, Zheng et al., "Judging LLM-as-a-Judge," arXiv:2306.05685, 2023, already used by the matrix for the self-enhancement bias.
- **Relation.** Feeds the model-assisted review entry of module 5 and the existing Verification Levels row.

### Structured Output

- **German.** Strukturierte Ausgaben (Skriptum DE, §3.4).
- **Working definition.** An output constrained to a defined format such as JSON, XML, a Markdown table or a file structure, which reduces ambiguity and enables deterministic checks. The scripts separate four levels of correctness, syntactic conformity, structural completeness, semantic correctness and scholarly adequacy, and state that the first two prove nothing about the last.
- **Source.** Skriptum DE, §3.4; CLARIAH, "From Generated Text to Structured Data"; Master EN, ".txt → JSON → CSV".
- **Literature.** No canonical source. The four levels are the corpus's own distinction.

### Prompt Sensitivity

- **German.** Promptwirkungen, with the qualifier modell-, aufgaben- und sprachabhängig (Skriptum DE, §3.5).
- **Working definition.** The empirical finding that model output can change in response to linguistic details with little relation to the task, so that prompting effects are local to model, version, task, language, position, metric and random variation and should be treated as experimental interventions rather than transferable rules.
- **Source.** Skriptum DE, §3.5 with figures 5 and 6 and the seven-step evaluation procedure; CLARIAH, "Prompting Is Weird"; Master EN, same section.
- **Literature.** Li et al., "Large Language Models Understand and Can Be Enhanced by Emotional Stimuli," DOI 10.48550/arXiv.2307.11760, 2023; Yin et al., "Should We Respect LLMs?," DOI 10.48550/arXiv.2402.14531, 2024; Battle and Gollapudi, "The Unreasonable Effectiveness of Eccentric Automatic Prompts," DOI 10.48550/arXiv.2402.10949, 2024; Rajeev et al., "Cats Confuse Reasoning LLM," DOI 10.48550/arXiv.2503.01781, 2025.

## 3 Knowledge and Context Engineering

### Context Window

- **German.** Context Window (Skriptum DE, §4.2); Kontextfenster (Deck).
- **Working definition.** The finite token-based processing space of one model call, containing the supplied input and those generated tokens that remain in the active sequence. The scripts treat its nominal size as a technical limit rather than as a target for how much information to supply.
- **Source.** Skriptum DE, §4.2 with the enumeration of what occupies it; CLARIAH, "Context Engineering Shapes the Working Context"; Master EN, "Context Window, Context Rot and Distillation"; Deck, the two 8K examples.
- **Literature.** Vaswani et al., arXiv:1706.03762, 2017.
- **Relation.** The matrix has a Context Engineering row but no entry for the object it operates on. The scripts build a three-level distinction of knowledge base, working context and context window that the matrix cannot express with one row.

### Working Context

- **German.** Working Context, untranslated (Skriptum DE, §4.5 and §4.6).
- **Working definition.** The task-specific configuration of information, documents, data access, instructions, tool descriptions, permissions, current state and feedback assembled for one assignment. Not every component is serialised into tokens, since an agent may reach a dataset through a tool while only selected results enter the model context.
- **Source.** Skriptum DE, §4.5 with the worked example for one edition page and §4.6 with the four-way loading matrix; Master EN, "Project Knowledge Base and Working Context"; Deck.
- **Literature.** Pollin, *Promptotyping. Translating Research Data into Research Artefacts through Context Engineering and Agentic Engineering*, review draft 0.9, 2026, which the master script cites as the source of this formulation.

### Project Knowledge Base

- **German.** Project Knowledge Base, untranslated (Skriptum DE, §4.5 and §5.3); Wissensbasis as the descriptive gloss.
- **Working definition.** The persistent, inspectable and revisable body of documented project knowledge holding the project's current understanding of its data, its purpose, its requirements, decisions and uncertainties. It describes and contextualises sources and research data rather than replacing them.
- **Source.** Skriptum DE, §5.3 with the concrete `knowledge/` folder layout; Master EN, "Project Knowledge Base and Working Context"; Deck.
- **Literature.** Pollin, *Promptotyping*, review draft 0.9, 2026.
- **Relation.** The counterpart the Knowledge Document row needs, since a document class without a maintained collection leaves the selection step of context engineering undefined.

### Context Rot

- **German.** Context Rot, untranslated (Skriptum DE, §4.2; Deck).
- **Working definition.** Observed degradation in a model's ability to retrieve and apply relevant information as the active context becomes longer, denser or more distracting. The scripts explicitly refuse to reduce it to one causal mechanism and list position effects, distractors, conflicting information and obsolete intermediate state as contributors.
- **Source.** Skriptum DE, §4.2; CLARIAH, "Context Engineering Shapes the Working Context"; Master EN, "Context Rot"; Deck, with the caveat that the reported evidence is task-specific.
- **Literature.** Hong, Troynikov, Huber, *Context Rot. How Increasing Input Tokens Impacts LLM Performance*, Chroma, 2025, https://research.trychroma.com/context-rot.

### Dense and Sufficient Context

- **German.** Dichter und hinreichender Kontext (Skriptum DE, §4.2; Deck).
- **Working definition.** The stated target quantity for a working context, as bounded as possible while carrying every distinction the task requires. The scripts argue against a shortening rule, because radical reduction removes provenance, conditions and uncertainty.
- **Source.** Skriptum DE, §4.2 closing paragraph; Master EN, "Why AI Agents Need Context"; Deck, "Warum AI Agents Context brauchen".
- **Literature.** No canonical source. Corpus formulation, derived from the Context Rot finding.

### Context Compression

- **German.** Context Compression, untranslated (Skriptum DE, §4.4; Deck).
- **Working definition.** Reduction of the amount of information entering an active context, through selection of relevant passages, summary, removal of repetition, aggregation of data, retention of representative examples or compaction of the previous working history.
- **Source.** Skriptum DE, §4.4; Master EN, "Selecting, Structuring and Distilling Knowledge"; Deck.
- **Literature.** Pollin, *Promptotyping*, review draft 0.9, 2026.

### Distillation

- **German.** Distillation, untranslated (Skriptum DE, §4.4 and §7.4; Deck).
- **Working definition.** The stronger operation beyond compression, transforming an existing understanding into a selective, structured and inspectable representation that preserves the concepts, relations, conditions, uncertainties and rationales a given purpose requires. The same material is distilled differently for a general introduction, an implementation task and a verification task.
- **Source.** Skriptum DE, §4.4 with its three operations of selection, structuring and condensation, and §7.4 as a Promptotyping phase; Master EN, "Selecting, Structuring and Distilling Knowledge"; Deck.
- **Literature.** Pollin, *Promptotyping*, review draft 0.9, 2026.
- **Relation.** Collides with the established machine-learning sense of distillation, where a smaller model is trained on a larger one. The glossary has to disambiguate explicitly, since the audience meets both.

### Over-Distillation

- **German.** Überdestillation (Skriptum DE, §4.4).
- **Working definition.** The counter-risk of distillation, present when provenance, uncertainty or details needed for action are lost, so that a shorter document turns several alternative statements into one apparently unambiguous rule.
- **Source.** Skriptum DE, §4.4.
- **Literature.** No canonical source. Corpus term.

### Knowledge Acquisition

- **German.** Knowledge Acquisition, untranslated (Skriptum DE, §5.2); Wissenserwerb on the Deck's knowledge-modelling slide.
- **Working definition.** The elicitation and explicitation of relevant knowledge from two sources, existing documents and data on one side, implicit knowledge of people and organisations on the other, through document analysis, interviews, workshops, observation of workflows, error analysis and joint modelling sessions.
- **Source.** Skriptum DE, §5.2 with the `<supplied>` example of an unwritten but practised rule; Master EN, "Scholar Centred Design and Requirements Engineering"; Deck.
- **Literature.** Studer, Benjamins, Fensel, "Knowledge Engineering. Principles and Methods," DOI 10.1016/S0169-023X(97)00056-6, 1998, already cited by the matrix for the Knowledge Engineering row; Schreiber et al., *Knowledge Engineering and Management. The CommonKADS Methodology*, MIT Press, 2000.
- **Relation.** Sits inside the existing Knowledge Engineering row as its first operation. It needs its own entry because the scripts assign it a distinct method set.

### Tacit Knowledge and Externalisation

- **German.** Implizites Wissen (Skriptum DE, §5.2 and §5.1); the Deck uses the slide title "I know things".
- **Working definition.** Knowledge held by people, teams or institutions without being documented in a form another person or system can inspect. The scripts locate the starting point of knowledge engineering in the gap between knowledge possessed and knowledge operationally available.
- **Source.** Master EN, "'I Know Things'" and "Why Knowledge Must Be Made Explicit"; Skriptum DE, §5.1; Deck.
- **Literature.** Nonaka, "A Dynamic Theory of Organizational Knowledge Creation," DOI 10.1287/orsc.5.1.14, 1994, which the matrix already cites under Knowledge Document.
- **Relation.** The matrix uses this anchor for the document class. The scripts use the same theory for the acquisition step, which is a different place in the workflow.

### Knowledge Modelling

- **German.** Wissensmodellierung (Deck; Skriptum DE has no separate section).
- **Working definition.** The classical construction of a knowledge base by identifying the concepts of a domain, representing them formally and making them queryable, named in the scripts as one of three neighbouring traditions that AI-supported knowledge work draws on.
- **Source.** Master EN, "Knowledge Modelling, Personal Information Management and Project Management"; Deck, the three-tradition slide with its process steps.
- **Literature.** Russell and Norvig, *Artificial Intelligence. A Modern Approach*, 4th ed., Pearson, 2020; Allen et al., "Knowledge Engineering Using Large Language Models," DOI 10.4230/TGDK.1.1.3, 2023.
- **Relation.** The Deck states the shift from the classical form explicitly, that the formalisation target is structured natural language with light metadata rather than logic and ontology, because the language model supplies the language understanding. This is a substantive claim the matrix row should carry.

### Personal Information Management

- **German.** Personal Information Management, untranslated (Deck).
- **Working definition.** The study of how people acquire, organise, maintain, retrieve, use and share information across formats and locations, with fragmentation as its core problem and the personal information collection as its core concept.
- **Source.** Master EN, "Knowledge Modelling, Personal Information Management and Project Management"; Deck, the three-tradition slide.
- **Literature.** Jones, Dinneen, Capra, Diekema, Pérez-Quiñones, "Personal Information Management," DOI 10.1081/E-ELIS4-120053695, 2017.

### Instruction File

- **German.** Instruktionsdatei (Skriptum DE, §5.6).
- **Working definition.** A persistent Markdown file such as `AGENTS.md` or `CLAUDE.md` that sets recurring rules for agentic work in a project, loaded at session start so that stable working rules do not have to be retyped into every prompt. The scripts note that discovery and precedence rules differ across tools and that such a file is context rather than an enforcement mechanism.
- **Source.** Skriptum DE, §5.6 with the four-way distinction of knowledge document, instruction file, skill and prompt; Master EN, "AGENTS.md and CLAUDE.md", "Global CLAUDE.md", "Project Specific CLAUDE.md"; Deck.
- **Literature.** AGENTS.md, https://agents.md; Anthropic, "How Claude Remembers Your Project," https://code.claude.com/docs/en/memory.
- **Relation.** The matrix cites AGENTS.md as an anchor for the Knowledge Document row. The scripts separate the two sharply, a knowledge document describes the object while an instruction file governs recurring work. That separation should survive into the matrix.

### Agent Skill and Progressive Disclosure

- **German.** Agent Skill, untranslated (Skriptum DE, §5.6; Deck).
- **Working definition.** A reusable folder holding a `SKILL.md` and optional scripts, references and assets for one recurring class of task, loaded in stages so that only name and description occupy the context until the skill becomes relevant.
- **Source.** Skriptum DE, §5.6 with edition-specific examples; Master EN, "Agent Skill"; Deck.
- **Literature.** Agent Skills specification, https://agentskills.io/specification; Anthropic, Agent Skills overview, https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.
- **Relation.** The matrix cites progressive disclosure under Knowledge Document as the mechanism that lets written knowledge enter a context without occupying it. The skill is the artefact carrying that mechanism and is procedural rather than descriptive.

### Markdown as Serialization

- **German.** Markdown als technische Repräsentation (Skriptum DE, §5.5); the Deck phrases it as Serialisierung.
- **Working definition.** The claim that the knowledge document is the conceptual artefact while Markdown is one possible technical representation of it, chosen for openness, versionability, linkability and direct readability by people and models, without any claim of superiority over richer formats.
- **Source.** Skriptum DE, §5.5; CLARIAH, "Markdown and Knowledge Documents"; Master EN, "Markdown Makes Document Structure Explicit for LLMs"; Deck.
- **Literature.** Markdown Guide, https://www.markdownguide.org.
- **Relation.** Belongs to the Knowledge Document row as its representational qualifier. The matrix currently carries drift note D4 on that row, and this distinction is one of the things the note has to resolve.

### Knowledge-Base Governance and Curation

- **German.** Governance und Kuration (Skriptum DE, §5.7).
- **Working definition.** Governance sets the rules for building, changing and using a knowledge base; curation applies those rules to the actual holdings, structurally for names, metadata, links, document types, versions and duplicates, and substantively for contradictions, outdated rules, missing constraints and over-condensed passages.
- **Source.** Skriptum DE, §5.7, which also states that an agent may locate problems and propose changes while substantive changes require human responsibility.
- **Literature.** No canonical source cited. Proposed anchor for the maintenance argument, Schreiber et al., CommonKADS, 2000.
- **Relation.** Sits between module 3 and module 5, since the responsibility rule it ends on is the same one the acceptance entry carries.

## 4 Agentic Engineering

### Tool Use

- **German.** Tool Use (Deck); Werkzeugnutzung (Skriptum DE, §6.1 and §6.4).
- **Working definition.** The connection of a model to executable functions and external resources such as file access, terminal, code execution, web search, database queries, browser control, validators and specialised APIs, which the scripts value most where a tool returns evidence about the consequences of an action.
- **Source.** Skriptum DE, §6.4; Master EN, "Tool Use"; CLARIAH, "LLMs as Jagged Alien 'Intelligences'" for the argument that tool use changes the effective system; Deck.
- **Literature.** Sapkota, Roumeliotis, Karkee, "AI Agents vs. Agentic AI," DOI 10.1016/j.inffus.2025.103599, 2025, already cited by the matrix.
- **Relation.** The matrix covers AI Agent and AI Harness but not the operation that separates an agent from a text generator.

### Compound System (Model, Harness and Environment)

- **German.** Proposal, Verbundsystem. The Skriptum states the matter in §2.3 and §2.4 without a term.
- **Working definition.** The claim that agentic capability is a property of model, harness and environment together, so that the unit of analysis is the complete system of model, harness, context, tools, state, permissions, executable environment and feedback rather than the model in isolation.
- **Source.** CLARIAH, "Agentic Engineering and AI Harnesses" with the explicit formula; Master EN, "AI Harness Architecture"; Deck.
- **Literature.** Zhong and Zhu, "AI Harness Engineering. A Runtime Substrate for Foundation-Model Software Agents," DOI 10.48550/arXiv.2605.13357, 2026.
- **Relation.** Belongs to the AI Harness row. Note that this paper is the anchor both scripts and the deck use for the harness, and that it is missing from the matrix's anchor set.

### Trajectory

- **German.** Arbeitstrajektorie (Skriptum DE, §3.7 and §6.1; Deck).
- **Working definition.** The complete sequence of observations, intermediate decisions, tool calls, file modifications, execution results and follow-up actions that an agentic run produces, which the scripts make the object of engineering in place of the single response.
- **Source.** Master EN, "Agentic Engineering" with the shift from response to trajectory; Skriptum DE, §6.1 with the propagating-error example; Deck.
- **Literature.** Zhong and Zhu, 2026, as above, for the argument that a final artefact is weak evidence about the process that produced it.

### Agentic Execution Loop

- **German.** Agentische Ausführungsschleife (Skriptum DE, §6.2 with figure 10).
- **Working definition.** The repeated cycle of registering the current state, planning a bounded next step, executing a tool or action, observing the result and updating the approach, bound to documented requirements, permissions, stopping conditions and human intervention points.
- **Source.** Skriptum DE, §6.2 with the ten-step edition example; Master EN, "Agentic Engineering"; Deck, hands-on step 1.
- **Literature.** No single canonical source. The Deck relates the loop to the cybernetic feedback loop, citing Wiener, *Cybernetics or Control and Communication in the Animal and the Machine*, 1948, and notes the difference that feedback arrives through tool output rather than sensors.

### Autonomy

- **German.** Autonomie (Skriptum DE, §6.2; Deck).
- **Working definition.** The extent of work performed between two human interventions. The Skriptum defines the term this way explicitly and states that autonomy in this sense does not mean the absence of human control.
- **Source.** Skriptum DE, §6.2, closing sentence; Deck, on the classical four properties.
- **Literature.** Wooldridge and Jennings, "Intelligent Agents. Theory and Practice," DOI 10.1017/S0269888900008122, 1995, already cited by the matrix.
- **Relation.** A deliberate narrowing against the classical property of autonomy in the agent definition the matrix cites. The two readings differ and the glossary has to say which one it states.

### Least-Privilege Tool Access

- **German.** Prinzip der geringsten erforderlichen Berechtigung (Skriptum DE, §6.4).
- **Working definition.** The rule that tool and file access is granted at the minimum required scope, with source files readable but not writable, generated artefacts confined to a working folder, validators running without confirmation, and publication or deployment steps requiring explicit release.
- **Source.** Skriptum DE, §6.4 with the edition-specific permission table; CLARIAH, "Prepare the Working Environment before the First Prompt"; Master EN, same section.
- **Literature.** Proposed anchor, Saltzer and Schroeder, "The Protection of Information in Computer Systems," *Proceedings of the IEEE* 63, no. 9, 1975, DOI 10.1109/PROC.1975.9939, for the principle itself. Not cited in the scripts.

### Intervention Point and Escalation Condition

- **German.** Menschliche Interventionspunkte, Eskalationsbedingungen (Skriptum DE, §6.1 and §6.6).
- **Working definition.** The defined places at which an agentic run hands back to a person, named in the scripts as contradictory requirements, missing disciplinary grounds, changes that are hard to reverse, sensitive resources, modelling decisions with disciplinary consequences, and validation and acceptance.
- **Source.** Skriptum DE, §6.6 with the reversibility requirement for intermediate states; Master EN, "Why Multi Step Work Must Be Organised".
- **Literature.** Anthropic, "Building Effective Agents," 2024, https://www.anthropic.com/engineering/building-effective-agents, already cited by the matrix for human checkpoints.

### Subagent

- **German.** Subagent (Skriptum DE, §6.5; Deck).
- **Working definition.** A delegated agent instance with a bounded partial task, its own fresh context and a defined return format, used to keep large volumes of intermediate information out of the parent context and to run parallelisable checks. The scripts state that it is an architectural pattern without a formal standard and that more agents raise coordination and verification effort.
- **Source.** Skriptum DE, §6.5 with four edition-specific subagent roles; Master EN, "Subagents" and "Subagents and Epistemic Infrastructure"; Deck.
- **Literature.** No standard and no citation in the four mined texts. The deck states explicitly that the subagent is the one item among the five agent concepts without a formal specification.
- **Relation.** The scripts add a methodological rule the matrix does not carry, that independent review distributes inspection and exposes disagreement while model agreement produces no truth by voting.

### Model Routing

- **German.** Model Routing, untranslated (Deck).
- **Working definition.** The assignment of different phases of an agentic workflow to different models and inference budgets, typically a stronger reasoning model for planning and review and a faster model for implementation, treated as an engineering decision that changes as models change.
- **Source.** Master EN, "Model Routing" with the sequence from research through specification, implementation and review to revision; Deck.
- **Literature.** No canonical source. Practitioner provenance, to be marked as such.

### Model Context Protocol (MCP)

- **German.** Model Context Protocol (MCP), untranslated (Skriptum DE, §6.5; Deck).
- **Working definition.** An open standard connecting AI applications with external tools, data sources and workflows through common client and server interactions, which addresses an integration problem and decides nothing about relevance, reliability or permissibility of a resource.
- **Source.** Skriptum DE, §6.5 with footnote 5 on implementation-dependent permission architecture; Master EN, "Model Context Protocol (MCP)"; Deck, with the M-times-N argument.
- **Literature.** Model Context Protocol, https://modelcontextprotocol.io/specification/2025-11-25.

### Agent2Agent Protocol (A2A)

- **German.** Agent2Agent (A2A), untranslated (Deck); the Skriptum speaks of Agent-to-Agent-Protokollen (§6.5).
- **Working definition.** An open protocol for discovery, task management and result exchange among independent agents without exposing internal memory, tools or proprietary logic, complementary to MCP in that it standardises agent-to-agent rather than agent-to-tool interaction.
- **Source.** Master EN, "A2A (Agent to Agent)"; Skriptum DE, §6.5 with the four methodological questions on responsibility, handover, conflict and decision authority; Deck.
- **Literature.** Agent2Agent Protocol, https://a2a-protocol.org/latest/topics/a2a-and-mcp/.

### Epistemic Infrastructure

- **German.** Epistemische Infrastruktur (Deck, in the subagent verification slide).
- **Working definition.** The arrangement in which knowledge documents, source data, schemas, tests, software tools, agents, project state and human judgment together establish the conditions under which a generated representation can be inspected, criticised, validated and accepted for a stated purpose.
- **Source.** CLARIAH, "AI-Supported Research Data Workflows & Epistemic Infrastructures" and "Agentic Engineering and AI Harnesses"; Master EN, "Critical Expert and Epistemic Infrastructure"; Deck.
- **Literature.** Pollin, *Promptotyping*, review draft 0.9, 2026. Proposed wider anchor, Edwards et al., "Understanding Infrastructure. Dynamics, Tensions, and Design," 2007, for the infrastructure-studies reading, which the scripts do not invoke.
- **Relation.** The concept that separates this corpus from a tooling account. It carries the load in the conclusion of both English texts and has no matrix row.

### Promptotyping Phase Model

- **German.** Preparation, Exploration, Distillation, Implementation as chapter headings (Skriptum DE, §7.2 to §7.6).
- **Working definition.** The recurring work forms of the method, preparing sources and workspace into a reconstructible initial state, exploring what data and sources permit and constrain, distilling the developed understanding into maintained documents, and implementing the artefact so that gaps in the knowledge become visible.
- **Source.** Skriptum DE, ch. 7; CLARIAH, "Promptotyping" with the five-stage flow diagram; Master EN, "Promptotyping as an Iterative Knowledge Loop".
- **Literature.** Pollin, *Promptotyping*, review draft 0.9, 2026; Digital Humanities Craft, Promptotyping specification, https://dhcraft.org/Promptotyping/.
- **Relation.** Belongs inside the Promptotyping row. The Deck's hands-on runs a different five-step sequence of Preparation, Planning, Feedback and Self Revision, Implementation, Verification, which is a divergence to resolve before the glossary states a phase list.

### Scholar-Centred Design

- **German.** Scholar-Centred Design, untranslated (Skriptum DE, §7.5; Deck).
- **Working definition.** The orientation of development towards the research practices, interpretative tasks and responsibilities of the participating scholars, asking which scholarly distinctions an interface keeps visible rather than only whether it is usable.
- **Source.** Skriptum DE, §7.5; Master EN, "Scholar Centred Design and Requirements Engineering"; Deck.
- **Literature.** Pollin, *Modelling, Operationalising and Exploring Historical Information*, Graz, 2025, https://resolver.obvsg.at/urn:nbn:at:at-ubg:1-220602.
- **Relation.** Named in the module map as part of the Promptotyping module and absent from the matrix.

### User Story

- **German.** User Story, untranslated (Deck).
- **Working definition.** A requirements format stating who acts, which capability is required and why it matters, used in the corpus as the bridge between structured research data and an implementable artefact because it is readable by people and usable as agent context.
- **Source.** Master EN, "As a … I Want to" with the liturgy and social-history examples; Deck, the Scholar-Centred Design slide with worked stories.
- **Literature.** Pollin, *Modelling, Operationalising and Exploring Historical Information*, Graz, 2025, as above.

### Spec-Driven Development

- **German.** Proposal, spezifikationsgetriebene Entwicklung. The Deck uses the English term.
- **Working definition.** The placement of an explicit specification between exploratory discussion and implementation, contextualised by the maintained knowledge base rather than written as a detached document, so that a reviewable object exists before code is produced.
- **Source.** Master EN, "Spec Driven Development"; Deck, with the note that the specification is contextualised in the `knowledge` folder.
- **Literature.** No canonical source. Practitioner provenance.

### Write-back

- **German.** Write-back, untranslated (Skriptum DE, §7.9).
- **Working definition.** The defined operation of returning findings from implementation and checking into the responsible documents, so that new knowledge does not remain in the chat, in the code or in one person's memory. Findings are examined before they are written back rather than treated as knowledge automatically.
- **Source.** Skriptum DE, §7.9 and §7.11; CLARIAH, "Promptotyping" as curated feedback; Master EN, "Promptotyping as an Iterative Knowledge Loop" as curated write back.
- **Literature.** Pollin, *Promptotyping*, review draft 0.9, 2026.

### Promptotype

- **German.** Promptotype (Skriptum DE, §7.10).
- **Working definition.** The documented and referenceable state of one iteration, comprising the relevant state of the knowledge base, the artefact, the referenced data state, the documented checks, the open questions and the bounded grounds of acceptance. It is a sufficiently determined state to continue from rather than a finished product.
- **Source.** Skriptum DE, §7.10.
- **Literature.** Pollin, *Promptotyping*, review draft 0.9, 2026.
- **Relation.** Distinct from the Promptotyping row, which names the method. The artefact state needs its own wording, since acceptance in module 5 attaches to it.

## 5 Critical Perspectives and Governance

### Evaluation

- **German.** Evaluation (Skriptum DE, §3.5 for prompt evaluation).
- **Working definition.** Measurement or assessment of outputs, models or workflows against explicit criteria, quantitative or qualitative, including benchmark scores, error rates, task-completion measures and structured expert review.
- **Source.** Master EN, "Evaluation, Verification, Validation and Acceptance"; CLARIAH, "Evaluation, Validation and Scholarly Verification".
- **Literature.** The master script marks the broad usage in its own footnote rather than citing a source. Proposed anchor for the model-based case, Zheng et al., arXiv:2306.05685, 2023, already used by the matrix.
- **Relation.** See the collision section. The three sources cut the checking vocabulary three different ways.

### Technical Verification

- **German.** Technische Verifikation (Skriptum DE, §7.7).
- **Working definition.** The check whether an artefact conforms to specified or formalised requirements, through schema validation, deterministic mappings, test suites, numerical consistency checks and executable acceptance criteria, and therefore largely automatable because the conditions have been formalised.
- **Source.** Skriptum DE, §7.7 with the edition-specific check list and the Verification Report template in the appendix; Master EN, "Evaluation, Verification, Validation and Acceptance".
- **Literature.** No external anchor in the scripts. The master script states that the distinction adapts established verification and validation terminology from software and systems engineering.

### Scholarly Validation

- **German.** Fachliche und wissenschaftliche Validierung (Skriptum DE, §7.7).
- **Working definition.** The check whether a representation, interpretation or artefact is adequate to the source, the purpose and the disciplinary context, which requires domain expertise and cannot be reduced to a deterministic test. A schema-valid document can encode a historically unjustified interpretation.
- **Source.** Skriptum DE, §7.7 with its four guiding questions; Master EN, same section; CLARIAH, "Evaluation, Validation and Scholarly Verification" under the name scholarly verification.
- **Literature.** Pollin, *Promptotyping*, review draft 0.9, 2026.

### Acceptance

- **German.** Acceptance, untranslated (Skriptum DE, §7.7, §7.10, §7.11).
- **Working definition.** The responsible decision to use an identified state for a named purpose. The scripts require it to be stated purpose-bound, since a technically verified artefact can be unsuitable for research use and an interesting demonstrator can be unready for publication.
- **Source.** Skriptum DE, §7.7 and the Acceptance Statement template with its sections for identified state, accepted-for purpose, technically verified, disciplinarily checked, not demonstrated, open questions and responsible decision; Master EN, "Evaluation, Verification, Validation and Acceptance".
- **Literature.** Pollin, *Promptotyping*, review draft 0.9, 2026.
- **Relation.** The scripts separate acceptance from publication. The matrix's Verification Levels row ends at checking and has no term for the decision.

### Critical Expert

- **German.** Critical Expert, untranslated (Skriptum DE, §7.8).
- **Working definition.** The responsible disciplinary authority in a project, defined by function rather than by person, which decides which reading is defensible, whether a model is adequate to the source, whether an interface preserves scholarly distinctions and whether a state is accepted for a named purpose. Agents and validators supply evidence for that decision.
- **Source.** Skriptum DE, §7.8; Master EN, "Critical Expert and Epistemic Infrastructure", which adds that the role designs the epistemic conditions rather than manually checking every output.
- **Literature.** Pollin, "Promptotyping mit Claude Sonnet 4. Vibe-Coding erfordert den Critical-Expert-in-the-Loop," Digital Humanities Craft, 2025, https://dhcraft.org/excellence/blog/Critical-Vibing-Claude-4/, which the matrix already cites under Verification Levels.
- **Relation.** The matrix uses this source for the top verification level. The scripts treat the Critical Expert as a role with authority, which is a different object from a level.

### Model-Assisted Review

- **German.** Agentisches Review (Skriptum DE, figure 12 caption).
- **Working definition.** The inspection of one model's output by a second model with access to the source and to executable tools, which can surface possible errors and direct human attention while reproducing the same mistake, introducing a new one or overstating confidence. The scripts attach the rule that model agreement is not scholarly verification.
- **Source.** CLARIAH, "Model-Assisted Review inside an AI Harness"; Skriptum DE, §7.7 with figure 12; Master EN, "Subagents and Epistemic Infrastructure"; Deck, the three-subagent TEI verification slide.
- **Literature.** Zheng et al., arXiv:2306.05685, 2023.

### Candidate Representation

- **German.** Proposal, Kandidatenrepräsentation. Absent from both German sources.
- **Working definition.** The status a model output holds before assessment, valuable as a plausible structured proposal while carrying no evidence of source fidelity, which the scripts generalise beyond transcription to every representational transition in a workflow.
- **Source.** Master EN, "Hands on 1 (Example Result)"; CLARIAH, "Example Result and Critical Review".
- **Literature.** No canonical source. Corpus term.
- **Relation.** Names the object that acceptance and validation operate on and closes the gap between generation and research data that the abstract of the CLARIAH notes opens.

### Deterministic Check

- **German.** Deterministische Prüfung (implied by Skriptum DE, §7.7; the Deck uses deterministische Validation).
- **Working definition.** A reproducible test over an explicit representation, such as recomputing row and column sums of a table or validating XML against a schema, which reveals internal inconsistency without establishing that the source was interpreted correctly.
- **Source.** CLARIAH, "From Generated Text to Structured Data"; Master EN, ".txt → JSON → CSV" with the pattern from probabilistic interpretation through structured representation to deterministic checking.
- **Literature.** No canonical source. Corpus formulation.

### Openness as a Multidimensional Property

- **German.** Proposal, mehrdimensionale Offenheit. Absent from the German sources, since the openness block exists only in the English lecture notes.
- **Working definition.** The reading of openness as a set of separately gradable dimensions covering training data, documentation, training code, architecture, parameters, licences and access conditions, in place of a binary open or closed classification.
- **Source.** CLARIAH, "The Current LLM Capability Landscape".
- **Literature.** European Open Source AI Index, https://osai-index.eu/, which evaluates fourteen dimensions.

### Open-Weight Model

- **German.** Proposal, Open-Weight-Modell.
- **Working definition.** A model whose trained parameters are available under a specified licence and can be downloaded, adapted and executed independently, which the scripts keep strictly separate from open source.
- **Source.** CLARIAH, "The Current LLM Capability Landscape" and the cyber-capability passage on diffusion risk; Master EN, "Which Frontier Models and AI Technologies Do You Use?".
- **Literature.** Open Source Initiative, The Open Source AI Definition 1.0, https://opensource.org/ai/open-source-ai-definition.

### Open Source AI Definition

- **German.** Proposal, Open-Source-KI-Definition.
- **Working definition.** The definition requiring the freedoms to use, study, modify and share an AI system together with access to the preferred form for modification, including sufficient information about training data, source code and model parameters.
- **Source.** CLARIAH, "The Current LLM Capability Landscape" with footnote 19.
- **Literature.** Open Source Initiative, The Open Source AI Definition 1.0, https://opensource.org/ai/open-source-ai-definition.

### Open-Washing

- **German.** Proposal, Open-Washing.
- **Working definition.** The presentation of an AI system as open where significant restrictions on accessibility or reproducibility remain.
- **Source.** CLARIAH, "The Current LLM Capability Landscape" with footnote 21.
- **Literature.** Liesenfeld and Dingemanse, "Rethinking Open Source Generative AI. Open-Washing and the EU AI Act," FAccT '24, DOI 10.1145/3630106.3659005, 2024.
- **Relation.** The one place in the four mined texts where the EU AI Act appears at all, and only inside a citation title.

### Local Deployment

- **German.** Proposal, lokaler Betrieb. The German Skriptum does not treat deployment.
- **Working definition.** Running model inference on hardware controlled by the researcher or the institution, which can increase control over research data, inference configuration and availability while shifting responsibility for hardware, security, maintenance and operation to the institution.
- **Source.** CLARIAH, "The Current LLM Capability Landscape" with footnote 23; Master EN, "Which Frontier Models and AI Technologies Do You Use?".
- **Literature.** No canonical source. The scripts name Ollama and LM Studio as environments.

### Governance Dilemma of Diffusion and Concentration

- **German.** Proposal, Governance-Dilemma zwischen Diffusion und Konzentration.
- **Working definition.** The tension the scripts state for cyber capability, where highly capable open-weight systems can spread offensive capability beyond their developers while proprietary frontier systems concentrate the most capable systems and their infrastructure within a small number of companies and states.
- **Source.** CLARIAH, "Frontier LLMs Asymmetrically Amplify Computational Research", cyber-capability passage, which the workshop profile assigns to module 5.
- **Literature.** AI Security Institute, *Frontier AI Trends Report*, https://www.aisi.gov.uk/frontier-ai-trends-report.
- **Relation.** Marked in the source as the author's own assessment. The glossary should preserve that marking.

### Critical Cyber Capability

- **German.** Proposal, kritische Cyberfähigkeiten.
- **Working definition.** The capability threshold at which a provider can no longer rule out that a model could develop functional zero-day exploits against hardened systems or devise and execute novel end-to-end attack strategies with minimal human direction.
- **Source.** CLARIAH, "Frontier LLMs Asymmetrically Amplify Computational Research" with footnote 31.
- **Literature.** OpenAI, "Responding to the Next Frontier of Critical Cyber Capabilities," 2026, https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/, and the Preparedness Framework it refers to.

### Research data framing

The five terms below open both English texts. The CLARIAH profile states that the module assignment of those opening sections is undecided, so their placement here follows the governance affinity of data documentation and stewardship. They would sit equally well at the head of module 1.

#### Research Data

- **German.** Forschungsdaten (Skriptum DE, §1; Deck).
- **Working definition.** Representations of research objects, sources, observations or processes that are selected, collected, constructed or produced through scholarly work, shaped by research decisions and dependent on documentation and context for critical assessment, reproducibility and reuse.
- **Source.** CLARIAH, "Humanities Research Data Are Constructed through Scholarly Workflows"; Master EN, same section.
- **Literature.** Geiger, "Daten / Forschungsdaten," DOI 10.17175/wp_2023_003_v2, 2024; Schöch, "Big? Smart? Clean? Messy? Data in the Humanities," *Journal of Digital Humanities* 2, no. 3, 2013.

#### Capta

- **German.** Capta, untranslated. Absent from the German sources.
- **Working definition.** The argument that humanities data are constructed through situated acts of observation and representation rather than given, so that a transcription already carries decisions about legibility and textual structure.
- **Source.** CLARIAH, "Humanities Research Data Are Constructed through Scholarly Workflows".
- **Literature.** Drucker, "Humanities Approaches to Graphical Display," *Digital Humanities Quarterly* 5, no. 1, 2011.

#### Research Data Workflow

- **German.** Proposal, Forschungsdaten-Workflow. The Skriptum describes the matter as durchgehender Arbeitszusammenhang (§1.4).
- **Working definition.** The organised process through which research materials and data are created, transformed, enriched, assessed and prepared for scholarly use, including source context, scholarly rules, provenance and the procedures for assessment and acceptance. Automated pipelines perform individual transformations inside it.
- **Source.** CLARIAH, "Humanities Research Data Are Constructed through Scholarly Workflows" and "AI-Supported Research Data Workflows & Epistemic Infrastructures".
- **Literature.** No canonical source. Corpus definition, positioned against a pipeline reading.

#### AI Readiness

- **German.** Proposal, KI-Bereitschaft von Forschungsdaten. Absent from the German sources.
- **Working definition.** Whether research data are sufficiently structured, documented and governed for effective use in AI-supported workflows, including machine-readable representations, clear provenance and usage conditions, and the information needed to assess quality, uncertainty and potential bias.
- **Source.** CLARIAH, "Humanities Research Data Are Constructed through Scholarly Workflows"; Master EN, same section.
- **Literature.** Majithia et al., "An Actionable Framework for AI-Ready Data," DOI 10.1002/aaai.70054, 2026; Wilkinson et al., "The FAIR Guiding Principles," DOI 10.1038/sdata.2016.18, 2016; MLCommons Croissant, https://mlcommons.org/working-groups/data/croissant/; Global Indigenous Data Alliance, CARE Principles, https://www.gida-global.org/careprinciples.

#### Provenance

- **German.** Provenienz (Skriptum DE, §1.4, §4.4, §5.4, §5.8, §7.2).
- **Working definition.** The documented relation between a source, the operations applied to it and the resulting representation, required in the scripts wherever generated artefacts are stored separately from unchanged originals, and explicitly separate from the question of validity.
- **Source.** Skriptum DE, §7.2 and §5.4 as a property of a knowledge document; CLARIAH, "Prepare the Working Environment before the First Prompt".
- **Literature.** No anchor in the four mined texts. The module map records PROV-O and the Web Annotation Data Model as the formal layer of the Skriptum's chapter 1, which is not present in the working version read here.

### Governance vocabulary outside the four mined texts

The four texts named for this pass carry no EU AI Act vocabulary. The only occurrence is the title of a cited paper on open-washing. The governance terms of the teaching line live in the VetMedAI workshop script (`workshops/2026-04-22-vetmedai-workshop-1/workshop-script.txt`), which the VetMed profile records as module 5 taught as a substantial block with its own exercise, and which the VetMed Winter School profile marks as the place where that emphasis belongs. The terms below are listed for completeness and are marked as sourced outside this pass, so they need a second reading of that script before they enter a glossary.

- **AI literacy obligation (Art. 4)**, German KI-Kompetenz. The duty to ensure AI literacy across staff, named as one of two obligations immediately relevant to a research institution that uses rather than builds AI systems.
- **Prohibited practices (Art. 5)**, German verbotene Praktiken. The eight absolutely prohibited categories of AI practice, the second immediately relevant obligation.
- **Provider (Art. 3(3))**, German Provider or Anbieter. A natural or legal person who develops or has developed an AI system or GPAI model and places it on the market or puts it into service under their own name or trademark.
- **Deployer**, German Deployer or Betreiber. A natural or legal person using an AI system under their own responsibility in a professional capacity, excluding purely private use.
- **High-risk system**, German Hochrisiko-System. The classification a research system reaches only when it leaves pure research for a regulated application area.
- **Research exemption (Art. 2(6))**, German Forschungsausnahme. The exemption for systems serving the sole purpose of scientific research and development before market placement.
- **General-purpose AI model (GPAI)**, German GPAI-Modell. The separate regulatory category for general-purpose models.
- **Risk-based approach**, German risikobasierter Ansatz. The four-tier classification whose tier determines the intensity of obligations.

Literature for all eight, Regulation (EU) 2024/1689, https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689.

## Collisions with the existing term set

1. **Program Key against Program Query.** The matrix row and the reference draft both say Program Key, and the reference draft's own open points already note that the coinage is unsupported by the literature. Both canonical scripts and the deck say Program Query throughout. The row should be renamed rather than defended.
2. **The checking vocabulary is cut three ways inside the corpus.** The CLARIAH notes name evaluation, validation and scholarly verification, where validation means conformance to a formal or operational requirement. The English master script names evaluation, technical verification, scholarly or domain validation and acceptance, where validation means domain adequacy and verification means formal conformance. The German Skriptum names technische Verifikation, fachliche und wissenschaftliche Validierung and Acceptance without a separate evaluation level. Verification and validation therefore swap meanings between the CLARIAH notes and the two master texts. This is the sharpest terminological conflict found in this pass and it sits on the matrix row that already carries drift note D3.
3. **Verification Levels against roles and decisions.** The matrix row treats checking as a ladder of levels. The scripts separate three different kinds of object, a procedure (deterministic check, model-assisted review), a role with authority (Critical Expert) and a decision (Acceptance). A level ladder cannot carry the authority column.
4. **Knowledge Document against instruction file and Agent Skill.** The matrix anchors the document class with AGENTS.md and with Agent Skills progressive disclosure. Both scripts separate the three explicitly, a knowledge document describes an object, an instruction file governs recurring work, a skill operationalises a reusable procedure, and a prompt states the current task. The matrix's anchor set currently blurs a distinction the teaching line makes.
5. **Knowledge Document has two definitions in the corpus.** The CLARIAH notes say atomic, structured and verifiable unit of externalised project knowledge. The master script and the Skriptum say bounded, structured and revisable representation distilled from a larger body. Atomic against bounded and verifiable against revisable are different claims, and drift note D4 has to choose.
6. **AI Harness anchors.** All four mined texts anchor the harness to Zhong and Zhu, "AI Harness Engineering," arXiv:2605.13357, 2026. The reference draft anchors it to Anthropic, a practitioner post and METR, and does not cite that paper. The two anchor sets should be merged.
7. **Agentic Engineering anchors.** The reference draft grounds the term in the Sequoia coinage and the ICSE workshop. The scripts define it operatively through the Promptotyping review draft and cite Sapkota et al. The definitions differ in scope, since the corpus definition covers work on data descriptions, specifications, mappings, design decisions and process documents rather than software alone. The deck states that widening explicitly.
8. **Promptotyping literature.** The scripts cite a monograph in review, *Promptotyping. Translating Research Data into Research Artefacts through Context Engineering and Agentic Engineering*, review draft 0.9, 2026, which is the load-bearing source for working context, project knowledge base, distillation, acceptance and epistemic infrastructure. The reference draft does not list it.
9. **Autonomy.** The matrix cites the classical agent definition, in which autonomy is a property of the system. The Skriptum redefines autonomy as the amount of work between two human interventions. Both readings are defensible and they are not the same.
10. **Distillation.** The corpus term collides with the established machine-learning sense in which a smaller model is trained on a larger one. The audience of the teaching line meets both senses, so the glossary entry needs an explicit disambiguation.

## Open points

1. The module assignment of the two opening sections on Applied Generative AI and on constructed research data is undecided in the CLARIAH profile, which leaves the research-data cluster of module 5 provisionally placed.
2. The EU AI Act vocabulary needs its own pass over the VetMedAI workshop script, which was outside the four texts named for this one.
3. Terms of the edition domain that the scripts use without defining were left out here, since they belong to a domain glossary rather than to the engineering vocabulary. They are diplomatic transcription, OCR and HTR, TEI, Character Error Rate, named entity and authority data, segmentation, and codebook. The CLARIAH notes raise the conceptual question whether the recognition task performed by a general multimodal model should still be called OCR or HTR, so at least that pair may need an entry after all.
4. Several terms have no canonical source and are the corpus's own, namely bounded specification, contextually plausible reading, candidate representation, over-distillation, dense and sufficient context, the four levels of output correctness and the governance dilemma. A decision is needed on whether the glossary marks in-house coinages as such, as the reference draft's open points already propose for the latent-program-space row.
5. The German equivalents marked as proposals concentrate in module 1 and module 5, because the German Skriptum has no capability-landscape chapter, no openness section and no LLM-internals chapter. Those German renderings will be set by the Skriptum's own extension rather than by a glossary decision.
