# this file is in development!
# import csv module
import csv

# create list of ric agents, record and agent numerators
doc_agent_list = []
number_records = 0
number_agents = 0

# create rdf/xml file
rdf_file = open("C:/Users/tfruehwirth/Desktop/amp-data/data/ric_metadata/ric_metadata.rdf", "w")

# write xml declaration and rdf/xml root element
rdf_file.write("<?xml version=\"1.0\" encoding=\"utf-8\"?><!-- this file is in development! -->")
rdf_file.write("\n<rdf:RDF xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\"")
rdf_file.write("\n         xmlns:rico=\"https://www.ica.org/standards/RiC/ontology#\">")
rdf_file.write("\n")

# introduce ric-records section
rdf_file.write("\n<!-- ric records -->")
rdf_file.write("\n")

# open `ric.metadata.csv`
with open("C:/Users/tfruehwirth/Desktop/amp-data/data/ric_metadata/ric_metadata.csv", "r", newline='') as csv_file:
    # read file and map data in dictionary
    table = csv.DictReader(csv_file, delimiter=',', quotechar='"')
    for row in table:
        # store cell data in variables
        doc_id = row['document_id']
        doc_title = row['document_title']
        doc_date = row['document_date']
        doc_author = row['document_author']
        doc_language = row['document_language']
        doc_content_type = row['content_type']
        # insert variables (unless empty) into ric-record entry in rdf/xml file
        rdf_file.write("\n<rico:Record rdf:about=\"https://amp.acdh.oeaw.ac.at/amp-transcript__" + doc_id + ".html\">")
        if doc_id != "":
            rdf_file.write("\n   <rico:hasOrHadIdentifier>amp_" + doc_id + "</rico:hasOrHadIdentifier>")
        if doc_title != "":
            rdf_file.write("\n   <rico:hasOrHadName>" + doc_title + "</rico:hasOrHadName>")
        if doc_date != "":
            rdf_file.write("\n   <rico:isAssociatedWithDate>" + doc_date + "</rico:isAssociatedWithDate>")
        if doc_author != "":
            doc_author_abbr = doc_author.partition(',')
            rdf_file.write("\n   <rico:hasAuthor>https://amp.acdh.oeaw.ac.at/" + doc_author_abbr[0].lower() + ".html</rico:hasAuthor>")
        if doc_content_type != "":
            rdf_file.write("\n   <rico:hasContentOfType>" + doc_content_type + "</rico:hasContentOfType>")
        if doc_language != "":
            rdf_file.write("\n   <rico:hasOrHadLanguage>" + doc_language + "</rico:hasOrHadLanguage>")
        rdf_file.write("\n</rico:Record>")
        rdf_file.write("\n")
        number_records += 1
        ''''# TEST TEST TEST !!!!
        with open("C:/Users/tfruehwirth/Desktop/amp-data/data/editions/amp-transcript__" + doc_id + ".xml", "r+") as edition_file:
            contents = edition_file.read().replace("      </fileDesc>", "      </fileDesc>"
                                                                        "\n      <xenoData>"
                                                                        "\n         <rico:Record rdf:about="
                                                                        "\"https://amp.acdh.oeaw.ac.at/amp-transcript__" + doc_id + ".html\">\n      </xenoData>")
            edition_file.seek(0)
            edition_file.truncate()
            edition_file.write(contents)

        '''# TEST TEST TEST !!!

# introduce ric-agents section
rdf_file.write("\n<!-- ric agents -->")
rdf_file.write("\n")

# open `ric.metadata.csv`
with open("C:/Users/tfruehwirth/Desktop/amp-data/data/ric_metadata/ric_metadata.csv", "r", newline='') as csv_file:
    # read file and map data in dictionary
    table = csv.DictReader(csv_file, delimiter=',', quotechar='"')
    for row in table:
        # store cell data in variable
        doc_agent = row['document_author']
        # test if variable is part of agents list
        if doc_agent not in doc_agent_list:
            # insert variable into ric-agent entry in rdf/xml file
            doc_agent_abbr = doc_agent.partition(',')
            rdf_file.write("\n<rico:Agent rdf:about=\"https://amp.acdh.oeaw.ac.at/" + doc_agent_abbr[0].lower() + ".html\">")
            rdf_file.write("\n   <rico:hasOrHadAgentName>")
            rdf_file.write("\n      " + doc_agent)
            rdf_file.write("\n   </rico:hasOrHadAgentName>")
            rdf_file.write("\n</rico:Agent>")
            rdf_file.write("\n")
            # add unlisted agent to agents list
            doc_agent_list.append(doc_agent)
            number_agents += 1

# close rdf/xml root element
rdf_file.write("\n</rdf:RDF>")

# close rdf/xml file
rdf_file.close()

# print log
print("")
print(str(number_records) + " record entry/ies written; " + str(number_agents) + " agent entry/ies written.\n")
print("             __|__\n        ______(_)______\n            \"  \"  \"\n")
print("Thank you for flying with AMP.")
