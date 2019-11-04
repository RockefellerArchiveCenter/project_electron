# RFC 005 - Arrangement Maps

Last updated November 4, 2019

## Background/Problem Statement
For a number of reasons, we need to create arrangement structures which extend the structures available to us in ArchivesSpace:
- Incoming records are largely accruals to existing collections or fonds (defined here as a single source of provenance), rather  than new provenance-based collections. As a result, our processing methodology has increasingly been to process by accession rather than collection, since the extent and structure of our collections is in constant flux. This results in a large number of resource records created in ArchivesSpace for each single source of provenance, which then need to be related to one another in meaningful relationships.
- Groups of records (such as format-based series) may meaningfully exist in multiple collections at once, so  we need a way to  articulate these relationships outside of the provenance-based arrangements in ArchivesSpace.

## Proposed Solution
A data structure, referred to as an Arrangement Map, will allow us to create and manage these relationships over time. The data structure will consist of nodes which point to an ArchivesSpace resource or archival object record, in a tree structure.

```
{
    "id": 1,
    "ref": "/api/components/1/",
    "title": "Asian Cultural Council records",
    "children": [
        {
            "id": 1,
            "title": "Asian Cultural Council records, Administrative Files, RG 1",
            "ref": "/api/components/1/",
            "parent": null,
            "archivesspace_uri": "/repositories/2/resources/626",
            "tree_index": 0
        },
        {
            "id": 2,
            "title": "Asian Cultural Council records, Conferences, Festivals and Seminars, RG 2",
            "ref": "/api/components/2/",
            "parent": null,
            "archivesspace_uri": "/repositories/2/resources/12464",
            "tree_index": 1
        },
        {
            "id": 3,
            "title": "Asian Cultural Council records, Indo-US Subcommission on Education and Culture, RG 3",
            "ref": "/api/components/3/",
            "parent": null,
            "archivesspace_uri": "/repositories/2/resources/12466",
            "tree_index": 2
        },
        {
            "id": 4,
            "title": "Asian Cultural Council records, Fellowships and Training Programs, RG 4",
            "ref": "/api/components/4/",
            "parent": null,
            "archivesspace_uri": "/repositories/2/resources/12475",
            "tree_index": 3
        },
        {
            "id": 5,
            "title": "Asian Cultural Council records, Grants, RG 5",
            "ref": "/api/components/5/",
            "parent": null,
            "archivesspace_uri": "/repositories/2/resources/12535",
            "tree_index": 4
        },
        {
            "id": 6,
            "title": "Asian Cultural Council records, Hong Kong Arts Program, Record Group 6",
            "ref": "/api/components/6/",
            "parent": null,
            "archivesspace_uri": "/repositories/2/resources/12628",
            "tree_index": 5
        }
    ],
    "publish": false,
    "created": "2019-11-04T16:16:08.934112-05:00",
    "modified": "2019-11-04T16:19:27.215211-05:00"
}
```

These data structures will be created and managed in a custom application called [Cartographer](https://github.com/RockefellerArchiveCenter/cartographer), which will be accessible both via a GUI as well as a REST API.

Descriptive data for each of the nodes in an arrangement tree will be created and managed in ArchivesSpace. Cartographer will only store references and possibly some minimal data (such as a title) about that node.
