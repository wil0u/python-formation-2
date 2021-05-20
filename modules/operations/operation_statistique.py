
def moyenne(list_numbers):
    from functools import reduce
    
    try:
        moy = reduce((lambda x,y: x+y), list_numbers)/len(list_numbers)
        return moy
    except:
        print("La moyenne se calcule avec des nombres.\nEt merci de les mettre dans une liste pour cette fonction ;-)")



def somme(list_numbers):
    from functools import reduce
    
    try:
        som = reduce((lambda x,y: x+y), list_numbers)
        return som
    except:
        print("La somme se calcule avec des nombres.\nEt merci de les mettre dans une liste pour cette fonction ;-)")


