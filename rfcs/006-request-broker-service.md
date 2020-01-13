# RFC 006 - Request Broker Service

Last updated January 13, 2020

## Background/Problem Statement

The RAC provides a discovery environment for users to search for archival records of interest. After finding relevant records, they often need to do something with the results of their search:
- Submit a request to view these records in the reading room
- Request copies of the records
- Download, print or email some data about these records

Although users can do many of these things in our current version of DIMES, the code which supports these functions is embedded throughout the application code of XTF, which makes it difficult to maintain or improve this functionality without impacting core application logic, such as indexing and search.

As we are about to move to a new generation of DIMES, we have an opportunity to rethink this integration pattern.

## Proposed Solution

We propose the development of a request broker service, which would encapsulates the logic required to process requests submitted by users.

### Endpoints and actions
The service will provide the following three endpoints, each of which would provide its own logic:
- `reading-room-request` - submits request(s) to the RAC's request management system (Aeon)
- `duplication-request` - submits request(s) to the RAC's digitization process management system (Aeon)
- `download` - returns a streaming comma-separated values (CSV) file
- `email` - sends an email with request data to an email address or list of addresses

For example, a request sent from DIMES to 'reading-room-request' endpoint would result in the following steps:
<!-- - Check if the user attempting to submit the requests is authenticated in Aeon (TBD if this is technically possible) -->
- Fetch data from ArchivesSpace for each request in the list (TODO: define which fields need to be pulled, particularly with regard to restriction data)
- Format the data for each request (for example adding grouping identifiers) and structuring it in the way Aeon expects (Question: should we merge requests for the same container here, so that users have a preview of what the request will look like in Aeon?)
- Deliver the final request data to Aeon via a POST request

### Authentication
The service will accept only requests from known sources, identified by an API key.

### Request Data Model

At minimum, requests specify a list of items.

```
{ "items":
  [
    "/repositories/2/archival_objects/1263",
    "/repositories/2/archival_objects/1264"
  ]
}
```

Additional data elements may be provided as needed.

```
{ "to_emails": ["test@example.org"]
  "items":
  [
    "/repositories/2/archival_objects/1265",
    "/repositories/2/archival_objects/1266"
  ]
}
```

### Important Caveats
Since it is envisioned largely as a passthrough, this request broker service would have a minimal UI. Users will not be able to create requests directly in the application, but they may be able to see requests submitted and/or a list of errors. Additionally, the service should store only the bare minimum of data necessary so we can avoid saving personally identifying information or information duplicated in other systems.
