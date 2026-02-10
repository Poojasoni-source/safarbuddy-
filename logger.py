import logging
import os
LOG_DIR='logs'
LOG_FILE=os.path.join(LOG_DIR,"app.log")
os.makedirs(LOG_DIR,exist_ok=True)
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"

)
def get_logger(name):
    return logging.getLogger(name)