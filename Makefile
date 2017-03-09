PYTHONPATH := ${PWD}:${PYTHONPATH}
export

repl:
	@echo "--- opening repl"
	@python3 forest/interp/interp.py

repl-debug:
	@echo "--- opening repl in debug mode"
	@python3 forest/interp/interp.py --debug

test:
	@echo "--- running tests"
	@echo "We should probably run tests here..."

clean:
	@echo "--- cleaning"
	@find "." -type f -name "*.pyc" -delete
	@find "." -type d -name "__pycache__" -delete
