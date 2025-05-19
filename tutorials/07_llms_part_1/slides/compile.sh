#!/bin/bash

cp slides.tex tmp.tex
pdflatex tmp.tex
#bibtex tmp.aux
pdflatex tmp.tex
pdflatex tmp.tex
cp tmp.pdf slides.pdf

rm tmp.*
