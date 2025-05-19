#!/bin/bash

cp e01-slides.tex tmp.tex
pdflatex tmp.tex
#bibtex tmp.aux
pdflatex tmp.tex
pdflatex tmp.tex
cp tmp.pdf e01-slides.pdf

rm tmp.*
