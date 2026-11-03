"""
MedEasy Presentation Slide Generator
HackCBS 9.0 — Open Innovation & YugabyteDB Track (Theme: HealthTech)
Team: axioms (Yashraj Rastogi - Team Lead, Amarpit Srivastav - Member)
Generates 8 high-resolution (1920x1080, 16:9 widescreen) slide images matching MedEasy MVP UI.
"""

import os
import subprocess
import sys
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent.resolve()
SLIDES_DIR = BASE_DIR / "docs" / "slides"
SLIDES_DIR.mkdir(parents=True, exist_ok=True)

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(CHROME_PATH):
    CHROME_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# Common Header & Footer HTML Component
def get_chrome_decorations(slide_num, total_slides=8, title_badge="HackCBS 9.0 · Open Innovation & YugabyteDB Track"):
    return f"""
    <!-- Top Bar -->
    <header style="height: 64px; display: flex; align-items: center; justify-content: space-between; padding: 0 48px; border-bottom: 1px solid #E2E8F0; background: #FFFFFF; flex-shrink: 0;">
      <div style="display: flex; align-items: center; gap: 14px;">
        <div style="width: 38px; height: 38px; border-radius: 10px; background: linear-gradient(135deg, #087BFF 0%, #0052CC 100%); display: flex; align-items: center; justify-content: center; box-shadow: 0 3px 10px rgba(8, 123, 255, 0.3);">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="m10.5 20.5 10-10a4.95 4.95 0 1 0-7-7l-10 10a4.95 4.95 0 1 0 7 7Z"/>
            <path d="m8.5 8.5 7 7"/>
          </svg>
        </div>
        <div style="display: flex; align-items: baseline; gap: 8px;">
          <span style="font-size: 24px; font-weight: 800; color: #102653; letter-spacing: -0.5px;">MedEasy</span>
          <span style="font-size: 13px; font-weight: 600; color: #087BFF; background: #EAF4FF; padding: 2px 10px; border-radius: 999px;">HealthTech for Bharat</span>
        </div>
      </div>
      <div style="display: flex; align-items: center; gap: 16px;">
        <span style="font-size: 13px; font-weight: 700; color: #102653; background: #F1F5F9; border: 1px solid #CBD5E1; padding: 4px 14px; border-radius: 999px;">
          {title_badge}
        </span>
        <span style="font-size: 13px; font-weight: 700; color: #087BFF; background: #EAF4FF; border: 1px solid #BFDBFE; padding: 4px 14px; border-radius: 999px;">
          Team axioms
        </span>
        <div style="font-size: 14px; font-weight: 700; color: #475569; font-family: 'JetBrains Mono', monospace; background: #F8FAFC; border: 1px solid #E2E8F0; padding: 4px 12px; border-radius: 8px;">
          {slide_num:02d} / {total_slides:02d}
        </div>
      </div>
    </header>

    <!-- Bottom Bar -->
    <footer style="height: 44px; display: flex; align-items: center; justify-content: space-between; padding: 0 48px; border-top: 1px solid #E2E8F0; background: #FFFFFF; font-size: 12px; color: #64748B; flex-shrink: 0;">
      <div style="display: flex; align-items: center; gap: 20px;">
        <span style="display: flex; align-items: center; gap: 6px; font-weight: 600; color: #059669;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          Evidence-Grounded Deck · Audit-Compliant Prototype
        </span>
        <span style="color: #CBD5E1;">|</span>
        <span>Theme: <strong>Health Tech</strong> · Track: <strong>Open Innovation & YugabyteDB</strong></span>
      </div>
      <div style="display: flex; align-items: center; gap: 16px;">
        <span>Team Lead: <strong style="color: #102653;">Yashraj Rastogi</strong></span>
        <span style="color: #CBD5E1;">•</span>
        <span>Member: <strong style="color: #102653;">Amarpit Srivastav</strong></span>
        <span style="color: #CBD5E1;">•</span>
        <span>hackCBS 9.0</span>
      </div>
    </footer>
    """

def get_base_styles():
    return """
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap');
    
    * { box-sizing: border-box; margin: 0; padding: 0; }
    
    body {
      width: 1920px;
      height: 1080px;
      overflow: hidden;
      background: #F8FAFC;
      color: #102653;
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      display: flex;
      flex-direction: column;
      -webkit-font-smoothing: antialiased;
    }
    
    .content-area {
      flex: 1;
      padding: 36px 48px;
      display: flex;
      flex-direction: column;
      position: relative;
      background: radial-gradient(circle at 10% 20%, rgba(8, 123, 255, 0.04) 0%, transparent 45%),
                  radial-gradient(circle at 90% 80%, rgba(16, 38, 83, 0.03) 0%, transparent 45%);
    }

    .card {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 16px;
      box-shadow: 0 4px 20px -2px rgba(16, 38, 83, 0.05), 0 2px 6px -1px rgba(16, 38, 83, 0.03);
    }

    .badge-blue {
      background: #EAF4FF;
      color: #087BFF;
      border: 1px solid #BFDBFE;
      padding: 3px 10px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }

    .badge-green {
      background: #ECFDF5;
      color: #059669;
      border: 1px solid #A7F3D0;
      padding: 3px 10px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }

    .badge-amber {
      background: #FFFBEB;
      color: #D97706;
      border: 1px solid #FDE68A;
      padding: 3px 10px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }

    .badge-navy {
      background: #F1F5F9;
      color: #102653;
      border: 1px solid #CBD5E1;
      padding: 3px 10px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }
    """

