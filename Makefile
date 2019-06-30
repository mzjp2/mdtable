lint:
	pylint -j 0 mdtable
	pylint -j 0 tests

test:
	pytest --cov=mdtable tests --cov-report term-missing --no-cov-on-fail --cov-config=.coveragerc

deploy:
	rm dist/*
	python3 setup.py bdist_wheel
	twine upload dist/*
