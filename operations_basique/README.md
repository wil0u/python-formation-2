# operations-basique

Petit package Python avec des opérations arithmétiques basiques rangées dans `src/operations_basique`.

## Structure
- `src/operations_basique/` : fonctions `add`, `subtract`, `multiply`, `divide`.
- `script.py` : exemple très simple qui importe le package et affiche une addition et une multiplication.
- `Makefile` : commandes pédagogiques pour créer l'environnement, l'activer, installer les dépendances, lancer le script ou fabriquer une distribution.

## Utilisation
```bash
make venv       # crée .venv
make install    # active .venv et installe les requirements
make run        # exécute script.py dans l'environnement
make build      # produit sdist + wheel
make clean      # supprime artefacts

# installation editable
.venv\Scripts\pip install -e .
```
