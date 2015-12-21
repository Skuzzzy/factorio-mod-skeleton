import os
import json
import shutil
from distutils.dir_util import copy_tree

try:
    shutil.rmtree("release") # Clean
except:
    pass
with open('info.json') as dat:
    info = json.load(dat)

    full_name = "{}_{}".format(info["name"], info["version"])
    base_dir = os.path.dirname(os.path.abspath(__file__))
    res_dir = os.path.join(base_dir, info["name"])
    release_dir = os.path.join(base_dir, "release", full_name)
    os.makedirs(release_dir) # Prep
    copy_tree(res_dir, release_dir)
