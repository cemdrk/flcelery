# flcelery
flask + celery example


docker run -d -p 6379:6379 redis

celery worker -A workers --loglevel=info

python app.py

pipenv run python app.py
