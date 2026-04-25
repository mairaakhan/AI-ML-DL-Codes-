import pandas as pd
df = pd.read_csv("download.csv")
df.shape

df.head()

features_cols = ['age', 'bmi', 'blood_pressure', 'glucose', 'smoker']
X = df[features_cols]
y = df.disease

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.39, random_state = 42)

from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
y_pred

y_test

logreg.score(X_test, y_test)

from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test,y_pred)
cnf_matrix



