---
permalink: doc/
title: "Documentation"
header:
  image: /assets/images/header.jpg
---

# About Linked Samian Ware

## Ontology

### Prefixes

**samian**:
  <http://lod.archaeology.link/data/samian/>

**crm**:
  <http://www.cidoc-crm.org/cidoc-crm/>

**dc**:
  <http://purl.org/dc/elements/1.1/>

**dct**:
  <http://purl.org/dc/terms/>

**dcmitype**:
  <http://purl.org/dc/dcmitype/>

**geosparql**:
  <http://www.opengis.net/ont/geosparql#>>

**lado**:
  <http://samian/ontology>

**owl**:
  <http://www.w3.org/2002/07/owl#>

**pleiades**:
  <https://pleiades.stoa.org/places/vocab#>

**rdf**:
  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

**rdfs**:
  <http://www.w3.org/2000/01/rdf-schema#>

**sf**:
  <http://www.opengis.net/ont/sf#>

**skos**:
  <http://www.w3.org/2004/02/skos/core#>

**xml**:
  <http://www.w3.org/XML/1998/namespace>

**xsd**:
  <http://www.w3.org/2001/XMLSchema#>

### Class Structure

#### Samian Map

{% include figure image_path="/assets/images/SamianLod_map.png" %}

#### Detailed InformationCarrier

{% include figure image_path="/assets/images/SamianLod_map_InformationCarrier.png" %}

#### Detailed Inscription

{% include figure image_path="/assets/images/SamianLod_map_Insription.png" %}

#### Detailed Actor

{% include figure image_path="/assets/images/SamianLod_map_Actor.png" %}

#### Detailed Location

{% include figure image_path="/assets/images/SamianLod_map_Location.png" %}

#### Detailed Potform

{% include figure image_path="/assets/images/SamianLod_map_Potform.png" %}

#### AMT-Model

{% include figure image_path="/assets/images/Samian_amt_model.png" %}

##### AMT-Model Examples

Samian AMT-Model for the potter **Advocisus (ae_120)**
and the productioncentre **Lezoux (loc_pc_2000016)**:

{% include figure image_path="/assets/images/Samian_amt_model_ae_pc_example.png" %}

Samian AMT-Model for **information carrier 203109 (ic_203109)**
and the productioncentre **Lezoux (loc_pc_2000016)**:

{% include figure image_path="/assets/images/Samian_amt_model_ic_pc_example.png" %}

Samian AMT-Model for **information carrier 203109 (ic_203109)**
and the potform **Dragendorff 33 (pf_28)**:

{% include figure image_path="/assets/images/Samian_amt_model_ic_pf_example.png" %}

## CSV-Documentation

### File Structure

{% include figure image_path="/assets/images/Samian_universal_map.png" %}

### Unique:

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
|                             | **pleiades_id**             | ---                                    |
|                             | **ancientname**             | ---                                    |
|                             | **wkt**                     | ---                                    |
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
|                             | **shapes**                  | ---                                    |
|                             | **number**                  | ---                                    |
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
|                             | **kilnregion_centroid_wkt** | ---                                    |
|                             | **kilnregion_wkt**          | ---                                    |
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
|                             | **wkt**                     | ---                                    |
| -------------------------   | -------------------------   | -------------------------              |
| repositorylocation          | **id**                      | identifier (numeric)                   |
|                             | **label**                   | identifier (string)                    |

### Crosstables:

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

## Samian Workflow

{% include figure image_path="/assets/images/Samian_Workflow.png" %}

## Credits

-   Florian Thiery M.Sc. (Römisch-Germanisches Zentralmuseum Leibniz-Forschungsinstitut für Archäologie)
-   Dr. Allard Mees FSA (Römisch-Germanisches Zentralmuseum Leibniz-Forschungsinstitut für Archäologie)
-   Dennis Gottwald B.A. (JGU Mainz)
