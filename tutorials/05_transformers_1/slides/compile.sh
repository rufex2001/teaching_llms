#!/bin/bash

cp e05_slides.tex tmp.tex
pdflatex tmp.tex
#bibtex tmp.aux
pdflatex tmp.tex
pdflatex tmp.tex
cp tmp.pdf e05_slides.pdf

rm tmp.*
