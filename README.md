# Disinformation Detection: Machine Learning Classifier for News Posts

[![Language: Python](https://img.shields.io/badge/Language-Python-3776AB?style=flat&logo=python&logoColor=white)]()
[![Language: R](https://img.shields.io/badge/Language-R-276DC3?style=flat&logo=r&logoColor=white)]()
[![Method: ML Classification](https://img.shields.io/badge/Method-ML%20Classification-blueviolet?style=flat)]()
[![Topic: Disinformation](https://img.shields.io/badge/Topic-Disinformation%20Detection-red?style=flat)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This repository provides a reproducible **machine learning pipeline** for detecting disinformation in social media news posts. It covers feature extraction from text, training and evaluating multiple classifiers, and interpreting model outputs — using both **Python** (scikit-learn) and **R** (caret / tidymodels).

> **Related Projects:**
> - 🦠 [facebook-reactions-covid19-india](https://github.com/sawoodanwar/facebook-reactions-covid19-india) — PhD thesis project
> - 📊 [meta-content-analysis](https://github.com/sawoodanwar/meta-content-analysis) — Meta platform analysis
> - 🗳️ [reddit-political-misinfo-coding](https://github.com/sawoodanwar/reddit-political-misinfo-coding) — Reddit coding project
> - ⏱️ [timeseries-facebook-engagement-r](https://github.com/sawoodanwar/timeseries-facebook-engagement-r) — Time-series toolkit

---

## Research Objectives

- Build a binary classifier to distinguish disinformation from credible news posts
- Compare ML algorithms: Logistic Regression, Random Forest, SVM, Naive Bayes
- Extract and evaluate NLP features: TF-IDF, n-grams, sentiment scores
- Evaluate model performance using precision, recall, F1, and AUC-ROC
- Interpret feature importance for explainability

---

## ML Pipeline

| Step | Tool | Description |
|---|---|---|
| Text preprocessing | Python / R | Cleaning, tokenization, stopword removal |
| Feature extraction | `TfidfVectorizer` / `tidytext` | TF-IDF, n-grams, word counts |
| Model training | `scikit-learn` / `caret` | LR, RF, SVM, Naive Bayes |
| Evaluation | `sklearn.metrics` / `yardstick` | Precision, Recall, F1, AUC-ROC |
| Interpretation | `eli5`, `SHAP` / `vip` | Feature importance and SHAP values |

---

## Repository Structure

```
disinformation-detection-ml/
├── scripts/
│   ├── python/
│   │   ├── 01_preprocessing.py       # Text cleaning and feature extraction
│   │   ├── 02_model_training.py      # Train and compare classifiers
│   │   ├── 03_evaluation.py          # Metrics and ROC curves
│   │   └── 04_interpretation.py      # SHAP / feature importance
│   └── R/
│       ├── 01_preprocessing.R        # R-based text prep with tidytext
│       └── 02_tidymodels_classifier.R # tidymodels ML workflow
├── data/
│   └── README.md
├── output/
│   ├── figures/
│   └── tables/
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

---

## Requirements

### Python
```bash
pip install -r requirements.txt
```

### R
```r
install.packages(c("tidymodels", "tidytext", "textrecipes", "vip", "ggplot2"))
```

---

## Author

**Sawood Anwar** — PhD in Humanities (Text and Communication Sciences), University of Urbino Carlo Bo
Defended: 22 September 2025 | Supervisor: Prof. Fabio Giglietto

- 🔗 [GitHub](https://github.com/sawoodanwar) | 💼 [LinkedIn](https://www.linkedin.com/in/sawood-anwar/) | 🎓 [Google Scholar](https://scholar.google.com/citations?hl=en&user=GgsMu3sAAAAJ)

---

## License
MIT License. See [LICENSE](LICENSE).

*Keywords: Disinformation Detection, Machine Learning, NLP, Text Classification, scikit-learn, tidymodels, R, Python, Fake News, Social Media*
