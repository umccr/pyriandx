help:
	@echo 'make doc'

doc:
	@(cd sphinx && make github)
	@pdoc --force --html pyriandx -o docs/
	@py.test --cov-report html:docs/coverage --cov=pyriandx tests/

test:
	@pytest

dist:
	@python setup.py sdist bdist_wheel

clean:
	@rm -rfv build/ dist/
