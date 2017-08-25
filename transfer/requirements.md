# Requirements for Transfer of Digital Records

Version 1.0.0 (2017-06-20)

## Table of Contents
*   [Structure](#structure)
*   [Metadata](#metadata)
*   [Notifications](#notifications)
    *   Success Messages
    *   Error Messages
*   [Protocol](#protocol)
*   [Size](#size)

## Transfers should...

*   be semantically meaningful
*   contain the necessary contextual information to be archivally managed and preserved
*   be structured consistently so as to allow for automated validation

## Structure

Transfers should be structured according to the [Rockefeller Archive Center BagIt Specification](bagit-specification.md).

This document extends the [BagIt specification](https://tools.ietf.org/html/draft-kunze-bagit-14), a hierarchical file packaging format for storage and transfer of arbitrary digital content suitable for disk-based or network-based storage and transfer, developed by the Library of Congress. Libraries for this specification are available in many languages including [Java](https://github.com/LibraryOfCongress/bagit-java), [Python](https://github.com/LibraryOfCongress/bagit-python), [PHP](https://github.com/scholarslab/BatItPHP) and [Ruby](https://github.com/topr/bagit).

A [BagIt Profile](https://github.com/ruebot/bagit-profiles) will be used to validate transfers. A [bag profile for organizational records](organizational-bag-profile.json) as well as [example scripts](example-scripts/) to create and validate bags are available in this repository.

## Metadata

A minimal set of data elements describing the group of records contained in the transfer must be included as key-value pairs in `bag-info.txt`. These are the minimum elements necessary to support archival management of records in any medium or format, as specified by [Describing Archives: A Content Standard](http://www2.archivists.org/standards/DACS). The RAC will index this metadata as structured data. For more details, please see the **Bag-Info Field Specification** section in the [Rockefeller Archive Center BagIt Specification](bagit-specification.md).

If desired, additional data elements may be supplied by the donor organization. This metadata should be serialized as a single [JSON](http://www.json.org/) or [JSON-LD](http://json-ld.org/) file named `metadata.json`, should use UTF-8 character encoding, and should be included in the `data/` directory of the bag. The RAC will preserve this file as a bitstream alongside the records that it pertains to, but it may not be indexed as structured data.

## Notifications

During the process of transferring digital records to the custody of the Rockefeller Archive Center, messages will be generated to allow humans and machines to understand the status of transfers, trigger processes, and take appropriate actions to correct any errors. Transfer notification messages indicate either success or error, and are provided in formats suitable for both machine and human consumption. Machine-actionable notifications comply with the [W3's Activity Streams 2.0 specification](https://www.w3.org/TR/activitystreams-core/). The below examples are illustrative of how the RAC may use the Activity Streams and should not be regarded as strictly prescriptive.

### Success Messages

#### For Machines

Machine-readable notifications indicating success will have a `type` value of `Accept`. The `summary` value provides information about the process that was successfully completed. The `object` value provides a reference to the object the action was taken on. The optional `result` value provides additional information about the actions that have been taken as a result of the successful process. The value of `endTime` is a timestamp of the time the process completed successfully.

```
{
  "type": "Accept",
  "summary": "Bag successfully checked for viruses",
  "object": "Bag_001",
  "result": {
    "name": "Staged for appraisal"
  }
  "endTime": 2017-04-21T20:01:07+00:00
}
```

#### For People

Success notifications for humans will contain the following information:
*   A description of the process(es) successfully completed
*   The time at which the process(es) completed
*   What process(es) will happen next
*   What actions, if any, need to be taken by a person

It may be desirable to bundle these notifications in a daily digest, rather than sending individual messages as they occur. It may also be desirable to send a single success message if a transfer successfully completes a set of automated processes (for example post-transfer virus check and bag validation) rather than a message for each process successfully completed.

### Error Messages

#### For Machines

Notifications indicating an error has occurred will have a `type` value of `Reject`. The `summary` provides information about the specific error and specific information about reason for the error. The `object` value provides a reference to the object the action was taken on. The optional `result` value indicates system actions that have been taken as a result of the error and `endTime` is a timestamp of the time the error occurred.

```
{
  "type": "Reject",
  "summary": "Bag validation failure. Metadata elements are missing",
  "object": "Bag_001",
  "result": {
    "name": "Staged for deletion"
  }
  "endTime": 2017-04-21T20:01:07+00:00
}
```

#### For People

Error notifications for people will contain the following information:
*   A description of the process(es) during which the error occurred
*   The time at which the error occurred
*   A complete error log
*   What process(es) will happen next
*   What actions, if any, need to be taken

Error notifications should be sent as soon as they occur.

## Protocol

Transfer packages should be pushed to RAC temporary storage via SFTP. If required by large file sizes or volume, file chunking may be implemented. Transfers will take place through a firewall with only non-standard ports open, and IP address whitelisting will be used.

## Size

A single bag should not exceed 2 gigabytes in size. Bags exceeding this size can be handled in three ways.

1.  For transfers containing multiple files, multiple bags can be created and linked by using `Bag-Group-Identifier` and `Bag-Count` fields.
2.  For transfers more than 2 gigabytes but less than 500 gigabytes in size which cannot be divided into sets of files as above, a single bag can be created and transferred via SFTP. Files in these transfers must be checked for viruses before they are sent to the RAC.
3.  For transfers exceeding 500 gigabytes in size which cannot be divided into sets of files as above, a single bag should be created and transferred via secured hard drives.
