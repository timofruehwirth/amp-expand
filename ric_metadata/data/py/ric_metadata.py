# import csv module
import csv

# create `ric_metadata.xml`
xml_file = open("C:/Users/tfruehwirth/Desktop/amp-data/data/ric_metadata/ric_metadata.xml", "w")

# print xml header
xml_file.write("<?xml version=\"1.0\" encoding=\"utf-8\"?><!-- in development -->")
xml_file.write("\n<rdf:RDF xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\"")
xml_file.write("\n         xmlns:rico=\"https://www.ica.org/standards/RiC/ontology#\">")
xml_file.write("\n")

# open `ric.metadata.csv`
with open("C:/Users/tfruehwirth/Desktop/amp-data/data/ric_metadata/ric_metadata.csv", "r", newline='') as csv_file:
    # read file and map data in dictionary
    table = csv.DictReader(csv_file, delimiter=',', quotechar='"')
    # store cell data in variables
    for row in table:
        doc_id = row['document_id']
        doc_title = row['document_title']
        doc_date = row['document_date']
        doc_author = row['document_author']
        # write variables in new file (unless empty)
        xml_file.write("\n<rico:Record>")
        if doc_id != "":
            xml_file.write("\n   <" + doc_id + ">")
        if doc_title != "":
            xml_file.write("\n   <" + doc_title + ">")
        if doc_date != "":
            xml_file.write("\n   <rico:" + doc_date + ">")
        if doc_author != "":
            xml_file.write("\n   <rico:hasAuthor " + doc_author + ">")
        xml_file.write("\n</rico:Record>")
        xml_file.write("\n")

# close `ric_metadata.xml`
xml_file.close()
