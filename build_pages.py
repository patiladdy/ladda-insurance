import os
import os.path
OUT = os.path.dirname(os.path.abspath(__file__))

CDN_CSS = """<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/aos@2.3.4/dist/aos.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/glightbox@3.3.0/dist/css/glightbox.min.css">"""
CDN_JS = """<script src="https://unpkg.com/lucide@0.344.0/dist/umd/lucide.min.js"></script>
<script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/glightbox@3.3.0/dist/js/glightbox.min.js"></script>"""

SCHEMA = """<script type="application/ld+json">{"@context":"https://schema.org","@type":"InsuranceAgency","name":"Ladda Insurance","founder":"Kartik Poonamchand Ladda","slogan":"You Select, We Cover","telephone":["+91-9422681476","+91-9422460294"],"email":"kartikladda1111@gmail.com","address":{"@type":"PostalAddress","streetAddress":"Homkar Nagar, Bhavani Peth","addressLocality":"Solapur","addressRegion":"Maharashtra","addressCountry":"IN"},"areaServed":"Solapur","award":["Excellence Award FY 2025-26 – GM Club Star Advisor, National Insurance Co. Ltd., Pune Regional Office","First Double Crorepati with Premium – National Insurance Co. Ltd., Solapur Business Office"]}</script>"""

def page(fname, title, desc, page_key, body, root="", extra_js="", schema=False):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="{root}assets/img/kartik.jpg">
<meta name="theme-color" content="#0B2E6B">
<link rel="icon" type="image/png" href="{root}assets/img/shield.png">
{CDN_CSS}
<link rel="stylesheet" href="{root}assets/css/style.css">
{SCHEMA if schema else ""}
</head>
<body data-root="{root}" data-page="{page_key}">
<main id="main">
{body}
</main>
{CDN_JS}
{extra_js}
<script src="{root}assets/js/layout.js"></script>
<script src="{root}assets/js/main.js"></script>
</body>
</html>"""
    path = os.path.join(OUT, fname); os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(html)

# ---------------- shared fragments ----------------
SERVICES = [
  ("health","heart-pulse","o","Health Insurance","Cashless hospitalisation, family floaters, senior-citizen and super top-up plans.","family salaried senior"),
  ("life","shield-check","","Life & LIC Policies","Endowment, whole-life, money-back, child and pension plans including LIC.","family salaried senior"),
  ("term","umbrella","o","Term Insurance","High life cover at low premium to protect your family's future income.","family salaried"),
  ("motor","car","","Vehicle Insurance","Two-wheeler, car and commercial vehicle cover with zero-dep & add-ons.","family salaried business"),
  ("fire","flame","o","Fire & Factory Insurance","Protect buildings, machinery and stock against fire, flood and allied perils.","business"),
  ("shop","store","","Shop Insurance","One package for shop premises, stock, cash, burglary and liability.","business"),
  ("marine","ship","o","Marine Insurance","Transit cover for goods moving by road, rail, sea or air.","business"),
  ("home","home","","Home Insurance","Cover for your house structure and contents against fire, theft and disasters.","family senior"),
  ("mf","trending-up","o","Mutual Funds & SIP","Goal-based SIPs, lumpsum and SWP planning for wealth and retirement.","family salaried senior business"),
]
def service_cards(link=True, ids=False):
    out=[]
    for i,(k,ic,o,t,d,p) in enumerate(SERVICES):
        out.append(f"""<article class="card service-card" data-persona="{p}" {'id="'+k+'"' if ids else ''} data-aos="fade-up" data-aos-delay="{(i%3)*80}">
  <div class="ic {o}"><i data-lucide="{ic}"></i></div><h3>{t}</h3><p>{d}</p>
  {'<a class="link-arrow" href="services.html#'+k+'">Learn more <i data-lucide="arrow-right"></i></a>' if link else ''}</article>""")
    return "\n".join(out)

PARTNERS = [
  ("LIC","Life Insurance Corporation","Life","#0B4FA0","life"),
  ("NIC","National Insurance","General · PSU","#0E7490","general"),
  ("NIA","New India Assurance","General · PSU","#1D4ED8","general"),
  ("UII","United India Insurance","General · PSU","#1E3A8A","general"),
  ("OIC","Oriental Insurance","General · PSU","#B45309","general"),
  ("TA","Tata AIG","General","#1E40AF","general"),
  ("BG","Bajaj General","General","#0369A1","general"),
  ("IL","ICICI Lombard","General","#C2410C","general"),
  ("HE","HDFC ERGO","General & Health","#B91C1C","general health"),
  ("GD","Go Digit","General","#111827","general"),
  ("SH","Star Health","Health","#1E3A8A","health"),
  ("CH","Care Health","Health","#15803D","health"),
  ("NB","Niva Bupa","Health","#0F766E","health"),
  ("MC","ManipalCigna","Health","#EA580C","health"),
  ("ABH","Aditya Birla Health","Health","#B91C1C","health"),
  ("SBI","SBI Mutual Fund","Mutual Fund","#1D4ED8","mf"),
  ("HDFC","HDFC Mutual Fund","Mutual Fund","#1E3A8A","mf"),
  ("ICICI","ICICI Pru Mutual Fund","Mutual Fund","#9A3412","mf"),
  ("PPFAS","Parag Parikh MF","Mutual Fund","#334155","mf"),
  ("NIP","Nippon India MF","Mutual Fund","#B91C1C","mf"),
]
def partners_html():
    chips = """<div class="chips partner-tabs" data-filter-target="#partnerGrid">
