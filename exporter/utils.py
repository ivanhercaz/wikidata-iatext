from subprocess import run, DEVNULL
from subprocess import CalledProcessError

import re, shutil, sys

class Utils:
    def prepareQuery(self, query):
        queryDuplicated = re.sub(r"\.rq", "-duplicated.rq", query)

        # shutil.copyfile(query, queryDuplicated)

        with open(query, "r") as queryFile:
            queryContent = queryFile.read()

        replacement = re.sub(r" \?item[A-Z]\w*", "", str(queryContent))

        with open(queryDuplicated, "w") as queryFile:
            queryFile.write(replacement)

        query = queryDuplicated

        return query
        """
        with open(queryDuplicated, "r+") as queryFile:
            print("query abierta")
            queryRead = queryFile.read()
            replacement = re.sub(r" \?item[A-Z]\w*", "", str(queryRead))
            queryFile.write(replacement)
        """

    def removeQuery(self, query):
        print(query)

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
        print("outputfile: {}".format(outputfile))
        print("inputfile: {}".format(inputfile))

        if outputfile is not "":
            if inputfile is not "": 
                try:
                    with open(inputfile, "r") as inputfile, open(outputfile, "w") as outputfile:
                        print(args)
                        return run(args, stdin=inputfile, stdout=outputfile)

                except FileNotFoundError as error:
                    # improve errors with an errors.py
                    print("Error: {}".format(error))
            try:
                with open(outputfile, "w") as outputfile:
                    print(args)
                    return run(args, stdout=outputfile)

            except FileNotFoundError as error:
                # improve errors with an errors.py
                print("Error: {}".format(error))
