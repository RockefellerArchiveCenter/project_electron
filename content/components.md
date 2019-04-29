---
layout: page
title: Project Components
permalink: /components/
hide: true
---

Project Electron consists of a specification and web application to facilitate ongoing transfers of digital records and their associated metadata from organizations to archives, a repository to store digital records and metadata, an API layer to manage system interactions, and integrations with current and future systems which assist in the archival processes of appraisal, acquisition, arrangement, description, access and preservation.

### Transfer Specification
A [specification to transfer digital records and metadata](/transfer/) to archives over a network connection.

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
