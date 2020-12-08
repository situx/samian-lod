---
permalink: doc/
title: "Documentation"
header:
  image: /assets/images/header.jpg
  caption: "Photo credit: Carole Raddato from FRANKFURT, Germany, CC BY-SA 2.0, via [**Wikimedia Commons**](https://commons.wikimedia.org/wiki/File:Terra_sigillata,_Gallo-Roman_Museum_of_Tongeren,_Belgium_(27032316984).jpg)"
sidebar:
  nav: "barDoc"
---

# Linked Open Samian Ware

## Transformation Workflow

{% include figure image_path="/assets/images/Samian_Workflow.png" %}

The Data used for the Linked Open Samian Ware-Project stems from multiple resources (e.g. Corpus Vasorum Arretinorum, User Entries of the Samian Research-Community), resulting in a partly normalised database.
To counter this issue we included several steps from the original Samian Research Database to our finished LOD result.
Several steps (especially the cfm-scripts) were necessary in order to normalise our source data and transform it into RDF:

**curate** entries in the Samian Research Database, stored in a PostgreSQL database

**create** database views from the original database tables via ColdFusion/SQL

**export** database views as CSV files

**transform** CSV files with Python to RDF according to our ontology

**import** RDF files with a Java application in a RDF4J triplestore

**link** our data to the Linked Open Data Cloud, e.g. Pleiades, Wikidata

## Ontology

### Prefixes

Linked Open Samian Ware features several preestablished prefixes as well as our own prefix *lado* and *samian*.
Uses are demonstrated in the Maps and examples below.

| Prefix        | Value                                         |
| ------------- | --------------------------------------------- |
| **samian**    | <http://lod.archaeology.link/data/samian/>    |
| **crm**       | <http://www.cidoc-crm.org/cidoc-crm/>         |
| **dc**        | <http://purl.org/dc/elements/1.1/>            |
| **dct**       | <http://purl.org/dc/terms/>                   |
| **dcmitype**  | <http://purl.org/dc/dcmitype/>                |
| **geosparql** | <http://www.opengis.net/ont/geosparql#>>      |
| **lado**      | <http://samian/ontology>                      |
| **owl**       | <http://www.w3.org/2002/07/owl#>              |
| **pleiades**  | <https://pleiades.stoa.org/places/vocab#>     |
| **rdf**       | <http://www.w3.org/1999/02/22-rdf-syntax-ns#> |
| **rdfs**      | <http://www.w3.org/2000/01/rdf-schema#>       |
| **sf**        | <http://www.opengis.net/ont/sf#>              |
| **skos**      | <http://www.w3.org/2004/02/skos/core#>        |
| **xml**       | <http://www.w3.org/XML/1998/namespace>        |
| **xsd**       | <http://www.w3.org/2001/XMLSchema#>           |

### Class Structure

#### Samian Map

{% include figure image_path="/assets/images/SamianLod_map.png" %}

The ontology represents a graph model of the original relational database which includes vague relations (amt).
Classes (white boxes) are related to each other through predicates (arrows).
Checkered lines present abstract relations to type classes (yellow and grey) as well as AMT-relations, which belong to their superclass but have been highlighted for visibility.

#### Detailed InformationCarrier

{% include figure image_path="/assets/images/SamianLod_map_InformationCarrier.png" %}

**Example Query - InformationCarrier**

_-> 100 Random InformationCarriers and their associated Discovery Site, Production Centre and Repository Location_

<pre>
  <code>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lado: <http://archaeology.link/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT *  WHERE {
  ?item	rdf:type lado:InformationCarrier.
  ?item 	rdfs:label ?label.
  ?item 	lado:disclosedAt ?loc_disc.
  ?loc_disc 	rdfs:label ?disc_label.
  ?item	lado:hasKilnsite ?loc_prod.
  ?loc_prod 	rdfs:label ?prod_label.
  ?item	lado:storedAt ?loc_rep.
  ?loc_rep	rdfs:label ?rep_label.   	
}
LIMIT 100
  </code>
</pre>

_Output_

