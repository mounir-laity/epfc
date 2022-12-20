import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier

def predict_image(index: int=100):
    image = digits['images'][index]
    test = image.reshape(1, -1)
    plt.imshow(image, cmap = 'Greys_r')
    print(f"L'image d'indice {index} est un {model.predict(test)[0]}")
    plt.show(block=False)

if __name__ == "__main__":
    # importons une base de données de chiffre
    digits = load_digits()
    X = digits.data
    y = digits.target
    print('dimension de X:', X.shape)
    # visualisons un de ces chiffres
    image = digits['images'][0]
    plt.imshow(image, cmap = 'Greys_r')
    # plt.show(block=False)
    # print(f"Cette image est un {digits.target[0]}")
    # Entraînement du modele
    max_score = 0
    best_index = 0
    for i in range(1,11):
        model = KNeighborsClassifier(n_neighbors=i)
        model.fit(X, y)
        score = model.score(X, y)
        if score > max_score:
            max_score = score
            best_index = i
        print(f"Score du modèle pour k={i}: {score}")
    print(f"Best value for k : {best_index}")
    #Test du modele
    index = 1000
    predict_image(index)
    print(f"La bonne catégorie est {digits.target[index]}")
    input("Appuyez sur entrée pour terminer...")