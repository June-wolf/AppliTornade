#-------------------------------------------------------------------------------
# Name:        AppliTornade.py
# Author:      <Jacquline><Achille><Lexy>
# Created:     10/11/2014
# Copyright:   (c) Lexy 2014
# Licence:     
#	The MIT License (MIT)
#	
#	Copyright (c) <2014> <copyright holders>
#
#	Permission is hereby granted, free of charge, to any person obtaining a copy
#	of this software and associated documentation files (the "Software"), to deal
#	in the Software without restriction, including without limitation the rights
#	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#	copies of the Software, and to permit persons to whom the Software is
#	furnished to do so, subject to the following conditions:
#
#	The above copyright notice and this permission notice shall be included in
#	all copies or substantial portions of the Software.
#
#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#	THE SOFTWARE.
#---------------------------------------------------------------------------------
#!/usr/bin/env python

run = 1
print(" ------------------------ ")
print("|Choisissez une saison : |")
print("|                        |")
print("|[1] Printemps           |")     #Bloc de choix des saisons
print("|[2] Eté                 |")
print("|[3] Automne             |")
print("|[4] Hivers              |")
print("|                        |")
print("|[0] Quitter             |")
print(" ------------------------ ")
saison = int(input())	                #L'utilisateur entre le numero de la saison choisie
print(" ------------------------ ")
print("|Choisissez un des       |")
print("|    dégats constatés :  |")
print("|                        |")
print("|[1] Maisons rasées      |")
print("|[2] Pt arbres cassés    |")     #Bloc de choix des conséquences
print("|[3] Toits arrachés      |")
print("|[4] Immeubles détruits  |")
print("|[5] Murs renversés      |")
print("|[6] Arbres déracinés    |")
print("|                        |")
print("|[0] Quitter             |")
print(" ------------------------ ")

consequence = int(input())              #L'utilisateur entre le numero de la consequence observee  

# NB : Retravailler la gestion des erreurs et du run
if(saison == 1):    #Si la saison choisie 
	print("Le printemps, plus précisément le mois de mai, peut être considéré comme la saison des tornades.") 
	print("En effet, 42% d’entre elles s’y produisent.")
	print("Au printemps les différences de température sur le front polaire sont maximales ; ")
	print("ce qui crée une atmosphère instable et favorise donc la formation de puissants orages.")
elif(saison == 2):
	print("Les températures chaudes de l'été sont propices à la formation d'orages, qui peuvent donner naissance à des tornades.")
elif(saison == 3):
	print("L'automne, saison plus fraiche, est donc moins propice aux tornades.")
elif(saison == 4):
	print("L'hivers étant une saison généralement très froide, elle n'est presque jamais propice à la création de tornades.")
else:
	run += 0
	
# Reflechir a creer une fonction saison et consequences separer, pour une meilleur gestion de l'affichage
if(consequence == 1):
	print("Echelle de Fujita = 4 / Vitesse du vent = 267-322 km/h / Type = Dévastateurs")
 	print("Maisons bien construites et maisons à charpente légère détruites, voitures soufflées à distance")
	print("et nombreux objets transformés en projectiles.")
elif(consequence == 2):
	print("Echelle de Fujita = 0 / Vitesse du vent = 105-137 km/h / Type = Légers") 
	print("Quelques morceaux de recouvrement de toit enlevés (tuile, etc.), dommages aux gouttières,")
	print("cheminées et revêtement de façade, branches cassées, arbres à racines de surface renversés")
elif(consequence == 3):
	print("Echelle de Fujita = 2 / Vitesse du vent = 179-218 km/h / Type = Considérables")
 	print("Toits soufflés sur des maisons bien construites, maisons à charpente légère déplacées de leurs fondations, ")
	print("maisons mobiles complètement détruites, gros arbres déracinés, objets légers devenus des projectiles, automobiles soulevées.")
elif(consequence == 4):
	print("Echelle de Fujita = 5 / Vitesse du vent = >322 km/h / Type = Incroyables")
	print("Maisons solides rasées et les débris projetés, objets de la grosseur d'une voiture projetés à plus de 100 mètres,") 
	print("gratte-ciels avec des dommages structuraux, etc.")
elif(consequence == 5):
	print("Echelle de Fujita = 3 / Vitesse du vent = 219-266 kkm/h / Type = Sévères")
	print("Étages complets de maisons solides détruits, dommages importants aux centres commerciaux et les centres d'affaires,")
	print("trains renversés, arbres écorcés, camions et grosses voitures déplacés, bâtiments légers complètement soufflés à distance")
elif(consequence == 6):
	print("Echelle de Fujita = 1 / Vitesse du vent = 138-178 km/h / Type = Modérés")
	print("Recouvrement de toit complètement enlevés, maisons mobiles endommagées sévèrement, portes extérieures envolées,")
	print("fenêtres et autres articles en verre cassés.")
else:
	run += 0