# -------------------------------------------------------------
# SLIDE 1: Title Slide
# -------------------------------------------------------------
def generate_slide_1():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  {get_base_styles()}
</style>
</head>
<body>
  {get_chrome_decorations(1, 8, "hackCBS 9.0 · Open Innovation & YugabyteDB Track")}
  
  <div class="content-area" style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 40px; align-items: center;">
    
    <!-- Left Column: Branding, Pitch & Details -->
    <div style="display: flex; flex-direction: column; gap: 24px;">
      
      <div style="display: flex; align-items: center; gap: 12px;">
        <span class="badge-blue" style="font-size: 13px; padding: 4px 14px;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          Open Innovation & YugabyteDB Track
        </span>
        <span class="badge-green" style="font-size: 13px; padding: 4px 14px;">
          Theme: HealthTech
        </span>
        <span class="badge-amber" style="font-size: 13px; padding: 4px 14px;">
          Working Prototype
        </span>
      </div>

      <div>
        <h1 style="font-size: 68px; font-weight: 800; color: #102653; line-height: 1.05; letter-spacing: -1.5px; margin-bottom: 12px;">
          MedEasy
        </h1>
        <p style="font-size: 26px; font-weight: 700; color: #087BFF; line-height: 1.3;">
          Make the next medication conversation easier to prepare.
        </p>
        <p style="font-size: 17px; color: #475569; margin-top: 8px; line-height: 1.5;">
          Prescription review · Indicative price comparison · Pharmacy enquiry preparation · Cautious AI guidance
        </p>
      </div>

      <!-- Core Capabilities Grid -->
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 4px;">
        
        <div class="card" style="padding: 16px 20px; display: flex; gap: 14px; align-items: flex-start;">
          <div style="width: 36px; height: 36px; border-radius: 8px; background: #EAF4FF; color: #087BFF; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
          </div>
          <div>
            <div style="font-size: 15px; font-weight: 700; color: #102653;">Prescription Review</div>
            <div style="font-size: 13px; color: #64748B; margin-top: 3px;">OCR extraction with mandatory human verification gate.</div>
          </div>
        </div>

        <div class="card" style="padding: 16px 20px; display: flex; gap: 14px; align-items: flex-start;">
          <div style="width: 36px; height: 36px; border-radius: 8px; background: #ECFDF5; color: #059669; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          </div>
          <div>
            <div style="font-size: 15px; font-weight: 700; color: #102653;">3-Way Price Benchmark</div>
            <div style="font-size: 13px; color: #64748B; margin-top: 3px;">Branded MRP vs PMBJP Jan Aushadhi & DavaIndia.</div>
          </div>
        </div>

        <div class="card" style="padding: 16px 20px; display: flex; gap: 14px; align-items: flex-start;">
          <div style="width: 36px; height: 36px; border-radius: 8px; background: #EFF6FF; color: #2563EB; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
          </div>
          <div>
            <div style="font-size: 15px; font-weight: 700; color: #102653;">Pharmacy Enquiry</div>
            <div style="font-size: 13px; color: #64748B; margin-top: 3px;">User-controlled WhatsApp handoff to verify local stock.</div>
          </div>
        </div>

        <div class="card" style="padding: 16px 20px; display: flex; gap: 14px; align-items: flex-start;">
          <div style="width: 36px; height: 36px; border-radius: 8px; background: #FEF3C7; color: #D97706; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <div>
            <div style="font-size: 15px; font-weight: 700; color: #102653;">Cautious AI & Safety</div>
            <div style="font-size: 13px; color: #64748B; margin-top: 3px;">Deterministic non-prescribing guardrails & CDSCO lookup.</div>
          </div>
        </div>

      </div>

      <!-- Team Details Box -->
      <div class="card" style="padding: 18px 24px; background: #FFFFFF; border-left: 4px solid #087BFF; display: flex; align-items: center; justify-content: space-between;">
        <div>
          <div style="font-size: 12px; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 0.5px;">Hackathon Team</div>
          <div style="font-size: 18px; font-weight: 800; color: #102653; margin-top: 2px;">axioms</div>
        </div>
        <div style="display: flex; gap: 32px;">
          <div>
            <div style="font-size: 12px; font-weight: 600; color: #64748B;">Team Lead</div>
            <div style="font-size: 15px; font-weight: 700; color: #102653;">Yashraj Rastogi</div>
          </div>
          <div>
            <div style="font-size: 12px; font-weight: 600; color: #64748B;">Member</div>
            <div style="font-size: 15px; font-weight: 700; color: #102653;">Amarpit Srivastav</div>
          </div>
        </div>
        <div>
          <span class="badge-navy" style="font-size: 12px;">React 19 · FastAPI · YugabyteDB</span>
        </div>
      </div>

    </div>

    <!-- Right Column: Interactive MVP UI Mockup Preview -->
    <div style="display: flex; flex-direction: column; gap: 16px;">
      
      <!-- Live Preview Card (Matching MVP UI Design) -->
      <div class="card" style="padding: 24px; background: #FFFFFF; border: 1.5px solid #CBD5E1; box-shadow: 0 20px 40px -10px rgba(16, 38, 83, 0.12);">
        
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #F1F5F9; padding-bottom: 16px;">
          <div style="display: flex; align-items: center; gap: 10px;">
            <div style="width: 12px; height: 12px; border-radius: 50%; background: #10B981;"></div>
            <span style="font-size: 14px; font-weight: 700; color: #102653;">Human-Confirmed Medicine Review</span>
          </div>
          <span class="badge-green">Verified Active Salt</span>
        </div>

        <div style="margin-top: 18px; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 18px;">
          <div style="display: flex; justify-content: space-between; align-items: baseline;">
            <div>
              <div style="font-size: 20px; font-weight: 800; color: #102653;">Rabeprazole + Domperidone</div>
              <div style="font-size: 13px; font-weight: 600; color: #64748B; margin-top: 2px;">Capsule · 20mg + 30mg SR · Strip of 10</div>
            </div>
            <span style="font-size: 12px; font-weight: 700; color: #087BFF; background: #EAF4FF; padding: 3px 10px; border-radius: 6px;">OCR Matched</span>
          </div>

          <div style="margin-top: 16px; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px;">
            
            <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 12px; text-align: center;">
              <div style="font-size: 11px; font-weight: 600; color: #64748B;">Private Brand (Razo-D)</div>
              <div style="font-size: 20px; font-weight: 800; color: #64748B; margin-top: 4px;">₹210.00</div>
              <div style="font-size: 10px; color: #94A3B8; margin-top: 2px;">Market MRP</div>
            </div>

            <div style="background: #ECFDF5; border: 1.5px solid #10B981; border-radius: 8px; padding: 12px; text-align: center; position: relative;">
              <div style="position: absolute; top: -8px; left: 50%; transform: translateX(-50%); background: #10B981; color: white; font-size: 9px; font-weight: 800; padding: 1px 6px; border-radius: 999px;">BEST VALUE</div>
              <div style="font-size: 11px; font-weight: 700; color: #065F46;">PMBJP Jan Aushadhi</div>
              <div style="font-size: 22px; font-weight: 800; color: #059669; margin-top: 4px;">₹28.00</div>
              <div style="font-size: 11px; font-weight: 700; color: #059669; margin-top: 2px;">Save ~86%</div>
            </div>

            <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 12px; text-align: center;">
              <div style="font-size: 11px; font-weight: 600; color: #64748B;">DavaIndia Generic</div>
              <div style="font-size: 20px; font-weight: 800; color: #102653; margin-top: 4px;">₹35.00</div>
              <div style="font-size: 10px; color: #059669; margin-top: 2px;">Save ~83%</div>
            </div>

          </div>
        </div>

        <!-- Pharmacy Action Preview -->
        <div style="margin-top: 16px; display: flex; align-items: center; justify-content: space-between; background: #F1F5F9; border-radius: 10px; padding: 12px 16px;">
          <div style="display: flex; align-items: center; gap: 10px;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="2"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>
            <div>
              <div style="font-size: 13px; font-weight: 700; color: #102653;">PMBJP Kendra Rohini Sec-7</div>
              <div style="font-size: 11px; color: #64748B;">0.8 km away · Call to confirm stock</div>
            </div>
          </div>
          <span style="font-size: 12px; font-weight: 700; color: #2563EB; background: #DBEAFE; padding: 4px 10px; border-radius: 6px;">WhatsApp Enquiry</span>
        </div>

        <div style="margin-top: 16px; display: flex; align-items: center; gap: 8px; font-size: 11px; color: #64748B;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#D97706" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
          <span>Prices are indicative catalogue references. Pack sizes and availability subject to pharmacy confirmation.</span>
        </div>

      </div>

    </div>

  </div>
