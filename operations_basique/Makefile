.PHONY: venv install editable run build clean

venv:
	python -m venv .venv2

install:
	python -m venv .venv2
	.venv2/Scripts/python -m pip install --upgrade pip
	.venv2/Scripts/python -m pip install -r requirements.txt

editable:
	.venv2/Scripts/python -m pip install -e .

run:
	.venv2/Scripts/python script.py

build:
	.venv2/Scripts/python setup.py sdist bdist_wheel

clean:
	python -c "import shutil, pathlib; \
	[shutil.rmtree(p, ignore_errors=True) for p in ('build','dist','.venv2')]; \
	[shutil.rmtree(str(path), ignore_errors=True) for path in pathlib.Path('.').glob('*.egg-info')]"
