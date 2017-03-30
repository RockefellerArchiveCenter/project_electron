# Preliminary Requirements for Transfer of Digital Records
Rockefeller Archive Center/Project Electron/March 2017

## Metadata

The data elements outlined below are the minimum elements necessary to support archival management of records in any medium or format, as specified by [Describing Archives: A Content Standard](http://www2.archivists.org/standards/DACS). These metadata elements should be applied at an aggregate level. If desired, additional data elements may be supplied by the donor organization.

This metadata should be serialized as a single JSON or JSON-LD file in each transfer.

#### Identifier (Record ID assigned by donor or system)
Required, not repeatable

#### Title
Required, not repeatable

#### Date
Required, repeatable

#### Creator
Required, repeatable

#### Language of Materials
Required, repeatable

#### Description (information about the nature of records)
Required, not repeatable

#### Restrictions (information about restrictions on records)
No required, repeatable

## Transfer Structure
Transfers should be structured according to [BagIt specification](https://tools.ietf.org/html/draft-kunze-bagit-14), a hierarchical file packaging format for storage and transfer of arbitrary digital content suitable for disk-based or network-based storage and transfer, developed by the Library of Congress. Libraries for this specification are available in many languages including Java, Python, PHP and Ruby.

## Transfer Protocol
Transfer packages should be pushed to RAC temporary storage via SFTP. If required by large file sizes or volume, file chunking may be implemented. Transfers will take place through a firewall with only non-standard ports open, and IP address whitelisting will be used.
