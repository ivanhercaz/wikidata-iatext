# -*- coding: utf-8 -*-
import re
import sys


class Errors():
    """ Format errors received

    Attributes
    ----------
    RED : str
        Store the code to print text in red.
    ENDC : str
        Store the code to end the colored string.
    """
    RED = "\x1b[1;37;41m"
    ENDC = "\x1b[0m"

    def fileNotFound(self, error):
        """ Format error when a file doesn't found

        Parameters
        ----------
        error : str
            This arg is used to get the error.

        Returns
        -------
        sys.exit
            Stop the script.

        """

        error = re.sub(r"\[\w*\ \d*]\s", "", str(error))

        print("{}Error:{} {}\nScript stopped. Check and solve the error"
              " before run it again.".format(
                self.RED,
                self.ENDC,
                error
              ))
        return sys.exit()

    def commandNotFound(self, commandName):
        """ Format the error when the command isn't available

        Parameters
        ----------
        commandName : str
            The name of the command when it is different from the keyword to
            execute it.
        Returns
        -------
        sys.exit
            Stop the script.
        """

        error = "probably {} {} {} isn't installed".format(
            self.RED,
            commandName,
            self.ENDC
        )

        print("{}Error:{} {}.\nScript stopped. Check and solve the error"
              " before run it again.".format(
                self.RED,
                self.ENDC,
                error
              ))
        return sys.exit()
