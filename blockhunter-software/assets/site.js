(function () {
    "use strict";

    var STORAGE_KEY = "bh_lang";
    var SUPPORTED_LANGUAGES = ["de", "en"];

    function detectLanguage() {
        var saved = localStorage.getItem(STORAGE_KEY);
        if (SUPPORTED_LANGUAGES.indexOf(saved) >= 0) {
            return saved;
        }

        var browserLanguage = (navigator.language || "en").toLowerCase();
        return browserLanguage.indexOf("de") === 0 ? "de" : "en";
    }

    function applyLanguage(language) {
        var activeLanguage = SUPPORTED_LANGUAGES.indexOf(language) >= 0 ? language : "en";

        document.documentElement.setAttribute("lang", activeLanguage);
        localStorage.setItem(STORAGE_KEY, activeLanguage);

        document.querySelectorAll("[data-lang]").forEach(function (element) {
            element.hidden = element.getAttribute("data-lang") !== activeLanguage;
        });

        var languageToggle = document.getElementById("lang-toggle");
        if (languageToggle) {
            languageToggle.textContent = activeLanguage === "de" ? "DE aktiv" : "EN active";
            languageToggle.setAttribute(
                "aria-label",
                activeLanguage === "de"
                    ? "Switch language to English"
                    : "Sprache auf Deutsch umstellen"
            );
        }

        document.querySelectorAll("details.dropdown summary").forEach(function (summary) {
            var deLabel = summary.getAttribute("data-label-de");
            var enLabel = summary.getAttribute("data-label-en");
            if (deLabel && enLabel) {
                summary.textContent = activeLanguage === "de" ? deLabel : enLabel;
            }
        });

        document.querySelectorAll("[data-current-year]").forEach(function (element) {
            element.textContent = String(new Date().getFullYear());
        });
    }

    function initNavigation() {
        var navToggle = document.getElementById("nav-toggle");
        var menu = document.getElementById("main-nav");

        if (!navToggle || !menu) {
            return;
        }

        navToggle.addEventListener("click", function () {
            var isOpen = menu.classList.toggle("open");
            navToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
        });

        document.addEventListener("click", function (event) {
            if (!menu.classList.contains("open")) {
                return;
            }

            var clickedInsideMenu = menu.contains(event.target) || navToggle.contains(event.target);
            if (!clickedInsideMenu) {
                menu.classList.remove("open");
                navToggle.setAttribute("aria-expanded", "false");
            }
        });
    }

    var currentLanguage = detectLanguage();
    applyLanguage(currentLanguage);
    initNavigation();

    var languageToggle = document.getElementById("lang-toggle");
    if (languageToggle) {
        languageToggle.addEventListener("click", function () {
            currentLanguage = currentLanguage === "de" ? "en" : "de";
            applyLanguage(currentLanguage);
        });
    }
})();
