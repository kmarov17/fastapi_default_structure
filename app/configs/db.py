from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 
import urllib
from app.models.tables import Base


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

try : 
    
    #Base = declarative_base()
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Base.metadata.create_all(bind=engine) 
     
    print('************** running ********************') 
    SessionLocal= sessionmaker(bind=engine,autocommit=False, autoflush=False) 
     
    def  get_db(): 
        try : 
 
            print('success session') 
 
            session=SessionLocal()  
            yield session 
            session.commit() 
         
        finally : 
            session.close() 
            print('session closed') 
 
 
except Exception as ex : 
    print("********************", ex)

