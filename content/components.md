---
layout: page
title: Project Components
permalink: /components/
hide: true
---

Project Electron consists of a specification and web application to facilitate ongoing transfers of digital records and their associated metadata from organizations to archives, a repository to store digital records and metadata, an API layer to manage system interactions, and integrations with current and future systems which assist in the archival processes of appraisal, acquisition, arrangement, description, access and preservation.

## Requests for Comments

Our [Requests for Comments](https://github.com/RockefellerArchiveCenter/project_electron/tree/master/rfcs) (RFCs) are lightly-structured documents which are intended primarily to create a record of decisions we've made regarding technical approaches to solve a particular problem. They are not intended to be policy statements, nor do we expect them to remain unchanged.

  - [RFC 001: Discovery and Delivery](https://github.com/RockefellerArchiveCenter/project_electron/blob/master/rfcs/001-discovery-and-delivery.md)
  - [RFC 002: API Conventions](https://github.com/RockefellerArchiveCenter/project_electron/blob/master/rfcs/002-api-conventions.md)
  - [RFC 003: Indexing](https://github.com/RockefellerArchiveCenter/project_electron/blob/master/rfcs/003-indexing.md)
  - [RFC 004: Merging](https://github.com/RockefellerArchiveCenter/project_electron/blob/master/rfcs/004-mergers.md)
  - [RFC 005: Arrangement Maps](https://github.com/RockefellerArchiveCenter/project_electron/blob/master/rfcs/005-arrangement-maps.md)
  - [RFC 006: Request Broker Service](https://github.com/RockefellerArchiveCenter/project_electron/blob/master/rfcs/006-request-broker-service.md)

## Aurora
A Django web application to support and regularize the ongoing secure transfer of digital records
and their metadata to the archives. Explore the [Aurora user documentation](https://docs.rockarch.org/aurora/) and find the code in our [Aurora GitHub repository](https://github.com/RockefellerArchiveCenter/aurora).

## API Gateway and microservices
An API gateway and set of microservice applications which support integrations between current and future systems and assist in the archival processes of accessioning, preservation, description, and access. Explore [all Project Electron repositories](https://github.com/topics/project-electron) on GitHub.

  - [zodiac](https://github.com/RockefellerArchiveCenter/zodiac): an API gateway and administration interface for Project Electron microservices, managed via a message queue.
  
  - [ursa major](https://github.com/RockefellerArchiveCenter/ursa_major): discovers and stories bags.
  
  - [fornax](https://github.com/RockefellerArchiveCenter/fornax): creates Archivematica-compliant Submission Information Packages.
  
  - [gemini](https://github.com/RockefellerArchiveCenter/gemini): stores Archival Information Packages and Dissemination Information Packages in Fedora.
  
  - [aquarius](https://github.com/RockefellerArchiveCenter/aquarius): transforms and delivers accessions, archival objects and digital objects to ArchivesSpace.
  
  - [libra](https://github.com/RockefellerArchiveCenter/libra): generates reports on files and activities in Fedora.
  
  - [zorya](https://github.com/RockefellerArchiveCenter/zorya): packages bags.
  
### Discovery

- [pisces](https://github.com/RockefellerArchiveCenter/pisces): retrieves and transforms data for discovery.

- [scorpio](https://github.com/RockefellerArchiveCenter/scorpio): merges, indexes, and deletes from index archival data (collections, objects, agents and terms).

- [request broker](https://github.com/RockefellerArchiveCenter/request_broker): processes and delivers request data submitted by users in discovery environment.

- [cartographer](https://github.com/RockefellerArchiveCenter/cartographer): application to manage JSON tree representations of all the archival collections, sub-collections, and parts (record group, subgroup, series, subseries, etc.) by a designated agent/creator.

### Libraries

  - [asterism](https://github.com/RockefellerArchiveCenter/asterism): helpers and common patterns used in Project Electron infrastructure.

  - [Electron Bonder](https://github.com/RockefellerArchiveCenter/ElectronBonder): client library for working with the Project Electron APIs built using [ArchivesSnake](https://github.com/archivesspace-labs/ArchivesSnake/).

  - [rac_es](https://github.com/RockefellerArchiveCenter/rac_es): helpers for Elasticsearch.
