# MEDEASY — HACKCBS 9.0 / MEKO TRACK A

## PPT content extraction and evidence audit

**Status:** Audit of the checked-out project and currently available Meko account. This is slide-ready content, not a completed presentation.  
**Evidence boundary:** Repository source/docs, Git state, a read-only database schema inspection, and the Meko tools/datapacks visible to this account. No app was launched, no tests were run, and no patient rows were queried. Existing user edits were left intact.

## Executive summary

MedEasy is a React/Vite and FastAPI prototype for prescription OCR, catalogue price comparison, pharmacy enquiry preparation, safety information, and an AI chat assistant called MedSaathi. Relevant code exists, but several product paths are prototype-level or disconnected. In particular, the application’s own Meko integration is not configured in the local backend environment, its privacy-consent UI does not update the in-memory consent state used by chat, and the visible memory panel is not wired to real recalled items or correction/deletion callbacks. The connected Codex Meko account is live, but it exposes only an empty personal default datapack; no shared team build datapack or promoted decisions were visible.

The strongest responsible deck is a transparent prototype demonstration, with the Meko portion presented as a build plan and a clearly labeled blocker until real app-level ON/OFF evidence is captured. Do not reuse the repository’s fictional Meko story, memory IDs, or claimed clinical outcome as evidence.

## Product and track framing

- **Product:** MedEasy; conversational assistant: MedSaathi.
- **Track:** HackCBS 9.0 HealthTech / Meko Track A, as stated in repository materials.
- **Team name and members:** Not evidenced in the repository. Insert only after the team confirms them.
- **Repository tagline:** “Empowering Bharat with Affordable Healthcare, Prescription Transparency, and Responsible AI Health Navigation.” This is branding, not a validated impact claim.
- **Suggested deck tagline:** “MedEasy — Make the next medication conversation easier to prepare.”
- **One-sentence product description:** “MedEasy helps a patient or caregiver turn a prescription into a reviewed medicine list, compare indicative catalogue prices, prepare a pharmacy enquiry, and ask a cautious AI assistant for help navigating the next step.”
- **Primary persona:** An illustrative adult patient or caregiver managing recurring medication. This is a working hypothesis, not a user-research finding.

## Evidence rules for the deck

Use the following labels on relevant slides or speaker notes:

- **Implemented in code:** A route/component/service exists. This does not mean it was exercised live.
- **Prototype:** Simulated, in-memory, seeded, or dependent on unverified data.
- **Unverified:** Requires credentials, a live run, or human confirmation.
- **Proposed:** A future workflow or target, not current functionality.
- **Measured:** Use only if a dated source artifact contains the measurement. No product outcome metrics were found in the audited repository.

Do not present screenshots or text from docs/MEKO_TRACK_A_SUBMISSION.md as live proof. It contains fictional demo details and claims that do not match the checked-out runtime.

## Slide 1 — Title

**Headline:** MedEasy  
**Exact slide copy:**

> Make the next medication conversation easier to prepare.  
> Prescription review · Indicative price comparison · Pharmacy enquiry preparation  
> HackCBS 9.0 · HealthTech · Meko Track A  
> Team: [confirm team name and members]

**Layout / visual:** Product name and one-line value proposition at left; a single genuine, scrubbed app screen at right. Use a small “working prototype” tag. Avoid “personal health memory” or “live Meko” claims on the title slide.

**Asset / screenshot:** Capture the actual current app after replacing the identifying sample prescription with synthetic, scrubbed content. No suitable capture screenshot was found in the repository. The tracked frontend/src/assets/sample-prescription.jpg contains identifying and clinical information; do not show it.

**Scoring relevance:** Clear problem framing and solution identity.

**Speaker notes:** “MedEasy is a prototype for helping patients and caregivers prepare for a medication conversation. We combine prescription review, indicative catalogue comparisons, pharmacy enquiry preparation, and a cautious assistant. Today I’ll be precise about what works in code, what is simulated, and what we still need to validate.”

**Text density:** Low.

## Slide 2 — The problem

**Headline:** A prescription starts a chain of decisions  
**Exact slide copy:**

> Patients and caregivers may need to:
> - Read a handwritten or photographed prescription.
> - Check that the medicine list is understood.
> - Compare available options and prices.
> - Contact a pharmacy to confirm availability.
> - Carry an accurate medication list between care settings.
>
> MedEasy is designed to make those steps easier to prepare. It does not diagnose or prescribe.

