# RFC 002 - API Conventions

Last updated August 25, 2020

## Problem Statement
In order to make our APIs predictable and usable with the minimum amount of documentation, we need to ensure all public endpoints conform to certain conventions. We also need to document these conventions and build unit tests against them.

## Proposed Solution
The following API conventions are used consistently across endpoints.

### Data Keys
  - Are lowercase
  - Use snake case

### Structured Filters
  - Non-scoring (no relevance rankings)
  - Supplied as query parameters
  - Use the name of the property they are used to filter
  - Multiple query parameters are combined using AND
  - Multiple double underscore (`__`) separated values within a single query parameter are combined using OR
  - Double underscore syntax is used to specify paths

#### Examples
`/agents/?title=Raffi`
`/collections/?ancestors__isnull=true`

### Full-text search
  - Scoring (ranked by relevance)
  - Supplied as a single query parameter called `query`
  - Can be combined with any combination of structured filters
  - Generally searches only fields with text content

#### Examples

`/search/?query=bananas`
`/agents/?query=born`

### Sorting
  - Default sort can be overridden using a sort parameter called `sort`
  - Properties which can be sorted on will vary
  - The value of this parameter is a single property
  - By default the named property will be sorted ascending. Descending order can be achieved by appending a `-` to the start of the property

### Limiting results
  - List views can return a limited number of results
  - Supplied as a single query parameter called `limit`

#### Examples
`/search/?query=bananas&limit=5`
