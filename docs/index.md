# About Samian Research

# About Linked Samian Ware

# Ontology

## Prefixes

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

## Class Structure

### Samian Map

![SamianLod_map](/assets/SamianLod_map.png)

### Detailed InformationCarrier

![SamianLod_map_InformationCarrier](/assets/SamianLod_map_InformationCarrier.png)

### Detailed Inscription

![SamianLod_map_Insription](/assets/SamianLod_map_Insription.png)

### Detailed Actor

![SamianLod_map_Actor](/assets/SamianLod_map_Actor.png)

### Detailed Location

![SamianLod_map_Location](/assets/SamianLod_map_Location.png)

### Detailed Potform

![SamianLod_map_Potform](/assets/SamianLod_map_Potform.png)

### AMT-Model

![Samian_amt_model](/assets/Samian_amt_model.png)

#### AMT-Model Examples

Samian AMT-Model for the potter **Advocisus (ae_120)**
and the productioncentre **Lezoux (loc_pc_2000016)**:
![Samian_amt_model_ae_pc](/assets/Samian_amt_model_ae_pc_example.png)
Samian AMT-Model for **information carrier 203109 (ic_203109)**
and the productioncentre **Lezoux (loc_pc_2000016)**:
![Samian_amt_model_ic_pc](/assets/Samian_amt_model_ic_pc_example.png)
Samian AMT-Model for **information carrier 203109 (ic_203109)**
and the potform **Dragendorff 33 (pf_28)**:
![Samian_amt_model_ic_pf](/assets/Samian_amt_model_ic_pf_example.png)

# CSV-Documentation

## File Structure

![Samian_universal_map](/assets/Samian_universal_map.png)

## Crosstables:

| Name                      | Columns                                                                                                                                               | Definition                |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| ct_ac_ae                  | **ac_id** **ae_id** [chiefpotter.id, cooperationpotter.id, independentpotter.id - partnerpotter.id, dependentpotter.id, cooperationandchiefpotter.id] | ---                       |
| ------------------------- | -------------------------                                                                                                                             | ------------------------- |
| ct_cpchp_dp               | **cpchp_id** [cooperationandchiefpotter.id] **dp_id** [dependentpotter.id]                                                                            | ---                       |
| ------------------------- | -------------------------                                                                                                                             | ------------------------- |
| ct_cpchp_pp               | **cpchp_id** [cooperationandchiefpotter.id]                                                                                                           | ---                       |
|                           | **pp_id** [partnerpotter.id]                                                                                                                          | ---                       |
| ------------------------- | -------------------------                                                                                                                             | ------------------------- |
| ct_ae_pc                  | **ae_id** [ct_ac_ae.fk2]                                                                                                                              | ---                       |
|                           | **pc_id** [ct_ac_ae.productioncentre]                                                                                                                 | ---                       |
|                           | **weight** [ct_ae_pc_2.weight]                                                                                                                        | ---                       |
| ------------------------- | -------------------------                                                                                                                             | ------------------------- |
| ct_chp_dp                 | **chp_id** [chiefpotter.id]                                                                                                                           |                           |
|                           | **dp_id** [dependentpotter.id]                                                                                                                        | ---                       |
| ------------------------- | -------------------------                                                                                                                             | ------------------------- |
| ct_cp_pp                  | **cp_id** [cooperationpotter.id]                                                                                                                      | ---                       |
|                           | **pp_id** [partnerpotter.id]                                                                                                                          | ---                       |
| ------------------------- | -------------------------                                                                                                                             | ------------------------- |
| ct_ic_ds                  | **ic_id** [informationcarrier.id]                                                                                                                     | ---                       |
|                           | **ds_id** [discoverysite.id]                                                                                                                          | ---                       |
| ------------------------- | -------------------------                                                                                                                             | ------------------------- |
| ct_ic_in                  | **ic_id** [informationcarrier.id]                                                                                                                     | ---                       |
|                           | **pottername** [informationcarrier.pottername]                                                                                                        | ---                       |
|                           | **die** [informationcarrier.die]                                                                                                                      | ---                       |
| ------------------------- | -------------------------                                                                                                                             | ------------------------- |
| ct_ic_pc                  | **ic_id** [ct_ic_pc_2.id]                                                                                                                             | ---                       |
|                           | **pc_id** [productioncentre.id]                                                                                                                       | ---                       |
|                           | **weight** [ct_ic_pc_2.weight]                                                                                                                        | ---                       |
| ------------------------- | -------------------------                                                                                                                             | ------------------------- |
| ct_ic_pf                  | **ic_id** [ct_ic_pf_2.id]                                                                                                                             | ---                       |
|                           | **weight** [ct_ic_pf_2.weight]                                                                                                                        | ---                       |
|                           | **pf_id** [potform.id]                                                                                                                                | ---                       |
| ------------------------- | -------------------------                                                                                                                             | ------------------------- |
| ct_ic_plc                 | **plc_id** [placeasaconcept.id]                                                                                                                       | ---                       |
|                           | **ic_id** [informationcarrier.id]                                                                                                                     | ---                       |
| ------------------------- | -------------------------                                                                                                                             | ------------------------- |
| ct_ic_rl                  | **ic_id** [informationcarrier.id]                                                                                                                     | ---                       |
|                           | **rl_id** [repositorylocation.id]                                                                                                                     | ---                       |
| ------------------------- | -------------------------                                                                                                                             | ------------------------- |
| ct_in_ac                  | **in_id** [inscription.id]                                                                                                                            | ---                       |
|                           | **ac_id** [actorsasaconcept.id]                                                                                                                       | ---                       |
| ------------------------- | -------------------------                                                                                                                             | ------------------------- |
| ct_mt_in                  | **in_id** [inscription.id]                                                                                                                            | ---                       |
|                           | **mt_id** [inscriptionmakingtype.id]                                                                                                                  | ---                       |
| ------------------------- | -------------------------                                                                                                                             | ------------------------- |
| ct_pc_kr                  | **kr_id** [kilnregion.id]                                                                                                                             | ---                       |
|                           | **pc_id** [productioncentre.id]                                                                                                                       | ---                       |
| ------------------------- | -------------------------                                                                                                                             | ------------------------- |
| ct_pf_gf                  | **gf_id** [genericpotform.id]                                                                                                                         | ---                       |
|                           | **pf_id** [potform.id]                                                                                                                                | ---                       |
| ------------------------- | -------------------------                                                                                                                             | ------------------------- |
| ct_plc_ds                 | **plc_id** [placeasaconcept.id]                                                                                                                       | ---                       |
|                           | **ds_id** [discoverysite.id]                                                                                                                          | ---                       |
| ------------------------- | -------------------------                                                                                                                             | ------------------------- |
| ct_plc_pc                 | **plc_id** [placeasaconcept.id]                                                                                                                       | ---                       |
|                           | **pc_id** [productioncentre.id]                                                                                                                       | ---                       |
| ------------------------- | -------------------------                                                                                                                             | ------------------------- |
| ct_plc_rl                 | **plc_id** [placeasaconcept.id]                                                                                                                       | ---                       |
|                           | **rl_id** [repositylocation.id]                                                                                                                       | ---                       |

