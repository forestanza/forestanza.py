TARGS := $(shell sed -n 's/^\([-a-z]\+\):.*/\1/p' Makefile|sort -u|xargs)
.PHONY: $(TARGS)

all: test

run:
	./forestanza.py

test: test-exec
test-exec: export PYTHONPATH += .
test-exec:
	py.test -- $(shell pwd)
