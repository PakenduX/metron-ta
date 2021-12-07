# Metron TA

Metron TA to manage an industrial site. 
The site has a manager and can have multiple assets.

### Requirements
##### Using python virtual environ
###### Install python
- Install `python 3.10` on your system.
- Create and activate a python virtual environment
    - `python -m venv env_name`
    - `source env_name/bin/activate`
- Install all the packages using `requirements.txt` file.
  `pip install -r requirements.txt`

###### Install mariadb
- Install `mariadb` on your system.
- create and grant access to a new user with username: `metron` and password `metron`
- create a database called `MetronTA`

You're now up to start the application.
##### Using docker
You can also install `docker` on your system to run the app within a docker container.

## Features

- Register and login of the manager
- All the CRUD operations for Manager, Site and Asset
## Build and execution

### Launch the API
##### Using python virtual env
In your folder `metron-ta` and your activated virtual environment you just created above run the command:

```
flask run
```
Your server will listen on http://127.0.0.1:5000
##### Using docker
In your folder `metron-ta` simply run :
```
 docker-compose up --build
```
Your server will listen on http://127.0.0.1:9000
### Launch the tests
##### Using virtual environment
in the same folder `metron-ta` launch the command :

```
python -m pytest --setup-show
```
##### Using docker

To launch to unit tests simply run :
```
docker exec metron_api python -m pytest --setup-show
```

### Test with POSTMAN

You can use the postman collection `METRON_API_COLLECTION.postman_collection.json` with environment variables `METRON_API_ENV.postman_environment.json` to test the API.

## TODO

- [ ] Add more tests case
- [ ] Add logout
- [ ] Add token blacklist
