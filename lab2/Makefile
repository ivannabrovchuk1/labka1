.DEFAULT_GOAL:= all
all:install test run deploy

install:
	@echo "installing pipenv and dependencies."
	pipenv --python 3.8
	pipenv install requests
	pipenv install ntplib
	pipenv install pytest

test:
	@echo "start tests."
	pipenv run pytest tests/tests.py >> results.txt

run:
	@echo "run python app."
	python app.py >> results.txt

deploy:
	@echo "adding and committing results.txt to git"
	git add results.txt
	git commit
	git push origin master
