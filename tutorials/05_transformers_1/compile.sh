#!/bin/bash

# exercise
cp exercise.tex tmp.tex
pdflatex tmp.tex
bibtex tmp.aux
pdflatex tmp.tex
pdflatex tmp.tex
cp tmp.pdf exercise.pdf
rm tmp.*
