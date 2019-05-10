---
layout: page
title: Project Components
permalink: /components/
hide: true
---

Project Electron consists of a specification and web application to facilitate ongoing transfers of digital records and their associated metadata from organizations to archives, a repository to store digital records and metadata, an API layer to manage system interactions, and integrations with current and future systems which assist in the archival processes of appraisal, acquisition, arrangement, description, access and preservation.

## Aurora
A Django web application to support and regularize the ongoing secure transfer of digital records
and their metadata to the archives. Explore the [Aurora user documentation](https://docs.rockarch.org/aurora/) and find the code in our [Aurora GitHub repository](https://github.com/RockefellerArchiveCenter/aurora).

## Microservices
An API gateway and set of microservice applications which support integrations between current and future systems and assist in the archival
processes of accessioning, preservation, description, and access.

<div class="container">
  <div class= "six columns card">
    <h3>
      <a href="https://github.com/RockefellerArchiveCenter/zodiac">zodiac</a>
    </h3>
    <p>An API gateway and administration interface for Project Electron microservices, managed via a message queue</p>
  </div>
</div>

<div class="container">
  <div class= "four columns card">
    <h3>
      <a href="https://github.com/RockefellerArchiveCenter/ursa-major">ursa major</a>
    </h3>
    <p>Discovers and stores bags</p>
  </div>

  <div class= "four columns card">
    <h3>
      <a href="https://github.com/RockefellerArchiveCenter/fornax">fornax</a>
    </h3>
    <p>Creates Archivematica-compliant Submission Information Packages</p>
  </div>

  <div class= "four columns card">
    <h3>
      <a href="https://github.com/RockefellerArchiveCenter/libra">libra</a>
    </h3>
    <p>Generates reports on files and activities in Fedora</p>
  </div>
</div>

<div class="container">
  <div class= "four columns card">
    <h3>
      <a href="https://github.com/RockefellerArchiveCenter/gemini">gemini</a>
    </h3>
    <p>Stores Archival Information Packages and Dissemination Information Packages in Fedora</p>
  </div>

  <div class= "four columns card">
    <h3>
      <a href="https://github.com/RockefellerArchiveCenter/aquarius">aquarius</a>
    </h3>
    <p>Transforms and delivers accessions, archival objects and digital objects to ArchivesSpace</p>
  </div>

  <div class= "four columns card">
    <h3>
      <a href="https://github.com/RockefellerArchiveCenter/pisces">pisces</a>
    </h3>
    <p>Retrieves and transforms data for discovery</p>
  </div>
</div>
