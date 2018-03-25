import os
from flask import Flask
from models import db

app = Flask(__name__)


@app.route('/')
def main():
    return "Hello World!"


def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


# the values of those depend on your setup
POSTGRES_URL = get_env_variable("POSTGRES_URL")  #127.0.0.1:5432
POSTGRES_USER = get_env_variable("POSTGRES_USER")  #test_user
POSTGRES_PW = get_env_variable("POSTGRES_PW")  #test12345
POSTGRES_DB = get_env_variable("POSTGRES_DB")  #test_db
CONFIG_NAME = get_env_variable("CONFIG_NAME")  #staging

app.config['DEBUG'] = True
# app.config[
#     'SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(pw)s@\%(host)s:%(port)s/%(db)s' % POSTGRES

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db.init_app(app)

if __name__ == '__main__':
    app.run()
