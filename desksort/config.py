"Collection of Rules"
from desksort.rule import Rule
class Config:
    "A configuration of rules"
    def __init__(self, file):
        "Creates a Config"
        self.name = file
        self.rules = []
        self.ignore_files = ["main.py", "config.cfg", "README.md", "LICENSE", ".gitignore"]


    def is_valid(self):
        "is_valid check for each rule"
        for rule in self.rules:
            if rule.isValid() is False:
                return False
        return True


    def import_rules(self):
        "loads rules from given config file in name"
        file = open(self.name, "r")
        for line in file:
            if line[0] != '#':
                pass
            else:
                rule = line.split()
                self.rules.append(Rule(rule[0], rule[1], rule[2]))
        file.close()

    def print_rules(self):
        "prints each rule in console"
        for rule in self.rules:
            print(rule.src + " " + rule.opr +" " + rule.dest)

    def check_config(self, file):
        "checks if given file matches a rule"
        for rule in self.rules:
            print(rule.getSource())

            if rule.match(file) is True:
                print("Matches :" + rule.getOperation() + rule.getDestination())
                return [rule.getOperation(), rule.getDestination()]
        return False

    def add_rule(self, rule: Rule):
        "adds a rule to the bottom of config file"
        file = open(self.name, "a")
        file.write(rule.get_source()+" "+rule.get_operation()+" "+rule.get_destination()+"\n")
        file.close()

    def get_rules(self):
        "returns config rules"
        return self.rules
