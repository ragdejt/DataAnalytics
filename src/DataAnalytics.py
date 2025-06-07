import streamlit
from functions.dashboard import main_dashboard
from config.page_config import page_config
DataAnalytics = page_config(initial_sidebar_state="collapsed")
if streamlit.session_state['login']:
    streamlit.header(":green[Desempenho de processos logisticos]", divider="green")
    main_dashboard()