</body>
</html>"""

# -------------------------------------------------------------
# SLIDE 2: The Problem
# -------------------------------------------------------------
def generate_slide_2():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  {get_base_styles()}
</style>
</head>
<body>
  {get_chrome_decorations(2, 8, "Problem Analysis & Real-World Friction")}
  
  <div class="content-area" style="display: flex; flex-direction: column; justify-content: space-between;">
    
    <div>
      <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
        <span class="badge-amber">The Healthcare Journey</span>
        <span style="font-size: 14px; font-weight: 600; color: #64748B;">Understanding the friction after leaving the doctor's clinic</span>
      </div>
      <h2 style="font-size: 42px; font-weight: 800; color: #102653; letter-spacing: -1px;">
        A Prescription Starts a Chain of Decisions
      </h2>
      <p style="font-size: 17px; color: #475569; margin-top: 4px;">
        Medication work does not end when a prescription is written. Patients and caregivers face 4 critical friction points.
      </p>
    </div>

    <!-- 4 Journey Cards -->
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin: 18px 0;">
      
      <!-- Step 1 -->
      <div class="card" style="padding: 24px; display: flex; flex-direction: column; justify-content: space-between; border-top: 4px solid #087BFF;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="width: 42px; height: 42px; border-radius: 10px; background: #EAF4FF; color: #087BFF; display: flex; align-items: center; justify-content: center;">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/></svg>
            </div>
            <span style="font-size: 13px; font-weight: 800; color: #94A3B8;">STEP 01</span>
          </div>
          <div style="font-size: 18px; font-weight: 800; color: #102653; margin-top: 16px;">Decipher & Read</div>
          <p style="font-size: 14px; color: #64748B; margin-top: 8px; line-height: 1.5;">
            Handwritten, rushed, or photographed doctor slips are notoriously difficult for patients and elderly caregivers to read with confidence.
          </p>
        </div>
        <div style="margin-top: 20px; background: #F8FAFC; border-radius: 8px; padding: 10px 12px; font-size: 12px; color: #475569; border: 1px solid #E2E8F0;">
          ⚠️ <strong>Risk:</strong> Misinterpreting active salts or dosages.
        </div>
      </div>

      <!-- Step 2 -->
      <div class="card" style="padding: 24px; display: flex; flex-direction: column; justify-content: space-between; border-top: 4px solid #6366F1;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="width: 42px; height: 42px; border-radius: 10px; background: #EEF2FF; color: #6366F1; display: flex; align-items: center; justify-content: center;">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
            </div>
            <span style="font-size: 13px; font-weight: 800; color: #94A3B8;">STEP 02</span>
          </div>
          <div style="font-size: 18px; font-weight: 800; color: #102653; margin-top: 16px;">Verify Medicine List</div>
          <p style="font-size: 14px; color: #64748B; margin-top: 8px; line-height: 1.5;">
            Patients struggle to confirm what each medicine does, which active salts exist, and whether generic alternatives match their prescribed formulation.
          </p>
        </div>
        <div style="margin-top: 20px; background: #F8FAFC; border-radius: 8px; padding: 10px 12px; font-size: 12px; color: #475569; border: 1px solid #E2E8F0;">
          ⚠️ <strong>Risk:</strong> Fear of switching to low-cost generics.
        </div>
      </div>

      <!-- Step 3 -->
      <div class="card" style="padding: 24px; display: flex; flex-direction: column; justify-content: space-between; border-top: 4px solid #059669;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="width: 42px; height: 42px; border-radius: 10px; background: #ECFDF5; color: #059669; display: flex; align-items: center; justify-content: center;">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
            </div>
            <span style="font-size: 13px; font-weight: 800; color: #94A3B8;">STEP 03</span>
          </div>
          <div style="font-size: 18px; font-weight: 800; color: #102653; margin-top: 16px;">Compare & Budget</div>
          <p style="font-size: 14px; color: #64748B; margin-top: 8px; line-height: 1.5;">
            Massive price asymmetries exist between commercial brands and Jan Aushadhi generic options, forcing families into out-of-pocket spending distress.
          </p>
        </div>
        <div style="margin-top: 20px; background: #ECFDF5; border-radius: 8px; padding: 10px 12px; font-size: 12px; color: #065F46; border: 1px solid #A7F3D0;">
          📊 <strong>Evidence:</strong> 39.4% out-of-pocket health spend (NHA).
        </div>
      </div>

      <!-- Step 4 -->
      <div class="card" style="padding: 24px; display: flex; flex-direction: column; justify-content: space-between; border-top: 4px solid #D97706;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="width: 42px; height: 42px; border-radius: 10px; background: #FFFBEB; color: #D97706; display: flex; align-items: center; justify-content: center;">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
            </div>
            <span style="font-size: 13px; font-weight: 800; color: #94A3B8;">STEP 04</span>
          </div>
          <div style="font-size: 18px; font-weight: 800; color: #102653; margin-top: 16px;">Enquire & Carry</div>
          <p style="font-size: 14px; color: #64748B; margin-top: 8px; line-height: 1.5;">
            Generics are not stocked at every pharmacy. Patients wander between stores with no direct way to check availability or carry structured records.
          </p>
        </div>
        <div style="margin-top: 20px; background: #FFFBEB; border-radius: 8px; padding: 10px 12px; font-size: 12px; color: #92400E; border: 1px solid #FDE68A;">
          ⚠️ <strong>Risk:</strong> Non-adherence due to stock friction.
        </div>
      </div>

    </div>

    <!-- Clinical Boundary & Authority Grounding -->
    <div style="display: grid; grid-template-columns: 1.4fr 1fr; gap: 20px;">
      
      <div class="card" style="padding: 18px 24px; background: #F8FAFC; border-left: 4px solid #102653; display: flex; align-items: center; gap: 16px;">
        <div style="width: 40px; height: 40px; border-radius: 50%; background: #E2E8F0; color: #102653; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        </div>
        <div>
          <div style="font-size: 14px; font-weight: 800; color: #102653;">Explicit Clinical Boundary</div>
          <div style="font-size: 13px; color: #475569; margin-top: 2px;">
            MedEasy is strictly designed to make these preparation and enquiry steps structured, transparent, and accessible. <strong>It does not diagnose, prescribe, or replace professional medical advice.</strong>
          </div>
        </div>
      </div>

      <div class="card" style="padding: 18px 24px; background: #FFFFFF; display: flex; align-items: center; justify-content: space-between;">
        <div>
          <div style="font-size: 11px; font-weight: 700; color: #64748B; text-transform: uppercase;">Evidence Grounding</div>
          <div style="font-size: 13px; font-weight: 700; color: #102653; margin-top: 2px;">WHO Medication Reconciliation</div>
          <div style="font-size: 11px; color: #64748B;">Transitions of Care Guidance (WHO-UHC-SDS-2019.9)</div>
        </div>
        <span class="badge-blue">Health Standards</span>
      </div>

    </div>

  </div>
</body>
</html>"""

# -------------------------------------------------------------
# SLIDE 3: Target User & Validation Framework
# -------------------------------------------------------------
def generate_slide_3():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  {get_base_styles()}
</style>
</head>
<body>
  {get_chrome_decorations(3, 8, "Target User Persona & Validation Framework")}
  
  <div class="content-area" style="display: flex; flex-direction: column; justify-content: space-between;">
    
    <div>
      <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
        <span class="badge-blue">User Centricity</span>
        <span style="font-size: 14px; font-weight: 600; color: #64748B;">Grounding product design in verifiable user workflows</span>
      </div>
      <h2 style="font-size: 42px; font-weight: 800; color: #102653; letter-spacing: -1px;">
        Target User & Validation Framework
      </h2>
      <p style="font-size: 17px; color: #475569; margin-top: 4px;">
        Distinguishing between our working persona hypothesis and the structured usability study to validate it.
      </p>
    </div>

    <!-- Main 2-Column Split -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin: 16px 0;">
      
      <!-- Left Column: Initial Persona Hypothesis -->
      <div class="card" style="padding: 28px; display: flex; flex-direction: column; justify-content: space-between; border-left: 4px solid #087BFF;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <span class="badge-blue">Primary Target Persona</span>
            <span class="badge-amber">Working Hypothesis</span>
          </div>

          <div style="margin-top: 18px; display: flex; align-items: center; gap: 16px;">
            <div style="width: 56px; height: 56px; border-radius: 14px; background: #EAF4FF; color: #087BFF; display: flex; align-items: center; justify-content: center; font-size: 26px; font-weight: 800;">
              👨🏽‍🦳
            </div>
            <div>
              <div style="font-size: 22px; font-weight: 800; color: #102653;">Adult Patient or Caregiver</div>
              <div style="font-size: 14px; font-weight: 600; color: #64748B;">Managing recurring medications for chronic conditions</div>
            </div>
          </div>

          <div style="margin-top: 22px; display: flex; flex-direction: column; gap: 14px;">
            
            <div style="background: #F8FAFC; border-radius: 10px; padding: 14px; border: 1px solid #E2E8F0;">
              <div style="font-size: 13px; font-weight: 700; color: #102653;">Core Behavioral Profile</div>
              <div style="font-size: 13px; color: #475569; margin-top: 4px; line-height: 1.5;">
                • Manages 2–4 daily prescriptions (e.g., Diabetes, Hypertension, Acid Reflux).<br>
                • Regularly visits local chemists or PMBJP Jan Aushadhi Kendras.<br>
                • Needs to decipher handwritten doctor notes and ensure salt equivalence.
              </div>
            </div>

            <div style="background: #F8FAFC; border-radius: 10px; padding: 14px; border: 1px solid #E2E8F0;">
              <div style="font-size: 13px; font-weight: 700; color: #102653;">Primary Jobs to be Done</div>
              <div style="font-size: 13px; color: #475569; margin-top: 4px; line-height: 1.5;">
                1. Verify active ingredients before purchasing unfamiliar generic brands.<br>
                2. Calculate out-of-pocket savings against commercial brand MRP.<br>
                3. Prepare pre-filled enquiries for local pharmacy stock availability.
              </div>
            </div>

          </div>
        </div>

        <div style="margin-top: 16px; font-size: 12px; color: #64748B; font-style: italic;">
          * Note: Framed as an illustrative hypothesis grounded in clinical transitions of care, not a finalized empirical cohort.
        </div>
      </div>

      <!-- Right Column: Evidence Baseline & Usability Study Protocol -->
      <div style="display: flex; flex-direction: column; gap: 18px;">
        
        <!-- Top: What We Know Today -->
        <div class="card" style="padding: 22px; background: #FFFFFF;">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="font-size: 16px; font-weight: 800; color: #102653;">Evidence Baseline: What We Know Today</div>
            <span class="badge-navy">Code Audited</span>
          </div>
          <div style="margin-top: 12px; display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
            <div style="background: #F8FAFC; padding: 12px; border-radius: 8px; border: 1px solid #E2E8F0;">
              <div style="font-size: 12px; font-weight: 700; color: #087BFF;">✓ Implemented Prototype</div>
              <div style="font-size: 12px; color: #64748B; margin-top: 2px;">React 19 + FastAPI + YugabyteDB full-stack flow verified.</div>
            </div>
            <div style="background: #F8FAFC; padding: 12px; border-radius: 8px; border: 1px solid #E2E8F0;">
              <div style="font-size: 12px; font-weight: 700; color: #059669;">✓ Seeded Data Sets</div>
              <div style="font-size: 12px; color: #64748B; margin-top: 2px;">508 generic medicines, 260 CDSCO NSQ records, 30 pharmacies.</div>
            </div>
          </div>
          <div style="margin-top: 10px; font-size: 12px; color: #94A3B8;">
            Honest Gap Acknowledgment: The repo currently contains zero user interview transcripts or usability logs.
          </div>
        </div>

        <!-- Bottom: Next Validation Study Protocol -->
        <div class="card" style="padding: 22px; background: #FFFFFF; border-left: 4px solid #10B981; flex: 1;">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="font-size: 16px; font-weight: 800; color: #102653;">Validation Protocol: The Next Study</div>
            <span class="badge-green">Planned Milestone</span>
          </div>
          
          <div style="margin-top: 14px; font-size: 13px; color: #475569;">
            <strong>Cohort:</strong> 8–10 Patients/Caregivers + 3 Community Pharmacists / Health Workers
          </div>

          <!-- 5 Tasks -->
          <div style="margin-top: 10px; display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px;">
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 10px 8px; text-align: center;">
              <div style="font-size: 10px; font-weight: 800; color: #087BFF;">TASK 1</div>
              <div style="font-size: 11px; font-weight: 700; color: #102653; margin-top: 4px;">OCR Review</div>
              <div style="font-size: 10px; color: #64748B; margin-top: 2px;">Confirm salts</div>
            </div>
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 10px 8px; text-align: center;">
              <div style="font-size: 10px; font-weight: 800; color: #087BFF;">TASK 2</div>
              <div style="font-size: 11px; font-weight: 700; color: #102653; margin-top: 4px;">Compare</div>
              <div style="font-size: 10px; color: #64748B; margin-top: 2px;">Evaluate prices</div>
            </div>
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 10px 8px; text-align: center;">
              <div style="font-size: 10px; font-weight: 800; color: #087BFF;">TASK 3</div>
              <div style="font-size: 11px; font-weight: 700; color: #102653; margin-top: 4px;">Enquire</div>
              <div style="font-size: 10px; color: #64748B; margin-top: 2px;">Draft WhatsApp</div>
            </div>
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 10px 8px; text-align: center;">
              <div style="font-size: 10px; font-weight: 800; color: #087BFF;">TASK 4</div>
              <div style="font-size: 11px; font-weight: 700; color: #102653; margin-top: 4px;">Consent</div>
              <div style="font-size: 10px; color: #64748B; margin-top: 2px;">AI disclosures</div>
            </div>
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 10px 8px; text-align: center;">
              <div style="font-size: 10px; font-weight: 800; color: #087BFF;">TASK 5</div>
              <div style="font-size: 11px; font-weight: 700; color: #102653; margin-top: 4px;">Control</div>
              <div style="font-size: 10px; color: #64748B; margin-top: 2px;">Forget memory</div>
            </div>
          </div>

          <div style="margin-top: 14px; background: #ECFDF5; border-radius: 8px; padding: 8px 12px; font-size: 11px; color: #065F46; display: flex; align-items: center; gap: 8px;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            <span><strong>Research Safety Rule:</strong> Zero real personal health records will be retained in study documentation.</span>
          </div>

        </div>

      </div>

    </div>

  </div>
