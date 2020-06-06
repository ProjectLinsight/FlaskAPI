import os

basedir = os.path.abspath(os.path.dirname(__file__))
#Database
SQLALCHEMY_DATABASE_URI='mysql://root:linsight37@localhost/linsight' 
SQLALCHEMY_TRACK_MODIFICATIONS = False