Project Setup
--------------
- Create Python virtual environment using your favourite ``venv`` tool or ``conda``
- Setup project like so::

    pip install ".[dev,test]" .

- Recommend to use PyCharm IDE
- 4 spaces, no tab for indentation


Running Test Suite
------------------
- To run unit test suite::

    python -m unittest

- To run a specific test case::

    python -m unittest tests.test_cli.CLIUnitTests.test_upload

- To run with ``pytest``::

    py.test


Documentation
-------------
- Use Sphinx and reStructuredText
- Document sources are in ``sphinx/source/*.rst``
- Build doc like so::

    (cd sphinx && make clean)
    (cd sphinx && make html)

- Browse doc locally in ``sphinx/build/html/index.html``
- Build for github page::

    (cd sphinx && make github)

- If everything looks good, make all docs::

    make doc

