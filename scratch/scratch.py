
import os 
import logging
import tempfile
import shutil
import sys
from pathlib import Path

# this had to be added to fix lib import problems :(
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from lib import utility

print(utility.root_dir())




# root_dir = Path(__file__).parent.parent
# root_dir = os.path.dirname(os.getcwd())
# path_to_aritfacts = os.path.join(root_dir, "scrapers", "artifacts")
# if not os.path.exists(path_to_aritfacts):
#     os.makedirs(path_to_aritfacts)
# if not os.path.exists('aritfacts'):
#     os.makedirs('artifacts')
# temp_dir = tempfile.mkdtemp(dir=f"{path_to_aritfacts}/")
# try:
#     temp_dir_path = os.path.join(path_to_aritfacts, temp_dir)
#     with open(f"{temp_dir_path}/copy.txt", "w") as file:
#         file.write("holy shit this worked!!!!")
# except Exception as e:
#     print(e)
# finally:
#     shutil.rmtree(temp_dir)
