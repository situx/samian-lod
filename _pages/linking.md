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

{% include figure image_path="/assets/images/pleiades_example.png" %}

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

Place data (discovery sites, kiln regions and production centres) are integrated into `Wikidata` using OpenRefine and Quick Statements. The mapping schemes in Open Refine can be seen at [ds_schema.json](<>), [kr_schema.json](<>) and [pc_schema.json](<>).
