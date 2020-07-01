from desksort.rule import Rule
from desksort.config import Config
from desksort.sort import Sort


def king():
    con = Sort("config.cfg")
    con.import_rules()
    con.print_rules()
    con.move_files()
    con.do_config()
    print(con.is_valid())
    con.print_rules()

king()