# Literature Anchors for the Terminology Matrix

Research draft for `knowledge/begriffe.md`. Each term of the matrix receives two to four citable anchors, so that the definitions rest on publicly verifiable references rather than on the author's private knowledge base. Anchor types are Anthropic documentation and engineering posts, peer-reviewed or archived academic papers, widely received practitioner posts, and standard reference works.

All web sources were accessed on 2026-08-20. Where a source carries a DOI it is given in place of a URL. The section "Knowledge Work" covers a term that appears in the project title but is missing from the matrix and should be added as a row.

## Knowledge Work

1. Drucker, Peter F. (1959). *Landmarks of Tomorrow. A Report on the New "Post-Modern" World*. New York, Harper & Brothers.
   Coins "knowledge worker" and "knowledge work" and sets the constitutive criterion, work paid for the application of theoretical knowledge and the exercise of judgment rather than for manual execution or supervision.
2. Drucker, Peter F. (1999). Knowledge-Worker Productivity. The Biggest Challenge. *California Management Review* 41(2), 79–94. DOI 10.2307/41165987.
   Reformulates knowledge work around the productivity question and names its six determining factors, including the worker's own definition of the task and the requirement of continuous learning; the reference point for any claim that agentic systems change knowledge-work productivity.
3. Davenport, Thomas H. (2005). *Thinking for a Living. How to Get Better Performance and Results from Knowledge Workers*. Boston, Harvard Business School Press. ISBN 978-1-59139-423-5.
   Supplies an empirically grounded typology of knowledge work by degree of interdependence and task complexity, which allows the matrix to distinguish knowledge work that agents can carry from work that they can only support.

## Knowledge Engineering

1. Studer, Rudi; Benjamins, V. Richard; Fensel, Dieter (1998). Knowledge Engineering. Principles and Methods. *Data & Knowledge Engineering* 25(1–2), 161–197. DOI 10.1016/S0169-023X(97)00056-6.
   The canonical definition. Establishes the shift from the transfer approach, which treats knowledge as something extracted from an expert and moved into a system, to the modelling approach, which treats knowledge engineering as the construction of a model of problem-solving behaviour.
2. Newell, Allen (1982). The Knowledge Level. *Artificial Intelligence* 18(1), 87–127. DOI 10.1016/0004-3702(82)90012-1.
   Introduces the knowledge level as a description layer above the symbol level, where an agent is characterized by goals, actions and the principle of rationality; the theoretical precondition for talking about knowledge independently of its representation.
3. Schreiber, Guus; Akkermans, Hans; Anjewierden, Anjo; de Hoog, Robert; Shadbolt, Nigel; Van de Velde, Walter; Wielinga, Bob (2000). *Knowledge Engineering and Management. The CommonKADS Methodology*. Cambridge MA, MIT Press. ISBN 978-0-262-19300-9.
   The methodological build-out of the modelling approach into an operational suite of models (organization, task, agent, knowledge, communication, design), useful as the historical foil against which document-based knowledge engineering for LLM agents can be positioned.

## Prompt Engineering

1. Brown, Tom B. et al. (2020). Language Models are Few-Shot Learners. *Advances in Neural Information Processing Systems* 33, 1877–1901. arXiv:2005.14165. DOI 10.48550/arXiv.2005.14165.
   Establishes in-context learning as the mechanism that makes prompting a form of programming at all, since task behaviour is induced through the input sequence without a parameter update.
2. Reynolds, Laria; McDonell, Kyle (2021). Prompt Programming for Large Language Models. Beyond the Few-Shot Paradigm. *CHI '21 Extended Abstracts*, Article 314. DOI 10.1145/3411763.3451760.
   The first sustained conceptualization of prompting as programming, arguing that a prompt locates a task within the model's learned distribution rather than teaching it; the direct conceptual bridge to the latent-program vocabulary of the matrix.
3. Liu, Pengfei; Yuan, Weizhe; Fu, Jinlan; Jiang, Zhengbao; Hayashi, Hiroaki; Neubig, Graham (2023). Pre-train, Prompt, and Predict. A Systematic Survey of Prompting Methods in Natural Language Processing. *ACM Computing Surveys* 55(9), Article 195. DOI 10.1145/3560815.
   The standard academic survey, providing the terminological grid (template, answer space, prompt-based learning paradigm) that allows prompt engineering to be defined without recourse to practitioner folklore.
