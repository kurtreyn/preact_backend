import psycopg2
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os

load_dotenv()

hostname = 'localhost'
database = 'demo_db'
username = 'postgres'
password = 'admin'
port_id = 5432


