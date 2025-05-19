# Import necessary modules.
import streamlit
from functions.create_tables import create_tables
from functions.create_directories import create_directories
from config.page_config import page_config


DataAnalytics = page_config(initial_sidebar_state="collapsed")

if streamlit.session_state['login']:
    pass
else:
    # Create necessary directories.
    create_directories()
    # Create all tables in the database.
    create_tables()