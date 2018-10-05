from subprocess import run, DEVNULL
from subprocess import CalledProcessError

import sys

class Utils:
    def checkCommand(self, command, **kwargs):
        if "commandName" in kwargs:
            commandName = kwargs["commandName"]

        else:
            commandName = command

        try:
            run(command, stdout=DEVNULL)

            print("{} installed".format(commandName))

        except FileNotFoundError:
            print("Error: probably {} isn't installed.".format(commandName))
            sys.exit()

    def runCommand(self, *args, inputfile="", outputfile=""):
        print(outputfile)
        if inputfile is not "":
            if outputfile is not "": 
                try:
                    with open(inputfile, "r") as inputfile, open(outputfile, "w") as outputfile:
                        return run(args, stdin=inputfile, stdout=outputfile)
                except FileNotFoundError as error:
                    # improve errors with an errors.py
                    print(inputfile)
                    print(outputfile)
                    print("Error: {}".format(error))

