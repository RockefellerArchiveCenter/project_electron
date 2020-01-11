# RFC 006 - DIMES-Aeon Integration

Last updated January 10, 2020

## Background/Problem Statement
In order for users to view archival records, either in the reading room or via remote delivery services, they need to submit requests to Aeon (our request management system) from DIMES (our discovery environment). The logic which integrates these two systems is currently embedded in XTF code in a number of places, which makes it difficult to maintain or improve without impacting other areas of the application. As we are about to move to a new generation of DIMES, we have an opportunity to rethink this integration pattern.

## Proposed Solution

We propose the development of a request broker application, which would encapsulates the logic required to integrate between DIMES and Aeon. This layer would accept lists of requests from DIMES, and perform a variety of steps before delivering that list to Aeon:
- Check if the user attempting to submit the requests is authenticated in Aeon (TBD if this is technically possible)
- Check if any of the requests are duplicates (TODO: define what is and is not a duplicate, TBD if this is technically possible)
- Fetch data from ArchivesSpace for each request in the list (TODO: define which fields need to be pulled, particularly with regard to restriction data)
- Format the data for each request (for example adding grouping identifiers) and structuring it in the way Aeon expects (Question: should we merge requests for the same container here, so that users have a preview of what the request will look like in Aeon?)
- Deliver the final request data to Aeon via a POST request

The request broker would have a minimal UI. Users will not be able to create requests directly in the application, but they may be able to see requests submitted and/or a list of errors.

Additionally, the broker should store only the bare minimum of data necessary so we can avoid saving personally identifying information or information duplicated in other systems.

### Request Data Model

#### Initial request data submitted from DIMES
Requests from DIMES are submitted to the request broker as a list of ArchivesSpace URIs.

```
{"items":
  [
    "/repositories/2/archival_objects/1263",
    "/repositories/2/archival_objects/1264"
  ]
}
```

#### Data retrieved from ArchivesSpace

The following fields are retrieved from ArchivesSpace for each request item:
- Title
- Date
- Creator
- Parent Series (or subseries)
- Container information
- Collection Title
- Collection Identifier
- Location
- Restrictions

(TODO: evaluate whether or not all of these fields are necessary in Aeon)

#### Requests data delivered to Aeon

The data retrieved from ArchivesSpace is delivered to Aeon as `multipart/form-data`.


### DIMES UI
The DIMES UI would need to provide the following functionality, at minimum:
- The ability to submit requests
- The ability to submit credentials
- The ability to confirm submission of requests marked as duplicate

Additional functionality, such as the ability to see a list of previously submitted requests, etc, may be desirable.
