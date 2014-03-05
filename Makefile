SOURCES := setup.py entangle

all:

test:
	@nosetests
	@flake8 $(SOURCES)

.PHONY: test
