# Notifications

Transfer notifications come in two flavors: success and error. They are provided in machine-readable and human-readable formats.

## Success

### For Machines

Machine-readable notifications indicating success will have a `code` value of `200`. The `message` value provides information about the process that was successfully completed, while the optional `action` value indicates system actions that have been taken as a result of the successful process and `time` is a timestamp taken when the process completed successfully.

```
{
  "code": 200,
  "message": "Bag successfully checked for viruses",
  "action": "Staged for appraisal"
  "time": 2017-04-21T20:01:07+00:00
}
```

### For People

Success notifications for humans will contain the following information:
*   A description of the process(es) successfully completed
*   The time the process(es) were completed
*   What process(es) will happen next
*   What actions, if any, need to be taken

It may be desirable to bundle these notifications in a daily digest, rather than sending individual messages as they occur. It may also be desirable to send a single success message if a transfer successfully completes a set of automated processes (for example post-transfer virus check and bag validation) rather than a message for each process successfully completed.

## Error

### For Machines

Notifications indicating an error has occurred will have a `code` value of `400`. The `error` value indicates a general category of error, while the `message` value provides information about the specific error that occurred. The optional `action` value indicates system actions that have been taken as a result of the error and `time` is a timestamp taken when the error occurred.

```
{
  "code": 400,
  "error": "Bag validation failure",
  "message": "Metadata elements are missing",
  "action": "Staged for deletion",
  "time": 2017-04-21T20:01:07+00:00
}
```

### For People

Error notifications for people will contain the following information:
*   A description of the process(es) during which the error occurred
*   The time at which the error occurred
*   A complete error log
*   What process(es) will happen next
*   What actions, if any, need to be taken

Error notifications should be sent as soon as they occur.