<button class="chip active" data-filter="all" type="button">All</button><button class="chip" data-filter="life" type="button">Life</button>
<button class="chip" data-filter="general" type="button">General</button><button class="chip" data-filter="health" type="button">Health</button>
<button class="chip" data-filter="mf" type="button">Mutual Funds</button></div>"""
    items = "".join(f"""<div class="partner" data-persona="{c}"><span class="mono" style="background:{col}">{m}</span><div><b>{n}</b><small>{t}</small></div></div>""" for m,n,t,col,c in PARTNERS)
    return chips + f'<div class="partners" id="partnerGrid">{items}</div>'

AWARDS_SECTION = """
<section class="section awards" id="awards">
  <div class="container awards-grid">
    <div data-aos="fade-right">
      <span class="eyebrow"><i data-lucide="trophy"></i>Recognition</span>
      <h2>Honoured for excellence by <span class="text-orange">National Insurance</span></h2>
      <p>Clients trust Kartik because he delivers, and the insurer has recognised it too. These honours reflect years of honest advice and dependable service to families and businesses in Solapur.</p>
      <div class="award-list">
        <div class="award-item"><div class="ic"><i data-lucide="award"></i></div><div><h3>Excellence Award · FY 2025-26</h3><p>GM Club Star Advisor, for an outstanding contribution towards the success of NICL. Presented by Pune Regional Office.</p></div></div>
        <div class="award-item"><div class="ic"><i data-lucide="scroll-text"></i></div><div><h3>Certificate of Appreciation</h3><p>GM Club Star Agent, Solapur BO, Pune Region. For excellent performance in premium procurement during 2025-26.</p></div></div>
        <div class="award-item"><div class="ic"><i data-lucide="gem"></i></div><div><h3>First "Double Crorepati" with Premium</h3><p>The very first advisor to reach this milestone at National Insurance Co. Ltd., Solapur Business Office (271400).</p></div></div>
      </div>
    </div>
    <div class="award-photos" data-aos="fade-left">
      <a class="big glightbox" href="{R}assets/img/double-crorepati.jpg" data-gallery="awards" data-title="First Double Crorepati with Premium – NICL Solapur Business Office"><img src="{R}assets/img/double-crorepati.jpg" alt="Framed felicitation: First Double Crorepati with Premium, National Insurance Solapur" loading="lazy"><span class="cap">First Double Crorepati · NICL Solapur</span></a>
      <a class="glightbox" href="{R}assets/img/excellence-award.jpg" data-gallery="awards" data-title="Excellence Award FY 2025-26 & Certificate of Appreciation – NICL Pune Regional Office"><img src="{R}assets/img/excellence-award.jpg" alt="Excellence Award trophy and Certificate of Appreciation FY 2025-26" loading="lazy"><span class="cap">Excellence Award · FY 2025-26</span></a>
      <a class="glightbox" href="{R}assets/img/award-felicitation.jpg" data-gallery="awards" data-title="Star Performers felicitation – NICL Pune Regional Office"><img src="{R}assets/img/award-felicitation.jpg" alt="Kartik Ladda receiving the Excellence Award at the NICL Pune Regional Office felicitation" loading="lazy" style="object-position:70% center"><span class="cap">Star Performers felicitation · Pune RO</span></a>
    </div>
  </div>
