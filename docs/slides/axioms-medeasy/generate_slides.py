from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

OUT = Path(__file__).parent
OUT.mkdir(parents=True, exist_ok=True)
W, H = 1920, 1080

NAVY = "#102653"
BLUE = "#087BFF"
BLUE_DARK = "#0066D6"
SKY = "#EAF4FF"
PALE = "#F5F9FF"
MUTED = "#5B6B86"
LINE = "#DCE7F5"
PURPLE = "#7555E8"
PURPLE_PALE = "#F2EEFF"
GREEN = "#14875A"
GREEN_PALE = "#EAF8F1"
AMBER = "#A85A00"
AMBER_PALE = "#FFF4E5"
RED = "#B33C47"
RED_PALE = "#FFF0F1"
WHITE = "#FFFFFF"

FONT = "C:/Windows/Fonts/segoeui.ttf"
BOLD = "C:/Windows/Fonts/segoeuib.ttf"
ITALIC = "C:/Windows/Fonts/segoeuii.ttf"

def font(size, bold=False, italic=False):
    return ImageFont.truetype(ITALIC if italic else (BOLD if bold else FONT), size)

def rgb(hexcolor):
    h = hexcolor.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def canvas():
    im = Image.new("RGB", (W, H))
    pix = im.load()
    top, bot = rgb("#FFFFFF"), rgb("#F3F8FF")
    for y in range(H):
        t = y / (H - 1)
        c = tuple(round(top[i] * (1-t) + bot[i] * t) for i in range(3))
        for x in range(W):
            pix[x, y] = c
    return im, ImageDraw.Draw(im)

def rounded(draw, box, fill, radius=24, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def card(draw, box, fill=WHITE, radius=28, outline=LINE):
    x0,y0,x1,y1 = box
    draw.rounded_rectangle((x0+3,y0+7,x1+3,y1+7), radius=radius, fill="#EAF0F9")
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=2)

def txt(draw, xy, value, size=28, color=NAVY, bold=False, anchor=None, spacing=7, italic=False):
    draw.multiline_text(xy, value, font=font(size,bold,italic), fill=color, anchor=anchor, spacing=spacing)

def measure(draw, value, f):
    b = draw.textbbox((0,0), value, font=f)
    return b[2]-b[0]

def wrap(draw, text, f, max_width):
    words = text.split()
    lines, line = [], ""
    for word in words:
        candidate = word if not line else line + " " + word
        if measure(draw, candidate, f) <= max_width:
            line = candidate
        else:
            if line: lines.append(line)
            line = word
    if line: lines.append(line)
    return "\n".join(lines)

def paragraph(draw, x, y, text, width, size=27, color=MUTED, bold=False, spacing=9):
    f = font(size,bold)
    value = wrap(draw, text, f, width)
    draw.multiline_text((x,y), value, font=f, fill=color, spacing=spacing)
    return draw.multiline_textbbox((x,y), value, font=f, spacing=spacing)[3]

