---
layout: page
title: About
permalink: /about/
---

## Project components

### Transfer Specification
A specification for transferring digital records to the RAC over a network connection. This was developed using existing standards and frameworks such as BagIt, BagIt Profiles, Activity Streams, and OAIS.

There are three basic pieces that comprise the transfer specification:

1. [Transfer Requirements](/transfer-requirements/): A document which outlines the major requirements for transfers of digital records, including required metadata, structure, notifications, transfer protocol and size.
2. [RAC BagIt Specification](/rac-bagit-spec/): Requirements for the structure of transfers of digital records, which are based on the BagIt specification. We also included a [BagIt Profile](https://gist.github.com/HaSistrunk/65d59e558c436b9d934d98fd8fb0f575) which encodes these requirements in a machine-readable format to ensure and facilitate compliance.
3. [Example Python scripts](/scripts/) to generate and validate sample bags. These allow users to point to whatever files they want to include in a sample bag’s payload directory.

### Aurora
A Django web application to support and regularize the ongoing secure transfer of digital records
and their metadata to the archives. Check out the [Aurora user documentation](https://docs.rockarch.org/aurora/) and the code in our [Aurora GitHub repository](https://github.com/RockefellerArchiveCenter/aurora).

### zodiac
An API Gateway to manage system interactions. Check out the code and learn more in our [zodiac GitHub repository](https://github.com/RockefellerArchiveCenter/zodiac).

### Microservices
A set of microservice applications which support integrations between current and future systems and assist in the archival
processes of accessioning, preservation, description, and access.

#### ursa major
Discovers and stores bags. Learn more in the [ursa major GitHub repo](https://github.com/RockefellerArchiveCenter/ursa_major).

#### fornax
Creates Archivematica-compliant Submission Information Packages (SIPs). Learn more in the [fornax GitHub repo](https://github.com/RockefellerArchiveCenter/fornax).

#### libra
Generates reports on files and activities in Fedora. Learn more in the [libra GitHub repo](https://github.com/RockefellerArchiveCenter/libra).

#### gemini
Stores Archival Information Packages (AIPs) and Dissemination Information Packages (DIPs) in Fedora. Learn more in the [gemini GitHub repo](https://github.com/RockefellerArchiveCenter/gemini).

#### aquarius
Transforms and delivers Accessions, Archival Objects and Digital Objects to ArchivesSpace. Learn more in the [aquarius GitHub repo](https://github.com/RockefellerArchiveCenter/aquarius).

#### pisces
Retrieves and Transforms data for discovery. Learn more in the [pisces GitHub repo](https://github.com/RockefellerArchiveCenter/pisces).

### Repository
A Fedora repository to store digital records and metadata.

### Discovery
An archival discovery system.

## Meet the RAC Team

{% include team.html %}
