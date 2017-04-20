# Messaging Specification

Transfer notifications come in two flavors: success and error.

## Success

```
{
  "result": "done",
  "message": "Bag successfully checked for viruses."
}
```

Should result be integers (ideally corresponding to error codes below)?

## Error

```
{
  "error": 200,
  "message": "Bag validation failed. Metadata elements are missing.",
  "action": "staged for deletion"
}
```

### Error codes

Should we care about avoiding collision (even if it's just perceived semantic collision) with existing error codes for HTTP and things like that?

### Actions

Should these be integers rather than text?

Thinking the list would look like this:
*   Viruses found
*   Incorrect bag structure
*   Incorrect metadata

Might be desirable to provide more granularity (particularly for bag structure or metadata)
