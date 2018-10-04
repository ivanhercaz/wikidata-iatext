from subprocess import run
from subprocess import CalledProcessError

class Utils:
    def runCommand(self, *args):
        print(args) # to test if the args are fine
        return run(args)
