# Script to export all the worked items from Wikidata to RDF/Turtle (.ttl)

from exporter import utils

class Exporter:
    utils = utils.Utils()

    def __init__(self):
        print("- Script to export the Wikidata items worked in the project wikidata-iatext to"
              " RDF/Turtle (.ttl).\n")
        print("Checking that everything is installed")
        self.utils.checkCommand(["node", "--version"], commandName="node")
        self.utils.checkCommand("npm")
        self.utils.checkCommand("wd", commandName="wikidata-cli")

    def run(self):
        start = self.utils.timeStart()
        # Command example of wikidata-cli: wd data --format ttl Q123 Q3548931 Q515168
        # self.utils.runCommand("wd", "data", "--format", "ttl", "Q123")
        print("\nExporting researchers...")
        query = self.utils.prepareQuery("researchers/researchers.rq")
        print("> Retrieving items from the SPARQL query")
        self.utils.runCommand("wd", "sparql", query, outputfile="researchers/researchers")
        self.utils.runCommand("wd", "data", "--format", "ttl", inputfile="researchers/researchers",
                              outputfile="researchers/researchers.ttl")
        self.utils.removeQuery(query)
        print("> Elapsed time: {}".format(self.utils.timeElapsed(start)))

        startPublications = self.utils.timeStart()
        print("\nExporting publications...")
        query = self.utils.prepareQuery("publications/publications.rq")
        self.utils.runCommand("wd", "sparql", query, outputfile="publications/publications")
        self.utils.runCommand("wd", "data", "--format", "ttl", inputfile="publications/publications",
                         outputfile="publications/publications.ttl")
        self.utils.removeQuery(query)
        print("> Elapsed time: {}".format(self.utils.timeElapsed(startPublications)))

        print("\nExport finished in {} minutes. Your RDF/Turtle datasets are their respective folders"
              " (publications and researchers).".format(self.utils.timeElapsed(start)))
