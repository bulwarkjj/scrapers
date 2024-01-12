"""
define all the web elements/locators
"""
import logging
import os
import tempfile
import shutil
import sys

# added to solve lib module import issue
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from lib import utility

path_to_aritfacts = utility.root_dir()

# setting up logging and pushing it to the artifacts dir
if not os.path.exists(path_to_aritfacts):
    os.makedirs(path_to_aritfacts)
temp_dir = tempfile.mkdtemp(dir=f"{path_to_aritfacts}/")


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s', 
                    datefmt='%a, %d %b %Y %H:%M:%S', filename=f'{temp_dir}/locators.log', filemode='w')


# logger.debug("test test test ")
# login page web locators 

# locators after login