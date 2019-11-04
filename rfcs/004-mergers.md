# RFC 004 - Mergers

Last updated October 2, 2019

## Background/Problem Statement
Because we fetch and transform data from multiple sources, the same object (Collection, Object, Agent or Term) can be independently referenced in different sources. However, when we index data, we want to ensure that object which are the same are merged into a single object.

## Proposed Solution
Implement a matching and merging service which finds matching data objects and merges them based on rules specific to the data object type and source.

### Definitions
**Transformed data objects** are received from data transformers. Each transformed data object:
  - has a source
  - has one or more fields
  - may contain data which extends existing data in an object from another source
  - may contain data which updates existing data in an object from the same source
  - may contain new data not yet indexed

**Fields** are distinct data elements within a transformed data object. Fields are either:
  - **Single source fields**, or fields that only exist in a single source and have implicit source awareness, meaning that their source is usually specified in mappings as opposed to explicitly stated in the data itself. In general, these fields can be replaced or ignored wholesale.
  - **Multi-source fields** are usually arrays  or lists of nested data objects such as identifiers or notes. In these fields, the source is explicitly stated in the data itself as part of the nested object. In general, merging for multi-source fields only acts on nested objects which match sources.

### Overall Process
The overal matching and merging process consists of three discrete steps.
#### Find existing matches
  - Matching is based on the transformed data object's `external_ids` array, search the index for the `source_id`, which is a concatenation of the `source` and `identifier`
#### Apply matching rules for each match found in step one
  - This will take place in two methods: `apply_single_source_merges()` and `apply_multi_source_merges()`.
  - Both the `source` and `identifier` value will likely need to be passed to the merging methods.
  - Merging methods should also add an external identifier object to the target object's `external_ids` array
#### Persist merged objects
  - TBD whether this is a message queue or a database.
