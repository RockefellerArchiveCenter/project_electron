---
layout: page
title:  Example Scripts for the Transfer of Digital Records
permalink: /scripts/
---
These example python scripts create and validate bags with user-supplied payloads. These scripts make use of existing Python libraries for working with BagIt-compliant bags. Both require [bagit-python](https://github.com/LibraryOfCongress/bagit-python), and `validate_bag.py` requires [bagit-profiles-validator](https://github.com/ruebot/bagit-profiles-validator).

## Create a valid bag
`create_bag.py` creates a valid bag using metadata values hardcoded into the script. The directory to bag (which may contain subdirectories) can either be passed as the first argument or entered when at the script prompt. [View the create_bag.py script](https://gist.github.com/HaSistrunk/39e4696eb3f1f5d0e983aed4f1403619).

## Validate bag
`validate_bag.py` prompts users to specify an existing bag to validate. This validates against the [Rockefeller Archive Center BagIt Profile](https://gist.github.com/HaSistrunk/65d59e558c436b9d934d98fd8fb0f575) and the BagIt Specification. [View the validate_bag.py script](https://gist.github.com/HaSistrunk/998a69e41924690554d0c6ae22a8fd9b).
