# LaTeX Documentation

Ce dossier contient le nécessaire pour générer votre propre TP.

## Structure

- `main.tex` - Document principal avec paquets importés et la structure du TP
- `part1.tex` - Première séance du TP
- `part2.tex` - Deuxième séance du TP 
- `part3.tex` - Troisième séance du TP

## Compilation

Pour compiler le document:

```bash
pdflatex main.tex
pdflatex main.tex  # Run twice for proper table of contents
```

## Fonctionnalités

- Mise en page sur une colonne (papier A4)
- Table des matières automatique
- Structure modulaire avec des fichiers séparés
- Mise en forme avec en-têtes et numéros de page

## Prérequis

Assurez-vous d'avoir les paquets suivant installés:
- inputenc
- fontenc
- babel (french)
- geometry
- amsmath, amsfonts, amssymb
- graphicx
- hyperref
- fancyhdr
- setspace
- titlesec
