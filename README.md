# Movie Collector Application #

Movie Collector application is created as a coding project. It collects movies from [Ghibli Studio API](https://ghibliapi.herokuapp.com/). Basic functionality is refreshing the content viewed from /movies endpoint in 1 minute. Also, it should cache results to avoid sending API requests every time.

## Requirements

* Python 3.6.5+
* Flask
* flask-socketio
* Flask-Caching
* Celery

## Basic Usage

1. Preferably, create a new virtual environment.
2. Install dependencies by using following command:

```bash
pip install -r requirements/dev.txt
```

3. Run celery worker to update movies content. Celery beat is used for scheduling.

```bash
celery -A app.celery.celery worker -EB -l info
```

4. Run application.

```bash
python app.py
```

## To Run Tests

Use following command to run tests.

```bash
pytest
```

This project is supporting coverage, so you can type following command too.

```bash
coverage run -m pytest
```

After that, you can get a report by using:

```bash
coverage report
```

or 

```bash
coverage html
```

## Methodology

Celery beat is used to schedule celery task that recollects movies from the API and stores the result in the cache. Also, visitors already in the /movies are seeing updated content via socketio implementation. Hence, results are recollected every minute, and the request to API is limited.