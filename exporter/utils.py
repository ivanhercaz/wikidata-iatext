# -*- coding: utf-8 -*-

from subprocess import run, DEVNULL

import re
import time

from exporter import errors


class Utils:
    """ Necessary methods to export

    Attributes
    ----------
    errors : class
        Format the errors happened.

    GREEN : str
        Store the code to print the text in green.
    ENDC : str
        Store the code to end the colored string.
    """

    errors = errors.Errors()

    GREEN = "\x1b[1;37;42m"
    ENDC = "\x1b[0m"

    def timeElapsed(self, start):
        """ Return the time elapsed

        Parameters
        ----------
        start : float
            Moment in which was started a process.

        Returns
        -------
        str
            Elapsed time formatted.
        """

        return time.strftime("%M:%S", time.gmtime(time.perf_counter() - start))

    def timeStart(self):
        """ Start to count the time

        Returns
        ------
        float
            Start the time counter.
        """

        return time.perf_counter()

    def countItems(self, identifiers):
        """ Return the total number of items in the identifiers file

        Parameters
        ----------
        identifiers : str
            SPARQL query file (.rq)

        Returns
        -------
        float
            Number of Q in the identifiers file.
        """

        identifiers = identifiers.replace(".rq", "")

        try:
            with open(identifiers, "r") as identifiersFile:
                identifiersContent = identifiersFile.read()

        except FileNotFoundError as error:
            return self.errors.fileNotFound(error)

        return len(re.findall("Q", identifiersContent))

    def prepareQuery(self, query):
        """ Create a new query file (queryDuplicated) with the same content
        that the query to save it and make safely the replacement of
        unnecessary data in the query

        Parameters
        ----------
        query : str
            SPARQL query file (.rq)

        Returns
        -------
        str
            Name of the duplicated query file: "*-duplicated.rq"
        """
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
        """ Remove the duplicated query and the identifiers file after the
        export because it is unnecessary.

        Parameters
        ----------
        query : str
            SPARQL query file (.rq)

        Returns
        -------
        tuple of CompletedProcess
           Run the self.runCommand method to remove both files, duplicated
           query and the identifiers file.
        """

        print("> Duplicated query ({}) removed.".format(query))

        identifiers = re.sub("-duplicated\.rq", "", query)
        print("> Identifiers file ({}) removed.".format(identifiers))

        return self.runCommand("rm", query), self.runCommand("rm", identifiers)

    def checkCommand(self, command, **kwargs):
        """ Check if the command is installed in the system, if not the script
        is stopped.

        Parameters
        ----------
        command : str
            command without arguments

        **kwargs
            The keyword arguments are used mainly to handle if it is specified
            a commandName parameter, which will be showed in the command-line
            interface, instead of the command.

        Returns
        -------
        CompletedProcess
            An specific print if the command is or not is installed.

        """

        if "commandName" in kwargs:
            commandName = kwargs["commandName"]

        else:
            commandName = command

        try:
            # run(command, stdout=DEVNULL)

            print("> {} {} {} installed".format(
                self.GREEN,
                commandName,
                self.ENDC
            ))

            return run(command, stdout=DEVNULL)

        except FileNotFoundError:
            return self.errors.commandNotFound(commandName)

    def runCommand(self, *args, inputfile="", outputfile=""):
        """ Run an specific command. Developed to handle special situations
        like the commands to export and query, which may need an input or an
        output file, or both.

        Parameters
        ----------
        *args
            The positional arguments are used to get the command and its
            parameters (e.g. ``wd data format --ttl``).
        inputfile : str
            File to use as the ``stding`` parameter of run() (the default
            value is empty).
        outputfile : str
            File to use as the ``stdout`` parameter of run() (the default
            value is empty).

        Returns
        -------
        CompletedProcess
            Run the command.
        """

        if outputfile is not "":
            if inputfile is not "":
                if outputfile.endswith("researchers") is False:
                    countItems = self.countItems(inputfile)
                    print("> Items (Qxxx) in the identifiers file ({}): {}"
                          " items".format(inputfile, countItems))

                if outputfile.endswith(".ttl") is True:
                    print("> Exporting the data retrieved from the SPARQL"
                          " query to RDF/Turtle.")

                try:
                    with open(inputfile, "r") as inputfile,\
                         open(outputfile, "w") as outputfile:
                        return run(args, stdin=inputfile, stdout=outputfile)

                except FileNotFoundError as error:
                    return self.errors.fileNotFound(error)
            try:
                with open(outputfile, "w") as outputfile:
                    return run(args, stdout=outputfile)

            except FileNotFoundError as error:
                return self.errors.fileNotFound(error)

        else:
            return run(args)