**Evidence note:** These are workflow hypotheses, not findings from MedEasy interviews. WHO describes medication reconciliation and an up-to-date medicine list as important during transitions of care, with a best possible history assembled from patient/family input and reliable sources. National Health Accounts 2021–22 report household out-of-pocket expenditure of 39.4% of total health expenditure; this is broad health spending context, not medicine-specific evidence or proof of MedEasy savings. [WHO](https://www.who.int/publications-detail-redirect/WHO-UHC-SDS-2019.9) · [MoHFW National Health Accounts 2021–22](https://www.mohfw.gov.in/sites/default/files/NHA%202021-22_up.pdf)

**Layout / visual:** A four-step patient journey with simple icons: understand → compare → ask → carry the reviewed list. Keep the slide free of market-size or savings statistics.

**Asset / screenshot:** Original diagram. No patient image is necessary.

**Scoring relevance:** Problem significance and user need.

**Speaker notes:** “Medication work does not end when a prescription is written. People still have to understand the list, ask about options, and confirm what a pharmacy can supply. WHO’s medication-reconciliation guidance supports the importance of an accurate list and patient participation. Our specific user pain points remain hypotheses; we have not yet completed interviews.”

**Text density:** Low.

## Slide 3 — Target user and validation

**Headline:** Start with the patient and caregiver workflow  
**Exact slide copy:**

> **Initial user hypothesis**  
> An adult patient or caregiver managing recurring medication who needs to review a prescription and prepare a pharmacy conversation.
>
> **What we know today**  
> The repository contains a working prototype and seeded datasets. It contains no interview notes, survey results, usability study, or pharmacist feedback.
>
> **Next validation**  
> Interview 8–10 patients/caregivers and 3 pharmacists or health workers. Observe five tasks: review an extracted list, compare a like-for-like option, prepare an availability enquiry, understand AI/privacy consent, and correct or remove saved context.

**Layout / visual:** Persona hypothesis on left; “known / to validate” evidence panel and next-study plan on right. Clearly mark the persona as a hypothesis.

**Asset / screenshot:** No identifiable user photo. A simple journey diagram is preferable.

**Scoring relevance:** User understanding, validation, and feasibility.

**Speaker notes:** “We have not yet earned the right to call this a validated persona. Our first study will include patients or caregivers managing recurring medication and a smaller group of pharmacy or health workers. We’ll observe task completion, where people hesitate, whether a comparison is truly comparable, and whether consent is understood. We will not retain participants’ real health details in the study notes.”

**Text density:** Medium.

## Slide 4 — The solution and feature status

**Headline:** One workflow to prepare, review, and ask  
**Exact slide copy:**

> **Upload → Review → Compare → Prepare enquiry → Ask for guidance**
>
> | Capability | Evidence status |
> |---|---|
> | Prescription image/PDF extraction | Implemented path; hosted Gemini call not exercised in this audit |
> | Human review and edit of extracted medicines | Implemented in Scan page |
> | Search confirmed medicines | Implemented against catalogue |
> | Indicative price comparison | Prototype dataset; provenance and pack-size comparability incomplete |
> | Cart | Session-only prototype; not an order |
> | Pharmacy directory | Seeded listings; call to confirm |
> | Pharmacy availability | Not live stock; enquiry must be sent and confirmed |
> | WhatsApp enquiry | Opens a prefilled user-controlled message; user sends it |
> | Pharmacy response | Simulated UI; no authenticated partner workflow |
> | CDSCO safety lookup | Dataset is review-only; current routes disagree on verification handling |
> | MedSaathi chat | Gemini-backed code path; live call not exercised |
> | Meko recall and memory | Code exists, but local backend has no Meko key/datapack configuration |
> | Memory review/correction/forget | Panel exists but is not connected to real items or callbacks |

**Layout / visual:** Five-step horizontal journey. Add short evidence labels under stages: “code path,” “seeded/prototype,” or “blocked pending Meko setup.” The status table can occupy the lower half or be split into a main workflow and three status callouts.

**Asset / screenshot:** Capture current scan/review and catalogue screens with synthetic data. Do not imply a pharmacy has stock or an enquiry was delivered.

**Scoring relevance:** Product quality, implementation, and honest demo scope.

**Speaker notes:** “The core interaction is upload, human review, catalogue lookup, and preparing a pharmacy enquiry. The catalogue is not a live quote, the directory does not establish stock, and WhatsApp requires the user to send the message. The pharmacy reply is simulated. CDSCO records need review before they can support a safety claim. The Meko memory UI is not yet a working user-visible loop.”

**Text density:** High; if necessary split the status table into slide notes while keeping the top five limitations visible.

## Slide 5 — Meko ON/OFF: current evidence and demo gate

**Headline:** Meko should add user-approved context; the app-level demo is not ready  
**Exact slide copy:**

> **OFF — verified design intent:** No recalled Meko context should be supplied to the assistant.  
> **ON — intended behavior:** With explicit consent, retrieve a relevant saved item, show its exact source text, allow correction or deletion, and pass it to the assistant as unverified context.  
>
> **Current app status:** Blocked. Backend Meko credentials/datapack are absent; the consent routes are disconnected; the memory panel has no live-item or correction/delete wiring.  
>
> **Demo rule:** Show ON/OFF only after a real synthetic memory is created, retrieved, visibly reviewed, corrected/deleted, and the OFF case is captured. Never substitute scripted output.

**Layout / visual:** Two-column OFF / ON states, with a red/amber “not yet evidenced in app” banner. Beneath the columns, show a compact checklist: backend connected, opt-in works, exact result visible, edit/delete works, OFF has no recall.

**Asset / screenshot:** Do not use the fictional Ramesh story or sample memory IDs from the submission notes. Capture actual runtime and tool results after the gate is completed; until then, use a clearly labeled wireframe or omit the screenshot.

**Scoring relevance:** Meko Track A adoption, privacy, and verifiable behavior.

**Speaker notes:** “Meko is a meaningful direction for user-controlled context, but the current local backend is not configured for it. The Meko connection available to this audit is a separate Codex connection and exposes an empty personal default datapack, not a MedEasy team build. We are not showing a fake ON/OFF result. Before this becomes a live demo, we need to connect the backend, align consent state, route data to the right user scope, and show the exact returned item with working correction and deletion.”

**Text density:** Medium.

## Slide 6 — Meko architecture and privacy

**Headline:** Separate identity, AI processing, and optional memory  
**Exact slide copy:**

> **Current code path**
> - React/Vite client → FastAPI API.
> - Prescription/pack image or PDF → hosted Gemini extraction.
> - Chat → hosted Gemini.
> - PostgreSQL-compatible YugabyteDB → account, profile metadata, consent, token hashes, and datapack-link records.
> - Meko MCP Streamable HTTP → optional conversation and memory calls, if configured and consented.
>
> **Privacy facts from the audited code**
> - No persistent local health vault was found.
> - If Meko consent is active, chat turns are logged as conversation messages; this is broader than saving only a user-approved fact.
> - The app currently uses a fixed datapack configuration rather than routing memory per patient.
> - The privacy screen’s “documents stay on this device” wording does not match the hosted Gemini upload path.
> - The delete endpoint queues a database status change; no completed remote Meko deletion was evidenced.

**Architecture diagram:**

> Patient device → MedEasy React app → FastAPI  
> FastAPI → Gemini (prescription extraction and chat)  
> FastAPI → YugabyteDB (identity/profile/consent/session metadata)  
> FastAPI → Meko MCP (optional conversation/memory; not configured in audited backend)  
> Pharmacy contact → user-controlled WhatsApp handoff; no stock/order confirmation

**Layout / visual:** Data-flow diagram with separate colored paths for identity metadata, document/chat processing, optional Meko, and user-controlled pharmacy contact. Mark hosted processors explicitly.

**Asset / screenshot:** Original diagram derived from code paths. Do not depict encryption, on-device storage, isolated per-patient Meko packs, or a verified delete unless implemented and verified.

**Scoring relevance:** Architecture, privacy, responsible AI, and data handling.

**Speaker notes:** “This slide describes the code we inspected, not a production deployment. The database schema contains identity, profile metadata, privacy consent, refresh-session hashes, and datapack-link metadata; it does not contain clinical record fields. Prescription images and chat are sent to hosted Gemini paths. Meko is optional in design, but the current backend configuration is absent. Before a live memory demo, consent must reach the same state the chat service reads, and the team must prove per-user isolation and remote deletion.”

**Text density:** Medium to high.

## Slide 7 — Build evidence and Meko proposal

**Headline:** A working prototype, with a concrete consent-aware Meko next step  
**Exact slide copy:**

> **Built in the repository**
> - React/Vite frontend and FastAPI backend.
> - Prescription extraction and human review flow.
> - Catalogue search, seeded pharmacy directory, safety-data paths, and MedSaathi chat.
> - Meko MCP client/service and consent/memory code paths.
>
> **Not evidenced as working live**
> - MedEasy backend connected to Meko.
> - Shared team build datapack, promoted decisions, or two-agent Check T.
> - Corrected/deleted memory shown in the app.
> - Live user outcomes, live pharmacy stock, or real pharmacy replies.
>
> **Proposed Meko feature: consent-aware memory lifecycle**  
> Attach explicit consent scope, source, capture time, and an expiry policy to a proposed memory; filter expired or disallowed items at recall; return a deletion status only after the remote operation is confirmed. This is a proposal, not a current capability.

**Grounding:** Meko documents describe isolated datapacks, conversation persistence, memory search/update/delete, and promotion into shared knowledge. The documented MCP surface accepts metadata, but the audited MedEasy flow does not provide a typed consent/retention enforcement loop. The feature proposal therefore adds lifecycle policy around existing storage/search operations; it does not claim Meko lacks metadata or deletion APIs. [Meko MCP reference](https://docs.mekodata.ai/reference/mcp-server/) · [Meko memory concepts](https://docs.mekodata.ai/architecture/core-concepts/memory/) · [Meko projects/datapacks](https://docs.mekodata.ai/architecture/core-concepts/projects/)

**Layout / visual:** Left: repository evidence with commit identifiers 3b157a5 and d1ae519; right: “now / next” lifecycle diagram for proposal. Do not call Git commits proof of deployment or successful Meko calls.

**Asset / screenshot:** Genuine repo screens and a clearly labeled proposal diagram. If Meko team pack artifacts are later shared, add dated screenshots/logs of the actual build and tool calls.

**Scoring relevance:** Technical execution, Meko adoption, and roadmap.

**Speaker notes:** “The repository contains the core prototype and a Meko client. That is implementation evidence, not proof of connected runtime behavior. A grounded next feature is a consent-aware lifecycle around memory capture and recall, with provenance, expiry, filtering, and a deletion receipt. This builds on documented Meko operations while addressing the product’s current gap between a consent toggle and the conversation data actually saved.”

**Text density:** Medium.

## Slide 8 — Impact, measures, and roadmap

**Headline:** Measure safer preparation before claiming impact  
**Exact slide copy:**

> **No product KPI or outcome is measured yet.**
>
> **First pilot measures**
> - ≥80% task completion in the first 10 target-user sessions.
> - Median ≤3 minutes from upload to reviewed medicine list.
> - 9/10 participants can explain what is sent to Gemini vs. optional Meko and how to opt in/out.
> - 100% of displayed memories trace to a real result; 0 cross-user recall in isolation checks.
> - Establish pharmacy enquiry response baseline with at least 10 opt-in pharmacies before setting a response-rate target.
> - Compare prices only where ingredient, strength, form, and pack size are verified as comparable.
>
> **Next:** Fix consent and user routing → remove sensitive sample asset → validate datasets and workflows → run a synthetic-data Meko ON/OFF demo → conduct patient/pharmacy pilot.

**Layout / visual:** Three-stage roadmap: readiness, controlled demo, pilot. Show all numeric values as “proposed targets,” not achieved outcomes.

**Asset / screenshot:** No impact chart until measurements exist. Use a roadmap graphic and label targets “proposed.”

**Scoring relevance:** Feasibility, measurable impact, and next steps.

**Speaker notes:** “We have no measured product outcomes yet, so these are proposed pilot thresholds. We will measure task completion and time, check whether consent is understood, verify every recalled item against a real Meko result, and test that users cannot retrieve each other’s context. Pharmacy response will first be measured as a baseline. We will not claim savings until the catalogue has comparable pack sizes and traceable sources.”

**Text density:** Medium.

## Five-minute rehearsal script

**0:00–0:30 — Opening (Slide 1)**  
“MedEasy is a prototype that helps a patient or caregiver prepare for the next medication conversation. It combines prescription review, indicative catalogue comparison, pharmacy enquiry preparation, and a cautious assistant.”

**0:30–1:05 — Need (Slide 2)**  
“After receiving a prescription, people may still need to understand the list, ask about options, and confirm availability. WHO guidance supports an accurate medication list and patient participation during transitions of care. Our local user problem is still a hypothesis; we have not completed interviews.”

**1:05–1:35 — User and validation (Slide 3)**  
“We start with adults managing recurring medicines and their caregivers. Our next study is eight to ten patients or caregivers and three pharmacy or health workers. We will observe five tasks and retain no real health details in study notes.”

**1:35–2:20 — Product walkthrough (Slide 4)**  
“The user uploads a prescription, reviews and edits extracted items, searches a seeded catalogue, and can prepare a pharmacy enquiry. Extraction and chat use hosted AI paths. Catalogue prices are indicative and lack complete pack-size provenance; directory listings require confirmation; WhatsApp is sent by the user; and the pharmacy response shown here is simulated. The safety dataset and route behavior need verification before safety claims.”

**2:20–3:10 — Meko (Slide 5)**  
“The intended Meko experience is OFF by default, then an explicit opt-in retrieves relevant context that the user can inspect, correct, or delete. I cannot demonstrate that as a live app feature today: the local backend lacks Meko configuration, consent is not wired through to the chat service, and the panel has no live result callbacks. We will not fake the ON state. A live demonstration requires a real synthetic memory, the exact returned result, and a working OFF case.”

**3:10–4:05 — Architecture and privacy (Slide 6)**  
“The client talks to FastAPI. Prescription files and chat go to hosted Gemini. YugabyteDB stores account and session metadata. The optional Meko path is not configured in this backend snapshot. There is no persistent local health vault in the code; the privacy copy needs correction. If Meko is enabled, the current logging path saves conversation turns, which is broader than a user-approved fact.”

**4:05–4:35 — Build and proposal (Slide 7)**  
“The codebase contains the core workflows and Meko service calls, but a code path is not a live integration. Our proposed Meko improvement is a consent-aware memory lifecycle: source and scope on capture, expiry-aware recall, and deletion status backed by a confirmed remote operation.”

**4:35–5:00 — Measures and close (Slide 8)**  
“We have not measured user outcomes. Our next step is to fix consent and per-user routing, replace the sensitive sample asset, verify the data, and run a synthetic ON/OFF demo. Then we’ll measure task completion, time, consent understanding, recall isolation, and pharmacy response. MedEasy aims to make the next medication conversation easier to prepare.”

**Rehearsal status:** Do not perform the Meko ON/OFF claim until the live evidence gate above is met. If the connection fails, state that the integration is not ready and continue with the architecture and roadmap slides.

## Compliance matrix — A1 to A5

| Criterion | Status | Evidence and gap |
|---|---|---|
| **A1 — Meko memory ON/OFF** | **Blocked / not demonstrated** | Backend .env has no MEKO_API_KEY, MEKO_DATAPACK_ID, or enable flags. Consent UI writes to the privacy route; chat reads a separate in-memory consent map. No live app result or reliable OFF/ON capture. |
| **A2 — Meko capability use** | **Partial code; runtime unverified** | Allowlisted calls include context search, conversation create/add, memory add/search/update/delete. App does not call promotion or document/knowledge workflows. Fixed datapack configuration is not per-patient routing. |
| **A3 — User story** | **Hypothesis only** | Recurring-medication patient/caregiver workflow is plausible and consistent with the prototype, but no interview or usability evidence is in the repository. |
| **A4 — Review/correct/delete** | **Not implemented end to end** | ContextPanel is rendered without recalled items or approve/forget callbacks. Privacy deletion marks a link as deleting but no remote Meko deletion is evidenced. |
| **A5 — Privacy, consent, isolation** | **Material gaps** | Default consent is false in code, but frontend and chat consent state diverge. Consent-active logging stores full turns. Fixed datapack is not patient-routed. No persistent local health vault; privacy copy says otherwise. |

## Evidence inventory and limits

### Repository and build

- Repository is on main, HEAD d1ae519 (“Improve prescription parsing and matching logic”); prior Meko submission material commit 3b157a5.
- Worktree already contained modifications in safety, main, auth test, frontend API/client, assistant service, auth context, TTS hook, and MedSaathi page. These were not edited during this audit.
- Frontend: React 19, Vite, TypeScript. Backend: FastAPI, SQLAlchemy async, PostgreSQL-compatible YugabyteDB configuration.
- Chat uses LangChain Google GenAI; prescription extraction has a direct Google GenAI provider path. Meko client uses MCP Streamable HTTP.
- backend/requirements.txt does not list the mcp package even though the client imports it dynamically. Resolve before claiming a reproducible connected setup.
- No deployment URL/configuration was found. No screenshot captures or validated build-in-public post URL were found.
- Tests exist, including Meko mock tests, but were not run. Mock tests do not prove live connectivity.

### Meko and user control

- The application requires an API key, datapack ID, enable flag, and demo-memory flag before its Meko service initializes.
- The checked-out backend environment lacks all Meko configuration keys; secret values were not printed.
- Current Codex Meko connection is a separate integration. The only visible datapack was an empty personal default datapack with no memories, knowledge, shared learnings, or files. No team build datapack or promoted decisions were visible.
- Meko docs describe datapack isolation, persisted conversations, memory search/update/delete, and promotion into shared knowledge. Those docs do not establish that this MedEasy app calls those features successfully.
- A temporary audit conversation created to inspect Meko was deleted after inspection.
- Existing submission notes are scenario prose, not telemetry. Their sample memory IDs and claimed antibiotic-family intervention are not in the application implementation.

### Privacy and data flow

- A read-only live database metadata query confirmed user, patient-profile metadata, privacy-consent, refresh-session, and Meko-datapack-link tables. No patient rows were queried.
- No clinical-record columns were found in those tables. This does not prove what third-party processors retain.
- No local persistent health vault or IndexedDB database was found. Cart and enquiry state use session storage; locale uses local storage.
- Prescription files are sent to a hosted Gemini extraction path. Chat uses hosted Gemini.
- Meko consent-active logging saves complete conversation turns; an explicit “remember” phrase may also trigger a memory addition.
- The frontend account consent action and chat’s in-memory consent state are not synchronized.
- Privacy deletion is represented as a queued database status. No remote deletion completion was observed.
- backend/app/db/base.py disables certificate verification for the Yugabyte SSL context; harden certificate validation before production use.

### Data and feature limitations

- Catalogue CSV has 508 data rows despite the “500 complete” naming. It lacks source URL/date and pack-size provenance; savings cannot be claimed as like-for-like.
- CDSCO extraction CSV has 260 records across June 2021–June 2025. Review statuses: 31 OCR/manual verification required, 174 extracted but verify before production, 55 source-PDF text extracted with manual review recommended; none marked official verified.
- Current safety routes disagree: one matching route can report a match without enforcing review status, while the batch checker only flags official-verified exact records. Another lookup maps the wrong status field and can fall through to no match. Do not say “clear” means safe.
- Pharmacy directory CSV has 30 seeded rows and asks users to call to confirm. It is not live stock. WhatsApp handoff is user-controlled; pharmacy response is simulated and not persisted as a verified partner reply.
- frontend/src/assets/sample-prescription.jpg is tracked and contains identifying and clinical information. Do not include it in slides or demos; replace it with scrubbed synthetic content and inspect its repository history before any public release.
- No interviews, surveys, user testing, measured savings, response rates, or clinical outcomes were found.

## Slide asset checklist

- [ ] Confirm team name and member names.
- [ ] Replace tracked sensitive sample prescription with fully synthetic, scrubbed fixture; inspect history/public exposure.
- [ ] Capture real app screens with synthetic content only.
- [ ] Capture live MedEasy-to-Meko ON/OFF only after the integration gate; record exact returned text and timestamps.
- [ ] Capture one corrected item and one confirmed remote deletion, with no real patient information.
- [ ] Label every price as indicative until comparable pack/source metadata is verified.
- [ ] Label pharmacy status as “call to confirm” and responses as simulated unless independently verified.
- [ ] Remove or rewrite privacy copy that says documents remain on device.
- [ ] Do not reuse fictional IDs, outcomes, or memory quotes from the submission script.

