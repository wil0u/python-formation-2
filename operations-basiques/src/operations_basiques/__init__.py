"""
Package `operations_basiques`.

Ce package contient des opérations mathématiques très simples
et quelques petites interfaces en ligne de commande (CLI).

Structure du package
--------------------

- `operations_basiques.operations` :
    Contient les fonctions de base :
    - `multiplier(a, b)`
    - `diviser(a, b)`

- `operations_basiques.cli` :
    Sous-package qui regroupe les scripts de ligne de commande basés sur `argparse` :
    - `operations_basiques.cli.multiplier_cli` : logique pour la commande `operations-multiplier`
    - `operations_basiques.cli.diviser_cli`    : logique pour la commande `operations-diviser`

Utilisation en Python
---------------------

>>> from operations_basiques.operations import multiplier, diviser
>>> multiplier(2, 3)
6
>>> diviser(10, 2)
5.0

Utilisation en ligne de commande
--------------------------------

Après installation du package (par exemple avec `pip install .`
ou `pip install -e .` dans un environnement virtuel), deux commandes
sont disponibles :

    operations-multiplier 2 3
    operations-diviser 10 2

Quelques variantes avec options :

    operations-multiplier --decimales=3 2 3
    operations-diviser --decimal=4 10 3
    operations-multiplier --verbose 2 3
    operations-diviser --verbose --decimales=2 10 3
"""