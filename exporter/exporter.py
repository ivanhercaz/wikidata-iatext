# Script to export all the worked items from Wikidata to RDF/Turtle (.ttl)

from exporter import utils

class Exporter:
    def run(self):
        # Command example of wikidata-cli: wd data --format ttl Q123 Q3548931 Q515168
       try:
           utils.runCommand("wd", "data", "--format", "ttl", "Q123")
       except:
            print("adios")


utils = utils.Utils()

# To test
exporter = Exporter()
exporter.run()
