#!/bin/bash

cp exercise_solutions.tex tmp.tex
pdflatex tmp.tex
bibtex tmp.aux
pdflatex tmp.tex
pdflatex tmp.tex
cp tmp.pdf exercise_solutions.pdf
rm tmp.*
