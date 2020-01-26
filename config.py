from cfenv import AppEnv
import os
env = AppEnv()
kavskdb = env.get_service(label='aws-rds-postgresql')

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = kavskdb.credentials['uri']
