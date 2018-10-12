# -*- coding: utf-8 -*-
""" Export all the worked items during the project Wikidata-IATEXT from
    Wikidata to RDF/Turtle (.ttl)

The script uses the ``wikidata-cli`` package, developed by Maxime Lathuilière
(maxlath), to query Wikidata with SPARQL and then export the results to
RDF/Turtle.

The main objective of the dataset in RDF/Turtle is, beside the CSV, to have an
easy way to query what was did it during the project, and nor the current state
of the data. This is useful to analyze just the results of the projects and nor
how the items created changed nor how has been increased the number of items
that fit to the SPARQL queries written for the Wikidata Query Service.

How-to use it:
    In the case you use this data or script, in a modifier form or not, you can
    cite this work using the DOI provided by Zenodo: 10.5281/zenodo.1442909

Credits:
    The projects was proposed to the Research Institute of Text Analysis and
    Applications (IATEXT), part of the Universidad de Las Palmas de Gran
    Canaria (ULPGC), by Iván Hernández Cazorla, who was responsible of its
    development and execution.

License:
    - All data is in the public domain, according to the CC0 mark of Wikidata.
    - This script, and all the ``wikidata-iatext`` repository, is under the
    GNU General Public License v.3.0:
    https://github.com/ivanhercaz/wikidata-iatext/blob/master/LICENSE
    - ``wikidata-cli``, by Maxime Lathuilière (maxlath), is under the
    MIT License:
    https://github.com/maxlath/wikidata-cli/blob/master/LICENSE

"""

from exporter import utils


class Exporter:
    """ Prepare and run the export
    Attributes
    ----------
    utils : str
        Utils class.
    """

    utils = utils.Utils()

    def __init__(self):
        """ Check if the necessary tools are installed in the system

        In the case in which the tools seem to be unavailable the script is
        stopped. The user have to install the tools (see export.md)

        """

        print("- Script to export the Wikidata items worked in the project"
              " Wikidata-IATEXT to RDF/Turtle (.ttl).\n")
        print("Checking that everything is installed")
        self.utils.checkCommand(["node", "--version"], commandName="node")
        self.utils.checkCommand("npm")
        self.utils.checkCommand("wd", commandName="wikidata-cli")

    def run(self):
        start = self.utils.timeStart()

        print("\nExporting researchers...")
        query = self.utils.prepareQuery("researchers/researchers.rq")
        print("> Retrieving items from the SPARQL query")
        self.utils.runCommand("wd", "sparql", query,
                              outputfile="researchers/researchers")
        self.utils.runCommand("wd", "data", "--format", "ttl",
                              inputfile="researchers/researchers",
                              outputfile="researchers/researchers.ttl")
        self.utils.removeQuery(query)
        print("> Elapsed time: {}".format(self.utils.timeElapsed(start)))

        startPublications = self.utils.timeStart()
        print("\nExporting publications...")
        query = self.utils.prepareQuery("publications/publications.rq")
        self.utils.runCommand("wd", "sparql", query,
                              outputfile="publications/publications")
        self.utils.runCommand("wd", "data", "--format", "ttl",
                              inputfile="publications/publications",
                              outputfile="publications/publications.ttl")
        self.utils.removeQuery(query)
        print("> Elapsed time: {}".format(
            self.utils.timeElapsed(startPublications)
        ))

        print("\nExport finished in {} minutes. Your RDF/Turtle datasets are"
              " their respective folders (publications and"
              " researchers).".format(self.utils.timeElapsed(start)))
