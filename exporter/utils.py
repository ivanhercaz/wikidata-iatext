from subprocess import run, DEVNULL
from subprocess import CalledProcessError

import re, shutil, sys, time

class Utils:
    def timeElapsed(self, start):
        elapsed = "Elapsed time from the beginning until the last process: {}".format(
            time.strftime("%M:%S", time.gmtime(time.perf_counter() - start))
        )

        return elapsed

    def timeStart(self):
        return time.perf_counter()

    def countItems(self, identifiers):
        identifiers = identifiers.replace(".rq", "")
        with open(identifiers, "r") as identifiersFile:
            identifiersContent = identifiersFile.read()

        return len(re.findall("Q", identifiersContent))

    def prepareQuery(self, query):
        queryDuplicated = re.sub(r"\.rq", "-duplicated.rq", query)

        # shutil.copyfile(query, queryDuplicated)

        with open(query, "r") as queryFile:
            queryContent = queryFile.read()

        regex = r"(\s\?[a-z]*[A-Z]\w*)*(\sWHERE\s{)$"
        subst = r"\2"
        replacement = re.sub(regex, subst, queryContent, 0, re.MULTILINE)

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
        self.runCommand("rm", query)

        identifiers = re.sub("-duplicated\.rq", "", query)
        self.runCommand("rm", identifiers)

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
                if inputfile.endswith(".rq") is False: 
                    countItems = self.countItems(inputfile)
                    print("Items (Qxxx) in the identifiers file".format(countItems))

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

        else:
            return run(args)
