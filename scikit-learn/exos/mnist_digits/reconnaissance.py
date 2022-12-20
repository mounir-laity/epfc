import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

def predict_image(index, df_test):
    image = df_test.iloc[index]
    test = image.values.reshape(1, -1)
    image = image.values.reshape(28,28)
    plt.imshow(image, cmap = 'Greys_r')
    print(f"La catégorie prédite pour l'image d'indice {index} est {model.predict(test)[0]}")
    plt.show(block=False)
    
def find_best_k():
    best_score = 0
    best_k = 0
    with open("scores.txt", "w") as file:
        for i in range(1,10):
            model = KNeighborsClassifier(n_neighbors=i)
            model.fit(X_train,y_train)
            score = model.score(X_test,y_test)
            if score > best_score:
                best_score = score
                best_k = i
            file.write(f"Pour k={i}, le score obtenu est {score}\n")
        file.write(f"La meilleure valeur pour k est {best_k}")

if __name__ == "__main__":
    filename = "chiffres.csv"
    df = pd.read_csv(filename)
    df_train, df_test = train_test_split(df, train_size=0.8)
    print(df_train.shape)
    print(df_test.shape)
    y_train = df_train["label"]
    y_test = df_test["label"]
    X_train = df_train.loc[:, df.columns != "label"]
    X_test = df_test.loc[:, df.columns != "label"]
    # find_best_k()
    model = KNeighborsClassifier(n_neighbors=1)
    # model = OneVsRestClassifier(LogisticRegression(max_iter=10000))
    model.fit(X_train,y_train)
    score = model.score(X_test,y_test)
    print(f"Le score du modèle est : {score}")
    index = 777
    predict_image(index, X_test)
    print(f"La bonne catégorie pour l'image d'indice {index} est {y_test.iloc[index]}")
    input("Appuyez sur entrée pour quitter...")
    