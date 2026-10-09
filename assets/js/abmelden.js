/* Newsletter-Abmeldung: Der Link in der Mail enthält c (Kontakt) und t (Signatur).
   Abgemeldet wird erst nach dem Klick auf den Knopf (Mail-Scanner rufen Links nur auf). */
(function () {
  var q = new URLSearchParams(location.search), c = q.get('c'), t = q.get('t');
  var btn = document.getElementById('unsub-btn'), msg = document.getElementById('unsub-msg'), title = document.getElementById('unsub-title');
  var contact = 'Schreiben Sie uns kurz an info@praxis-huewel.de, dann tragen wir Sie von Hand aus.';
  if (!c || !t) { btn.style.display = 'none'; msg.textContent = 'Dieser Link ist unvollständig. ' + contact; return; }
  btn.addEventListener('click', function () {
    btn.disabled = true; btn.textContent = 'Einen Moment …';
    fetch('https://galjmtozcgxcwtzkzbpi.supabase.co/functions/v1/newsletter-unsub', {
      method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ c: c, t: t })
    }).then(function (r) { return r.json(); }).then(function (d) {
      if (d && d.ok) { title.textContent = 'Sie sind abgemeldet.'; msg.textContent = 'Wir haben Sie aus dem Verteiler ausgetragen. Sie erhalten keine Newsletter mehr von uns.'; btn.style.display = 'none'; }
      else { throw new Error('fail'); }
    }).catch(function () {
      btn.disabled = false; btn.textContent = 'Jetzt abmelden';
      msg.textContent = 'Das hat leider nicht geklappt. ' + contact;
    });
  });
})();
