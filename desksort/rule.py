"""Structure for configuration rules"""


class Rule:
    """Defines Rules for Configurations"""

    def __init__(self, src, op, dest):
        self.src = src
        self.dest = dest
        self.opr = op

    def get_source(self) -> str:
        """Returns Source"""
        return str(self.src)

    def get_operation(self) -> str:
        """Returns Operator"""
        return str(self.opr)

    def get_destination(self) -> str:
        """Returns Destination"""
        return str(self.dest)

    def is_valid(self) -> bool:
        """Checks each rule for errors"""
        if self.src.isalnum():
            pass
        else:
            return False
        if self.opr == '=':
            pass
        else:
            return False
        return self.dest.isalnum()

    def match(self, file):
        """Checks if file matches the rule"""
        wildcard = self.src.find("*")
        print(self.src.find("*"))
        if wildcard == -1:  # Keyword
            return file.find(self.src) > -1
        if wildcard == 0:  # Suffix
            print("Is Suffix")
            if len(self.src) - 1 > len(file):
                print("Length Problem")
                return False

            print(len((file[-len(self.src) + 1::])))
            print(len(self.src[1::]))
            print(file[-len(self.src) + 1::] == self.src[1::])
            return file[-len(self.src) + 1::] == self.src[1::]

        print("Is a Prefix")
        if len(self.src) - 1 > len(file):
            print("Length Problem")
            return False

        for char in range(0, len(self.src) - 2, 1):
            if file[char] != self.src[char]:
                return False
        return True
