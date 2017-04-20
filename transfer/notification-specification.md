# Messaging Specification

Transfer notifications come in two flavors: success and error.

## Success

Notifications indicating success will have a `code` value of `200`. The `message` value provides information about the process that was successfully completed, while the optional `action` value indicates system actions that have been taken as a result of the successful process.

```
{
  "code": 200,
  "message": "Bag successfully checked for viruses",
  "action": "Staged for appraisal"
}
```

## Error

Notifications indicating an error has occurred will have a `code` value of `400`. The `error` value indicates a general category of error, while the `message` value provides information about the specific error that occurred. The optional `action` value indicates system actions that have been taken as a result of the error.

```
{
  "code": 400,
  "error": "Bag validation failure",
  "message": "Metadata elements are missing",
  "action": "Staged for deletion",
}
```