4. Anthropic (n.d.). Prompt engineering overview. Claude Platform Docs. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
   The vendor-side operational framing. Makes prompt engineering conditional on prior success criteria and evaluations, and delimits it against choices better solved by model selection; the living technique reference it points to is Prompting best practices (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).

## Context Engineering

1. Karpathy, Andrej (2025-06-25). Post on X. https://x.com/karpathy/status/1937902205765607626
   The coinage that established the term in practice, defining context engineering as the art and science of filling the context window with exactly the right information for the next step and explicitly positioning it against the narrower reading of prompt engineering.
2. Anthropic (2025-09-29). Effective context engineering for AI agents. Anthropic Engineering Blog. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
   The load-bearing definition for the matrix, context engineering as the set of strategies for curating and maintaining the optimal set of tokens during inference, together with the two decisive framings, context as a finite resource with diminishing marginal returns, and just-in-time retrieval through lightweight identifiers instead of pre-loading.
3. LangChain (2025-07-02). Context Engineering. LangChain Blog. https://www.langchain.com/blog/context-engineering-for-agents
   Supplies the widely adopted four-part taxonomy of strategies (write, select, compress, isolate), which gives the matrix a structure for the operational side of the term.

## Agentic Engineering

1. Karpathy, Andrej (2026-04-30). Sequoia Ascent 2026 summary. https://karpathy.bearblog.dev/sequoia-ascent-2026/
   Karpathy's own account of the term he introduced at Sequoia Ascent 2026, agentic engineering as the discipline of coordinating fallible agents without sacrificing the quality bar of professional software, delimited against vibe coding by the claim that it raises the ceiling rather than the floor.
2. AGENT 2026. International Workshop on Agentic Engineering, co-located with ICSE 2026, 2026-04-14. https://conf.researchr.org/home/icse-2026/agent-2026
   The academic institutionalization of the term, scoping agentic engineering as the design, development and operation of systems exhibiting goal-directed autonomy, and naming the new challenges (autonomy, tool integration, prompt-driven behaviour, post-deployment adaptation) that separate it from classical agent-oriented software engineering.
3. Hassan, Ahmed E.; Li, Hao; Lin, Dayi; Adams, Bram; Chen, Tse-Hsun; Kashiwa, Yutaro; Qiu, Dong (2025). Agentic Software Engineering. Foundational Pillars and a Research Roadmap. arXiv:2509.06216. DOI 10.48550/arXiv.2509.06216.
   Proposes the dual-modality distinction between software engineering for humans and for agents, plus the split into a command environment for oversight and an execution environment for agent work; the most explicit research-side articulation of what an engineering discipline around agents has to cover.

## AI Agent and Agentic AI

1. Anthropic (2024-12-19). Building effective agents. Anthropic Engineering Blog. https://www.anthropic.com/engineering/building-effective-agents
   The reference distinction the matrix should adopt. Agentic systems is the umbrella; workflows are systems where models and tools are orchestrated through predefined code paths; agents are systems where models dynamically direct their own processes and tool usage.
2. Wooldridge, Michael; Jennings, Nicholas R. (1995). Intelligent Agents. Theory and Practice. *The Knowledge Engineering Review* 10(2), 115–152. DOI 10.1017/S0269888900008122.
   The classical agent definition (autonomy, reactivity, pro-activeness, social ability) against which the LLM-era usage can be measured, and the historical link between the agent concept and knowledge engineering.
3. Sapkota, Ranjan; Roumeliotis, Konstantinos I.; Karkee, Manoj (2025). AI Agents vs. Agentic AI. A Conceptual Taxonomy, Applications and Challenges. arXiv:2505.10468. DOI 10.48550/arXiv.2505.10468.
   Argues the terminological separation the matrix has to decide on, AI agents as modular systems for task-specific automation, agentic AI as a paradigm of multi-agent collaboration, dynamic task decomposition, persistent memory and coordinated autonomy.

