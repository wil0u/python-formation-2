# le code de la fonction est compilé lorsque l'user fait import
import re 
import unidecode

# la fonction principale
def chercheautonomie(str_enentree):
    ch = unidecode.unidecode(str_enentree.lower())
    ch = str_enentree.replace("heures","h").replace("heure","h")
    if re.search("[0-9]{1,2}\s{0,1}[h]\s{0,1}[0-9]{1,2}",ch):
        return re.sub("([0-9]{1,2})\s{0,1}[h]\s{0,1}([0-9]{1,2})","-autonomie:\\1h\\2-",ch)
    elif re.search("[0-9]{1,2}\s{0,1}[h]",ch):
        return re.sub("([0-9]{1,2})\s{0,1}[h]","-autonomie:\\1-",ch)
    else:
        return str_enentree

#test unitaire
chaine="bla bla"
chercheautonomie(chaine)



# fonction main c'est une convention
# son code contient lexecution des autres fonctions
# on ne met pas le code dans la fonction main() mais plutot l'appel aux sous taches
# ainsi chaque sous tache est bien une fonction independante
def main():
    while True:
        print("Test d'une regex qui cherche l'autonomie")
        s=str(input("saisir une chaine libre contenant du texte :"))    

        s=chercheautonomie(s)
        print("Après Regex")

        print("Résultat :{}".format(s))

# main : exécuté lorsque le pgm est lancé comme pgm principal notamment quand on lance en shell
if __name__=="__main__":
    main()