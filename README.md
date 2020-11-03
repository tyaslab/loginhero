# Login Hero

## Requirements
- Python 3.8
- PostgreSQL (or any database backend you like)
- Redis (if not exist it won't be a show stopper. trust me!)

### How to run (with Docker)
1. Create file ```.env``` (copy from ```.env-example```)
2. Create file ```app/local_config.py``` (You can copy from ```local_config.py-example```), **edit to fit your need!**
3. You can run this app with docker by ```$ docker-compose up --build``` and everything should be OK


## How to Install

1. Install virtualenv  ```$ python3.8 -m venv env```
2. Activate virtualenv ```$ source env/bin/activate```
3. Install required modules ```$ pip install -r requirements.txt```
4. Create a database
5. Create file ```app/local_config.py``` (You can copy from ```local_config.py-example```), **edit to fit your need!**
4. It includes script to create table (for the first time)  ```python main.py create-table```
5. Run it! ```python main.py``` or just ```./main.py``` (for *nix users)

## APIDOCS
You can access apidocs at ```/api/v1/apidocs```

## P.S.
Thanks :)


## Created by
Aditya Darmawan
