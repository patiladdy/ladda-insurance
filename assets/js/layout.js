/* Shared header, footer, floating buttons & quote modal (injected on every page) */
(function () {
  const R = document.body.dataset.root || "";          // "" for root pages, "../" for /blog pages
  const page = document.body.dataset.page || "";
  window.SITE = {
    phone1: "919422681476", phone2: "919422460294",
    phone1Label: "+91 94226 81476", phone2Label: "+91 94224 60294",
    email: "kartikladda1111@gmail.com",
    address: "Homkar Nagar, Bhavani Peth, Solapur, Maharashtra"
  };
  const S = window.SITE;
  const links = [
    ["index.html", "Home", "home"], ["about.html", "About", "about"], ["services.html", "Services", "services"],
    ["calculators.html", "Calculators", "calculators"], ["blog/index.html", "Blogs", "blog"], ["contact.html", "Contact", "contact"]
  ];
  const navHTML = links.map(([h, t, k]) =>
    `<li><a href="${R}${h}" class="${page === k ? "active" : ""}">${t}</a></li>`).join("");
  const mNavHTML = links.map(([h, t, k]) =>
    `<a class="m-link ${page === k ? "active" : ""}" href="${R}${h}">${t}</a>`).join("");

  const header = `
  <div class="topbar"><div class="container">
    <div class="tb-left">
      <span><i data-lucide="map-pin"></i>Homkar Nagar, Solapur</span>
      <a href="tel:+${S.phone1}"><i data-lucide="phone"></i>${S.phone1Label}</a>
      <a href="mailto:${S.email}"><i data-lucide="mail"></i>${S.email}</a>
    </div>
    <div class="tb-right"><span><i data-lucide="award"></i>GM Club Star Advisor · National Insurance FY 2025-26</span></div>
  </div></div>
  <header class="site-header" id="siteHeader">
    <div class="container nav">
      <a class="brand" href="${R}index.html" aria-label="Ladda Insurance home"><img src="${R}assets/img/logo-light.png" alt="Ladda Insurance – You Select, We Cover"></a>
      <nav aria-label="Main"><ul class="nav-links">${navHTML}</ul></nav>
      <div class="nav-cta">
        <a class="btn btn-outline btn-sm" href="tel:+${S.phone1}"><i data-lucide="phone"></i>Call</a>
        <button class="btn btn-primary btn-sm" data-quote type="button">Get a Free Quote <i data-lucide="arrow-right"></i></button>
        <button class="menu-toggle" id="menuOpen" type="button" aria-label="Open menu"><i data-lucide="menu"></i></button>
      </div>
    </div>
  </header>
  <div class="mobile-menu" id="mobileMenu" aria-hidden="true">
    <div class="panel" role="dialog" aria-label="Menu">
      <div class="panel-head"><img src="${R}assets/img/logo-light.png" alt="Ladda Insurance"><button class="close" id="menuClose" type="button" aria-label="Close menu"><i data-lucide="x"></i></button></div>
      ${mNavHTML}
      <div style="display:grid;gap:.6rem;margin-top:1.2rem">
        <button class="btn btn-primary" data-quote type="button">Get a Free Quote</button>
        <a class="btn btn-wa" href="https://wa.me/${S.phone1}" target="_blank" rel="noopener"><i data-lucide="message-circle"></i>WhatsApp</a>
      </div>
    </div>
  </div>`;

  const footer = `
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <img class="footer-logo" src="${R}assets/img/logo.png" alt="Ladda Insurance">
          <p>Kartik Poonamchand Ladda – Insurance Advisor, Solapur. Health, life, motor, fire, shop, marine & business insurance plus investment guidance. <b style="color:#fff">You Select, We Cover.</b></p>
          <div class="socials">
            <a href="https://wa.me/${S.phone1}" aria-label="WhatsApp" target="_blank" rel="noopener"><i data-lucide="message-circle"></i></a>
            <a href="#" aria-label="Facebook"><i data-lucide="facebook"></i></a>
            <a href="#" aria-label="Instagram"><i data-lucide="instagram"></i></a>
            <a href="#" aria-label="YouTube"><i data-lucide="youtube"></i></a>
          </div>
        </div>
        <div><h4>Quick Links</h4><ul>
          <li><a href="${R}index.html">Home</a></li><li><a href="${R}about.html">About Kartik</a></li>
          <li><a href="${R}services.html">Services</a></li><li><a href="${R}calculators.html">Calculators</a></li>
          <li><a href="${R}blog/index.html">Blogs</a></li><li><a href="${R}contact.html">Contact</a></li></ul></div>
        <div><h4>Insurance</h4><ul>
          <li><a href="${R}services.html#health">Health Insurance</a></li><li><a href="${R}services.html#life">Life & LIC Plans</a></li>
          <li><a href="${R}services.html#motor">Vehicle Insurance</a></li><li><a href="${R}services.html#fire">Fire & Factory</a></li>
          <li><a href="${R}services.html#shop">Shop Insurance</a></li><li><a href="${R}services.html#marine">Marine Insurance</a></li>
          <li><a href="${R}services.html#mf">Mutual Funds</a></li></ul></div>
        <div><h4>Get in Touch</h4><ul class="footer-contact">
          <li><i data-lucide="phone"></i><span><a href="tel:+${S.phone1}">${S.phone1Label}</a><br><a href="tel:+${S.phone2}">${S.phone2Label}</a></span></li>
          <li><i data-lucide="mail"></i><a href="mailto:${S.email}">${S.email}</a></li>
          <li><i data-lucide="map-pin"></i><span>${S.address}</span></li>
          <li><i data-lucide="clock"></i><span>Mon–Sat · 10:00 AM – 7:00 PM</span></li></ul></div>
      </div>
      <p class="footer-disclaimer">Insurance is the subject matter of solicitation. Mutual fund investments are subject to market risks; read all scheme-related documents carefully. Past performance is not indicative of future returns. Calculator results are indicative estimates only. Policy benefits, premiums and terms are as per the respective insurer's policy wording.</p>
      <div class="footer-bottom"><span>© <span id="yr"></span> Ladda Insurance · Kartik Poonamchand Ladda. All rights reserved.</span><span>Solapur, Maharashtra · India</span></div>
    </div>
  </footer>
  <div class="fab">
    <a class="call" href="tel:+${S.phone1}" aria-label="Call Kartik"><i data-lucide="phone"></i></a>
    <a class="wa" href="https://wa.me/${S.phone1}?text=${encodeURIComponent("Hello Kartik ji, I would like to know about insurance.")}" target="_blank" rel="noopener" aria-label="WhatsApp Kartik"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.9 9.9 0 0 0 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91S17.5 2 12.04 2Zm5.8 14.13c-.24.68-1.42 1.3-1.96 1.35-.5.05-.97.23-3.27-.68-2.77-1.09-4.52-3.92-4.66-4.1-.13-.18-1.11-1.48-1.11-2.83 0-1.34.7-2 .96-2.28.24-.27.53-.34.71-.34h.51c.16 0 .38-.06.6.46.24.55.79 1.9.86 2.04.07.14.11.3.02.48-.09.18-.14.3-.27.46l-.41.48c-.14.14-.28.29-.12.56.16.27.71 1.17 1.52 1.9 1.05.93 1.93 1.22 2.2 1.36.27.14.43.11.59-.07.16-.18.68-.79.86-1.07.18-.27.36-.23.6-.14.25.09 1.58.75 1.85.88.27.14.45.2.52.32.07.11.07.66-.17 1.34Z"/></svg></a>
  </div>
  <nav class="bottom-bar" aria-label="Quick actions">
    <a class="call" href="tel:+${S.phone1}"><i data-lucide="phone"></i>Call</a>
    <a class="wa" href="https://wa.me/${S.phone1}" target="_blank" rel="noopener"><i data-lucide="message-circle"></i>WhatsApp</a>
    <button class="quote" data-quote type="button"><i data-lucide="file-text"></i>Get Quote</button>
    <button id="menuOpen2" type="button"><i data-lucide="menu"></i>Menu</button>
  </nav>
  <div class="modal" id="quoteModal" aria-hidden="true">
    <div class="box" role="dialog" aria-labelledby="qmTitle">
      <div class="box-head"><div><span class="eyebrow">Free · No obligation</span><h3 id="qmTitle" style="font-size:1.4rem">Get your free quote</h3><p class="muted" style="margin:0">Kartik will reply on WhatsApp shortly.</p></div>
        <button class="close" data-close type="button" aria-label="Close"><i data-lucide="x"></i></button></div>
      <form class="form js-wa-form">
        <div><label for="qName">Your name</label><input id="qName" name="name" required autocomplete="name"></div>
        <div class="row">
          <div><label for="qPhone">Mobile</label><input id="qPhone" name="phone" type="tel" inputmode="numeric" pattern="[0-9+ ]{10,14}" required autocomplete="tel"></div>
          <div><label for="qCity">City</label><input id="qCity" name="city" value="Solapur"></div>
        </div>
        <div><label for="qType">I'm interested in</label><select id="qType" name="interest">
          <option>Health Insurance</option><option>Life Insurance / LIC Policy</option><option>Term Insurance</option><option>Vehicle Insurance</option>
          <option>Fire / Factory Insurance</option><option>Shop Insurance</option><option>Marine Insurance</option><option>Home Insurance</option><option>Mutual Funds / SIP</option><option>Other</option></select></div>
        <div><label for="qMsg">Message (optional)</label><textarea id="qMsg" name="message" rows="3"></textarea></div>
        <button class="btn btn-wa" type="submit"><i data-lucide="send"></i>Send on WhatsApp</button>
      </form>
    </div>
  </div>`;

  document.body.insertAdjacentHTML("afterbegin", header);
  document.body.insertAdjacentHTML("beforeend", footer);
  document.getElementById("yr").textContent = new Date().getFullYear();
})();
