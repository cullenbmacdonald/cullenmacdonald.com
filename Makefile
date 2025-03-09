install:
	brew install hugo pandoc
	pipenv install

update-content:
	pipenv run python copy_from_vault.py

build-site:
	hugo build
	find docs -type f ! -name 'CNAME' -delete
	find docs -type d -empty -delete
	mkdir -p docs
	mv public/* docs/

dev:
	hugo server -D
