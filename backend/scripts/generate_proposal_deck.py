import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# Color Palette
COLOR_BG = RGBColor(11, 15, 25)          # Deep Midnight Slate (#0B0F19)
COLOR_CARD = RGBColor(19, 24, 41)        # Dark Card Container (#131829)
COLOR_CARD_BORDER = RGBColor(39, 47, 74) # Subtle Card Border (#272F4A)
COLOR_CODE_BG = RGBColor(13, 16, 28)     # Code Background (#0D101C)
COLOR_WHITE = RGBColor(255, 255, 255)    # White
COLOR_SLATE_100 = RGBColor(241, 245, 249)# Slate 100
COLOR_SLATE_300 = RGBColor(203, 213, 225)# Slate 300
COLOR_SLATE_400 = RGBColor(148, 163, 184)# Slate 400
COLOR_SLATE_500 = RGBColor(100, 116, 139)# Slate 500
COLOR_PURPLE = RGBColor(139, 92, 246)    # Meko Violet (#8B5CF6)
COLOR_CYAN = RGBColor(20, 184, 166)      # Cyan / Teal (#14B8A6)
COLOR_ROSE = RGBColor(244, 63, 94)       # Coral / Rose (#F43F5E)
COLOR_AMBER = RGBColor(245, 158, 11)     # Amber (#F59E0B)

