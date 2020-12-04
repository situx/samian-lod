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
file_out = dir_path.replace("\\py", "\\ttl") + "\\" + "productioncentre.ttl"

# set input csv
csv = "productioncentre.csv"
url = "https://www1.rgzm.de/ips/lod/" + csv

print(url)

# read csv file
data = pd.read_csv(
    url,
    encoding='utf-8',
    sep='|',
    usecols=['id', 'label', 'lat', 'long', 'wikidata'],
    na_values=['.', '??']  # take any '.' or '??' values as NA
)
print(data.info())

# create triples from dataframe
lineNo = 2
outStr = ""
lines = []
for index, row in data.iterrows():
    # print(lineNo)
    tmpno = lineNo - 2
    if tmpno % 50 == 0:
        print(tmpno)
    lineNo += 1
    lines.append("samian:loc_pc_" + str(row['id']) + " " + "rdf:type" + " lado:Location .")
    lines.append("samian:loc_pc_" + str(row['id']) + " " + "amt:instanceOf" + " lado:Location .")
    lines.append("samian:loc_pc_" + str(row['id']) + " " + "lado:hasType" + " lado:ProductionCentre .")
    lines.append("samian:loc_pc_" + str(row['id']) + " " + "rdfs:label" + " " + "'" + str(row['label']).replace('\'', '`') + "'@en" + ".")
    lines.append("samian:loc_pc_" + str(row['id']) + " " + "dc:identifier" + " " + "" + str(row['id']) + "" + ".")
    lines.append("samian:loc_pc_" + str(row['id']) + " " + "lado:exactMatch" + " " + "wd:" + str(row['wikidata']) + " . ")
    # geom
    lines.append("samian:loc_pc_" + str(row['id']) + " " + "geosparql:hasGeometry" + " samian:loc_pc_" + str(row['id']) + "_geom .")
    lines.append("samian:loc_pc_" + str(row['id']) + "_geom " + "rdf:type" + " sf:Point .")
    point = "POINT(" + str(float(row['lat'])) + " " + str(float(row['long'])) + ")"
    point = "\"<http://www.opengis.net/def/crs/EPSG/0/4326> " + point + "\"^^geosparql:wktLiteral"
    lines.append("samian:loc_pc_" + str(row['id']) + "_geom " + "geosparql:asWKT " + point + ".")
    # prov-o
    lines.append("samian:loc_pc_" + str(row['id']) + " " + "prov:wasAttributedTo" + " samian:ImportPythonScript_Samian .")
    lines.append("samian:loc_pc_" + str(row['id']) + " " + "prov:wasDerivedFrom" + " <http://www.wikidata.org/entity/Q90412636> .")
    lines.append("samian:loc_pc_" + str(row['id']) + " " + "prov:wasGeneratedBy" + " samian:activity_loc_pc_" + str(row['id']) + " .")
    lines.append("samian:activity_loc_pc_" + str(row['id']) + " " + "rdf:type" + " <http://www.w3.org/ns/prov#Activity> .")
    lines.append("samian:activity_loc_pc_" + str(row['id']) + " " + "prov:startedAtTime '" + starttime + "'^^xsd:dateTime .")
    lines.append("samian:activity_loc_pc_" + str(row['id']) + " " + "prov:endedAtTime '" + datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "'^^xsd:dateTime .")
    lines.append("samian:activity_loc_pc_" + str(row['id']) + " " + "prov:wasAssociatedWith" + " samian:ImportPythonScript_Samian .")

files = (len(lines) / 100000) + 1
print("lines", len(lines), "files", int(files))

# write output file
print("start writing turtle file...")
file = codecs.open(file_out, "w", "utf-8")
file.write("# create triples from " + url + " \r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\nPREFIX sf: <http://www.opengis.net/ont/sf#> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\nPREFIX wd: <http://www.wikidata.org/entity/> \r\n"
prefixes += "\r\n"
file.write(prefixes)
for line in lines:
    file.write(line)
    file.write("\r\n")

print("Yuhu!")
file.close()
print("*****************************************")
print("SUCCESS")
print("closing script")
print("*****************************************")