</section>"""

GALLERY = """
<div class="gallery">
  <a class="glightbox" href="{R}assets/img/award-felicitation.jpg" data-gallery="honors" data-title="Advisors felicitation programme – NICL Pune Regional Office"><img src="{R}assets/img/award-felicitation.jpg" alt="Felicitation at NICL Pune Regional Office" loading="lazy"><span class="cap">Advisors felicitation · Pune Regional Office</span></a>
  <a class="glightbox" href="{R}assets/img/honor-office.jpg" data-gallery="honors" data-title="Felicitated at National Insurance Solapur Business Office"><img src="{R}assets/img/honor-office.jpg" alt="Kartik Ladda felicitated at the NICL Solapur Business Office" loading="lazy"><span class="cap">Felicitation · NICL Solapur BO</span></a>
  <a class="glightbox" href="{R}assets/img/honor-event.jpg" data-gallery="honors" data-title="Honoured with a memento at an industry meet"><img src="{R}assets/img/honor-event.jpg" alt="Kartik Ladda receiving a memento at an event" loading="lazy"><span class="cap">Honoured at an industry meet</span></a>
</div>"""

def cta(R=""):
    return f"""<section class="section" style="padding-top:0"><div class="container"><div class="cta-band" data-aos="zoom-in">
<div><h2>Not sure which plan is right for you?</h2><p>Get honest advice from Kartik. Compare plans from leading insurers with no pressure and no hidden charges.</p></div>
<div class="actions"><button class="btn btn-primary" data-quote type="button">Book Free Consultation</button><a class="btn btn-ghost" href="https://wa.me/919422681476" target="_blank" rel="noopener"><i data-lucide="message-circle"></i>WhatsApp</a></div>
</div></div></section>"""

CALC_TILES = [("emi","calculator","EMI Calculator","Monthly EMI for any loan"),("loan","landmark","Loan Eligibility","How much can you borrow"),
 ("sip","trending-up","SIP Calculator","Grow wealth with small steps"),("swp","wallet","SWP Calculator","Monthly income from funds"),
 ("term","shield-check","Term Cover","Right life cover for you"),("health","heart-pulse","Health Cover","Ideal family floater size"),
 ("lic","badge-indian-rupee","LIC Maturity","Estimate maturity value"),("irr","percent","Policy Return (IRR)","Real return of a policy"),
 ("lumpsum","piggy-bank","Lumpsum","One-time investment growth"),("retire","sunset","Retirement","Corpus & SIP you need")]
def calc_tiles(R=""):
    return "".join(f"""<a class="card calc-tile" href="{R}calculators.html#{k}" data-aos="fade-up" data-aos-delay="{(i%4)*60}"><div class="ic {'o' if i%2 else ''}"><i data-lucide="{ic}"></i></div><h3>{t}</h3><p class="muted">{d}</p></a>""" for i,(k,ic,t,d) in enumerate(CALC_TILES))

TESTIMONIALS = [  # REPLACE with genuine client reviews (with permission) before going live
 ("Client from Solapur","Health insurance","Kartik explained every clause of our family floater in simple Marathi and helped us with the cashless claim when my father was hospitalised."),
 ("Shop owner, Bhavani Peth","Shop insurance","He covered my shop, stock and cash in one policy at a fair premium. He visits for renewal personally every year."),
 ("Textile unit owner","Fire & marine insurance","Our factory and goods-in-transit are properly covered now. Quick response and complete paperwork support."),
 ("Salaried professional","Term + SIP","He showed me how much term cover I really needed and set up SIPs for my child's education. Very transparent."),
]
def testimonials():
    sl = "".join(f"""<div class="swiper-slide"><div class="testimonial"><i class="q" data-lucide="quote"></i><p>{q}</p><div class="who"><span class="avatar">{n[0]}</span><div><b>{n}</b><small>{t}</small></div></div></div></div>""" for n,t,q in TESTIMONIALS)
    return f"""<!-- NOTE: sample testimonials – replace with real client reviews --><div class="swiper t-swiper"><div class="swiper-wrapper">{sl}</div><div class="swiper-pagination"></div></div>"""

FAQ = [("Which insurance companies do you work with?","Kartik works with leading life, general and health insurers. These include LIC, National Insurance, New India Assurance, Star Health, Care Health, Tata AIG and more. He compares plans across them so you get the best fit, not just one company's product."),
("Do you help at the time of a claim?","Yes. Claim support is the most important part of the service. Kartik helps with documents, cashless approvals, surveys and follow-ups until the claim is settled."),
("Is there any extra charge for your advice?","No. You pay the premium charged by the insurance company. Consultation and comparison are free."),
("Can I buy a policy without visiting the office?","Yes. Most policies can be completed on WhatsApp with e-KYC and online payment. Home or shop visits are also available within Solapur."),
("Do you help with mutual fund SIPs?","Yes. Kartik helps you plan goal-based SIPs, lumpsum investments and SWPs for regular income. Mutual funds are subject to market risks.")]
def faq_html():
    return '<div class="faq">' + "".join(f"<details {'open' if i==0 else ''}><summary>{q}</summary><p>{a}</p></details>" for i,(q,a) in enumerate(FAQ)) + "</div>"

from blog_data import POSTS
def post_card(p, R=""):
    return f"""<a class="post-card" href="{R}blog/{p['slug']}.html" data-persona="{p['cat_key']}" data-aos="fade-up"><div class="post-thumb {p['theme']}"><i data-lucide="{p['icon']}"></i></div>
