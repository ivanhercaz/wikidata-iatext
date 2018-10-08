import re, sys


class Errors():
    RED = "\x1b[1;37;41m"
    ENDC = "\x1b[0m"

    def fileNotFound(self, error):
        error = re.sub(r"\[\w*\ \d*]\s", "", str(error))

        print("{}Error:{} {}\nScript stopped. Check and solve the error before run it again.".format(
            self.RED,
            self.ENDC,
            error
        ))
        return sys.exit()

    def commandNotFound(self, commandName):
        error = "probably {} {} {} isn't installed".format(
            self.RED,
            commandName,
            self.ENDC
        )

        print("{}Error:{} {}.\nScript stopped. Check and solve the error before run it again.".format(
            self.RED,
            self.ENDC,
            error
        ))
        return sys.exit()
