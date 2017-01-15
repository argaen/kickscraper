syntax:
	flake8

pylint:
	pylint --disable=C0111 aiocache

acceptance:
	pytest -sv tests/acceptance