</body>
</html>"""

# -------------------------------------------------------------
# SLIDE 4: The Solution & Feature Status Matrix
# -------------------------------------------------------------
def generate_slide_4():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  {get_base_styles()}
</style>
</head>
<body>
  {get_chrome_decorations(4, 8, "Product Capabilities & Evidence Status")}
  
  <div class="content-area" style="display: flex; flex-direction: column; justify-content: space-between;">
    
    <div>
      <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
        <span class="badge-blue">End-to-End Workflow</span>
        <span style="font-size: 14px; font-weight: 600; color: #64748B;">Audit-transparent status of all functional modules</span>
      </div>
      <h2 style="font-size: 42px; font-weight: 800; color: #102653; letter-spacing: -1px;">
        One Workflow to Prepare, Review, and Ask
      </h2>
      <p style="font-size: 16px; color: #475569; margin-top: 2px;">
        A single cohesive pipeline designed to protect patient safety and deliver price transparency.
      </p>
    </div>

    <!-- 5-Step Pipeline Flow Bar -->
    <div style="display: flex; align-items: center; justify-content: space-between; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 14px 24px; margin: 10px 0;">
      
      <div style="display: flex; align-items: center; gap: 10px;">
        <span style="width: 28px; height: 28px; border-radius: 50%; background: #087BFF; color: white; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 800;">1</span>
        <div>
          <div style="font-size: 13px; font-weight: 800; color: #102653;">Upload Prescription</div>
          <div style="font-size: 11px; color: #64748B;">Image or PDF</div>
        </div>
      </div>
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#94A3B8" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>

      <div style="display: flex; align-items: center; gap: 10px;">
        <span style="width: 28px; height: 28px; border-radius: 50%; background: #087BFF; color: white; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 800;">2</span>
        <div>
          <div style="font-size: 13px; font-weight: 800; color: #102653;">Human Review Gate</div>
          <div style="font-size: 11px; color: #64748B;">Confirm extracted salt</div>
        </div>
      </div>
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#94A3B8" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>

      <div style="display: flex; align-items: center; gap: 10px;">
        <span style="width: 28px; height: 28px; border-radius: 50%; background: #059669; color: white; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 800;">3</span>
        <div>
          <div style="font-size: 13px; font-weight: 800; color: #102653;">Compare Prices</div>
          <div style="font-size: 11px; color: #64748B;">Brand vs Jan Aushadhi</div>
        </div>
      </div>
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#94A3B8" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>

      <div style="display: flex; align-items: center; gap: 10px;">
        <span style="width: 28px; height: 28px; border-radius: 50%; background: #087BFF; color: white; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 800;">4</span>
        <div>
          <div style="font-size: 13px; font-weight: 800; color: #102653;">Pharmacy Enquiry</div>
          <div style="font-size: 11px; color: #64748B;">User WhatsApp handoff</div>
        </div>
      </div>
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#94A3B8" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>

      <div style="display: flex; align-items: center; gap: 10px;">
        <span style="width: 28px; height: 28px; border-radius: 50%; background: #102653; color: white; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 800;">5</span>
        <div>
          <div style="font-size: 13px; font-weight: 800; color: #102653;">Ask MedSaathi</div>
          <div style="font-size: 11px; color: #64748B;">Cautious guidance</div>
        </div>
      </div>

    </div>

    <!-- Evidence Status Grid -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 8px;">
      
      <!-- Column 1: Core Product Modules -->
      <div class="card" style="padding: 16px 20px;">
        <div style="font-size: 14px; font-weight: 800; color: #102653; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center;">
          <span>Core Healthcare Capabilities</span>
          <span style="font-size: 11px; color: #64748B;">Code Implementation State</span>
        </div>

        <div style="display: flex; flex-direction: column; gap: 10px;">
          
          <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; background: #F8FAFC; border-radius: 8px; border: 1px solid #E2E8F0;">
            <div>
              <div style="font-size: 13px; font-weight: 700; color: #102653;">Prescription OCR Extraction</div>
              <div style="font-size: 11px; color: #64748B;">FastAPI endpoint + Gemini Vision extraction path</div>
            </div>
            <span class="badge-green">Implemented</span>
          </div>

          <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; background: #F8FAFC; border-radius: 8px; border: 1px solid #E2E8F0;">
            <div>
              <div style="font-size: 13px; font-weight: 700; color: #102653;">Human Review & Confirmation Gate</div>
              <div style="font-size: 11px; color: #64748B;">ScanPage requires patient verification of salts</div>
            </div>
            <span class="badge-green">Implemented</span>
          </div>

          <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; background: #F8FAFC; border-radius: 8px; border: 1px solid #E2E8F0;">
            <div>
              <div style="font-size: 13px; font-weight: 700; color: #102653;">3-Way Indicative Price Comparison</div>
              <div style="font-size: 11px; color: #64748B;">508 formulations (Brand vs Jan Aushadhi vs DavaIndia)</div>
            </div>
            <span class="badge-amber">Indicative Data</span>
          </div>

          <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; background: #F8FAFC; border-radius: 8px; border: 1px solid #E2E8F0;">
            <div>
              <div style="font-size: 13px; font-weight: 700; color: #102653;">Enquiry Cart & Handoff</div>
              <div style="font-size: 11px; color: #64748B;">Session-based enquiry builder; not a financial order</div>
            </div>
            <span class="badge-blue">Session Proto</span>
          </div>

        </div>
      </div>

      <!-- Column 2: Safety, Pharmacy & AI -->
      <div class="card" style="padding: 16px 20px;">
        <div style="font-size: 14px; font-weight: 800; color: #102653; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center;">
          <span>Safety, Pharmacy & AI Services</span>
          <span style="font-size: 11px; color: #64748B;">Evidence Audit Status</span>
        </div>

        <div style="display: flex; flex-direction: column; gap: 10px;">
          
          <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; background: #F8FAFC; border-radius: 8px; border: 1px solid #E2E8F0;">
            <div>
              <div style="font-size: 13px; font-weight: 700; color: #102653;">Pharmacy Directory & Availability</div>
              <div style="font-size: 11px; color: #64748B;">30 seeded Delhi locations; flagged "Call to confirm"</div>
            </div>
            <span class="badge-amber">Call to Confirm</span>
          </div>

          <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; background: #F8FAFC; border-radius: 8px; border: 1px solid #E2E8F0;">
            <div>
              <div style="font-size: 13px; font-weight: 700; color: #102653;">WhatsApp Availability Enquiry</div>
              <div style="font-size: 11px; color: #64748B;">Generates pre-filled wa.me text; user-dispatched</div>
            </div>
            <span class="badge-green">Implemented</span>
          </div>

          <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; background: #F8FAFC; border-radius: 8px; border: 1px solid #E2E8F0;">
            <div>
              <div style="font-size: 13px; font-weight: 700; color: #102653;">CDSCO Batch Safety Verification</div>
              <div style="font-size: 11px; color: #64748B;">260 NSQ records; manual verification recommended</div>
            </div>
            <span class="badge-amber">Review Dataset</span>
          </div>

          <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; background: #F8FAFC; border-radius: 8px; border: 1px solid #E2E8F0;">
            <div>
              <div style="font-size: 13px; font-weight: 700; color: #102653;">MedSaathi Cautious AI Assistant</div>
              <div style="font-size: 11px; color: #64748B;">Bilingual chat with strict deterministic refusal guardrails</div>
            </div>
            <span class="badge-green">Implemented</span>
          </div>

        </div>
      </div>

    </div>

    <!-- Bottom Boundary Callout -->
    <div style="background: #FFFBEB; border: 1px solid #FDE68A; border-radius: 10px; padding: 10px 18px; font-size: 12px; color: #92400E; display: flex; align-items: center; gap: 12px;">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
      <div>
        <strong>Transparent Evidence Statement:</strong> Indicative catalogue prices are not live quotes; pharmacy listings do not guarantee stock; and CDSCO records require manual confirmation before clinical safety claims.
      </div>
    </div>

  </div>
</body>
</html>"""

