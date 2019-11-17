# flcelery
flask + celery example

pipenv install

docker run -d -p 6379:6379 redis

celery worker -A workers --loglevel=info

pipenv run python app.py
