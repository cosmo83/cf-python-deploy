from cfenv import AppEnv
import os
env = AppEnv()
<<<<<<< HEAD
kavskdb = env.get_service(label='aws-rds-postgresql')
print(kavskdb.credentials)
=======
kavskdb = env.get_service(label='aws-rds-postgresql').credentials

>>>>>>> 6a749c08851de6adc9a55dd23903cd6380f245a7


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
<<<<<<< HEAD
SQLALCHEMY_DATABASE_URI = kavskdb.credentials['uri']
=======
SQLALCHEMY_DATABASE_URI = kavskdb.uri
print("DB Information")
print(SQLALCHEMY_DATABASE_URI)
>>>>>>> 6a749c08851de6adc9a55dd23903cd6380f245a7
