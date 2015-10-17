# -*- coding: utf-8 -*-

import fonctions as fc

print("*-* Bienvenue au jeu du pendu *-*")
nom = input("Entrez votre nom : ")

score = fc.score(nom)
print("Vous disposez d'un score de {}".format(score))

points = 8

mot_initial, mot_list = fc.init()
print("Jouons avec le mot : {}".format("".join(mot_list)))

while fc.end(mot_list) == False and points > 0:
	lettre = fc.ask()
	mot_list, boo = fc.check(mot_initial, mot_list, lettre)
	if boo:
		print("Vous avez trouvé une lettre !")
		print("Mot : {}".format("".join(mot_list)))
	else:
		points -= 1
		print("Vous n'avez pas trouvé la bonne lettre... Essayez encore, il vous reste {} points".format(points))

if points > 0:
	score = fc.record(nom, points)
	print("Bravo {}, vous avez trouvé le mot ! Vous gagnez {} points et disposez d'un score de {}".format(nom, points, score))
else:
	print("Désolé, vous avez perdu... Le mot était {}".format("".join(mot_initial)))