# -------------------------------------------------------------
# SLIDE 5: Context & Memory: The ON/OFF Evidence & Demo Gate
# -------------------------------------------------------------
def generate_slide_5():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  {get_base_styles()}
</style>
</head>
<body>
  {get_chrome_decorations(5, 8, "Context Architecture & Demo Readiness Gate")}
  
  <div class="content-area" style="display: flex; flex-direction: column; justify-content: space-between;">
    
    <div>
      <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
        <span class="badge-blue">Track A Focus</span>
        <span style="font-size: 14px; font-weight: 600; color: #64748B;">The Core Thesis: Remembering Must Change the Outcome — Safely</span>
      </div>
      <h2 style="font-size: 42px; font-weight: 800; color: #102653; letter-spacing: -1px;">
        Context Architecture: The ON / OFF Design & Gate
      </h2>
      <p style="font-size: 16px; color: #475569; margin-top: 2px;">
        Demonstrating the material difference between stateless AI and verifiable, user-controlled clinical memory.
      </p>
    </div>

    <!-- Two-Column ON / OFF Comparison -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin: 12px 0;">
      
      <!-- OFF State -->
      <div class="card" style="padding: 22px; border-top: 4px solid #94A3B8;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <div style="width: 10px; height: 10px; border-radius: 50%; background: #94A3B8;"></div>
            <span style="font-size: 17px; font-weight: 800; color: #475569;">OFF — Stateless Default</span>
          </div>
          <span class="badge-navy">Default Consent = False</span>
        </div>

        <div style="margin-top: 14px; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 10px; padding: 14px;">
          <div style="font-size: 12px; font-weight: 700; color: #64748B; text-transform: uppercase;">Behavioral State</div>
          <p style="font-size: 13px; color: #102653; margin-top: 4px; line-height: 1.5;">
            • Zero past health context is retrieved or supplied to the model.<br>
            • System treats each conversation turn as an isolated, cold session.<br>
            • Cannot remember previously stated drug hypersensitivities.
          </p>
        </div>

        <div style="margin-top: 14px; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px; padding: 14px;">
          <div style="font-size: 12px; font-weight: 700; color: #64748B;">User Inquiry Example:</div>
          <div style="font-size: 13px; font-style: italic; color: #102653; margin-top: 2px;">"Can I take Amoxicillin for my throat infection?"</div>
          <div style="margin-top: 8px; font-size: 12px; color: #64748B; border-left: 2px solid #94A3B8; padding-left: 8px;">
            <strong>Generic Response:</strong> Refuses prescription, advises seeing a doctor. Cannot issue specific allergy warning.
          </div>
        </div>
      </div>

      <!-- ON State -->
      <div class="card" style="padding: 22px; border-top: 4px solid #10B981;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <div style="width: 10px; height: 10px; border-radius: 50%; background: #10B981;"></div>
            <span style="font-size: 17px; font-weight: 800; color: #059669;">ON — Context-Aware Memory</span>
          </div>
          <span class="badge-green">Explicit Opt-In Required</span>
        </div>

        <div style="margin-top: 14px; background: #ECFDF5; border: 1px solid #A7F3D0; border-radius: 10px; padding: 14px;">
          <div style="font-size: 12px; font-weight: 700; color: #065F46; text-transform: uppercase;">Materially Changed Outcome</div>
          <p style="font-size: 13px; color: #065F46; margin-top: 4px; line-height: 1.5;">
            • Recalls verified patient-reported facts <em>before</em> reasoning.<br>
            • Identifies cross-drug contraindication (Amoxicillin is Penicillin class).<br>
            • Triggers immediate clinical safety alert and home care alternative.
          </p>
        </div>

        <div style="margin-top: 14px; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px; padding: 14px;">
          <div style="font-size: 12px; font-weight: 700; color: #059669;">Recalled Memory Trigger:</div>
          <div style="font-size: 13px; font-style: italic; color: #102653; margin-top: 2px;">"Patient reported severe penicillin allergy (anaphylaxis risk)"</div>
          <div style="margin-top: 8px; font-size: 12px; color: #DC2626; border-left: 2px solid #DC2626; padding-left: 8px;">
            <strong>🚨 Material Clinical Interception:</strong> "CRITICAL ALLERGY ALERT: Amoxicillin is a penicillin-class antibiotic..."
          </div>
        </div>
      </div>

    </div>

    <!-- The Demo Readiness Gate (Closing PPT_GAP_REPORT) -->
    <div class="card" style="padding: 16px 24px; background: #FFFFFF; border: 1.5px solid #CBD5E1;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
        <div style="display: flex; align-items: center; gap: 8px;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#087BFF" stroke-width="2.5"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
          <span style="font-size: 15px; font-weight: 800; color: #102653;">Our Strict 5-Point Demo Readiness Gate</span>
        </div>
        <span class="badge-blue">Audit Rule: No Scripted Fictions</span>
      </div>

      <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px; font-size: 12px;">
        
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 10px;">
          <div style="font-weight: 700; color: #087BFF;">1. Dedicated Pack</div>
          <div style="color: #64748B; margin-top: 2px;">Synthetic demo datapack; zero real patient data.</div>
        </div>

        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 10px;">
          <div style="font-weight: 700; color: #087BFF;">2. Synced Consent</div>
          <div style="color: #64748B; margin-top: 2px;">UI toggle synchronizes directly with chat runtime.</div>
        </div>

        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 10px;">
          <div style="font-weight: 700; color: #087BFF;">3. Visible Source</div>
          <div style="color: #64748B; margin-top: 2px;">Context Panel shows exact returned text & ID.</div>
        </div>

        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 10px;">
          <div style="font-weight: 700; color: #087BFF;">4. Working Forget</div>
          <div style="color: #64748B; margin-top: 2px;">One-click remote delete confirmation receipt.</div>
        </div>

        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 10px;">
          <div style="font-weight: 700; color: #087BFF;">5. Zero Leakage</div>
          <div style="color: #64748B; margin-top: 2px;">Strict per-user datapack isolation verified.</div>
        </div>

      </div>
    </div>

  </div>
