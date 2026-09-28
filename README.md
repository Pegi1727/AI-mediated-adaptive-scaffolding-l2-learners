# Dismantling Symbolic Violence: AI-Mediated Adaptive Scaffolding and the Reconfiguration of Academic Identity among Low-Attaining L2 Learners

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXXX)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![R >= 4.2](https://img.shields.io/badge/R-%3E%3D4.2-276DC3.svg)](https://www.r-project.org/)
[![Reproducibility: Full](https://img.shields.io/badge/Reproducibility-100%25_Verified-success.svg)](#empirical-results)
[![Open Science](https://img.shields.io/badge/Open%20Science-OSF%20%2F%20Zenodo-informational.svg)](#citation)

---

## 📌 Graphical Abstract

![Graphical Abstract](figures/graphical_abstract.png)

> **Visual Overview:** Schematic representation of the study trajectory—from institutional symbolic violence and communicative freeze to non-evaluative adaptive scaffolding, micro-success cycles, and the resulting reconfiguration of L2 academic identity.

---

## 📖 Overview & Abstract

This repository constitutes the comprehensive, publication-grade **Reproducibility Package** for the empirical study:
> **"Dismantling Symbolic Violence: AI-Mediated Adaptive Scaffolding and the Reconfiguration of Academic Identity among Low-Attaining L2 Learners."**

Conventional classroom pedagogies often entrench institutional asymmetries, inadvertently exerting *symbolic violence* (Bourdieu, 1991) against structurally marginalized or low-attaining language learners through evaluative gaze and communicative paralysis. This study reports a mixed-methods intervention ($N = 50$) evaluating whether an AI-driven, adaptive scaffolding tutor operating strictly within each learner's Zone of Proximal Development (ZPD; Vygotsky, 1978)—under an explicit **Scaffolding-Fading Protocol**—can dismantle structural affective barriers, enhance L2 achievement, and catalyze a fundamental shift in learners' academic habitus and socio-psychological agency.

---

## 🖼️ Methodological & Theoretical Architecture

### Figure 1: Theoretical Framework and Research Model
![Figure 1: Theoretical Framework](figures/1.png)
*Integration of Vygotskyan sociocultural theory (Zone of Proximal Development) with Bourdieusian critical sociolinguistics (habitus, symbolic capital, and field restructuring) mediating AI-assisted interaction.*

---

### Figure 2: Intervention Design & Scaffolding-Fading Protocol
![Figure 2: Intervention Protocol](figures/2.png)
*Detailed 5-stage scaffolding and systematic fading pipeline, participant progression, cognitive diagnostic micro-assessments, and iterative autonomy transfer.*

---

## 📊 Empirical Results

### 1. Primary L2 Achievement Metric ($N = 50$)

Statistical reproduction of the primary achievement outcome via paired-samples $t$-test confirms large-magnitude, statistically significant gains across all 50 low-attaining participants.

| Metric | Pre-Intervention | Post-Intervention | Mean Gain ($\Delta$) | $95\%$ CI of $\Delta$ | $t$-statistic | $df$ | $p$-value | Cohen's $d_z$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **L2 Achievement Score** | $14.07 \pm 2.05$ | $17.35 \pm 1.63$ | $+3.28$ | $[2.91, 3.65]$ | **$17.99$** | $49$ | **$< .001$** | **$2.54$** |

*Note: All analyses reproduced from verified raw data sheets (`pre_post_scores_full_50students.csv`). Normality of paired differences validated via Shapiro-Wilk test.*

---

### Figure 3: Quantitative Findings (Achievement & Self-Efficacy)
![Figure 3: Quantitative Results](figures/3.jpg)
*Comparative distributions of pre- and post-intervention scores, showing profound shifts across all quartile bands and self-efficacy metrics.*

---

### 2. Multi-Domain Psychosocial & Agency Questionnaire ($N = 50$)

Analysis of the 12-item bilingual post-intervention instrument across three core constructs:

| Subscale Domain | Items | Pre-Mean (SD) | Post-Mean (SD) | Gain ($\Delta$) | $t(49)$ | $p$-value | Cohen's $d_z$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **General L2 Self-Efficacy** | Items 1–4 | $2.52 \ (0.83)$ | $4.00 \ (0.64)$ | $+1.48$ | $8.07$ | $< .001$ | $1.14$ |
| **AI Trust & Non-Judgmental Safety** | Items 5–8 | $3.42 \ (0.76)$ | $3.78 \ (0.68)$ | $+0.36$ | $3.82$ | $< .001$ | $0.54$ |
| **Socio-Psychological Agency** | Items 9–12 | $1.62 \ (0.72)$ | $3.48 \ (0.75)$ | $+1.86$ | $14.22$ | $< .001$ | $2.01$ |
| **Overall Instrument Composite** | Items 1–12 | $7.56 \ (1.68)$ | $11.26 \ (1.52)$ | $+3.70$ | $13.15$ | $< .001$ | $1.86$ |

---

## 🧠 Qualitative Synthesis & Thematic Architecture

### Figure 4: Qualitative Findings & Identity Reconfiguration
![Figure 4: Qualitative Findings](figures/4.png)
*Five-theme grounded model leading to Reconfigured Academic Identity: (1) Neutralization of the Evaluative Gaze, (2) Low-Stakes Iteration, (3) Internalization of Linguistic Agency, (4) Restoration of Legitimate Speaker Status, and (5) Rescaled Future Self-Guides.*

---

## 🎯 Key Theoretical & Pedagogical Takeaways

1. **Eradication of Symbolic Violence via Algorithmic Neutrality:**
   Traditional face-to-face classroom settings often silence low-attaining learners due to anxiety over peer evaluation and corrective feedback. The AI tutor provides an *affectively neutral communicative sanctuary*, eliminating communicative hesitation.
2. **Precision ZPD Calibration:**
   Unlike static textbooks, adaptive scaffolding modulates prompt complexity, lexicon, and syntactic hints in real-time, consistently keeping cognitive load within the sweet spot of achievable challenge.
3. **From Self-Censorship to Legitimate Speaker:**
   Micro-successes within non-threatening interactions accumulate, catalyzing a qualitative restructuring of learners' academic identity. Participants no longer perceive themselves as structurally deficient, but as capable, agentive language users.

---

## 📂 Repository Directory Structure
```text
├── .github/
│   └── workflows/
│       ├── reproducibility_test.yml   # Continuous Integration Python test suite
│       └── r_validation.yml           # Continuous Integration R test suite
├── CITATION.cff                       # Machine-readable academic citation metadata
├── LICENSE                            # MIT Open Source License
├── README.md                          # Primary repository documentation
├── config.yml                         # Global pipeline parameter specifications
├── environment.yml                    # Conda environment definition file
├── requirements.txt                   # Standard pip dependencies
├── mkdocs.yml                         # Documentation site configuration
├── data/                              # Verified raw and processed empirical data
│   ├── Full_Raw_Data.xlsx
│   ├── Complete_Individual_Data_and_Questionnaire_Analysis.xlsx
│   ├── pre_post_scores_full_50students.csv
│   ├── questionnaire_post_intervention_corrected.csv
│   └── questionnaire_post_intervention_raw.csv
├── figures/                           # High-resolution figures and graphical abstract
│   ├── graphical_abstract.png
│   ├── 1.png
│   ├── 2.png
│   ├── 3.jpg
│   └── 4.png
├── notebooks/                         # Self-contained literate computing notebooks
│   ├── 01_data_audit.ipynb
│   ├── 02_achievement_reproduction.ipynb
│   ├── 03_questionnaire_aggregate_analysis.ipynb
│   └── 04_full_reproducibility_report.ipynb
├── python/                            # Modular Python analysis pipeline
│   ├── 01_import_validate.py
│   ├── 02_prepare_achievement.py
│   ├── 03_descriptives.py
│   ├── 04_assumption_tests.py
│   ├── 05_inferential_analysis.py
│   └── 06_tables_figures_report.py
├── R/                                 # Modular R statistical validation pipeline
│   ├── 01_import_validate.R
│   ├── 02_prepare_achievement.R
│   ├── 03_descriptives.R
│   ├── 04_assumption_tests.R
│   ├── 05_inferential_analysis.R
│   └── 06_tables_figures_report.R
└── outputs/                           # Generated analytical CSVs and summary reports
