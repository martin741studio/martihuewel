/* Einwilligung (Hinweisfenster) + Google Analytics 4 mit Consent Mode v2.
   Strikt: Das Google-Skript wird erst geladen, wenn der Besucher „Zustimmen“ klickt.
   Ohne Zustimmung: kein Skript, keine Cookies, keine Verbindung zu Google.
   Die Messkennung steht nur hier. Weitere Mess- oder Werbeskripte nur nach Anweisung von 741 Studio. */
(function () {
  var GA_ID = 'G-4FP95Y92XY';
  var KEY = 'ph_consent_v1';
  var MAX_AGE = 365 * 24 * 3600 * 1000;   // nach 12 Monaten wird neu gefragt
  var granted = false, loaded = false;

  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  gtag('consent', 'default', { ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'denied' });

  function read() {
    try {
      var v = JSON.parse(localStorage.getItem(KEY) || 'null');
      if (v && typeof v.a === 'boolean' && v.t && Date.now() - v.t < MAX_AGE) return v;
    } catch (e) { /* ohne Speicher: Banner erscheint bei jedem Besuch */ }
    return null;
  }
  function write(a) { try { localStorage.setItem(KEY, JSON.stringify({ a: a, t: Date.now() })); } catch (e) { /* ignorieren */ } }

  function clearGaCookies() {
    var host = location.hostname, parts = host.split('.'), base = parts.slice(-2).join('.');
    document.cookie.split(';').forEach(function (c) {
      var n = c.split('=')[0].trim();
      if (n === '_ga' || n.indexOf('_ga_') === 0 || n === '_gid' || n.indexOf('_gat') === 0) {
        [host, '.' + host, '.' + base].forEach(function (d) {
          document.cookie = n + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/; domain=' + d;
        });
        document.cookie = n + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/';
      }
    });
  }

  function grant() {
    granted = true;
    gtag('consent', 'update', { analytics_storage: 'granted', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied' });
    if (loaded) return;
    loaded = true;
    gtag('js', new Date());
    gtag('config', GA_ID, { allow_google_signals: false, allow_ad_personalization_signals: false });
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(GA_ID);
    document.head.appendChild(s);
  }
  function revoke() {
    granted = false;
    gtag('consent', 'update', { analytics_storage: 'denied' });
    clearGaCookies();
  }

  /* Ereignisse: nur nach Zustimmung (sonst wird nichts in die Warteschlange gelegt). */
  window.phTrack = function (name, params) {
    if (!granted) return;
    gtag('event', name, params || {});
  };

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var h = a.getAttribute('href') || '';
    if (/^tel:/i.test(h)) window.phTrack('phone_click', { link_url: h.replace(/^tel:/i, '') });
    else if (/^(https?:\/\/(wa\.me|api\.whatsapp\.com|web\.whatsapp\.com)\/(send\?phone=)?\+?\d+|whatsapp:\/\/send\?phone=)/i.test(h)) window.phTrack('whatsapp_click', { link_url: h.split('?')[0] });
    else if (/^mailto:info@praxis-huewel\.de/i.test(h)) window.phTrack('email_click', { link_url: 'info@praxis-huewel.de' });
  });

  /* Hinweisfenster */
  function banner() {
    var old = document.getElementById('ph-cc');
    if (old) { old.focus(); return; }
    var d = document.createElement('div');
    d.id = 'ph-cc'; d.className = 'cc'; d.setAttribute('role', 'dialog'); d.setAttribute('aria-labelledby', 'ph-cc-t'); d.tabIndex = -1;
    d.innerHTML = '<div class="cc-box"><p class="cc-title" id="ph-cc-t">Statistik: Ihre Entscheidung</p>' +
      '<p>Ich möchte verstehen, welche Seiten hilfreich sind und ob Anfragen ankommen. Dafür nutze ich Google Analytics, aber nur mit Ihrer Zustimmung. ' +
      'Ohne Zustimmung wird nichts an Google übertragen. Sie können das jederzeit unten über „Cookie-Einstellungen“ ändern. ' +
      'Mehr in der <a href="/datenschutz.html#statistik">Datenschutzerklärung</a>.</p>' +
      '<div class="cc-btns"><button type="button" class="btn btn-ghost" data-cc="no">Ablehnen</button>' +
      '<button type="button" class="btn btn-ghost" data-cc="yes">Zustimmen</button></div></div>';
    d.addEventListener('click', function (e) {
      var b = e.target.closest('[data-cc]');
      if (!b) return;
      var yes = b.getAttribute('data-cc') === 'yes';
      write(yes);
      if (yes) grant(); else if (granted || loaded) revoke();
      d.remove();
    });
    document.body.appendChild(d);
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a');
    if (a && /Cookie-Einstellungen/.test(a.textContent)) { e.preventDefault(); banner(); }
  });

  var saved = read();
  if (saved && saved.a) grant();
  else if (!saved) {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', banner); else banner();
  }
})();
