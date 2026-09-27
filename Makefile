install:
	brew install hugo
	pipenv install

# pull every #blog/publish note from the vault; ARGS=--prune removes posts whose note lost the tag
update-content:
	pipenv run python copy_from_vault.py $(ARGS)

preview-content:
	pipenv run python copy_from_vault.py --dry-run

build-site:
	hugo build --minify --cleanDestinationDir --destination docs

dev:
	hugo server -D --buildFuture

# import, build, and commit locally; review with `git show --stat` then push
publish: update-content build-site
	git add content static docs
	git commit -m "publish $$(date +%F)"
	git push
