PYTHONPATH := ${PWD}:${PYTHONPATH}
export

.PHONY: test clean

repl:
	@echo "--- opening repl"
	@python3 forest/forest.py

repl-debug:
	@echo "--- opening repl in debug mode"
	@python3 forest/forest.py --debug

test:
	@echo "--- running tests"
	pytest

clean:
	@echo "--- cleaning"
	@find "." -type f -name "*.pyc" -delete
	@find "." -type d -name "__pycache__" -delete
