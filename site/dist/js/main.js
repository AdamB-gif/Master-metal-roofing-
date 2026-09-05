(function () {
  "use strict";

  // Header shadow on scroll
  var header = document.getElementById("site-header");
  function onScroll() {
    if (!header) return;
    header.classList.toggle("is-scrolled", window.scrollY > 4);
  }
  document.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Mobile drawer
  var hamburger = document.getElementById("hamburger-btn");
  var drawer = document.getElementById("mobile-drawer");
  var closeBtn = document.getElementById("drawer-close-btn");
  function openDrawer() {
    drawer.classList.add("is-open");
    hamburger.setAttribute("aria-expanded", "true");
    document.body.style.overflow = "hidden";
  }
  function closeDrawer() {
    drawer.classList.remove("is-open");
    hamburger.setAttribute("aria-expanded", "false");
    document.body.style.overflow = "";
  }
  if (hamburger && drawer) {
    hamburger.addEventListener("click", openDrawer);
    closeBtn && closeBtn.addEventListener("click", closeDrawer);
    drawer.addEventListener("click", function (e) {
      if (e.target.tagName === "A") closeDrawer();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeDrawer();
    });
  }

  // Gallery filter (does not remove items from the DOM/crawlers — just hides visually)
  var filterBtns = document.querySelectorAll(".filter-btn");
  var galleryGrid = document.getElementById("gallery-grid");
  if (filterBtns.length && galleryGrid) {
    filterBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        filterBtns.forEach(function (b) { b.classList.remove("is-active"); });
        btn.classList.add("is-active");
        var filter = btn.getAttribute("data-filter");
        galleryGrid.querySelectorAll("[data-service]").forEach(function (item) {
          var match = filter === "all" || item.getAttribute("data-service") === filter;
          item.style.display = match ? "" : "none";
        });
      });
    });
  }

  // Phone / email click tracking (fires a dataLayer event if analytics is present later)
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href^='tel:'], a[href^='mailto:']");
    if (!a) return;
    var eventName = a.href.indexOf("tel:") === 0 ? "phone_click" : "email_click";
    if (window.dataLayer) window.dataLayer.push({ event: eventName });
  });

  // Estimate / contact form: honeypot + time-trap + inline validation
  document.querySelectorAll("#estimate-form").forEach(function (form) {
    var renderedAt = Date.now ? Date.now() : new Date().getTime();
    var renderedField = form.querySelector("#form_rendered_at");
    if (renderedField) renderedField.value = String(renderedAt);

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = form.querySelector("#form-status");
      var honeypot = form.querySelector("#company_website");

      // Spam checks
      if (honeypot && honeypot.value) {
        return; // silently discard
      }
      var elapsed = (Date.now ? Date.now() : new Date().getTime()) - renderedAt;
      if (elapsed < 3000) {
        return; // silently discard — submitted too fast to be human
      }

      // Inline validation
      var valid = true;
      form.querySelectorAll("[required]").forEach(function (field) {
        var wrapper = field.closest(".field");
        var ok = field.value && field.value.trim().length > 0;
        if (wrapper) wrapper.classList.toggle("has-error", !ok);
        if (!ok) valid = false;
      });
      if (!valid) {
        if (status) {
          status.textContent = "Please fill in the required fields above.";
          status.className = "form-status error is-visible";
        }
        return;
      }

      // Delivery goes live only once FORM_ACCESS_KEY is set in data.py.
      if (form.getAttribute("data-live") !== "1") {
        if (status) {
          status.textContent = "This preview form isn't connected to a live inbox yet.";
          status.className = "form-status success is-visible";
        }
        return;
      }

      var btn = form.querySelector("button[type=submit]");
      if (btn) { btn.disabled = true; btn.textContent = "Sending..."; }
      if (status) {
        status.textContent = "Sending...";
        status.className = "form-status is-visible";
      }
      fetch(form.action, {
        method: "POST",
        headers: { "Accept": "application/json" },
        body: new FormData(form)
      }).then(function (res) {
        if (!res.ok) throw new Error("Request failed");
        window.location.href = "/thank-you/";
      }).catch(function () {
        // Never silently drop a lead: keep what they typed, point them at the phone.
        if (btn) { btn.disabled = false; btn.textContent = "Get My Free Estimate"; }
        var hp = document.querySelector(".header-phone");
        if (status) {
          status.textContent = "Something went wrong sending that. Please call us instead" +
            (hp ? " on " + hp.textContent.trim() : "") + ".";
          status.className = "form-status error is-visible";
        }
      });
    });

    form.querySelectorAll("[required]").forEach(function (field) {
      field.addEventListener("blur", function () {
        var wrapper = field.closest(".field");
        var ok = field.value && field.value.trim().length > 0;
        if (wrapper) wrapper.classList.toggle("has-error", !ok);
      });
    });
  });
})();
