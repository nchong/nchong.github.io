time convert -density 150 -antialias "../PLDI-20June2018.pdf" -quality 100 "slide.%03d.png"
/usr/local/Cellar/python/3.6.5/bin/python3 script-to-html.py > index.html
