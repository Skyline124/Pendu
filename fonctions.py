# -*- coding: utf-8 -*-
import re
import donnees as d
from random import randrange
import pickle as pk

def score(nom):
	""" Récupère le score de l'utilisateur <nom>.
	Si le fichier n'existe pas, on le crée et on 
	envoie un dictionnaire avec juste un utilisateur dedans.
	Si l'utilisateur n'est pas dans la base de données, on 
	le crée avec un solde initial nul.
	"""
	try:
		f = open(d.nom_fichier_scores,'rb')
	except FileNotFoundError:
		f = open(d.nom_fichier_scores,'wb')
		pk.dump({'Grégoire': 23},f)
		f.close()
		return 0

	scores = pk.load(f)

	try:
		return scores[nom]
	except KeyError:
		f.close()
		scores[nom] = 0
		f = open(d.nom_fichier_scores,'wb')
		pk.dump(scores,f)
		f.close()
		return 0


	

def init():
	""" On récupère un mot au hasard dans la liste de mot
	et ensuite on coupe ce mot en deux listes de lettres,
	l'une en "claire" et l'autre "masquée" que l'on affiche
	à l'utilisateur.
	"""
	n = randrange(0, len(d.liste_mots))
	mot = d.liste_mots[n]
	mot_initial = list(mot)
	mot_list = list(mot)
	for i in range(1, len(mot_initial)-1):
		mot_list[i] = ' _ '
	return mot_initial, mot_list


def ask():
	""" demande une letrte à l'utilisateur et la renvoie si
	c'est bien une lettre. 
	"""
	l = input("Devinez une lettre : ")
	if re.match("^[A-Za-z]{1}$",l):
		return l.lower()
	else:
		print("Erreur d'entrée !")
		ask()

def check(mot_initial, mot_list, lettre):
	""" Check si la lettre donnée en paramètre n'as pas encore été
	trouvée si elle est contenue dans le mot, renvoie le mot avec la lettre
	trouvée si oui avec True, et ne fait rien et renvoie False sinon.
	"""
	boo = False
	for i in range(1, len(mot_initial) - 1):
		if lettre == mot_initial[i]:
			mot_list[i] = lettre
			boo = True
	return mot_list, boo

def end(mot_list):
	"Check si le mot a été trouvé en entier"
	return re.findall("(_)","".join(mot_list)) == []
	
def record(nom, points):
	"Enregistre les points supplémentaires pour l'utilisateur nom."
	f = open("scores","rb")
	dico = pk.load(f)
	f.close()
	dico[nom] += points
	f = open("scores","wb")
	pk.dump(dico, f)
	f.close
	return dico[nom]



	