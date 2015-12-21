import os
import json
import shutil

def infer_modname(title):
    return title.lower().replace(" ", "-").replace("'", "")

def spaceorblank(string):
    return not string or len(string) == 0 or string.isspace()

mod_info = {}
# Get Mod Title
while spaceorblank(mod_info.get("title")):
    mod_info["title"] = raw_input("Mod Title(required)> ")
# Get Mod Name
mod_info["name"] = raw_input("Mod Name(optional)> ")
if spaceorblank(mod_info.get("name")):
    mod_info["name"] = infer_modname(mod_info["title"])
    print "Inferred mod name as {} from mod title".format(mod_info["name"])
# Get description
mod_info["description"] = raw_input("Mod Description(optional)> ")
# Get Author
mod_info["author"] = raw_input("Mod Author(optional)> ")
# Contact
mod_info["contact"] = raw_input("Mod Contact(optional)> ")
# Homepage
mod_info["homepage"] = raw_input("Mod Homepage(optional)> ")

# os.makedirs()
# Create important directories
mod_folder = "{}_mod".format(mod_info["name"])
current_dir = os.path.dirname(os.path.abspath(__file__))
managed_mod_dir = os.path.join(current_dir, mod_folder)
required_dirs = ["graphics", "prototypes", "sound", "migrations", "locale"]

base_mod_dir = os.path.join(managed_mod_dir, mod_info["name"])

gen_dirs = []
gen_dirs.extend(os.path.join(base_mod_dir, folder) for folder in required_dirs)

for each in gen_dirs:
    if not os.path.exists(each):
        os.makedirs(each)
        print "CREATED {}".format(each)

gen_files = []
gen_files.extend([os.path.join(base_mod_dir, "control.lua"), os.path.join(base_mod_dir, "data.lua")])
for each in gen_files:
    open(each, "w").close()
    print "CREATED {}".format(each)


# Create info.json
json_info_path = os.path.join(managed_mod_dir, 'info.json')
with open(json_info_path, 'w') as info_file:
    info = {}
    info["version"] = "0.0.0"
    info.update(mod_info)
    info_string = json.dumps(info, indent=4, sort_keys=True)
    info_file.write(info_string)
    print "CREATED {}".format(json_info_path)

build_script_from = os.path.join(current_dir, 'build.py')
build_script_to = os.path.join(managed_mod_dir, 'build.py')
try:
    shutil.copy(build_script_from, build_script_to)
except:
    pass