def pill(draw, x, y, label, fill=SKY, color=BLUE, size=19, pad_x=18, h=42, outline=None):
    f = font(size, True)
    tw = measure(draw,label,f)
    rounded(draw,(x,y,x+tw+pad_x*2,y+h),fill,20,outline=outline,width=1 if outline else 0)
    txt(draw,(x+pad_x,y+h//2),label,size,color,True,anchor="lm")
    return x+tw+pad_x*2

def dot(draw, x, y, color=BLUE, r=7):
    draw.ellipse((x-r,y-r,x+r,y+r),fill=color)

def base(slide, section, title, subtitle=None, total=8):
    im, d = canvas()
    # MVP identity: the plus-mark and compact app-like top bar
    rounded(d,(82,52,132,102),BLUE,15)
    txt(d,(107,76),"+",33,WHITE,True,anchor="mm")
    txt(d,(150,77),"Med",28,NAVY,True,anchor="lm")
    txt(d,(218,77),"Easy",28,BLUE,True,anchor="lm")
    pill(d,1338,55,"AXIOMS  ·  HACKCBS 9.0",WHITE,NAVY,17,18,40,LINE)
    pill(d,1640,55,"OPEN INNOVATION  /  YUGABYTE",SKY,BLUE,15,15,40)
    txt(d,(92,152),section.upper(),20,BLUE,True)
    txt(d,(92,191),title,53,NAVY,True,spacing=5)
    if subtitle:
        paragraph(d,94,265,subtitle,1640,24,MUTED,spacing=7)
    d.line((92,1012,1828,1012),fill=LINE,width=2)
    txt(d,(94,1035),"HEALTH TECH  ·  PRESCRIPTION REVIEW  ·  RESPONSIBLE AI",17,MUTED,True)
    txt(d,(1824,1035),f"{slide:02d}  /  {total:02d}",18,BLUE,True,anchor="ra")
    return im,d

def save(im, n):
    path=OUT/f"slide-{n:02d}.png"
    im.save(path,optimize=True)
    return path

def checkmark(draw,cx,cy,color=GREEN):
    draw.line((cx-9,cy,cx-2,cy+7,cx+12,cy-9),fill=color,width=4,joint="curve")

def icon_circle(draw,cx,cy,label,color=BLUE,bg=SKY):
    draw.ellipse((cx-30,cy-30,cx+30,cy+30),fill=bg)
    txt(draw,(cx,cy),label,23,color,True,anchor="mm")

def slide1():
    im,d=base(1,"HackCBS 9.0  ·  Health Tech","",None)
    txt(d,(96,185),"Med",94,NAVY,True)
    txt(d,(295,185),"Easy",94,BLUE,True)
    paragraph(d,101,315,"Make the next medication conversation easier to prepare.",700,41,NAVY,True,spacing=12)
    paragraph(d,101,445,"Prescription review, indicative price comparison, and pharmacy enquiry preparation.",690,27,MUTED,False,spacing=10)
    x=101
    x=pill(d,x,560,"PRESCRIPTION REVIEW",SKY,BLUE,17,17,42)+12
    x=pill(d,x,560,"PRICE COMPARISON",WHITE,NAVY,17,17,42,LINE)+12
    pill(d,x,560,"PHARMACY ENQUIRY",PURPLE_PALE,PURPLE,17,17,42)
    card(d,(95,680,794,900),WHITE,24)
    txt(d,(128,715),"TEAM AXIOMS",18,BLUE,True)
    txt(d,(128,754),"Yashraj Rastogi  ·  Team Lead",27,NAVY,True)
    txt(d,(128,798),"Amarpit Srivastav  ·  Member",25,MUTED)
    txt(d,(128,850),"Open Innovation  /  YugaByte Track",22,NAVY,True)
    # App-style preview panel, explicitly labeled as a conceptual synthetic workflow
    card(d,(940,145,1793,923),WHITE,34)
    rounded(d,(940,145,1793,215),NAVY,34)
    d.rectangle((940,181,1793,215),fill=NAVY)
    for i,c in enumerate((RED,"#E7B74A",GREEN)):
        d.ellipse((972+i*28,172,986+i*28,186),fill=c)
    txt(d,(1090,180),"MedEasy  /  Review workspace",20,WHITE,True,anchor="lm")
    pill(d,1512,160,"SYNTHETIC PREVIEW",PURPLE_PALE,PURPLE,14,12,31)
    txt(d,(1000,258),"Your next step",17,MUTED,True)
    txt(d,(1000,292),"Review before you compare",34,NAVY,True)
    paragraph(d,1000,345,"Confirm extracted items first. You stay in control of what gets shared.",660,22,MUTED)
    # progress strip
    steps=[("01","Upload",BLUE),("02","Review",BLUE),("03","Compare", "#A8B9D0")]
    for i,(num,label,col) in enumerate(steps):
        xx=1015+i*245
        icon_circle(d,xx+22,456,num,col,SKY if col==BLUE else "#F0F3F8")
        txt(d,(xx+63,456),label,21,NAVY if col==BLUE else MUTED,True,anchor="lm")
        if i<2:d.line((xx+132,456,xx+210,456),fill=LINE,width=4)
    card(d,(995,515,1738,634),PALE,20,PALE)
    rounded(d,(1018,540,1080,603),WHITE,14,LINE,2)
    txt(d,(1049,571),"Rx",21,BLUE,True,anchor="mm")
    txt(d,(1104,540),"Prescription image",22,NAVY,True)
    txt(d,(1104,576),"Awaiting human review",18,MUTED)
    pill(d,1530,549,"REVIEW FIRST",AMBER_PALE,AMBER,15,14,38)
    card(d,(995,658,1738,795),WHITE,20)
    txt(d,(1022,684),"Price list",20,NAVY,True)
    paragraph(d,1022,724,"Indicative catalogue data · pack size/source not fully verified",600,18,MUTED)
    pill(d,1515,697,"NOT A LIVE QUOTE",SKY,BLUE,14,12,34)
    rounded(d,(995,818,1738,876),GREEN_PALE,16)
    txt(d,(1021,847),"A preparation tool — it does not diagnose or prescribe.",19,GREEN,True,anchor="lm")
    return save(im,1)

def slide2():
    im,d=base(2,"01  ·  The need","A prescription starts a chain of decisions","Patients and caregivers may still need to understand the list, compare options, and confirm availability.")
    # Four-step patient journey
    labels=[("01","UNDERSTAND","Read and review the medicine list",BLUE,SKY),
            ("02","COMPARE","Check indicative options and prices",PURPLE,PURPLE_PALE),
            ("03","ASK","Contact a pharmacy to confirm supply",GREEN,GREEN_PALE),
            ("04","CARRY","Keep an accurate list between visits",AMBER,AMBER_PALE)]
    x0=93
    for i,(num,head,body,col,bg) in enumerate(labels):
        x=x0+i*438
        card(d,(x,365,x+394,625),WHITE,28)
        icon_circle(d,x+60,422,num,col,bg)
        txt(d,(x+34,478),head,20,col,True)
        paragraph(d,x+34,520,body,318,26,NAVY,True,spacing=8)
        if i<3:
            d.line((x+400,496,x+426,496),fill="#AFC5E2",width=4)
            d.polygon([(x+426,486),(x+442,496),(x+426,506)],fill="#AFC5E2")
    # Evidence context card
    card(d,(94,690,1040,932),NAVY,26,NAVY)
    txt(d,(132,728),"39.4%",67,WHITE,True)
    txt(d,(410,742),"of total health expenditure",25,WHITE,True)
    paragraph(d,410,785,"was household out-of-pocket expenditure in India’s National Health Accounts 2021–22.",520,22,"#D8E8FF")
    txt(d,(132,886),"Broad health-spending context · not medicine-specific · not MedEasy savings",16,"#C8D8F0",True)
    # Validation caveat
    card(d,(1090,690,1818,932),WHITE,26)
    pill(d,1130,726,"WHAT WE HAVE NOT VALIDATED",AMBER_PALE,AMBER,16,15,38)
    paragraph(d,1130,790,"These workflow needs are a product hypothesis. No patient interviews or usability study were found in the project evidence.",620,24,NAVY,True,spacing=10)
    txt(d,(1130,888),"Next: observe real tasks with patients and caregivers.",18,MUTED,True)
    txt(d,(95,963),"Sources: MoHFW National Health Accounts 2021–22 · WHO medication transitions guidance",17,MUTED)
    return save(im,2)

def slide3():
    im,d=base(3,"02  ·  Who it is for","Start with the patient and caregiver workflow","An initial hypothesis to test—not a validated persona.")
    # Persona
    card(d,(96,350,790,905),WHITE,30)
    pill(d,136,386,"INITIAL USER HYPOTHESIS",SKY,BLUE,16,15,38)
    icon_circle(d,178,506,"+",BLUE,SKY)
    txt(d,(235,478),"Patient or caregiver",34,NAVY,True)
    paragraph(d,138,565,"Managing recurring medication and preparing for a pharmacy or care conversation.",575,28,MUTED,False,spacing=12)
    d.line((138,688,745,688),fill=LINE,width=2)
    txt(d,(138,722),"Needs to be explored",18,BLUE,True)
    for j,s in enumerate(["Can they review an extracted list confidently?","Are comparisons genuinely like-for-like?","Do they understand AI and memory consent?"]):
        yy=771+j*43; dot(d,151,yy+10,BLUE,6); txt(d,(173,yy),s,20,NAVY)
    # Study plan
    card(d,(839,350,1818,905),WHITE,30)
    pill(d,879,386,"PROPOSED VALIDATION",PURPLE_PALE,PURPLE,16,15,38)
    txt(d,(879,455),"8–10",55,NAVY,True)
    txt(d,(1056,476),"patients / caregivers",23,MUTED,True)
    txt(d,(1390,455),"3",55,NAVY,True)
    txt(d,(1440,476),"pharmacy / health workers",21,MUTED,True)
    d.line((879,535,1775,535),fill=LINE,width=2)
    txt(d,(879,570),"Observe five tasks",23,NAVY,True)
    tasks=["Review an extracted medicine list","Compare a verified equivalent","Prepare an availability enquiry","Explain what goes to Gemini vs Meko","Correct or remove saved context"]
    for j,s in enumerate(tasks):
        yy=628+j*48
        icon_circle(d,901,yy+12,str(j+1),BLUE,SKY)
        txt(d,(947,yy),s,21,NAVY)
    rounded(d,(879,855,1775,887),AMBER_PALE,13)
    txt(d,(900,871),"Study notes: anonymized; do not retain participants’ health details.",16,AMBER,True,anchor="lm")
    return save(im,3)

def slide4():
    im,d=base(4,"03  ·  The product","One workflow to prepare, review, and ask","Prototype status is shown explicitly; seeded data and code paths are not live service evidence.")
    # 5-step workflow
    stages=[
        ("01","UPLOAD","Prescription\nimage or PDF","CODE PATH",BLUE,SKY),
        ("02","REVIEW","Human checks\nextracted items","IN APP",GREEN,GREEN_PALE),
        ("03","COMPARE","Catalogue prices\nare indicative","DATA GAP",AMBER,AMBER_PALE),
        ("04","PREPARE","User sends\nWhatsApp enquiry","HANDOFF",PURPLE,PURPLE_PALE),
        ("05","ASK","MedSaathi\nAI guidance","LIVE UNVERIFIED",BLUE,SKY),
    ]
    for i,(n,h,b,status,c,bg) in enumerate(stages):
        x=94+i*352
        card(d,(x,370,x+315,624),WHITE,25)
        icon_circle(d,x+50,420,n,c,bg)
        txt(d,(x+30,472),h,19,c,True)
        txt(d,(x+30,510),b,25,NAVY,True,spacing=8)
        pill(d,x+30,574,status,bg,c,14,12,32)
        if i<4:
            d.line((x+319,497,x+340,497),fill="#AFC5E2",width=4)
            d.polygon([(x+340,488),(x+353,497),(x+340,506)],fill="#AFC5E2")
    # Status rail
    card(d,(95,676,1818,930),NAVY,26,NAVY)
    txt(d,(132,712),"DEMO LIMITS",18,"#AFCBFF",True)
    cols=[
        ("Price","Not a live quote; pack sizes and sources are incomplete."),
        ("Pharmacy","Seeded listings; call to confirm. No live stock."),
        ("Safety","CDSCO records require review. No match ≠ safe."),
        ("Meko","Code exists; app is unconfigured and not demo-ready."),
    ]
    for i,(head,body) in enumerate(cols):
        x=132+i*420
        if i: d.line((x-27,750,x-27,887),fill="#334B72",width=2)
        txt(d,(x,765),head,23,WHITE,True)
        paragraph(d,x,808,body,350,19,"#D7E3F5",spacing=7)
    return save(im,4)

def slide5():
    im,d=base(5,"04  ·  Optional Meko context","Meko ON/OFF is a design intent—not a live app demo","The MedEasy backend is not configured for Meko, and its current consent and memory UI paths do not connect end to end.")
    # OFF / ON cards
    card(d,(94,354,882,758),WHITE,30)
    pill(d,134,392,"OFF",GREEN_PALE,GREEN,18,17,40)
    txt(d,(134,468),"No memory context",36,NAVY,True)
    paragraph(d,134,528,"Expected behavior: no Meko recall, logging, or memory write when consent is off.",670,26,MUTED,spacing=11)
    rounded(d,(134,667,838,715),GREEN_PALE,16)
    txt(d,(157,691),"Required proof: trace shows zero Meko calls.",18,GREEN,True,anchor="lm")
    card(d,(924,354,1818,758),WHITE,30)
    pill(d,964,392,"ON · INTENDED",PURPLE_PALE,PURPLE,18,17,40)
    txt(d,(964,468),"Review before use",36,NAVY,True)
    paragraph(d,964,528,"With explicit consent: retrieve a relevant item, show its exact text and source, then let the person correct or remove it.",765,26,MUTED,spacing=11)
    rounded(d,(964,667,1774,715),PURPLE_PALE,16)
    txt(d,(987,691),"Required proof: real synthetic result + edit/delete + OFF case.",17,PURPLE,True,anchor="lm")
    # Blocker banner
    rounded(d,(95,808,1818,938),RED_PALE,24)
    icon_circle(d,150,873,"!",RED,WHITE)
    txt(d,(205,832),"CURRENT STATUS: BLOCKED",20,RED,True)
    paragraph(d,205,872,"No backend Meko credentials/datapack; consent routes are disconnected; memory panel has no live items or correction/delete callbacks. Do not show scripted output as a real retrieval.",1515,21,NAVY,True,spacing=8)
    return save(im,5)

def slide6():
    im,d=base(6,"05  ·  Architecture & privacy","Separate identity, AI processing, and optional memory","Current code paths, not a claim of production deployment.")
    # app flow top
    card(d,(96,355,454,493),WHITE,24)
    icon_circle(d,148,424,"U",BLUE,SKY)
    txt(d,(194,393),"Patient device",22,NAVY,True)
    txt(d,(194,430),"React / Vite",19,MUTED)
    card(d,(548,355,925,493),WHITE,24)
    icon_circle(d,603,424,"API",BLUE,SKY)
    txt(d,(655,393),"MedEasy backend",22,NAVY,True)
    txt(d,(655,430),"FastAPI",19,MUTED)
    d.line((454,424,540,424),fill=BLUE,width=5)
    d.polygon([(540,414),(555,424),(540,434)],fill=BLUE)
    # downstream cards
    targets=[
        (1020,330,1428,518,"Gemini","Hosted extraction + chat",BLUE,SKY),
        (1490,330,1818,518,"YugaByteDB","Account + metadata",GREEN,GREEN_PALE),
        (1020,576,1428,764,"Meko MCP","Optional; unconfigured",PURPLE,PURPLE_PALE),
        (1490,576,1818,764,"Pharmacy","User-controlled handoff",AMBER,AMBER_PALE),
    ]
    for x0,y0,x1,y1,h,b,c,bg in targets:
        card(d,(x0,y0,x1,y1),WHITE,22)
        icon_circle(d,x0+48,y0+51,h[0],c,bg)
        txt(d,(x0+92,y0+31),h,22,NAVY,True)
        paragraph(d,x0+28,y0+108,b,x1-x0-55,18,MUTED,spacing=6)
    # connectors from backend
    for y_end in (424,670):
        d.line((925,424,974,424),fill="#8BB4EA",width=4)
        if y_end!=424:
            d.line((974,424,974,y_end),fill="#8BB4EA",width=4)
        d.line((974,y_end,1010,y_end),fill="#8BB4EA",width=4)
        d.polygon([(1010,y_end-8),(1023,y_end),(1010,y_end+8)],fill="#8BB4EA")
        d.line((974,y_end,1480,y_end),fill="#8BB4EA",width=4)
        d.polygon([(1480,y_end-8),(1493,y_end),(1480,y_end+8)],fill="#8BB4EA")
    # privacy ribbon
    rounded(d,(96,816,1818,938),NAVY,23)
    txt(d,(132,844),"PRIVACY FACTS FROM THE AUDIT",17,"#AFCBFF",True)
    statements=[
        "No persistent local health vault found.",
        "Meko consent can log full chat turns.",
        "No per-patient datapack routing shown.",
        "Deletion is queued, not confirmed remote.",
    ]
    for i,s in enumerate(statements):
        x=132+(i%2)*826; y=882+(i//2)*31
        dot(d,x,y+9,"#86B9FF",5)
        txt(d,(x+18,y),s,17,WHITE,True)
    return save(im,6)

def slide7():
    im,d=base(7,"06  ·  What is built / what is next","A working prototype, with evidence gaps made visible","YugaByte Track framing: the repository uses a PostgreSQL-compatible YugaByte database for account and consent metadata.")
    # Left: built
    card(d,(96,356,878,906),WHITE,28)
    pill(d,136,392,"IN THE REPOSITORY",GREEN_PALE,GREEN,16,15,38)
    items=[
        ("Frontend","React 19 · Vite · TypeScript"),
        ("Backend","FastAPI · SQLAlchemy async"),
        ("Database","YugaByte-compatible PostgreSQL"),
        ("AI paths","Gemini extraction and chat code"),
        ("Meko","MCP client and memory code paths"),
    ]
    for i,(head,body) in enumerate(items):
        y=470+i*78
        icon_circle(d,163,y+12,"✓",GREEN,GREEN_PALE)
        txt(d,(210,y-9),head,19,MUTED,True)
        txt(d,(210,y+19),body,22,NAVY,True)
    rounded(d,(136,860,836,887),AMBER_PALE,12)
    txt(d,(151,873),"Code presence does not prove a live integration.",15,AMBER,True,anchor="lm")
    # Right: proposal
    card(d,(924,356,1818,906),WHITE,28)
    pill(d,964,392,"PROPOSED · NOT CURRENT",PURPLE_PALE,PURPLE,16,15,38)
    txt(d,(964,458),"Consent-aware Meko memory lifecycle",30,NAVY,True)
    paragraph(d,964,510,"Make memory capture and recall traceable to a clear user choice.",735,22,MUTED)
    lifecycle=[
        ("01","Scope","Record what the person approved."),
        ("02","Provenance","Attach source and capture time."),
        ("03","Expiry","Filter expired items at recall."),
        ("04","Delete","Confirm remote removal before saying done."),
    ]
    for i,(num,head,body) in enumerate(lifecycle):
        col=i%2; row=i//2; x=964+col*405; y=603+row*116
        rounded(d,(x,y,x+365,y+94),PALE,18,LINE)
        pill(d,x+16,y+14,num,SKY,BLUE,14,10,29)
        txt(d,(x+70,y+14),head,19,NAVY,True)
        paragraph(d,x+16,y+51,body,330,16,MUTED,spacing=5)
    rounded(d,(964,842,1778,884),RED_PALE,13)
    txt(d,(983,863),"Before a Meko demo: configure, isolate users, wire consent, prove deletion.",16,RED,True,anchor="lm")
    return save(im,7)

def slide8():
    im,d=base(8,"07  ·  Impact & next steps","Measure safer preparation before claiming impact","No product KPIs, savings, pharmacy response rates, or clinical outcomes are measured yet.")
    # metrics
    card(d,(96,354,1138,928),WHITE,28)
    pill(d,136,390,"PROPOSED PILOT TARGETS",SKY,BLUE,16,15,38)
    metrics=[
        ("≥80%","task completion in first 10 target-user sessions"),
        ("≤3 min","median upload-to-reviewed-list time"),
        ("9 / 10","participants explain Gemini vs Meko consent"),
        ("100%","displayed memories trace to real results"),
    ]
    for i,(val,label) in enumerate(metrics):
        col=i%2; row=i//2; x=136+col*485; y=466+row*182
        rounded(d,(x,y,x+445,y+145),PALE,22,PALE)
        txt(d,(x+24,y+22),val,44,BLUE if i<2 else PURPLE,True)
        paragraph(d,x+25,y+80,label,395,19,NAVY,True,spacing=6)
    txt(d,(136,858),"Also measure: 0 cross-user recall · pharmacy reply baseline · comparable-price coverage",17,MUTED,True)
    # roadmap
    card(d,(1180,354,1818,928),NAVY,28,NAVY)
    txt(d,(1223,393),"NEXT",18,"#AFCBFF",True)
    steps=[
        ("01","READY","Fix consent + user routing; replace sensitive sample asset."),
        ("02","DEMO","Use synthetic data; prove Meko ON/OFF and deletion."),
        ("03","PILOT","Run patient/pharmacy sessions; publish measured results."),
    ]
    for i,(num,head,body) in enumerate(steps):
        y=465+i*145
        icon_circle(d,1260,y+23,num,"#FFFFFF","#25416E")
        txt(d,(1312,y),head,19,"#AFCBFF",True)
        paragraph(d,1312,y+36,body,430,19,WHITE,True,spacing=7)
        if i<2:d.line((1260,y+58,1260,y+127),fill="#43618F",width=3)
    rounded(d,(1223,884,1774,914),"#203C68",14)
    txt(d,(1242,899),"Every number shown here is a target, not a result.",16,WHITE,True,anchor="lm")
    return save(im,8)

def contact_sheet(paths):
    thumb_w,thumb_h=640,360
    gap=24; margin=32
    im=Image.new("RGB",(margin*2+thumb_w*2+gap,margin*2+thumb_h*4+gap*3),rgb("#EDF3FB"))
    for i,p in enumerate(paths):
        tile=Image.open(p).convert("RGB").resize((thumb_w,thumb_h),Image.Resampling.LANCZOS)
        x=margin+(i%2)*(thumb_w+gap)
        y=margin+(i//2)*(thumb_h+gap)
        im.paste(tile,(x,y))
    p=OUT/"contact-sheet.png"; im.save(p,optimize=True); return p

def make_powerpoint(paths):
    # The presentation is a full-bleed image deck: each slide is exactly its
    # matching 16:9 PNG, so fonts and layout remain consistent across systems.
    from pptx import Presentation
    from pptx.util import Inches
    prs=Presentation()
    prs.slide_width=Inches(13.333333)
    prs.slide_height=Inches(7.5)
    blank=prs.slide_layouts[6]
    for p in paths:
        slide=prs.slides.add_slide(blank)
        slide.shapes.add_picture(str(p),0,0,width=prs.slide_width,height=prs.slide_height)
    target=OUT/"Axioms-MedEasy-HackCBS9.pptx"
    prs.save(target)
    return target

if __name__=="__main__":
    paths=[slide1(),slide2(),slide3(),slide4(),slide5(),slide6(),slide7(),slide8()]
    contact_sheet(paths)
    make_powerpoint(paths)
    print("\n".join(str(p) for p in paths))
