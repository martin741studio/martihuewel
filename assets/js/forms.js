/* Formulare: senden an die Praxis-Funktion (Supabase, Frankfurt) und zeigen eine Rückmeldung. */
(function () {
  var ENDPOINT = 'https://galjmtozcgxcwtzkzbpi.supabase.co/functions/v1/site-form';
  var PHONE = '<a href="tel:+499116007651">0911 6007651</a>';

  function status(form) {
    var s = form.querySelector('.form-status');
    if (!s) {
      s = document.createElement('div');
      s.className = 'form-status';
      s.setAttribute('role', 'status');
      s.setAttribute('aria-live', 'polite');
      form.appendChild(s);
    }
    return s;
  }

  document.querySelectorAll('form[data-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('button[type=submit]');
      var label = btn.textContent;
      var out = status(form);
      var data = { form: form.getAttribute('data-form') };
      new FormData(form).forEach(function (v, k) { data[k] = typeof v === 'string' ? v : ''; });
      data.datenschutz = !!(form.elements.datenschutz && form.elements.datenschutz.checked);
      var c = form.querySelector('.consent span');
      if (c) data.consent_text = c.textContent.replace(/\s+/g, ' ').trim();
      btn.disabled = true;
      btn.textContent = 'Wird gesendet …';
      out.className = 'form-status';
      out.textContent = '';
      fetch(ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      }).then(function (r) {
        return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; });
      }).then(function (res) {
        if (res.ok && res.j.ok) {
          var box = document.createElement('div');
          box.className = 'form-success';
          box.setAttribute('role', 'status');
          box.innerHTML = '<h3>Vielen Dank für Ihre Anfrage.</h3><p>' +
            (form.getAttribute('data-success') || 'Ihre Nachricht ist bei mir angekommen. Ich melde mich zeitnah bei Ihnen.') +
            '</p><p>Wenn es eilig ist, erreichen Sie mich auch telefonisch: ' + PHONE + '.</p>';
          form.replaceWith(box);
          box.scrollIntoView({ block: 'center', behavior: 'smooth' });
        } else {
          throw new Error((res.j && res.j.error) || 'Fehler');
        }
      }).catch(function (err) {
        out.className = 'form-status error';
        var msg = err && err.message && err.message !== 'Failed to fetch' && err.message !== 'Fehler' ? err.message : 'Ihre Anfrage konnte leider nicht gesendet werden.';
        out.innerHTML = msg + ' Bitte versuchen Sie es erneut oder rufen Sie an: ' + PHONE + ' – oder schreiben Sie an <a href="mailto:info@praxis-huewel.de">info@praxis-huewel.de</a>.';
        btn.disabled = false;
        btn.textContent = label;
      });
    });
  });
})();
