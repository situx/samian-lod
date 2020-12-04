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

dir_path = os.path.dirname(os.path.realpath(__file__))
file_out_1 = dir_path.replace("\\py", "\\ttl") + "\\" + "ct_ic_in_1.ttl"
file_out_2 = dir_path.replace("\\py", "\\ttl") + "\\" + "ct_ic_in_2.ttl"
file_out_3 = dir_path.replace("\\py", "\\ttl") + "\\" + "ct_ic_in_3.ttl"
file_out_4 = dir_path.replace("\\py", "\\ttl") + "\\" + "ct_ic_in_4.ttl"

# set input csv
csv = "ct_ic_in.csv"
url = "https://www1.rgzm.de/ips/lod/" + csv

print(url)

# read csv file
data = pd.read_csv(
    url,
    encoding='utf-8',
    sep='|',
    usecols=['ic_id', 'in_id', 'dieposition']
)
print(data.info())

# create triples from dataframe
lineNo = 2
outStr = ""
lines = []
for index, row in data.iterrows():
    # print(lineNo)
    tmpno = lineNo - 2
    if tmpno % 25000 == 0:
        print(tmpno)
    lineNo += 1
    lines.append("samian:ic_" + str(row['ic_id']) + " lado:carries " + "samian:insc_" + str(row['in_id']) + ".")
    lines.append("samian:ic_" + str(row['ic_id']) + " " + "lado:dieposition" + "'" + str(row['dieposition']).replace('\'', '`') + "'" + ".")

files = (len(lines) / 100000) + 1
print("triples", len(lines), "files", int(files))

# write output file
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

print("*****************************************")
print("SUCCESS")
print("closing script")
print("*****************************************")
