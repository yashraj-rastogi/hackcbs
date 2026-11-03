from pathlib import Path
from PIL import Image
from pptx import Presentation
from pptx.util import Inches
import sys

HERE = Path(__file__).parent
HERE.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(HERE.parent / "axioms-medeasy"))
import generate_slides as g

def feature_base(num, section, title, subtitle):
    im,d=g.base(num,section,title,subtitle,total=3)
    # Use the proposal label in the MVP's existing track badge.
    g.rounded(d,(1580,49,1915,101),g.PURPLE_PALE,22)
    g.txt(d,(1747,75),"MEKO FEATURE PROPOSAL",14,g.PURPLE,True,anchor="mm")
    return im,d

def slide1():
    im,d=feature_base(1,"Build friction  ·  Evidence from MedEasy","The context gap is real in our build","MedSaathi’s Meko path has code, but the current app flow does not yet preserve user-approved context end to end.")
    cards=[
      ("01","Context resets","Without a connected recall path, a new chat may not carry forward context the user already shared.","REPO EVIDENCE",g.BLUE,g.SKY),
      ("02","Consent splits","Privacy consent is stored through one route; chat checks a separate in-memory consent state.","REPO EVIDENCE",g.AMBER,g.AMBER_PALE),
      ("03","Control is missing","The memory panel has no live recalled items or correction/forget callbacks; deletion is queued, not remotely confirmed.","REPO EVIDENCE",g.RED,g.RED_PALE),
    ]
    for i,(n,title,body,badge,col,bg) in enumerate(cards):
        y=356+i*172
        g.card(d,(96,y,1215,y+143),g.WHITE,24)
        g.icon_circle(d,151,y+48,n,col,bg)
        g.txt(d,(205,y+24),title,24,g.NAVY,True)
        g.paragraph(d,205,y+63,body,735,20,g.MUTED,spacing=7)
        g.pill(d,970,y+90,badge,bg,col,14,12,30)
    # Evidence boundary and build datapack provenance
    g.card(d,(1260,356,1818,895),g.NAVY,26,g.NAVY)
    g.txt(d,(1302,398),"EVIDENCE BOUNDARY",18,"#AFCBFF",True)
    g.paragraph(d,1302,445,"Repository audit of MekoService, AI chat, privacy consent, and ContextPanel code.",450,22,g.WHITE,True,spacing=10)
    g.line if False else None
    d.line((1302,563,1776,563),fill="#38547E",width=2)
    g.txt(d,(1302,591),"Meko runtime status",19,"#AFCBFF",True)
    g.paragraph(d,1302,628,"Backend credentials/datapack are absent in the audited setup. No live MedEasy Meko trace was captured.",450,20,g.WHITE,spacing=8)
    g.pill(d,1302,747,"CODE-PATH EVIDENCE", "#203C68","#D5E4FA",14,12,31)
    g.pill(d,1302,792,"NOT A LIVE TEST RESULT", "#203C68","#D5E4FA",14,12,31)
    g.rounded(d,(96,900,1818,963),g.AMBER_PALE,17)
    g.txt(d,(122,931),"Build datapack: Axioms MedEasy HackCBS 9.0 holds project context; it does not currently contain live ON/OFF test traces.",18,g.AMBER,True,anchor="lm")
    return im

def slide2():
    im,d=feature_base(2,"The Meko feature  ·  Proposed interface","Proposal: consent-scoped, expiring health context","Use Meko’s datapacks and memory operations, with server-enforced consent and expiry rules at both write and recall.")
    # Meko vocabulary band
    terms=[
      ("DATAPACK","Isolation boundary"),
      ("MEMORY","User-approved fact"),
      ("SEARCH","Recall active context"),
      ("PROMOTION","Shared team knowledge"),
    ]
    for i,(a,b) in enumerate(terms):
        x=96+i*433
        g.card(d,(x,348,x+397,425),g.WHITE,18)
        g.txt(d,(x+18,368),a,15,g.BLUE,True)
        g.txt(d,(x+18,394),b,20,g.NAVY,True)
    # call / response proposal
    g.card(d,(96,455,1095,858),g.NAVY,25,g.NAVY)
    g.pill(d,128,481,"PROPOSED MCP EXTENSION · SYNTHETIC DATA", "#203C68","#C8D8F0",14,12,31)
    g.txt(d,(128,532),"memory_add(..., consent, expires_at)",25,g.WHITE,True)
    call='''memory_add(
  text="User reports asthma",
  datapack_id="patient-scoped-pack",
  consent={granted:true, scope:"medsaathi_context",
           basis:"explicit_user_approval"},
  expires_at="2026-12-01T00:00:00Z"
)'''
    d.rounded_rectangle((128,579,1061,827),radius=15,fill="#0A1A37")
    d.multiline_text((154,600),call,font=g.font(17),fill="#E4EEFF",spacing=4)
    # response card
    g.card(d,(1130,455,1818,858),g.WHITE,25)
    g.pill(d,1168,481,"EXAMPLE RESPONSE · PROPOSAL",g.GREEN_PALE,g.GREEN,14,12,31)
    g.txt(d,(1168,532),"Stored with a reviewable lifecycle",23,g.NAVY,True)
    response='''{
  "status": "stored",
  "memory_id": "…",
  "scope": "medsaathi_context",
  "expires_at": "2026-12-01T00:00:00Z",
  "visibility": "patient_datapack"
}'''
    d.rounded_rectangle((1168,579,1780,760),radius=15,fill="#F5F9FF",outline=g.LINE,width=1)
    d.multiline_text((1190,595),response,font=g.font(18),fill=g.NAVY,spacing=7)
    g.paragraph(d,1168,784,"memory_search returns only consented, unexpired items in the authorized user scope.",590,17,g.MUTED,spacing=5)
    g.rounded(d,(96,886,1818,963),g.PURPLE_PALE,18)
    g.txt(d,(122,911),"Keep health memory in a patient-scoped datapack. Promote only non-sensitive team learnings to collective memory.",19,g.PURPLE,True)
    g.txt(d,(122,941),"New value: typed policy enforced by Meko—not metadata that the caller must remember to honor.",16,g.NAVY,True)
    return im

