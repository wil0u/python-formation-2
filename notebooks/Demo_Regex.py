# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:54:35 2020

@author: RND
"""


import re

##############################
# re.match vs re.search
##############################
    # Vérifier si une expression est présente dans une chaine de charactère
expression = "Romeo"
chaine1 = "je suis Romeo, merci"
chaine2 = "Romeo est mon prénom"


if re.match(expression, chaine2) is not None:
    print("l'expression est en début de la chaîne")

if re.search(expression, chaine1):
    print("l'expression est dans la chaîne")


##############################
# re.search
##############################
    # Vérifier qu'un numero de téléphone est valide """
chaine = ""
expression = r"^0[0-9]([ .-]?[0-9]{2}){4}$"
while re.search(expression, chaine) is None:
    chaine = input("Saisissez un numéro de téléphone (valide) :")


##############################
# re.compile
##############################
    # vérifier qu'un mot de passe fait au moins 8 caractères 
    # et qu'il ne contient que des lettres majuscules, minuscules et des chiffres

chn_mdp = r"^[A-Za-z0-9]{8,}$"
exp_mdp = re.compile(chn_mdp)
mot_de_passe = ""
while exp_mdp.search(mot_de_passe) is None:
    mot_de_passe = input("Tapez votre mot de passe : ")


##############################
# re.sub
##############################
    # substituer une expression par une autre dans une chaine de charactère
chaine = "Voici mon adresse mail: roméo@gmail.com "

chaine = re.sub(r"[éèêë]", "e", chaine)
chaine = re.sub(r"\S*@\S*\s?", " ", chaine)  # Remove Emails