<div class="post-body"><div class="post-meta"><span class="tag {'o' if p['cat_key'] in ('investment',) else ''}">{p['cat']}</span><span>{p['read']} min read</span></div><h3>{p['title']}</h3><p>{p['excerpt']}</p><span class="link-arrow">Read more <i data-lucide="arrow-right"></i></span></div></a>"""

# ---------------- HOME ----------------
home = f"""
<section class="hero">
  <div class="container">
    <div class="hero-copy">
      <span class="eyebrow"><i data-lucide="map-pin"></i>Serving Solapur & nearby</span>
      <h1>Your Family's <span>Financial Shield</span> in Solapur</h1>
      <p class="lead">Every type of insurance, plus smart investments, from one trusted advisor. <b>You Select, We Cover.</b></p>
      <ul class="ticks"><li><i data-lucide="check"></i>Protect what you love</li><li><i data-lucide="check"></i>Plan your dreams</li><li><i data-lucide="check"></i>Grow your wealth</li><li><i data-lucide="check"></i>Full claim support</li></ul>
      <div class="hero-actions"><button class="btn btn-primary" data-quote type="button">Get a Free Quote <i data-lucide="arrow-right"></i></button>
      <a class="btn btn-wa" href="https://wa.me/919422681476?text=Hello%20Kartik%20ji%2C%20I%20need%20insurance%20advice." target="_blank" rel="noopener"><i data-lucide="message-circle"></i>Chat on WhatsApp</a></div>
    </div>
    <div class="hero-visual">
      
      <img class="person" src="assets/img/kartik.jpg" alt="Kartik Poonamchand Ladda, Insurance Advisor, Solapur" width="590" height="720">
      <div class="float-card fc1"><span class="ic"><i data-lucide="award"></i></span><div><strong>GM Club Star</strong>Advisor · FY 2025-26</div></div>
      <div class="float-card fc2"><span class="ic"><i data-lucide="gem"></i></span><div><strong>1st Double Crorepati</strong>NICL Solapur BO</div></div>
    </div>
  </div>
</section>

<section class="stats"><div class="container"><div class="stats-grid">
  <div class="stat"><span class="ic"><i data-lucide="trophy"></i></span><div><strong>Star Advisor</strong><span>GM Club · NICL Pune Region</span></div></div>
  <div class="stat"><span class="ic"><i data-lucide="building-2"></i></span><div><strong><span data-count="20" data-suffix="+">20+</span></strong><span>Insurer & AMC partners</span></div></div>
  <div class="stat"><span class="ic"><i data-lucide="layers"></i></span><div><strong><span data-count="9">9</span> Solutions</strong><span>Insurance & investments</span></div></div>
  <div class="stat"><span class="ic"><i data-lucide="headset"></i></span><div><strong>Claim Support</strong><span>From paperwork to settlement</span></div></div>
</div></div></section>

<section class="section" id="services"><div class="container">
  <div class="section-head"><div><span class="eyebrow">What we do</span><h2>Solutions for every stage of life</h2></div><p>Tell us who you are and we'll show the protection that matters most to you.</p></div>
  <div class="chips" data-filter-target="#svcGrid" role="group" aria-label="Filter services">
    <button class="chip active" data-filter="all" type="button">Everyone</button><button class="chip" data-filter="family" type="button">Family</button>
    <button class="chip" data-filter="salaried" type="button">Salaried</button><button class="chip" data-filter="business" type="button">Business Owner</button><button class="chip" data-filter="senior" type="button">Senior Citizen</button></div>
  <div class="grid g-3" id="svcGrid">{service_cards()}</div>
</div></section>