| **item**         | **label**                           | **loc_disc**          | **disc_label**      | **loc_prod**          | **prod_label** | **loc_rep**           | **rep_label**       |
| ---------------- | ----------------------------------- | --------------------- | ------------------- | --------------------- | -------------- | --------------------- | ------------------- |
| samian:ic_208496 | "redslipvessel formtype Unknown"@en | samian:loc_ds_1002687 | "Plessis-du-Mée"@en | samian:loc_pc_2000016 | "Lezoux"@en    | samian:loc_rl_3102331 | "Plessis-du-Mée"@en |
| samian:ic_207892 | "redslipvessel formtype 37"@en      | samian:loc_ds_1000357 | "Susa"@en           | samian:loc_pc_2000017 | "Lubié"@en     | samian:loc_rl_3446482 | "Susa"@en           |
| samian:ic_207892 | "redslipvessel formtype 37"@en      | samian:loc_ds_1000357 | "Susa"@en           | samian:loc_pc_2000016 | "Lezoux"@en    | samian:loc_rl_3446482 | "Susa"@en           |
| ...              | ...                                 | ...                   | ...                 | ...                   | ...            | ...                   | ...                 |

_-> 100 distinct InformationCarriers and their weight (vagueness) & production centres_

<pre>
  <code>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lado: <http://archaeology.link/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX vocab: <http://academic-meta-tool.xyz/vocab#>

SELECT ?item (SAMPLE (?Info_label) as ?Info_label) (SAMPLE(?weight)as ?weight) (SAMPLE (?prod_label) as ?prod_label) WHERE {
  ?item rdf:type lado:InformationCarrier;
  rdfs:label ?Info_label;
  lado:hasKilnsite ?productioncentre;
  lado:hasAMT ?amt.
  ?amt vocab:weight ?weight.
  ?productioncentre rdfs:label ?prod_label;
}
GROUP BY ?item
LIMIT 100
</code>
</pre>

_Output_

| **item**         | **Info_label**                      | **weight** | **prod_label** |
| ---------------- | ----------------------------------- | ---------- | -------------- |
| samian:ic_112680 | "redslipvessel formtype 31"@en      | 1          | "Lezoux"@en    |
| samian:ic_55293  | "redslipvessel formtype Unknown"@en | 1          | "Lezoux"@en    |
| samian:ic_55292  | "redslipvessel formtype Unknown"@en | 1          | "Lezoux"@en    |
| ...              | ...                                 | ...        | ...            |

#### Detailed Inscription

{% include figure image_path="/assets/images/SamianLod_map_Insription.png" %}

**Example Query - Inscription**

_-> Inscriptions with a reading stemming from a die impression and the actor which is mentioned in it_

<pre>
  <code>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lado: <http://archaeology.link/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT *  WHERE {
  ?insc	rdf:type lado:Inscription;
  lado:simpleReading ?reading;
  lado:hasType lado:DieImpression;
  lado:isAbout ?actor.
  ?actor lado:name ?name.  
}
  </code>
</pre>

_Output_

| **Insc**          | **Reading** | **Actor**         | **Name**                          |
| ----------------- | ----------- | ----------------- | --------------------------------- |
| samian:insc_43034 | "DIOMEDES"  | samian:ac_7010018 | "(M.) (Perennius) (Tigranus) (4)" |
| samian:insc_43389 | "POTITVS"   | samian:ac_7009673 | "Potitus (1)"                     |
| samian:insc_43415 | "PRIMVS"    | samian:ac_7009402 | "Primus (1)"                      |
| ...               | ...         | ...               | ...                               |

_-> InformationCarriers, their inscriptions and makingtypes_

<pre>
  <code>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lado: <http://archaeology.link/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?item ?info_label ?inscription ?inscriptionmakingtype ?die WHERE {
  ?item rdf:type lado:InformationCarrier;
  rdfs:label ?info_label;
  lado:carries ?inscription.
  ?inscription lado:wasMadeBy ?inscriptionmakingtype.
  ?inscriptionmakingtype lado:hasType ?die.
}
LIMIT 100
  </code>
</pre>

_Output_

