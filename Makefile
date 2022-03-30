SHELL:=/usr/bin/env bash

default: help
# via https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build: fix-attachment-permissions  ## Perform a one off build to ./_site
	rm -rf ./_site
	@mkdir -p .docker-vendor/bundle
	docker run --rm -it \
		--volume="$(PWD):/srv/jekyll" \
		--volume="$(PWD)/.docker-vendor/bundle:/usr/local/bundle" \
		--env JEKYLL_ENV=production \
		jekyll/jekyll:4 \
		jekyll build

.PHONY: clean
clean:  ## Remove all generated files: destination folder, metadata file, Sass and Jekyll caches
	rm -rf ./_site
	docker run --rm -it \
		--volume="$(PWD):/srv/jekyll" \
		--volume="$(PWD)/.docker-vendor/bundle:/usr/local/bundle" \
		jekyll/jekyll:4 \
		jekyll clean

.PHONY: serve
serve:  ## Serve the site locally, rebuilding it any time a source file changes
	rm -rf ./_site
	@mkdir -p .docker-vendor/bundle
	docker run --rm \
		--volume="$(PWD):/srv/jekyll" \
		--volume="$(PWD)/.docker-vendor/bundle:/usr/local/bundle" \
		--env JEKYLL_ENV=development \
		--name fesite_jekyll_preview \
		-p 4002:4000 \
		-p 35729:35729 \
		jekyll/jekyll:4 \
		jekyll serve --livereload &
	./scripts/_wait_url "http://localhost:4002"
	@echo ""
	@echo "Access the site at: http://localhost:4002"
	@echo "Run 'make stop' to stop the server."
	@echo ""
	@osascript -e "tell application \"Safari\" to make new document with properties {URL:\"http://localhost:4002/$$SERVE_PAGE\"}"
	@osascript -e "tell application \"Safari\" to activate"

.PHONY: stop
stop:  ## Stop the local preview server started via 'serve'
	docker kill --signal="SIGINT" fesite_jekyll_preview

.PHONY: deploy
deploy: build  ## Deploy to https://fatalerror.fm
	rsync -avz --delete _site/ cdzombak@burr.cdzombak.net:/home/cdzombak/www/fatalerror/production/
	@terminal-notifier -title "fatalerror.fm" -message "Deployed Production" -open "https://fatalerror.fm"

.PHONY: open
open:  ## Open the production website
	@open "https://fatalerror.fm"

.PHONY: fix-attachment-permissions
fix-attachment-permissions:
	# Fix permissions on files that come from my NAS over SMB
	chmod -x attachments/*.mp3
	chmod 644 attachments/*.mp3
