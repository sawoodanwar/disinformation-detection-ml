# Disinformation Detection: Machine Learning Classifier for News Posts

[![Language: Python](https://img.shields.io/badge/Language-Python-3776AB?style=flat&logo=python&logoColor=white)]()
[![Language: R](https://img.shields.io/badge/Language-R-276DC3?style=flat&logo=r&logoColor=white)]()
[![Method: ML Classification](https://img.shields.io/badge/Method-ML%20Classification-blueviolet?style=flat)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

Reproducible **ML pipeline** for detecting disinformation in news posts using Python (scikit-learn) and R (tidymodels). Compares LR, RF, SVM, and Naive Bayes with SHAP-based interpretation.

---

## 🔗 Related Projects

| Repository | Description |
|---|---|
| 🦠 [facebook-reactions-covid19-india](https://github.com/sawoodanwar/facebook-reactions-covid19-india) | PhD thesis project |
| ⏱️ [timeseries-facebook-engagement-r](https://github.com/sawoodanwar/timeseries-facebook-engagement-r) | Time-series toolkit |
| 🧠 [stm-social-media-r](https://github.com/sawoodanwar/stm-social-media-r) | STM topic modeling toolkit |
| 💬 [sentiment-lexicon-comparison](https://github.com/sawoodanwar/sentiment-lexicon-comparison) | AFINN, Bing, NRC lexicon comparison |
| 📊 [meta-content-analysis](https://github.com/sawoodanwar/meta-content-analysis) | Facebook & Instagram health misinformation analysis |
| 🗳️ [reddit-political-misinfo-coding](https://github.com/sawoodanwar/reddit-political-misinfo-coding) | Reddit political communication manual coding |
| 🔄 [cross-platform-engagement-analysis](https://github.com/sawoodanwar/cross-platform-engagement-analysis) | Unified cross-platform engagement framework |
| 🟣 [nlp-news-classification-r](https://github.com/sawoodanwar/nlp-news-classification-r) | Supervised NLP news classification |
| 🟢 [crowdtangle-meta-api-workflow](https://github.com/sawoodanwar/crowdtangle-meta-api-workflow) | Academic data collection pipeline |
| 📊 [survey-data-analysis-r](https://github.com/sawoodanwar/survey-data-analysis-r) | Survey data cleaning, Likert analysis & descriptives |
| 📝 [survey-scale-validation-r](https://github.com/sawoodanwar/survey-scale-validation-r) | Scale validation: EFA/CFA, Cronbach alpha, reliability |
| 🧪 [survey-experiment-analysis-r](https://github.com/sawoodanwar/survey-experiment-analysis-r) | Survey experiment & vignette study analysis |

---

## ML Pipeline

| Step | Tool | Description |
|---|---|---|
| Preprocessing | Python / R | Cleaning, tokenization, stopword removal |
| Feature extraction | `TfidfVectorizer` / `tidytext` | TF-IDF, n-grams |
| Model training | `scikit-learn` / `caret` | LR, RF, SVM, Naive Bayes |
| Evaluation | `sklearn.metrics` / `yardstick` | Precision, Recall, F1, AUC-ROC |
| Interpretation | `SHAP` / `vip` | Feature importance |

## Requirements

```bash
pip install -r requirements.txt
```
```r
install.packages(c("tidymodels", "tidytext", "textrecipes", "vip", "ggplot2"))
```

---

## Author

**Sawood Anwar** — PhD in Humanities, University of Urbino Carlo Bo | Defended: 22 September 2025

- 🔗 [GitHub](https://github.com/sawoodanwar) | 💼 [LinkedIn](https://www.linkedin.com/in/sawood-anwar/) | 🎓 [Google Scholar](https://scholar.google.com/citations?hl=en&user=GgsMu3sAAAAJ)

## License
MIT License.

*Keywords: Disinformation Detection, Machine Learning, NLP, scikit-learn, tidymodels, R, Python*
