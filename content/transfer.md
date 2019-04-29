---
layout: page
title: Transfer
permalink: /transfer/
---

## Transfer Specification
We have developed a specification for transferring digital records and their metadata over a network connection. We used existing standards and frameworks such as BagIt, BagIt Profiles, Activity Streams, and OAIS.

There are three basic pieces that comprise the transfer specification:

### [Transfer Requirements](/transfer-requirements/)
 A document which outlines the major requirements for transfers of digital records, including required metadata, structure, notifications, transfer protocol and size.

### [RAC BagIt Specification](/rac-bagit-spec/)
Requirements for the structure of transfers of digital records, which are based on the BagIt specification. We also included a [BagIt Profile](https://gist.github.com/HaSistrunk/65d59e558c436b9d934d98fd8fb0f575) which encodes these requirements in a machine-readable format to ensure and facilitate compliance.

### [Example Python scripts](/scripts/)
Scripts to generate and validate sample bags. These allow users to point to whatever files they want to include in a sample bag’s payload directory.
