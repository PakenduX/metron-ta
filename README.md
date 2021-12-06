# Metron TA

Metron technical assessment to manage an industrial site. 
The site has a manager and can have multiple assets.

### Requirements
##### Using python virtual environ
- Install `python 3.10` on your system.
- Create and activate a python virtual environment
    - `python -m venv env_name`
    - `source venv/bin/activate`
- Install all the packages using `requirements.txt` file.
  `pip install -r requirements.txt`

You're now up to start the application.
##### Using docker
You can also install `docker` on your system to run the app in a docker container.

## Features

- Register and login of the manager
- All the CRUD operations for Manager, Site and Asset
## Build and execution

### Launch the API
##### Using python virtual env
in your folder `metron-ta` and your activated virtual environment you just created above run the command:

```
flask run

```

##### Using docker
Coming soom
### Launch the tests
in the same folder `metron-ta` launch the command :

```
python -m pytest

```

## TODO

- [ ] Add more tests case
- [ ] Add logout
- [ ] Add token blacklist
