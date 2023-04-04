# Project Electron

Project Electron is an initiative to build sustainable, open, and user-centered infrastructure for the archival management of digital records at the [Rockefeller Archive Center](http://rockarch.org/).

Project Electron consists of a specification and web application to facilitate ongoing transfers of digital records and their associated metadata from organizations to archives, a repository to store digital records and metadata, an API layer to manage system interactions, and integrations with current and future systems which assist in the archival processes of appraisal, acquisition, arrangement, description, access and preservation. 

Read the [project values](project-values.md) and see our [licensing principles and approaches](licensing).

## Transfer applications
### Aurora
A Django web application to support and regularize the ongoing secure transfer of digital records and their metadata to the archives. Explore the [Aurora user documentation](https://docs.rockarch.org/aurora-docs/) and find the code in the [Aurora GitHub repository](https://github.com/RockefellerArchiveCenter/aurora).

### API Gateway and microservices
An API gateway, microservice applications, and supporting libraries which enable integrations between current and future systems and assist in the archival processes of accessioning, preservation, and discovery. Explore [all Project Electron repositories](https://github.com/topics/project-electron) on GitHub.

  - [zodiac](https://github.com/RockefellerArchiveCenter/zodiac): an API gateway and administration interface for Project Electron microservices, managed via a message queue.
  - [ursa major](https://github.com/RockefellerArchiveCenter/ursa_major): discovers and stores bags.
  - [fornax](https://github.com/RockefellerArchiveCenter/fornax): creates Archivematica-compliant Submission Information Packages.
  - [gemini](https://github.com/RockefellerArchiveCenter/gemini): downloads packages from the Archivematica Storage Service and stores them in Fedora.
  - [aquarius](https://github.com/RockefellerArchiveCenter/aquarius): transforms and delivers accessions, archival objects and digital objects to ArchivesSpace.
  - [libra](https://github.com/RockefellerArchiveCenter/libra): generates reports on files and activities in Fedora.
  - [zorya](https://github.com/RockefellerArchiveCenter/zorya): creates bags from files generated by disk imaging and digitization processes.
  - [aquila](https://github.com/RockefellerArchiveCenter/aquila): stores, calculates, and assigns PREMIS rights statements.

## Archival Discovery
### DIMES
[DIMES](https://github.com/RockefellerArchiveCenter/dimes) is a React web application which provides the front-end user interface for the online discovery of archival collections, objects, and agents.

### Request Broker
The [Request Broker](https://github.com/RockefellerArchiveCenter/request_broker) processes and delivers request data submitted by users from an archival discovery environment.

### Cartographer
[Cartographer](https://github.com/RockefellerArchiveCenter/cartographer) manages JSON tree representations of all the archival collections, sub-collections, and parts (record group, subgroup, series, subseries, etc.) by a designated agent/creator.

### Data Pipeline
A data pipeline which fetches data from ArchivesSpace, transforms it according to our data model, indexes it in Elasticsearch, and serves it up via an API.

- [pisces](https://github.com/RockefellerArchiveCenter/pisces): retrieves, merges and transforms data for discovery.
- [scorpio](https://github.com/RockefellerArchiveCenter/scorpio): adds and deletes archival data (collections, objects, agents and terms) from an Elasticsearch index.
- [argo](https://github.com/RockefellerArchiveCenter/argo): provides a wrapper around the Elasticsearch REST API, and adds additional endpoints required by the DIMES user interface.

## Libraries

  - [asterism](https://github.com/RockefellerArchiveCenter/asterism): helpers and common patterns used in Project Electron infrastructure.
  - [Electron Bonder](https://github.com/RockefellerArchiveCenter/ElectronBonder): client library for working with the Project Electron APIs built using [ArchivesSnake](https://github.com/archivesspace-labs/ArchivesSnake/).
  - [rac_es](https://github.com/RockefellerArchiveCenter/rac_es): helpers for Elasticsearch.
  - [rac-schemas](https://github.com/RockefellerArchiveCenter/rac_schemas): JSON schemas and validation helpers.
  - [IIIF pipeline](https://github.com/RockefellerArchiveCenter/iiif-pipeline): a pipeline to create image derivatives and IIIF Manifests.

## Data Model

Our model for archival data is based on the Portland Common Data Model (PCDM). Check out the [working model overview](https://github.com/RockefellerArchiveCenter/rac_schemas/blob/base/Simplified_Data_Model.png) and JSON schema validations in the [RAC Schemas Repository](https://github.com/RockefellerArchiveCenter/rac_schemas).

## License

All code and documentation are available under the [MIT license](LICENSE), and all documentation is available under the [CC0 license](LICENSE-CC0.md).
