# MEDEASY — Prioritized deck and product evidence gaps

**Purpose:** Close the highest-risk evidence and implementation gaps before presenting MedEasy at HackCBS 9.0 / Meko Track A. This report reflects the checked-out repository and Meko resources visible to the current account. It is not a production security or clinical review.

## Priority summary

| Priority | Gap | Why it matters |
|---|---|---|
| **Critical** | Sensitive prescription image is tracked in the repository | It contains identifying and clinical information and must not appear in a deck/demo or public release. |
| **Critical** | Meko app integration is unconfigured and ON/OFF is not demonstrable | No backend Meko key/datapack settings; current account’s Meko pack is empty and personal. |
| **Critical** | Consent state does not reach the chat service; deletion is only queued | The product cannot substantiate opt-in, user control, or completed deletion. |
| **Critical** | Fixed datapack configuration is not per-patient isolation | Potential cross-user exposure if multiple users share the configured datapack. |
| **High** | Context panel has no real recall/correct/delete wiring | A4 is not implemented end-to-end; no auditable patient-visible result. |
| **High** | CDSCO dataset is entirely review-only and routes conflict | A “no match” or “clear” result could be misunderstood as safety confirmation. |
| **High** | Chat and document data are sent to hosted providers; privacy copy says files stay local | User-facing disclosure does not match code paths. |
| **High** | Catalogue provenance/pack sizes are incomplete | Comparisons and savings cannot be defended as like-for-like. |
| **High** | No user/problem validation or product outcome metrics | Persona, impact, and traction claims remain hypotheses. |
| **Medium** | Pharmacy directory and replies are seeded/simulated | Availability, response rate, and partner claims are not supported. |
| **Medium** | Meko dependency absent from requirements; DB TLS certificate checks disabled | Reproducibility and transport trust need hardening before a connected demo/production claim. |
| **Medium** | Shared team Meko build evidence is not available to this account | Cannot claim datapack build, promoted memories, or two-agent Check T without artifacts. |

## Detailed gaps and actions

### 1. Remove and replace the sensitive sample prescription

- **Priority:** Critical
- **Evidence:** frontend/src/assets/sample-prescription.jpg is tracked and includes identifying and clinical information.
- **Why it matters:** Screenshots, demos, repository access, or a public fork can expose sensitive information.
- **Action:** Replace with a fully synthetic, clearly labeled fixture. Inspect repository history and any shared copies; if the image was ever public, follow the repository owner’s incident/removal process.
- **Evidence to capture:** Scrubbed replacement asset, clean screenshot, and documented history review.
- **Owner:** Frontend owner + security/privacy owner.

### 2. Configure and prove MedEasy’s own Meko connection

- **Priority:** Critical
- **Evidence:** Backend configuration requires MEKO_API_KEY, MEKO_DATAPACK_ID, enable, and demo-memory settings. The ignored local backend environment has none of these keys. The Codex Meko connection is separate from the application. Only an empty personal default datapack was visible; no team build pack was visible.
- **Why it matters:** Meko code in the repository does not prove that the app connects to Meko.
- **Action:** Provision a dedicated synthetic-data demo datapack, configure the backend through the approved secret store, ensure the MCP package is installed, and run an end-to-end create/search/recall test from the application.
- **Evidence to capture:** Dated backend startup showing connected state without printing the key; exact MCP tool result; synthetic memory ID and text; ON and OFF app screenshots; shared datapack ownership/access evidence if Track A requires it.
- **Owner:** Backend/Meko owner.

### 3. Make consent one authoritative state and verify opt-in/out

- **Priority:** Critical
- **Evidence:** The frontend updates /api/privacy/consent/meko-memory; chat reads the Meko service’s in-memory consent map. A separate /api/memory/consent path changes that map, but the frontend does not use it.
- **Why it matters:** A UI choice may not change the behavior it purports to control.
- **Action:** Use one authoritative, user-scoped consent source for the UI, chat, and background logging; make opt-out take effect immediately and across sessions. Decide explicitly whether conversation logging is allowed or only approved facts are saved.
- **Evidence to capture:** Automated/manual trace showing OFF causes zero Meko calls and zero stored messages; ON shows the exact disclosed data; opt-out stops further calls; persisted choice survives session changes.
- **Owner:** Backend owner + frontend owner + privacy owner.

