# Ladda Insurance – Website (Kartik Poonamchand Ladda, Solapur)

A static, responsive website built with HTML, CSS and JavaScript. It needs no build step.

## Run / host
- Open `index.html` in a browser, or serve it locally with `python -m http.server`.
- To host on GitHub Pages or Netlify, upload the whole folder. The `.nojekyll` file is already included.
- Icons, animations and charts load from CDNs, so the site needs an internet connection.

## Structure
- `index.html`: home page (hero, services filter, awards, calculators, partners, testimonials, blogs, FAQ)
- `about.html`: profile, awards and the honours gallery (lightbox)
- `services.html`: 9 services with quote buttons
- `calculators.html`: 10 calculators (EMI, Loan Eligibility, SIP, Lumpsum, SWP, Term Cover, Health Cover, LIC Maturity, Policy IRR, Retirement)
- `contact.html`: contact details, a form that opens WhatsApp, and a map
- `blog/`: blog index and 11 articles, including Top 5 Mutual Funds and Top LIC Policies
- `assets/css/style.css`: design system and responsive breakpoints (1280 / 1024 / 768 / 640)
- `assets/js/layout.js`: shared header, footer, floating buttons and quote modal. **Change phone, email and address here.**
- `assets/js/main.js`: menu, modal, forms, counters, filters, slider and lightbox
- `assets/js/calculators.js`: calculator logic

## Libraries (CDN)
Google Fonts (Poppins and Inter), Lucide icons, AOS, GSAP, Swiper, GLightbox, Chart.js

## Before going live
1. Replace the sample testimonials in `index.html` with real client reviews.
2. Add real social media links in `layout.js`, in the footer `.socials` section.
3. Confirm the insurer and AMC list in `PARTNERS` in `build_pages.py`, or edit the HTML directly.
4. If you offer mutual funds, add your AMFI ARN to the footer.
5. Have the blog facts reviewed. Fund names, LIC plans and tax rules change over time.

## Regenerating pages (optional)
`build_pages.py` and `blog_data.py` generate all the HTML. Edit the content in them, then run `python build_pages.py` after setting `OUT` to this folder.
