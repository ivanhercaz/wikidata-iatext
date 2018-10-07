# Script to export all the worked items from Wikidata to RDF/Turtle (.ttl)

from exporter import utils

class Exporter:
    def __init__(self):
            utils.checkCommand("npm")
            utils.checkCommand("wd", commandName="wikidata-cli")

    def run(self):
        start = utils.timeStart()
        # Command example of wikidata-cli: wd data --format ttl Q123 Q3548931 Q515168
        # utils.runCommand("wd", "data", "--format", "ttl", "Q123")
        query = utils.prepareQuery("researchers/researchers.rq")
        utils.runCommand("wd", "sparql", query, outputfile="researchers/researchers")
        utils.runCommand("wd", "data", "--format", "ttl", inputfile="researchers/researchers", outputfile="researchers/researchers.ttl")
        utils.removeQuery(query)
        print(utils.timeElapsed(start))

        query = utils.prepareQuery("publications/publications.rq")
        utils.runCommand("wd", "sparql", query, outputfile="publications/publications")
        utils.runCommand("wd", "data", "--format", "ttl", inputfile="publications/publications", outputfile="publications/publications.ttl")
        utils.removeQuery(query)
        print(utils.timeElapsed(start))

utils = utils.Utils()

# To test
# exporter = Exporter()
# exporter.run()
