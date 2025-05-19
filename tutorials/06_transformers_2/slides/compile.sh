#!/bin/bash

cp e06_slides.tex tmp.tex
pdflatex tmp.tex
#bibtex tmp.aux
pdflatex tmp.tex
pdflatex tmp.tex
cp tmp.pdf e06_slides.pdf

rm tmp.*
