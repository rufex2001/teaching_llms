#!/bin/bash

cp e02-slides.tex tmp.tex
pdflatex tmp.tex
#bibtex tmp.aux
pdflatex tmp.tex
pdflatex tmp.tex
cp tmp.pdf e02-slides.pdf

rm tmp.*
