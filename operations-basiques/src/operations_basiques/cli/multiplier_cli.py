"""
CLI simple pour multiplier deux nombres.

Cette commande permet de multiplier deux nombres, avec éventuellement :
- un arrondi du résultat à un certain nombre de décimales
- un mode verbeux

Arguments
---------
a : premier nombre (positionnel)
b : deuxième nombre (positionnel)

Options
-------
-d, --decimales, --decimal : nombre de décimales pour l'affichage du résultat
-v, --verbose              : affiche une phrase explicative en plus du résultat

Exemples d'utilisation
----------------------

Appel simple (résultat brut) :

    operations-multiplier 2 3

Avec arrondi à 3 décimales (plusieurs variantes équivalentes) :

    operations-multiplier -d 3 2 3
    operations-multiplier -d=3 2 3
    operations-multiplier --decimales 3 2 3
    operations-multiplier --decimales=3 2 3
    operations-multiplier --decimal 3 2 3
    operations-multiplier --decimal=3 2 3

En mode verbeux (affiche une phrase explicative) :

    operations-multiplier -v 2 3
    operations-multiplier --verbose 2 3

Combiner verbeux + décimales :

    operations-multiplier -v -d 4 2 3
    operations-multiplier --verbose --decimal=4 2 3
"""

import argparse
from operations_basiques.operations import multiplier


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Multiplie deux nombres."
    )

    # Nombres positionnels
    parser.add_argument("a", type=float, help="Premier nombre.")
    parser.add_argument("b", type=float, help="Deuxième nombre.")

    # Option : nombre de décimales pour arrondir le résultat
    parser.add_argument(
        "-d",
        "--decimales",
        "--decimal",
        type=int,
        default=None,
        dest="decimales",
        help="Nombre de décimales pour l'affichage du résultat.",
    )

    # Flag : mode verbeux
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Affiche un message explicatif en plus du résultat brut.",
    )

    args = parser.parse_args()

    result = multiplier(args.a, args.b)

    if args.decimales is not None:
        result = round(result, args.decimales)

    if args.verbose:
        print(f"Résultat de la multiplication de {args.a} par {args.b} : {result}")
    else:
        print(result)


if __name__ == "__main__":
    main()