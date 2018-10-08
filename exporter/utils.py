from subprocess import run, DEVNULL
from subprocess import CalledProcessError

import re, sys, time

from exporter import errors

class Utils:
    errors = errors.Errors()

    GREEN = "\x1b[1;37;42m"
    ENDC = "\x1b[0m"

    def timeElapsed(self, start):
        elapsed = "Elapsed time from the beginning until the last process: {}".format(
            time.strftime("%M:%S", time.gmtime(time.perf_counter() - start))
        )
        return elapsed

    def timeStart(self):
        return time.perf_counter()

    def countItems(self, identifiers):
        identifiers = identifiers.replace(".rq", "")

        try:
            with open(identifiers, "r") as identifiersFile:
                identifiersContent = identifiersFile.read()

        except FileNotFoundError as error:
            errors = self.errors.fileNotFound(error)
            print(errors)

        return len(re.findall("Q", identifiersContent))

    def prepareQuery(self, query):
        queryDuplicated = re.sub(r"\.rq", "-duplicated.rq", query)

        with open(query, "r") as queryFile:
            queryContent = queryFile.read()

        regex = r"(\s\?[a-z]*[A-Z]\w*)*(\sWHERE\s{)$"
        subst = r"\2"
        replacement = re.sub(regex, subst, queryContent, 0, re.MULTILINE)

        with open(queryDuplicated, "w") as queryFile:
            queryFile.write(replacement)

        return queryDuplicated

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

            print("> {} {} {} installed".format(
                self.GREEN,
                commandName,
                self.ENDC
            ))

        except FileNotFoundError:
            self.errors.commandNotFound(commandName)
            sys.exit()

    def runCommand(self, *args, inputfile="", outputfile=""):
        if outputfile is not "":
            print("Output file: {}".format(outputfile))

            if inputfile is not "":
                print("Input file: {}".format(inputfile))

                if inputfile.endswith(".rq") is False: 
                    countItems = self.countItems(inputfile)
                    print("Items (Qxxx) in the identifiers file ({}): {} items".format(inputfile, countItems))

                try:
                    with open(inputfile, "r") as inputfile, open(outputfile, "w") as outputfile:
                        return run(args, stdin=inputfile, stdout=outputfile)

                except FileNotFoundError as error:
                    # improve errors with an errors.py
                    return "Error: {}".format(error)
            try:
                with open(outputfile, "w") as outputfile:
                    return run(args, stdout=outputfile)

            except FileNotFoundError as error:
                # improve errors with an errors.py
                print("Error: {}".format(error))

        else:
            return run(args)
