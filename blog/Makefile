install:
	brew install hugo
	pipenv install

update-content:
	pipenv run python copy_from_vault.py

dev:
	hugo server -D