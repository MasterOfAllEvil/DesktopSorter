"Operations of DeskSorter"
import os
from os import path
from desksort.config import Config


def create_config(file):
    """

    @rtype: None
    """
    con = open(file, "w+")
    con.write("# Config Rules\n")
    con.write("# To move name contains a prefix, write prefix* = Directory Name\n")
    con.write("# Homework* = Homework\n")
    con.write("# HW* = Homework")
    con.close()


class Sort(Config):
    "Sorts using Config"

    def __init__(self, file):
        "Initializes with given config file"
        print(path.isfile(file))
        if not path.isfile(file):
            create_config(file)

        super().__init__(file)

    def move_files(self):
        "Move Files"
        # If Sort Folder does not exist, make folder
        if not path.exists('Sort'):
            os.mkdir('Sort')

        current_files = os.listdir()
        is_ignored = False
        for file in current_files:  # For all of list, move all files except for Class.cfg
            if not file == "config.cfg":
                is_ignored = False
                for ignored_file in self.ignore_files:
                    if file == ignored_file:
                        is_ignored = True
                        break
                if not is_ignored:
                    if path.isfile(file):
                        if os.path.exists(".\\Sort\\" + file):
                            file_name = file.split('.')
                            print(file_name)
                            file_name[0] = file_name[0] + "(1)"
                            os.rename(os.getcwd() + "\\" + file, os.getcwd() + "\\Sort\\" + str(file_name))
                        else:
                            os.rename(os.getcwd() + "\\" + file, os.getcwd() + "\\Sort\\" + file)
                    else:
                        print("Ignored File Detected")

    def do_config(self):
        "check for config"
        if not path.isfile(self.name):
            create_config(self.name)

        files = os.listdir("Sort")
        print(files)
        print(os.getcwd())

        for file in files:
            print(file)
            check = super().check_config(file)
            print(check)
            if not check:
                print("Found One: " + file)
                if check[0] != "=":
                    print(str(check[0] + " is not an implemented operation."))
                else:
                    try:
                        print(check[0])
                        print(check[1])
                        print(file)
                        os.rename("./Sort/" + file, "./" + check[1] + "/" + file)
                    except:
                        print("An Exception occured")
                        exit()
