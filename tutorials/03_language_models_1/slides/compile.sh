#!/bin/bash

cp e03_slides.tex tmp.tex
pdflatex tmp.tex
#bibtex tmp.aux
pdflatex tmp.tex
pdflatex tmp.tex
cp tmp.pdf e03_slides.pdf

rm tmp.*
