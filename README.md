# Getting Started Python Django

1. To run django server firstly create virtualenv

### `$ virtualenv venv`

2. Start vitualenv

### `$ source venv/Scripts/activate`

3. install all requirements

### `$ pip install -r requirement.txt`

4. Run django server

### `$ python manage.py runserver`

# Getting Started React js

1. Open react_django folder

2. Install related dependencies / Modules

### `$ npm install`

3. Run node server

### `$ npm run dev`




# Getting Started Python Django in linux

To use this project in linux follow this steps

1. curl https://pyenv.run|bash
2. copy data and path from instructions
3. nano ~/.bashrc (and paste)
4. sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
5. pyenv install 3.8.0
6. pyenv virtualenv 3.8.0 venv
7. pyenv activate venv
8. now follow early first steps


# Use celery with dajngo

To use celery with django follow billow steps

1. Create and open virtualenv
2. pip install celery redis
3. Create a file (celery.py) in project folder (parelel with settings.py) and paste the celery.py from this repo
4. Paste the repo project/__init__.py  (for run celery when django starts)
5. Create a file (tasks.py) anywhere ( in project or in app ) and define your task for auto run
6. Run this where and when you want