{AWARDS_SECTION.replace("{R}","")}

<section class="section soft"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Plan smarter</span><h2>Free financial calculators</h2></div><a class="link-arrow" href="calculators.html">View all calculators <i data-lucide="arrow-right"></i></a></div>
  <div class="grid g-5">{calc_tiles()}</div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Our partners</span><h2>We work with leading insurers & fund houses</h2></div><p>One advisor, many companies. You get unbiased comparisons and the best value for your needs.</p></div>
  {partners_html()}
  <p class="muted" style="font-size:.8rem;margin-top:1rem">Company names are trademarks of their respective owners and are shown to indicate products we can help you with.</p>
</div></section>

<section class="section cream"><div class="container">
  <div class="section-head center" style="flex-direction:column;align-items:center;text-align:center"><span class="eyebrow">How it works</span><h2>Covered in 3 simple steps</h2></div>
  <div class="steps">
    <div class="step" data-aos="fade-up"><div class="step-ic o"><i data-lucide="messages-square"></i></div><h3>Consult</h3><p class="muted">Share your needs on a call, on WhatsApp or in person. We understand your family, business and goals.</p></div>
    <div class="step" data-aos="fade-up" data-aos-delay="100"><div class="step-ic"><i data-lucide="scale"></i></div><h3>Compare</h3><p class="muted">We compare plans from multiple insurers for cover, exclusions, claim record and price, and explain everything simply.</p></div>
    <div class="step" data-aos="fade-up" data-aos-delay="200"><div class="step-ic o"><i data-lucide="badge-check"></i></div><h3>Covered & supported</h3><p class="muted">Paperless issuance, renewal reminders and personal support when you need to make a claim.</p></div>
  </div>
</div></section>

<section class="section soft"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Client stories</span><h2>What our clients say</h2></div></div>
  {testimonials()}
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Knowledge centre</span><h2>Latest blogs & insights</h2></div><a class="link-arrow" href="blog/index.html">View all blogs <i data-lucide="arrow-right"></i></a></div>
  <div class="grid g-3">{''.join(post_card(p) for p in POSTS[:3])}</div>
</div></section>

<section class="section soft"><div class="container">
  <div class="section-head center" style="flex-direction:column;align-items:center;text-align:center"><span class="eyebrow">FAQ</span><h2>Frequently asked questions</h2></div>
  {faq_html()}
</div></section>
<div style="height:3rem"></div>
{cta()}
"""
page("index.html","Ladda Insurance | Kartik Ladda – Insurance Advisor in Solapur",
 "Kartik Poonamchand Ladda: a trusted insurance advisor in Solapur for health, life, LIC, term, vehicle, fire, shop and marine insurance, plus mutual funds. You Select, We Cover.",
 "home", home, schema=True)

# ---------------- ABOUT ----------------
about = f"""
<section class="page-hero"><div class="container"><p class="breadcrumb"><a href="index.html">Home</a> / About</p><h1>About Kartik Ladda</h1><p>An insurance advisor who treats every client's family and business like his own.</p></div></section>
<section class="section"><div class="container about-grid">
  <div class="about-photo" data-aos="fade-right"><img src="assets/img/kartik.jpg" alt="Kartik Poonamchand Ladda" loading="lazy">
    <div class="badge"><i data-lucide="award"></i><b>GM Club Star Advisor<br><small class="muted">NICL · FY 2025-26</small></b></div></div>
  <div data-aos="fade-left">
    <span class="eyebrow">Insurance Advisor · Solapur</span>
    <h2>Kartik Poonamchand Ladda</h2>
    <p>Kartik founded <b>Ladda Insurance</b> with a simple promise: <b>You Select, We Cover.</b> From Homkar Nagar, Bhavani Peth, he advises families, salaried professionals, shop owners and manufacturers across Solapur on health, life, vehicle, fire, shop and marine insurance, and on long-term investing through mutual funds.</p>
    <p>His approach is personal. He explains policies in plain language, compares plans from several insurers, and stays with clients through renewals and claims. That consistency has made him one of the top advisors in the National Insurance Pune Region.</p>
    <div class="grid g-2" style="margin-top:1.5rem">
      <div class="card"><div class="ic o"><i data-lucide="target"></i></div><h3>Mission</h3><p>To make sure every family and business in Solapur is properly insured and financially prepared.</p></div>
      <div class="card"><div class="ic"><i data-lucide="eye"></i></div><h3>Values</h3><p>Transparency, the right cover over the costliest one, and support until the claim is settled.</p></div>
    </div>
  </div>
