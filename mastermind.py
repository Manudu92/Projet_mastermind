import random 

color = ["rouge", "bleu", "jaune" , "vert", "gris", "noir" ]
random_color = random.sample(color, 4)
print("Vous devez trouver une combinaison de 4 couleur dans le bon ordre. Vous avez droit à six(6) chances ")

remaining_chances=6
index=0
user_colors=[]
while remaining_chances > 0 and len(user_colors) != len(random_color):
	choice = input("Entrer une couleur ")
	user_colors.append(choice)
	if user_colors[index] in random_color and user_colors[index] != random_color[index]:
		print("Réponse correcte mais pas dans le bon ordre; Veuillez réessayer!!")


	if user_colors[index] != random_color[index]:

		print("Mauvaise couleur. Veuillez réessayer!!")
		user_colors.pop(index)
		remaining_chances-=1
		if index == 0:
			index=0
		else:
		    index-=1
		print("Il vous reste "+str(remaining_chances)+" chances")
	if len(user_colors)>=1:
		index+=1
		


	
	
	
if len(user_colors) == len(random_color):

	print(f"Bravo vous avez pu deviné toutes les couleurs qui sont : {user_colors}")
else:
	print("Dommange vous avez utilisé toutes vos chances... Prochainement!")


	
	




