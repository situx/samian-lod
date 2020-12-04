__author__ = "Florian Thiery, Dennis Gottwald"
__copyright__ = "MIT Licence 2020, RGZM, Florian Thiery"
__credits__ = ["Florian Thiery, Dennis Gottwald"]
__license__ = "MIT"
__version__ = "beta"
__maintainer__ = "Florian Thiery"
__email__ = "thiery@rgzm.de"
__status__ = "beta"
__update__ = "2020-12-03"

# import dependencies
import uuid
import requests
import io
import pandas as pd
import os
import codecs
import datetime
import importlib  # py3
import sys

# set UTF8 as default
importlib.reload(sys)  # py3
# reload(sys) #py2

# uncomment the line below when using Python version <3.0
# sys.setdefaultencoding('UTF8')

# set starttime
starttime = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

# set output path
dir_path = os.path.dirname(os.path.realpath(__file__))
file_out_1 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_1.ttl"
file_out_2 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_2.ttl"
file_out_3 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_3.ttl"
file_out_4 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_4.ttl"
file_out_5 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_5.ttl"
file_out_6 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_6.ttl"
file_out_7 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_7.ttl"
file_out_8 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_8.ttl"
file_out_9 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_9.ttl"
file_out_10 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_10.ttl"
file_out_11 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_11.ttl"
file_out_12 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_12.ttl"
file_out_13 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_13.ttl"
file_out_14 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_14.ttl"
file_out_15 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_15.ttl"
file_out_16 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_16.ttl"
file_out_17 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_17.ttl"
file_out_18 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_18.ttl"
file_out_19 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_19.ttl"
file_out_20 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_20.ttl"
file_out_21 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_21.ttl"
file_out_22 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_22.ttl"
file_out_23 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_23.ttl"
file_out_24 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_24.ttl"
file_out_25 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_25.ttl"
file_out_26 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_26.ttl"
file_out_27 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_27.ttl"
file_out_28 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_28.ttl"
file_out_29 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_29.ttl"
file_out_30 = dir_path.replace("\\py", "\\ttl") + "\\" + "informationcarrier_30.ttl"

# set input csv
csv = "informationcarrier.csv"
url = "https://www1.rgzm.de/ips/lod/" + csv

print(url)

# read csv file
data = pd.read_csv(
    url,
    encoding='utf-8',
    sep='|',
    usecols=['id', 'label', 'shapes', 'number', 'kilnsite', 'timeinterval']
)
print(data.info())

# create triples from dataframe
lineNo = 2
outStr = ""
lines = []
for index, row in data.iterrows():
    # print(lineNo)
    tmpno = lineNo - 2
    if tmpno % 10000 == 0:
        print(tmpno)
    lineNo += 1
    lines.append("samian:ic_" + str(row['id']) + " " + "rdf:type" + " lado:InformationCarrier .")
    lines.append("samian:ic_" + str(row['id']) + " " + "amt:instanceOf" + " lado:InformationCarrier .")
    lines.append("samian:ic_" + str(row['id']) + " " + "rdfs:label" + " " + "'" + str(row['label']).replace('\'', '`') + "'@en" + ".")
    lines.append("samian:ic_" + str(row['id']) + " " + "lado:number" + " " + "" + str(row['number']).replace('\'', '`') + "" + ".")
    lines.append("samian:ic_" + str(row['id']) + " " + "lado:hasKilnsiteString" + " " + "'" + str(row['kilnsite']).replace('\'', '`') + "'" + ".")
    lines.append("samian:ic_" + str(row['id']) + " " + "lado:representedByString" + " " + "'" + str(row['shapes']).replace('\'', '`') + "'" + ".")
    lines.append("samian:ic_" + str(row['id']) + " " + "dc:identifier" + " " + "" + str(row['id']) + "" + ".")
    if str(row['timeinterval']).replace('\'', '`') != 'nan':
        if str(row['timeinterval']).replace('\'', '`') != '?':
            lines.append("samian:ic_" + str(row['id']) + " " + "lado:timeinterval " + "'" + str(row['timeinterval']).replace('\'', '`') + "'" + ".")
    # prov-o
    lines.append("samian:ic_" + str(row['id']) + " " + "prov:wasAttributedTo" + " samian:ImportPythonScript_Samian .")
    lines.append("samian:ic_" + str(row['id']) + " " + "prov:wasDerivedFrom" + " <http://www.wikidata.org/entity/Q90412636> .")
    lines.append("samian:ic_" + str(row['id']) + " " + "prov:wasGeneratedBy" + " samian:activity_ic_" + str(row['id']) + " .")
    lines.append("samian:activity_ic_" + str(row['id']) + " " + "rdf:type" + " <http://www.w3.org/ns/prov#Activity> .")
    lines.append("samian:activity_ic_" + str(row['id']) + " " + "prov:startedAtTime '" + starttime + "'^^xsd:dateTime .")
    lines.append("samian:activity_ic_" + str(row['id']) + " " + "prov:endedAtTime '" + datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "'^^xsd:dateTime .")
    lines.append("samian:activity_ic_" + str(row['id']) + " " + "prov:wasAssociatedWith" + " samian:ImportPythonScript_Samian .")