</div></section>
{AWARDS_SECTION.replace("{R}","")}
<section class="section"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Moments of pride</span><h2>Honours & felicitations</h2></div><p>Moments from felicitation programmes by National Insurance and from industry meets. Tap any photo to view it larger.</p></div>
  {GALLERY.replace("{R}","")}
</div></section>
<section class="section soft"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Why choose us</span><h2>The Ladda Insurance difference</h2></div></div>
  <div class="grid g-4">
    <div class="card"><div class="ic o"><i data-lucide="user-check"></i></div><h3>Client first</h3><p>Advice based on your needs, not on commissions.</p></div>
    <div class="card"><div class="ic"><i data-lucide="eye"></i></div><h3>Transparent</h3><p>Every exclusion, waiting period and clause explained.</p></div>
    <div class="card"><div class="ic o"><i data-lucide="building-2"></i></div><h3>Multiple insurers</h3><p>Compare LIC, PSU, private and health insurers in one place.</p></div>
    <div class="card"><div class="ic"><i data-lucide="headset"></i></div><h3>Claim support</h3><p>Personal help from intimation to settlement.</p></div>
  </div>
</div></section>
<div style="height:3rem"></div>{cta()}"""
page("about.html","About Kartik Ladda | Ladda Insurance Solapur","Meet Kartik Poonamchand Ladda, GM Club Star Advisor at National Insurance (FY 2025-26) and first Double Crorepati advisor at NICL Solapur.","about",about)

# ---------------- SERVICES ----------------
DETAIL = {
 "health":["Family floater & individual plans","Senior citizen health plans","Super top-up for high cover at low cost","Cashless claims at network hospitals","Tax benefit u/s 80D (old regime)"],
 "life":["LIC endowment, whole-life & money-back plans","Child education & marriage plans","Pension / annuity plans","Guaranteed + bonus-based options","Loan facility on traditional policies"],
 "term":["₹50 lakh to ₹5 crore+ cover","Critical illness & accidental riders","Return-of-premium options","Lowest cost per lakh of cover","Help with medicals and documentation"],
 "motor":["Comprehensive & third-party","Zero depreciation, engine protect, RSA","NCB transfer guidance","Commercial vehicles & fleets","Quick claim and survey coordination"],
 "fire":["Bharat Sookshma / Laghu Udyam policies","Building, plant, machinery & stock","Flood, earthquake & riot add-ons","Burglary & machinery breakdown","Loss of profit cover"],
 "shop":["Shopkeeper package policy","Stock, furniture & fittings","Cash in safe / in transit","Plate glass & signboards","Public liability"],
 "marine":["Single transit & open policies","Inland & import/export cargo","Textile, engineering & agro goods","All-risk or named perils","Claim survey support"],
 "home":["Building structure cover","Contents & valuables","Fire, theft, flood & earthquake","Bharat Griha Raksha policy","Affordable long-term plans"],
 "mf":["Goal-based SIP planning","Equity, hybrid & debt funds","ELSS tax-saving funds","SWP for monthly income","Periodic portfolio review"],
}
svc_blocks = ""
for i,(k,ic,o,t,d,p) in enumerate(SERVICES):
    lis = "".join(f"<li>{x}</li>" for x in DETAIL[k])
    interest = {"health":"Health Insurance","life":"Life Insurance / LIC Policy","term":"Term Insurance","motor":"Vehicle Insurance","fire":"Fire / Factory Insurance","shop":"Shop Insurance","marine":"Marine Insurance","home":"Home Insurance","mf":"Mutual Funds / SIP"}[k]
    svc_blocks += f"""<article class="card service-card" id="{k}" data-persona="{p}" data-aos="fade-up" style="scroll-margin-top:110px"><div class="ic {o}"><i data-lucide="{ic}"></i></div><h3>{t}</h3><p>{d}</p><ul>{lis}</ul>
<button class="btn btn-primary btn-sm" data-quote="{interest}" type="button">Get quote</button></article>"""
services = f"""
<section class="page-hero"><div class="container"><p class="breadcrumb"><a href="index.html">Home</a> / Services</p><h1>Complete protection. Greater possibilities.</h1><p>From your health to your shop, your car to your factory, and your SIP to your retirement, we've got you covered.</p></div></section>
<section class="section"><div class="container">
  <div class="chips" data-filter-target="#svcGrid2"><button class="chip active" data-filter="all" type="button">All</button><button class="chip" data-filter="family" type="button">Family</button><button class="chip" data-filter="salaried" type="button">Salaried</button><button class="chip" data-filter="business" type="button">Business</button><button class="chip" data-filter="senior" type="button">Senior Citizen</button></div>
  <div class="grid g-3" id="svcGrid2">{svc_blocks}</div>
