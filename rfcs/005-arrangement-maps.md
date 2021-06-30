# RFC 005 - Arrangement Maps

Last updated June 30, 2021

## Background/Problem Statement
In order to represent the entirety of provenance-based collections, we need to create arrangement structures for archival records which extend the explicit structures created by archivists in ArchivesSpace. Incoming records are largely accruals to existing collections or fonds (defined here as a single source of provenance), rather than new provenance-based collections. As a result, we have increasingly processed by accession rather than collection. This has a few implications:
  - The extent and structure of our collections is in constant flux.
  - There are a large number of resource records created in ArchivesSpace for each single source of provenance.

## Proposed Solution

### Data Structure
A machine-actionable data structure, referred to as an Arrangement Map, will allow us to create and manage these relationships over time. The data structure will consist of nodes which point to an ArchivesSpace resource record, in a tree structure.

```
{
    "id": 13,
    "ref": "/api/maps/13/",
    "title": "Asian Cultural Council records",
    "children": [
        {
            "id": 54,
            "title": "Asian Cultural Council records",
            "ref": "/api/components/54/",
            "level": "collection",
            "parent": null,
            "archivesspace_uri": "/repositories/2/resources/12995",
            "order": 0,
            "children": [
                {
                    "id": 55,
                    "title": "Asian Cultural Council records, Administrative Files, RG 1",
                    "ref": "/api/components/55/",
                    "level": "recordgrp",
                    "parent": 54,
                    "archivesspace_uri": "/repositories/2/resources/626",
                    "order": 1
                },
                {
                    "id": 56,
                    "title": "Asian Cultural Council records, Conferences, Festivals and Seminars, RG 2",
                    "ref": "/api/components/56/",
                    "level": "recordgrp",
                    "parent": 54,
                    "archivesspace_uri": "/repositories/2/resources/12464",
                    "order": 2
                },
                {
                    "id": 57,
                    "title": "Asian Cultural Council records, Indo-US Subcommission on Education and Culture, RG 3",
                    "ref": "/api/components/57/",
                    "level": "recordgrp",
                    "parent": 54,
                    "archivesspace_uri": "/repositories/2/resources/12466",
                    "order": 3
                },
                {
                    "id": 58,
                    "title": "Asian Cultural Council records, Fellowships and Training Programs, RG 4",
                    "ref": "/api/components/58/",
                    "level": "recordgrp",
                    "parent": 54,
                    "archivesspace_uri": "/repositories/2/resources/12475",
                    "order": 4
                },
                {
                    "id": 59,
                    "title": "Asian Cultural Council records, Grants, RG 5",
                    "ref": "/api/components/59/",
                    "level": "recordgrp",
                    "parent": 54,
                    "archivesspace_uri": "/repositories/2/resources/12535",
                    "order": 5
                },
                {
                    "id": 60,
                    "title": "Asian Cultural Council records, Hong Kong Arts Program, Record Group 6",
                    "ref": "/api/components/60/",
                    "level": "recordgrp",
                    "parent": 54,
                    "archivesspace_uri": "/repositories/2/resources/12628",
                    "order": 6
                }
            ]
        }
    ],
    "publish": true,
    "created": "2020-07-24T10:08:34.093785-04:00",
    "modified": "2020-07-24T10:11:46.450617-04:00"
}
```

Each component of the Arrangement Map will also have a detail view:
```
{
    "id": 879,
    "ref": "/api/components/879/",
    "title": "Ford Foundation records, Central Index",
    "map": 37,
    "parent": 878,
    "order": 1,
    "level": "collection",
    "archivesspace_uri": "/repositories/2/resources/13103",
    "publish": true,
    "ancestors": [
        {
            "title": "Ford Foundation records",
            "ref": "/api/components/878/",
            "archivesspace_uri": "/repositories/2/resources/12990",
            "level": "collection",
            "order": 0
        }
    ],
    "children": [
        {
            "title": "Ford Foundation records, Grants",
            "ref": "/api/components/880/",
            "archivesspace_uri": "/repositories/2/resources/918",
            "level": "collection",
            "order": 2
        },
        {
            "title": "Ford Foundation records, General Correspondence",
            "ref": "/api/components/893/",
            "archivesspace_uri": "/repositories/2/resources/921",
            "level": "collection",
            "order": 15
        },
        {
            "title": "Ford Foundation records, Projects",
            "ref": "/api/components/894/",
            "archivesspace_uri": "/repositories/2/resources/919",
            "level": "collection",
            "order": 16
        },
        {
            "title": "Ford Foundation records, Project and Event Photographs, Accession 2018:033",
            "ref": "/api/components/895/",
            "archivesspace_uri": "/repositories/2/resources/12637",
            "level": "collection",
            "order": 17
        },
        {
            "title": "Ford Foundation records, Log Files (Grant and Project Proposals)",
            "ref": "/api/components/896/",
            "archivesspace_uri": "/repositories/2/resources/11361",
            "level": "collection",
            "order": 18
        },
        {
            "title": "Ford Foundation records, Action Control Slips",
            "ref": "/api/components/897/",
            "archivesspace_uri": "/repositories/2/resources/11341",
            "level": "collection",
            "order": 19
        },
        {
            "title": "Ford Foundation records, Central Index",
            "ref": "/api/components/898/",
            "archivesspace_uri": "/repositories/2/resources/922",
            "level": "collection",
            "order": 20
        }
    ]
}
```

### Technical Implementation

These data structures will be created and managed in a custom application called [Cartographer](https://github.com/RockefellerArchiveCenter/cartographer), which will provide a GUI for archivists to create and manage Arrangement Maps as well as a REST API which produces JSON responses.

Descriptive data for each of the nodes in an Arrangement Map will be created and managed in ArchivesSpace. Cartographer will only store references and some minimal data (such as a title) about that node.

### Find By URI

There should be an endpoint which returns data about an Arrangement Map component which matches a particular ArchivesSpace URI. This will support integration of these data structures into the larger data pipeline which fetches data from ArchivesSpace, transforms it, and indexes it in Elasticsearch.