</body>
</html>"""

# -------------------------------------------------------------
# SLIDE 6: System Architecture, YugabyteDB & Privacy Boundary
# -------------------------------------------------------------
def generate_slide_6():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  {get_base_styles()}
</style>
</head>
<body>
  {get_chrome_decorations(6, 8, "Distributed Architecture & YugabyteDB Track")}
  
  <div class="content-area" style="display: flex; flex-direction: column; justify-content: space-between;">
    
    <div>
      <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
        <span class="badge-blue">System Design</span>
        <span style="font-size: 14px; font-weight: 600; color: #64748B;">Distributed resilience with enterprise data isolation</span>
      </div>
      <h2 style="font-size: 42px; font-weight: 800; color: #102653; letter-spacing: -1px;">
        Architecture, YugabyteDB & Privacy Boundaries
      </h2>
      <p style="font-size: 16px; color: #475569; margin-top: 2px;">
        Separation of identity, distributed ACID metadata, ephemeral AI processing, and optional memory.
      </p>
    </div>

    <!-- Architecture Visual Data Flow -->
    <div style="display: grid; grid-template-columns: 1.35fr 0.65fr; gap: 24px; margin: 12px 0;">
      
      <!-- Left: Diagram Flow Cards -->
      <div class="card" style="padding: 24px; background: #FFFFFF; display: flex; flex-direction: column; justify-content: space-between;">
        
        <div style="font-size: 15px; font-weight: 800; color: #102653; margin-bottom: 14px; display: flex; justify-content: space-between;">
          <span>End-to-End Component Flow</span>
          <span style="font-size: 12px; font-weight: 600; color: #087BFF;">Async Python & Distributed SQL</span>
        </div>

        <div style="display: flex; flex-direction: column; gap: 12px;">
          
          <!-- Client to API -->
          <div style="display: flex; align-items: center; gap: 14px;">
            <div style="flex: 1; background: #F8FAFC; border: 1.5px solid #CBD5E1; border-radius: 10px; padding: 12px; text-align: center;">
              <div style="font-size: 14px; font-weight: 800; color: #102653;">Patient Client</div>
              <div style="font-size: 11px; color: #64748B; margin-top: 2px;">React 19 · Vite · Tailwind · Audio API</div>
            </div>
            <div style="color: #087BFF; font-weight: 700; font-size: 18px;">➔</div>
            <div style="flex: 1; background: #EAF4FF; border: 1.5px solid #BFDBFE; border-radius: 10px; padding: 12px; text-align: center;">
              <div style="font-size: 14px; font-weight: 800; color: #087BFF;">FastAPI Backend</div>
              <div style="font-size: 11px; color: #1E40AF; margin-top: 2px;">Async SQLAlchemy · Pydantic · Guardrails</div>
            </div>
          </div>

          <!-- API Connected Services -->
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 6px;">
            
            <!-- YugabyteDB Box (Prominent for Yugabyte Track!) -->
            <div style="background: #EFF6FF; border: 2px solid #3B82F6; border-radius: 12px; padding: 16px;">
              <div style="display: flex; align-items: center; justify-content: space-between;">
                <div style="display: flex; align-items: center; gap: 8px;">
                  <div style="width: 24px; height: 24px; border-radius: 6px; background: #3B82F6; color: white; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 800;">Y</div>
                  <div style="font-size: 15px; font-weight: 800; color: #1E3A8A;">YugabyteDB</div>
                </div>
                <span class="badge-blue" style="font-size: 10px;">Distributed SQL</span>
              </div>
              <div style="font-size: 12px; color: #1E40AF; margin-top: 8px; line-height: 1.4;">
                • Cloud-native, distributed PostgreSQL ACID storage.<br>
                • Stores: User accounts, profile metadata, privacy consent states, token hashes & datapack link records.<br>
                • Resilient horizontal scalability & high availability.
              </div>
            </div>

            <!-- AI & Memory Providers -->
            <div style="background: #F8FAFC; border: 1.5px solid #CBD5E1; border-radius: 12px; padding: 16px;">
              <div style="display: flex; align-items: center; justify-content: space-between;">
                <div style="font-size: 15px; font-weight: 800; color: #102653;">Hosted AI & Memory</div>
                <span class="badge-navy" style="font-size: 10px;">Ephemeral / MCP</span>
              </div>
              <div style="font-size: 12px; color: #475569; margin-top: 8px; line-height: 1.4;">
                • <strong>Google Gemini:</strong> Vision OCR & conversational LLM.<br>
                • <strong>Meko MCP Stream:</strong> Optional user-consented context layer.<br>
                • <strong>WhatsApp:</strong> User-controlled local pharmacy enquiry.
              </div>
            </div>

          </div>

        </div>

        <div style="margin-top: 14px; background: #F1F5F9; border-radius: 8px; padding: 10px 14px; font-size: 12px; color: #475569; display: flex; align-items: center; gap: 8px;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
          <span><strong>Architectural Invariant:</strong> Identity & consent metadata stay in YugabyteDB; zero raw medical scans persist in cloud storage.</span>
        </div>

      </div>

      <!-- Right: Privacy Boundary Facts -->
      <div class="card" style="padding: 24px; background: #FFFFFF; border-left: 4px solid #10B981; display: flex; flex-direction: column; justify-content: space-between;">
        
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="font-size: 16px; font-weight: 800; color: #102653;">Hardened Privacy Facts</div>
            <span class="badge-green">Verified</span>
          </div>

          <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 12px; font-size: 13px; color: #475569;">
            
            <div style="padding-bottom: 10px; border-bottom: 1px solid #F1F5F9;">
              <strong style="color: #102653;">Zero Permanent Scan Storage:</strong><br>
              Uploaded prescription files are processed ephemerally in-memory for OCR and immediately discarded.
            </div>

            <div style="padding-bottom: 10px; border-bottom: 1px solid #F1F5F9;">
              <strong style="color: #102653;">Strict Separation of Concerns:</strong><br>
              Account authentication and consent records stored in YugabyteDB are completely decoupled from external AI prompts.
            </div>

            <div style="padding-bottom: 10px; border-bottom: 1px solid #F1F5F9;">
              <strong style="color: #102653;">Patient-Governed Memory:</strong><br>
              Meko is invoked only when active consent is set to TRUE. Users can purge their datapack with a single tap.
            </div>

            <div>
              <strong style="color: #102653;">No Silent Tracking:</strong><br>
              Pharmacy interactions require explicit user initiation through WhatsApp (`wa.me`).
            </div>

          </div>
        </div>

        <div style="margin-top: 14px; background: #ECFDF5; border-radius: 8px; padding: 10px; font-size: 11px; color: #065F46;">
          🔒 Fully compliant with Indian Digital Personal Data Protection (DPDP) Act 2023 principles.
        </div>

      </div>

    </div>

  </div>
</body>
</html>"""

