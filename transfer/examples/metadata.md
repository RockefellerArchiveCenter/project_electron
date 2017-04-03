# Metadata Template

A file named `metadata.json` should be included in the `data/` directory of the bag.

```
{
  "identifier": "OyGpXmSFVkCpds7i4gRv",
  "title": "Annual Reports",
  "dates":[
    {
      "type": "creation",
      "start": "1994-01-01",
      "end": "1997-01-01"
    }
  ],
  "creators": [
    {
      "name": "Ford Foundation",
      "id": "https://www.fordfoundation.org#organization"
    }
  ],
  "languages": ["http://id.loc.gov/vocabulary/iso639-2/eng", "http://id.loc.gov/vocabulary/iso639-2/spa"],
  "description": "Annual reports from the Ford Foundation.",
  "restrictions": [{}]
}
```

## Identifier  

*   **Definition**: A unique identifier applied to each group of record composed of characters, numbers or letters, or a combination thereof, that uniquely identify the record within a given domain.
*   **Purpose**: Ensures that records can be identified as unique within a system or during a system migration.
*   **Data type**: String
*   **Obligation**: Required
*   **Repeatability**: No
*   **Examples**:

## Title

*   **Definition**: The title of a group of records. Do not include dates in the title element.
*   **Purpose**: Enables information search and discovery, facilitates user choice and provides additional context.
*   **Data type**: String
*   **Obligation**: Required
*   **Repeatability**: No
*   **Examples**:


## Dates

*   **Definition**: The date on or date range in which the group of records was created.
*   **Purpose**: 	Provides evidence that the record is authentic and records date information about the item.
*   **Data type**: Values must meet ISO 8601: Standard for Representation of Dates and Times.
*   **Obligation**: Required
*   **Repeatability**: No
*   **Examples**:

What happens when there are significant gaps in records? What is the use case for making this element repeatable?

Look at AS date model. How complex these are may depend a lot on what parsers are available to us.

## Creators

*   **Definition**: Identifies the individuals, organizations or departments that created the group of records.
*   **Purpose**: Provides evidence and context for records by identifying the creator of the record and supports user search, allowing information to be filtered.
*   **Data type**: Name object
*   **Obligation**: Required
*   **Repeatability**: Yes
*   **Examples**:

### Name Object

#### Name String

A human-readable string.

#### Name Scheme

Used when a naming scheme is used for assigning names.

Possible to have a more robust data model; look at AS model.

*   role (could be something other than creator)
*   type (person/organization)
*   URI
*   Name String

## Languages

*   **Definition**: The natural language(s) in which the materials are written.
*   **Purpose**: Assists user evaluation of relevance and facilitates machine translation.
*   **Data type**: Values must meet ISO 639-2: Codes for the Representation of Names of Languages.
*   **Obligation**: Required
*   **Repeatability**: Yes
*   **Examples**:

Use URIs? What about records that have no language content?

Could also make this a single value and just ask organizations to use `mul` if there are multiple languages present.

## Description

*   **Definition**: A prose description of the nature and contents of the group of records.
*   **Purpose**: Aids user discovery by providing description about the content and context of records.
*   **Data type**: String
*   **Obligation**: Required
*   **Repeatability**: No
*   **Examples**:

## Restrictions

*   **Definition**: Any specific restrictions related specifically to the group of records. Do not record general restrictions related to all records (or record types) from a given person or organization.
*   **Purpose**: Provides information to users about the availability of records, and assists archivists in responsibly providing access to records.
*   **Data type**: String
*   **Obligation**: Optional
*   **Repeatability**: No
*   **Examples**:

Depends a lot on what "restriction" means to our donors; may have to just be a text field.

Wouldn't it be great if we had a set of locally-maintained restrictions? Or would that be a waste of time?

What about IP?