FONT_HEADING = "Segoe UI"
FONT_BODY = "Segoe UI"
FONT_CODE = "Consolas"

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG
        bg.line.fill.background()
        return bg

    def add_header(slide, tag_text, title_text, subtitle_text):
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.15))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        # Tag / Pill line
        p_tag = tf.paragraphs[0]
        p_tag.text = tag_text.upper()
        p_tag.font.name = FONT_HEADING
        p_tag.font.size = Pt(10)
        p_tag.font.bold = True
        p_tag.font.color.rgb = COLOR_PURPLE

        # Title line
        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.name = FONT_HEADING
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_WHITE
        p_title.space_before = Pt(3)

        # Subtitle line
        p_sub = tf.add_paragraph()
        p_sub.text = subtitle_text
        p_sub.font.name = FONT_BODY
        p_sub.font.size = Pt(12)
        p_sub.font.color.rgb = COLOR_SLATE_400
        p_sub.space_before = Pt(2)

    def add_card(slide, left, top, width, height, border_color=COLOR_CARD_BORDER, bg_color=COLOR_CARD):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)
        return card

    # =========================================================================
    # SLIDE 1: The Friction & The Solution (Points 1 & 2)
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1)
    add_header(
        slide1,
        "HackCBS 9.0 · Meko Feature Proposal · Deliverable (1/3)",
        "Meko Regulatory Memory Envelopes (RME)",
        "1. The Friction We Hit While Building  &  2. The Feature Defined in Meko's Own Terms"
    )

    # Left Column: The Friction & Workaround (Point 1)
    add_card(slide1, Inches(0.8), Inches(1.65), Inches(5.65), Inches(5.35), border_color=COLOR_ROSE)
    tb1_left = slide1.shapes.add_textbox(Inches(1.05), Inches(1.85), Inches(5.15), Inches(4.95))
    tf1_l = tb1_left.text_frame
    tf1_l.word_wrap = True
    tf1_l.margin_left = tf1_l.margin_top = tf1_l.margin_right = tf1_l.margin_bottom = 0

    p = tf1_l.paragraphs[0]
    p.text = "1. THE FRICTION (WHAT BROKE IN HEALTHCARE)"
    p.font.name = FONT_HEADING
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_ROSE

    items_fric = [
        ("Monolithic & Flat Permanence: ", "Meko currently treats all memories as permanent, static facts. In clinical navigation, an acute symptom ('fever 101°F on Oct 31') becomes toxic and clinically misleading 6 months later, whereas a Penicillin allergy must persist permanently."),
        ("Provenance Asymmetry: ", "Meko provides no native distinction between an unverified patient self-report, a physician-signed lab record, or an agent-inferred preference. The LLM treats hearsay as clinical truth."),
        ("Unverifiable Deletion (DPDP / HIPAA): ", "Regulated applications require cryptographic proof of vector memory deletion to comply with the Indian DPDP Act and HIPAA 'Right to be Forgotten'."),
        ("Our Ugly Client Workaround: ", "We had to write fragile regex filters (HEALTH_KEYWORDS_PATTERN), manual timestamp slicing, and ad-hoc client-side metadata wrappers in Python before calling Meko MCP.")
    ]

    for title, desc in items_fric:
        p = tf1_l.add_paragraph()
        p.space_before = Pt(8)
        run1 = p.add_run()
        run1.text = "• " + title
        run1.font.name = FONT_HEADING
        run1.font.bold = True
        run1.font.size = Pt(10.5)
        run1.font.color.rgb = COLOR_SLATE_100

        run2 = p.add_run()
        run2.text = desc
        run2.font.name = FONT_BODY
        run2.font.size = Pt(10)
        run2.font.color.rgb = COLOR_SLATE_400

    # Right Column: The Feature in Meko's Terms (Point 2)
    add_card(slide1, Inches(6.85), Inches(1.65), Inches(5.65), Inches(5.35), border_color=COLOR_PURPLE)
    tb1_right = slide1.shapes.add_textbox(Inches(7.1), Inches(1.85), Inches(5.15), Inches(4.95))
    tf1_r = tb1_right.text_frame
    tf1_r.word_wrap = True
    tf1_r.margin_left = tf1_r.margin_top = tf1_r.margin_right = tf1_r.margin_bottom = 0

    p = tf1_r.paragraphs[0]
    p.text = "2. THE FEATURE IN MEKO'S TERMS (RME ENVELOPE)"
    p.font.name = FONT_HEADING
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_PURPLE

    items_feat = [
        ("Datapacks with Envelopes: ", "Memories stored inside Datapacks carry a first-class lifecycle envelope containing temporal decay rules, provenance tiering, and tombstone deletion receipts."),
        ("Native Temporal TTL & Decay: ", "Three lifecycle policies:\n   - permanent: Chronic conditions & allergies (never expire).\n   - transient_acute: Exponential decay over N days (e.g., ttl_days: 14 for fevers/colds).\n   - session_ephemeral: Automatically purged on consultation discharge."),
        ("Clinical Provenance Tiers: ", "Every memory explicitly carries a verified trust level: patient_reported, clinician_verified, or inferred_preference for LLM prompt grounding."),
        ("Promotion & Scoped Sharing: ", "Datapack promotion rules: only clinician_verified or patient-promoted memories can transition from local session scopes to shared clinical datapacks.")
    ]

    for title, desc in items_feat:
        p = tf1_r.add_paragraph()
        p.space_before = Pt(8)
        run1 = p.add_run()
        run1.text = "• " + title
        run1.font.name = FONT_HEADING
        run1.font.bold = True
        run1.font.size = Pt(10.5)
        run1.font.color.rgb = COLOR_CYAN

        run2 = p.add_run()
        run2.text = desc
        run2.font.name = FONT_BODY
        run2.font.size = Pt(10)
        run2.font.color.rgb = COLOR_SLATE_400

    # =========================================================================
    # SLIDE 2: The Interface & Before/After Scenario (Points 3 & 4)
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2)
    add_header(
        slide2,
        "HackCBS 9.0 · Meko Feature Proposal · Deliverable (2/3)",
        "The Interface & Real-World Clinical Scenario",
        "3. New MCP Tool Parameters & Call Contract  &  4. Patient Scenario Before vs. After"
    )

    # Left Column: MCP Interface & Contract (Point 3)
    add_card(slide2, Inches(0.8), Inches(1.65), Inches(5.65), Inches(5.35), border_color=COLOR_CYAN)
    tb2_left = slide2.shapes.add_textbox(Inches(1.05), Inches(1.85), Inches(5.15), Inches(4.95))
    tf2_l = tb2_left.text_frame
    tf2_l.word_wrap = True
    tf2_l.margin_left = tf2_l.margin_top = tf2_l.margin_right = tf2_l.margin_bottom = 0

    p = tf2_l.paragraphs[0]
    p.text = "3. THE INTERFACE (MCP TOOL SCHEMA)"
    p.font.name = FONT_HEADING
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_CYAN

    p = tf2_l.add_paragraph()
    p.text = "MCP memory_create with Envelope:"
    p.font.name = FONT_CODE
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.space_before = Pt(4)

    code1 = (
        '{\n'
        '  "datapack_id": "dp-patient-ramesh-77",\n'
        '  "text": "Severe Penicillin allergy (anaphylaxis)",\n'
        '  "envelope": {\n'
        '    "ttl_days": null,\n'
        '    "decay_policy": "permanent",\n'
        '    "provenance_tier": "patient_reported",\n'
        '    "clinical_category": "allergy_intolerance"\n'
        '  }\n'
        '}'
    )
    p_c1 = tf2_l.add_paragraph()
    p_c1.text = code1
    p_c1.font.name = FONT_CODE
    p_c1.font.size = Pt(8.5)
    p_c1.font.color.rgb = COLOR_CYAN
    p_c1.space_before = Pt(2)

    p = tf2_l.add_paragraph()
    p.text = "MCP memory_delete Response (Tombstone Receipt):"
    p.font.name = FONT_CODE
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.space_before = Pt(8)

    code2 = (
        '{\n'
        '  "status": "purged",\n'
        '  "memory_id": "mem-allergy-402",\n'
        '  "purged_at": "2026-11-01T08:30:00Z",\n'
        '  "tombstone_receipt": {\n'
        '    "algorithm": "Ed25519",\n'
        '    "hash": "e3b0c44298fc1c149afbf4c8996fb9242...",\n'
        '    "signature": "30450221008f...c9e12"\n'
        '  }\n'
        '}'
    )
    p_c2 = tf2_l.add_paragraph()
    p_c2.text = code2
    p_c2.font.name = FONT_CODE
    p_c2.font.size = Pt(8.5)
    p_c2.font.color.rgb = COLOR_PURPLE
    p_c2.space_before = Pt(2)

    # Right Column: Scenario Before vs. After (Point 4)
    add_card(slide2, Inches(6.85), Inches(1.65), Inches(5.65), Inches(5.35), border_color=COLOR_AMBER)
    tb2_right = slide2.shapes.add_textbox(Inches(7.1), Inches(1.85), Inches(5.15), Inches(4.95))
    tf2_r = tb2_right.text_frame
    tf2_r.word_wrap = True
    tf2_r.margin_left = tf2_r.margin_top = tf2_r.margin_right = tf2_r.margin_bottom = 0

    p = tf2_r.paragraphs[0]
    p.text = "4. PATIENT SCENARIO: BEFORE VS. AFTER"
    p.font.name = FONT_HEADING
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_AMBER

    p_scen = tf2_r.add_paragraph()
    p_scen.text = "Context: 62-year-old Ramesh reports acute fever in Oct, and has a Penicillin allergy. In April (6 months later), he returns for health advice."
    p_scen.font.name = FONT_BODY
    p_scen.font.size = Pt(9.5)
    p_scen.font.color.rgb = COLOR_SLATE_300
    p_scen.space_before = Pt(4)

    # BEFORE BOX
    p = tf2_r.add_paragraph()
    p.space_before = Pt(8)
    r = p.add_run()
    r.text = "❌ BEFORE (CURRENT STATE - HALLUCINATION TRAP)"
    r.font.name = FONT_HEADING
    r.font.bold = True
    r.font.size = Pt(10.5)
    r.font.color.rgb = COLOR_ROSE

    items_before = [
        ("Stale Recall: ", "Meko retrieves 6-month-old acute fever along with the allergy."),
        ("Diagnostic Distortion: ", "LLM flags 'chronic unexplained fever lasting 6 months' and triggers unnecessary autoimmune/oncology panics."),
        ("Audit Exposure: ", "If Ramesh requests data deletion, app cannot mathematically prove vectors were purged.")
    ]
    for k, v in items_before:
        p = tf2_r.add_paragraph()
        p.space_before = Pt(2)
        r1 = p.add_run()
        r1.text = "  • " + k
        r1.font.bold = True
        r1.font.size = Pt(9)
        r1.font.color.rgb = COLOR_SLATE_100
        r2 = p.add_run()
        r2.text = v
        r2.font.size = Pt(9)
        r2.font.color.rgb = COLOR_SLATE_400

    # AFTER BOX
    p = tf2_r.add_paragraph()
    p.space_before = Pt(8)
    r = p.add_run()
    r.text = "✅ AFTER (WITH MEKO REGULATORY ENVELOPES)"
    r.font.name = FONT_HEADING
    r.font.bold = True
    r.font.size = Pt(10.5)
    r.font.color.rgb = COLOR_CYAN

    items_after = [
        ("Auto-Decay: ", "Acute fever auto-expires after 14 days (TTL=14) and is silenced."),
        ("Permanent Preservation: ", "Penicillin allergy (TTL=permanent) remains active, successfully intercepting Amoxicillin."),
        ("Compliance Receipt: ", "Ramesh purges his datapack and receives an Ed25519 cryptographic tombstone receipt.")
    ]
    for k, v in items_after:
        p = tf2_r.add_paragraph()
        p.space_before = Pt(2)
        r1 = p.add_run()
        r1.text = "  • " + k
        r1.font.bold = True
        r1.font.size = Pt(9)
        r1.font.color.rgb = COLOR_SLATE_100
        r2 = p.add_run()
        r2.text = v
        r2.font.size = Pt(9)
        r2.font.color.rgb = COLOR_SLATE_400

    # =========================================================================
    # SLIDE 3: Why It's New & Risk Mitigation (Points 5 & 6)
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3)
    add_header(
        slide3,
        "HackCBS 9.0 · Meko Feature Proposal · Deliverable (3/3)",
        "Why It's New & Enterprise Risk Mitigation",
        "5. What No Context Layer Does Today  &  6. Managing Privacy, Compute & Abuse Risks"
    )

    # Left Column: Why It's New / Strategic Moat (Point 5)
    add_card(slide3, Inches(0.8), Inches(1.65), Inches(5.65), Inches(5.35), border_color=COLOR_PURPLE)
    tb3_left = slide3.shapes.add_textbox(Inches(1.05), Inches(1.85), Inches(5.15), Inches(4.95))
    tf3_l = tb3_left.text_frame
    tf3_l.word_wrap = True
    tf3_l.margin_left = tf3_l.margin_top = tf3_l.margin_right = tf3_l.margin_bottom = 0

    p = tf3_l.paragraphs[0]
    p.text = "5. WHY IT'S NEW (THE REGULATED MOAT)"
    p.font.name = FONT_HEADING
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_PURPLE

    items_new = [
        ("Flat vs. Temporal Context: ", "Competitors (Mem0, Zep, LangChain, OpenAI Memory) treat memories as static text embeddings. None offer native mathematical half-life decay curves."),
        ("The Regulated Enterprise Gap: ", "General-purpose memory layers assume chat context is consumer trivialities (e.g., 'user likes pizza'). They fail in high-stakes domains where remembering stale facts causes medical errors or financial liabilities."),
        ("Auditable Right to be Forgotten: ", "No context provider issues signed cryptographic receipts proving vector deletion. Meko RME transforms agent memory into an enterprise compliance standard."),
        ("Zero Client Wrapper Overhead: ", "Developers no longer need to write fragile timestamp parsers, custom cron jobs, or database layers to enforce memory freshness.")
    ]

    for title, desc in items_new:
        p = tf3_l.add_paragraph()
        p.space_before = Pt(8)
        run1 = p.add_run()
        run1.text = "• " + title
        run1.font.name = FONT_HEADING
        run1.font.bold = True
        run1.font.size = Pt(10.5)
        run1.font.color.rgb = COLOR_CYAN

        run2 = p.add_run()
        run2.text = desc
        run2.font.name = FONT_BODY
        run2.font.size = Pt(10)
        run2.font.color.rgb = COLOR_SLATE_400

    # Right Column: Risk Analysis & Mitigation (Point 6)
    add_card(slide3, Inches(6.85), Inches(1.65), Inches(5.65), Inches(5.35), border_color=COLOR_ROSE)
    tb3_right = slide3.shapes.add_textbox(Inches(7.1), Inches(1.85), Inches(5.15), Inches(4.95))
    tf3_r = tb3_right.text_frame
    tf3_r.word_wrap = True
    tf3_r.margin_left = tf3_r.margin_top = tf3_r.margin_right = tf3_r.margin_bottom = 0

    p = tf3_r.paragraphs[0]
    p.text = "6. RISKS & CONCRETE MITIGATIONS"
    p.font.name = FONT_HEADING
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_ROSE

    items_risk = [
        ("Compute & Cost Risk (Background Sweepers): ", "Continuous cron-sweeping millions of expiring vector embeddings would cause severe CPU spikes.\n-> Mitigation: Lazy Query-Time Evaluation. Decay weights are calculated dynamically during cosine similarity scoring; expired items are pruned opportunistically."),
        ("Privilege Escalation & Provenance Spoofing: ", "Malicious actors or prompt injections could falsely mark an unverified fact as clinician_verified.\n-> Mitigation: Cryptographic Key Signing. Client agents can only write patient_reported. Elevated provenance requires authorized private key signatures."),
        ("Envelope Metadata Privacy Leakage: ", "Exposing category or diagnosis in unencrypted envelope fields could leak sensitive PHI.\n-> Mitigation: Envelopes are AES-256 encrypted within the patient Datapack partition and only decrypted inside secure enclaves during recall.")
    ]

    for title, desc in items_risk:
        p = tf3_r.add_paragraph()
        p.space_before = Pt(8)
        run1 = p.add_run()
        run1.text = "• " + title
        run1.font.name = FONT_HEADING
        run1.font.bold = True
        run1.font.size = Pt(10)
        run1.font.color.rgb = COLOR_AMBER

        run2 = p.add_run()
        run2.text = desc
        run2.font.name = FONT_BODY
        run2.font.size = Pt(9.5)
        run2.font.color.rgb = COLOR_SLATE_400

    # Output path
    output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "MEKO_FEATURE_PROPOSAL_3_SLIDES.pptx"))
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    create_presentation()

