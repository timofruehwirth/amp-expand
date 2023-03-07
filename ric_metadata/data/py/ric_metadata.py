# this file is in development!

# import csv module
import csv

# import datetime.datetime module
from datetime import datetime

# import os module
import os

# this script uses the lxml library for creating xml
# alternatively use the rdflib library for creating rdf

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

# create a `Document` class
class Document:
    def __init__(self, doc_id, doc_title, doc_date, doc_author_01, doc_author_02, doc_author_03, doc_author_04, doc_language, doc_content_type):
        # assigning values:
        self.doc_id = doc_id
        self.doc_title = doc_title
        self.doc_date = doc_date
        self.doc_author_01 = doc_author_01
        self.doc_author_02 = doc_author_02
        self.doc_author_03 = doc_author_03
        self.doc_author_04 = doc_author_04
        self.doc_language = doc_language
        self.doc_content_type = doc_content_type

# open `ric_metadata.csv`
with open("C:/Users/tfruehwirth/Desktop/amp-data/data/ric_metadata/ric_metadata.csv", "r", newline='') as csv_file:
    # read csv file and map data in dictionary
    table = csv.DictReader(csv_file, delimiter=',', quotechar='"')
    for row in table:
        # store cell data as features of a `document_object` object of the `Document` class
        document_object = Document(row['document_id'], row['document_title'], row['document_date'],
                                   row['document_author_01'], row['document_author_02'], row['document_author_03'],
                                   row['document_author_04'], row['document_language'], row['content_type'])
        # create rdf/xml record sub-elements
        record = etree.SubElement(root, etree.QName(nsmap['rico'], 'Record'))
        record.attrib[etree.QName(nsmap["rdf"], "about")] = "https://amp.acdh.oeaw.ac.at/amp-transcript__" + document_object.doc_id
        # insert variables unless empty
        if document_object.doc_id != "":
            etree.SubElement(record, etree.QName(nsmap["rico"], "hasOrHadIdentifier")).text = "amp_" + document_object.doc_id
        if document_object.doc_title != "":
            etree.SubElement(record, etree.QName(nsmap["rico"], "hasOrHadName")).text = document_object.doc_title
        if document_object.doc_date != "":
            etree.SubElement(record, etree.QName(nsmap["rico"], "isAssociatedWithDate")).text = document_object.doc_date
        if document_object.doc_author_01 != "":  # ATTENTION: PROBLEM WITH OTHER STRING FORMATS, SEE DOC0049; FIND ALTERNATIVE SOLUTION
            # partition author name string for surnames plus first-name initials
            doc_author_01_abbr = document_object.doc_author_01.partition(',')
            etree.SubElement(record, etree.QName(nsmap["rico"], "hasAuthor")).text = "https://amp.acdh.oeaw.ac.at/" + doc_author_01_abbr[0].lower() + "_" + doc_author_01_abbr[2][1].lower() + ".html"
        if document_object.doc_author_02 != "":
            doc_author_02_abbr = document_object.doc_author_02.partition(',')
            etree.SubElement(record, etree.QName(nsmap["rico"], "hasAuthor")).text = "https://amp.acdh.oeaw.ac.at/" + doc_author_02_abbr[0].lower() + "_" + doc_author_02_abbr[2][1].lower() + ".html"
        if document_object.doc_author_03 != "":
            doc_author_03_abbr = document_object.doc_author_03.partition(',')
            etree.SubElement(record, etree.QName(nsmap["rico"], "hasAuthor")).text = "https://amp.acdh.oeaw.ac.at/" + doc_author_03_abbr[0].lower() + "_" + doc_author_03_abbr[2][1].lower() + ".html"
        if document_object.doc_author_04 != "":
            doc_author_04_abbr = document_object.doc_author_04.partition(',')
            etree.SubElement(record, etree.QName(nsmap["rico"], "hasAuthor")).text = "https://amp.acdh.oeaw.ac.at/" + doc_author_04_abbr[0].lower() + "_" + doc_author_04_abbr[2][1].lower() + ".html"
        if document_object.doc_content_type != "":
            etree.SubElement(record, etree.QName(nsmap["rico"], "hasContentOfType")).text = document_object.doc_content_type
        if document_object.doc_language != "":
            etree.SubElement(record, etree.QName(nsmap["rico"], "hasOrHadLanguage")).text = document_object.doc_language
        # add ric record entry to record numerator
        number_records += 1

with open("C:/Users/tfruehwirth/Desktop/amp-data/data/ric_metadata/ric_metadata.csv", "r", newline='') as csv_file:
    table = csv.DictReader(csv_file, delimiter=',', quotechar='"')
    for row in table:
        # store author names in variables, and store variables in `doc_agents` list to enable `for` loop
        doc_agent_01 = row["document_author_01"]
        doc_agent_02 = row["document_author_02"]
        doc_agent_03 = row["document_author_03"]
        doc_agent_04 = row["document_author_04"]
        doc_agents = [doc_agent_01, doc_agent_02, doc_agent_03, doc_agent_04]
        for doc_agent in doc_agents:
            # test if variables are part of ric agent list or empty
            if doc_agent not in doc_agent_list and doc_agent != "":
                # create rdf/xml agent sub-elements
                agent = etree.SubElement(root, etree.QName(nsmap["rico"], "Agent"))
                doc_agent_abbr = doc_agent.partition(",")
                agent.attrib[etree.QName(nsmap["rdf"], "about")] = "https://amp.acdh.oeaw.ac.at/" + doc_agent_abbr[0].lower() + "_" + doc_agent_abbr[2][1].lower() + ".html"
                etree.SubElement(agent, etree.QName(nsmap["rico"], "hasOrHadAgentName")).text = doc_agent
                # add unlisted agent to ric agent list
                doc_agent_list.append(doc_agent)
                # add ric agent entry to agent numerator
                number_agents += 1

# write rdf/xml tree in rdf file
with open("C:/Users/tfruehwirth/Desktop/amp-data/data/ric_metadata/ric_metadata.rdf", "w") as rdf_file:
    rdf_file.write(str(etree.tostring(root, encoding="utf-8", xml_declaration=True, pretty_print=True).decode("utf-8")))

# print log
print("")
print(str(number_records) + " record entry/ies and " + str(number_agents) + " agent entry/ies written on " + str(datetime.now()) + ".")
print("\n             __|__\n        ______(_)______\n            \"  \"  \"\n")

# prompt user input w/ regard to starting rdf file
showFile = input("Thank you for flying with AMP. Do you want to open ric_metadata.rdf? Enter y/n: ")

if showFile.lower() == "y":
    print("Here you go.")
    #  start rdf file w/ its associated program
    os.startfile("C:/Users/tfruehwirth/Desktop/amp-data/data/ric_metadata/ric_metadata.rdf")
elif showFile.lower() == "n":
    print("Alrighty. Have a nice day.")
else:
    print("Invalid input.")
