"""
Task 10: Machine Learning - KNN & Naive Bayes
a. Install: pip install scikit-learn
"""
import sklearn
print(sklearn.__version__)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.datasets import load_iris

# b. Load dataset
iris = load_iris(as_frame=True)
df = iris.frame
print(df.head())

# c. Features/labels, train/test split
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# d. KNN - fit and predict
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)

# e. KNN - evaluate
print("KNN Accuracy:", accuracy_score(y_test, knn_pred))
print("KNN Classification Report:\n", classification_report(y_test, knn_pred))

# f. Mathematics behind KNN
"""
KNN Explanation:
KNN classifies a new point by looking at its 'k' nearest neighbors
in the training data and taking a majority vote of their classes.

Euclidean distance between two points A(x1, y1) and B(x2, y2):
    d(A, B) = sqrt((x2 - x1)^2 + (y2 - y1)^2)
For higher dimensions (n features):
    d = sqrt(sum((xi - yi)^2 for i in range(n)))

Choosing k:
- Small k (e.g. k=1) is sensitive to noise and can overfit.
- Large k smooths predictions but can blur class boundaries (underfit).
- k is usually chosen as an odd number to avoid ties, and tested
  using cross-validation to find the value that gives best accuracy.
  Here k=3 was chosen as a common small, stable default for a
  small dataset like Iris.
"""

# g. Naive Bayes - fit and predict
nb = GaussianNB()
nb.fit(X_train, y_train)
nb_pred = nb.predict(X_test)

# h. Naive Bayes - evaluate
print("Naive Bayes Accuracy:", accuracy_score(y_test, nb_pred))
print("Naive Bayes Confusion Matrix:\n", confusion_matrix(y_test, nb_pred))

# i. Mathematics behind Naive Bayes
"""
Naive Bayes Explanation:
Naive Bayes is based on Bayes' Theorem:
    P(class | features) = [P(features | class) * P(class)] / P(features)

Where:
- P(class | features) = posterior probability of a class given the data
- P(features | class) = likelihood of the features given the class
- P(class)             = prior probability of the class
- P(features)          = overall probability of the features (evidence)

It is called 'naive' because it assumes all features are conditionally
independent given the class, i.e.:
    P(features | class) = P(f1|class) * P(f2|class) * ... * P(fn|class)

GaussianNB assumes each feature follows a normal (Gaussian) distribution
within each class, and predicts the class with the highest posterior
probability.
"""