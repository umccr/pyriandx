help:
	@echo 'make doc'

install:
	@pip install '.[test,dev]'
	@pre-commit install

check:
	@pre-commit run --all-files

scan:
	@ggshield secret scan repo .

doc:
	@(cd sphinx && make github)
	@pdoc --force --html pyriandx -o docs/
	@py.test --cov-report html:docs/coverage --cov=pyriandx tests/
	@rm -rf docs/.buildinfo
	@rm -rf docs/coverage/status.json

test:
	@pytest

tox:
	@tox -vv

nose:
	@nose2 -vv

clean:
	@rm -rfv build/
	@rm -rfv pyriandx.egg-info/

.PHONY: dist
dist: clean
	@python3 -m build

# Usage: make ver version=0.1.0
ver: dist/pyriandx-$(version).tar.gz
	@echo $(version)

testpypi: dist/pyriandx-$(version).tar.gz
	@python3 -m twine upload --repository testpypi dist/pyriandx-$(version).tar.gz
	@python3 -m twine upload --repository testpypi dist/pyriandx-$(version)-*.whl

pypi: dist/pyriandx-$(version).tar.gz
	@python3 -m twine upload dist/pyriandx-$(version).tar.gz
	@python3 -m twine upload dist/pyriandx-$(version)-*.whl
