# Adapted from KC Sivaramakrishnan's annotated talk
# http://kcsrk.info/multicore/gc/2017/07/06/multicore-ocaml-gc
# License: CC BY 4.0

import markdown2

TITLE = "The Semantics of Transactions and Weak Memory in x86, Power, ARM, and C++"
SCRIPT = "script.md"
PATH = ""

header = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang='en' xml:lang='en' xmlns='http://www.w3.org/1999/xhtml'>
  <head>
    <meta content='text/html;charset=UTF-8' http-equiv='content-type' />
    <title>Nathan Chong</title>
    <link href='../../stylesheets/main.css?v=1.0' rel='stylesheet' />
  </head>
<body>
<div id='screen'>
<div class='central700'>
<p><a href="https://nchong.github.com">Home</a> > Annotated PLDI 2018 talk</p>
<h1>%s</h1>

<style>
.annotslide{display:none}
</style>

<p>
Annotated slides of my talk from <a href="https://pldi18.sigplan.org">PLDI 2018</a>.
The slide annotation code is adapted from <a href="http://kcsrk.info/multicore/gc/2017/07/06/multicore-ocaml-gc/">KC Sivaramakrishnan</a> (CC BY 4.0).
</p>

<p align="center">
  Slide <input type="number" id="slidenumber" min="1" /> of <span id="totalslides"></span>
  <input type="button" value="Go" onclick="currentSlide()" />
  <button onclick="deltaSlide(-1)">❮ Prev</button>
  <button onclick="deltaSlide(1)">Next ❯</button>
  ( ← and → arrow keys also work)
</p>
""" % TITLE
slide="""<div class="annotslide">
<p align="center"> <img src="%sslide.%03d.png" border="1" alt="slide.%03d" width="80%%" /> </p>
%s
</div>"""
footer="""<script>
var slideIndex = 1;

function init() {
  showSlide(slideIndex);
  var x = document.getElementsByClassName("annotslide");
  document.getElementById("slidenumber").max = x.length;
  document.getElementById("totalslides").innerHTML = x.length;
}

init();

function deltaSlide(n) {
  showSlide(slideIndex += n);
}

function currentSlide() {
  showSlide(slideIndex = Number(document.getElementById("slidenumber").value));
}

function showSlide(n) {
  var i;
  var x = document.getElementsByClassName("annotslide");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  x[slideIndex-1].style.display = "block";
  document.getElementById("slidenumber").value = slideIndex;
}

document.onkeydown = function(evt) {
	evt = evt || window.event;
	switch (evt.keyCode) {
		case 37:
			deltaSlide(-1);
			break;
		case 39:
			deltaSlide(1);
			break;
	}
};

</script>
</div>
</div>
</body>
</html>
"""

text = []
acc = []
with open(SCRIPT, 'r', encoding='utf-8') as f:
    for line in f:
        if line == "---\n":
            text.append(acc)
            acc = []
        else:
            acc.append(line)

print(header)
for i, md in enumerate(text):
    md_line = ''.join(md)
    html = markdown2.markdown(md_line)
    print(slide % (PATH, i, i, html))
print(footer)