### 4. Enforce per-user datapack isolation

- **Priority:** Critical
- **Evidence:** Meko service config uses a fixed datapack ID; patient ID is used for an in-memory consent key and not datapack routing. Auth service helpers for linking a user datapack are not used in Meko orchestration.
- **Why it matters:** A shared fixed datapack can expose one user’s context to another.
- **Action:** Resolve an authorized datapack from the authenticated user’s mapping for every operation; deny access if no mapping exists; avoid trusting a client-supplied patient ID. Test with two synthetic users.
- **Evidence to capture:** Two-user isolation test with distinct synthetic memories; logs showing resolved user scope without secrets; zero cross-user recall.
- **Owner:** Backend/Meko owner.

### 5. Complete the user-visible memory review and deletion loop

- **Priority:** High
- **Evidence:** ContextPanel is rendered without recalled items or approve/forget callbacks. Privacy deletion updates database link state to deleting; no actual remote Meko delete call or completion receipt was observed.
- **Why it matters:** The product claims user control without presenting what was retrieved or proving that deletion finished.
- **Action:** Display exact returned text and source; support correction and forget from the same user scope; call the remote delete operation; distinguish requested, in-progress, completed, and failed states. Do not report completion until confirmed.
- **Evidence to capture:** Actual recalled item; correction reflected in subsequent recall; confirmed remote deletion and subsequent absence; app screenshots for each state.
- **Owner:** Frontend owner + backend/Meko owner.

### 6. Correct privacy disclosures and data-flow behavior

- **Priority:** High
- **Evidence:** Prescription/pack files go to hosted Gemini; chat goes to hosted Gemini. With Meko consent active, full conversation turns are logged. No persistent local health vault was found, though privacy copy says original files and detailed history stay on the device.
- **Why it matters:** People need accurate, understandable disclosure before sending health-related information.
- **Action:** Align privacy text with actual processors, retention, and data categories. Minimize content sent to Meko; store only the chosen content if that is the product promise. Add provider retention/deletion facts only after verifying provider terms and configuration.
- **Evidence to capture:** Reviewed data-flow inventory, updated UI copy, consent comprehension results, and provider configuration evidence.
- **Owner:** Privacy owner + backend owner + product lead.

### 7. Fix CDSCO verification semantics before showing safety results

- **Priority:** High
- **Evidence:** All 260 extracted records have manual-review statuses; none is marked official verified. The batch checker only flags official-verified exact records, while the standalone verification route can match without enforcing review status. Another route reads the wrong status field and can return no match. Safety route file already has uncommitted user edits; do not overwrite those changes.
- **Why it matters:** “No match” or “clear” could be mistaken for “safe,” and extraction records are not verified alerts.
- **Action:** Reconcile route behavior, use one explicit status model, never map missing/unverified data to “safe,” and manually verify source records against authoritative CDSCO notices before production claims.
- **Evidence to capture:** Reviewed source-to-record audit trail; route tests covering verified, unverified, no-match, and error cases; UI wording review.
- **Owner:** Safety-data owner + backend owner + clinical reviewer.

### 8. Establish catalogue provenance and comparable pricing

- **Priority:** High
- **Evidence:** Catalogue has 508 rows but no source URL/date or pack-size provenance. README’s “500 complete” label is imprecise. The price comparison cannot establish equivalent quantity/formulation across rows.
- **Why it matters:** A displayed difference could compare unlike products or stale prices.
- **Action:** Add source, retrieval date, pack size, strength, dosage form, and match rationale; define matching rules; show “indicative” until verified. Avoid total savings claims.
- **Evidence to capture:** Data dictionary, source links/dates, reviewed comparable pairs, and reproducible calculation.
- **Owner:** Data owner + product owner.

### 9. Validate the user problem and workflow

- **Priority:** High
- **Evidence:** No interview, survey, usability test, or pharmacist feedback artifacts were found.
- **Why it matters:** The persona and pain points are hypotheses, and the team cannot claim validated demand.
- **Action:** Conduct 8–10 patient/caregiver sessions and 3 pharmacist/health-worker sessions; observe five tasks; record task outcomes and friction without retaining identifiable health details.
- **Evidence to capture:** Consent process, anonymized notes, task completion/time results, themes, and changes made in response.
- **Owner:** Validation lead.

