from desksort.sort import Sort


def start():
    con = Sort("config.cfg")
    con.import_rules()
    con.print_rules()
    con.move_files()
    con.do_config()