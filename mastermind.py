import random
#fonction qui génère la combinaison
def generate_combination():
	#affectation de la variable aléatoire(list)
    random_colors = ["rouge", "bleu", "jaune", "vert", "gris", "noir"]
    return random.sample(random_colors, 4)
#definition de la fonction qui donne des indices 
def check_guesses(random_color, max_chances=10):
    remaining_chances = max_chances
    user_colors = []
    #Information des chances utilisateurs
    print(f"Vous devez trouver une combinaison de 4 couleurs dans le bon ordre. Vous avez droit à {max_chances} chances.")
    #une boucle qui vérifie si les chances restantes sont supérieurs à zéro et la longueur des couleur de l'utilisateur n'est pas infèrieu
    while remaining_chances > 0 and len(user_colors) < len(random_color):
        choice = input("Entrer une couleur : ").strip().lower()
        index = len(user_colors)

        if choice == random_color[index]:
            # ajout de la valeur choice a la list user_colors
            user_colors.append(choice)
            print("Bonne couleur et bonne position !")
        elif choice in random_color:
            # Couleur correcte mais mauvaise position 
            print("Bonne couleur mais pas dans le bon ordre. Veuillez réessayer !!")
            remaining_chances -= 1
            print(f"Il vous reste {remaining_chances} chances")
        else:
            # Couleur incorrecte
            print("Mauvaise couleur. Veuillez réessayer !!")
            remaining_chances -= 1
            print(f"Il vous reste {remaining_chances} chances")

    return user_colors, remaining_chances
#fonction qui affiche le résultat
def show_result(user_colors, random_color, remaining_chances):
    if len(user_colors) == len(random_color):
        print(f"Bravo ! Vous avez deviné toutes les couleurs : {user_colors}")
    else:
        print("Dommage, vous avez utilisé toutes vos chances...")
        print(f"La combinaison était : {random_color}")
#fonction main
def main():
    Generate = generate_combination()
    user_colors, remaining_chances = check_guesses(Generate)
    show_result(user_colors, Generate, remaining_chances)
#si  tout est ok alors le code run
if __name__ == "__main__":
    main()




	
	




