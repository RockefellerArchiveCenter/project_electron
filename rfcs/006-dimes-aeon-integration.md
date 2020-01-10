# RFC 006 - DIMES-Aeon Integration

Last updated January 10, 2020

## Background/Problem Statement
In order for users to view archival records, either in the reading room or via remote delivery services, they need to submit requests to Aeon (our request management system) from DIMES (our discovery environment). The logic which integrates these two systems is currently embedded in XTF code in a number of places, which makes it difficult to maintain or improve without impacting other areas of the application. As we are about to move to a new generation of DIMES, we have an opportunity to rethink this integration pattern.

## Proposed Solution
A request broker, which encapsulates the logic required to integrate between DIMES and Aeon. This layer would accept lists of requests from DIMES, and perform a variety of steps before passing that list on to Aeon:
- Check if the user attempting to submit the requests is authenticated in Aeon (TBD if this is technically possible)
- Check if any of the requests are duplicates (TODO: define what is and is not a duplicate, TBD if this is technically possible)
- Fetch additional data from ArchivesSpace such as restriction and location information for each request in the list (TODO: define source and scope -- i.e. container or request item -- of restriction data)
- Format the data for each request (for example adding grouping identifiers) and structuring it in the way Aeon expects (Question: should we merge here, so that users have a preview of what the request will look like in Aeon?)
- Deliver the final request data to Aeon via a POST request

The request broker would have a minimal UI. Users will not be able to create requests directly in the request broker, but they may be able to see requests submitted and/or a list of errors.

Additionally, the broker should store only the bare minimum of data necessary so we can avoid saving personally identifying information or information duplicated in other systems.

### DIMES UI
The DIMES UI would need to provide the following functionality, at minimum:
- The ability to submit requests
- The ability to submit credentials
- The ability to confirm submission of requests marked as duplicate

Additional functionality, such as the ability to see a list of previously submitted requests, etc, may be desirable.

### Request Model
Requests from DIMES are submitted to the request broker as a list. The request broker can remove items from this list (if they are duplicates) and can add data to an item, but it cannot add new items to this list. Aeon may further merge items on this list if they represent portions of the same circulating container, for example multiple folders from the same box. (TBD we may want to do this deduplication in the request broker)
