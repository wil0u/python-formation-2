"""
CLI simple pour diviser deux nombres.

Cette commande permet de diviser un nombre par un autre, avec :
- gestion de la division par zéro (message d'erreur clair)
- possibilité d'arrondir le résultat
- option de mode verbeux

Arguments
---------
a : numérateur (positionnel)
b : dénominateur (positionnel, non nul)

Options
-------
-d, --decimales, --decimal : nombre de décimales pour l'affichage du résultat
-v, --verbose              : affiche une phrase explicative en plus du résultat

Exemples d'utilisation
----------------------

Appel simple (résultat brut) :

    operations-diviser 10 2

Avec arrondi à 2 décimales (plusieurs variantes équivalentes) :

    operations-diviser -d 2 10 3
    operations-diviser -d=2 10 3
    operations-diviser --decimales 2 10 3
    operations-diviser --decimales=2 10 3
    operations-diviser --decimal 2 10 3
    operations-diviser --decimal=2 10 3

En mode verbeux :

    operations-diviser -v 10 2
    operations-diviser --verbose 10 2

Combiner verbeux + décimales :

    operations-diviser -v -d 4 10 3
    operations-diviser --verbose --decimal=4 10 3

Cas de division par zéro (affiche un message d'erreur) :

    operations-diviser 10 0
"""

import argparse
from operations_basiques.operations import diviser


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Divise un nombre par un autre."
    )

    # Nombres positionnels
    parser.add_argument("a", type=float, help="Numérateur.")
    parser.add_argument("b", type=float, help="Dénominateur (non nul).")

    parser.add_argument(
        "-d",
        "--decimales",
        "--decimal",
        type=int,
        default=None,
        dest="decimales",
        help="Nombre de décimales pour l'affichage du résultat.",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Affiche un message explicatif en plus du résultat brut.",
    )

    args = parser.parse_args()

    try:
        result = diviser(args.a, args.b)
    except ZeroDivisionError:
        parser.error(
            "Erreur : division par zéro interdite "
            "(le deuxième nombre ne doit pas être 0)."
        )

    if args.decimales is not None:
        result = round(result, args.decimales)

    if args.verbose:
        print(f"Résultat de la division de {args.a} par {args.b} : {result}")
    else:
        print(result)


if __name__ == "__main__":
    main()