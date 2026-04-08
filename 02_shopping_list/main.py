menu = ["Ajouter un élément", "Afficher la liste", "Supprimer un élément", "Quitter"]

shopping_list = []

def show_list(array):
    if len(array) > 0:
        for i in range(0, len(array)):
            print(f"{i+1} : {array[i]}")
        print("---Fin de la liste de courses---")
        print()
    else:
        print("Aucun élément à afficher !")
        print()

def add_element():
    while True:
        element_to_add = input("Ajouter un item à la liste de courses : ")
        print()
        if element_to_add == "":
            print("La saisie ne doit pas être vide ! ")
            print()
        else:
            return element_to_add

def delete_element(array):
    show_list(array)
    if len(array) == 0:
        return
    else:
        while True:
            item_str = input("Quel élément voulez-vous supprimer ? ")
            if item_str.isdigit():
                item_to_delete = int(item_str)
                if 1 <= item_to_delete <= len(array):
                    return item_to_delete
                else:
                    print("Entrée invalide !")
            else:
                print("L'entrée doit être un chiffre !")




while True:
    for i in range(0, len(menu)):
        print(f"{i+1} : {menu[i]}")
    user_choice_str = input("Choisissez une action à réaliser : ")
    if user_choice_str.isdigit():
        user_choice_int = int(user_choice_str)
        if not 1 <= user_choice_int <= len(menu):
            print("Choix invalide !")
            print()
        elif user_choice_int == 1:
            shopping_item = add_element()
            shopping_list.append(shopping_item)
        elif user_choice_int == 2:
            show_list(shopping_list)
        elif user_choice_int == 3:
            element_to_delete = delete_element(shopping_list)
            if element_to_delete:
                shopping_list.remove(shopping_list[element_to_delete-1])
        elif user_choice_int == 4:
            print()
            print("Sortie du programme.")
            break
    else:
        print("L'entrée doit être un chiffre")