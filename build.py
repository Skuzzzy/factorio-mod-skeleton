import os
import json
import shutil
from distutils.dir_util import copy_tree

try:
    shutil.rmtree("release") # Clean
except:
    pass
with open("info.json") as dat:
    info = json.load(dat)

    full_name = "{}_{}".format(info["name"], info["version"])
    base_dir = os.path.dirname(os.path.abspath(__file__))
    res_dir = os.path.join(base_dir, info["name"])
    release = os.path.join(base_dir, "release")
    release_dir = os.path.join(release, full_name)
    os.makedirs(release_dir) # Prep
    copy_tree(res_dir, release_dir)
    # get info json in there as well
    # Create info.json
    json_info_path = os.path.join(release_dir, 'info.json')
    with open(json_info_path, 'w') as info_file:
        info_string = json.dumps(info, indent=4, sort_keys=True)
        info_file.write(info_string)

    # Generate zip release
    print os.path.join(release, full_name)
    print "zip"
    print release
    print release_dir
    shutil.make_archive(os.path.join(release, full_name), "zip", release, release_dir)
