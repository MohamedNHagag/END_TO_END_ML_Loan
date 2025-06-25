import logging
import os
from datetime import datetime

#get time now and convert to string style
log_file=f"a{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

#create file logs to store and check exist or not
log_path=os.path.join(os.getcwd(),"logs")
os.makedirs(log_path,exist_ok=True)

#collect log_paths in log_file
log_file_path=os.path.join(log_path, log_file)

#message style 
logging.basicConfig(
    filename=log_file_path,
            #data&time     number line             level message 
    format="[%(asctime)s] [%(lineno)d] [%(name)s] [%(levelname)s] - %(message)s",
    level=logging.INFO
)