| **item**         | **info_label**                      | **inscription** | **inscriptionmakingtype** | **die**  |
| ---------------- | ----------------------------------- | --------------- | ------------------------- | -------- |
| samian:ic_14040  | "redslipvessel formtype 27"@en      | samian:insc_1   | samian:mt_1               | lado:Die |
| samian:ic_14058  | "redslipvessel formtype Unknown"@en | samian:insc_10  | samian:mt_10              | lado:Die |
| samian:ic_202856 | "redslipvessel formtype 29"@en      | samian:insc_100 | samian:mt_100             | lado:Die |
| ...              | ...                                 | ...             | ...                       | ...      |

#### Detailed Actor

{% include figure image_path="/assets/images/SamianLod_map_Actor.png" %}

**Example Query - Actor**

_-> 100 Random ActorEntities and their associated Production Centre and Status_

<pre>
  <code>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lado: <http://archaeology.link/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT *  WHERE {
  ?actor_ent	rdf:type lado:ActorEntity;
  rdfs:label ?label;
  lado:hasStatus ?status;
  lado:worksAtPlace ?worksAt.
  ?worksAt rdfs:label ?loc_label.
}
LIMIT 100
  </code>
</pre>

_Output_

| **actor_ent**  | **label**          | **status**             | **worksAt**           | **loc_label** |
| -------------- | ------------------ | ---------------------- | --------------------- | ------------- |
| samian:ae_564  | "Arvernicus ii"@en | lado:IndependentPotter | samian:loc_pc_2000048 | "Sinzig"@en   |
| samian:ae_1044 | "Boudus ii"@en     | lado:IndependentPotter | samian:loc_pc_2000048 | "Sinzig"@en   |
| samian:ae_1541 | "Arvernicus ii"@en | lado:IndependentPotter | samian:loc_pc_2000048 | "Sinzig"@en   |
| ...            | ...                | ...                    | ...                   | ...           |

_-> ChiefPotters who interact with DependentPotters_

<pre>
  <code>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lado: <http://archaeology.link/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?chief ?chief_label ?dependent ?dependent_label  WHERE {
  ?chief rdf:type lado:ActorEntity;
  rdfs:label ?chief_label;
  lado:hasStatus lado:ChiefPotter;
  lado:interactsWith ?dependent.
  ?dependent rdf:type lado:ActorEntity;
  rdfs:label ?dependent_label;
  lado:hasStatus lado:DependentPotter.
}
  </code>
</pre>

_Output_

| **chief**       | **chief_label**               | **dependent**    | **dependent_label** |
| --------------- | ----------------------------- | ---------------- | ------------------- |
| samian:ae_10348 | "Vibius Iucun(dus) Vibius"@en | samian:ae_136996 | "IVCVN(DVS)"@en     |
| samian:ae_7878  | "Serius Thyrsus Serius"@en    | samian:ae_214084 | "THYRSVS"@en        |
| samian:ae_8314  | "L. Umbricius Thyrsus"@en     | samian:ae_214084 | "THYRSVS"@en        |
| ...             | ...                           | ...              | ...                 |

#### Detailed Location

{% include figure image_path="/assets/images/SamianLod_map_Location.png" %}

**Example Query - Location**

_-> Kilnregion, Workers & their Status of the Productioncentre "La Graufesenque"_

<pre>
  <code>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lado: <http://archaeology.link/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?loc_label ?kr_label ?name ?status WHERE {
  ?item rdf:type lado:Location.
  ?item rdfs:label ?loc_label.
  ?item rdfs:label "La Graufesenque"@en.
  ?item lado:clusteredAs ?kilnregion.
  ?kilnregion rdfs:label ?kr_label.
  ?item lado:hasWorker ?worker.
  ?worker lado:name ?name.
  ?worker lado:hasStatus ?status.
}
  </code>
</pre>

_Output_

