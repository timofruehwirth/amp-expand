# import csv module
import csv

# create `ric_metadata.xml`
xml_file = open("C:/Users/tfruehwirth/Desktop/amp-data/data/ric_metadata/ric_metadata.xml", "w")

# opening file
with open("C:/Users/tfruehwirth/Desktop/amp-data/data/ric_metadata/ric_metadata.csv", "r", newline='') as csv_file:
    table = csv.DictReader(csv_file, delimiter=',', quotechar='"')
    for row in table:
        doc_id = row['document_id']
        doc_title = row['document_title']
        doc_date = row['document_date']
        doc_author = row['document_author']
        xml_file.write("\n<xml doc type etc.>")
        xml_file.write("\n<further xml info etc.>")
        if doc_id != "":
            xml_file.write("\n<" + doc_id + ">")
        if doc_title != "":
            xml_file.write("\n<" + doc_title + ">")
        if doc_date != "":
            xml_file.write("\n<" + doc_date + ">")
        if doc_author != "":
            xml_file.write("\n<" + doc_author + ">")
        xml_file.write("\n")

xml_file.close()
