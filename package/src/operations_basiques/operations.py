"""
Module contenant les opérations mathématiques basiques.

Deux fonctions simples sont proposées :

- multiplier(a, b)
- diviser(a, b)
"""


def multiplier(a, b):
    """
    Multiplie deux nombres.

    Parameters
    ----------
    a : float
        Premier opérande.
    b : float
        Deuxième opérande.

    Returns
    -------
    float
        Le produit de `a` et `b`.
    """
    return a * b


def diviser(a, b):
    """
    Divise un nombre par un autre.

    Parameters
    ----------
    a : float
        Numérateur.
    b : float
        Dénominateur (ne doit pas être égal à zéro).

    Returns
    -------
    float
        Le résultat de la division `a / b`.

    Raises
    ------
    ZeroDivisionError
        Si `b` vaut zéro.
    """
    return a / b