| **loc_label**        | **kr_label**       | **name**                | **status**             |
| -------------------- | ------------------ | ----------------------- | ---------------------- |
| "La Graufesenque"@en | "South Gaulish"@en | "ABC (or Abc- or ABG-)" | lado:IndependentPotter |
| "La Graufesenque"@en | "South Gaulish"@en | "Abitus (Habitus)"      | lado:IndependentPotter |
| "La Graufesenque"@en | "South Gaulish"@en | "Acanus (Acaunus)"      | lado:IndependentPotter |
| ...                  | ...                | ...                     | ...                    |

#### Detailed Potform

{% include figure image_path="/assets/images/SamianLod_map_Potform.png" %}

**Example Query - Potform**

_-> Potforms and their labels with tradition "Gaulish"_

<pre>
  <code>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lado: <http://archaeology.link/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?item ?tradition ?label WHERE {
  ?item rdf:type lado:Potform.
  ?item lado:hasType ?tradition; lado:hasType lado:Gaulish.
  ?item rdfs:label ?label.
}
  </code>
</pre>

_Output_

| **Item**     | **Tradition** | **Label** |
| ------------ | ------------- | --------- |
| samian:pf_1  | lado:Gaulish  | "15"      |
| samian:pf_11 | lado:Gaulish  | "18/31"   |
| samian:pf_12 | lado:Gaulish  | "18/31R"  |
| ...          | ...           | ...       |

#### AMT-Model

{% include figure image_path="/assets/images/Samian_amt_model.png" %}

The data contains strings with vague expressions.
We model this vagueness using the Academic Meta Tool.
The AMT-Model depends on the keywords **AND** (_AMT-weight = 1_) and **OR** (_AMT-weight/2_).
Attributions for e.g. productionscenters can result in more than one place, which has to be recorded accordingly.
This vagueness has been taken into consideration with the Linked Open Samian Ware Project.

In the following examples we're mapping relations for the potter Quietus/Quetus (ae_5889), his production centres as well as the information carrier 118117 (ic_118117).

##### AMT-Model Examples

**Example 1:**

Samian AMT-Model for the potter **Quietus/Quetus (ae_5889)**
and the productioncentre **Rheinzabern (loc_pc_2000047)**:

{% include figure image_path="/assets/images/Samian_amt_model_ae_pc_example.png" %}

_Example Query: Filter all weights for the Potter Quietus' Productioncentres:_
The String containing the necessary data reads as follows "Kräherwald and Rheinzabern"

<pre>
  <code>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lado: <http://archaeology.link/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX amt: <http://academic-meta-tool.xyz/vocab#>
PREFIX samian: <http://data.archaeology.link/data/samian/>

SELECT ?subject ?subjectLabel ?predicateLabel ?objectLabel ?weight WHERE {
  ?subject lado:hasAMT ?amt.
  ?amt rdf:subject ?subject.
  ?subject rdfs:label ?subjectLabel.
  ?amt rdf:predicate ?predicate.
  ?predicate rdfs:label ?predicateLabel.
  ?amt rdf:object ?object.
  ?object rdfs:label ?objectLabel.
  ?amt amt:weight ?weight.
  FILTER(?subject = samian:ae_5889)
  FILTER(?predicate = lado:worksAtPlace)
  FILTER (lang(?predicateLabel) = 'en')
}
  </code>
</pre>

_Output:_

| **subject**    | **subjectLabel**      | **predicateLabel**  | **objectLabel**  | **weight** |
| -------------- | --------------------- | ------------------- | ---------------- | ---------- |
| samian:ae_5889 | "Quietus (Quetus)"@en | "works at place"@en | "Kräherwald"@en  | 1          |
| samian:ae_5889 | "Quietus (Quetus)"@en | "works at place"@en | "Rheinzabern"@en | 1          |

_-> Quietus worked at Kräherwald AND Rheinzabern, so the weight results in 1_

**Example 2:**

Samian AMT-Model for **information carrier 118117 (ic_118117)**
and the productioncentre **Rheinzabern (loc_pc_2000047)**:

{% include figure image_path="/assets/images/Samian_amt_model_ic_pc_example.png" %}

_Example Query: Filter all weights for the Kilnsites of Information Carrier 118117_
The String containing the necessary data reads as follows "Kräherwald and Rheinzabern"

<pre>
  <code>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lado: <http://archaeology.link/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX amt: <http://academic-meta-tool.xyz/vocab#>
