from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
df = load_breast_cancer()
x = df['data']
y = df['target']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.40, random_state = 42)
#instanciation
model_Gaussian = GaussianNB()
#training
model_Gaussian.fit(x_train, y_train)
#prédiction
prediction = model_Gaussian.predict(x_test)
print(prediction)
#evaluation du modèle
precision = accuracy_score(y_test, prediction)*100
print(precision)