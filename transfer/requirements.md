# Preliminary Requirements for Transfer of Digital Records
Rockefeller Archive Center/Project Electron/March 2017

Transfers should:

*   be semantically meaningful
*   contain the necessary contextual information to be archivally managed and preserved
*   be structured consistently so as to allow for automated validation

## Metadata

The data elements outlined below are the minimum elements necessary to support archival management of records in any medium or format, as specified by [Describing Archives: A Content Standard](http://www2.archivists.org/standards/DACS). These metadata elements should be applied at an aggregate level. If desired, additional data elements may be supplied by the donor organization.

This metadata should be serialized as a single JSON or JSON-LD file in each transfer.

See [Metadata Template](examples/metadata.md) for further details.

## Transfer Structure

Transfers should be structured according to [BagIt specification](https://tools.ietf.org/html/draft-kunze-bagit-14), a hierarchical file packaging format for storage and transfer of arbitrary digital content suitable for disk-based or network-based storage and transfer, developed by the Library of Congress. Libraries for this specification are available in many languages including Java, Python, PHP and Ruby.

We prefer transfers that are both semantically meaningful and smaller in size. In cases where large transfers need to bro separated into multiple bags, the `bagCount` and `groupIdentifier` fields will be used to create relationships between bags.

[BagIt Profiles](https://github.com/ruebot/bagit-profiles) may be used to extend the BagIt specification and make use of [existing validation tools](https://github.com/ruebot/bagit-profiles-validator).

## Transfer Protocol

Transfer packages should be pushed to RAC temporary storage via SFTP. If required by large file sizes or volume, file chunking may be implemented. Transfers will take place through a firewall with only non-standard ports open, and IP address whitelisting will be used.

## Transfer Size

A single bag should not exceed 500 gigabytes in size. Bags exceeding this size can be handled in two ways.

1.  For transfers containing multiple files, multiple bags can be created and linked by using `Bag-Group-Identifier` and `Bag-Count` fields.
2.  For transfers which cannot be divided into sets of files as above, a single bag should be created and transferred via secured hard drives.
