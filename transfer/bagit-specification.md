under_construction.gif

# Rockefeller Archive Center BagIt Specification
This page describes the specifics of the RAC's BagIt specification. Senders will create and bag all materials before sending them to the RAC for ingest.

## Specification
1. RAC packages conform to the [BagIt packaging specification](https://tools.ietf.org/html/draft-kunze-bagit-14 "BagIt Specification")
2. RAC packages may be
  1. serialized (single zip, rar, or tar)
  2. un-serialized
3. All bags must conform to the [RAC BagIt profile] (https://github.com/RockefellerArchiveCenter/project_electron/blob/master/transfer/bagit_spec.json "RAC BagIt JSON")

## RAC BagIt Structure
This section includes a single suggestion for sending bags to the RAC. The RAC accepts both serialized and un-serialized bags, but for this example, we will just provide an un-serialized example.

```
<RAC-BAG-ID>/
    | bagit.txt
    | manifest-md5.txt
    | bag-info.txt
    \--- data/
          | [payload files]
          | metadata.json
```

### Description

###### RAC-BAG-ID
The name of the root directory of the bag.

###### bagit.txt
As required in the BagIt spec. Includes BagIt version and tag file character encoding.
```
BagIt-Version: 0.97
Tag-File-Character-Encoding: UTF-8
```

###### manifest-md5.txt
This is a required element from the BagIt spec. For our example we have chosed md5, but sha256 is also acceptable.
Contains a checksum for every item included in the bag's payload.

###### bag-info.txt
The RAC requires the the presence of the following fields, but some of them may be nil or empty.
For more details on the content and usage of each field, please see the Bag Info information at the bottom of this document. The RAC will only index and ingest metadata from bag-info.txt into our linked data storage.
```
Source-Organization
External-Identifier
Internal-Sender-Description
Title
Date-Start
Date-End
Record-Creators
Record-Type
Language
Restrictions
Bagging-Date
Payload-Oxum
```
###### data
Required directory for payload items. May be serialized or un-serialized.

###### metadata.json
Valid JSON or JSON-LD file that includes any additional metadata that our donors would like to provide to the RAC.

---

## RAC Bag-Info Field Specifications

### Source-Organization

* **Definition:** Reserved field specified by the BagIt specification. Include the organization sending the content.
* **Purpose:** Provides information to the RAC about the organization sending the records.
* **Data type:** Locally controlled: Ford Foundation, Rockefeller Foundation, Commonwealth Fund, etc. Will be expanded as necessary.
* **Obligation:** Required
* **Repeatability:** No
* **Examples:** "Ford Foundation"

### External-Identifier

* **Definition:** A unique identifier applied to each group of records composed of characters, numbers or letters, or a combination thereof, that uniquely identify the record within a given domain.
* **Purpose:** Ensures that records can be uniquely identified within the RAC's systems during archival processes.
* **Data type:** String
* **Obligation:** Required
* **Repeatability:** No
* **Examples:** "OyGpXmSFVkCpds7i4gRv"

### Internal-Sender-Description

* **Definition:** A prose description of the nature and contents of the group of records.
* **Purpose:** Aids user discovery by providing description about the content and context of records.
* **Data type:** String
* **Obligation:** Required
* **Repeatability:** No
* **Examples:** "Annual reports discussing the accomplishments and major strategic initiatives of the Ford Foundation."

### Title

* **Definition:** The title of a group of records. Do not include dates in the title element. This should not be a description of the type of materials, and instead a declarative title for all records.
* **Purpose:** Enables information search and discovery, facilitates user choice and provides additional context for archival records.
* **Data type:** String
* **Obligation:** Required
* **Repeatability:** No
* **Examples:** "Annual Reports"

### Date-Start

* **Definition:** The start date for which the group of records was created.
* **Purpose:** Enables information search and discovery, facilitates user choice and provides additional context for archival records.
* **Data type:** Values must meet ISO 8601: Standard for Representation of Dates and Times.
* **Obligation:** Required
* **Repeatability:** No
* **Examples:** "1995-01-01"

### Date-End

* **Definition:** The start date for which the group of records ends.
* **Purpose:** Enables information search and discovery, facilitates user choice and provides additional context for archival records.
* **Data type:** Values must meet ISO 8601: Standard for Representation of Dates and Times.
* **Obligation:** Required
* **Repeatability:** No
* **Examples:** "1997-12-31"

### Record-Creators

* **Definition:** Identifies the individuals, organizations or departments that created the group of records.
* **Purpose:** Provides evidence and context for records by identifying the creator of the record and supports user search, allowing information to be filtered.
* **Data type:** String
* **Obligation:** Required
* **Repeatability:** Yes
* **Examples:**
  * "Ford Foundation"
  * "Walker, Darren"

### Record-Type

* **Definition:** The broad category into which the records fall.
* **Purpose:** Allows different validation rules for transfer metadata to be used for different kinds of records.
* **Data type:** Locally controlled: administrative records, annual reports, board materials, communications and publications, grant records. The RAC may expand or reduce these types as necessary.
* **Obligation:** Required
* **Repeatability:** Yes
* **Examples:**
  * "annual reports"
  * "grant records"

### Languages

* **Definition:** The natural language(s) in which the materials are written.
* **Purpose:** Assists user evaluation of relevance and facilitates machine translation.
* **Data type:** Values must meet ISO 639-2: Codes for the Representation of Names of Languages. Use URIs linking directly to the language code. If materials have no language, please use "nil"
* **Obligation:** Required
* **Repeatability:** Yes
* **Examples:**
  * "http://id.loc.gov/vocabulary/iso639-2/eng"
  * "http://id.loc.gov/vocabulary/iso639-2/spa"

### Restrictions

* **Definition:** Any specific restrictions related specifically to the group of records. Do not record general restrictions related to all records (or record types) from a given person or organization. This field is only for special-case restrictions out of the ordinary.
* **Purpose:** Provides information to users about the availability of records, and assists archivists in responsibly providing access to records that deviate from the overall restriction agreements with donors.
* **Data type:** String
* **Obligation:** Optional
* **Repeatability:** No
* **Examples:** "The annual report for 1996 might have IP restrictions due to photographs appearing in it that the Ford Foundation does not have rights over."

### Bagging-Date

* **Definition:** Reserved field specified by the BagIt specification. Date that the content was prepared for delivery.
* **Puropose:** Provides the date the bag was created.
* **Data type:** Values must meet ISO 8601: Standard for Representation of Dates and Times.
* **Obligation:** Required
* **Repeatability:** No
* **Examples:** "2016-04-24"

### Payload-Oxum

* **Definition:** Reserved field specified by the BagIt specification. The "octetstream sum" of the payload, namely, a two-part number of the form "OctetCount.StreamCount", where OctetCount is the total number of octets (8-bit bytes) across all payload file content and StreamCount is the total number of payload files. Payload-Oxum should be included in "bag-info.txt" if at all possible.
* **Purpose:** Payload-Oxum is intended for machine consumption.
* **Data type:** OctetCount.StreamCount
* **Obligation:** Required
* **Repeatability:** No
* **Examples:** "279164409832.1198"
