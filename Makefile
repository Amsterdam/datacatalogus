.PHONY: submodules

GIT = git


submodules:
	git submodule update --recursive --remote

