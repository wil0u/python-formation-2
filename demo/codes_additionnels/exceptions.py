class MyCustomError(Exception):
    """Exception levée quand une condition spécifique est rencontrée."""
    pass

# Une fonction pouvant engendrer des exceptions, erreurs etc.
def risky_operation():
    #return
    raise MyCustomError()

try:
    # Code qui peut lever plusieurs types d'exceptions
    risky_operation()
    
except ValueError as e:  # exception spécifique
    print("Erreur de valeur:", e)

except KeyError as e:  # autre exception spécifique
    print("Clé manquante:", e)

except (TypeError, IndexError) as e:  # grouper plusieurs exceptions
    print("Erreur de type ou d'index:", e)

except Exception as e:  # attrape toutes les autres exceptions
    print("Autre exception:", type(e).__name__, e)
finally:
    print("Ce bloque est tout le temps exécuté")
 