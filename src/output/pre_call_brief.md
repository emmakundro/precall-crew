# Pre-Call Brief: CrewAI

---

## Company Snapshot

- **What they do:** CrewAI builds an open-source multi-agent orchestration platform (47.8K+ GitHub stars, 27M+ PyPI downloads) that lets enterprises design, deploy, and govern collaborative AI agent "crews" across complex workflows. Their full lifecycle pitch: *Discover → Build → Deploy → Govern → Optimize.*
- **Who they sell to:** Enterprise companies ($100M+ revenue) across Financial Services, Healthcare, Manufacturing, and Government. Named customers include PwC, PepsiCo, DocuSign, Johnson & Johnson, and the U.S. Department of Defense — spanning 63% of the Fortune 500 by their own claim.
- **Scale signals:** 2 billion agentic workflow executions in the past 12 months; 150+ enterprise beta customers signed in under 6 months after enterprise launch; average deal size up 5.5x YoY; customers expanding 11x within their first 12 months.
- **Leadership:** CEO João (Joe) Moura is a technical founder with 20+ years in software engineering. He is the public face of the company's architecture thinking, publishes regularly on production AI lessons, and runs CrewAI agents internally across GTM, engineering, and marketing. Expect a peer-level technical conversation, not a sales pitch back.

---

## What's Happening Now

- **Fresh capital, April 2026:** CrewAI closed a **$20M Series B-1** at an approximately $177M post-money valuation (PitchBook), bringing total disclosed funding to ~$38–44M. Boldstart Ventures and Insight Partners are lead investors; Andrew Ng and Dharmesh Shah are angel backers. Money signals aggressive product investment — João publicly stated 2026 is the company's "most R&D-intensive year ever" with unannounced internal breakthroughs pending.
- **CrewAI Discovery launched May 5, 2026:** Their biggest recent product release moves CrewAI *upstream* from build-time to planning-time. Discovery ingests a company's tickets, chats, and workflows and surfaces ranked, evidence-backed automation use cases drawn from patterns across billions of real agent runs. CEO's framing: *"The agent bottleneck is not building — it's knowing what and how to build it."* This is a strategic GTM shift, not just a feature drop.
- **PwC Agent OS (July 2025):** PwC selected CrewAI as the foundational orchestration layer of its global "Agent OS," following 700%+ accuracy improvements on internal code generation tasks. This is full-scale production deployment, not a pilot — and it is CrewAI's strongest enterprise credibility signal going into 2026.
- **Named to Enterprise Tech 30 for second consecutive year (March 2026):** Voted on by 98 investors across 85 firms managing $2.6T in assets, under the *Agent Development* sub-category of AI Infrastructure — a category that grew from 0% of ET30 in 2019 to 43% in 2026.
- **Token cost research, June 2026:** CrewAI published research stating that an estimated 60–80% of enterprise token spend goes to use cases that haven't proven business value — and explicitly named **Arize** (alongside Galileo and Datadog) as an observability prerequisite to solving this problem. This is the direct opening for our conversation.

---

## Competitive Landscape

- **LangGraph** is CrewAI's sharpest technical challenger — surpassing CrewAI in enterprise production adoption in Q4 2025 with ~34.5M monthly PyPI downloads vs. CrewAI's ~5M. Enterprise CTOs increasingly cite LangGraph's state persistence and debugging depth when comparing the two. CrewAI's counter: role-based simplicity, the AMP control plane, and a 2B-run behavioral dataset no framework competitor can replicate.
- **Microsoft Foundry** (GA at Build 2026) is the biggest distribution threat — Azure-bundled agent orchestration, governance, and observability offered natively to enterprises already committed to Azure. CrewAI's counter-moves are cloud-agnostic positioning, the PwC Agent OS deal, and IBM co-sell — but the 18–24 month window to win enterprise defaults before hyperscalers crowd out third-party decisions is closing.
- **Google ADK** and **OpenAI Agents SDK** are ecosystem-aligned plays (GCP and OpenAI shops respectively) that pull developer mindshare away from CrewAI at the framework level — particularly with teams that haven't yet committed to a model-agnostic strategy.
- **The market urgency signal CrewAI lives inside:** Gartner simultaneously projects 40% of enterprise apps will embed task-specific agents by end of 2026 *and* warns that 40%+ of agentic AI projects will be canceled by 2027 due to cost overruns, unclear ROI, and inadequate risk controls. CrewAI's entire AMP control plane is architected for the governance and accountability crisis this creates — and Arize sits directly in that same stack as the observability layer.

---

## Suggested Talking Points

