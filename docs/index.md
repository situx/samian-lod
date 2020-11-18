# Samian LOD Documentation

## Prefixes

samian (base):
  http://lod.archaeology.link/data/samian/
crm:
  http://www.cidoc-crm.org/cidoc-crm/
dc:
  http://purl.org/dc/elements/1.1/
dct:
  http://purl.org/dc/terms/
dcmitype:
  http://purl.org/dc/dcmitype/
geosparql:
  http://www.opengis.net/ont/geosparql#>
lado
  http://samian/ontology
owl:
  http://www.w3.org/2002/07/owl#
pleiades:
  https://pleiades.stoa.org/places/vocab#
rdf:
  http://www.w3.org/1999/02/22-rdf-syntax-ns#
rdfs:
  http://www.w3.org/2000/01/rdf-schema#
sf:
  http://www.opengis.net/ont/sf#
skos:
  http://www.w3.org/2004/02/skos/core#
xml:
  http://www.w3.org/XML/1998/namespace
xsd:
  http://www.w3.org/2001/XMLSchema#

## Class Structure

![SamianLod_map](/docs/pictures/Samian_map_png.png){:class="img-responsive"}
![SamianLod_map_InformationCarrier](/docs/pictures/SamianLod_map_InformationCarrier.png){:class="img-responsive"}
![SamianLod_map_Insription](/docs/pictures/SamianLod_map_Insription.png){:class="img-responsive"}
![SamianLod_map_Actor](/docs/pictures/SamianLod_map_Actor.png){:class="img-responsive"}
![SamianLod_map_Location](/docs/pictures/SamianLod_map_Location.png){:class="img-responsive"}
![SamianLod_map_Potform](/docs/pictures/SamianLod_map_Potform.png){:class="img-responsive"}

## File Structure

![Samian_universal_map](/docs/pictures/Samian_universal_map.png){:class="img-responsive"}

## CSV-Documentation

### Crosstables:

ct_ac_ae:    
        (ac_id)
        (ae_id) [chiefpotter.id, cooperationpotter.id, independentpotter.id - partnerpotter.id, dependentpotter.id, cooperationandchiefpotter.id]

ct_cpchp_dp:
        (cpchp_id) [c[ooperationandchiefpotter.id]
        (dp_id) [dependentpotter.id]

ct_cpchp_pp
        (cpchp_id) [cooperationandchiefpotter.id]
        (pp_id) [partnerpotter.id]

ct_ae_pc:
        (ae_id) [ct_ac_ae.fk2]
        (pc_id) [ct_ac_ae.productioncentre]
        (weight) [ct_ae_pc_2.weight]

ct_chp_dp:    
        (chp_id) [chiefpotter.id] |
        (dp_id) [dependentpotter.id]

ct_cp_pp:
        (cp_id) [cooperationpotter.id]
        (pp_id) [partnerpotter.id]

ct_ic_ds:
        (ic_id) [informationcarrier.id]
        (ds_id) [discoverysite.id]

ct_ic_in:   
        (ic_id) [informationcarrier.id]
        (pottername) [informationcarrier.pottername]
        (die) [informationcarrier.die]

ct_ic_pc:
        (ic_id) [ct_ic_pc_2.id]
        (pc_id) [productioncentre.id]
        (weight) [ct_ic_pc_2.weight]

ct_ic_pf:
        (ic_id) [ct_ic_pf_2.id]
        (weight) [ct_ic_pf_2.weight]
        (pf_id) [potform.id]

ct_ic_plc:
        (plc_id) [placeasaconcept.id]
        (ic_id) [informationcarrier.id]

ct_ic_rl:
        (ic_id) [informationcarrier.id]
        (rl_id) [repositorylocation.id]

ct_in_ac:
        (in_id) [inscription.id]
        (ac_id) [actorsasaconcept.id]

ct_mt_in:
        (in_id) [inscription.id]
        (mt_id) [inscriptionmakingtype.id]

ct_pc_kr:
        (kr_id) [kilnregion.id]
        (pc_id) [productioncentre.id]

ct_pf_gf:
        (gf_id) [genericpotform.id]
        (pf_id) [potform.id]

ct_plc_ds:
        (plc_id) [placeasaconcept.id]
        (ds_id) [discoverysite.id]

ct_plc_pc:
        (plc_id) [placeasaconcept.id]
        (pc_id) [productioncentre.id]

ct_plc_rl:
        (plc_id) [placeasaconcept.id]
        (rl_id) [repositylocation.id]




### Unique:

actorsasaconcept:
        (id)
        (name)

chiefpotter:
        (id)
        (name)
        (praenomen)
        (cognomen)
        (slave)
        (gentilicium)
        (partner)
        (kilnsite)

cooperationandchiefpotter:
        (id)
        (name)
        (praenomen)
        (cognomen)
        (slave)
        (gentilicium)
        (partner)
        (kilnsite)

cooperationpotter:
        (id)
        (pottername)
        (praenomen)
        (cognomen)
        (slave)
        (gentilicium)
        (partner)
        (kilnsite)

dependentpotter:
        (id)
        (slave)

discoverysite:
        (id)
        (label)
        (long)
        (pleiades_id)
        (ancientname)
        (wkt)
genericpotform:
        (id)
        (label)

independentpotter:
        (id)
        (pottername)
        (praenomen)
        (cognomen)
        (slave)
        (gentilicium)
        (partner)
        (kilnsite)

informationcarrier:
        (id)
        (label)
        (shapes)
        (number)
        (kilnsite)
        (pottername)
        (die)
        (site)
        (repositorysite)

inscriptiondie:
(id)
        (reading)
        (simplereading)
        (direction)

inscriptiongraffito:
(id)
        (reading)
        (simplereading)
        (direction)

inscriptionmakingtypedie:
(id)
        (label)
        (pottername)
        (die)

inscriptionmakingtypestylus:
(id)
        (label)
        (pottername)
        (die)

kilnregion:
        (id)
        (label)
        (kilnregion_centroid_wkt)
        (kilnregion_wkt)

partnerpotter:
        (id)
        (name)

placeasaconcept:
        (id)
        (label)

potformgaulish:
        (id)
        (label)
        (image)
        (genericform)
        (tradition)

potformitalian:
        (id)
        (label)
        (image)
        (genericform)
        (tradition)

productioncentre:
        (id)
        (label)
        (kilnregion)
        (lat)
        (long)
        (wkt)

repositorylocation:
        (id)
        (label)
