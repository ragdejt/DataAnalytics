import logging
from constants.constants import LOG_FOLDER
def logger():
    """Configura o logger para o projeto."""
    logging.basicConfig(
        filename=f'{LOG_FOLDER / "DataAnalytics.log"}',
        encoding='utf-8',
        filemode='a',
        format='%(message)s',
        level=logging.DEBUG
    )
    return logging.getLogger()