## AI Harness

1. Anthropic (2025-11-26). Effective harnesses for long-running agents. Anthropic Engineering Blog. https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
   Shows the harness as the environment-management layer for work spanning multiple context windows, with initializer and coding agent, feature lists, testing frameworks, initialization scripts and progress artefacts as its components.
2. Martin, Lance (2026-04-02). Agent Harness Design. 3 Patterns for Harnessing Claude's Intelligence. Claude by Anthropic. https://claude.com/blog/harnessing-claudes-intelligence
   Carries the crispest available definition, the harness as the software scaffolding around a model, comprising the loop, tools, context management and guardrails that turn raw intelligence into a working agent.
3. METR (2024-03-15). Guidelines for capability elicitation. https://metr.org/blog/2024-03-15-guidelines-for-capability-elicitation/
   The evaluation-side vocabulary. Treats scaffolding as the structural support around a model (chain-of-thought, command-line access with returned output, management of long tasks under context limits) and elicitation as the process of actively improving model performance on evaluation tasks through prompting, tooling and finetuning; establishes that measured capability is a property of model and harness together. METR's evaluation reports add the operative phrasing, an agent as a language model wrapped by an agent scaffolding program that repeatedly chooses a tool action or a reasoning step (https://evaluations.metr.org/gpt-4o-report/).

## Promptotyping

1. Pollin, Christopher (2025-04-24). Promptotyping. Von der Idee zur Anwendung. Digital Humanities Craft. https://dhcraft.org/excellence/blog/Promptotyping/
   The first published statement of the method, defining Promptotyping as the contraction of prompt and prototype and stating its aim, documenting requirements quickly and precisely rather than producing finished software directly. Also introduces the Promptotyping Documents and their WHAT, USING WHAT, HOW structure.
2. Pollin, Christopher; Steyer, Timo; Scholger, Martina; Schiller-Stoff, Sebastian David (2025). Fortgeschrittenes Prompt und AI Agent Engineering für wissenschaftliche Textproduktion. DHd 2025, Under Construction. DOI 10.5281/zenodo.14943178.
   The citable conference record that anchors the method in the Digital Humanities community and supplies a peer-reviewed reference point instead of a blog-only provenance.
3. Pollin, Christopher (2026-01-17). Promptotyping. Zwischen Vibe Coding, Vibe Research und Context Engineering. L.I.S.A. Wissenschaftsportal der Gerda Henkel Stiftung. https://lisa.gerda-henkel-stiftung.de/digitale_geschichte_pollin
   The current definition, Promptotyping as an iterative context-engineering technique in four phases for developing research artefacts with frontier models in a data-driven way, with the delimitation against vibe coding and the role of context compression.
4. Digital Humanities Craft OG (n.d.). Promptotyping. Specification of the Method. https://dhcraft.org/Promptotyping/
   The method's own specification site, to be cited as the source of truth for the current phase model and document set.

## Knowledge Document

1. Pollin, Christopher (2025-04-24). Promptotyping. Von der Idee zur Anwendung. Digital Humanities Craft. https://dhcraft.org/excellence/blog/Promptotyping/
   The origin of the Promptotyping Documents as a document class, structured Markdown files that hold requirements, data model and implementation rules in compressed form for model consumption; the immediate ancestor of the matrix term.
2. Anthropic (n.d.). Agent Skills. Claude Platform Docs. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
   Provides the mechanism that makes a knowledge document operational, progressive disclosure across three levels, metadata always loaded, instructions loaded on trigger, bundled resources read only when referenced; the vendor-side answer to the question of how written knowledge enters a working context without occupying it permanently.
3. AGENTS.md (n.d.). https://agents.md/
   The cross-vendor standardization of the repository-level knowledge document, described on the site as a simple open format for guiding coding agents and as a README for agents, stewarded by the Agentic AI Foundation under the Linux Foundation; shows that the document class exists independently of any single tool.
