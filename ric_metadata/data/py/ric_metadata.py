# in development!
# import csv module
import csv

# create rdf/xml file
rdf_file = open("C:/Users/tfruehwirth/Desktop/amp-data/data/ric_metadata/ric_metadata.rdf", "w")

# write xml declaration and root element
rdf_file.write("<?xml version=\"1.0\" encoding=\"utf-8\"?><!-- this file is in development! -->")
rdf_file.write("\n<rdf:RDF xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\"")
rdf_file.write("\n         xmlns:rico=\"https://www.ica.org/standards/RiC/ontology#\">")
rdf_file.write("\n")
# write ric agent entities
rdf_file.write("\n<!-- ric agents -->")
rdf_file.write("\n<rico:Agent rdf:about=\"https://amp.acdh.oeaw.ac.at/auden.html\">")
rdf_file.write("\n   <rico:hasOrHadAgentName>")
rdf_file.write("\n      Auden, W. H.")
rdf_file.write("\n   </rico:hasOrHadAgentName>")
rdf_file.write("\n</rico:Agent>")
rdf_file.write("\n")
rdf_file.write("\n<!-- ric records -->")

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
        doc_language = row['document_language']
        # write variables in new file (unless empty)
        rdf_file.write("\n<rico:Record rdf:about=\"https://amp.acdh.oeaw.ac.at/" + doc_id + ".html\">")
        if doc_id != "":
            rdf_file.write("\n   <rico:hasOrHadIdentifier>amp_" + doc_id + "</rico:hasOrHadIdentifier>")
        if doc_title != "":
            rdf_file.write("\n   <rico:hasOrHadName>" + doc_title + "</rico:hasOrHadName>")
        if doc_date != "":
            rdf_file.write("\n   <rico:isAssociatedWithDate>" + doc_date + "</rico:isAssociatedWithDate>")
        if doc_author != "":
            # add RiC agents
            doc_author_abbr = doc_author.partition(',')
            rdf_file.write("\n   <rico:hasAuthor>https://amp.acdh.oeaw.ac.at/" + doc_author_abbr[0].lower() + ".html</rico:hasAuthor>")
        if doc_language != "":
            rdf_file.write("\n   <rico:hasOrHadLanguage>" + doc_language + "</rico:hasOrHadLanguage>")
        rdf_file.write("\n</rico:Record>")
        rdf_file.write("\n")

# close xml root element
rdf_file.write("\n</rdf:RDF>")

# close rdf/xml file
rdf_file.close()
