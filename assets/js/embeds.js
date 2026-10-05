/* Zwei-Klick-Lösung: Google Maps und Calendly laden erst nach Einwilligung per Klick. */
(function () {
  function load(gate) {
    var type = gate.getAttribute('data-embed');
    if (type === 'map') {
      var f = document.createElement('iframe');
      f.title = gate.getAttribute('data-title') || 'Karte';
      f.src = gate.getAttribute('data-src');
      f.loading = 'lazy';
      f.referrerPolicy = 'no-referrer-when-downgrade';
      gate.replaceWith(f);
    } else if (type === 'calendly') {
      var box = document.createElement('div');
      box.style.cssText = 'max-width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch';
      var w = document.createElement('div');
      w.className = 'calendly-inline-widget';
      w.setAttribute('data-url', gate.getAttribute('data-url'));
      w.style.cssText = 'min-width:320px;height:700px;margin-top:20px';
      box.appendChild(w);
      gate.replaceWith(box);
      var s = document.createElement('script');
      s.src = 'https://assets.calendly.com/assets/external/widget.js';
      s.async = true;
      document.body.appendChild(s);
    }
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('.embed-gate button');
    if (b) load(b.closest('.embed-gate'));
  });
})();