- **"You named Arize in your own playbook."** CrewAI's June 2026 token cost research explicitly cites Arize as an observability prerequisite — *"you cannot manage what you cannot measure."* This isn't a cold outreach; the technical alignment between our platforms is something your own team already documented. I want to understand where that thinking is coming from internally and what you're doing about it today.
- **"Your 2B-run dataset is your moat — and it's also your monitoring challenge."** At that execution volume, the difference between a well-governed workflow and a runaway agent burning 10x the token budget is instrumentation. The enterprises in your customer base that are expanding 11x within 12 months are the same ones who will surface cost and reliability questions at renewal. Arize is designed to make those questions answerable before they become account risk.
- **"The cancellation cliff is real and it lands on your customers."** Gartner's projection that 40%+ of agentic AI projects will be canceled by 2027 due to cost and governance failures is a direct threat to CrewAI's expansion motion. Every enterprise customer you have that can't answer "what did our agents do, and was it worth it?" is a cancellation risk. Arize's LLM observability and evaluation layer is what makes that question answerable at runtime — not after the fact.
- **"PwC chose you for governance — observability is the next layer they'll ask about."** The PwC Agent OS deal specifically highlighted RBAC, audit trails, and MCP-based data access as selection criteria. Those are table-stakes governance controls. The next question enterprise security and finance leaders ask after "who approved this?" is "what did it actually do, and how much did it cost?" That's an observability question, and it's ours to solve together.
- **"You're in your most R&D-intensive year with unannounced breakthroughs pending."** I'm not here to pitch a product you don't need — I'm here to understand where the gaps in your current observability and evaluation story are, so we can figure out whether Arize fills something real. If there's a POC conversation worth having, I'd rather scope it around your actual production workflows than a demo environment.

---

## Discovery Questions

1. **"Your June 2026 token cost research explicitly called out observability as a prerequisite to managing agent ROI — and named Arize in that context. What's the conversation inside CrewAI right now about how you're instrumenting your own platform and advising your enterprise customers to do the same?"**

2. **"With 2 billion workflow executions behind you, you have more production agentic data than almost anyone. When a customer comes to you and says their agent costs spiked or a crew behaved unexpectedly — what does the current debugging and root-cause workflow actually look like for them?"**

3. **"You launched Discovery to move upstream into the planning layer, and the AMP control plane owns the execution layer — where does the evaluation and continuous improvement loop close today? How are your enterprise customers measuring whether the agents they deployed three months ago are still performing as designed?"**

4. **"The Gartner cancellation warning is about cost overruns and unclear business value — both of which are fundamentally observability problems. Which of your current enterprise customers are closest to that risk profile, and what are you doing at the platform layer to give them the evidence they need to keep exec buy-in?"**

5. **"You mentioned internal breakthroughs not yet public and flagged 2026 as your most R&D-intensive year. Without getting into anything confidential — are there capability areas in the roadmap where having a deeper observability and evaluation integration would change what you can promise enterprise customers around reliability, cost predictability, or compliance?"**

---

## Sources

- https://crewai.com/
- https://crewai.com/blog/crewai-discovery
- https://crewai.com/blog/how-to-optimize-token-spend-for-better-agentic-roi
- https://blog.crewai.com/lessons-from-2-billion-agentic-workflows/
- https://blog.crewai.com/pwc-choses-crewai/
- https://blog.crewai.com/crewai-building-the-agentic-future-together/
- https://blog.crewai.com/crewai-selected-for-the-enterprise-tech-30/
- https://www.businesswire.com/news/home/20251119857048/en/CrewAI-Strengthens-AI-Agent-Operations-Platform-With-New-Product-Global-Expansion-and-AI-Course-with-Andrew-Ng
- https://siliconangle.com/2024/10/22/agentic-ai-startup-crewai-closes-18m-funding-round/
- https://pitchbook.com/profiles/company/590845-78
- https://forgeglobal.com/crew-ai_ipo/
- https://tracxn.com/d/companies/crewai/__5sItJve5QhflF2dH7U1TN7h20PJauFNCVGN8ZUg5wrM
- https://www.getpanto.ai/blog/crewai-platform-statistics
- https://www.agentconference.com/speaker/Joe-Moura
- https://www.linkedin.com/posts/joaomdmoura_2025-was-a-defining-year-for-crewai-we-activity-7414398929120878592-bdzW
- https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
- https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
- https://devblogs.microsoft.com/foundry/agent-service-build2026/
- https://azure.microsoft.com/en-us/products/ai-foundry
- https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-agent-governance-framework-gap-20260403/
- https://www.appventurez.com/blog/langgraph-vs-crewai
- https://www.zenml.io/blog/langgraph-vs-crewai
- https://aws.amazon.com/blogs/machine-learning/build-agentic-systems-with-crewai-and-amazon-bedrock/
- https://events.snowflake.com/build/emea/agenda/speakers/3801783
- https://crewai.com/blog/the-state-of-agentic-ai-in-2026