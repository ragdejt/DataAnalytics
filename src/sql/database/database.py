from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from constants.paths import SQL_FOLDER
# Define the database URL
DATABASE_URL = f"sqlite:///{SQL_FOLDER / 'DataAnalytics.db'}"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a configured "Session" class  
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()
