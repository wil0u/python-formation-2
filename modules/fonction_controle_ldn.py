# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 20:28:29 2019

@author: DGA
"""

# exemples
"""
LE MANS
ROANNE (42)
SAINT-GERMAIN-EN-LAYE
Fontenay-aux-Roses
Marly-le-Roi
BAGNOLS-SUR-CEZE
BAGNOLS SUR CEZE
BAGNOLS SUR CÈZE

"""
# tips
#'MonsieurDAMIEN'.startswith('Monsieur')
#'GARROUSTEnée'.endswith("née")



def controle_LDN(string,liste_lieux):
    """
    passe tout en maj
    remplace les ( par des blancs, cela permet de regler les cas comme Paris(75) 
    
    cas 0 : toute la chaine matche avec le ref => OK
    cas 1 : 1 mot sans departement
        - tester si ce nest pas un nombre et 
        - si pas 
            => Controle dans une liste de lieux => OK
            si ce n'est pas dans liste => KO
            
    cas 2 : 2 mot
     - avec à la fin  INT comme Paris 75 ou PARIS 75015
            => OK
        - si pas de INT => LE MANS
            => Controle dans une liste de lieux => OK
            si ce n'est pas dans liste => KO
            
    cas 3 : 3 mots et +
        - LE MANS (72)
        MARLY LE ROI
        MARLY LE ROI 78
        
        
    """
    
    
    controle=-1
    cas=''
    # on modifie le texte pour que ca corresponde a liste et attention aux car speciaux
    string=' '+string.upper().replace(',',' ').replace('(',' ').replace(')',' ')+' '
    mots=string.split()
    nbmots_dsentite=len(mots)
    #print (string)
    # toute la chaine matche avec le ref
    if string.strip() in liste_lieux:
        cas="OK entité est dans le ref"
        controle=1
    # à partir de 5 mots KO
    elif nbmots_dsentite>4:
        conforme=0
        cas='KO >4 mots'
    # 1 mot en chiffre
    elif nbmots_dsentite==1 and string.isdigit()==True:
        conforme=0
        cas='KO 1 mot en chiffres'
    elif nbmots_dsentite==1:
        # est ce que le mot est dans le ref
        if mots[0] in liste_lieux:
            cas="OK 1 mot=Lieu"+w
            controle=1
        # est ce qu'on utilise le fait que le mot etait en maj ou capitalisé = à voir
        else:
            cas="KO 1 mot != lieu"
            # afficher ces cas et ajouter manuellement au référentiel
            controle=0
    elif nbmots_dsentite==2:

            
        # cas général  1 lieu 1 dpt
        if mots[0] in liste_lieux:
            if mots[1].isdigit()==True:
                cas="OK 2 mots : 1 lieu, 1 dept"
                controle=1
            else:
                cas="KO 2 mots : 1 lieu + ?"
                # afficher ces cas pour voir si c'est pas des departements en texte comme Mazamet(tarn)
                controle=0
        # autres 1 mot 1 dpt
        elif mots[1].isdigit()==True:
             cas="OK 2 mots : 1 mot, 1 dept"
             # afficher ces cas pour ajouter au référentiel
             controle=1
        else:
            cas="KO 2 mots : 1 mot + ?"
            # afficher ces cas pour voir si c'est pas des departements en texte comme Mazamet(tarn)
            controle=0
    
    elif nbmots_dsentite>=3:
        last=mots[-1]
        # on regarde si la chaine sans le dernier mot est dans le référentiel
        if string.replace(last,'').strip() in liste_lieux:
            if last.isdigit()==True:
                cas='OK lieu lieu ... dept'
                controle=1
            else:
                cas="KO la chaine commence par un lieu mais finit par autre chose qu'un num"
                controle=0
        else:
            if last.isdigit()==True:
                cas='OK mot mot ... dept'
                controle=1
            else:
                cas="KO la chaine ne commence par un lieu et finit par autre chose qu'un num"
                controle=0
            
                
    return (controle,cas)
            
# =============================================================================
# TEST DE LA FONCTION SUR DIFFERENTS CAS    
# =============================================================================

cl="Damien né à Fontenay Aux roses"
cl="Virginie née à Saint-Germain en Laye"
cl="Fontenay Aux roses"
cl="Fontenay Aux roses"
cl="Le mans (72)"

cl="Saint-joseph-de-porterie"


cl="Saint-germain-en-LAYE"

cl="Saint-germain-en-LAYE 78"
cl="BAGNOLS SUR CÈZE 83"

cl="BAGNOLS SUR CÈZE PARIS"

cl="MAZAMET TARN"
%timeit controle_LDN(cl,liste_lieux)