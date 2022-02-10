---
permalink: /linking/
title: "External Linking"
header:
  image: /assets/images/header.jpg
  caption: "Photo credit: Carole Raddato from FRANKFURT, Germany, CC BY-SA 2.0, via [**Wikimedia Commons**](https://commons.wikimedia.org/wiki/File:Terra_sigillata,_Gallo-Roman_Museum_of_Tongeren,_Belgium_(27032316984).jpg)"
sidebar:
  nav: "barLinking"
---

## Pleiades

Discovery Sites are linked to `Pleiades` using the Open Annotation data model according to the [Pelagios Cookbook](<according to https://github.com/pelagios/pelagios-cookbook/wiki/Joining-Pelagios#minimum-example>).

{% include figure image_path="/assets/images/pleiades_example.png" description="example of a Pleiades annotation" %}

**Example Query - InformationCarrier**

_-> 3 Random Pleiades Annotations_

<pre>
  <code>
PREFIX oa: <http://www.w3.org/ns/oa#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?body ?target ?targetLabel WHERE {
?node oa:hasBody ?body.
?node oa:hasTarget ?target.
?target rdfs:label ?targetLabel.
} LIMIT 3
  </code>
</pre>

_Output:_

| **body**        | **target**            | **targetLabel** |
| --------------- | --------------------- | --------------- |
| pleiades:109338 | samian:loc_ds_1002582 | "Sinzig"@en     |
| pleiades:109468 | samian:loc_ds_1003961 | "Haute-Yutz"@en |
| pleiades:118986 | samian:loc_ds_1002381 | "Burghöfe"@en   |

## Wikidata

Place data (discovery sites, kiln regions and production centres) are integrated into `Wikidata` using `OpenRefine` and `Quick Statements`. The mapping schemes in Open Refine can be seen at [ds_schema.json](https://github.com/RGZM/samian-lod/blob/main/wikidata/ds_schema.json), [kr_schema.json](https://github.com/RGZM/samian-lod/blob/main/wikidata/kr_schema.json) and [pc_schema.json](https://github.com/RGZM/samian-lod/blob/main/wikidata/pc_schema.json).

For each category we created a specific identifier in Wikidata [Samian Ware Discovery Site](https://www.wikidata.org/wiki/Q102202066), [Samian Ware Productioncentre](https://www.wikidata.org/wiki/Q102202026) and [Samian Ware Kilnregion](https://www.wikidata.org/wiki/Q102201947). All entries are instances (P31) of a category and part of (P361) [Samian Research](https://www.wikidata.org/wiki/Q90412636). In Wikidata we used the exact match (P2888) property to link to the Linked Open Samian Ware resource. In the Samian LOD dataset we used our `lado:exactMatch` property to create a bidirectional link.

_-> 3 Random Wikidata matches_

<pre>
  <code>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX lado: <http://archaeology.link/ontology#>

SELECT DISTINCT ?node ?nodeLabel ?wikidata WHERE {
?node lado:exactMatch ?wikidata.
?node rdfs:label ?nodeLabel.
} LIMIT 3
  </code>
</pre>

_Output:_

| **node**              | **nodeLabel**         | **wikidata**        |
| --------------------- | --------------------- | ------------------- |
| samian:loc_ds_1000003 | "Baumes-de-Venise"@en | wikidata:Q103145968 |
| samian:loc_ds_1000004 | "Brigstock"@en        | wikidata:Q103155047 |
| samian:loc_ds_1000005 | "Highworth"@en        | wikidata:Q103163787 |

Via the Wikidata SPARQL Query interface we may query our matching resources:

-   discovery sites: <https://w.wiki/owf>
-   production centres: <https://w.wiki/owe>
-   kiln regions (centroid): <https://w.wiki/owZ>
-   kiln regions (geoshape): <https://w.wiki/4pDk> [embedded HTML](https://w.wiki/4pDu)
-   all geospatial matches: <https://w.wiki/qxX>

{% include figure image_path="/assets/images/wikidata_matches.png" description="map of geospatial data which matches between Linked Open Samian Ware and Wikidata" %}

Map of geospatial data which matches between Linked Open Samian Ware and Wikidata.

{% include figure image_path="/assets/images/wikidata_kilnregions.png" description="map of Wikidata kilnregions as geoshape" %}

Map of Wikidata kilnregions as geoshape.
