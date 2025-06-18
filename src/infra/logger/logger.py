import logging

def get_logger(name="API_dispositivo"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.FileHandler("logs_dispositivo.log") 
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger