/* Interactions: icons, menu, modal, forms → WhatsApp, counters, filters, sliders, lightbox */
document.addEventListener("DOMContentLoaded", () => {
  if (window.lucide) lucide.createIcons();
  const S = window.SITE;

  // Sticky header shadow
  const hdr = document.getElementById("siteHeader");
  const onScroll = () => hdr && hdr.classList.toggle("scrolled", window.scrollY > 10);
  onScroll(); window.addEventListener("scroll", onScroll, { passive: true });

  // Mobile menu
  const menu = document.getElementById("mobileMenu");
  const openMenu = () => { menu.classList.add("open"); menu.setAttribute("aria-hidden", "false"); document.body.style.overflow = "hidden"; };
  const closeMenu = () => { menu.classList.remove("open"); menu.setAttribute("aria-hidden", "true"); document.body.style.overflow = ""; };
  ["menuOpen", "menuOpen2"].forEach(id => { const b = document.getElementById(id); b && b.addEventListener("click", openMenu); });
  document.getElementById("menuClose").addEventListener("click", closeMenu);
  menu.addEventListener("click", e => { if (e.target === menu) closeMenu(); });

  // Quote modal
  const modal = document.getElementById("quoteModal");
  const openModal = (interest) => {
    closeMenu(); modal.classList.add("open"); modal.setAttribute("aria-hidden", "false");
    if (interest) { const sel = modal.querySelector("select"); [...sel.options].forEach(o => { if (o.text === interest) sel.value = o.text; }); }
    setTimeout(() => modal.querySelector("input").focus(), 200);
  };
  const closeModal = () => { modal.classList.remove("open"); modal.setAttribute("aria-hidden", "true"); };
  document.querySelectorAll("[data-quote]").forEach(b => b.addEventListener("click", () => openModal(b.dataset.quote)));
  modal.addEventListener("click", e => { if (e.target === modal || e.target.closest("[data-close]")) closeModal(); });
  document.addEventListener("keydown", e => { if (e.key === "Escape") { closeModal(); closeMenu(); } });

  // All lead forms → WhatsApp (no backend needed)
  document.querySelectorAll(".js-wa-form").forEach(f => f.addEventListener("submit", e => {
    e.preventDefault();
    const d = new FormData(f);
    const lines = ["Hello Kartik ji, I'd like a free consultation."];
    for (const [k, v] of d.entries()) if (String(v).trim()) lines.push(`${k[0].toUpperCase() + k.slice(1)}: ${v}`);
    window.open(`https://wa.me/${S.phone1}?text=${encodeURIComponent(lines.join("\n"))}`, "_blank", "noopener");
    f.reset(); closeModal();
  }));

  // AOS
  if (window.AOS) AOS.init({ duration: 700, once: true, offset: 60, easing: "ease-out-cubic" });

  // Counters
  const counters = document.querySelectorAll("[data-count]");
  if (counters.length && "IntersectionObserver" in window) {
    const io = new IntersectionObserver(entries => entries.forEach(en => {
      if (!en.isIntersecting) return;
      const el = en.target, end = +el.dataset.count, suf = el.dataset.suffix || "";
      const t0 = performance.now(), dur = 1400;
      const tick = t => { const p = Math.min((t - t0) / dur, 1); el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))).toLocaleString("en-IN") + suf; if (p < 1) requestAnimationFrame(tick); };
      requestAnimationFrame(tick); io.unobserve(el);
    }), { threshold: .5 });
    counters.forEach(c => io.observe(c));
  }

  // Generic chip filters: <div class="chips" data-filter-target="#grid"> <button data-filter="all|x">
  document.querySelectorAll(".chips[data-filter-target]").forEach(group => {
    const target = document.querySelector(group.dataset.filterTarget);
    group.addEventListener("click", e => {
      const b = e.target.closest(".chip"); if (!b) return;
      group.querySelectorAll(".chip").forEach(c => c.classList.toggle("active", c === b));
      const f = b.dataset.filter;
      target.querySelectorAll("[data-persona]").forEach(el => el.classList.toggle("hide", f !== "all" && !el.dataset.persona.split(" ").includes(f)));
      if (window.AOS) AOS.refresh();
    });
  });

  // Testimonials slider
  if (window.Swiper && document.querySelector(".t-swiper")) {
    new Swiper(".t-swiper", {
      slidesPerView: 1, spaceBetween: 20, loop: true, autoHeight: false,
      autoplay: { delay: 5000, disableOnInteraction: false },
      pagination: { el: ".swiper-pagination", clickable: true },
      breakpoints: { 700: { slidesPerView: 2 }, 1024: { slidesPerView: 3 } }
    });
  }

  // Lightbox
  if (window.GLightbox) GLightbox({ selector: ".glightbox", touchNavigation: true, loop: true });

  // Hero intro (GSAP)
  if (window.gsap && document.querySelector(".hero") && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
    gsap.from(".hero-copy > *", { y: 30, opacity: 0, duration: .8, stagger: .1, ease: "power3.out" });
    gsap.from(".hero-visual .person", { x: 60, opacity: 0, duration: 1, delay: .2, ease: "power3.out" });
    gsap.from(".float-card", { scale: .6, opacity: 0, duration: .6, delay: .8, stagger: .2, ease: "back.out(1.7)" });
    gsap.to(".float-card.fc1", { y: -10, duration: 2.5, repeat: -1, yoyo: true, ease: "sine.inOut" });
    gsap.to(".float-card.fc2", { y: 10, duration: 2.8, repeat: -1, yoyo: true, ease: "sine.inOut" });
  }
});
