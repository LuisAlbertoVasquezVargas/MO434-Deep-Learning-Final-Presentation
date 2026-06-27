<!-- README.md -->

# MO434 Deep Learning Final Presentation

Overleaf-compatible Beamer presentation for the final project of **MO434 — Deep Learning** at **IC/UNICAMP**.

This repository contains the LaTeX source code for the course final presentation. The project is organized as a modular Beamer workspace, keeping metadata, theme configuration, slide sections, figures, utility scripts, and generated outputs separated.

## Repository

```text
https://github.com/LuisAlbertoVasquezVargas/MO434-Deep-Learning-Final-Presentation.git
```

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

```text
src/main.tex
```

## Render Locally

```bash
cd src
latexmk -pdf -outdir=../output main.tex
zathura ../output/main.pdf
```

The rendered PDF is generated at:

```text
output/main.pdf
```

## LWC Script

`LWC` stands for **Last Working Code**.

The script `scripts/lwc.py` exports the current project source into a single text file so the full project context can be shared with an LLM in one conversation.

Run from the repository root:

```bash
python scripts/lwc.py
```

Default output:

```text
output/lwc.txt
```

Custom output path:

```bash
python scripts/lwc.py --output output/mo434_context.txt
```

