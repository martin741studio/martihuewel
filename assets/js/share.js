/* Teilen-Buttons: Link kopieren und (am Handy) das System-Teilen-Menü, z. B. für Instagram. Keine Drittanbieter-Skripte. */
(function () {
  var box = document.querySelector('.share');
  if (!box) return;
  var url = box.getAttribute('data-url'), title = box.getAttribute('data-title');
  var copy = box.querySelector('[data-copy]'), nat = box.querySelector('[data-native]');
  if (navigator.share && nat) {
    nat.hidden = false;
    nat.addEventListener('click', function () { navigator.share({ title: title, url: url }).catch(function () {}); });
  }
  if (copy) copy.addEventListener('click', function () {
    var done = function () { var t = copy.textContent; copy.textContent = 'Link kopiert ✓'; setTimeout(function () { copy.textContent = t; }, 2200); };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(url).then(done, function () { window.prompt('Link kopieren:', url); });
    else window.prompt('Link kopieren:', url);
  });
})();