4. Nonaka, Ikujiro (1994). A Dynamic Theory of Organizational Knowledge Creation. *Organization Science* 5(1), 14–37. DOI 10.1287/orsc.5.1.14.
   Supplies the theoretical frame for what writing a knowledge document does, externalization as the conversion of tacit into explicit knowledge, and the reminder that the conversion is lossy and cyclical rather than a one-time transfer.

## Latent Program Space and Program Key

1. Chollet, François (2019). On the Measure of Intelligence. arXiv:1911.01547. DOI 10.48550/arXiv.1911.01547.
   The conceptual source, intelligence as skill-acquisition efficiency relative to priors, experience and generalization difficulty, and the framing of a task solution as a program to be found rather than a skill to be possessed.
2. Bonnet, Clement; Macfarlane, Matthew V. (2024). Searching Latent Program Spaces. arXiv:2411.08706. DOI 10.48550/arXiv.2411.08706.
   Gives the term its technical content, a learned latent space of implicit programs mapping inputs to outputs, searchable at test time by gradient, without a predefined domain-specific language; the closest published referent for the matrix entry.
3. Xie, Sang Michael; Raghunathan, Aditi; Liang, Percy; Ma, Tengyu (2022). An Explanation of In-context Learning as Implicit Bayesian Inference. ICLR 2022. arXiv:2111.02080. DOI 10.48550/arXiv.2111.02080.
   The mechanism behind the program-key intuition, in-context learning as inference of a shared latent concept from the prompt, which grounds the claim that a prompt selects a program rather than instructing one.
4. Reynolds, Laria; McDonell, Kyle (2021). Prompt Programming for Large Language Models. Beyond the Few-Shot Paradigm. *CHI '21 Extended Abstracts*, Article 314. DOI 10.1145/3411763.3451760.
   States the locating reading of prompts explicitly, a prompt as a way of finding an already-learned task in the model, which is the practitioner-facing formulation of the program key.

## Verification Levels

1. Wei, Jason (2025-07). Asymmetry of verification and verifier's law. https://www.jasonwei.net/blog/asymmetry-of-verification-and-verifiers-law
   Supplies the ordering principle for the levels, the asymmetry between solving and checking, and verifier's law, the ease of training a system for a task being proportional to how verifiable the task is; also names the inverse case where verification costs more than proposal.
2. Zheng, Lianmin; Chiang, Wei-Lin; Sheng, Ying; Zhuang, Siyuan; Wu, Zhanghao; Zhuang, Yonghao; Lin, Zi; Li, Zhuohan; Li, Dacheng; Xing, Eric P.; Zhang, Hao; Gonzalez, Joseph E.; Stoica, Ion (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. *Advances in Neural Information Processing Systems* 36. arXiv:2306.05685. DOI 10.48550/arXiv.2306.05685.
   The empirical basis for the level between machine-decidable checking and human judgment, showing both the agreement rates that make model-based judging usable and the biases (position, verbosity, self-enhancement) that keep it from being an automatic check.
3. Pollin, Christopher (2025-05-27). Promptotyping mit Claude Sonnet 4. Vibe-Coding erfordert den Critical-Expert-in-the-Loop. Digital Humanities Craft. https://dhcraft.org/excellence/blog/Critical-Vibing-Claude-4/
   Names the top verification level in the project's own vocabulary, the critical expert in the loop as the combination of domain competence and epistemic reflection, with a double feedback loop of human examination and machine self-critique.
4. Anthropic (2024-12-19). Building effective agents. Anthropic Engineering Blog. https://www.anthropic.com/engineering/building-effective-agents
   Locates verification inside the system design, through the evaluator-optimizer pattern for automated checking loops and through the guidance on human checkpoints and guardrails where autonomy is granted.

## Open Points

- The matrix row "Latent Program Space, Program Key" carries drift note D1. The published literature supports "latent program space" as a technical term but not "program key" as a received term; the anchors above justify the concept while leaving the coinage to be marked as the project's own.
- "Agentic Engineering" now has a datable coinage and an academic venue, so the matrix can state the term as established rather than as an in-house label.
- "Knowledge Document" has no single canonical definition. The four anchors cover the method side, the mechanism side, the standardization side and the theory side, which is enough for a defensible definition but requires the matrix to state which reading it adopts.
