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

## Microservices
An API gateway and set of microservice applications which support integrations between current and future systems and assist in the archival
processes of accessioning, preservation, description, and access.

<div class="container equal-height">
  <div class= "twelve columns card">
    <h3>
      <a href="https://github.com/RockefellerArchiveCenter/zodiac">zodiac</a>
    </h3>
    <p>An API gateway and administration interface for Project Electron microservices, managed via a message queue</p>
  </div>
</div>

<div class="container equal-height">
  <div class= "six columns card">
    <h3>
      <a href="https://github.com/RockefellerArchiveCenter/ursa_major">ursa major</a>
    </h3>
    <p>Discovers and stores bags</p>
  </div>

  <div class= "six columns card">
    <h3>
      <a href="https://github.com/RockefellerArchiveCenter/fornax">fornax</a>
    </h3>
    <p>Creates Archivematica-compliant Submission Information Packages</p>
  </div>
</div>

<div class="container equal-height">
  <div class= "six columns card">
    <h3>
      <a href="https://github.com/RockefellerArchiveCenter/libra">libra</a>
    </h3>
    <p>Generates reports on files and activities in Fedora</p>
  </div>

  <div class= "six columns card">
    <h3>
      <a href="https://github.com/RockefellerArchiveCenter/gemini">gemini</a>
    </h3>
    <p>Stores Archival Information Packages and Dissemination Information Packages in Fedora</p>
  </div>
</div>

<div class="container equal-height">
  <div class= "six columns card">
    <h3>
      <a href="https://github.com/RockefellerArchiveCenter/aquarius">aquarius</a>
    </h3>
    <p>Transforms and delivers accessions, archival objects and digital objects to ArchivesSpace</p>
  </div>

  <div class= "six columns card">
    <h3>
      <a href="https://github.com/RockefellerArchiveCenter/pisces">pisces</a>
    </h3>
    <p>Retrieves and transforms data for discovery</p>
  </div>
</div>
