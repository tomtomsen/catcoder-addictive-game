.PHONY: default
default: run

.PHONY: run
run: test clean
	python main.py

.PHONY: test
test:
	python -m unittest

.PHONY: clean
clean:
	-@rm data/out/*.out