PREFIX samian: <http://data.archaeology.link/data/samian/>

SELECT ?subject ?subjectLabel ?predicateLabel ?objectLabel ?weight WHERE {
  ?subject lado:hasAMT ?amt.
  ?amt rdf:subject ?subject.
  ?subject rdfs:label ?subjectLabel.
	?amt rdf:predicate ?predicate.
  ?predicate rdfs:label ?predicateLabel.
  ?amt rdf:object ?object.
  ?object rdfs:label ?objectLabel.
  ?amt amt:weight ?weight.
  FILTER(?subject = samian:ic_118117)
  FILTER(?predicate = lado:hasKilnsite)
  FILTER (lang(?predicateLabel) = 'en')
}
  </code>
</pre>

_Output:_

| **subject**      | **subjectLabel**                                 | **predicateLabel** | **objectLabel**  | **weight** |
| ---------------- | ------------------------------------------------ | ------------------ | ---------------- | ---------- |
| samian:ic_118117 | "redslipvessel formtype 15/17 or 18 or 18/31"@en | "has kilnsite"@en  | "Kräherwald"@en  | 1          |
| samian:ic_118117 | "redslipvessel formtype 15/17 or 18 or 18/31"@en | "has kilnsite"@en  | "Rheinzabern"@en | 1          |

_-> The Informationcarrier's Productioncentre has been attributed to Kräherwald AND Rheinzabern, so the weight results in 1_

**Example 3:**

Samian AMT-Model for **information carrier 118117 (ic_118117)**
and the potform **18 (pf_9)**:

{% include figure image_path="/assets/images/Samian_amt_model_ic_pf_example.png" %}

_Example Query: Filter all weights for the potforms of Information Carrier 118117_
The String containing the necessary data reads as follows "15/17 or 18 or 18/31"

<pre>
  <code>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lado: <http://archaeology.link/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX amt: <http://academic-meta-tool.xyz/vocab#>
PREFIX samian: <http://data.archaeology.link/data/samian/>

SELECT ?subject ?subjectLabel ?predicateLabel ?objectLabel ?weight WHERE {
	?subject lado:hasAMT ?amt.
  ?amt rdf:subject ?subject.
  ?subject rdfs:label ?subjectLabel.
	?amt rdf:predicate ?predicate.
  ?predicate rdfs:label ?predicateLabel.
  ?amt rdf:object ?object.
  ?object rdfs:label ?objectLabel.
  ?amt amt:weight ?weight.
  FILTER(?subject = samian:ic_118117)
  FILTER(?predicate = lado:representedBy)
  FILTER (lang(?predicateLabel) = 'en')
}
  </code>
</pre>

_Output:_

| **subject**      | **subjectLabel**                                 | **predicateLabel**  | **objectLabel** | **weight**  |
| ---------------- | ------------------------------------------------ | ------------------- | --------------- | ----------- |
| samian:ic_118117 | "redslipvessel formtype 15/17 or 18 or 18/31"@en | "represented by"@en | "15/17"         | 0.330000013 |
| samian:ic_118117 | "redslipvessel formtype 15/17 or 18 or 18/31"@en | "represented by"@en | "18"            | 0.330000013 |
| samian:ic_118117 | "redslipvessel formtype 15/17 or 18 or 18/31"@en | "represented by"@en | "18/31"         | 0.330000013 |

_-> The Informationcarriers either has the potform 15/17, 18 OR 18/31 (vagueness), so each weight results in 0.33_

## Provenance Modelling

{% include figure image_path="/assets/images/provO.jpg" %}

