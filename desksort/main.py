from desksort.rule import Rule
from desksort.config import Config
from desksort.sort import Sort


def __main__():
    con = Sort("config.cfg")
    con.importRules()
    con.printRules()
    con.moveFiles()
    con.doConfig()
    print(con.isValid())
