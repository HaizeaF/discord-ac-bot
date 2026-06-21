import logging

def setup_logger() -> logging.Logger:
    """Configure the logger to write to the console."""
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger("discord")
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger