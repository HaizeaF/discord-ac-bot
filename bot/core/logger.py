import logging
import os

from bot.core.config import LOG_DIR, LOG_FILE

def setup_logger() -> logging.Logger:
    os.makedirs(LOG_DIR,exist_ok=True)

    handler = logging.FileHandler(filename=LOG_FILE, encoding='utf-8', mode='w')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger("discord")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    return logger