## Unique:

| Name                        | Columns                     | Definition                |     |
| --------------------------- | --------------------------- | ------------------------- | --- |
| actorsasaconcept            | **id**                      | ---                       |     |
|                             | **name**                    | ---                       |     |
| -------------------------   | -------------------------   | ------------------------- |     |
| chiefpotter                 | **id**                      | ---                       | --- |
|                             | **name**                    | ---                       |     |
|                             | **praenomen**               | ---                       |     |
|                             | **cognomen**                | ---                       |     |
|                             | **slave**                   | ---                       |     |
|                             | **gentilicium**             | ---                       |     |
|                             | **partner**                 | ---                       |     |
|                             | **kilnsite**                | ---                       |     |
| -------------------------   | -------------------------   | ------------------------- |     |
| cooperationandchiefpotter   | **id**                      | ---                       |     |
|                             | **name**                    | ---                       |     |
|                             | **praenomen**               | ---                       |     |
|                             | **cognomen**                | ---                       |     |
|                             | **slave**                   | ---                       |     |
|                             | **gentilicium**             | ---                       |     |
|                             | **partner**                 | ---                       |     |
|                             | **kilnsite**                | ---                       |     |
| -------------------------   | -------------------------   | ------------------------- |     |
| cooperationpotter           | **id**                      | ---                       |     |
|                             | **pottername**              | ---                       |     |
|                             | **praenomen**               | ---                       |     |
|                             | **cognomen**                | ---                       |     |
|                             | **slave**                   | ---                       |     |
|                             | **gentilicium**             | ---                       |     |
|                             | **partner**                 | ---                       |     |
|                             | **kilnsite**                | ---                       |     |
| -------------------------   | -------------------------   | ------------------------- |     |
| dependentpotter             | **id**                      | ---                       |     |
|                             | **slave**                   | ---                       |     |
| -------------------------   | -------------------------   | ------------------------- |     |
| discoverysite               | **id**                      | ---                       |     |
|                             | **label**                   | ---                       |     |
|                             | **long**                    | ---                       |     |
|                             | **pleiades_id**             | ---                       |     |
|                             | **ancientname**             | ---                       |     |
|                             | **wkt**                     | ---                       |     |
| -------------------------   | -------------------------   | ------------------------- |     |
| genericpotform              | **id**                      | ---                       |     |
|                             | **label**                   | ---                       |     |
| -------------------------   | -------------------------   | ------------------------- |     |
| independentpotter           | **id**                      | ---                       |     |
|                             | **pottername**              | ---                       |     |
|                             | **praenomen**               | ---                       |     |
|                             | **cognomen**                | ---                       |     |
|                             | **slave**                   | ---                       |     |
|                             | **gentilicium**             | ---                       |     |
|                             | **partner**                 | ---                       |     |
|                             | **kilnsite**                | ---                       |     |
| -------------------------   | -------------------------   | ------------------------- |     |
| informationcarrier          | **id**                      | ---                       |     |
|                             | **label**                   | ---                       |     |
|                             | **shapes**                  | ---                       |     |
|                             | **number**                  | ---                       |     |
|                             | **kilnsite**                | ---                       |     |
|                             | **pottername**              | ---                       |     |
|                             | **die**                     | ---                       |     |
|                             | **site**                    | ---                       |     |
|                             | **repositorysite**          | ---                       |     |
| -------------------------   | -------------------------   | ------------------------- |     |
| inscriptiondie              | **id**                      | ---                       |     |
|                             | **reading**                 | ---                       |     |
|                             | **simplereading**           | ---                       |     |
|                             | **direction**               | ---                       |     |
| -------------------------   | -------------------------   | ------------------------- |     |
| inscriptiongraffito         | **id**                      | ---                       |     |
|                             | **reading**                 | ---                       |     |
|                             | **simplereading**           | ---                       |     |
|                             | **direction**               | ---                       |     |
| -------------------------   | -------------------------   | ------------------------- |     |
| inscriptionmakingtypedie    | **id**                      | ---                       |     |
|                             | **label**                   | ---                       |     |
|                             | **pottername**              | ---                       |     |
|                             | **die**                     | ---                       |     |
| -------------------------   | -------------------------   | ------------------------- |     |
| inscriptionmakingtypestylus | **id**                      | ---                       |     |
|                             | **label**                   | ---                       |     |
|                             | **pottername**              | ---                       |     |
|                             | **die**                     | ---                       |     |
| -------------------------   | -------------------------   | ------------------------- |     |
| kilnregion                  | **id**                      | ---                       |     |
|                             | **label**                   | ---                       |     |
|                             | **kilnregion_centroid_wkt** | ---                       |     |
|                             | **kilnregion_wkt**          | ---                       |     |
| -------------------------   | -------------------------   | ------------------------- |     |
| partnerpotter               | **id**                      | ---                       |     |
|                             | **name**                    | ---                       |     |
| -------------------------   | -------------------------   | ------------------------- |     |
| placeasaconcept             | **id**                      | ---                       |     |
|                             | **label**                   | ---                       |     |
| -------------------------   | -------------------------   | ------------------------- |     |
| potformgaulish              | **id**                      | ---                       |     |
|                             | **label**                   | ---                       |     |
|                             | **image**                   | ---                       |     |
|                             | **genericform**             | ---                       |     |
|                             | **tradition**               | ---                       |     |
| -------------------------   | -------------------------   | ------------------------- |     |
| potformitalian              | **id**                      | ---                       |     |
|                             | **label**                   | ---                       |     |
|                             | **image**                   | ---                       |     |
|                             | **genericform**             | ---                       |     |
|                             | **tradition**               | ---                       |     |
| -------------------------   | -------------------------   | ------------------------- |     |
| productioncentre            | **id**                      | ---                       |     |
|                             | **label**                   | ---                       |     |
|                             | **kilnregion**              | ---                       |     |
|                             | **lat**                     | ---                       |     |
|                             | **long**                    | ---                       |     |
|                             | **wkt**                     | ---                       |     |
| -------------------------   | -------------------------   | ------------------------- |     |
| repositorylocation          | **id**                      | ---                       |     |
|                             | **label**                   | ---                       |     |

# Samian Workflow

![Samian_Workflow](/assets/Samian_Workflow.png)

# Credits

-   Florian Thiery M.Sc. (Römisch-Germanisches Zentralmuseum Leibniz-Forschungsinstitut für Archäologie)
-   Dr. Allard Mees FSA (Römisch-Germanisches Zentralmuseum Leibniz-Forschungsinstitut für Archäologie)
-   Dennis Gottwald B.A. (JGU Mainz)