# -------------------------------------------------------------
# SLIDE 7: Technical Execution & Meko Regulatory Memory Proposal
# -------------------------------------------------------------
def generate_slide_7():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  {get_base_styles()}
</style>
</head>
<body>
  {get_chrome_decorations(7, 8, "Engineering Deliverables & Feature Proposal")}
  
  <div class="content-area" style="display: flex; flex-direction: column; justify-content: space-between;">
    
    <div>
      <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
        <span class="badge-blue">Innovation Proposal</span>
        <span style="font-size: 14px; font-weight: 600; color: #64748B;">Grounded feature specification addressing regulated enterprise domains</span>
      </div>
      <h2 style="font-size: 42px; font-weight: 800; color: #102653; letter-spacing: -1px;">
        Technical Execution & Regulatory Memory Proposal
      </h2>
      <p style="font-size: 16px; color: #475569; margin-top: 2px;">
        Pairing verified repository implementation with our feature proposal for Meko's next evolution.
      </p>
    </div>

    <!-- 2-Column Split: Build Evidence vs Proposal -->
    <div style="display: grid; grid-template-columns: 0.9fr 1.1fr; gap: 24px; margin: 12px 0;">
      
      <!-- Left: Repository Execution Evidence -->
      <div class="card" style="padding: 24px; display: flex; flex-direction: column; justify-content: space-between; border-left: 4px solid #102653;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="font-size: 16px; font-weight: 800; color: #102653;">Repository Build Deliverables</div>
            <span class="badge-navy">Branch: main</span>
          </div>

          <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 12px;">
            
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 12px;">
              <div style="font-size: 13px; font-weight: 700; color: #102653;">✓ Full-Stack Clean Architecture</div>
              <div style="font-size: 12px; color: #64748B; margin-top: 2px;">React 19 + TypeScript + FastAPI + async SQLAlchemy.</div>
            </div>

            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 12px;">
              <div style="font-size: 13px; font-weight: 700; color: #102653;">✓ YugabyteDB Distributed SQL Layer</div>
              <div style="font-size: 12px; color: #64748B; margin-top: 2px;">Tables for users, profiles, consent, refresh hashes & datapacks.</div>
            </div>

            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 12px;">
              <div style="font-size: 13px; font-weight: 700; color: #102653;">✓ Safety & Anti-Hallucination Guardrails</div>
              <div style="font-size: 12px; color: #64748B; margin-top: 2px;">Deterministic refusal to prescribe; antibiotic interceptors.</div>
            </div>

            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 12px;">
              <div style="font-size: 13px; font-weight: 700; color: #102653;">✓ Human Confirmation OCR Gate</div>
              <div style="font-size: 12px; color: #64748B; margin-top: 2px;">Interactive UI ensuring extracted salts are user-verified.</div>
            </div>

          </div>
        </div>

        <div style="font-size: 12px; color: #64748B;">
          Commits audited: <code>3b157a5</code> & <code>d1ae519</code>.
        </div>
      </div>

      <!-- Right: Proposed Meko Feature: Regulatory Memory Envelopes -->
      <div class="card" style="padding: 24px; background: #FFFFFF; border-left: 4px solid #087BFF; display: flex; flex-direction: column; justify-content: space-between;">
        
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="font-size: 16px; font-weight: 800; color: #102653;">Proposed Meko Feature: Regulatory Envelopes</div>
            <span class="badge-blue">Meko Roadmap Proposal</span>
          </div>

          <p style="font-size: 13px; color: #475569; margin-top: 6px;">
            In regulated domains (Healthcare, FinTech, Legal), memory cannot be a permanent, unverified key-value store. We propose native <strong>Regulatory Memory Envelopes</strong>:
          </p>

          <div style="margin-top: 14px; display: flex; flex-direction: column; gap: 12px;">
            
            <!-- Pillar 1 -->
            <div style="background: #EAF4FF; border: 1px solid #BFDBFE; border-radius: 8px; padding: 12px;">
              <div style="font-size: 13px; font-weight: 800; color: #087BFF;">1. Temporal TTL & Decay Policies</div>
              <div style="font-size: 12px; color: #1E40AF; margin-top: 2px;">
                Acute symptoms (e.g. fever, cough) auto-decay after 7–14 days to prevent stale hallucinations; chronic conditions (allergies, diabetes) persist permanently.
              </div>
            </div>

            <!-- Pillar 2 -->
            <div style="background: #ECFDF5; border: 1px solid #A7F3D0; border-radius: 8px; padding: 12px;">
              <div style="font-size: 13px; font-weight: 800; color: #059669;">2. Clinical Provenance Tiers</div>
              <div style="font-size: 12px; color: #065F46; margin-top: 2px;">
                Typed envelope metadata distinguishing <code>patient_reported (unverified)</code> from <code>clinician_verified</code> and <code>inferred_preference</code>.
              </div>
            </div>

            <!-- Pillar 3 -->
            <div style="background: #FFFBEB; border: 1px solid #FDE68A; border-radius: 8px; padding: 12px;">
              <div style="font-size: 13px; font-weight: 800; color: #D97706;">3. Cryptographic Deletion Receipts</div>
              <div style="font-size: 12px; color: #92400E; margin-top: 2px;">
                Ed25519-signed tombstone hashes returned on memory delete, providing mathematical proof of deletion for GDPR & DPDP Act compliance audits.
              </div>
            </div>

          </div>
        </div>

        <div style="font-size: 12px; color: #64748B;">
          Strategic Impact: Positions Meko as the preeminent agent memory platform for enterprise-regulated industries.
        </div>

      </div>

    </div>

  </div>
</body>
</html>"""

# -------------------------------------------------------------
# SLIDE 8: Proposed Pilot Measures, Impact & Roadmap
# -------------------------------------------------------------
def generate_slide_8():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  {get_base_styles()}
</style>
</head>
<body>
  {get_chrome_decorations(8, 8, "Target Pilot Measures & 3-Stage Roadmap")}
  
  <div class="content-area" style="display: flex; flex-direction: column; justify-content: space-between;">
    
    <div>
      <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
        <span class="badge-blue">Execution Roadmap</span>
        <span style="font-size: 14px; font-weight: 600; color: #64748B;">Defining rigorous target thresholds before claiming market impact</span>
      </div>
      <h2 style="font-size: 42px; font-weight: 800; color: #102653; letter-spacing: -1px;">
        Measure Safer Preparation Before Claiming Impact
      </h2>
      <p style="font-size: 16px; color: #475569; margin-top: 2px;">
        Honest, verifiable targets for our upcoming clinical usability pilot and system expansion.
      </p>
    </div>

    <!-- 4 Key Target Pilot Metrics Cards -->
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; margin: 12px 0;">
      
      <div class="card" style="padding: 20px; border-top: 4px solid #087BFF; text-align: center;">
        <div style="font-size: 11px; font-weight: 800; color: #087BFF; text-transform: uppercase;">Usability Target</div>
        <div style="font-size: 42px; font-weight: 800; color: #102653; margin: 8px 0;">≥ 80%</div>
        <div style="font-size: 13px; font-weight: 700; color: #102653;">Task Completion Rate</div>
        <div style="font-size: 12px; color: #64748B; margin-top: 4px;">Across first 10 patient & caregiver usability sessions.</div>
      </div>

      <div class="card" style="padding: 20px; border-top: 4px solid #059669; text-align: center;">
        <div style="font-size: 11px; font-weight: 800; color: #059669; text-transform: uppercase;">Efficiency Target</div>
        <div style="font-size: 42px; font-weight: 800; color: #059669; margin: 8px 0;">≤ 3 min</div>
        <div style="font-size: 13px; font-weight: 700; color: #102653;">Median Preparation Time</div>
        <div style="font-size: 12px; color: #64748B; margin-top: 4px;">From prescription image upload to reviewed salt list.</div>
      </div>

      <div class="card" style="padding: 20px; border-top: 4px solid #6366F1; text-align: center;">
        <div style="font-size: 11px; font-weight: 800; color: #6366F1; text-transform: uppercase;">Transparency Target</div>
        <div style="font-size: 42px; font-weight: 800; color: #6366F1; margin: 8px 0;">9 / 10</div>
        <div style="font-size: 13px; font-weight: 700; color: #102653;">Consent Comprehension</div>
        <div style="font-size: 12px; color: #64748B; margin-top: 4px;">Participants can clearly articulate data flows & opt-in.</div>
      </div>

      <div class="card" style="padding: 20px; border-top: 4px solid #D97706; text-align: center;">
        <div style="font-size: 11px; font-weight: 800; color: #D97706; text-transform: uppercase;">Safety Invariant</div>
        <div style="font-size: 42px; font-weight: 800; color: #D97706; margin: 8px 0;">0%</div>
        <div style="font-size: 13px; font-weight: 700; color: #102653;">Cross-User Leakage</div>
        <div style="font-size: 12px; color: #64748B; margin-top: 4px;">100% of memories trace to verified user-scoped datapacks.</div>
      </div>

    </div>

    <!-- 3-Stage Delivery Roadmap -->
    <div class="card" style="padding: 22px; background: #FFFFFF;">
      <div style="font-size: 15px; font-weight: 800; color: #102653; margin-bottom: 12px; display: flex; justify-content: space-between;">
        <span>3-Stage Delivery & Validation Roadmap</span>
        <span class="badge-blue">Next Milestones</span>
      </div>

      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;">
        
        <!-- Stage 1 -->
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 10px; padding: 14px;">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <span style="font-size: 11px; font-weight: 800; color: #087BFF;">STAGE 1 · IMMEDIATE</span>
            <span class="badge-green" style="font-size: 10px;">In Progress</span>
          </div>
          <div style="font-size: 14px; font-weight: 800; color: #102653; margin-top: 8px;">Hardening & Verification</div>
          <div style="font-size: 12px; color: #475569; margin-top: 6px; line-height: 1.4;">
            • Synchronize UI consent with chat runtime state.<br>
            • Enable strict TLS certificate validation for YugabyteDB.<br>
            • Complete pack-size comparability audit on catalogue.
          </div>
        </div>

        <!-- Stage 2 -->
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 10px; padding: 14px;">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <span style="font-size: 11px; font-weight: 800; color: #6366F1;">STAGE 2 · SHORT TERM</span>
            <span class="badge-blue" style="font-size: 10px;">Milestone</span>
          </div>
          <div style="font-size: 14px; font-weight: 800; color: #102653; margin-top: 8px;">Controlled Synthetic Demo</div>
          <div style="font-size: 12px; color: #475569; margin-top: 6px; line-height: 1.4;">
            • Execute live ON/OFF test with synthetic persona.<br>
            • Wire Context Inspection drawer with delete receipts.<br>
            • Verify zero cross-user recall across isolated datapacks.
          </div>
        </div>

        <!-- Stage 3 -->
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 10px; padding: 14px;">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <span style="font-size: 11px; font-weight: 800; color: #059669;">STAGE 3 · FIELD PILOT</span>
            <span class="badge-navy" style="font-size: 10px;">Expansion</span>
          </div>
          <div style="font-size: 14px; font-weight: 800; color: #102653; margin-top: 8px;">Partner Pilot & Localization</div>
          <div style="font-size: 12px; color: #475569; margin-top: 6px; line-height: 1.4;">
            • Onboard 10 opt-in Jan Aushadhi Kendras for response SLA.<br>
            • Conduct 10-patient usability study (zero PHI retained).<br>
            • Expand multilingual voice navigation (Hindi, Tamil, Marathi).
          </div>
        </div>

      </div>
    </div>

  </div>
</body>
</html>"""

