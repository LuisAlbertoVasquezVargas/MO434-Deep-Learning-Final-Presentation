<!-- README.md -->

# MO434 Deep Learning Final Presentation

Overleaf-compatible Beamer presentation for the final project of **MO434 — Deep Learning** at **IC/UNICAMP**.

This repository contains the LaTeX source code for the course final presentation. The project is organized as a modular Beamer workspace, keeping metadata, theme configuration, slide sections, figures, and utility scripts separated.

## Repository

```text
https://github.com/LuisAlbertoVasquezVargas/MO434-Deep-Learning-Final-Presentation.git
````

## Clone Repository

```bash
cd /Projects
git clone https://github.com/LuisAlbertoVasquezVargas/MO434-Deep-Learning-Final-Presentation.git
cd MO434-Deep-Learning-Final-Presentation
```

## Project Structure

```text
MO434-Deep-Learning-Final-Presentation/
├── README.md
├── src/
│   ├── main.tex
│   ├── sections/
│   │   ├── 00_title.tex
│   │   ├── 01_intro.tex
│   │   ├── 02_methodology.tex
│   │   ├── 03_experiments.tex
│   │   ├── 04_results.tex
│   │   ├── 05_conclusion.tex
│   │   └── 99_questions.tex
│   ├── structure/
│   │   ├── engine.tex
│   │   └── metadata.tex
│   └── img/
├── scripts/
│   └── lwc.py
└── output/
```

## Main Entry Point

The main LaTeX file is:

```text
src/main.tex
```

When uploading the project to Overleaf, keep the same folder structure and set `src/main.tex` as the main file.

## Presentation Backbone

The presentation is planned with the following initial structure:

```text
Title
Outline
Introduction and Motivation
Methodology
Experimental Setup
Results
Conclusion
Questions
```

## Overleaf Compatibility

This project is intended to work both locally and on Overleaf.

All LaTeX source files are placed under `src/`. Images should be stored under:

```text
src/img/
```

Section files should be imported from `src/main.tex`, while presentation metadata and theme configuration should remain under:

```text
src/structure/
```

## LWC Script

`LWC` stands for **Last Working Code**.

The `scripts/lwc.py` script is used to export the current project source into a single text file. This makes it easier to share the full project context with an LLM in one conversation.

Default usage:

```bash
python scripts/lwc.py
```

Default output:

```text
output/lwc.txt
```

## Development Workflow

A simple workflow for stable checkpoints is:

```bash
python scripts/lwc.py
git add .
git commit -m "Describe checkpoint"
git push origin main
```

If the local shell has the `gpm` alias configured, pushing can also be done with:

```bash
gpm
```

## Current Status

Initial repository setup.

Next planned step:

```text
Add the Overleaf-compatible Beamer backbone under src/.
```

