import argparse
from pathlib import Path

import numpy as np
import pandas as pd


if __name__ == "__main__":
    # -----------------------------------
    # 1. Definition de la commande
    # -----------------------------------
    parser = argparse.ArgumentParser(
        prog="standardisation",
        description="Standardise une serie de nombres.",
    )

    parser.add_argument(
        "values",
        nargs="*",
        type=float,
        help="Valeurs numeriques a standardiser",
    )
    parser.add_argument(
        "--csv",
        type=Path,
        help="Chemin vers un fichier CSV",
    )
    parser.add_argument(
        "--column",
        type=str,
        help="Nom de la colonne a standardiser",
    )
    parser.add_argument(
        "--sep",
        type=str,
        default=";",
        help="Separateur du CSV",
    )

    args = parser.parse_args()

    # -----------------------------------
    # 2. Lecture des donnees
    # -----------------------------------
    if args.csv and args.values:
        parser.error("Choisissez soit des valeurs directes, soit --csv.")

    if not args.csv and not args.values:
        parser.error("Donnez des valeurs ou utilisez --csv.")

    if args.csv:
        if not args.column:
            parser.error("Avec --csv, il faut aussi --column.")

        if not args.csv.exists():
            parser.error(f"Fichier introuvable : {args.csv}")

        dataframe = pd.read_csv(args.csv, sep=args.sep)

        if args.column not in dataframe.columns:
            parser.error(f"Colonne introuvable : {args.column}")

        values = pd.to_numeric(dataframe[args.column], errors="coerce").dropna().to_numpy(dtype=float)

        if len(values) == 0:
            parser.error("La colonne ne contient pas de valeurs numeriques.")
    else:
        values = np.array(args.values, dtype=float)

    # -----------------------------------
    # 3. Standardisation
    # -----------------------------------
    mean = values.mean()
    std = values.std()

    if std == 0:
        print("Erreur : impossible de standardiser une serie constante.")
    else:
        standardized = (values - mean) / std

        # -----------------------------------
        # 4. Affichage du resultat
        # -----------------------------------
        print("Valeurs d'entree :")
        print(np.array2string(values, precision=3, separator=", "))

        print("\nValeurs standardisees :")
        print(np.array2string(standardized, precision=3, separator=", "))

        print(f"\nMoyenne finale : {standardized.mean():.6f}")
        print(f"Ecart-type final : {standardized.std():.6f}")
