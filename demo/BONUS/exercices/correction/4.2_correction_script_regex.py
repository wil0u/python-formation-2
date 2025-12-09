# le code de la fonction est compilé lorsque l'user fait import
import re 
import unidecode

# la fonction principale
def normalisation_heure(str_enentree):
    ch = unidecode.unidecode(str_enentree.lower())
    ch = ch.replace("heures","h").replace("heure","h").replace(" et ",", ")
    split_ch = ch.split(',')
    res = []
    for element in split_ch :
        # pattern 10h30, 10 h 30 
        if re.search("[0-9]{1,2}\s{0,1}[h]\s{0,1}[0-9]{1,2}",element):
            res+= [re.sub("([0-9]{1,2})\s{0,1}[h]\s{0,1}([0-9]{1,2})","\\1h\\2",element)]
        # pattern 10h 10 h
        elif re.search("[0-9]{1,2}\s{0,1}[h]",ch):
            res+=[re.sub("([0-9]{1,2})\s{0,1}[h]","\\1h",element)]
        else:
            res+= [element]
    return ",".join(res)

#test unitaire
chaine="bla bla"
normalisation_heure(chaine)



# fonction main c'est une convention
# son code contient l'execution des autres fonctions
# on ne met pas le code dans la fonction main() mais plutot l'appel aux sous taches
# ainsi chaque sous tache est bien une fonction independante
def main():
    while True:
        print("Test d'une regex à normaliser")
        s=str(input("saisir une chaine libre contenant du texte :"))    

        s=normalisation_heure(s)
        print("Après Regex")

        print("Résultat :{}".format(s))

# main : exécuté lorsque le pgm est lancé comme pgm principal notamment quand on lance en shell
if __name__=="__main__":
    main()