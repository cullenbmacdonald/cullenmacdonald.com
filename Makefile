install:
	brew install hugo pandoc
	pipenv install

update-content:
	pipenv run python copy_from_vault.py

build-site:
	hugo build
	mkdir -f docs
	mv public/* docs/

dev:
	hugo server -D