</div></section>
<section class="section soft"><div class="container"><div class="section-head"><div><span class="eyebrow">Partners</span><h2>All leading insurers supported</h2></div></div>{partners_html()}</div></section>
<div style="height:3rem"></div>{cta()}"""
page("services.html","Insurance Services in Solapur | Ladda Insurance","Health, life, LIC, term, vehicle, fire, factory, shop, marine and home insurance plus mutual funds. Compare plans from all leading insurers with Kartik Ladda.","services",services)

# ---------------- CALCULATORS ----------------
calcs = """
<section class="page-hero"><div class="container"><p class="breadcrumb"><a href="index.html">Home</a> / Calculators</p><h1>Financial Calculators</h1><p>Plan better and live smarter. Work out EMIs, loan eligibility, SIP and SWP returns, term and health cover, and LIC maturity in seconds.</p></div></section>
<section class="section soft"><div class="container" id="calcApp">
  <div class="calc-tabs" role="tablist" aria-label="Calculators"></div>
  <div class="calc-panels"></div>
  <p class="disclaimer" style="margin-top:2rem">All calculators give indicative estimates for education and planning only. Mutual fund returns are not guaranteed. LIC bonus rates are declared annually by LIC. Insurance premiums and benefits are as per the insurer's terms. Please consult Kartik before making decisions.</p>
</div></section>
<div style="height:3rem"></div>""" + cta()
page("calculators.html","EMI, SIP, SWP, Loan, LIC & Insurance Calculators | Ladda Insurance","Free EMI, loan eligibility, SIP, lumpsum, SWP, retirement, term cover, health cover, LIC maturity and policy IRR calculators.","calculators",calcs,
 extra_js='<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>\n<script src="assets/js/calculators.js"></script>')

# ---------------- CONTACT ----------------
contact = """
<section class="page-hero"><div class="container"><p class="breadcrumb"><a href="index.html">Home</a> / Contact</p><h1>Let's talk about your goals</h1><p>Call, WhatsApp or drop by the office. Kartik will personally help you choose the right cover.</p></div></section>
<section class="section"><div class="container contact-grid">
  <div class="contact-list" data-aos="fade-right">
    <div class="contact-item"><span class="ic"><i data-lucide="phone"></i></span><div><b>Call us</b><a href="tel:+919422681476">+91 94226 81476</a><br><a href="tel:+919422460294">+91 94224 60294</a></div></div>
    <div class="contact-item"><span class="ic" style="background:#DCFCE7;color:#16A34A"><i data-lucide="message-circle"></i></span><div><b>WhatsApp</b><a href="https://wa.me/919422681476" target="_blank" rel="noopener">Chat with Kartik</a></div></div>
    <div class="contact-item"><span class="ic"><i data-lucide="mail"></i></span><div><b>Email</b><a href="mailto:kartikladda1111@gmail.com">kartikladda1111@gmail.com</a></div></div>
    <div class="contact-item"><span class="ic"><i data-lucide="map-pin"></i></span><div><b>Office</b>Homkar Nagar, Bhavani Peth,<br>Solapur, Maharashtra</div></div>
    <div class="contact-item"><span class="ic"><i data-lucide="clock"></i></span><div><b>Working hours</b>Mon–Sat · 10:00 AM – 7:00 PM<br><small class="muted">Sunday by appointment</small></div></div>
  </div>
  <div class="card" data-aos="fade-left" style="padding:2rem">
    <h2 style="font-size:1.6rem">Send a message</h2><p class="muted">Your details will open in WhatsApp, ready to send.</p>
    <form class="form js-wa-form">
      <div class="row"><div><label for="cName">Name</label><input id="cName" name="name" required autocomplete="name"></div><div><label for="cPhone">Mobile</label><input id="cPhone" name="phone" type="tel" inputmode="numeric" required autocomplete="tel"></div></div>
      <div><label for="cType">Service</label><select id="cType" name="interest"><option>Health Insurance</option><option>Life Insurance / LIC Policy</option><option>Term Insurance</option><option>Vehicle Insurance</option><option>Fire / Factory Insurance</option><option>Shop Insurance</option><option>Marine Insurance</option><option>Home Insurance</option><option>Mutual Funds / SIP</option><option>Claim Assistance</option></select></div>
      <div><label for="cMsg">Message</label><textarea id="cMsg" name="message"></textarea></div>
      <button class="btn btn-primary" type="submit"><i data-lucide="send"></i>Send Message</button>
    </form>
  </div>
