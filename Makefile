lint:
	pylint -j 0 mdtable
	pylint -j 0 tests

test:
	pytest --cov=mdtable tests --cov-report term-missing
