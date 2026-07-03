# Disinformation Detection | Script 02: Model Training
# Author: Sawood Anwar

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split, cross_val_score

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# models = {
#     'Logistic Regression': LogisticRegression(max_iter=1000),
#     'Random Forest': RandomForestClassifier(n_estimators=100),
#     'Linear SVM': LinearSVC(),
#     'Naive Bayes': MultinomialNB()
# }

# for name, model in models.items():
#     scores = cross_val_score(model, X_train, y_train, cv=5, scoring='f1')
#     print(f'{name}: F1 = {scores.mean():.3f} (+/- {scores.std():.3f})')
print('Model training script ready.')