</div>
<div class="container" style="margin-top:2rem"><iframe class="map" title="Ladda Insurance location – Bhavani Peth, Solapur" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=Homkar+Nagar,+Bhavani+Peth,+Solapur,+Maharashtra&output=embed"></iframe></div>
</section>"""
page("contact.html","Contact Kartik Ladda | Insurance Advisor Solapur","Call +91 94226 81476 or WhatsApp Kartik Ladda. Office at Homkar Nagar, Bhavani Peth, Solapur.","contact",contact)

# ---------------- BLOG ----------------
cats = [("all","All"),("health","Health"),("life","Life & LIC"),("investment","Investments"),("general","General Insurance")]
blog_index = f"""
<section class="page-hero"><div class="container"><p class="breadcrumb"><a href="../index.html">Home</a> / Blogs</p><h1>Insights for a brighter tomorrow</h1><p>Simple, practical guides on insurance, LIC policies and mutual funds, written for Solapur families and businesses.</p></div></section>
<section class="section"><div class="container">
  <div class="chips" data-filter-target="#postGrid">{''.join(f'<button class="chip {"active" if k=="all" else ""}" data-filter="{k}" type="button">{v}</button>' for k,v in cats)}</div>
  <div class="grid g-3" id="postGrid">{''.join(post_card(p,"../") for p in POSTS)}</div>
</div></section><div style="height:3rem"></div>{cta("../")}"""
page("blog/index.html","Blogs – Insurance, LIC & Mutual Fund Guides | Ladda Insurance","Guides on health insurance, LIC policies, term insurance, SIP, SWP, top mutual funds, and fire, shop, marine and motor insurance.","blog",blog_index,root="../")

for p in POSTS:
    others = [q for q in POSTS if q["slug"] != p["slug"]][:6]
    side = "".join(f'<li><a href="{q["slug"]}.html">{q["title"]}</a></li>' for q in others)
    body = f"""
<section class="article-hero"><div class="container"><p class="breadcrumb"><a href="../index.html">Home</a> / <a href="index.html">Blogs</a> / {p['cat']}</p>
<span class="tag">{p['cat']}</span><h1 style="margin-top:.8rem">{p['title']}</h1><p class="post-meta">By Kartik Ladda · {p['read']} min read · Updated October 2026</p></div></section>
<section class="section"><div class="container article-layout">
  <article class="prose">{p['body']}
  <div class="callout"><b>Need help choosing?</b> Kartik can compare options for you for free. <a href="https://wa.me/919422681476" style="color:var(--blue);font-weight:600" target="_blank" rel="noopener">WhatsApp now →</a></div>
  <p class="disclaimer">This article is for general awareness only and is not a recommendation to buy a specific product. Insurance is the subject matter of solicitation. Mutual fund investments are subject to market risks; read all scheme-related documents carefully. Tax benefits are as per prevailing laws and may change.</p></article>
  <aside class="sidebar">
    <div class="side-card dark"><img class="mini" src="../assets/img/kartik.jpg" alt="Kartik Ladda"><h3>Talk to Kartik</h3><p style="font-size:.92rem">GM Club Star Advisor. Free, honest advice for your family and business.</p>
      <div style="display:grid;gap:.5rem"><button class="btn btn-primary btn-sm" data-quote type="button">Get Free Quote</button><a class="btn btn-wa btn-sm" href="https://wa.me/919422681476" target="_blank" rel="noopener">WhatsApp</a></div></div>
    <div class="side-card"><h3>Try a calculator</h3><ul class="side-links"><li><a href="../calculators.html#sip">SIP Calculator</a></li><li><a href="../calculators.html#swp">SWP Calculator</a></li><li><a href="../calculators.html#lic">LIC Maturity Estimator</a></li><li><a href="../calculators.html#term">Term Cover Calculator</a></li><li><a href="../calculators.html#emi">EMI Calculator</a></li></ul></div>
    <div class="side-card"><h3>More articles</h3><ul class="side-links">{side}</ul></div>
  </aside>
</div></section>"""
    page(f"blog/{p['slug']}.html", p['title'] + " | Ladda Insurance", p['excerpt'], "blog", body, root="../")
print("built", len(POSTS), "posts")
