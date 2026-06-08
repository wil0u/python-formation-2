# operations-basiques

Petit exemple de package Python très simple, contenant deux opérations
mathématiques basiques : `multiplier` et `diviser`.

## Installation en local (développement)

Depuis la racine du projet :

#### 1. Créer le venv une fois
make venv

#### 2. (Optionnel mais conseillé) voir la commande d’activation
make activate
source .venv/bin/activate

#### 3. Installer les dépendances de dev
make install

#### 4. Installer ton package en mode éditable
make editable

#### 5. Lancer les tests
make test

#### 6. Builder le package
make build

operations-basiques/
├─ pyproject.toml
├─ README.md
├─ Makefile
├─ requirements.txt
├─ src/
│  └─ operations_basiques/
│     ├─ __init__.py
│     ├─ operations.py
└─ tests/
   └─ test_operations.py