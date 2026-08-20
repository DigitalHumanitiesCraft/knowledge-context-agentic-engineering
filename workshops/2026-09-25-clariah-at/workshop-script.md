# Knowledge, Context and Agentic Engineering for Research Data Workflows & Digital Editions

***Lecture Notes*** 

Christopher Pollin, Digital Humanities Craft OG 

CLARIAH-AT Summer School 2026 *Machine Learning for Digital Scholarly Editions* 25

## **Abstract**

Frontier large language models (LLMs) increasingly operate within AI harnesses that connect models with files, tools, executable environments and project knowledge. These lecture notes examine how such systems reshape research data workflows, with examples from digital scholarly editions. They distinguish prompt, knowledge, context and agentic engineering as complementary approaches to designing and implementing AI-supported research environments, and present Promptotyping as a context-engineering method that integrates project knowledge, agentic implementation and scholarly verification. AI-supported research is therefore not simply the automation of a processing pipeline, but the construction of technical and epistemic environments in which sources are transformed, interpreted and assessed. Model-generated outputs become research data only when they have been appropriately assessed and accepted within the research workflow.

## **Applied Generative AI for Research Data Workflows**

**Applied Generative AI** refers to the application and adaptation of generative AI methods and systems to problems in specific research domains, following the tradition of *applied computer science*. When co-founding AGKI-DH,[^1] I argued for *Applied Generative AI* rather than the broader label *Machine Learning* to emphasise the specific methodological and practical questions raised by generative AI. The focus is not primarily on developing new foundation models, but on integrating generative AI into domain-specific research practices, here particularly research data workflows in the Digital Humanities.

Generative models can be used throughout such workflows. They can interpret and structure research material, transform data between representations, generate code for deterministic operations, or be used within AI harnesses to construct and modify project-specific software environments.

These lecture notes focus particularly on **frontier models** because I consider their current capabilities qualitatively significant for computational research. This does not imply that frontier models are the appropriate solution for every task. Smaller, local or open-weight models, specialised models and other machine-learning methods may be substantially more efficient, controllable or appropriate for particular problems. Nevertheless, the combination of multimodality, reasoning, coding, tool use and agentic capabilities found in frontier systems creates new possibilities for research workflows that require sustained critical examination. Their ecological costs, social consequences and concentration of technological power are part of this examination rather than reasons to ignore these systems.

These lecture notes bring together and further develop selected material from my previous work, including the following resources:

