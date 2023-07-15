"""Module responsable by database connections and management."""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

_print_sql = False

env = os.getenv('KASA_DESKTOP_ENV', 'DEV')
if env == 'PROD':
    db_path = os.environ['KASA_DESKTOP_SQLLITE']
else:
    db_path = '///./kasa_desktop_dev.db'
    
engine = create_engine(f"sqlite:{db_path}",echo=_print_sql) #, connect_args={"check_same_thread": False})

#data_session = Session(engine)
def get_data_session():
    return Session(engine)

#data_session = sessionmaker(autocommit=False, autoflush=False, bind=engine )

Base = declarative_base()