files = (len(lines) / 100000) + 1
print("lines", len(lines), "files", int(files))

# write output files
print("start writing turtle file...")

file = codecs.open(file_out_1, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 0
for i, line in enumerate(lines):
    if (i > -1 and i < 100000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_2, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 100000
for i, line in enumerate(lines):
    if (i > 99999 and i < 200000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_3, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 200000
for i, line in enumerate(lines):
    if (i > 199999 and i < 300000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_4, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 300000
for i, line in enumerate(lines):
    if (i > 299999 and i < 400000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_5, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 400000
for i, line in enumerate(lines):
    if (i > 399999 and i < 500000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_6, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 500000
for i, line in enumerate(lines):
    if (i > 499999 and i < 600000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_7, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 600000
for i, line in enumerate(lines):
    if (i > 599999 and i < 700000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_8, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 700000
for i, line in enumerate(lines):
    if (i > 699999 and i < 800000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_9, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 800000
for i, line in enumerate(lines):
    if (i > 799999 and i < 900000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_10, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 900000
for i, line in enumerate(lines):
    if (i > 899999 and i < 1000000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_11, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 1000000
for i, line in enumerate(lines):
    if (i > 999999 and i < 1100000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_12, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 1100000
for i, line in enumerate(lines):
    if (i > 1099999 and i < 1200000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_13, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 1200000
for i, line in enumerate(lines):
    if (i > 1199999 and i < 1300000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_14, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 1300000
for i, line in enumerate(lines):
    if (i > 1299999 and i < 1400000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_15, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 1400000
for i, line in enumerate(lines):
    if (i > 1399999 and i < 1500000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_16, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 1500000
for i, line in enumerate(lines):
    if (i > 1499999 and i < 1600000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_17, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 1600000
for i, line in enumerate(lines):
    if (i > 1599999 and i < 1700000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_18, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 1700000
for i, line in enumerate(lines):
    if (i > 1699999 and i < 1800000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_19, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 1800000
for i, line in enumerate(lines):
    if (i > 1799999 and i < 1900000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_20, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 1900000
for i, line in enumerate(lines):
    if (i > 1899999 and i < 2000000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_21, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 2000000
for i, line in enumerate(lines):
    if (i > 1999999 and i < 2100000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_22, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 2100000
for i, line in enumerate(lines):
    if (i > 2099999 and i < 2200000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_23, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 2200000
for i, line in enumerate(lines):
    if (i > 2199999 and i < 2300000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_24, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 2300000
for i, line in enumerate(lines):
    if (i > 2299999 and i < 2400000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_25, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 2400000
for i, line in enumerate(lines):
    if (i > 2399999 and i < 2500000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_26, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 2500000
for i, line in enumerate(lines):
    if (i > 2499999 and i < 2600000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_27, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 2600000
for i, line in enumerate(lines):
    if (i > 2599999 and i < 2700000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_28, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 2700000
for i, line in enumerate(lines):
    if (i > 2699999 and i < 2800000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_29, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 2800000
for i, line in enumerate(lines):
    if (i > 2799999 and i < 2900000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

file = codecs.open(file_out_30, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
file.write(prefixes)
i = 2900000
for i, line in enumerate(lines):
    if (i > 2899999 and i < 3000000):
        file.write(line)
        file.write("\r\n")
print("Yuhu!")
file.close()

print("*****************************************")
print("SUCCESS")
print("closing script")
print("*****************************************")
