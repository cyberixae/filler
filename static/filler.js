
var foo = []
var i = 0;
var ce;

function init() {
  ce = document.getElementById('counter');
  loop()
}

function loop() {
  ce.innerHTML = String(i)
  foo.push(Math.random());
  i += 1;
  setTimeout(loop, 0);
}

document.addEventListener('DOMContentLoaded', init);