### 10. Measure product impact without overstating it

- **Priority:** High
- **Evidence:** No measured product KPIs, savings, pharmacy response rates, or clinical outcomes were found.
- **Why it matters:** Impact claims and traction must be defensible.
- **Action:** Start with proposed measures: first-task completion, time to reviewed list, consent comprehension, correct user-scoped recall, pharmacy response baseline, and comparable-price coverage. Treat numeric thresholds as targets only.
- **Evidence to capture:** Dated pilot protocol, raw anonymized observations, metric definitions, and results.
- **Owner:** Product lead + validation lead.

### 11. Label pharmacy workflow as a prototype

- **Priority:** Medium
- **Evidence:** Directory seed has 30 rows marked “call to confirm” or equivalent; no live stock evidence. WhatsApp is a user-controlled prefilled handoff. Pharmacy replies are simulated and not persisted as verified responses. One directory parsing path may infer WhatsApp availability from the presence of a phone number.
- **Why it matters:** A listing or simulated reply must not be represented as confirmed stock or a real partner interaction.
- **Action:** Keep “call to confirm” visible, remove unsupported WhatsApp availability inference, and label simulated responses. Add authenticated partner confirmation and durable enquiry state before reporting response metrics.
- **Evidence to capture:** Live partner opt-ins, timestamped stock confirmations, sent enquiry records, and actual response status.
- **Owner:** Pharmacy integration owner.

### 12. Make the connected setup reproducible and secure

- **Priority:** Medium
- **Evidence:** backend/requirements.txt does not declare the MCP client dependency used dynamically; database TLS setup disables certificate verification.
- **Why it matters:** A fresh setup may fail to connect, and disabled verification weakens transport identity checks.
- **Action:** Declare and pin the supported MCP client dependency; test clean setup in a controlled environment; configure trusted certificate validation for Yugabyte.
- **Evidence to capture:** Reproducible setup log, dependency lock, successful startup/health check, and validated TLS configuration.
- **Owner:** Backend/platform owner.

### 13. Obtain the shared team build and Track A evidence

- **Priority:** Medium
- **Evidence:** The connected Meko account exposed one empty personal default datapack, with no shared team pack, promoted decisions, or Check T artifacts. Repository script claims are not runtime evidence.
- **Why it matters:** Track-specific collaboration claims need artifacts tied to the actual shared build.
- **Action:** Ask the teammate/team workspace owner to share the build datapack or provide timestamped screenshots/tool logs and the exact challenge rubric. Keep account-level Codex Meko distinct from MedEasy backend credentials.
- **Evidence to capture:** Shared datapack identifier and access, conversation/tool logs, promoted decision records, two-agent Check T result, and timestamps.
- **Owner:** Meko track lead.

## Demo readiness gate

Do not present Meko as a live app feature until all are true:

1. MedEasy backend connects to a dedicated synthetic-data Meko datapack.
2. OFF produces no recall, logging, or memory write.
3. ON requires explicit consent and shows the exact retrieved text and provenance.
4. User correction changes future recall.
5. Remote deletion is confirmed and the item is absent on later search.
6. Two synthetic users cannot retrieve each other’s context.
7. Screenshots and logs contain no real patient information or secrets.

## Deck language to use now

- “Implemented code path” for source-level functionality not exercised live.
- “Prototype” for seeded data, temporary state, simulated replies, and unverified integrations.
- “Indicative price” until comparable product and pack provenance is complete.
- “Call to confirm” for seeded pharmacy listings.
- “Proposed target” for all numeric pilot thresholds.
- “Meko integration not yet demonstrated in the MedEasy app” until the readiness gate passes.

## Do not claim yet

- Proven medicine savings or “50–90% savings” from this catalogue.
- Live pharmacy inventory, completed pharmacy response, or an order.
- “Safe” based on no CDSCO match.
- A live Meko ON/OFF flow, shared team datapack, promoted decision, or two-agent Check T.
- Per-patient memory isolation, completed remote deletion, or local encrypted health storage.
- User validation, clinical outcome, traction, or impact metrics.
- The scripted antibiotic-family intervention or fictional memory IDs in the submission notes.
