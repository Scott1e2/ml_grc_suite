
# logging_util.py - Centralized Logging Utility for ML-GRC Suite

import logging

def setup_logging(log_file="ml_grc_suite.log", level=logging.INFO):
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger()
    logger.info("Logging setup complete.")
    return logger
