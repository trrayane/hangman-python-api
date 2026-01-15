import requests

def get_random_word():
    url = "https://random-word-api.herokuapp.com/word?lang=fr"
    response = requests.get(url)
    return response.json()[0]

mot_mystere = get_random_word()
mot_visible = ["_"] * len(mot_mystere)

nb_vies = 5

while True:
    print("Mot :", "".join(mot_visible))
    print("Il vous reste", nb_vies, "vies")

    lettre = input("Proposez une lettre : ").lower()

    if lettre in mot_mystere:
        for i, c in enumerate(mot_mystere):
            if c == lettre:
                mot_visible[i] = lettre
    else:
        nb_vies -= 1

    if mot_mystere == "".join(mot_visible):
        print(" Gagné ! Le mot était :", mot_mystere)
        break
    elif nb_vies == 0:
        print(" Perdu ! Le mot était :", mot_mystere)
        break

    print("=" * 20)