# Generate and assemble PowerPoint
def generate_pptx(image_paths, output_path):
    from pptx import Presentation
    from pptx.util import Inches

    prs = Presentation()
    # 16:9 Aspect ratio: 13.333 x 7.5 inches
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6] # Blank slide layout

    for img_path in image_paths:
        slide = prs.slides.add_slide(blank_layout)
        slide.shapes.add_picture(str(img_path), 0, 0, width=prs.slide_width, height=prs.slide_height)

    prs.save(str(output_path))
    print(f"[OK] PowerPoint saved successfully to: {output_path}")

# Generate interactive viewer HTML
def generate_presentation_viewer(image_filenames):
    cards_html = ""
    for idx, fname in enumerate(image_filenames, 1):
        cards_html += f"""
        <div class="slide-card" id="slide-{idx}" onclick="setSlide({idx})">
          <div class="slide-thumb-header">Slide {idx:02d}</div>
          <img src="{fname}" alt="Slide {idx}" loading="lazy" />
        </div>
        """

    viewer_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MedEasy — HackCBS 9.0 Presentation Deck (Team axioms)</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=JetBrains+Mono:wght@600&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background: #0B132B;
    color: #FFFFFF;
    font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
    display: flex;
    flex-direction: column;
    height: 100vh;
    overflow: hidden;
  }}
  header {{
    height: 56px;
    background: #102653;
    border-bottom: 1px solid #1E3A8A;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 24px;
    flex-shrink: 0;
  }}
  .brand {{
    display: flex;
    align-items: center;
    gap: 12px;
    font-weight: 800;
    font-size: 18px;
  }}
  .controls {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  button {{
    background: #087BFF;
    border: none;
    color: white;
    padding: 6px 14px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 700;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 6px;
    transition: background 0.2s;
  }}
  button:hover {{ background: #0066D6; }}
  button.secondary {{
    background: #1E293B;
    border: 1px solid #334155;
  }}
  button.secondary:hover {{ background: #334155; }}
  .main-stage {{
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 16px;
    background: #050B14;
    position: relative;
  }}
  .slide-viewport {{
    width: 100%;
    max-width: 1400px;
    aspect-ratio: 16 / 9;
    box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.8), 0 0 0 1px rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    overflow: hidden;
    position: relative;
  }}
  .slide-viewport img {{
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
    background: #FFFFFF;
  }}
  .thumb-bar {{
    height: 120px;
    background: #0F172A;
    border-top: 1px solid #1E293B;
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 0 24px;
    overflow-x: auto;
    flex-shrink: 0;
  }}
  .slide-card {{
    width: 160px;
    aspect-ratio: 16 / 9;
    background: #1E293B;
    border-radius: 6px;
    overflow: hidden;
    cursor: pointer;
    border: 2px solid transparent;
    transition: all 0.2s;
    position: relative;
    flex-shrink: 0;
  }}
  .slide-card.active {{
    border-color: #087BFF;
    transform: scale(1.04);
  }}
  .slide-card img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .slide-thumb-header {{
    position: absolute;
    bottom: 2px;
    left: 4px;
    background: rgba(0,0,0,0.7);
    color: white;
    font-size: 10px;
    font-weight: 700;
    padding: 1px 6px;
    border-radius: 4px;
  }}
  .counter {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: #94A3B8;
  }}
</style>
</head>
<body>
  <header>
    <div class="brand">
      <span style="color: #087BFF;">MedEasy</span>
      <span style="font-size: 13px; font-weight: 600; color: #94A3B8;">| HackCBS 9.0 · Open Innovation & YugabyteDB Track · Team axioms</span>
    </div>
    <div class="controls">
      <span class="counter" id="counter">Slide 01 of {len(image_filenames):02d}</span>
      <button class="secondary" onclick="prevSlide()">◀ Prev</button>
      <button class="secondary" onclick="nextSlide()">Next ▶</button>
      <button onclick="toggleFullscreen()">⛶ Fullscreen</button>
      <a href="MedEasy_HackCBS9_Deck.pptx" download style="text-decoration: none;">
        <button style="background: #059669;">📥 Download .PPTX</button>
      </a>
    </div>
  </header>

  <div class="main-stage">
    <div class="slide-viewport" id="viewport">
      <img id="current-slide" src="{image_filenames[0]}" alt="Slide Presentation View" />
    </div>
  </div>

  <div class="thumb-bar">
    {cards_html}
  </div>

  <script>
    const images = {image_filenames};
    let currentIndex = 0;

    function updateView() {{
      document.getElementById('current-slide').src = images[currentIndex];
      document.getElementById('counter').innerText = `Slide ${{String(currentIndex + 1).padStart(2, '0')}} of ${{String(images.length).padStart(2, '0')}}`;
      
      document.querySelectorAll('.slide-card').forEach((card, idx) => {{
        if (idx === currentIndex) {{
          card.classList.add('active');
          card.scrollIntoView({{ behavior: 'smooth', inline: 'center', block: 'nearest' }});
        }} else {{
          card.classList.remove('active');
        }}
      }});
    }}

    function nextSlide() {{
      if (currentIndex < images.length - 1) {{
        currentIndex++;
        updateView();
      }}
    }}

    function prevSlide() {{
      if (currentIndex > 0) {{
        currentIndex--;
        updateView();
      }}
    }}

    function setSlide(num) {{
      currentIndex = num - 1;
      updateView();
    }}

    function toggleFullscreen() {{
      const elem = document.getElementById('viewport');
      if (!document.fullscreenElement) {{
        elem.requestFullscreen().catch(err => alert(err.message));
      }} else {{
        document.exitFullscreen();
      }}
    }}

    window.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') nextSlide();
      if (e.key === 'ArrowLeft' || e.key === 'PageUp') prevSlide();
      if (e.key === 'f' || e.key === 'F') toggleFullscreen();
    }});

    updateView();
  </script>
</body>
</html>"""
    return viewer_html

def main():
    print("=" * 60)
    print("MedEasy Presentation Slide Generator (HackCBS 9.0)")
    print("Track: Open Innovation & YugabyteDB Track | Team: axioms")
    print("=" * 60)

    slides = [
        ("slide_1.html", "slide_1.png", generate_slide_1()),
        ("slide_2.html", "slide_2.png", generate_slide_2()),
        ("slide_3.html", "slide_3.png", generate_slide_3()),
        ("slide_4.html", "slide_4.png", generate_slide_4()),
        ("slide_5.html", "slide_5.png", generate_slide_5()),
        ("slide_6.html", "slide_6.png", generate_slide_6()),
        ("slide_7.html", "slide_7.png", generate_slide_7()),
        ("slide_8.html", "slide_8.png", generate_slide_8()),
    ]

    png_paths = []
    png_filenames = []

    for html_name, png_name, html_content in slides:
        html_file = SLIDES_DIR / html_name
        png_file = SLIDES_DIR / png_name
        
        # Write HTML file
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"[HTML] Wrote: {html_file.name}")

        # Render HTML to 1920x1080 PNG via headless Chrome/Edge
        cmd = [
            CHROME_PATH,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--force-device-scale-factor=1",
            "--window-size=1920,1080",
            f"--screenshot={png_file}",
            str(html_file.resolve())
        ]
        
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode == 0 and png_file.exists():
            print(f"[PNG]  Rendered 1920x1080: {png_file.name} ({os.path.getsize(png_file) // 1024} KB)")
            png_paths.append(png_file)
            png_filenames.append(png_name)
        else:
            print(f"[ERR]  Failed to render {png_name}: {proc.stderr}")

    # Generate PPTX
    pptx_path = SLIDES_DIR / "MedEasy_HackCBS9_Deck.pptx"
    generate_pptx(png_paths, pptx_path)

    # Generate interactive presentation viewer
    viewer_html = generate_presentation_viewer(png_filenames)
    viewer_file = SLIDES_DIR / "index.html"
    with open(viewer_file, "w", encoding="utf-8") as f:
        f.write(viewer_html)
    print(f"[VIEWER] Interactive presentation viewer saved to: {viewer_file}")

    print("\n[SUCCESS] All 8 slides rendered in 16:9 widescreen format!")

if __name__ == "__main__":
    main()
