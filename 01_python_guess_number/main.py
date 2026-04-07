import random

random_int = random.randint(1, 100)

while True:
    guess = input("Devinez le Chiffre entre 1 et 100 : ")
    if guess.isdigit():
        guessed_int = int(guess)
        if 1 <= guessed_int <= 100:
            if guessed_int == random_int:
                print(f"Bravo, vous avez trouve la réponse : {random_int} !")
                break
            elif guessed_int < random_int:
                hint = "grand"
            else:
                hint = "petit"
            print(f"Dommage ! Ressayez, le chiffre est plus {hint}.")
        else:
            print("Le chiffre doit être compris entre 1 et 100 !")
    else:
        print("L'entrée doit être un chiffre !")