def slide3():
    im,d=feature_base(3,"Scenario  ·  Novelty  ·  Risks","A continuity layer that stays under the user’s control","Synthetic scenario, not a live MedEasy result. The goal is less repetition and better follow-up—not automated clinical judgment.")
    # before / after
    g.card(d,(96,354,615,744),g.WHITE,25)
    g.pill(d,130,384,"BEFORE",g.AMBER_PALE,g.AMBER,15,13,34)
    g.txt(d,(130,445),"“I told you last time…”",25,g.NAVY,True)
    g.paragraph(d,130,502,"The next MedSaathi chat starts without the user-approved context. The person repeats details or the assistant asks again.",425,21,g.MUTED,spacing=9)
    g.rounded(d,(130,650,579,705),g.AMBER_PALE,15)
    g.txt(d,(150,677),"More repetition · context can be missed",16,g.AMBER,True,anchor="lm")
    g.card(d,(645,354,1170,744),g.WHITE,25)
    g.pill(d,679,384,"AFTER · PROPOSED",g.GREEN_PALE,g.GREEN,15,13,34)
    g.txt(d,(679,445),"Recall, then confirm",25,g.NAVY,True)
    g.paragraph(d,679,502,"With opt-in, retrieve a scoped, unexpired user-reported detail. MedSaathi says: “You previously shared this—does it still apply?”",430,20,g.MUTED,spacing=8)
    g.rounded(d,(679,650,1134,705),g.GREEN_PALE,15)
    g.txt(d,(700,677),"Relevant follow-up · user can correct or remove",15,g.GREEN,True,anchor="lm")
    # Novelty and safeguards
    g.card(d,(1200,354,1818,744),g.NAVY,25,g.NAVY)
    g.txt(d,(1238,388),"WHAT’S NEW",17,"#AFCBFF",True)
    g.paragraph(d,1238,426,"Meko already has datapacks and memory search. This proposal adds typed consent, expiry enforcement at recall, and a deletion receipt.",520,20,g.WHITE,True,spacing=8)
    d.line((1238,540,1778,540),fill="#38547E",width=2)
    g.txt(d,(1238,562),"RISKS → LIMITS",17,"#AFCBFF",True)
    risk_text="Stale facts → expiry + reconfirmation   ·   Privacy → save one approved fact, not raw chat   ·   Cross-user exposure → isolated datapack   ·   Abuse/cost → size limits, rate limits, audit trail"
    g.paragraph(d,1238,596,risk_text,520,17,"#E5EDFA",spacing=7)
    # guardrails footer
    g.rounded(d,(96,780,1818,955),g.PALE,22)
    g.txt(d,(132,809),"NON-NEGOTIABLE GUARDRAILS",17,g.BLUE,True)
    safeguards=[
      "Consent off = no save or recall",
      "Treat memory as user-reported, not verified",
      "No diagnosis or prescribing from memory",
      "User can inspect, correct, revoke, delete",
    ]
    for i,s in enumerate(safeguards):
        col=i%2; row=i//2; x=132+col*822; y=851+row*42
        g.dot(d,x,y+9,g.BLUE,5)
        g.txt(d,(x+20,y),s,18,g.NAVY,True)
    return im

def make_deck(images):
    prs=Presentation()
    prs.slide_width=Inches(13.333333)
    prs.slide_height=Inches(7.5)
    layout=prs.slide_layouts[6]
    for path in images:
        slide=prs.slides.add_slide(layout)
        slide.shapes.add_picture(str(path),0,0,width=prs.slide_width,height=prs.slide_height)
    out=HERE/"Axioms-MedEasy-Meko-Feature-Proposal.pptx"
    prs.save(out)
    return out

if __name__=="__main__":
    ims=[slide1(),slide2(),slide3()]
    paths=[]
    for i,im in enumerate(ims,1):
        p=HERE/f"slide-{i:02d}.png"
        im.save(p,optimize=True)
        paths.append(p)
    sheet=Image.new("RGB",(1312,1132),g.rgb("#EDF3FB"))
    for i,p in enumerate(paths):
        tile=Image.open(p).convert("RGB").resize((640,360),Image.Resampling.LANCZOS)
        sheet.paste(tile,(12+(i%2)*652,12+(i//2)*370))
    sheet.save(HERE/"contact-sheet.png",optimize=True)
    deck=make_deck(paths)
    print("Created:")
    print(deck)
    for p in paths: print(p)
