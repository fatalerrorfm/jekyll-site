SHELL:=/usr/bin/env bash

default: help
# via https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: bootstrap
bootstrap:  ## Install dependencies (gems in ./vendor/bundle)
	# https://github.com/castwide/vscode-solargraph/issues/78#issuecomment-538124124
	SDKROOT=/Library/Developer/CommandLineTools/SDKs/MacOSX10.14.sdk/ \
	bundle install --path vendor/bundle

.PHONY: build
build:  ## Perform a one off build to ./_site
	bundle exec jekyll doctor
	bundle exec jekyll build

.PHONY: clean
clean:  ## Remove all generated files: destination folder, metadata file, Sass and Jekyll caches
	bundle exec jekyll clean

.PHONY: serve
serve:  ## Serve the site locally, rebuilding it any time a source file changes
	bundle exec jekyll serve
