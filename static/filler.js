
var foo = []
var i = 0;
var ce;
var runid = randomid();

function init() {
  ce = document.getElementById('counter');
  loop()
}

function d16() {
  return Math.floor(Math.random() * 16);
}


function hex(x) {
  nums = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f'];
  return String(nums[x]);
}

function randomid() {
  id = '';
  for (var i = 0; i < 32; i++) {
    id += hex(d16());
  }
  return id
}

function report(reserved) {
  var unit = "numbers";

  ce.innerHTML = String(reserved) + " " + unit + " reserved!";

  var xhr = new XMLHttpRequest();
  var url = "/heartbeat";
  var body = JSON.stringify({"reserved": reserved, "unit": unit, "runid": runid});
  xhr.open("POST", url, false);
  xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhr.setRequestHeader("Content-length", body.length);
  xhr.setRequestHeader("Connection", "close");
  xhr.onreadystatechange = function() {
	if (xhr.readyState == 4 && xhr.status != 200) {
		console.log('ERROR: report fail');
	}
  }
  xhr.send(body);
}

function loop() {
  if (i % 1000 == 0) {
    report(i);
  }
  foo.push(Math.random());
  i += 1;
  setTimeout(loop, 0);
}

document.addEventListener('DOMContentLoaded', init);

