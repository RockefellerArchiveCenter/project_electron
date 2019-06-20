---
layout: page
title:  Example Scripts and BagIt Profile for The Transfer of Digital Records
permalink: /scripts/
hide: true
---
These example Python scripts create and validate bags with user-supplied payloads. These scripts make use of existing Python libraries for working with BagIt-compliant bags. Both require [bagit-python](https://github.com/LibraryOfCongress/bagit-python), and `validate_bag.py` requires [bagit-profiles-validator](https://github.com/ruebot/bagit-profiles-validator). `validate-bag.py` validates against `organizational-bag-profile.json`, an example Rockefeller Archive Center BagIt Profile.

## Create a valid bag
`create_bag.py` creates a valid bag using metadata values hardcoded into the script. The directory to bag (which may contain subdirectories) can either be passed as the first argument or entered when at the script prompt.

<script src="https://gist.github.com/HaSistrunk/39e4696eb3f1f5d0e983aed4f1403619.js"></script>

## Validate bag
`validate_bag.py` prompts users to specify an existing bag to validate. This validates against the [Rockefeller Archive Center BagIt Profile](#rockefeller-archive-center-bagit-profile) and the BagIt Specification.

<script src="https://gist.github.com/HaSistrunk/998a69e41924690554d0c6ae22a8fd9b.js"></script>

## Rockefeller Archive Center BagIt Profile

`organizational-bag-profile.json` is a sample Rockefeller Archive Center BagIt Profile which encodes transfer requirements in a machine-readable format to ensure and facilitate compliance. Each organization has a BagIt Profile which is customized to meet their needs.

<script src="https://gist.github.com/HaSistrunk/65d59e558c436b9d934d98fd8fb0f575.js"></script>