The provenance information for the transformation process is stored using the [PROV-O ontology](https://www.w3.org/TR/prov-o/). Each entity is modelled as item which is derived form the `Samian Research` database, was attributed to the `Python Transformation Script` which acted on behalf of Research Engineers (RGZM), and was generated by an `Algorithm Activity` (associated with the `Python Transformation Script`) with a defined start and ending point.

## CSV-Documentation

### File Structure

The CSV files can be downloaded under <https://www1.rgzm.de/ips/lod/{filename}.csv>

{% include figure image_path="/assets/images/Samian_universal_map.png" %}

Our CSV files are split into the categories *Instances*, containing unique lists (of classes/objects), and *Semantic Relations*, containing the necessary crosstables to link our instances by their IDs.

### Instances

| Name                        | Columns                     | Definition                             |
| --------------------------- | --------------------------- | -------------------------------------- |
| actorsasaconcept            | **id**                      | identifier (numeric)                   |
|                             | **name**                    | name of the potter                     |
| -------------------------   | -------------------------   | -------------------------              |
| chiefpotter                 | **id**                      | identifier (numeric)                   |
|                             | **name**                    | name of the potter                     |
|                             | **praenomen**               | praenomen of the potter                |
|                             | **cognomen**                | cognomen of the potter                 |
|                             | **slave**                   | name of associated dependent potter(s) |
|                             | **gentilicium**             | family name (gentilicium)              |
|                             | **partner**                 | name of associated partner potter(s)   |
|                             | **kilnsite**                | associated production centre(s)        |
| -------------------------   | -------------------------   | -------------------------              |
| cooperationandchiefpotter   | **id**                      | identifier (numeric)                   |
|                             | **name**                    | name of the potter                     |
|                             | **praenomen**               | praenomen of the potter                |
|                             | **cognomen**                | cognomen of the potter                 |
|                             | **slave**                   | name of associated dependent potter(s) |
|                             | **gentilicium**             | family name (gentilicium)              |
|                             | **partner**                 | name of associated partner potter(s)   |
|                             | **kilnsite**                | associated production centre(s)        |
| -------------------------   | -------------------------   | -------------------------              |
| cooperationpotter           | **id**                      | identifier (numeric)                   |
|                             | **pottername**              | name of the potter                     |
|                             | **praenomen**               | praenomen of the potter                |
|                             | **cognomen**                | cognomen of the potter                 |
|                             | **slave**                   | name of associated dependent potter(s) |
|                             | **gentilicium**             | family name (gentilicium)              |
|                             | **partner**                 | name of associated partner potter(s)   |
|                             | **kilnsite**                | associated production centre(s)        |
| -------------------------   | -------------------------   | -------------------------              |
| dependentpotter             | **id**                      | identifier (numeric)                   |
|                             | **slave**                   | name of the dependent potter           |
| -------------------------   | -------------------------   | -------------------------              |
| discoverysite               | **id**                      | identifier (numeric)                   |
|                             | **label**                   | identifier (string)                    |
|                             | **long**                    | longitude                              |
|                             | **pleiades_id**             | pleiades id                            |
|                             | **ancientname**             | ancient name of the site               |
|                             | **wkt**                     | well-known text format                 |
| -------------------------   | -------------------------   | -------------------------              |
| genericpotform              | **id**                      | identifier (numeric)                   |
|                             | **label**                   | identifier (string)                    |
| -------------------------   | -------------------------   | -------------------------              |
| independentpotter           | **id**                      | identifier (numeric)                   |
|                             | **pottername**              | name of the potter                     |
|                             | **praenomen**               | praenomen of the potter                |
|                             | **cognomen**                | cognomen of the potter                 |
|                             | **slave**                   | name of associated dependent potter(s) |
|                             | **gentilicium**             | family name (gentilicium)              |
|                             | **partner**                 | name of associated partner potter(s)   |
|                             | **kilnsite**                | associated production centre(s)        |
| -------------------------   | -------------------------   | -------------------------              |
| informationcarrier          | **id**                      | identifier (numeric)                   |
|                             | **label**                   | identifier (string)                    |
|                             | **shapes**                  | formtype (int)                         |
|                             | **number**                  | number of pieces                       |
|                             | **kilnsite**                | associated production centre(s)        |
|                             | **pottername**              | name of the potter                     |
|                             | **die**                     | die stamp or stylus                    |
|                             | **site**                    | discoverysite of the object(s)         |
|                             | **repositorysite**          | repositorysite of the object(s)        |
| -------------------------   | -------------------------   | -------------------------              |
| inscriptiondie              | **id**                      | identifier (numeric)                   |
|                             | **reading**                 | reading on the object(s)               |
|                             | **simplereading**           | simplified reading on the object(s)    |
|                             | **direction**               | reading direction of the inscription   |
| -------------------------   | -------------------------   | -------------------------              |
| inscriptiongraffito         | **id**                      | identifier (numeric)                   |
|                             | **reading**                 | reading on the object(s)               |
|                             | **simplereading**           | simplified reading on the object(s)    |
|                             | **direction**               | reading direction of the inscription   |
| -------------------------   | -------------------------   | -------------------------              |
| inscriptionmakingtypedie    | **id**                      | identifier (numeric)                   |
|                             | **label**                   | identifier (string)                    |
|                             | **pottername**              | name of the potter                     |
|                             | **die**                     | die stamp or stylus                    |
| -------------------------   | -------------------------   | -------------------------              |
| inscriptionmakingtypestylus | **id**                      | identifier (numeric)                   |
|                             | **label**                   | identifier (string)                    |
|                             | **pottername**              | name of the potter                     |
|                             | **die**                     | die stamp or stylus                    |
| -------------------------   | -------------------------   | -------------------------              |
| kilnregion                  | **id**                      | identifier (numeric)                   |
|                             | **label**                   | identifier (string)                    |
|                             | **kilnregion_centroid_wkt** | well-known text centroid (geometry)    |
|                             | **kilnregion_wkt**          | well-known text (geometry)             |
| -------------------------   | -------------------------   | -------------------------              |
| partnerpotter               | **id**                      | identifier (numeric)                   |
|                             | **name**                    | name of the potter                     |
| -------------------------   | -------------------------   | -------------------------              |
| placeasaconcept             | **id**                      | identifier (numeric)                   |
|                             | **label**                   | identifier (string)                    |
| -------------------------   | -------------------------   | -------------------------              |
| potformgaulish              | **id**                      | identifier (numeric)                   |
|                             | **label**                   | identifier (string)                    |
|                             | **image**                   | image of potform                       |
|                             | **genericform**             | generic potform label                  |
|                             | **tradition**               | tradition gaulish or italian           |
| -------------------------   | -------------------------   | -------------------------              |
| potformitalian              | **id**                      | identifier (numeric)                   |
|                             | **label**                   | identifier (string)                    |
|                             | **image**                   | image of potform                       |
|                             | **genericform**             | generic potform label                  |
|                             | **tradition**               | tradition gaulish or italian           |
| -------------------------   | -------------------------   | -------------------------              |
| productioncentre            | **id**                      | identifier (numeric)                   |
|                             | **label**                   | identifier (string)                    |
|                             | **kilnregion**              | Region of productioncentre             |
|                             | **lat**                     | latitude                               |
|                             | **long**                    | longitude                              |
|                             | **wkt**                     | well-known text format                 |
| -------------------------   | -------------------------   | -------------------------              |
| repositorylocation          | **id**                      | identifier (numeric)                   |
|                             | **label**                   | identifier (string)                    |

### Semantic Relations

| Name                      | Columns                   | Definition                                                                                                                      |
| ------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| ct_ac_ae                  | **ac_id**                 | actorsasaconcept.id                                                                                                             |
|                           | **ae_id**                 | chiefpotter.id, cooperationpotter.id, independentpotter.id - partnerpotter.id, dependentpotter.id, cooperationandchiefpotter.id |
| ------------------------- | ------------------------- | -------------------------                                                                                                       |
| ct_cpchp_dp               | **cpchp_id**              | cooperationandchiefpotter.id                                                                                                    |
|                           | **dp_id**                 | dependentpotter.id                                                                                                              |
| ------------------------- | ------------------------- | -------------------------                                                                                                       |
| ct_cpchp_pp               | **cpchp_id**              | cooperationandchiefpotter.id                                                                                                    |
|                           | **pp_id**                 | partnerpotter.id                                                                                                                |
| ------------------------- | ------------------------- | -------------------------                                                                                                       |
| ct_ae_pc                  | **ae_id**                 | ct_ac_ae.fk2                                                                                                                    |
|                           | **pc_id**                 | ct_ac_ae.productioncentre                                                                                                       |
|                           | **weight**                | ct_ae_pc_2.weight                                                                                                               |
| ------------------------- | ------------------------- | -------------------------                                                                                                       |
| ct_chp_dp                 | **chp_id**                | chiefpotter.id                                                                                                                  |
|                           | **dp_id**                 | dependentpotter.id                                                                                                              |
| ------------------------- | ------------------------- | -------------------------                                                                                                       |
| ct_cp_pp                  | **cp_id**                 | cooperationpotter.id                                                                                                            |
|                           | **pp_id**                 | partnerpotter.id                                                                                                                |
| ------------------------- | ------------------------- | -------------------------                                                                                                       |
| ct_ic_ds                  | **ic_id**                 | informationcarrier.id                                                                                                           |
|                           | **ds_id**                 | discoverysite.id                                                                                                                |
| ------------------------- | ------------------------- | -------------------------                                                                                                       |
| ct_ic_in                  | **ic_id**                 | informationcarrier.id                                                                                                           |
|                           | **pottername**            | informationcarrier.pottername                                                                                                   |
|                           | **die**                   | informationcarrier.die                                                                                                          |
| ------------------------- | ------------------------- | -------------------------                                                                                                       |
| ct_ic_pc                  | **ic_id**                 | ct_ic_pc_2.id                                                                                                                   |
|                           | **pc_id**                 | productioncentre.id                                                                                                             |
|                           | **weight**                | ct_ic_pc_2.weight                                                                                                               |
| ------------------------- | ------------------------- | -------------------------                                                                                                       |
| ct_ic_pf                  | **ic_id**                 | ct_ic_pf_2.id                                                                                                                   |
|                           | **weight**                | ct_ic_pf_2.weight                                                                                                               |
|                           | **pf_id**                 | potform.id                                                                                                                      |
| ------------------------- | ------------------------- | -------------------------                                                                                                       |
| ct_ic_plc                 | **plc_id**                | placeasaconcept.id                                                                                                              |
|                           | **ic_id**                 | informationcarrier.id                                                                                                           |
| ------------------------- | ------------------------- | -------------------------                                                                                                       |
| ct_ic_rl                  | **ic_id**                 | informationcarrier.id                                                                                                           |
|                           | **rl_id**                 | repositorylocation.id                                                                                                           |
| ------------------------- | ------------------------- | -------------------------                                                                                                       |
| ct_in_ac                  | **in_id**                 | inscription.id                                                                                                                  |
|                           | **ac_id**                 | actorsasaconcept.id                                                                                                             |
| ------------------------- | ------------------------- | -------------------------                                                                                                       |
| ct_mt_in                  | **in_id**                 | inscription.id                                                                                                                  |
|                           | **mt_id**                 | inscriptionmakingtype.id                                                                                                        |
| ------------------------- | ------------------------- | -------------------------                                                                                                       |
| ct_pc_kr                  | **kr_id**                 | kilnregion.id                                                                                                                   |
|                           | **pc_id**                 | productioncentre.id                                                                                                             |
| ------------------------- | ------------------------- | -------------------------                                                                                                       |
| ct_pf_gf                  | **gf_id**                 | genericpotform.id                                                                                                               |
|                           | **pf_id**                 | potform.id                                                                                                                      |
| ------------------------- | ------------------------- | -------------------------                                                                                                       |
| ct_plc_ds                 | **plc_id**                | placeasaconcept.id                                                                                                              |
|                           | **ds_id**                 | discoverysite.id                                                                                                                |
| ------------------------- | ------------------------- | -------------------------                                                                                                       |
| ct_plc_pc                 | **plc_id**                | placeasaconcept.id                                                                                                              |
|                           | **pc_id**                 | productioncentre.id                                                                                                             |
| ------------------------- | ------------------------- | -------------------------                                                                                                       |
| ct_plc_rl                 | **plc_id**                | placeasaconcept.id                                                                                                              |
|                           | **rl_id**                 | repositylocation.id                                                                                                             |
