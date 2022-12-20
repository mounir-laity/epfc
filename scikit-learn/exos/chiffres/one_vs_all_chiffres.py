from sklearn.multiclass import OneVsRestClassifier
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression

def predict_image(index: int=100):
    image = digits['images'][index]
    test = image.reshape(1, -1)
    plt.imshow(image, cmap = 'Greys_r')
    print(f"L'image d'indice {index} est un {model.predict(test)[0]}")
    plt.show(block=False)

digits = load_digits()
X = digits.data
y = digits.target
print('dimension de X:', X.shape)
model = OneVsRestClassifier(LogisticRegression(max_iter=10000)).fit(X, y)
print(model.score(X,y))
index = 777
predict_image(index)
print(f"La bonne catégorie est {digits.target[index]}")
input("Appuyez sur entrée pour terminer...")