* **YouTube:** [Digital Humanities Craft](https://www.youtube.com/@DigitalHumanitiesCraft)  
* **Slides:** [GM-DH](https://chpollin.github.io/GM-DH)  
* **Blog:** [Digital Humanities Craft Blog](https://dhcraft.org/excellence/blog)  
* **Zotero Library:** [AGKI-DH](https://www.zotero.org/groups/5319178/agki-dh)  
* **Patreon:** [Digital Humanities Craft](https://www.patreon.com/c/DigitalHumanitiesCraft)

## **Humanities Research Data Are Constructed through Scholarly Workflows**

**Digital Humanities research data** are digital, machine-actionable representations of research objects or sources that are created and shaped through scholarly work.[^2] They are necessarily selective because computational representations make particular aspects of their objects of inquiry explicit while leaving others implicit.[^3] The concept of *capta* emphasises that such data are not simply given, but constructed through situated acts of observation and representation.[^4] A transcription, for example, already involves decisions about what is legible and how textual structure is represented, while encoding adds another interpretative layer by determining which structures become computationally explicit. Such data therefore require sufficient documentation and context to make these decisions assessable and to support scholarly interpretation, reproducibility and reuse.

A **research data workflow** is the organised process through which research materials and data are created, transformed, enriched, assessed and prepared for scholarly use. Automated pipelines may perform individual transformations within this wider process, while the workflow also includes source context, scholarly rules, provenance and procedures for assessment and acceptance. Formal validity does not by itself establish scholarly adequacy.

The digitised pages of the notebook *Clarissa* from the Stefan Zweig collection show how such layers accumulate.[^5] A scan captures the visual appearance of a page, while identification and catalogue metadata establish what the object is, where it belongs and how it can be found and referenced. Collection and project context make individual pages interpretable within the larger research object. Even an empty page can become relevant when its position within the notebook is documented. Further modelling can make textual structures, entities, relations or editorial decisions explicit and thereby support additional forms of computational processing.

**AI readiness** concerns whether research data are sufficiently structured, documented and governed for effective use in AI-supported workflows. This includes machine-readable representations, clear provenance and usage conditions, and information needed to assess data quality, uncertainty and potential bias.[^6] FAIR provides broader principles for making research data findable, accessible, interoperable and reusable,[^7] while formats such as Croissant support dataset description for machine-learning environments.[^8] Domain-specific formats such as TEI remain important for representing scholarly content and semantics. CARE complements these approaches where Indigenous data or knowledge require particular attention to governance, responsibility and authority.[^9]

## **Learning Objectives and Core Concepts**

The learning objectives are to understand how **Prompt Engineering**, **Knowledge Engineering**, **Context Engineering** and **Agentic Engineering** relate to AI-supported research data workflows. **Prompt Engineering** concerns the iterative design and refinement of prompts for a particular model and task.[^10] **Knowledge Engineering** creates, curates and maintains explicit project knowledge for use by researchers and AI systems,[^11] while **Context Engineering** selects, structures and manages the task-relevant information available to an LLM during a particular interaction.[^12] **Agentic Engineering** concerns the design and governance of multi-step, tool-supported workflows in which **AI agents**, systems that use models to select and execute actions across multiple steps, operate within an **AI harness**, the environment that provides context, tools, state and feedback.[^13] 

Participants should learn how these layers interact when project knowledge is made usable for LLMs and AI agents, how agent-supported workflows transform sources into research data, where outputs require validation and scholarly verification, and how frontier LLMs are changing research practices and the role of the scholar. 

## **AI-Supported Research Data Workflows & Epistemic Infrastructures**

The **Jeanne Hersch workflow** was developed in collaboration with the Zentralbibliothek Zürich for the digital republication of Hersch’s writings.[^14] It transforms scans of multilingual printed publications into structured edition data. Mistral OCR produces text and page-level document representations, Docling supports local layout analysis, and additional model calls can review or classify structures that depend on visual or textual context.[^15] The resulting representations are transformed into TEI XML and enriched with information such as named entities and authority data. The complete workflow can be inspected through the [project frontend](https://chpollin.github.io/zbz-ocr-tei) and the underlying [GitHub repository](https://github.com/chpollin/zbz-ocr-tei).

The workflow combines model-generated data with deterministic transformations, schema validation, project-specific tests, provenance and editorial curation. Researchers can compare generated representations with the source, correct transcription and encoding, curate entities and record editorial status. The surrounding software environment was developed and iteratively refined with AI agents operating through Claude Code.[^16] The workflow is therefore not simply automated. LLMs perform individual transformations, while AI agents **amplify the research software developer**, increasing the scale and speed at which research workflows, data models, validation procedures and interfaces can be designed, implemented and revised. 

The **Stefan Zweig workflow** applies a related approach to handwritten and typed material from Stefan Zweig Digital at the Literaturarchiv Salzburg. Gemini receives a facsimile together with project-specific source context and transcription instructions and generates a transcription from visual and linguistic information.[^17] The relation between source image and generated transcription is preserved, uncertainty can be recorded, and the original model output remains available after editorial correction. This makes it possible to compare generated and curated representations and to calculate measures such as Character Error Rate (CER). The [project frontend](https://chpollin.github.io/szd-htr-ocr-pipeline) functions both as a catalogue and as a curation environment, while the [GitHub repository](https://github.com/chpollin/szd-htr-ocr-pipeline) contains the underlying processing workflow.

Both projects treat model output as an intermediate state within a larger **research data workflow** rather than as a finished research result. AI agents can work directly with project knowledge, files, code, structured data, tests and generated outputs. At the same time, an ***epistemic infrastructure*** connects these technical operations with provenance, validation, scholarly verification, curation and decisions about the status and acceptance of research data.

## **The Current LLM Capability Landscape**

The current LLM landscape contains several overlapping model ecosystems. Proprietary frontier systems are dominated by providers such as Anthropic, OpenAI, Google and xAI. Chinese developers such as Alibaba, DeepSeek and Moonshot AI have produced highly capable model families, several of which are available with open weights. In Europe, Mistral AI is currently the most prominent developer of general-purpose large language models. Because model capabilities change rapidly, continuously updated comparisons such as the Artificial Analysis LLM Leaderboard are useful for locating the current **capability frontier** across reasoning, coding, agentic tasks, speed and cost.[^18]

Models also differ in their degree of **openness**. Proprietary models are primarily accessed through hosted products or APIs while model weights and major training artefacts remain inaccessible. **Open-weight models** make trained parameters available under a specified licence and can often be downloaded, adapted and executed independently. This is not equivalent to **open source**. The Open Source AI Definition 1.0 requires the freedoms to use, study, modify and share an AI system together with access to the preferred form for modification, including sufficient information about training data, source code and model parameters.[^19]

For research, openness determines which parts of a system can be inspected, reproduced, modified or operated under institutional control. It is therefore better understood as **multidimensional** rather than binary. Training data, documentation, training code, model architecture, parameters, licences and access conditions may each be available to different degrees. The European Open Source AI Index evaluates contemporary models across 14 dimensions of openness and shows substantial variation among systems commonly described as open.[^20] Related work describes **open-washing** as the presentation of AI systems as open despite significant restrictions on accessibility or reproducibility.[^21] Dingemanse’s broader work on generative AI and research integrity provides a complementary values-based perspective on the selection and use of generative AI systems in research.[^22] I do not share all of his conclusions, but the concerns he raises are important for understanding the broader debate on generative AI in research.

**Local deployment** is a separate dimension. Open-weight models can run on institutionally controlled infrastructure using environments such as Ollama or LM Studio, but they can also be accessed through external providers.[^23] Local execution can increase control over research data, inference configuration and system availability, while shifting responsibility for hardware, security, maintenance and model operation to the institution. Hosted systems may provide stronger capabilities or simpler access, but they also create dependencies on external providers, their infrastructure and their governance conditions.

**AI harnesses** constitute another system layer. Environments such as Claude Code, Codex, Gemini CLI, Mistral Vibe, Qwen Code, Kimi Code, Pi and Cursor connect models with project context, files, tools, executable environments, state and feedback.[^24] The contemporary LLM landscape can therefore be examined along at least four distinct dimensions: **capability**, **openness**, **deployment** and **agentic integration**. These dimensions interact, but they describe different properties of an AI-supported research environment.

## **Frontier LLMs Asymmetrically Amplify Computational Research**

Frontier AI companies increasingly treat the automation of research and development as a strategic objective. I think this direction should be taken seriously. We are seeing a growing number of signals that frontier models are becoming substantially more capable at tasks relevant to research, particularly where reasoning, coding, tool use, longer-horizon action and structured feedback can be combined. None of these signals demonstrates that research as a whole can or will be automated. Taken together, however, they suggest a trajectory that I consider both significant and still substantially underestimated in the broader discussion about AI.[^25]

One signal is the rapid movement of the **capability frontier** across very different evaluations. METR measures how long software tasks AI agents can complete with specified levels of reliability and finds a continuing increase in these task horizons.[^26] ARC-AGI-3 tests a very different capability: agents must explore unfamiliar interactive environments, infer their rules and goals, and adapt through experience without natural-language instructions. At its launch in March 2026, frontier systems scored around 0.5 percent while the environments were designed to be solvable by humans. By July 2026, Claude Opus 5 reached 30.2 percent on the public ARC-AGI-3 evaluation.[^27] The significance is not that ARC-AGI-3 has been “solved”, but that substantial capability gains can occur within months on a benchmark explicitly designed around adaptation to novel environments.

Mathematics provides another signal. Frontier systems are improving not only on mathematical benchmarks but also in environments where outputs can be externally checked. Formal theorem proving connects generative reasoning with proof assistants such as Lean, which can mechanically verify whether a proposed proof satisfies a formal specification.[^28] In 2026, OpenAI reported that an internal model generated new results resolving or substantially advancing ten open problems in mathematics and theoretical computer science and subsequently formalised the arguments as Lean certificates.[^29] Such results require independent mathematical scrutiny, but they are relevant because they move beyond short-answer benchmarks towards research-level problems with unusually strong possibilities for external verification.

**Cyber capabilities** show a similar expansion in a different domain. Cyber tasks combine software understanding, tool use, exploration, planning and feedback from executable environments. Evaluations by the UK AI Security Institute indicate rapid improvement across the cyber capabilities it tests. In late 2023, frontier systems rarely completed apprentice-level cyber tasks, while current leading systems complete such tasks around half of the time on average and have begun to solve expert-level tasks requiring substantially greater human experience.[^30] OpenAI reported in August 2026 that evaluations of its upcoming Astra model showed sufficiently advanced agentic coding and cybersecurity performance that the company could no longer rule out **critical cyber capabilities** under its Preparedness Framework.[^31]

Cybersecurity is therefore another domain in which increasing model capability becomes particularly visible when models can act within computational environments and observe the consequences of their actions. It is also the capability domain I find most concerning. Highly capable **open-weight models** can diffuse offensive cyber capabilities beyond the organisations that developed them and may lower barriers for criminal activity, hybrid warfare or state-sponsored operations. Proprietary frontier systems create a different risk. Access can be restricted, monitored and governed more directly, but the most capable systems and their underlying infrastructure remain concentrated within a small number of companies and nation states. Cyber capability therefore exposes a broader governance dilemma between the diffusion of powerful capabilities and the concentration of technological power.

Scenario work provides a different kind of signal and should not be confused with empirical evaluation. **AI 2027**, for example, explores a trajectory in which increasingly capable AI systems accelerate AI research itself, potentially creating feedback between model capability and the rate of further development.[^32] The scenario does not demonstrate that such a trajectory will occur. Its relevance lies in making a particular possibility explicit: research automation could become not merely another application of frontier AI, but a mechanism that influences the speed at which the technology itself develops.

My own work with AI agents in research software development and research data workflows provides a further, practice-based observation. It is not a controlled evaluation and cannot establish a general trend. What I observe, however, is a substantial increase in the scale, speed and complexity of computational research work that can be undertaken when experienced researchers and research software developers work with current frontier agents.

Agents can operate across repositories, research data and executable environments, but they remain dependent on **expert guidance**. Researchers and research software developers define the goals, externalise relevant project knowledge, make modelling decisions, set constraints and validation criteria, interpret feedback and decide whether resulting artefacts are adequate for the research task. The relevant effect is therefore not merely task automation, but the **amplification of expert capability** across a computational research workflow.

I describe this effect as **asymmetric amplification**.[^33] Frontier LLMs particularly amplify **data-driven, computer-based knowledge work** where research objects and knowledge are digitally represented, actions can be executed through software, and the environment can return meaningful feedback. Research software development, data processing, formal modelling and many Digital Humanities workflows exhibit precisely these properties. The amplification is asymmetric because it depends on existing expertise, the structure of the task and the quality of the surrounding technical and epistemic environment. The same AI system may therefore amplify an experienced computational researcher far more strongly than someone working in an environment where knowledge remains largely tacit, materials are not computationally accessible or outputs cannot be systematically assessed.

No single benchmark provides an overall measure of research capability. METR task horizons, ARC-AGI, mathematical theorem proving, cyber evaluations and other benchmarks probe different regions of a highly **jagged capability landscape**. Benchmark results are also shaped by the model, harness, tools, inference budget, task specification and evaluation procedure. The important signal is therefore not that one benchmark has reached a particular score. It is that the capability frontier appears to be moving across several very different, research-relevant domains at the same time.

This jaggedness also makes the trajectory difficult to evaluate. Frontier models can display extraordinary performance on a difficult computational task while failing on a neighbouring task that appears simpler to a human observer. Their increasing capabilities should therefore neither be extrapolated naively into general intelligence nor dismissed because conspicuous failures remain. Understanding this combination of rapid progress and uneven reliability is essential for assessing what these systems currently are and what forms of research they may increasingly amplify.

## **LLMs as Jagged Alien “Intelligences”**

The metaphor of *alien intelligence* describes an unfamiliar capability profile rather than consciousness or human-like understanding. LLMs generate tokens from learned numerical representations and transformations. They can support complex computation while also producing plausible but unsupported claims. In these notes, such behaviour is described as **confabulation**.

Models can also reproduce biases introduced through training and post-training. **Sycophancy** describes a tendency to align an answer with a user’s expressed belief even when this reduces factual accuracy.[^34] Prompts that merely ask a model to confirm a preferred interpretation are therefore methodologically weak.

Mechanistic interpretability research indicates that model behaviour can depend on structured internal computational pathways that differ substantially from human reasoning.[^35] The metaphor of learned *vector programs* provides one way of thinking about this repertoire of internal representations and transformations.

Tool use changes the effective system. Search can provide information beyond training data. File access can provide project-specific knowledge. Code execution can return evidence about the consequences of an action. Reasoning modes allocate additional inference-time computation, but additional computation does not eliminate the need for external assessment.[^36]

## **Prepare the Working Environment before the First Prompt**

Agentic work begins before the first substantive prompt. The demonstrations use Visual Studio Code together with AI harnesses that can access project files and a terminal.[^37] Claude Code is used in several examples, but another environment with equivalent capabilities can be substituted.

A project workspace should contain the relevant source material, research question, project documentation and expected outputs. File and tool permissions should remain limited to the intended workspace. Original sources should remain unchanged, while generated outputs should be stored separately and connected to sufficient provenance.

Preparing the workspace determines which files, tools, knowledge and forms of feedback later become available to the system. The environment is therefore part of the methodological design.

### **Generative Models through an API**

An API is an agreed interface through which software systems communicate. A script can send an image and an instruction to a hosted multimodal model and receive generated text in return. The model therefore does not have to be used through a conversational interface. It can become one component inside a processing pipeline.

For document transcription, a program may send each page image together with a task specification defining reading order, treatment of tables, uncertainty markers and output structure. The returned text can then be stored, transformed, compared or assessed by later stages of the workflow.

API access changes the scale and repeatability of the task. Instead of manually uploading one image, the same operation can be applied across a collection. This increases the importance of provenance, model configuration, failure handling and cost monitoring.

### **Model-Assisted Review inside an AI Harness**

A second frontier model can inspect the output of a source-processing model and compare it with the original image. In an AI harness such as Claude Code, a multimodal model can open the facsimile, inspect the generated transcription and use executable tools to compare or transform the result.

This does not guarantee correctness. A second model can reproduce the same mistake, introduce a new one or overstate confidence. Model-assisted review is therefore an additional checking layer that can surface possible errors and direct human attention.

The methodological rule remains:

**Model agreement is not scholarly verification.**

Automated comparison, formal validation and expert review answer different questions and should remain distinguishable.

### **From Generated Text to Structured Data**

Generated transcription can become an intermediate representation for later deterministic processing. Plain text or Markdown may be transformed into JSON, CSV or XML. Structured output makes it possible to run consistency checks, aggregate values, compare fields and integrate data with other project resources.

For numerical tables, deterministic checks can provide particularly strong feedback. Row and column sums can be compared, numerical relationships can be verified and deviations can be surfaced automatically. Such checks do not establish that the source was interpreted correctly, but they can reveal internal inconsistencies and reduce the number of cases requiring manual inspection.

A recurring pattern emerges: LLMs are particularly useful when combined with environments that can return evidence about their outputs. The goal is not to replace deterministic methods, but to combine model flexibility with reproducible checks wherever the research task permits them.

## **Prompt Engineering**

**Prompt Engineering** is the iterative design and evaluation of instructions for a specific model and task.[^38] A prompt specifies an immediate operation, supplies relevant information and constraints, and defines the expected form of the result.

A useful working structure for research prompts is:

1. **Task** What should the model do?

2. **Context** What source information or project knowledge does the model need?

3. **Rules** Which scholarly, technical or representational constraints should govern the result?

4. **Output** In which form should the result be returned?

This is not a universal prompt template. It is a transparent way to separate different functions of an instruction so that they can be inspected and revised independently.

Earlier prompt-engineering practice often concentrated on finding particularly effective formulations, roles, examples and linguistic strategies. With current frontier models, the individual prompt has become less central. Many techniques depend strongly on model, version, task and system configuration. Prompt engineering therefore remains useful, but should not be treated as a collection of universal hacks.

### **Prompting Is Weird — and Keeps Changing**

Prompt-engineering research has repeatedly demonstrated that model performance can change in response to linguistic details with little direct relation to the underlying task. EmotionPrompt, for example, added phrases such as “This is very important for my career\!” and reported measurable effects in the evaluated models and datasets.[^39] Other studies have investigated incentive framing, formality, concreteness and politeness.[^40][^41][^42]

Automatically optimised prompts can produce eccentric formulations that no human expert would have designed manually.[^43] Irrelevant information can also alter reasoning performance in contemporary models.[^44]

The methodological conclusion is not that these formulations should be memorised. It is that **prompting effects are model-, task- and time-dependent**. Strategies that work for one generation may weaken or disappear with another.

Role prompting illustrates this problem. Assigning a model a generic expert identity does not reliably improve factual accuracy or reasoning performance,[^45] although roles may remain useful where a task genuinely requires a particular perspective, audience, communicative style or evaluative frame.[^46]

Prompting recommendations therefore have a short half-life. They should be treated as empirical findings tied to particular models and evaluation settings rather than stable laws of interaction.

## **Transcribe a Facsimile with Gemini 3.7 Flash**

A simple Stefan Zweig order slip provides a compact example of the four-part prompt structure.[^47]

Create a diplomatic transcription of this facsimile.

\# Context

German order slip from May 1935\.

Printed form with pencil entries by Stefan Zweig.

\# Rules

\- Transcribe printed and handwritten text.

\- Preserve spelling, abbreviations, line breaks and field order.

\- Mark uncertainty as word\[?\] and illegible text as \[...\].

\- Mark deletions as \~\~text\~\~ and insertions as {text}.

\- Ignore show-through.

\# Output

Return only the transcription as plain text in reading order.

The task identifies the operation. The context identifies the document. The rules encode a transcription policy. The output section defines the expected representation.

These categories can be modified independently. A different source requires different context. A different editorial policy requires different rules. A different downstream workflow may require structured JSON or TEI rather than plain text.

## **Hands-on 1: Transcribe a Complex Facsimile**

The hands-on exercise uses a more difficult page from Stefan Zweig’s manuscript *Radiovortrag über Newyork*, dated 1935.[^48] The manuscript consists of twelve leaves written primarily in violet ink and contains corrections and annotations in several writing materials. Page 1 begins with the words “Sieht man einen alten Freund …”.

Participants first receive a reusable prompt skeleton:

Create a diplomatic transcription of this facsimile.

\# Context

{{add the context}}

\# Rules

\- Transcribe all handwritten text in reading order.

\- Preserve original spelling, punctuation, abbreviations and line breaks.

\- Mark uncertain readings as word\[?\] and illegible passages as \[...\].

\- Represent deletions as \~\~text\~\~ and insertions as {text}.

\- Preserve visible revisions rather than silently resolving them into a clean text.

\- Ignore show-through and non-textual marks unless they affect the reading of the text.

\- {{add here a new rule}}

\# Output

Return only the diplomatic transcription in reading order.

Relevant catalogue information includes:

* **Author:** Stefan Zweig  
* **Title:** *Radiovortrag über Newyork*  
* **Incipit:** “Sieht man einen alten Freund …”  
* **Date:** 1935  
* **Language:** German  
* **Material:** manuscript, 12 leaves  
* **Writing materials:** violet ink, pencil, red and blue coloured pencil  
* **Hand:** Stefan Zweig  
* **Pagination:** 1–12  
* **Current location:** Literaturarchiv Salzburg  
* **Shelfmark:** SZ-AAP/W27

A possible context is therefore:

\# Context

The facsimile shows page 1 of a 12-page handwritten manuscript by Stefan Zweig.

\- Title: Radiovortrag über Newyork

\- Incipit: “Sieht man einen alten Freund …”

\- Date: 1935

\- Language: German

\- Material: manuscript written primarily in violet ink, with corrections and annotations in pencil and coloured pencil

\- Hand: Stefan Zweig

\- Pagination: 1–12

\- Collection: Literaturarchiv Salzburg

\- Shelfmark: SZ-AAP/W27

A useful additional rule addresses a characteristic risk of multimodal foundation models:

\- Do not reconstruct or complete words from linguistic context when the reading is not visually supported by the facsimile. Mark uncertainty instead.

The instruction asks the model to prefer explicit uncertainty over a linguistically plausible reconstruction. Whether it succeeds must be assessed against the facsimile.

### **Example Result and Critical Review**

A generated transcription can be remarkably fluent while individual readings remain incorrect. It therefore has to be compared directly with the source.

A model may correctly reconstruct long passages of difficult handwriting while misreading a short sequence elsewhere. It may generate a word that fits the surrounding sentence even when the visual evidence supports a different reading. It may also fail to express uncertainty in places where a human reader would hesitate.

This is a characteristic property of VLM-based transcription. Errors are not necessarily local character-recognition errors. They can be **contextually plausible readings that do not match the source**.

The generated transcription should therefore be treated as an output requiring assessment. Fluency, grammaticality and internal coherence are not evidence of source fidelity.

This leads to a conceptual question:

**Are we doing OCR, HTR, or something technically different?**

OCR and HTR remain useful descriptions of the recognition task. The system performing that task, however, is not necessarily a dedicated OCR or HTR model. It may instead be a general-purpose multimodal foundation model.

### **Multimodality and Vision-Language Models**

**Gemini 3.7 Flash is a general-purpose multimodal foundation model**, not a dedicated OCR or HTR system. A **Vision-Language Model (VLM)** processes visual and linguistic information within the same task.

A VLM can attempt to transcribe previously unseen handwritten or printed text zero-shot from an image and an instruction. Visual patterns, layout, linguistic context and task instructions can all influence the generated result.

FACSIMILE                       INSTRUCTION

visual information             task \+ rules

        \\                         /

         \\                       /

          \+---------------------+

                    |

                    v

          VISION-LANGUAGE MODEL

                    |

                    v

              TRANSCRIPTION

This differs conceptually from dedicated OCR or HTR pipelines, which typically separate operations such as layout analysis, segmentation and recognition. A general-purpose VLM receives the image and instruction as parts of the same multimodal inference process.

This broader capability can help with difficult material because visual, textual and task-specific context can interact. The same property creates a characteristic failure mode: the model may generate a contextually plausible reading that is not supported by the source.

The Stefan Zweig example is particularly interesting because Gemini has not been project-specifically trained or fine-tuned for Zweig’s handwriting. Public documentation does not disclose the complete training mixture, however, so it would be too strong to claim that the model has never encountered related handwriting or transcription material.

The resulting open question is:

**To what extent is zero-shot HTR an emergent capability of large multimodal models?**

The observed capability is real. Whether it should be described as *emergent* depends on the definition of emergence, the composition of the training data and the development of the capability across model scale and training stages. These factors are not fully observable for proprietary frontier models.

## **Prompt Engineering as Search in a Latent Program Space**

A useful conceptual model treats an LLM as containing a large repertoire of learned *vector programs* rather than only as a system that predicts the next token.[^49] Prompt engineering can then be understood as a form of search through a latent program space.

The concepts can be expressed compactly:

* **Vector Program** \= a learned transformation that realises a capability or behaviour  
* **Latent Program Space** \= the space of possible learned transformations  
* **Program Query** \= an address or search signal within that space  
* **Prompt Engineering** \= external search for an effective address  
* **Reasoning / Test-Time Compute** \= internal search for an effective computation

A **Vector Program** is not a discrete symbolic program stored somewhere inside the model. It is a learned and distributed transformation across high-dimensional representations that realises a particular capability or behaviour. As a didactic metaphor, it can be imagined as a fuzzy cascade of interconnected representations and transformations.

A **Program Query** is the prompt considered as an address or search signal. Part of a prompt may steer the model towards a relevant region of its learned repertoire, while other parts provide the material on which the selected transformation operates.

For a transcription task, different Program Queries may condition different combinations of visual recognition, historical-script patterns, reading order, document structure and editorial policy. Prompt engineering can therefore be understood as an empirical external search in which a human varies the query and evaluates the resulting behaviour.

The language of coordinates, programs and trajectories remains metaphorical. It does not imply that these capabilities exist as neatly separated software modules or that the internal space of a model has been empirically mapped as a database of programs.

### **Reasoning and Test-Time Compute as Internal Search**

Reasoning models allocate additional computation during inference. Rather than immediately producing a final answer from the initial prompt, a system can use additional computational steps before committing to an output.

Within the latent-program-space metaphor, this can be understood as a partial shift from **external search** to **internal search**. Classical prompt engineering places much of the search burden on the user, who modifies a prompt and compares outputs. Reasoning and test-time compute allow more of that search to occur within a single model invocation.

This distinction is conceptual rather than mechanistic. The exact internal pathways remain only partially observable.

### **Training Shapes the Latent Program Space**

The **Latent Program Space is not designed explicitly**. It emerges from representations, transformations and behaviours learned across several training stages. **Pretraining** establishes broad statistical representations of language, images, code and other modalities. Additional training may introduce specifications or specialised material. **Post-training** shapes assistant behaviour through demonstrations, preference learning, reinforcement learning and related techniques and may also teach behaviours such as tool use.

At inference time, prompts and context condition parts of this learned repertoire for a particular task. Reasoning modes can allocate additional inference-time computation, while an AI harness extends the effective system by supplying tools, state, feedback and control over multi-step work.

This helps explain why prompting strategies cannot be universal. A formulation that works well for one model may be ineffective for another because training, post-training, system instructions, tools and inference configurations differ.

### **Excursus: Mechanistic Interpretability**

Mechanistic interpretability investigates the internal computations through which models produce outputs. Attribution-graph research has identified internal features and pathways associated with multi-step processing and other behaviours.[^50]

Related work has examined internal representations associated with concepts such as emotional states.[^51] Steering these representations can alter generated behaviour.

Such findings do not provide a direct empirical map of a latent program space. They support the more limited claim that model computation is structured, distributed and dependent on input and context. The program-space model remains a higher-level didactic metaphor.

## **The Assistant Is a Character Generated by the Model**

The conversational assistant encountered through a product interface should not be equated with the underlying model. Providers shape assistant behaviour through system instructions, post-training, policy layers and product design. Anthropic, for example, explicitly describes the design of Claude’s character and publishes a constitution that informs parts of its behaviour.[^52]

Models are trained on human communication and can therefore produce convincing social behaviour. They may appear helpful, defensive, apologetic, confident or empathetic without providing evidence of subjective experience. Generated social behaviour should not be treated as evidence that a human-like subject exists behind the interface.

A practical consequence follows. Clear and constructive communication can improve interaction, but confidence, argument and social fluency do not substitute for evidence.

### **Practical Prompting Principles**

There is no single prompt template that performs optimally across models and tasks. Useful working principles include:

* **Define the task clearly.** State what the model should do.  
* **Provide relevant context.** Supply the information required for the current task.  
* **Make constraints explicit.** Encode scholarly or technical rules where they matter.  
* **Define the output.** State the required representation or format.  
* **Iterate and evaluate.** Compare results on representative examples against explicit criteria.  
* **Use reasoning selectively.** Match inference-time reasoning to the complexity and evaluability of the task.  
* **Counter sycophancy.** Ask for evidence, alternatives or independent assessment where agreement with the user could bias the result.  
* **Generate, compare and reconcile.** Independent outputs can expose disagreements that deserve closer inspection.

These are working principles rather than timeless laws. Their value depends on the model, task and evaluation setting.

The larger engineering question is therefore increasingly not only **how a prompt is worded**, but **which knowledge, evidence, examples and tools are available when the task is executed**.

## **From Prompt Engineering to Knowledge and Context Engineering**

A research project contains more knowledge than should be inserted into a single prompt. Research questions, source documentation, data models, editorial policies, examples, mappings, design decisions, validation rules and previous findings may all matter, but not all at the same time.

**Knowledge Engineering** concerns the construction and maintenance of explicit, revisable project knowledge. It externalises assumptions and decisions so that they can be inspected, corrected and reused by people and AI systems.

**Context Engineering** concerns the information state of a particular model interaction or agent step. It determines which parts of the available knowledge are loaded, how they are ordered, which examples and tools are available and what is deliberately left out.

**Prompt Engineering** operates inside this information environment by specifying the immediate task.

The distinction can again be expressed compactly:

**Knowledge Engineering → What does the project know?** **Context Engineering → What does the model need now?** **Prompt Engineering → What should the model do now?**

The progression from prompt engineering to context engineering is therefore not a replacement of one technique by another. It is a shift in the principal engineering surface.

### **Context Engineering Shapes the Working Context**

The **context window** is the bounded sequence of tokenised information available to a model during inference.[^53] It contains supplied input together with generated tokens that remain available. Through self-attention, the model can relate information within this sequence when producing subsequent tokens.

The formal context limit is not equivalent to effective context use. Research on **context rot** indicates that the ability to retrieve and apply relevant information can decline as contexts become longer and more cluttered.[^54] A large context window therefore does not imply that every included token contributes equally to reliable performance.

Context engineering selects, orders, retrieves, compresses and sometimes discards information so that relevant knowledge remains available when needed.

The goal is not to maximise the amount of context. It is to maximise the usefulness of the active context for the current task.

### **Markdown and Knowledge Documents**

Markdown is a lightweight markup language that represents document structure in human-readable plain text. Headings, lists, links, code blocks and emphasis are expressed with minimal syntax. This makes Markdown convenient for project knowledge that should be readable by researchers, versionable in Git and directly usable as model context.

Markdown is not universally superior to other formats. TEI, JSON, RDF, XML, databases, schemas and configuration files remain essential where richer semantics or formal constraints are required. Its practical advantage for project knowledge is portability and low representational overhead.

A **knowledge document** is an atomic, structured and verifiable unit of externalised project knowledge, distilled from sources, data or experience for reuse by people and AI systems.

Useful knowledge documents are:

* **Dual-readable:** usable by people and AI systems.  
* **Compact:** distilled within a limited context budget.  
* **Traceable:** claims and decisions can be related to sources or project evidence.  
* **Revisable:** errors and new findings can be incorporated.  
* **Portable:** open and text-based formats can be retrieved, linked, versioned and exchanged.

A project knowledge base may contain Markdown documents alongside schemas, configuration files, structured data and executable tests. The important point is not the file extension but the externalisation of knowledge in forms that can be inspected and operationalised.

This also changes the role of documentation. The persistent research record does not necessarily have to consist of every individual prompt issued to a model. What must be documented depends on the research claim and evaluation goal.

When prompts themselves are the object of an experiment, their wording and configuration are evidence. In a production workflow, however, a prompt may be a transient operational artefact generated from a larger maintained knowledge base.

Documentation should preserve the information required to reconstruct and assess the relevant process. Depending on the workflow, this may include source identifiers, project rules, relevant system configurations, transformations, outputs, validation results, editorial status and provenance.

## **Promptotyping**

**Promptotyping** is an iterative, knowledge-based **context-engineering method** that translates structured research data and curated project knowledge into digital research artefacts for specific projects.[^55]

It integrates knowledge engineering, context engineering and agentic engineering within a single development process and keeps implementation connected to scholarly assessment.

Promptotyping begins with maintained project knowledge rather than an isolated prompt. Research data, scholarly requirements, examples, design decisions and verification criteria are made explicit. Relevant parts of this knowledge are selected as context for a concrete task.

An agent uses this context to create or modify a research artefact inside an executable environment. The resulting implementation is assessed against technical and scholarly criteria. Findings from implementation and review are not automatically treated as new knowledge. They are examined before relevant information is incorporated into the maintained project knowledge base.

The process can be represented as:

MAINTAINED PROJECT KNOWLEDGE

            |

            v

      CONTEXT SELECTION

            |

            v

     AGENTIC IMPLEMENTATION

            |

            v

EVALUATION / VALIDATION / VERIFICATION

            |

            v

      CURATED FEEDBACK

            |

            \+--------------------\> PROJECT KNOWLEDGE

Promptotyping therefore treats research software and research data as evolving artefacts whose development remains connected to explicit project knowledge and scholarly judgement.

The prompt is one operational component inside this process, not its persistent centre.

## **Agentic Engineering and AI Harnesses**

An **AI agent** is a system that can select and execute actions across multiple steps in response to intermediate results. The concept predates LLMs.[^56] LLM-based agents are a contemporary form in which natural language, code and heterogeneous project files can become part of the same control interface.

An **AI harness** is the software environment that enables a model to operate within such a system. It manages context, tools, action execution, feedback, state, permissions and the control loop.[^57]

Examples include Claude Code, Codex, Cursor and Pi. A harness may allow a model to inspect a repository, edit files, execute terminal commands and interpret the resulting output. It can preserve state across several actions and constrain which resources are available.

**Agentic Engineering** concerns the design and governance of this complete environment rather than the generation of a single response.

An agent may:

* inspect files,  
* modify documents,  
* write code,  
* execute programs,  
* run tests,  
* compare outputs,  
* query project knowledge,  
* interpret feedback,  
* revise previous actions.

The relevant unit of analysis is therefore the complete system:

**model \+ harness \+ context \+ tools \+ state \+ permissions \+ executable environment \+ feedback**

In research data workflows, agentic engineering should govern at least four questions:

1. What information and files may the agent access?  
2. What actions and tools may it execute?  
3. What evidence does the environment return about those actions?  
4. Which outputs require further assessment before they are accepted?

The harness is not itself the scholarly method. It does not determine which project knowledge is relevant, which representation is adequate or whether an interpretation should be accepted. Those decisions belong to the research design and its epistemic infrastructure.

### **AI Agents Existed Long before LLMs**

The concept of an AI agent predates large language models. Classical definitions describe agents as systems that perceive an environment, select actions and pursue goals with some degree of autonomy.[^58]

Earlier AI systems demonstrated planning, game playing and embodied interaction without LLMs. Systems such as AlphaGo and multi-agent reinforcement-learning environments already involved autonomous action and feedback.

LLMs changed the practical design space because natural language, code and heterogeneous project files can now serve as interfaces for action. Systems such as Voyager demonstrated how an LLM can guide an embodied agent through repeated interaction with an environment.[^59]

LLM-based agents should therefore be understood as one contemporary form of a much older computational concept.

## **Hands-on 2: From Transcription to Information Extraction**

The transcription produced in Hands-on 1 can become the input for a second task. Instead of reproducing the source text, the model now transforms an existing textual representation according to an explicit information model.

The workflow therefore distinguishes:

**facsimile → transcription**

from

**transcription → structured information**

These operations have different inputs, outputs, failure modes and verification criteria. The extraction schema, target entities and acceptance criteria must therefore be defined independently of the transcription task.

The exercise illustrates a broader principle: a research data workflow consists of multiple representational transitions. Each transition can introduce new information, interpretation and uncertainty and therefore requires its own form of assessment.

## **Evaluation, Validation and Scholarly Verification**

AI-supported research workflows require several forms of checking that should not be collapsed into a single category.

**Evaluation** measures performance against an explicit criterion.

**Validation** tests whether an artefact conforms to a formal or operational requirement.

**Scholarly verification** assesses whether a representation, claim or decision is adequate to the source, research question and disciplinary standards.

For example, a transcription can be evaluated against a human reference using Character Error Rate. TEI XML can be validated against a schema. A named entity can be compared with a curated authority record. An ambiguous historical reference may still require disciplinary judgement that cannot be reduced to a formal test.

These distinctions matter because formal correctness does not entail scholarly adequacy. A schema can establish that an element is legally placed without establishing that the editor selected the appropriate element. A model-based review can identify disagreement without determining which interpretation is historically justified.

Not every research object requires the same combination of evaluation, validation and verification. The relevant procedures depend on the representation, research claim and acceptance criteria.

Responsibility therefore remains with the researchers who define those criteria and decide when the available evidence is sufficient for an output to be accepted within the research workflow.

## **Conclusion**

The practical significance of contemporary generative AI for research data workflows does not lie in a single prompting technique. It lies in the combination of general-purpose models with explicit project knowledge, managed context, tools, executable environments and feedback.

**Prompt Engineering** specifies the immediate task. **Knowledge Engineering** maintains what the project knows. **Context Engineering** determines what the model needs for the current task. **Agentic Engineering** governs how an LLM-based system can act within a computational environment. Promptotyping connects these layers through iterative implementation, assessment and curated feedback.

The resulting shift is from individual model outputs towards the design of complete **technical and epistemic research environments**. Generative models can substantially amplify computational research where knowledge can be externalised and outputs can be checked. This does not remove scholarly responsibility. It increases the importance of making assumptions, provenance, transformations, assessment procedures and decisions inspectable within the research workflow.

[^1]: The term *Applied Generative AI* also informs the DHd Working Group [*Angewandte Generative KI in den Digitalen Geisteswissenschaften (AGKI-DH)*](https://agki-dh.github.io/), founded by Christopher Pollin and Gerrit Brüning.

[^2]: Jonathan D. Geiger, [Daten / Forschungsdaten](https://doi.org/10.17175/wp_2023_003_v2), version 2.0, 2024\.

[^3]: Christof Schöch, [Big? Smart? Clean? Messy? Data in the Humanities](https://journalofdigitalhumanities.org/2-3/big-smart-clean-messy-data-in-the-humanities/), *Journal of Digital Humanities* 2, no. 3, 2013\.

[^4]: Johanna Drucker, [Humanities Approaches to Graphical Display](https://digitalhumanities.org/dhq/vol/5/1/000091/000091.html), *Digital Humanities Quarterly* 5, no. 1, 2011\.

[^5]: Stefan Zweig Digital, [Notizbuch *Clarissa*, SZ-AAP/W1](https://gams.uni-graz.at/o:szd.947), dated 1 November 1941\.

[^6]: Neil Majithia et al., [An Actionable Framework for AI-Ready Data](https://doi.org/10.1002/aaai.70054), *AI Magazine* 47, no. 1, 2026\.

[^7]: Mark D. Wilkinson et al., [The FAIR Guiding Principles for Scientific Data Management and Stewardship](https://doi.org/10.1038/sdata.2016.18), *Scientific Data* 3, 2016\.

[^8]: MLCommons, [Croissant](https://mlcommons.org/working-groups/data/croissant/).

[^9]: Global Indigenous Data Alliance, [CARE Principles for Indigenous Data Governance](https://www.gida-global.org/careprinciples).

[^10]: Sander Schulhoff et al., [The Prompt Report: A Systematic Survey of Prompting Techniques](https://doi.org/10.48550/arXiv.2406.06608), 2024\.

[^11]: Bradley Allen et al., [Knowledge Engineering Using Large Language Models](https://doi.org/10.4230/TGDK.1.1.3), 2023\.

[^12]: Linyao Mei et al., [A Survey of Context Engineering for Large Language Models](https://doi.org/10.48550/arXiv.2507.13334), 2025\.

[^13]: See Hailin Zhong and Shengxin Zhu, [AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents](https://doi.org/10.48550/arXiv.2605.13357), 2026, and Ranjan Sapkota et al., [AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications, and Challenges](https://doi.org/10.1016/j.inffus.2025.103599), 2026\.

[^14]: Zentralbibliothek Zürich, [Jeanne Hersch: Digitale Neuauflage der Schriften](https://www.zb.uzh.ch/de/jeanne-hersch-digitale-neuauflage-der-schriften).

[^15]: The Jeanne Hersch repository uses `mistral-document-ai-2512` as its Azure deployment name. The corresponding Mistral API model is `mistral-ocr-2512`. See Mistral AI, [Introducing Mistral OCR 3](https://mistral.ai/news/mistral-ocr-3/) and the [OCR 3 model documentation](https://docs.mistral.ai/models/model-cards/ocr-3-25-12). See also the [Docling documentation](https://docling.ai/) and Nikolaos Livathinos et al., [Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion](https://arxiv.org/abs/2501.17887), 2025\.

[^16]: Claude Code is Anthropic’s agentic development environment for working with repositories and executable tools. See Anthropic, [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview).

[^17]: Google, [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite). The Stefan Zweig repository records the preview identifier `gemini-3.1-flash-lite-preview` for its initial transcription data.

[^18]: Artificial Analysis maintains a continuously updated comparison of contemporary models across capability, price, speed, latency and related characteristics. [Artificial Analysis LLM Leaderboard](https://artificialanalysis.ai/leaderboards/models).

[^19]: **Open Source AI Definition 1.0** defines Open Source AI through the freedoms to use, study, modify and share and requires access to the preferred form for modification, including information about training data, source code and model parameters. Open Source Initiative, [The Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition).

[^20]: The **European Open Source AI Index** is an academic resource for comparing AI systems across 14 dimensions of openness, including training data, documentation, licensing and access. [European Open Source AI Index](https://osai-index.eu/).

[^21]: **Open-washing** describes claims of openness that overstate the actual accessibility or reproducibility of generative AI systems. Andreas Liesenfeld and Mark Dingemanse, “Rethinking Open Source Generative AI: Open-Washing and the EU AI Act,” *FAccT ’24*, 2024\. [https://doi.org/10.1145/3630106.3659005](https://doi.org/10.1145/3630106.3659005).

[^22]: Mark Dingemanse, “Generative AI and Research Integrity,” preprint, OSF, 14 May 2024\. The paper develops a values-first approach to generative AI in academic research. [https://doi.org/10.31219/osf.io/2c48n](https://doi.org/10.31219/osf.io/2c48n).

[^23]: **Local deployment** means that model inference runs on hardware controlled by the researcher or institution rather than exclusively through a third-party hosted service. Examples include [Ollama](https://ollama.com) and [LM Studio](https://lmstudio.ai).

[^24]: An **AI harness** is the software environment through which a model receives context, accesses tools, executes actions, maintains state and processes feedback. Examples include [Claude Code](https://www.anthropic.com/product/claude-code), [Codex](https://openai.com/codex), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [Mistral Vibe](https://mistral.ai/news/devstral-2-vibe-cli), [Qwen Code](https://github.com/QwenLM/qwen-code), [Kimi Code](https://github.com/MoonshotAI/kimi-cli), [Pi](https://pi.dev) and [Cursor](https://cursor.com).

[^25]: OpenAI chief scientist Jakub Pachocki has described “automating research” as a major objective, while Anthropic CEO Dario Amodei has discussed the prospect of extremely capable AI systems as “a country of geniuses in a datacenter”. See Christopher Pollin, [“Asymmetric Amplification. Why AI Does Not Automate Research — But Disruptively Amplifies Computer-Based Research Work”](https://dhcraft.org/excellence/blog/Asymmetric-Amplification/) and Dario Amodei, [*The Adolescence of Technology*](https://www.darioamodei.com/essay/the-adolescence-of-technology), 2026\.

[^26]: The **METR Task-Completion Time Horizon** estimates the duration of software tasks that AI agents can complete at specified success probabilities. It is not a general measure of intelligence or research capability. See [METR, Task-Completion Time Horizons of Frontier AI Models](https://metr.org/time-horizons) and Megan Kinniment et al., [“Measuring AI Ability to Complete Long Tasks”](https://arxiv.org/abs/2503.14499), 2025\.

[^27]: **ARC-AGI-3** is an interactive benchmark in which agents must explore unfamiliar environments, infer goals and rules, plan and adapt without natural-language instructions. ARC Prize reported a frontier-model score of 0.51% when the benchmark launched in March 2026\. Claude Opus 5 subsequently reached 30.16% on the ARC-AGI-3 Public Demo evaluation in July 2026\. See [ARC Prize, “Announcing ARC-AGI-3”](https://arcprize.org/blog/arc-agi-3-launch) and [Claude Opus 5: ARC-AGI Results](https://arcprize.org/results/anthropic-claude-opus-5).

[^28]: **Formal theorem proving** represents mathematical statements and proofs in a formal language and checks them mechanically with a proof assistant such as Lean. This provides a particularly strong feedback environment because invalid proof steps can be rejected deterministically. See Nikil Ravi et al., [“FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?”](https://arxiv.org/abs/2603.26996), 2026, and Po-Nien Kung et al., [“LEAP: Supercharging LLMs for Formal Mathematics with Agentic Frameworks”](https://arxiv.org/abs/2606.03303), 2026\.

[^29]: OpenAI reported ten results produced by an internal version of Astra that resolve or substantially advance open problems across several areas of mathematics and theoretical computer science. The company states that the resulting arguments were subsequently formalised as Lean certificates and explicitly assumes responsibility for the correctness of the published results. See OpenAI, [“Ten advances in mathematics and theoretical computer science”](https://openai.com/index/ten-advances-in-mathematics/), 2026\.

[^30]: The UK AI Security Institute evaluates frontier systems across cyber tasks involving vulnerability discovery, exploitation and malware development. Its *Frontier AI Trends Report* finds rapid improvement across all tested cyber difficulty levels and reports that leading systems now complete apprentice-level tasks around 50% of the time on average, compared with below 9% in late 2023\. [AI Security Institute, *Frontier AI Trends Report*](https://www.aisi.gov.uk/frontier-ai-trends-report).

[^31]: OpenAI reported on 7 August 2026 that internal evaluations of its upcoming Astra model showed sufficiently advanced agentic coding and cybersecurity performance that the company could no longer rule out **Critical** cybersecurity capability under its Preparedness Framework. At this threshold, a model could potentially develop functional zero-day exploits against hardened real-world systems or devise and execute novel end-to-end attack strategies with minimal human direction. [OpenAI, “Responding to the next frontier of critical cyber capabilities”](https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/).

[^32]: **AI 2027** is a scenario rather than a forecast or empirical evaluation. It explores a possible trajectory in which AI-assisted AI research contributes to accelerating further model development. See AI Futures Project, [*AI 2027*](https://ai-2027.com).

[^33]: **Asymmetric amplification** describes the uneven strengthening of existing human capabilities by AI systems. Amplification is particularly strong where expertise can be externalised, tasks are computationally actionable and outputs receive meaningful feedback. Christopher Pollin, [“Asymmetric Amplification. Why AI Does Not Automate Research — But Disruptively Amplifies Computer-Based Research Work”](https://dhcraft.org/excellence/blog/Asymmetric-Amplification/), 2026\.

[^34]: Mrinank Sharma et al., [Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548), 2023\.

[^35]: Jack Lindsey et al., [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html), Transformer Circuits, 2025\.

[^36]: Anthropic, [Thinking](https://platform.claude.com/docs/en/about-claude/models/extended-thinking-models).

[^37]: Microsoft, [Get Started with Visual Studio Code](https://code.visualstudio.com/docs/getstarted/overview).

[^38]: Sander Schulhoff et al., [The Prompt Report: A Systematic Survey of Prompting Techniques](https://doi.org/10.48550/arXiv.2406.06608), 2024\.

[^39]: Cheng Li et al., [Large Language Models Understand and Can Be Enhanced by Emotional Stimuli](https://doi.org/10.48550/arXiv.2307.11760), 2023\.

[^40]: Sondos Mahmoud Bsharat, Aidar Myrzakhan and Zhiqiang Shen, [Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4](https://doi.org/10.48550/arXiv.2312.16171), 2023\.

[^41]: Vipula Rawte et al., [Exploring the Relationship between LLM Hallucinations and Prompt Linguistic Nuances: Readability, Formality, and Concreteness](https://doi.org/10.48550/arXiv.2309.11064), 2023\.

[^42]: Ziqi Yin et al., [Should We Respect LLMs? A Cross-Lingual Study on the Influence of Prompt Politeness on LLM Performance](https://doi.org/10.48550/arXiv.2402.14531), 2024\.

[^43]: Rick Battle and Teja Gollapudi, [The Unreasonable Effectiveness of Eccentric Automatic Prompts](https://doi.org/10.48550/arXiv.2402.10949), 2024\.

[^44]: Meghana Rajeev et al., [Cats Confuse Reasoning LLM: Query Agnostic Adversarial Triggers for Reasoning Models](https://doi.org/10.48550/arXiv.2503.01781), 2025\.

[^45]: Savir Basil et al., [Playing Pretend: Expert Personas Don’t Improve Factual Accuracy](https://arxiv.org/abs/2512.05858), 2025\.

[^46]: Tiancheng Hu and Nigel Collier, [Quantifying the Persona Effect in LLM Simulations](https://doi.org/10.48550/arXiv.2402.10811), 2024\.

[^47]: Stefan Zweig Digital, [Source object `o:szd.139`](https://gams.uni-graz.at/o:szd.139) and the corresponding [facsimile in the project interface](https://chpollin.github.io/szd-htr-ocr-pipeline/#view/o_szd.139_gemini-3.1-flash-lite-preview/1).

[^48]: Stefan Zweig Digital, *Radiovortrag über Newyork*, 1935, manuscript, 12 leaves, Literaturarchiv Salzburg, shelfmark SZ-AAP/W27.

[^49]: François Chollet, [How I think about LLM prompt engineering](https://fchollet.substack.com/p/how-i-think-about-llm-prompt-engineering), 2023\.

[^50]: Jack Lindsey et al., [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html), Transformer Circuits, 2025\.

[^51]: Nicholas Sofroniew et al., [Emotion Concepts and Their Function in a Large Language Model](https://transformer-circuits.pub/2026/emotions/index.html), 2026\.

[^52]: Anthropic, [Claude’s Constitution](https://www.anthropic.com/constitution) and [Claude’s Character](https://www.anthropic.com/research/claude-character).

[^53]: Ashish Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017\.

[^54]: Kelly Hong, Anton Troynikov and Jeff Huber, [Context Rot: How Increasing Input Tokens Impacts LLM Performance](https://research.trychroma.com/context-rot), Chroma, 2025\.

[^55]: Christopher Pollin, [Promptotyping: Zwischen Vibe Coding, Vibe Research und Context Engineering](https://lisa.gerda-henkel-stiftung.de/digitale_geschichte_pollin), 2026, and the [Promptotyping repository](https://github.com/DigitalHumanitiesCraft/Promptotyping).

[^56]: Michael Wooldridge and Nicholas R. Jennings, [Intelligent Agents: Theory and Practice](https://doi.org/10.1017/S0269888900008122), *The Knowledge Engineering Review* 10, no. 2, 1995\.

[^57]: Hailin Zhong and Shengxin Zhu, [AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents](https://doi.org/10.48550/arXiv.2605.13357), 2026\.

[^58]: Michael Wooldridge and Nicholas R. Jennings, [Intelligent Agents: Theory and Practice](https://doi.org/10.1017/S0269888900008122), *The Knowledge Engineering Review* 10, no. 2, 1995\.

[^59]: Guanzhi Wang et al., [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291), 2023\.