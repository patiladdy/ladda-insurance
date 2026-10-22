/* Financial calculators – config-driven. All results are indicative only. */
(function () {
  const fmt = n => "₹ " + Math.round(n).toLocaleString("en-IN");
  const short = n => { n = Math.round(n); if (n >= 1e7) return "₹ " + (n / 1e7).toFixed(2) + " Cr"; if (n >= 1e5) return "₹ " + (n / 1e5).toFixed(2) + " L"; return fmt(n); };
  const C = { navy: "#0B2E6B", blue: "#1456B8", orange: "#F37021", green: "#16A34A", line: "#E2E8F0" };
  const emi = (P, rAnnual, months) => { const r = rAnnual / 1200; return r === 0 ? P / months : P * r * Math.pow(1 + r, months) / (Math.pow(1 + r, months) - 1); };

  const CALCS = {
    emi: {
      title: "EMI Calculator", icon: "calculator",
      seg: { key: "preset", options: { "Home Loan": { amount: 3000000, rate: 8.5, years: 20 }, "Car Loan": { amount: 800000, rate: 9.5, years: 5 }, "Personal Loan": { amount: 300000, rate: 12, years: 3 }, "Business Loan": { amount: 1500000, rate: 13, years: 7 } } },
      fields: [["amount", "Loan amount", 50000, 50000000, 10000, 3000000, "₹"], ["rate", "Interest rate (p.a.)", 5, 24, 0.1, 8.5, "%"], ["years", "Tenure", 1, 30, 1, 20, "Yrs"]],
      calc: v => { const m = v.years * 12, e = emi(v.amount, v.rate, m), tot = e * m;
        return { main: ["Monthly EMI", fmt(e)], rows: [["Principal", fmt(v.amount)], ["Total interest", fmt(tot - v.amount)], ["Total payment", fmt(tot)], ["No. of EMIs", m]],
          chart: { type: "doughnut", labels: ["Principal", "Interest"], data: [v.amount, tot - v.amount] } }; }
    },
    loan: {
      title: "Loan Eligibility Calculator", icon: "landmark",
      fields: [["income", "Net monthly income", 10000, 1000000, 1000, 60000, "₹"], ["existing", "Existing EMIs / month", 0, 500000, 500, 5000, "₹"], ["foir", "Max EMI as % of income", 30, 65, 1, 50, "%"], ["rate", "Interest rate (p.a.)", 5, 20, 0.1, 8.5, "%"], ["years", "Tenure", 1, 30, 1, 20, "Yrs"]],
      calc: v => { const capacity = Math.max(0, v.income * v.foir / 100 - v.existing), r = v.rate / 1200, n = v.years * 12;
        const P = r === 0 ? capacity * n : capacity * (Math.pow(1 + r, n) - 1) / (r * Math.pow(1 + r, n));
        return { main: ["You may be eligible for up to", short(P)], rows: [["Affordable EMI", fmt(capacity)], ["Total interest", fmt(capacity * n - P)], ["Tenure", v.years + " years"], ["Rate", v.rate + "%"]],
          chart: { type: "doughnut", labels: ["Eligible loan", "Interest over tenure"], data: [P, Math.max(0, capacity * n - P)] },
          note: "Banks also consider credit score, age, property value and employment type. Actual eligibility may differ." }; }
    },
    sip: {
      title: "SIP Calculator", icon: "trending-up",
      fields: [["monthly", "Monthly investment", 500, 200000, 500, 5000, "₹"], ["rate", "Expected return (p.a.)", 1, 30, 0.5, 12, "%"], ["years", "Time period", 1, 40, 1, 15, "Yrs"], ["stepup", "Annual step-up", 0, 25, 1, 0, "%"]],
      calc: v => { const r = v.rate / 1200; let fv = 0, inv = 0, amt = v.monthly; const lab = [], a = [], b = [];
        for (let y = 1; y <= v.years; y++) { for (let m = 0; m < 12; m++) { fv = (fv + amt) * (1 + r); inv += amt; } lab.push("Y" + y); a.push(Math.round(inv)); b.push(Math.round(fv)); amt *= 1 + v.stepup / 100; }
        return { main: ["Estimated value", short(fv)], rows: [["Invested amount", fmt(inv)], ["Est. returns", fmt(fv - inv)], ["Wealth gain", (inv ? ((fv / inv - 1) * 100).toFixed(0) : 0) + "%"], ["Total value", fmt(fv)]],
          chart: { type: "line", labels: lab, series: [["Invested", a, C.orange], ["Value", b, C.blue]] } }; }
    },
    lumpsum: {
      title: "Lumpsum Calculator", icon: "piggy-bank",
      fields: [["amount", "One-time investment", 5000, 50000000, 5000, 100000, "₹"], ["rate", "Expected return (p.a.)", 1, 30, 0.5, 12, "%"], ["years", "Time period", 1, 40, 1, 10, "Yrs"]],
      calc: v => { const lab = [], d = []; for (let y = 0; y <= v.years; y++) { lab.push("Y" + y); d.push(Math.round(v.amount * Math.pow(1 + v.rate / 100, y))); }
        const fv = d[d.length - 1];
        return { main: ["Estimated value", short(fv)], rows: [["Invested", fmt(v.amount)], ["Est. returns", fmt(fv - v.amount)], ["Multiple", (fv / v.amount).toFixed(2) + "x"], ["Total value", fmt(fv)]],
          chart: { type: "line", labels: lab, series: [["Value", d, C.blue]] } }; }
    },
    swp: {
      title: "SWP Calculator", icon: "wallet",
      fields: [["corpus", "Total investment", 100000, 100000000, 10000, 2500000, "₹"], ["withdraw", "Monthly withdrawal", 1000, 1000000, 500, 15000, "₹"], ["rate", "Expected return (p.a.)", 1, 20, 0.5, 8, "%"], ["years", "Time period", 1, 40, 1, 15, "Yrs"]],
      calc: v => { const r = v.rate / 1200; let bal = v.corpus, out = 0, lastMonth = null; const lab = [], d = [];
        for (let y = 1; y <= v.years; y++) { for (let m = 0; m < 12; m++) { if (bal <= 0) { if (lastMonth === null) lastMonth = (y - 1) * 12 + m; continue; } bal = bal * (1 + r); const w = Math.min(v.withdraw, bal); bal -= w; out += w; } lab.push("Y" + y); d.push(Math.max(0, Math.round(bal))); }
        return { main: ["Balance after " + v.years + " yrs", short(Math.max(0, bal))], rows: [["Total withdrawn", fmt(out)], ["Initial corpus", fmt(v.corpus)], ["Monthly income", fmt(v.withdraw)], ["Money lasts", lastMonth === null ? "Full period ✓" : (lastMonth / 12).toFixed(1) + " yrs"]],
          chart: { type: "line", labels: lab, series: [["Remaining corpus", d, C.blue]] },
          note: lastMonth !== null ? "⚠ Your corpus runs out before the chosen period. Reduce withdrawal or increase corpus." : "" }; }
    },
    term: {
      title: "Term Insurance Cover Calculator", icon: "shield-check",
      fields: [["age", "Your age", 18, 65, 1, 30, "Yrs"], ["income", "Annual income", 100000, 50000000, 50000, 1000000, "₹"], ["expenses", "Annual family expenses", 50000, 20000000, 10000, 500000, "₹"], ["loans", "Outstanding loans", 0, 50000000, 50000, 2000000, "₹"], ["goals", "Future goals (education, marriage)", 0, 50000000, 50000, 2500000, "₹"], ["savings", "Existing savings & cover", 0, 50000000, 50000, 500000, "₹"]],
      calc: v => { const yrs = Math.max(5, 60 - v.age), real = 0.02; // inflation-adjusted real return
        const pv = v.expenses * (1 - Math.pow(1 + real, -yrs)) / real;
        const need = Math.max(0, pv + v.loans + v.goals - v.savings), rule = v.income * 15;
        const rec = Math.ceil(Math.max(need, 0) / 2500000) * 2500000;
        return { main: ["Recommended life cover", short(rec)], rows: [["Needs-based cover", short(need)], ["15× income thumb rule", short(rule)], ["Years till 60", yrs], ["Loans + goals", short(v.loans + v.goals)]],
          chart: { type: "doughnut", labels: ["Family expenses", "Loans", "Goals"], data: [pv, v.loans, v.goals] },
          note: "Based on the expense-replacement (needs) method, rounded up to the nearest ₹25 lakh." }; }
    },
    health: {
      title: "Health Cover Estimator", icon: "heart-pulse",
      seg: { key: "city", options: { "Tier-2 city (Solapur)": { cityFactor: 1 }, "Metro (Pune / Mumbai)": { cityFactor: 1.5 } } },
      fields: [["adults", "Adults in family", 1, 6, 1, 2, ""], ["kids", "Children", 0, 4, 1, 1, ""], ["eldest", "Age of eldest member", 18, 80, 1, 35, "Yrs"], ["cityFactor", "City cost factor", 1, 1.5, 0.5, 1, "x"]],
      calc: v => { let base = 500000; if (v.eldest >= 45) base = 1000000; if (v.eldest >= 60) base = 1500000;
        const fam = base + Math.max(0, v.adults - 2) * 250000 + v.kids * 100000; const rec = Math.ceil(fam * v.cityFactor / 500000) * 500000;
        return { main: ["Suggested family floater", short(rec)], rows: [["Members", v.adults + v.kids], ["Super top-up idea", short(rec * 2)], ["Base cover", short(base)], ["City factor", v.cityFactor + "x"]],
          chart: { type: "doughnut", labels: ["Base floater", "Super top-up (suggested)"], data: [rec, rec * 2] },
          note: "A practical rule of thumb used in advisory. Final premium depends on insurer, health history and add-ons." }; }
    },
    lic: {
      title: "LIC Maturity Estimator", icon: "badge-indian-rupee",
      seg: { key: "plan", options: { "Endowment / Jeevan Labh type": { bonus: 45, fab: 150 }, "Jeevan Anand type": { bonus: 45, fab: 150 }, "Money-back type": { bonus: 40, fab: 100 } } },
      fields: [["sa", "Basic sum assured", 100000, 10000000, 25000, 1000000, "₹"], ["term", "Policy term", 10, 35, 1, 21, "Yrs"], ["bonus", "Bonus rate per ₹1,000 SA / yr", 20, 70, 1, 45, "₹"], ["fab", "Final additional bonus per ₹1,000 SA", 0, 600, 10, 150, "₹"]],
      calc: v => { const bonus = v.sa / 1000 * v.bonus * v.term, fab = v.sa / 1000 * v.fab, total = v.sa + bonus + fab;
        return { main: ["Estimated maturity value", short(total)], rows: [["Sum assured", fmt(v.sa)], ["Reversionary bonus", fmt(bonus)], ["Final add. bonus", fmt(fab)], ["Term", v.term + " years"]],
          chart: { type: "doughnut", labels: ["Sum assured", "Bonus", "FAB"], data: [v.sa, bonus, fab] },
          note: "Bonus rates are declared by LIC every year and are not guaranteed. Money-back plans pay part of the SA earlier, so maturity will be lower. Ask Kartik for the official benefit illustration." }; }
    },
    irr: {
      title: "Policy Return (IRR) Calculator", icon: "percent",
      fields: [["premium", "Annual premium", 5000, 1000000, 1000, 50000, "₹"], ["ppt", "Premium paying years", 1, 35, 1, 15, "Yrs"], ["term", "Policy term (maturity year)", 1, 40, 1, 21, "Yrs"], ["maturity", "Maturity amount", 10000, 50000000, 10000, 1800000, "₹"]],
      calc: v => { const ppt = Math.min(v.ppt, v.term), fv = r => { let s = 0; for (let i = 0; i < ppt; i++) s += v.premium * Math.pow(1 + r, v.term - i); return s; };
        let lo = -0.5, hi = 0.5; for (let k = 0; k < 100; k++) { const mid = (lo + hi) / 2; fv(mid) > v.maturity ? hi = mid : lo = mid; }
        const irr = (lo + hi) / 2 * 100, paid = v.premium * ppt;
        return { main: ["Effective annual return (IRR)", irr.toFixed(2) + "%"], rows: [["Total premium paid", fmt(paid)], ["Maturity amount", fmt(v.maturity)], ["Gain", fmt(v.maturity - paid)], ["Multiple", (v.maturity / paid).toFixed(2) + "x"]],
          chart: { type: "doughnut", labels: ["Premium paid", "Gain"], data: [paid, Math.max(0, v.maturity - paid)] },
          note: "Use this to compare any traditional policy's real yield with FD / PPF. Enter figures from your policy's benefit illustration." }; }
    },
    retire: {
      title: "Retirement Calculator", icon: "sunset",
      fields: [["age", "Current age", 18, 60, 1, 30, "Yrs"], ["retAge", "Retirement age", 40, 70, 1, 60, "Yrs"], ["expense", "Current monthly expenses", 5000, 500000, 1000, 30000, "₹"], ["infl", "Inflation", 3, 10, 0.5, 6, "%"], ["preRet", "Return before retirement", 4, 16, 0.5, 12, "%"], ["postRet", "Return after retirement", 3, 12, 0.5, 7, "%"]],
      calc: v => { const n = Math.max(1, v.retAge - v.age), life = 25;
        const expAtRet = v.expense * 12 * Math.pow(1 + v.infl / 100, n);
        const real = (1 + v.postRet / 100) / (1 + v.infl / 100) - 1;
        const corpus = Math.abs(real) < 1e-6 ? expAtRet * life : expAtRet * (1 - Math.pow(1 + real, -life)) / real * (1 + real);
        const r = v.preRet / 1200, m = n * 12, sip = corpus * r / ((Math.pow(1 + r, m) - 1) * (1 + r));
        return { main: ["Retirement corpus needed", short(corpus)], rows: [["Monthly SIP needed", fmt(sip)], ["Expense at retirement / mo", fmt(expAtRet / 12)], ["Years to retire", n], ["Plan for", life + " yrs after"]],
          chart: { type: "doughnut", labels: ["Your SIP contributions", "Growth"], data: [sip * m, Math.max(0, corpus - sip * m)] } }; }
    }
  };

  const root = document.getElementById("calcApp"); if (!root) return;
  const tabs = root.querySelector(".calc-tabs"), panels = root.querySelector(".calc-panels");
  const charts = {};

  Object.entries(CALCS).forEach(([key, c], idx) => {
    tabs.insertAdjacentHTML("beforeend", `<button class="calc-tab ${idx ? "" : "active"}" data-tab="${key}" type="button" role="tab"><i data-lucide="${c.icon}"></i>${c.title.replace(" Calculator", "").replace(" Estimator", "")}</button>`);
    const seg = c.seg ? `<div class="seg" role="group">${Object.keys(c.seg.options).map((o, i) => `<button type="button" class="${i ? "" : "active"}" data-seg="${o}">${o}</button>`).join("")}</div>` : "";
    const fields = c.fields.map(([id, label, min, max, step, val, unit]) => `
      <div class="field"><label for="${key}-${id}-n">${label}<span class="val">${unit === "₹" ? "₹" : ""}<input id="${key}-${id}-n" type="number" inputmode="decimal" min="${min}" max="${max}" step="${step}" value="${val}" data-id="${id}">${unit && unit !== "₹" ? unit : ""}</span></label>
      <input type="range" aria-label="${label}" min="${min}" max="${max}" step="${step}" value="${val}" data-id="${id}"></div>`).join("");
    panels.insertAdjacentHTML("beforeend", `
      <div class="calc-panel ${idx ? "" : "active"}" id="panel-${key}" role="tabpanel">
        <div class="calc-box"><h3><i data-lucide="${c.icon}"></i>${c.title}</h3>${seg}${fields}</div>
        <div class="calc-box"><div class="result-main"><small class="rm-l"></small><strong class="rm-v"></strong></div>
          <div class="result-rows"></div><div class="chart-wrap"><canvas></canvas></div><p class="disclaimer"></p>
          <div style="display:flex;gap:.6rem;flex-wrap:wrap;margin-top:.5rem"><button class="btn btn-primary btn-sm" data-quote type="button">Talk to Kartik</button>
          <a class="btn btn-outline btn-sm share-wa" target="_blank" rel="noopener" href="#"><i data-lucide="share-2"></i>Share result</a></div></div>
      </div>`);
    const panel = document.getElementById("panel-" + key);
    const ranges = panel.querySelectorAll("input[type=range]"), nums = panel.querySelectorAll("input[type=number]");
    const paint = r => r.style.setProperty("--p", ((r.value - r.min) / (r.max - r.min) * 100) + "%");
    const read = () => { const v = {}; ranges.forEach(r => v[r.dataset.id] = parseFloat(r.value)); return v; };
    const run = () => {
      const v = read(), out = c.calc(v);
      panel.querySelector(".rm-l").textContent = out.main[0]; panel.querySelector(".rm-v").textContent = out.main[1];
      panel.querySelector(".result-rows").innerHTML = out.rows.map(([a, b]) => `<div><small>${a}</small><b>${b}</b></div>`).join("");
      panel.querySelector(".disclaimer").textContent = (out.note ? out.note + " " : "") + "Results are indicative estimates, not a guarantee or offer.";
      panel.querySelector(".share-wa").href = `https://wa.me/${window.SITE.phone1}?text=${encodeURIComponent(`Hi Kartik ji, I used the ${c.title} on your website.\n${out.main[0]}: ${out.main[1]}\n` + out.rows.map(r => r.join(": ")).join("\n") + "\nPlease guide me.")}`;
      drawChart(key, panel.querySelector("canvas"), out.chart);
    };
    ranges.forEach((r, i) => { paint(r); r.addEventListener("input", () => { nums[i].value = r.value; paint(r); run(); }); });
    nums.forEach((n, i) => n.addEventListener("change", () => { let x = parseFloat(n.value); if (isNaN(x)) x = +ranges[i].min; x = Math.min(+ranges[i].max, Math.max(+ranges[i].min, x)); n.value = x; ranges[i].value = x; paint(ranges[i]); run(); }));
    if (c.seg) panel.querySelectorAll(".seg button").forEach(b => b.addEventListener("click", () => {
      panel.querySelectorAll(".seg button").forEach(x => x.classList.toggle("active", x === b));
      Object.entries(c.seg.options[b.dataset.seg]).forEach(([id, val]) => { const r = panel.querySelector(`input[type=range][data-id=${id}]`); if (r) { r.value = val; panel.querySelector(`input[type=number][data-id=${id}]`).value = val; paint(r); } });
      run();
    }));
    panel._run = run;
  });

  function drawChart(key, canvas, cfg) {
    if (!window.Chart || !cfg) return;
    if (charts[key]) charts[key].destroy();
    const common = { responsive: true, maintainAspectRatio: false, animation: { duration: 400 }, plugins: { legend: { position: "bottom", labels: { usePointStyle: true, boxWidth: 8, font: { family: "Inter" } } },
      tooltip: { callbacks: { label: ctx => " " + ctx.dataset.label + ": " + short(ctx.raw ?? ctx.parsed) } } } };
    if (cfg.type === "doughnut") {
      charts[key] = new Chart(canvas, { type: "doughnut", data: { labels: cfg.labels, datasets: [{ label: "", data: cfg.data, backgroundColor: [C.navy, C.orange, "#60A5FA", C.green], borderWidth: 0 }] },
        options: { ...common, cutout: "68%", plugins: { ...common.plugins, tooltip: { callbacks: { label: ctx => " " + ctx.label + ": " + short(ctx.raw) } } } } });
    } else {
      charts[key] = new Chart(canvas, { type: "line", data: { labels: cfg.labels, datasets: cfg.series.map(([l, d, col]) => ({ label: l, data: d, borderColor: col, backgroundColor: col + "22", fill: true, tension: .35, pointRadius: 0, borderWidth: 2.5 })) },
        options: { ...common, interaction: { mode: "index", intersect: false }, scales: { y: { ticks: { callback: v => short(v).replace("₹ ", "₹") }, grid: { color: C.line } }, x: { grid: { display: false }, ticks: { maxTicksLimit: 8 } } } } });
    }
  }

  const activate = key => {
    if (!CALCS[key]) return;
    tabs.querySelectorAll(".calc-tab").forEach(t => t.classList.toggle("active", t.dataset.tab === key));
    panels.querySelectorAll(".calc-panel").forEach(p => p.classList.toggle("active", p.id === "panel-" + key));
    document.getElementById("panel-" + key)._run();
    const t = tabs.querySelector(`[data-tab=${key}]`); t && t.scrollIntoView({ block: "nearest", inline: "center", behavior: "smooth" });
  };
  tabs.addEventListener("click", e => { const t = e.target.closest(".calc-tab"); if (t) { activate(t.dataset.tab); history.replaceState(null, "", "#" + t.dataset.tab); } });
  document.addEventListener("DOMContentLoaded", () => activate(location.hash.slice(1) in CALCS ? location.hash.slice(1) : "emi"));
})();
