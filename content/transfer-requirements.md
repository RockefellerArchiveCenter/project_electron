---
layout: page
title:  Requirements for the Transfer of Digital Records
permalink: /transfer-requirements/
hide: true
---

Version 1.3 (2019-06-20)

## Table of Contents
*   [Structure](#structure)
*   [Metadata](#metadata)
*   [Protocol](#protocol)
*   [Size](#size)

## Transfers should...

*   Be semantically meaningful.
*   Contain the necessary contextual information to be archivally managed and preserved.
*   Be structured consistently so as to allow for automated validation.

## Structure

Transfers should be structured according to the [Rockefeller Archive Center BagIt Specification](/rac-bagit-spec/).

This document extends the [BagIt specification](https://tools.ietf.org/html/draft-kunze-bagit-14), a hierarchical file packaging format for storage and transfer of arbitrary digital content suitable for disk-based or network-based storage and transfer, developed by the Library of Congress. Libraries for this specification are available in many languages including [Java](https://github.com/LibraryOfCongress/bagit-java), [Python](https://github.com/LibraryOfCongress/bagit-python), [PHP](https://github.com/scholarslab/BagItPHP) and [Ruby](https://github.com/tipr/bagit).

A [BagIt Profile](https://github.com/ruebot/bagit-profiles) will be used to validate transfers.

## Metadata

A minimal set of data elements describing the group of records contained in the transfer must be included as key-value pairs in `bag-info.txt`. These are the minimum elements necessary to support archival management of records in any medium or format, as specified by [Describing Archives: A Content Standard](https://saa-ts-dacs.github.io/). The RAC will index this metadata as structured data. For more details, please see the [Bag-Info Field Specification](/rac-bagit-spec/#bag-info-field-specifications) section in the Rockefeller Archive Center BagIt Specification.

If desired, additional data elements may be supplied by the donor organization. This metadata should be serialized as a single [JSON](https://www.json.org/) or [JSON-LD](https://json-ld.org/) file named `metadata.json`, should use UTF-8 character encoding, and should be included in the `data/` directory of the bag. The RAC will preserve this file as a bitstream alongside the records that it pertains to, but it may not be indexed as structured data.

## Protocol

Transfer packages should be pushed to RAC temporary storage via SFTP. If required by large file sizes or volume, file chunking may be implemented. Transfers will take place through a firewall with only non-standard ports open, and IP address whitelisting may be used.

## Size

A single bag should not exceed 2 gigabytes in size. If a bag exceeds this size limit and contains multiple files, the preferred approach is to divide it into multiple bags which do not exceed the size limit, linking these bags together by using `Bag-Group-Identifier` and `Bag-Count` fields. These smaller bags can then be transferred via regular processes.

Bags which exceed the size limit and cannot be subdivided are are considered edge cases. The RAC should be consulted before any attempt is made to deliver these bags so that the appropriate method of transfer can be determined. These bags must be checked for viruses prior to transfer, and a system-generated log of that activity - including the application, version and last updated date of virus definitions - must accompany each bag.
