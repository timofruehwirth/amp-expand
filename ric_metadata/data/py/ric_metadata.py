# this file is in development!

# import csv module
import csv

# import datetime.datetime module
from datetime import datetime

# this script uses the lxml library for creating xml
# alternatively the rdflib library for creating rdf might be used

# import lxml.etree library
from lxml import etree

# define rdf and rico namespace prefixes
nsmap = {"rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rico": "https://www.ica.org/standards/RiC/ontology#"}

# create rdf/xml root element
root = etree.Element(etree.QName(nsmap["rdf"], "RDF"), nsmap=nsmap)

# create list of ric agents, create ric record and agent numerators
doc_agent_list = []
number_records = 0
number_agents = 0

# open `ric_metadata.csv`
with open("C:/Users/tfruehwirth/Desktop/amp-data/data/ric_metadata/ric_metadata.csv", "r", newline='') as csv_file:
    # read csv file and map data in dictionary
    table = csv.DictReader(csv_file, delimiter=',', quotechar='"')
    for row in table:
        # store cell data in variables
        doc_id = row['document_id']
        doc_title = row['document_title']
        doc_date = row['document_date']
        doc_author_01 = row['document_author_01']
        doc_author_02 = row['document_author_02']
        doc_language = row['document_language']
        doc_content_type = row['content_type']
        # create rdf/xml record sub-elements
        record = etree.SubElement(root, etree.QName(nsmap['rico'], 'Record'))
        record.attrib[etree.QName(nsmap["rdf"], "about")] = "https://amp.acdh.oeaw.ac.at/amp-transcript__" + doc_id
        # insert variables unless empty
        if doc_id != "":
            etree.SubElement(record, etree.QName(nsmap["rico"], "hasOrHadIdentifier")).text = "amp_" + doc_id
        if doc_title != "":
            etree.SubElement(record, etree.QName(nsmap["rico"], "hasOrHadName")).text = doc_title
        if doc_date != "":
            etree.SubElement(record, etree.QName(nsmap["rico"], "isAssociatedWithDate")).text = doc_date
        if doc_author_01 != "":
            # partitioning author name string for surname
            doc_author_01_abbr = doc_author_01.partition(',')
            etree.SubElement(record, etree.QName(nsmap["rico"], "hasAuthor")).text = "https://amp.acdh.oeaw.ac.at/" + doc_author_01_abbr[0].lower() + ".html"
        if doc_author_02 != "":
            doc_author_02_abbr = doc_author_02.partition(',')
            etree.SubElement(record, etree.QName(nsmap["rico"], "hasAuthor")).text = "https://amp.acdh.oeaw.ac.at/" + doc_author_02_abbr[0].lower() + ".html"
        if doc_content_type != "":
            etree.SubElement(record, etree.QName(nsmap["rico"], "hasContentOfType")).text = doc_content_type
        if doc_language != "":
            etree.SubElement(record, etree.QName(nsmap["rico"], "hasOrHadLanguage")).text = doc_language
        # add to record numerator
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
    
            # TEST TEST TEST !!!'''

with open("C:/Users/tfruehwirth/Desktop/amp-data/data/ric_metadata/ric_metadata.csv", "r", newline='') as csv_file:
    table = csv.DictReader(csv_file, delimiter=',', quotechar='"')
    for row in table:
        doc_agent_01 = row['document_author_01']
        doc_agent_02 = row['document_author_02']
        # test if variable is part of agent list or empty
        if doc_agent_01 not in doc_agent_list and doc_agent_01 != "":
            # create rdf/xml agent sub-elements
            doc_agent_01_abbr = doc_agent_01.partition(',')
            agent = etree.SubElement(root, etree.QName(nsmap["rico"], "Agent"))
            agent.attrib[etree.QName(nsmap["rdf"], "about")] = "https://amp.acdh.oeaw.ac.at/" + doc_agent_01_abbr[0].lower() + ".html"
            etree.SubElement(agent, etree.QName(nsmap["rico"], "hasOrHadAgentName")).text = doc_agent_01
            # add unlisted agent to agent list
            doc_agent_list.append(doc_agent_01)
            # add to agent numerator
            number_agents += 1
        if doc_agent_02 not in doc_agent_list and doc_agent_02 != "":
            doc_agent_02_abbr = doc_agent_02.partition(',')
            agent = etree.SubElement(root, etree.QName(nsmap["rico"], "Agent"))
            agent.attrib[etree.QName(nsmap["rdf"], "about")] = "https://amp.acdh.oeaw.ac.at/" + doc_agent_02_abbr[0].lower() + ".html"
            etree.SubElement(agent, etree.QName(nsmap["rico"], "hasOrHadAgentName")).text = doc_agent_02
            doc_agent_list.append(doc_agent_02)
            number_agents += 1

# write rdf/xml tree in rdf file
with open("C:/Users/tfruehwirth/Desktop/amp-data/data/ric_metadata/ric_metadata.rdf", "w") as rdf_file:
    rdf_file.write(str(etree.tostring(root, encoding="utf-8", xml_declaration=True, pretty_print=True).decode("utf-8")))

# print log
print("")
print(str(number_records) + " record entry/ies and " + str(number_agents) + " agent entry/ies written on " + str(datetime.now()) + ".")
print("\n             __|__\n        ______(_)______\n            \"  \"  \"\n")
print("Thank you for flying with AMP.")
