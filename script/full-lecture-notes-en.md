# Knowledge, Context and Agentic Engineering for Knowledge Work

***Lecture Notes***

* Web Resource:  
* [Slides](https://docs.google.com/presentation/d/1FtJpBn8l49I6B-r6b8bdIsbTngLQ9-LdP5BeylXD3M4/edit)

Dr. Christopher Pollin, Digital Humanities Craft OG

## **Abstract**

Frontier large language models (LLMs) increasingly operate within AI harnesses that connect models with files, tools, executable environments and maintained knowledge. These lecture notes examine how such systems reshape **knowledge work**, understood broadly as research, analysis, planning, coding, documentation, decision support and the coordination of complex tasks. They introduce the foundations of contemporary LLMs and distinguish **Prompt Engineering**, **Knowledge Engineering**, **Context Engineering** and **Agentic Engineering** as complementary layers for designing AI supported work.[^1] Research data workflows and digital scholarly editions provide demanding recurring examples because they make provenance, uncertainty, validation and scholarly responsibility particularly visible.

The central argument is that effective work with frontier LLMs depends on more than selecting a capable model or writing an effective prompt. Relevant knowledge must be made explicit and maintained, task specific context must be selected and represented, and multi step work must be organised through an AI harness that provides tools, state, permissions and feedback.[^2] **Promptotyping** integrates these concerns into an iterative method in which maintained project knowledge, requirements, implementation, evaluation and human judgment develop together.[^3]

## **About These Lecture Notes**

These lecture notes accompany the corresponding slide deck and follow its dramaturgy. Each substantive slide is represented by a `##` section. The slides condense concepts, processes, examples and exercises visually, while the notes provide the compact explanation that would otherwise be given during the lecture. Concepts may be introduced orientingly and developed more fully at the point where they become methodologically relevant.

These lecture notes as a whole are framed around **knowledge work** rather than one disciplinary field. Research data workflows and digital scholarly editions remain central examples because they combine heterogeneous sources, structured data, modelling decisions, software, provenance and expert validation. The same engineering distinctions can also be applied to organisational knowledge, coding, strategy, controlling, administration and other information intensive forms of work.

## **Applied Generative AI for Research Data Workflows**

**Applied Generative AI** refers here to the application and adaptation of generative AI methods and systems to domain specific problems, following the broader tradition of applied computer science. The focus is not primarily on developing new foundation models, but on integrating generative AI into existing knowledge practices and examining the methodological consequences of doing so.[^4]

Research data workflows provide a demanding field of application. Generative models can interpret and structure research material, transform data between representations, generate code for deterministic operations and operate inside AI harnesses that provide access to project files, tools and executable environments. Frontier models are particularly relevant because multimodality, reasoning, coding, tool use and agentic capabilities are increasingly combined within the same systems. This does not imply that frontier models are appropriate for every task. Smaller, specialised, local or open weight models may be more efficient, controllable or reproducible for particular purposes.

## **Humanities Research Data Are Constructed through Scholarly Workflows**

**Research data** are analogue or digital representations of research objects, sources, observations or processes that are selected, collected, constructed or produced through scholarly work. They are shaped by research decisions and require sufficient documentation, context and preservation to support scholarly claims, critical assessment, reproducibility and reuse.[^5] In the humanities, this constructed character is especially visible because transcription, annotation, modelling and encoding make particular aspects of a source explicit while leaving others implicit.

A facsimile, a transcription and a TEI representation of the same historical document are therefore not interchangeable. Each is a different representation with different affordances and different forms of uncertainty. The Stefan Zweig notebook *Clarissa* illustrates how facsimile, descriptive metadata, collection context and later modelling together make the object computationally and scholarly usable.

**AI ready data** are data structured and documented for effective use in AI and machine learning workflows. This includes machine readable formats and metadata, clear provenance and usage conditions, and transparent information about quality, uncertainty and potential biases.[^6] AI readiness complements broader research data principles such as FAIR rather than replacing them.[^7]

## **Learning Objectives and Core Concepts**

The learning objectives are to understand how **Prompt Engineering**, **Knowledge Engineering**, **Context Engineering** and **Agentic Engineering** relate to AI supported knowledge work, and how they interact in workflows that involve files, tools, persistent knowledge and multiple execution steps.

**Prompt Engineering** is the iterative design and evaluation of instructions for a specific model and task.[^8] **Knowledge Engineering** creates, curates and maintains explicit knowledge for use by people and AI systems.[^9] **Context Engineering** refers here to the systematic selection, organisation, maintenance and provision of the information an LLM based system requires for its work.[^10] **Agentic Engineering** refers to the systematic organisation of extended work performed by AI agents, including task decomposition, tool use, responses to intermediate results, human intervention and the inspection and continuation of work.[^11]

An **AI agent** pursues a goal through multiple actions and can adapt subsequent actions to intermediate results. An **AI harness** is the technical environment through which an agent receives context, accesses resources, invokes tools, executes actions and obtains feedback. Agentic capability therefore arises from the combined model, harness and environment system rather than from the model alone.[^12]

## **Two AI Supported Research Data Workflows & Epistemic Infrastructures**

Two workflows provide recurring examples. The first processes multilingual printed sources associated with the writings of Jeanne Hersch. Scanned pages are transformed through OCR and layout analysis into structured representations, converted to TEI XML and enriched with information such as named entities and authority data. The second processes handwritten and typed material from the Stefan Zweig collection with multimodal foundation models for transcription and subsequent editorial curation.[^13]

Both workflows combine **probabilistic operations** with **deterministic operations**. A model may propose a transcription, classification or structured representation. Deterministic software can transform data, validate XML, execute tests or check numerical relations. Researchers can compare generated representations with sources, correct them and determine their editorial status.

The surrounding project environment is therefore an **epistemic infrastructure**. Files, project knowledge, schemas, tests, provenance information, model outputs and editorial decisions together establish the conditions under which a generated representation can be inspected, criticised, validated and accepted for a particular purpose.[^3]

## **Which Frontier Models and AI Technologies Do You Use?**

The contemporary LLM landscape contains several overlapping ecosystems. Hosted frontier systems are provided by companies such as Anthropic, OpenAI, Google and xAI. Other important model families include Mistral, Llama, DeepSeek, Qwen and Kimi. Open weight systems can additionally be executed on locally controlled infrastructure with environments such as Ollama or LM Studio. Because relative capabilities, speed and cost change rapidly, continuously updated comparative resources such as Artificial Analysis are useful for locating the current frontier.[^14]

Model choice should not be reduced to benchmark performance. Systems differ in capability, modalities, inference cost, latency, openness, deployment options, context capacity, tool use and the AI harnesses through which they can operate. Hosted proprietary services, open weight models and locally executed systems therefore represent different technical and governance arrangements.

AI harnesses form another layer of this landscape. Claude Code, Codex, Gemini CLI, Mistral Vibe, Qwen Code, Kimi Code, Pi and Cursor connect models with files, tools, state and executable environments. The effective AI system is increasingly a compound system rather than a model considered in isolation.[^12]

## **Frontier LLMs Asymmetrically Amplify Computational Research**

Frontier AI companies increasingly describe research automation as a strategic objective. Jakub Pachocki has publicly described automating research as a major goal at OpenAI, while Dario Amodei has used the image of “geniuses in a data center”. Such statements are not evidence that research has been automated. They indicate, however, the direction in which leading laboratories are attempting to extend model capability.[^15]

Several heterogeneous evaluations show substantial progress in capabilities relevant to computational research. METR measures the duration of software tasks that agents can complete at specified levels of reliability. ARC AGI probes adaptation to unfamiliar tasks. FrontierMath and formal theorem proving examine mathematical reasoning in settings where at least parts of an output can be checked externally. Cyber evaluations probe software understanding, exploration, planning and tool use in executable environments. These evaluations measure different things and should not be collapsed into one scale of intelligence.[^16]

I describe the practical effect as **asymmetric amplification**. Frontier LLMs particularly amplify work where relevant information is digitally represented, actions can be executed through software and the environment can return useful feedback. Coding, data transformation, formal modelling and many computational research workflows have these properties. The effect is asymmetric because it depends on existing expertise, accessible data, technical infrastructure and the ability to assess outputs. The same model can therefore amplify an experienced developer or computational researcher much more strongly than someone working without structured knowledge, tools or evaluative criteria.[^17]

## **LLMs as Jagged Alien “Intelligences”**

The metaphor of **jagged alien intelligence** describes an unfamiliar capability profile rather than consciousness or human like understanding. Frontier LLMs can perform extremely difficult tasks while failing on neighbouring tasks that appear simple to human observers. Their competence is therefore powerful, uneven and difficult to extrapolate.[^18]

Several model properties contribute to this profile. Outputs are probabilistic and can contain plausible but unsupported claims. Models can reproduce biases and display **sycophancy**, a tendency to align an answer with the user’s expressed belief even when this reduces factual reliability. Their internal computations are only partially understood. At the same time, contemporary systems can use tools, work with large contexts, generate and execute code and allocate additional inference time computation to difficult tasks.

Mechanistic interpretability research indicates that model behaviour can depend on structured internal computational pathways that differ substantially from familiar human procedures.[^19] This motivates a theoretical perspective developed later in these notes. LLMs can be understood not only as next token predictors, but also as systems in which training has produced a repertoire of learned transformations or **vector programs**.

## **How Large Language Models Work**

For a more extensive visual introduction, see *Wie LLMs funktionieren*.[^20]

A **large language model** is a neural network trained on very large collections of tokenised data to predict how a sequence continues. In an autoregressive language model, the model estimates a probability distribution over possible next tokens conditioned on the tokens already available in its context. A selected token becomes part of the sequence and therefore influences the next prediction.[^21]

The crucial distinction is that the **training objective is not identical to the capabilities acquired during training**. Next token prediction describes the optimisation problem used in autoregressive language modelling. To perform that objective well across heterogeneous data, the model learns representations and transformations associated with syntax, concepts, relations, styles, code and recurring patterns of reasoning. These structures can subsequently support generation, translation, classification, coding, analysis and reasoning without a separate manually written program for every task.[^21]

The basic objective also does not directly ask whether a proposition is true. It asks which continuation is probable given the available context. Yoshua Bengio uses this distinction to contrast ordinary autoregressive language modelling with his proposed *Scientist AI*, which would explicitly estimate probabilities for hypotheses about the world.[^22] Human generated language contains extensive information about the world, so language modelling can still produce broad world representations. The narrower point is that truth is not identical to the next token objective.

## **Transformer Architecture**

Most contemporary LLMs are based on the **Transformer architecture**. A Transformer processes token representations through repeated layers in which attention mechanisms allow information at different positions in the sequence to influence one another.[^23]

A simple next token diagram such as `cat sat on a → mat` illustrates the output objective, but the probability assigned to `mat` results from transformations across many layers and high dimensional representations. **Self attention** allows the model to construct context dependent representations rather than treating every token independently.

This connection matters for the later engineering chapters. Prompts and context alter the token sequence supplied to the model. That sequence conditions the distributed computation through which the model produces subsequent tokens. Prompting is therefore an intervention on the model’s current computation, not merely a textual wrapper around an otherwise fixed answer.

## **Pretraining and Posttraining**

During **pretraining**, a model learns statistical structure from large and heterogeneous corpora. This process creates broad linguistic, conceptual and procedural representations and can support many capabilities that were not separately programmed.[^21] It is sometimes useful to describe pretraining as building a broad repertoire of knowledge and capabilities, but this remains a simplification because knowledge and capability are entangled throughout model training.

**Posttraining** shapes how that repertoire is expressed in an assistant. Instruction tuning, demonstrations, preference learning, reinforcement learning and related methods can stabilise instruction following, behavioural tendencies and interface specific capabilities.[^24] Contemporary development pipelines may also include intermediate stages between broad pretraining and later alignment training. The boundaries and terminology differ across laboratories and papers.

A useful high level distinction is therefore:

`training → changes model parameters`

`inference → uses the trained parameters for a current interaction`

Ordinary inference does not normally update the model weights. The model can nevertheless adapt strongly to examples, instructions and information supplied in its current context.

## **The Shape of a Wikipedia Article About Zebras**

An LLM does not normally retrieve an addressable copy of a training document when it answers a question. Training changes model parameters so that statistical structure from training data influences later generation. Andrej Karpathy has described this metaphorically as a form of lossy compression. What remains is not the original document but a learned statistical structure that can contribute to later outputs.[^25]

This distinction is important for **parametric knowledge**. A model may produce an accurate description of zebras because its parameters encode patterns learned from relevant material. It cannot thereby provide direct provenance for every generated claim or reconstruct the exact source from which a statement was learned.

Tool use changes the situation. Web search, retrieval systems, files and databases can obtain external information and make selected representations of it available during inference. Three information layers should therefore be distinguished:

`model parameters → learned representations`

`external resources → retrievable information`

`current context → information available for this inference`

The boundary of the model is therefore not the boundary of the complete AI system.

## **Tokenization**

LLMs do not directly process text as semantic words. A **tokenizer** converts character sequences into discrete units called **tokens**. Depending on the tokenizer, one token may correspond to a word, part of a word, punctuation or another recurring sequence. Each token is mapped to a numerical identifier before it enters the neural network.[^26]

Tokenisation is partly an engineering decision. A useful tokenizer balances vocabulary size, sequence length and the ability to represent previously unseen strings. The boundaries it creates are not necessarily linguistically intuitive. A long word may consist of several tokens while a short, frequent sequence may be represented by one token.

The practical consequence is that context windows, input costs and output lengths are measured in tokens rather than words or characters. Tokenisation therefore determines the discrete sequence over which model computation and context limits operate.

## **Embeddings and Contextual Representations**

Tokens are converted from discrete identifiers into continuous numerical representations. **Embeddings** provide the initial mapping into a high dimensional vector space. During training, systematic relations can emerge among representations associated with recurring linguistic and conceptual patterns.[^23]

The familiar illustration in which `dog` and `cat` appear closer than `dog` and `stone` provides a useful first intuition, but it is not a complete account of meaning. Initial embeddings are transformed repeatedly across the network, producing **contextual representations** that depend on surrounding tokens and the current task.

A sentence written in Shakespearean English and a semantically similar sentence written in contemporary English can therefore condition different internal representations and activation patterns. This helps explain why wording matters without assuming that the model stores one fixed meaning for each token. Prompting provides a structured pattern of tokens that participates in selecting and combining learned computations.

## **Prepare the Working Environment before the First Prompt**

Agentic work begins before the first substantive prompt. The first decision is therefore not necessarily how to phrase an instruction, but **where the model is going to work**. An AI harness such as Claude Code, Codex, Gemini CLI or Cursor can provide controlled access to files, a terminal and project specific tools.[^12]

A project workspace should contain relevant source material, project documentation, expected outputs and the context needed to understand the task. Access should remain limited to the intended working boundary. Original sources should remain unchanged, while generated artefacts should be stored separately and connected to sufficient provenance.

Preparing the workspace determines which files, tools, knowledge and forms of feedback later become available to the model or agent. The environment is therefore part of the methodological design rather than neutral technical plumbing.

## **Prompt Engineering**

**Prompt Engineering is the iterative design and evaluation of instructions for a specific model and task.**[^8] A prompt can specify an immediate operation, supply relevant information and constraints, and define the expected form of the result.

The chapter is organised around three additional claims from the slide. First, the engineering focus increasingly shifts from the isolated prompt towards **Context Engineering**. Second, **there is no prompt to rule them all** because prompting effects depend on model, version, task, context and evaluation. Third, these notes adopt the theoretical thesis that prompting can be understood as **finding coordinates in a Latent Program Space**.[^27]

Prompt Engineering therefore remains important, but it is one layer within a larger informational and technical environment.

## **Prompting Is Weird, and Keeps Changing**

Prompt engineering research has repeatedly shown that outputs can change in response to linguistic variations whose relation to the intended task is indirect. Studies have examined emotional framing, incentive language, politeness, formality, concreteness and apparently irrelevant triggers.[^28]

The methodological conclusion is not to memorise individual prompt tricks. Effects found for one generation of models may weaken, disappear or reverse for another. Prompting strategies should therefore be treated as empirical interventions tied to particular model and evaluation conditions.

This also applies to role prompting. A generic expert persona does not add factual knowledge to the model. Roles can still be useful where the task genuinely requires a particular perspective, audience, communicative style or evaluative frame. The broader principle is that prompt effects are contingent rather than universal.

## **Transcribe a Facsimile with Gemini 3.7 Flash**

A Stefan Zweig order slip provides a compact example of a prompt treated as a **bounded specification**. The instruction separates the immediate task, source context, transcription rules and expected output.[^29]

```text
Create a diplomatic transcription of this facsimile

# Context

German order slip from May 1935
Printed form with pencil entries by Stefan Zweig

# Rules

* Transcribe printed and handwritten text
* Preserve spelling, abbreviations, line breaks and field order
* Mark uncertainty as word[?] and illegible text as [...]
* Mark deletions as ~~text~~ and insertions as {text}
* Ignore show through

# Output

Return only the transcription as plain text in reading order
```

The categories can be changed independently. A different source changes the context. A different editorial policy changes the rules. A different downstream workflow may require JSON, XML or TEI rather than plain text. This is not a universal prompt template. It is a transparent way of separating parts of the specification so that they can be inspected and revised.

## **Hands on 1: Transcribe a Facsimile with Gemini 3.7 Flash**

The exercise applies the same structure to a more difficult page from Stefan Zweig’s *Radiovortrag über Newyork*. Participants receive a reusable prompt skeleton and add task relevant source context and at least one rule based on the characteristics of the material.

The exercise has two purposes. First, participants must decide which information is actually useful for the transcription. Second, they must formulate a rule that addresses a plausible failure mode rather than simply increasing prompt length.

A useful additional rule is:

```text
Do not reconstruct or complete words from linguistic context when the reading
is not visually supported by the facsimile. Mark uncertainty instead.
```

The instruction asks the model to preserve explicit uncertainty rather than resolve difficult readings through linguistic plausibility. Whether the rule works has to be assessed against the facsimile.

## **Hands on 1: Transcribe a Facsimile with Gemini 3.7 Flash (Example Result)**

The example prompt adds catalogue and material information about the manuscript, including title, date, language, hand, pagination, collection and shelfmark. It also makes the transcription policy more explicit.

The generated transcription can appear remarkably fluent while individual readings remain wrong. Fluency, grammaticality and internal coherence are therefore not evidence of source fidelity. A model may produce a word that fits the sentence even where the visual evidence supports another reading, or it may fail to express uncertainty where a human editor would hesitate.

The output should consequently be treated as a **candidate representation** that requires comparison with the source. This principle generalises beyond transcription. Model outputs can be valuable because they provide plausible structured candidates, but plausibility is not equivalent to validation.

## **Multimodality & Vision Language Models**

A **Vision Language Model (VLM)** processes visual and linguistic information within the same task. A general purpose multimodal foundation model can therefore receive a facsimile together with an instruction and generate a transcription without being a dedicated OCR or HTR system.[^30]

```text
FACSIMILE                      INSTRUCTION
visual information             task and rules
          \                       /
           \                     /
            VISION LANGUAGE MODEL
                      |
                      v
               TRANSCRIPTION
```

The distinction matters because a VLM does not merely recognise isolated characters. Visual patterns, layout, linguistic context and task instructions can jointly influence the generated output. This flexibility can help with heterogeneous documents, but it creates a characteristic failure mode. Errors may be **contextually plausible rather than locally obvious**.

The ability to transcribe previously unseen handwriting is therefore interesting as a possible emergent capability of large multimodal models. Whether it should technically be classified as emergent depends on the definition of emergence, model scale and the unknown composition of proprietary training data.

## **Prompt Engineering: Finding Coordinates in a Latent Program Space**

These lecture notes adopt a theoretical model inspired particularly by François Chollet’s account of LLM prompting.[^27] The central claim is that an LLM can be understood as containing a large repertoire of **learned computational transformations**, and that prompts act partly as signals that select and combine these transformations.

The terminology used here is:

* **Vector Program**: a learned transformation that realises a capability or behaviour
* **Latent Program Space**: the space of possible learned transformations
* **Program Query**: an address or search signal within that space
* **Prompt Engineering**: external search for an effective address
* **Reasoning / Test Time Compute**: internal search for an effective computation

A Vector Program is not a conventional symbolic program stored as a discrete object inside the model. It is a distributed transformation implemented through high dimensional representations and model parameters. The thesis is nevertheless stronger than a purely rhetorical metaphor. It proposes that useful model behaviours correspond to learned computational structures that can be differentially elicited through prompts and context.

For the transcription example, a Program Query may condition and combine transformations associated with visual recognition, historical language, layout, reading order, document structure and diplomatic transcription policy. Iterative Prompt Engineering is then an external search process in which the user varies the query and evaluates the resulting behaviour.

## **Excursus: Mechanistic Interpretability and Activation Paths**

**Mechanistic interpretability** investigates the internal computations through which neural networks produce behaviour. Attribution graph research has reconstructed partial internal pathways associated with multi step computations, including arithmetic and linguistic processing.[^19]

Related work by Sofroniew and colleagues identifies internal representations associated with concepts described as emotional states. Intervening on vectors associated with concepts such as *desperate* or *calm* can causally alter subsequent model behaviour.[^31]

These findings do not provide a complete empirical map of a Latent Program Space. They do, however, support several elements of the theoretical account. Internal computation is structured rather than undifferentiated, different pathways can contribute to different behaviours, and interventions on representations can change outputs systematically. The Latent Program Space thesis generalises from such findings to an account of how learned computational possibilities may be addressed through prompts and context.

## **.txt → JSON → CSV**

Generative models can be combined with deterministic processing rather than replacing it. The Islington public health example starts with extracted text and tables, transforms relevant information into structured JSON and CSV, and then applies deterministic consistency checks.

This distinction is methodologically important. Recognising a table, interpreting its layout or extracting values from noisy source material may require probabilistic model behaviour. Once values have been represented explicitly, arithmetic relations can be recomputed deterministically.

A recurring workflow pattern is therefore:

`probabilistic interpretation → structured representation → deterministic checking`

Row totals, column totals and other invariants can provide strong feedback. Such checks do not prove that the original source was interpreted correctly, but they can expose internal inconsistencies and focus subsequent human inspection.

## **Training Builds and Shapes the Latent Program Space**

The Latent Program Space is not explicitly hand designed. It develops through several stages of training.

**Pretraining** establishes a broad repertoire of representations, capabilities and behavioural patterns from language, knowledge, code and other training material.[^21] **Model Spec Midtraining** is a recently proposed technique in which, after broad pretraining but before later alignment training, a model is trained on synthetic documents that discuss a Model Spec or Constitution. The objective is to influence how subsequent alignment training generalises.[^32] Midtraining is therefore a useful category here, but it is not a universally standardised phase across all model providers.

**Posttraining** shapes how the learned repertoire is expressed in an assistant. Demonstrations, preference learning, reinforcement learning and related methods can stabilise instruction following, behavioural tendencies and interface specific capabilities such as tool calling.[^24]

At **inference** time, prompts and context condition and combine parts of the trained repertoire for a particular task. An **AI Harness** extends the effective system by providing tools, state, feedback, permissions and control for agentic work.[^12]

## **The Assistant Is a Character Generated by the Model**

The **Assistant** encountered in a conversational interface should not simply be equated with the underlying neural network. Providers shape assistant behaviour through training, runtime instructions, policy layers and product design. Anthropic provides an unusually explicit example because it describes Claude in terms of a cultivated **character** and publishes a Constitution that states intended values and behavioural dispositions.[^33]

These notes use the distinction as an ontological and practical working model. The model can represent and generate many possible styles and behavioural patterns. “Claude” refers to a particular assistant character that Anthropic attempts to strengthen and stabilise through training and system design. This formulation follows Anthropic’s own public account, while remaining neutral about stronger claims concerning consciousness or subjective experience.[^33]

Models are extensively trained on human communication and can therefore generate convincing social behaviour. Clear and constructive communication can improve interaction, but social fluency, confidence and empathy are not evidence that the system is a human interlocutor or that its claims are correct.

## **How Anthropic Shapes Claude’s Assistant Character**

Anthropic’s **Claude Constitution** is a public description of the values and behaviour the company aims to cultivate in Claude. It is not simply a runtime system prompt. Anthropic states that the Constitution is used at various stages of training and can be used to construct synthetic data, responses and rankings for future training.[^34]

This distinction separates three layers. **Training artefacts**, such as a Constitution or Model Spec, can shape what is learned during model development. **Character training and posttraining** can stabilise behavioural tendencies and assistant dispositions. **System prompts** operate at runtime and provide instructions within a particular deployment context.[^35]

Claude’s behaviour is therefore produced by the interaction between trained model parameters and current runtime context. The Constitution, character training and system prompt are related, but they are not technically the same thing.

## **Prompting Strategies: There Is No Prompt to Rule Them All**

No single prompting strategy performs optimally across all models, tasks and evaluation settings. Effective prompting is better understood as a combination of several practices rather than the discovery of one universal prompt.[^8]

* **Organize the Context**: provide relevant information at the right time and in a usable form.
* **Structure the Prompt**: separate task, source context, rules and output contract.
* **Iterate and Evaluate**: compare variants on fixed examples and explicit criteria.
* **Use Reasoning Selectively**: match inference time reasoning to the complexity and evaluability of the task.[^36]
* **Counter Sycophancy**: require evidence, alternatives or independent critical review where agreement with the user could bias the result.
* **Generate, Compare and Reconcile**: produce independent candidates, inspect their differences and adjudicate the result.

Effective prompting therefore combines **context selection, instruction design, inference strategy and evaluation**. This already moves beyond the prompt itself and leads directly to Knowledge and Context Engineering.

## **Knowledge & Context Engineering**

Complex knowledge work contains more relevant information than should be placed into a single prompt. Project goals, documents, data, policies, requirements, examples, design decisions, previous findings, unresolved questions and validation criteria may all matter, but they do not all matter at the same time.

**Knowledge Engineering** organises the persistent informational basis. It makes relevant knowledge explicit, inspectable and revisable so that people and AI systems can work from a maintained state rather than from undocumented assumptions.[^9] **Context Engineering** constructs the task specific information state from that broader environment.[^10]

The distinction can be expressed through three questions:

`Knowledge Engineering → What does the project or organisation know?`

`Context Engineering → What does the model or agent need now?`

`Prompt Engineering → What should the model or agent do now?`

Knowledge work therefore becomes an engineering problem of maintaining available knowledge and providing the right subset of that knowledge for a particular action.

## **Knowledge Engineering**

**Knowledge Engineering** refers here to the systematic construction and maintenance of explicit, revisable knowledge for use by people and AI systems. In project settings, it records the current understanding of relevant data, purpose, requirements, decisions, uncertainty and process knowledge.[^9]

The shift in focus is:

`files → maintained knowledge`

A collection of documents is not automatically a usable knowledge base. Information may be duplicated, contradictory, outdated, locally structured or understandable only through tacit background knowledge. Knowledge Engineering therefore concerns not only storage, but acquisition, structuring, curation, provenance, revision and governance.

The conceptual goal is to make knowledge **explicit, inspectable and revisable**.

## **“I Know Things”**

Knowledge can exist without being explicitly documented, shared or usable by an AI agent. Experts often rely on tacit distinctions, remembered decisions, local file structures, disciplinary conventions and experience that are not represented in a form another person or system can inspect.[^37]

This becomes a practical limitation for AI supported work. A model cannot reliably use information that remains only in someone’s memory, and an agent cannot reconstruct project conventions that were never documented. The problem is therefore not simply whether information exists somewhere, but whether relevant knowledge has been externalised in a usable and revisable form.

Knowledge Engineering starts from this gap between **knowledge possessed** and **knowledge operationally available**.

## **Why Knowledge Must Be Made Explicit**

Implicit and fragmented knowledge can be distributed across documents, datasets, notes, working practices and individual people. Existing local order does not automatically become a shared and system wide knowledge base. Statements may be incomplete, contradictory, outdated or intelligible only within their original context.[^37]

Persistent project knowledge addresses this by representing relevant concepts, decisions and uncertainties explicitly. Humans and LLM based systems can then refer to the same documented state. Statements can be criticised, updated and linked to evidence, while changes remain visible through versioning.

The central principle is therefore:

**Knowledge Engineering makes relevant knowledge explicit, inspectable and revisable.**

## **Knowledge Modelling, Personal Information Management and Project Management**

The form of Knowledge Engineering developed here draws on several neighbouring traditions. Classical **knowledge modelling** identifies concepts in a domain, represents relations and supports querying or inference.[^9] **Personal Information Management** studies how people acquire, organise, maintain, retrieve, use and share information across formats and locations, with fragmentation as a recurring problem.[^38] **Project management** contributes procedures for initiating, planning, executing, monitoring and closing work within explicit constraints.[^39]

AI supported knowledge work combines concerns from all three. It needs domain representations, usable information collections and operational project state. A maintained knowledge environment may therefore contain conceptual definitions, source references, requirements, decisions, process descriptions, instructions, open questions and evaluation criteria.

The goal is not to collapse these traditions into one discipline. It is to recognise that advanced work with AI agents requires aspects of all three.

## **Context Engineering**

**Context Engineering refers here to the systematic selection, organisation, maintenance and provision of the information an LLM based system requires for its work.**[^10]

The shift in focus is:

`prompt → working context`

Context Engineering extends Prompt Engineering from the design of an immediate instruction to the wider informational environment in which the instruction is interpreted. It concerns what information is available, how it is represented, in which order it appears, which resources can be retrieved and what is deliberately omitted.

The core principle is therefore not accumulation but selection:

**the right information, in the right representation, at the right time.**

## **Context Engineering Shapes the Model’s Working Context**

The **context window** is the finite token based working space available to a model during inference. It contains the supplied input and those previously generated tokens that remain in the active sequence. Through self attention, the model can relate information within this bounded context when generating subsequent tokens.[^23]

The context window should be distinguished from the **context** itself. The window is the technical capacity. The context is the information currently represented within it. **In context learning** refers to the ability of a model to adapt its behaviour to instructions, examples and information supplied in the context without changing model parameters.[^21]

For agentic work, a third concept is useful. The **Working Context** is the task specific configuration of information, documents, data access, instructions, tools and current state made available for a particular assignment.[^3] Not every component must itself be serialised into tokens. An agent may access a file or database through a tool while only selected results enter the immediate model context.

## **Context Rot**

A large context window does not guarantee that all information inside it will be used equally well. **Context Rot** describes observed degradation in a model’s ability to retrieve and apply relevant information as contexts become longer, denser or more distracting.[^40]

The empirical pattern varies across models and tasks. Context Rot should not be reduced to one established causal mechanism such as a simple decline in the precision of attention. Position effects, distractors, conflicting information, obsolete intermediate state and the structure of the task can all contribute to degraded long context performance.

The practical implication is important. More context is not automatically better context. The objective is not to keep the context short at all costs, but to keep it **dense, relevant and sufficient** for the task.

## **Selecting, Structuring and Distilling Knowledge**

**Context Compression** can initially be understood as reducing the amount of information that enters an active Working Context. This may involve selecting relevant passages, summarising material, removing repetition, aggregating data or retaining only representative examples.[^3]

**Distillation** is a stronger operation. It does not merely reduce token count. It transforms an existing understanding into a selective, structured and inspectable representation that remains sufficient for a particular purpose. Relevant concepts, relations, conditions, uncertainties, rationales and open questions should be preserved where they matter.[^3]

The same source material can therefore be distilled differently for different tasks. A general introduction, an implementation specification and a verification task require different representations of the same underlying knowledge. Distillation is task dependent and epistemically consequential because every reduction determines which distinctions remain available for subsequent work.

## **Markdown Makes Document Structure Explicit for LLMs**

**Markdown** is a lightweight markup language that represents document structure directly in human readable plain text. Headings, lists, links, emphasis, tables and code blocks require comparatively little syntax, which makes the structure visible both to humans and to language models.[^41]

This can be useful for project knowledge because the same file can be read directly by a person, placed under version control, linked from other documents and supplied to an LLM without complex conversion. Compared with the internal XML representation of a word processing document, Markdown exposes a useful structural layer with substantially less markup overhead.

Markdown is not intrinsically superior to richer formats. TEI, XML, JSON, RDF, databases, schemas and configuration files remain preferable where their semantics or formal constraints are required. Markdown is simply a practical serialization for many forms of documentary project knowledge.

## **Knowledge Documents**

A **knowledge document** is a bounded, structured and revisable representation of relevant knowledge, distilled from a larger body of sources, data or experience, maintained for human inspection and made available for use by LLM based systems as context.[^3]

Useful knowledge documents are **bounded**, because they address a defined subject or function. They are **structured**, because relevant concepts, relations, rules, conditions and uncertainties are organised explicitly. They are **revisable**, because they remain readable, criticisable, extensible and correctable. They are **dual readable**, because humans can inspect and edit them while AI systems can use them as context. They are **compact but sufficient**, because redundancy is reduced without removing distinctions necessary for their intended purpose.

The conceptual artefact should be distinguished from its technical representation. **The knowledge document is the concept. Markdown is one possible serialization.**

## **Project Knowledge Base and Working Context**

Knowledge documents can form part of a larger **Project Knowledge Base**. In Promptotyping, the Project Knowledge Base is the persistent, inspectable and revisable body of maintained project knowledge. It records the project’s current understanding of its data and purpose together with requirements, decisions, uncertainties and process knowledge.[^3]

The Project Knowledge Base must be distinguished from the **Working Context**. The Working Context contains the information and access required for a specific task. It may include the task description, selected knowledge documents, examples, data access, agent instructions, tool descriptions, permissions, current results and feedback.[^3]

Not every relevant object must be fully loaded into the context window. An agent can use tools to inspect complete datasets or files while only summaries, query results or selected excerpts enter the active token sequence.

The central distinction is therefore:

`Project Knowledge Base → preserves available knowledge`

`Working Context → provides what is needed for this task`

## **As a … I Want to**

User stories provide a compact requirements engineering format for expressing how a person should be able to work with an artefact:

```text
As a ...
I want to ...
so that I can ...
```

The format makes three questions explicit. Who is acting? What capability is required? Why does the capability matter? In research software, this connects implementation requirements directly to scholarly practice.[^42]

A liturgy scholar may want to compare the structure of an office across several *Libri Ordinarii* to identify regional differences. A social historian may want to compare network change across several decades to investigate changing economic relationships. The data model alone does not determine these operations. Requirements arise from the relation among data, research questions and scholarly practices.

## **Persona Engineering: “You Are a …”**

A persona can be used as a structured perspective for evaluation or requirements work. The purpose is not to make the model “become” a real person, but to define a consistent set of characteristics from which it should inspect an artefact or scenario.[^43]

For example, a workshop guide can be evaluated from the perspective of a participant with strong disciplinary expertise but little experience with terminals, Git or development environments. The model can then identify unexplained terms, likely points of confusion and steps that may require support.

Such synthetic personas are useful as an exploratory method, but they are not substitutes for actual users or empirical user research. Their value lies in making assumptions about intended users explicit and creating additional perspectives for review.

## **Mapping Mobile Musicians**

*Mapping Mobile Musicians* provides an example of how maintained knowledge and project specific artefacts can support several distinct scholarly activities. The project can be understood through four operations: **capture**, **curate**, **understand** and **explore**.

These operations require different representations and different working contexts. Capturing source information requires attention to provenance and extraction. Curation requires decisions about entities, relations and uncertainty. Understanding requires domain context and interpretation. Exploration requires interfaces and analytical operations that reflect scholarly questions.

The example therefore illustrates why an AI supported knowledge environment cannot be reduced to a single prompt or one static database. Different phases of work require different combinations of data, knowledge, tools and validation.

## **Promptotyping**

**Promptotyping** is an iterative, knowledge driven method for developing project specific digital research artefacts from structured research data and maintained project knowledge through Context Engineering and Agentic Engineering.[^3]

The method starts from the observation that project specific requirements often cannot be completely specified before implementation. A provisional artefact can make assumptions and possibilities visible, reveal limitations of the underlying data and allow researchers to compare alternative operationalisations.

Implementation therefore becomes part of enquiry. LLM based agents can reduce parts of the implementation effort, while domain experts remain responsible for the consequential judgments through which requirements, representations and resulting artefacts are assessed.[^44]

## **Promptotyping as an Iterative Knowledge Loop**

The organising structure of Promptotyping is an evolving and versioned Project Knowledge Base. For a particular assignment, relevant knowledge and resource access are selected into a Working Context. An AI agent then develops or revises an artefact inside an executable project environment.[^3]

Implementation produces observations, errors and new questions. These findings do not automatically become project knowledge. They are inspected and, where warranted, written back into the maintained knowledge base.

```text
MAINTAINED PROJECT KNOWLEDGE
            ↓
      WORKING CONTEXT
            ↓
    AGENTIC IMPLEMENTATION
            ↓
         ARTEFACT
            ↓
 EVALUATION AND EXAMINATION
            ↓
      CURATED WRITE BACK
            ↓
     REVISED KNOWLEDGE
```

The prompt is one operational component inside this loop rather than its persistent centre.

## **Scholar Centred Design and Requirements Engineering**

In research settings, requirements should be developed through sustained engagement with scholars, source material and the modelling decisions through which data were produced. **Knowledge Acquisition** may therefore include workshops, expert interviews, literature review, direct examination of research data and the creation of provisional personas and user stories.[^42]

This approach is described here as **Scholar Centred Design**. It does not imply that every design preference of a researcher should be implemented literally. The purpose is to make the relation between scholarly questions, data affordances and digital operations explicit enough to be inspected and negotiated.

Requirements Engineering then translates this knowledge into operational specifications, including user stories, acceptance criteria, constraints and dependencies. These specifications can themselves become maintained project knowledge and later form part of an agent’s Working Context.

## **Spec Driven Development**

**Spec Driven Development** places an explicit specification between exploratory discussion and implementation. Instead of asking an agent to “build something useful”, the workflow develops a structured account of requirements, user stories, data constraints, interfaces and verification criteria before substantial implementation begins.

The specification should be contextualised by the maintained knowledge environment rather than treated as a detached document. Data descriptions, research knowledge, design decisions and validation rules can remain in dedicated knowledge documents while the specification references the parts relevant to the implementation task.

This reduces the amount of tacit interpretation delegated to the agent and creates a clearer object for review before code or other artefacts are produced.

## **Agentic Engineering**

**Agentic Engineering refers here to the systematic organisation of extended work performed by LLM based AI agents.**[^11] It concerns how tasks are bounded, decomposed and coordinated, how agents use tools, how they respond to intermediate results, when human intervention is required and how work can be inspected and continued.

The principal shift is:

`response → trajectory`

A chatbot interaction can often be evaluated through a single response. An agentic system produces a **trajectory** containing observations, intermediate decisions, tool calls, file modifications, execution results and subsequent actions. Reliability therefore depends on the organisation of the complete trajectory.

A simplified loop is:

`observe → plan → act → inspect → update`

Agentic Engineering is therefore about **engineering trajectories, not answers**.

## **Why Multi Step Work Must Be Organised**

An AI agent pursues a goal across several model and tool calls. It may read and modify files, execute programs, inspect outputs and select subsequent actions according to errors and feedback from the environment.[^11]

This extended work creates organisational requirements. Tasks must be bounded and decomposed. Tools, permissions and stopping conditions must be defined. Intermediate results must be inspected and, where necessary, escalated to people. Project state must remain understandable across several steps.

The core point is that agentic capability is not simply “more autonomy”. It is a new engineering surface in which context, state, tools, control and evaluation have to be coordinated over time.

## **AI Harness**

An **AI harness** is the technical software environment through which an LLM based agent receives context, accesses project resources, invokes tools, acts within a working environment and processes feedback. The harness also manages state, permissions and parts of the control flow.[^12]

Examples include Claude Code, Codex, Cursor and Pi. Depending on the environment, an agent may inspect and modify files, invoke shell commands, run programs, use web or database tools and interpret the resulting output.

The harness should not be confused with the model. A capable model in a weak harness may be unable to inspect or verify the consequences of its actions. Conversely, tools, tests, persistent state and well designed feedback can make the complete system substantially more capable and more inspectable than model evaluation alone would suggest.

## **AI Agents Existed Long Before LLMs**

The concept of an **intelligent agent** predates large language models by decades. Classical work defines agents through their relationship with an environment and their capacity for autonomous, reactive and goal directed action.[^45]

Wooldridge and Jennings identify properties such as autonomy, reactivity, proactiveness and social ability. Earlier AI systems such as AlphaGo and multi agent reinforcement learning environments demonstrate that agency is not intrinsically tied to language models.

LLMs changed the practical design space because natural language, code and heterogeneous digital resources can now become part of a common interface for planning and action. Systems such as *Voyager* demonstrated how an LLM can guide an embodied agent through repeated interaction with a complex environment.[^46]

LLM based agents should therefore be understood as a contemporary form of a much older AI concept.

## **AI Agent**

In these notes, an **AI agent** is an LLM based system that pursues a goal through a sequence of tool supported actions and adapts subsequent actions to intermediate results.[^11]

A simple chatbot pattern can be represented as:

`user input → LLM → response`

An agentic pattern is closer to:

`goal → model ↔ tools ↔ environment ↔ feedback → further action`

The distinction does not require complete autonomy. Contemporary agents normally operate inside human defined goals, tools, permissions and stopping conditions. What matters is that the model participates in selecting and coordinating multiple actions rather than producing only one terminal response.

## **AI Harness Architecture**

A useful systems perspective treats the harness as the runtime substrate that enables a foundation model to operate as an agent. Zhong and Zhu argue that software engineering capability arises from a **model, harness and environment system** rather than from the model in isolation.[^12]

The harness can manage task specification, context selection, file and tool access, action execution, current state, feedback, permissions, verification and intervention points. This changes what should be evaluated. A final patch, document or answer provides only partial evidence about the process that produced it.

A stronger harness can preserve execution traces, test results, failure information and other evidence that makes an agentic trajectory inspectable and easier to continue or correct.

## **AI Agent Concepts**

Several technical concepts recur across contemporary agent systems. **Tool Use** connects models with executable functions and external resources. **AI Harnesses** organise the runtime environment. **Instruction files** such as `AGENTS.md` or `CLAUDE.md` provide persistent project guidance. **Agent Skills** package reusable procedural knowledge. **MCP** standardises connections to tools and resources. **A2A** standardises communication among independent agents. **Subagents** provide isolated contexts for delegated tasks.[^47]

These concepts solve different problems. They should not be treated as interchangeable labels for “agent functionality”. The engineering task is to decide which mechanism should carry which type of information or capability.

## **Tool Use**

Tool use allows an LLM based system to obtain information or perform operations that cannot be reduced to text generation. Tools may include file access, web search, databases, code execution, validators, browsers, APIs and specialised software.

Tools are especially important when they return evidence about the consequences of an action. A model can propose code, but a compiler, test suite or executable environment can provide deterministic feedback. A model can propose XML, while a schema validator can determine whether the document conforms to formal constraints.

Tool use therefore changes the epistemic structure of the workflow. The system is no longer relying only on model generated text. It can obtain external observations that constrain subsequent actions.

## **AGENTS.md and CLAUDE.md**

`AGENTS.md` is an open Markdown based format for providing coding agents with project specific instructions such as setup commands, tests, code conventions and repository guidance.[^48] `CLAUDE.md` is the corresponding Claude Code mechanism for persistent project, user or organisation level instructions.[^49]

The formats should not be collapsed. Different tools implement different discovery and precedence rules. Claude Code reads `CLAUDE.md` natively and can import an existing `AGENTS.md`; the broader `AGENTS.md` format is intended to work across many coding agents.[^48][^49]

The methodological principle is broader than either file name. Information that should guide an agent repeatedly should not have to be typed into every prompt. Persistent instruction artefacts externalise stable working rules and make them inspectable and versionable.

## **Global CLAUDE.md**

Claude Code supports persistent instructions at several scopes. User level instructions can be stored in `~/.claude/CLAUDE.md` and apply across projects, while organisation managed policies and local variants provide additional layers.[^49]

A global or user level instruction file should contain information that is genuinely stable across projects, such as preferred working practices, communication conventions or general completion criteria. Project specific facts should remain in the project environment rather than being duplicated globally.

This is not a hard security mechanism. Claude Code documentation explicitly distinguishes behavioural guidance in `CLAUDE.md` from permissions and hooks, which can enforce technical boundaries independently of model compliance.[^49]

## **Project Specific CLAUDE.md**

A project specific `CLAUDE.md` can be stored at the repository root or in `.claude/CLAUDE.md`. It provides persistent project context such as architecture, build and test commands, conventions and workflows.[^49]

A compact project instruction file might contain a role and working mode, implementation principles, explicit completion criteria and references to more detailed project knowledge. For example, it can require that verification be run before a task is reported as complete and that any unavailable verification is stated explicitly.

Claude Code treats these files as context, not as infallible configuration. Project instructions therefore need to remain concise, specific and internally consistent. Procedural content that is only relevant for particular tasks may be better represented as a Skill rather than loaded in every session.[^49]

## **Agent Skill**

An **Agent Skill** is a reusable folder containing a `SKILL.md` file and, optionally, scripts, references and assets for a particular capability or workflow.[^50] Skills are procedural artefacts rather than merely descriptive knowledge documents.

The Agent Skills specification uses **progressive disclosure**. At session start, the agent can receive only the name and description of available skills. The full instructions are loaded when the skill becomes relevant, and additional resources can be loaded later as required.[^50]

This design helps control context consumption. A system can maintain many specialised capabilities without injecting all instructions into every task. Examples include skills for producing a PowerPoint presentation, reviewing a legal document or applying a project specific data transformation procedure.

## **Model Context Protocol (MCP)**

The **Model Context Protocol (MCP)** is an open standard for connecting AI applications with external tools, data sources and workflows through a common protocol.[^51] Rather than building a different connector for every combination of agent and external system, MCP defines common client and server interactions.

An MCP server can expose resources, prompts and tools. An MCP compatible client can discover and invoke these capabilities through standardised messages. The protocol therefore addresses an integration problem rather than a reasoning or knowledge modelling problem.

MCP is useful for Agentic Engineering because it can make external resources available through a consistent interface. It does not itself decide which resource is relevant, whether the data are reliable or whether an action should be permitted.

## **A2A (Agent to Agent)**

The **Agent2Agent Protocol (A2A)** is an open protocol for communication and collaboration among independent agents. It supports agent discovery, task management and the exchange of information or results without requiring one agent to expose its internal memory, tools or proprietary implementation.[^52]

A2A and MCP address complementary interaction surfaces. MCP primarily standardises how an agent interacts with tools and resources. A2A primarily standardises how independent agents collaborate as peers.[^52]

Multi agent interoperability can be useful where tasks are genuinely distributed across specialised systems. It also increases coordination and verification requirements. More agents create more possible handoffs, divergent assumptions and failure points.

## **Subagents**

A **subagent** is a delegated agent instance used for a bounded part of a larger task. A subagent can operate with its own fresh context, inspect a defined subset of resources and return a compact result to the parent agent.

This pattern is useful for two reasons. First, it can protect the parent context from large volumes of intermediate information. A subagent may inspect hundreds of files and return a structured synthesis instead of copying all file contents into the parent context. Second, independent subagents can execute parallelisable checks or analyses.

Subagents are an architectural pattern rather than one universally standardised protocol. Their value depends on task decomposition, information boundaries and the quality of the returned evidence. Delegation does not remove the need to validate results.

## **Model Routing**

Agentic workflows can route different phases of work to different models. Planning, implementation and review do not necessarily require the same model or the same inference budget.

One useful pattern is:

`research → specification → implementation → review → revision`

Planning and review can be assigned to a model selected for stronger reasoning, while implementation can be assigned to a model that offers a favourable balance of coding capability, latency and cost. The resulting specification remains contextualised by project knowledge rather than becoming an isolated prompt.

Model routing should be treated as an engineering decision that can change as models evolve. The important abstraction is the separation of functions and evaluation criteria, not any particular provider combination.

## **Subagents and Epistemic Infrastructure**

A multi agent workflow becomes methodologically interesting when specialised agents operate against an explicit **epistemic infrastructure**. For example, one agent may coordinate several independent reviewers that inspect TEI XML using project knowledge, schemas and deterministic Python scripts.

The additional agents do not create truth by voting. Independent review can expose disagreements, locate suspicious cases and distribute inspection across different contexts. The evidence returned by schemas, tests, source comparisons and domain specific knowledge remains more important than model agreement by itself.

The purpose of multi agent orchestration is therefore to create structured trajectories of independent work and feedback, not merely to multiply model calls.

## **Why AI Agents Need Context**

As agentic trajectories become longer, the quality of context becomes increasingly important. Long running work accumulates intermediate outputs, errors, tool results and previous decisions. If all of this remains in one undifferentiated context, the agent may spend substantial effort navigating its own history rather than solving the current task.[^40]

Persistent knowledge and task specific context provide a way to manage this problem. Stable knowledge can remain outside the transient conversation. Relevant parts can be loaded or retrieved when needed. Completed stages can produce compact artefacts that later stages consume rather than carrying every intermediate token forward.

The target is therefore not the shortest possible context. It is a **dense and sufficient Working Context** that contains what is required for the current step while preserving access to the wider project environment.

## **Context Window, Context Rot and Distillation**

The **Context Window** is the finite token based capacity available to a model during inference. It is a technical limit, not a target for how much information should be supplied.[^23]

**Context Rot** describes the empirical observation that the effective use of information can deteriorate as active contexts become longer or more cluttered.[^40] **Context Engineering** therefore selects, organises and provides information under finite computational constraints.[^10]

**Context Compression** reduces the amount of information entering an active context. **Distillation** goes further by producing a selective, structured and inspectable representation that preserves the distinctions needed for a particular purpose.[^3]

The overall architecture can be expressed as:

```text
PROJECT KNOWLEDGE BASE
persistent, inspectable and revisable knowledge

            ↓ selection and distillation

WORKING CONTEXT
task specific information, instructions, access and state

            ↓ representation

CONTEXT WINDOW
the tokenised information currently available to the model
```

The knowledge base preserves what is available to be known. Context Engineering constructs from that environment what the model or agent needs for the current task.

## **Evaluation, Verification, Validation and Acceptance**

AI supported workflows require several forms of assessment that should remain conceptually distinct. **Evaluation** is the broader measurement or assessment of outputs, models or workflows against explicit criteria. It may be quantitative or qualitative and can include benchmark scores, error rates, task completion measures or structured expert review.[^53]

**Technical Verification** asks whether an artefact conforms to specified or formalised requirements. Examples include schema validation, deterministic mappings, test suites, numerical consistency checks and executable acceptance criteria. Verification can often be automated because the relevant conditions have been formalised.[^54]

**Scholarly or domain Validation** asks whether a representation, interpretation or artefact is adequate to the source, purpose and disciplinary context. A TEI document can be technically valid while still encoding a historically unjustified interpretation. Validation therefore often requires domain expertise and cannot always be reduced to a deterministic test.[^3]

**Acceptance** is the responsible decision to use an identified state for a specified purpose. An artefact may be verified and validated to a particular degree while still requiring an explicit decision about whether the available evidence is sufficient for publication, analysis or operational use.[^3]

## **Critical Expert and Epistemic Infrastructure**

AI supported work does not remove the need for expertise. It changes where expertise is applied. Experts define research or organisational purposes, externalise relevant knowledge, establish modelling distinctions, determine constraints, design evaluation criteria and decide how evidence should affect the status of an output.

A **Critical Expert** is therefore not merely a person who manually checks everything a model produces. The role is to design and maintain the epistemic conditions under which model generated and deterministic outputs can be interpreted. This includes provenance, validation rules, acceptance criteria and procedures for handling uncertainty.[^3]

The complete system can be understood as an **epistemic infrastructure** in which knowledge documents, source data, schemas, tests, software tools, AI agents, project state and human judgment work together. The central question is not only whether a model can produce an output, but under which technical and epistemic conditions that output can be inspected, justified and used.

## **Conclusion**

The practical significance of contemporary frontier LLMs for knowledge work does not lie in a single prompting technique. It lies in the interaction of capable models with explicit knowledge, managed context, tools, executable environments, feedback and responsible human judgment.

**Prompt Engineering** specifies and evaluates the immediate instruction. **Knowledge Engineering** builds and maintains the available body of explicit knowledge. **Context Engineering** constructs the task specific information state required for the current work. **Agentic Engineering** organises multi step trajectories in which agents use tools, inspect state and respond to feedback. **Promptotyping** integrates these layers into an iterative process in which implementation and evaluation can produce curated revisions to maintained knowledge.[^3]

The resulting shift is from individual model outputs towards the design of complete technical and epistemic environments for knowledge work. Frontier models can asymmetrically amplify computational work where knowledge can be externalised, actions can be executed through software and outputs can be checked. This does not eliminate human responsibility. It increases the importance of making assumptions, provenance, transformations, verification, validation and acceptance inspectable within the workflow.

## **References**

Allen, Bradley P., et al. “Knowledge Engineering Using Large Language Models.” *Transactions on Graph Data and Knowledge* 1, no. 1, 2023. https://doi.org/10.4230/TGDK.1.1.3.

Anthropic. “Claude’s Character.” https://www.anthropic.com/research/claude-character.

Anthropic. “Claude’s Constitution.” 2026. https://www.anthropic.com/constitution.

Anthropic. “Claude’s New Constitution.” 2026. https://www.anthropic.com/research/claude-new-constitution.

Anthropic. “Effective Context Engineering for AI Agents.” 2025. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents.

Bengio, Yoshua. “Godfather of AI: How To Make Safe Superintelligent AI.” Interview with Rob Wiblin. *80,000 Hours*, 2026. https://youtu.be/PZqDFs2sbiY.

Brown, Tom B., et al. “Language Models are Few Shot Learners.” 2020. https://arxiv.org/abs/2005.14165.

Chollet, François. “How I Think About LLM Prompt Engineering.” 2023. https://fchollet.substack.com/p/how-i-think-about-llm-prompt-engineering.

Dell’Acqua, Fabrizio, et al. “Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality.” *Organization Science* 37, no. 2, 2026, 403 to 423. https://doi.org/10.1287/orsc.2025.21838.

Gans, Joshua. “A Model of Artificial Jagged Intelligence.” 2026. https://doi.org/10.48550/arXiv.2601.07573.

Geiger, Philipp. “Daten / Forschungsdaten.” 2024. https://doi.org/10.17175/wp_2023_003_v2.

Hong, Kelly, Anton Troynikov, and Jeff Huber. *Context Rot: How Increasing Input Tokens Impacts LLM Performance*. Chroma, 2025. https://research.trychroma.com/context-rot.

Jones, William, Jesse David Dinneen, Robert Capra, Anne R. Diekema, and Manuel A. Pérez Quiñones. “Personal Information Management.” 2017. https://doi.org/10.1081/E-ELIS4-120053695.

Li, Chloe, Nevan Wichers, Sara Price, Samuel Marks, and Jon Kutasov. “Model Spec Midtraining: Improving How Alignment Training Generalizes.” 2026. https://arxiv.org/abs/2605.02087.

Lindsey, Jack, Wes Gurnee, Emmanuel Ameisen, et al. “On the Biology of a Large Language Model.” Transformer Circuits, 2025. https://transformer-circuits.pub/2025/attribution-graphs/biology.html.

Majithia, A., et al. “An Actionable Framework for AI Ready Data.” 2026. https://doi.org/10.1002/aaai.70054.

Mei, Lingrui, Jiayu Yao, Yuyao Ge, et al. “A Survey of Context Engineering for Large Language Models.” 2025. https://doi.org/10.48550/arXiv.2507.13334.

Ouyang, Long, et al. “Training Language Models to Follow Instructions with Human Feedback.” 2022. https://arxiv.org/abs/2203.02155.

Pollin, Christopher. *Modelling, Operationalising and Exploring Historical Information. Using Historical Financial Sources as an Example*. Graz, 2025. https://resolver.obvsg.at/urn:nbn:at:at-ubg:1-220602.

Pollin, Christopher. “Asymmetric Amplification. Why AI Does Not Automate Research, But Disruptively Amplifies Computer Based Research Work.” Digital Humanities Craft, 2026. https://dhcraft.org/excellence/blog/Asymmetric-Amplification.

Pollin, Christopher. *Promptotyping. Translating Research Data into Research Artefacts through Context Engineering and Agentic Engineering*. Review draft 0.9, 2026.

Russell, Stuart J., and Peter Norvig. *Artificial Intelligence: A Modern Approach*. 4th ed. Pearson, 2020. https://aima.cs.berkeley.edu.

Sapkota, Ranjan, Konstantinos I. Roumeliotis, and Manoj Karkee. “AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges.” *Information Fusion* 126, 2025, 103599. https://doi.org/10.1016/j.inffus.2025.103599.

Schulhoff, Sander, Michael Ilie, Nishant Balepur, Konstantine Kahadze, Amanda Liu, et al. “The Prompt Report: A Systematic Survey of Prompting Techniques.” 2024. https://doi.org/10.48550/arXiv.2406.06608.

Sofroniew, Nicholas, Isaac Kauvar, William Saunders, et al. “Emotion Concepts and Their Function in a Large Language Model.” 2026. https://transformer-circuits.pub/2026/emotions/index.html.

Summerfield, Christopher. *These Strange New Minds: How AI Learned to Talk and What It Means*. Viking, 2025.

Vaswani, Ashish, Noam Shazeer, Niki Parmar, et al. “Attention Is All You Need.” *Advances in Neural Information Processing Systems* 30, 2017. https://arxiv.org/abs/1706.03762.

Wang, Guanzhi, Yuqi Xie, Yunfan Jiang, et al. “Voyager: An Open Ended Embodied Agent with Large Language Models.” 2023. https://arxiv.org/abs/2305.16291.

Wilkinson, Mark D., et al. “The FAIR Guiding Principles for Scientific Data Management and Stewardship.” *Scientific Data* 3, 2016. https://doi.org/10.1038/sdata.2016.18.

Wooldridge, Michael, and Nicholas R. Jennings. “Intelligent Agents: Theory and Practice.” *The Knowledge Engineering Review* 10, no. 2, 1995, 115 to 152. https://doi.org/10.1017/S0269888900008122.

Zhong, Hailin, and Shengxin Zhu. “AI Harness Engineering: A Runtime Substrate for Foundation Model Software Agents.” 2026. https://doi.org/10.48550/arXiv.2605.13357.

## **Appendix: Knowledge Document Template**

```markdown
# Subject

## Purpose

## Concepts and Distinctions

## Relevant Evidence and Sources

## Rules and Constraints

## Relationships and Dependencies

## Uncertainties

## Open Questions

## Decisions

## Provenance
```

## **Appendix: Agent Instruction Template**

```markdown
# Role and Working Mode

# Project Structure

# Binding Working Rules

# Tools and Commands

# Permissions and Boundaries

# Rules for Questions and Escalation

# Completion Criteria

# References to Knowledge Documents
```

## **Appendix: Working Context Template**

```markdown
# Task

# Relevant Requirements

# Provided Knowledge

# Data and Resource Access

# Instructions

# Tools

# Current State

# Verification Criteria

# Escalation Conditions
```

## **Appendix: Verification Report**

```markdown
# Object

# Version or State

# Verification Criteria

# Checks Performed

# Results

# Failures and Warnings

# Unverified Properties

# Evidence
```

## **Appendix: Validation and Acceptance Record**

```markdown
# Object

# Intended Purpose

# Relevant Sources and Evidence

# Domain Validation

# Remaining Uncertainty

# Acceptance Decision

# Responsible Person or Role

# Date and Version
```

[^1]: Schulhoff et al. 2024; Allen et al. 2023; Mei et al. 2025; Sapkota, Roumeliotis, and Karkee 2025; Zhong and Zhu 2026.

[^2]: Zhong and Zhu 2026. See also Pollin, *Promptotyping*, review draft 0.9, 2026.

[^3]: Christopher Pollin, *Promptotyping. Translating Research Data into Research Artefacts through Context Engineering and Agentic Engineering*, review draft 0.9, 2026.

[^4]: The term *Applied Generative AI* is used here for domain specific application and adaptation of generative AI, following the framing developed in teaching and AGKI DH activities by Christopher Pollin.

[^5]: Philipp Geiger, “Daten / Forschungsdaten,” 2024, https://doi.org/10.17175/wp_2023_003_v2. See also Johanna Drucker, “Humanities Approaches to Graphical Display,” *Digital Humanities Quarterly* 5, no. 1, 2011.

[^6]: Majithia et al., “An Actionable Framework for AI Ready Data,” 2026, https://doi.org/10.1002/aaai.70054.

[^7]: Mark D. Wilkinson et al., “The FAIR Guiding Principles for Scientific Data Management and Stewardship,” *Scientific Data* 3, 2016, https://doi.org/10.1038/sdata.2016.18.

[^8]: Sander Schulhoff et al., “The Prompt Report: A Systematic Survey of Prompting Techniques,” 2024, https://doi.org/10.48550/arXiv.2406.06608.

[^9]: Bradley P. Allen et al., “Knowledge Engineering Using Large Language Models,” 2023, https://doi.org/10.4230/TGDK.1.1.3; Stuart Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach*, 4th ed., 2020, https://aima.cs.berkeley.edu.

[^10]: Lingrui Mei et al., “A Survey of Context Engineering for Large Language Models,” 2025, https://doi.org/10.48550/arXiv.2507.13334. The formulation used here follows Pollin, *Promptotyping*, review draft 0.9, 2026.

[^11]: Ranjan Sapkota, Konstantinos I. Roumeliotis, and Manoj Karkee, “AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges,” *Information Fusion* 126, 2025, https://doi.org/10.1016/j.inffus.2025.103599. The specific definition of Agentic Engineering follows Pollin, *Promptotyping*, review draft 0.9, 2026.

[^12]: Hailin Zhong and Shengxin Zhu, “AI Harness Engineering: A Runtime Substrate for Foundation Model Software Agents,” 2026, https://doi.org/10.48550/arXiv.2605.13357.

[^13]: Jeanne Hersch workflow, https://chpollin.github.io/zbz-ocr-tei and https://github.com/chpollin/zbz-ocr-tei. Stefan Zweig workflow, https://chpollin.github.io/szd-htr-ocr-pipeline and https://github.com/chpollin/szd-htr-ocr-pipeline.

[^14]: Artificial Analysis, https://artificialanalysis.ai.

[^15]: See the sources collected on the corresponding lecture slide and Pollin, “Asymmetric Amplification,” 2026, https://dhcraft.org/excellence/blog/Asymmetric-Amplification.

[^16]: METR, https://metr.org/time-horizons; ARC Prize, https://arcprize.org/leaderboard; SimpleBench, https://simple-bench.com; Humanity’s Last Exam, https://lastexam.ai; Epoch AI FrontierMath, https://epoch.ai/frontiermath.

[^17]: Christopher Pollin, “Asymmetric Amplification,” 2026, https://dhcraft.org/excellence/blog/Asymmetric-Amplification.

[^18]: Fabrizio Dell’Acqua et al., “Navigating the Jagged Technological Frontier,” *Organization Science* 37, no. 2, 2026, https://doi.org/10.1287/orsc.2025.21838; Joshua Gans, “A Model of Artificial Jagged Intelligence,” 2026, https://doi.org/10.48550/arXiv.2601.07573; Christopher Summerfield, *These Strange New Minds*, 2025.

[^19]: Jack Lindsey et al., “On the Biology of a Large Language Model,” Transformer Circuits, 2025, https://transformer-circuits.pub/2025/attribution-graphs/biology.html.

[^20]: Christopher Pollin, *Wie LLMs funktionieren*, YouTube, 2026, https://youtu.be/u4RRxi5tgTA.

[^21]: Tom B. Brown et al., “Language Models are Few Shot Learners,” 2020, https://arxiv.org/abs/2005.14165. For the Transformer architecture see Vaswani et al. 2017.

[^22]: Yoshua Bengio, “Godfather of AI: How To Make Safe Superintelligent AI,” interview with Rob Wiblin, *80,000 Hours*, 2026, https://youtu.be/PZqDFs2sbiY.

[^23]: Ashish Vaswani et al., “Attention Is All You Need,” 2017, https://arxiv.org/abs/1706.03762.

[^24]: Long Ouyang et al., “Training Language Models to Follow Instructions with Human Feedback,” 2022, https://arxiv.org/abs/2203.02155. See also Anthropic’s work on Constitutional AI and Claude’s Character.

[^25]: Andrej Karpathy, *Intro to Large Language Models*, 2023, https://www.youtube.com/watch?v=zjkBMFhNj_g. The compression language is a didactic analogy, not a literal model of parameter storage.

[^26]: For subword tokenisation see Rico Sennrich, Barry Haddow, and Alexandra Birch, “Neural Machine Translation of Rare Words with Subword Units,” 2016, https://arxiv.org/abs/1508.07909.

[^27]: François Chollet, “How I Think About LLM Prompt Engineering,” 2023, https://fchollet.substack.com/p/how-i-think-about-llm-prompt-engineering.

[^28]: Cheng Li et al., “Large Language Models Understand and Can Be Enhanced by Emotional Stimuli,” 2023, https://doi.org/10.48550/arXiv.2307.11760; Sondos Mahmoud Bsharat, Aidar Myrzakhan, and Zhiqiang Shen, “Principled Instructions Are All You Need for Questioning LLaMA 1/2, GPT 3.5/4,” 2023, https://doi.org/10.48550/arXiv.2312.16171; Ziqi Yin et al., “Should We Respect LLMs?” 2024, https://doi.org/10.48550/arXiv.2402.14531; Meghana Rajeev et al., “Cats Confuse Reasoning LLM,” 2025, https://doi.org/10.48550/arXiv.2503.01781.

[^29]: Google Gemini, “Prompt Design Strategies,” https://ai.google.dev/gemini-api/docs/prompting-strategies.

[^30]: Gemini Team, “Gemini: A Family of Highly Capable Multimodal Models,” 2023, https://arxiv.org/abs/2312.11805.

[^31]: Nicholas Sofroniew et al., “Emotion Concepts and Their Function in a Large Language Model,” 2026, https://transformer-circuits.pub/2026/emotions/index.html.

[^32]: Chloe Li, Nevan Wichers, Sara Price, Samuel Marks, and Jon Kutasov, “Model Spec Midtraining: Improving How Alignment Training Generalizes,” 2026, https://arxiv.org/abs/2605.02087.

[^33]: Anthropic, “Claude’s Character,” https://www.anthropic.com/research/claude-character; Anthropic, “Claude’s Constitution,” 2026, https://www.anthropic.com/constitution.

[^34]: Anthropic, “Claude’s New Constitution,” 2026, https://www.anthropic.com/research/claude-new-constitution.

[^35]: Anthropic, “System Prompts,” https://platform.claude.com/docs/en/release-notes/system-prompts; Anthropic, “Claude’s New Constitution,” 2026.

[^36]: For inference time scaling as a broader category see Charlie Snell et al., “Scaling LLM Test Time Compute Optimally Can Be More Effective Than Scaling Model Parameters,” 2024, https://arxiv.org/abs/2408.03314.

[^37]: The distinction between tacit, fragmented and maintained project knowledge is developed in Pollin, *Promptotyping*, review draft 0.9, 2026.

[^38]: William Jones, Jesse David Dinneen, Robert Capra, Anne R. Diekema, and Manuel A. Pérez Quiñones, “Personal Information Management,” 2017, https://doi.org/10.1081/E-ELIS4-120053695.

[^39]: See Jürg Kuster et al., *Handbuch Projektmanagement*, Springer, and the project management literature referenced in the slide deck.

[^40]: Kelly Hong, Anton Troynikov, and Jeff Huber, *Context Rot: How Increasing Input Tokens Impacts LLM Performance*, Chroma, 2025, https://research.trychroma.com/context-rot.

[^41]: Markdown Guide, https://www.markdownguide.org.

[^42]: Christopher Pollin, *Modelling, Operationalising and Exploring Historical Information. Using Historical Financial Sources as an Example*, Graz, 2025, https://resolver.obvsg.at/urn:nbn:at:at-ubg:1-220602.

[^43]: Ishan Anand, “Persona Engineering: A Field Guide to AI Synthetic Personas,” https://youtu.be/YnNF55QV0zs.

[^44]: Christopher Pollin, “Promptotyping: Zwischen Vibe Coding, Vibe Research und Context Engineering,” L.I.S.A. Wissenschaftsportal Gerda Henkel Stiftung, 2026, https://lisa.gerda-henkel-stiftung.de/digitale_geschichte_pollin.

[^45]: Michael Wooldridge and Nicholas R. Jennings, “Intelligent Agents: Theory and Practice,” *The Knowledge Engineering Review* 10, no. 2, 1995, https://doi.org/10.1017/S0269888900008122.

[^46]: Guanzhi Wang et al., “Voyager: An Open Ended Embodied Agent with Large Language Models,” 2023, https://arxiv.org/abs/2305.16291.

[^47]: For the individual concepts see the official documentation referenced in footnotes 48 to 52.

[^48]: AGENTS.md, https://agents.md.

[^49]: Anthropic, “How Claude Remembers Your Project,” Claude Code Docs, https://code.claude.com/docs/en/memory.

[^50]: Agent Skills, https://agentskills.io and https://agentskills.io/specification.

[^51]: Model Context Protocol, https://modelcontextprotocol.io/docs/getting-started/intro and https://modelcontextprotocol.io/specification/2025-11-25.

[^52]: Agent2Agent Protocol, https://a2a-protocol.org/latest/topics/a2a-and-mcp/.

[^53]: The term evaluation is used broadly here for assessment against explicit criteria. In research workflows this may include quantitative metrics, qualitative review and system level evaluation.

[^54]: The distinction between technical verification and domain validation adapts established verification and validation terminology from software and systems engineering to AI supported research workflows. See Pollin, *Promptotyping*, review draft 0.9, 2026.
