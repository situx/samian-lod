__author__ = "Florian Thiery, Dennis Gottwald"
__copyright__ = "MIT Licence 2020, RGZM, Florian Thiery"
__credits__ = ["Florian Thiery, Dennis Gottwald"]
__license__ = "MIT"
__version__ = "beta"
__maintainer__ = "Florian Thiery"
__email__ = "thiery@rgzm.de"
__status__ = "beta"
__update__ = "2020-12-09"

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

# set input csv
csv = "independentpotter.csv"
url = "https://www1.rgzm.de/ips/lod/" + csv

print(url)

# read csv file
data = pd.read_csv(
    url,
    encoding='utf-8',
    sep='|',
    usecols=['id', 'name', 'praenomen', 'cognomen', 'gentilicium', 'kilnsite', 'timeinterval']
)
print(data.info())

# create triples from dataframe
lineNo = 2
outStr = ""
lines = []
for index, row in data.iterrows():
    # print(lineNo)
    tmpno = lineNo - 2
    if tmpno % 1000 == 0:
        print(tmpno)
    lineNo += 1
    lines.append("samian:ae_" + str(row['id']) + " " + "rdf:type" + " lado:ActorEntity .")
    lines.append("samian:ae_" + str(row['id']) + " " + "amt:instanceOf" + " lado:ActorEntity .")
    lines.append("samian:ae_" + str(row['id']) + " " + "rdfs:label" + " " + "'" + str(row['name']).replace('\'', '`') + "'@en" + ".")
    lines.append("samian:ae_" + str(row['id']) + " " + "lado:name" + " " + "'" + str(row['name']).replace('\'', '`') + "'" + ".")
    if str(row['praenomen']).replace('\'', '`') != 'nan':
        if str(row['praenomen']).replace('\'', '`') != '?':
            lines.append("samian:ae_" + str(row['id']) + " " + "lado:praenomen " + "'" + "" + str(row['praenomen']).replace('\'', '`') + "'" + ".")
    if str(row['praenomen']).replace('\'', '`') != 'nan':
        if str(row['praenomen']).replace('\'', '`') != '?':
            lines.append("samian:ae_" + str(row['id']) + " " + "lado:cognomen " + "'" + "" + str(row['cognomen']).replace('\'', '`') + "'" + ".")
    if str(row['praenomen']).replace('\'', '`') != 'nan':
        if str(row['praenomen']).replace('\'', '`') != '?':
            lines.append("samian:ae_" + str(row['id']) + " " + "lado:gentilicium " + "'" + "" + str(row['gentilicium']).replace('\'', '`') + "'" + ".")
    if str(row['praenomen']).replace('\'', '`') != 'nan':
        if str(row['praenomen']).replace('\'', '`') != '?':
            lines.append("samian:ae_" + str(row['id']) + " " + "lado:worksAtPlaceString " + "'" + "" + str(row['kilnsite']).replace('\'', '`') + "'" + ".")
    if str(row['timeinterval']).replace('\'', '`') != 'nan':
        if str(row['timeinterval']).replace('\'', '`') != '?':
            lines.append("samian:ae_" + str(row['id']) + " " + "lado:timeinterval " + "'" + str(row['timeinterval']).replace('\'', '`') + "'" + ".")
    lines.append("samian:ae_" + str(row['id']) + " " + "dc:identifier" + " " + "'" + str(row['id']) + "'" + ".")
    lines.append("samian:ae_" + str(row['id']) + " " + "lado:hasStatus" + " lado:IndependentPotter .")
    lines.append("samian:ae_" + str(row['id']) + " " + "lado:hasType" + " lado:Potmaker .")
    lines.append("samian:ae_" + str(row['id']) + " " + "lado:hasType" + " lado:MouldMaker .")
    lines.append("samian:ae_" + str(row['id']) + " " + "lado:hasType" + " lado:KilnFiringPerson .")
    # prov-o
    lines.append("samian:ae_" + str(row['id']) + " " + "prov:wasAttributedTo" + " samian:ImportPythonScript_Samian .")
    lines.append("samian:ae_" + str(row['id']) + " " + "prov:wasDerivedFrom" + " <http://www.wikidata.org/entity/Q90412636> .")
    lines.append("samian:ae_" + str(row['id']) + " " + "prov:wasGeneratedBy" + " samian:activity_ae_" + str(row['id']) + " .")
    lines.append("samian:activity_ae_" + str(row['id']) + " " + "rdf:type" + " <http://www.w3.org/ns/prov#Activity> .")
    lines.append("samian:activity_ae_" + str(row['id']) + " " + "prov:startedAtTime '" + starttime + "'^^xsd:dateTime .")
    lines.append("samian:activity_ae_" + str(row['id']) + " " + "prov:endedAtTime '" + datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "'^^xsd:dateTime .")
    lines.append("samian:activity_ae_" + str(row['id']) + " " + "prov:wasAssociatedWith" + " samian:ImportPythonScript_Samian .")

files = (len(lines) / 100000) + 1
print("triples", len(lines), "files", int(files))

# set output path
dir_path = os.path.dirname(os.path.realpath(__file__))

# write output files
print("start writing turtle files...")

f = 0
step = 100000
fileprefix = "ae_independentpotter_"
prefixes = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \r\nPREFIX owl: <http://www.w3.org/2002/07/owl#> \r\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \r\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \r\nPREFIX geosparql: <http://www.opengis.net/ont/geosparql#> \r\nPREFIX dc: <http://purl.org/dc/elements/1.1/> \r\nPREFIX sf: <http://www.opengis.net/ont/sf#> \r\n"
prefixes += "PREFIX lado: <http://archaeology.link/ontology#> \r\nPREFIX samian: <http://data.archaeology.link/data/samian/> \r\nPREFIX wd: <http://www.wikidata.org/entity/> \r\n PREFIX pelagios: <http://pelagios.github.io/vocab/terms#> \r\nPREFIX oa: <http://www.w3.org/ns/oa#> \r\nPREFIX dcterms: <http://purl.org/dc/terms/> \r\nPREFIX foaf: <http://xmlns.com/foaf/0.1/> \r\nPREFIX relations: <http://pelagios.github.io/vocab/relations#> \r\nPREFIX cnt: <http://www.w3.org/2011/content#> \r\nPREFIX pleiades: <http://pleiades.stoa.org/places/> \r\nPREFIX amt: <http://academic-meta-tool.xyz/vocab#> \r\n"
prefixes += "\r\n"
for x in range(1, int(files) + 1):
    strX = str(x)
    filename = dir_path.replace("\\py", "\\ttl") + "\\" + fileprefix + strX + ".ttl"
    file = codecs.open(filename, "w", "utf-8")
    file.write("# create triples from " + url + " \r\n")
    file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n\r\n")
    file.write(prefixes)
    i = f
    for i, line in enumerate(lines):
        if (i > f - 1 and i < f + step):
            file.write(line)
            file.write("\r\n")
    f = f + step
    print("Yuhu! > " + fileprefix + strX + ".ttl")
    file.close()

print("*****************************************")
print("SUCCESS")
print("closing script")
print("*****************************************")
