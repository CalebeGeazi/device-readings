# Device Readings API

Written using [Django](https://www.djangoproject.com/) and [Django Rest Framework](https://www.django-rest-framework.org/). With the help of [Pydantic](https://docs.pydantic.dev/latest/) for data validation and serializing Model Objects.

## Prerequisites
Please make sure you have Python 3.10^ installed, and if not please install the [latest Python3](https://www.python.org/downloads/) version to get started. After installing `Python3`, you can now install [poetry](https://python-poetry.org/docs/#installation). This project uses `poetry` to manage dependencies. Please follow the instructions on the poetry site for installing, I recommend installing with `pipx`, but feel free to use whatever option works best for you.

## Quick start
Now that `poetry` is installed, we're ready to get started!

1. First, let's start by cloning this repo and then `cd` to the root directory of this project.
2. Let's activate a virtual env for our `python` project:
```sh
eval $(poetry env activate)
```

3. Verify the python version being used for this project:
```sh
which python # you should see something like: ~/.cache/pypoetry/virtualenvs/device-readings-9Av4IO8W-py3.10/bin/python
python --version # you should get python 3.10^
```

4. Install dependencies:
```sh
poetry install
```

5. Once all the dependencies are installed we can start the app:
```sh
python manage.py runserver
```

6. Open your browser to http://localhost:8000/api/devices

## API Endpoints
Here are all the endpoints this API supports:

1. GET `http://localhost:8000/api/devices` - fetches all devices and their corresponding readings
2. POST `http://localhost:8000/api/devices` - save device readings. Request body must be in JSON. Example:
```json
{
    "id": "36d5658a-6908-479e-887e-a949ec199272",
    "readings": [
        {
            "timestamp": "2021-09-29T16:08:15+01:00",
            "count": 2
        },
        {
            "timestamp": "2021-09-29T16:09:15+01:00",
            "count": 15
        }
    ]
}
```
3. GET `http://localhost:8000/api/devices/<ID>` - fetches all readings for a given device ID in the request path. Will return a `404` if device is not found.
4. GET `http://localhost:8000/api/devices/<ID>/sum` - fetches the sum of all the counts for a given device ID in the request path. Will return a `404` if device is not found.
5. GET `http://localhost:8000/api/devices/<ID>/latest` - fetches the timestamp for the latest reading for a given device ID in the request path. Will return a `404` if device is not found.

Feel free to import the [included Postman Collection](https://github.com/CalebeGeazi/device-readings/blob/main/Device%20Readings%20API.postman_collection.json) to interact with this API.

## Project Structure
This project is structured with a Model class that defines the Device and Reading objects. In addition to an InMemoryDevices object for storing device data. This is laid out in the `./device_readings/api/` directory.

- `urls.py` - is used as the API router.
- `models.py` - defines our models.
- `views.py` - is where the endpoint implementations live.
- `apps.py` - registers this app 

## Running Tests
To run tests:
```sh
poetry run pytest -vv
```

To run tests with coverage report:
```sh
poetry run coverage run -m pytest && coverage report
```

## Additional Improvenments/Optimizations
If given more time here's a list of improvements and optimizations I would have like to add.

1. Use an in-memory Redis Cache for storing the devices data. This would allow for use of distributed cache for better perfromance and scalability.
2. Better Swagger API documentation. This project does include Swagger docs at `http://localhost:8000/swagger/`, however, better descriptions and API use needs to be added for it to be more useful.
3. Better CI/CD Pipeline with Github Actions. I did include a basic Github Action for running tests on the `main` branch, however, there are many improvements that could be made to ensure code quality and testings. In addition to just running the tests, the pipeline could also run a linter to verify the code meets standards as well as a code-coverage check to ensure the project maintains a high test coverage threshold.
4. Use docker for seemless installation and running of project.
