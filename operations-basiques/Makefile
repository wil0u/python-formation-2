# Nom du répertoire de l'environnement virtuel
VENV := ~/.venv

.PHONY: venv install editable test build clean activate

# Crée un environnement virtuel local
venv:
	python -m venv $(VENV)

# Affiche la commande pour activer l'environnement dans TON shell
activate:
	@echo ""
	@echo "Pour activer l'environnement virtuel, exécute :"
	@echo ""
	@echo "    source $(VENV)/bin/activate"
	@echo ""

# Installe les dépendances depuis requirements.txt
# (on suppose que le venv existe déjà)
install:
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt

# Installe le package en mode éditable (développement)
editable:
	$(VENV)/bin/pip install -e .

# Lance les tests unitaires
test:
	$(VENV)/bin/python -m unittest discover -s tests

# Construit le package (sdist + wheel) dans dist/
build:
	$(VENV)/bin/python -m build

# Nettoyage simple
clean:
	rm -rf $(VENV) dist *.egg-info