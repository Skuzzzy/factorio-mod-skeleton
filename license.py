import string
import os
from os import listdir
from os.path import isfile, join

licence_dir = os.path.join("res", "licence")

def available_licenses():
    templ_files = [templ for templ in listdir(licence_dir) if isfile(join(licence_dir, templ))]
    return templ_files

def template_template(info, templ_path): # Keeping this method name because it makes sense, and is funny at the same time
    with open(templ_path) as doc:
        text = doc.read()
        inserted = string.Template(text).substitute(info)
        return inserted

def prompt():
    options = available_licenses()
    for n, each in enumerate(options):
        print "[{}] {}".format(n,each)
    while True:
        try:
            selection = int(raw_input("Select the licence you would like: "))
            if selection >= 0 and selection < len(options):
                return options[selection]
            else:
                print "Please input a integer coresponding to one of the licenses"
        except:
            print "Please input a valid integer"

# print available_licenses()
# selection = prompt()
# template_path = os.path.join(licence_dir, selection)
# inf = {"name":"Daniel Baird", "year": 2015}
# print template_template(inf, template_path)
