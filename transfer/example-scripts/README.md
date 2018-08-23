# Example Scripts

Scripts to create and validate bags.

`create_bag.py` creates a valid bag using metadata values hardcoded into the script. The directory to bag (which may contain subdirectories) can either be passed as the first argument or entered when at the script prompt.

`validate_bag.py` prompts users to specify an existing bag to validate. In addition to validating against the BagIt Specification, this validates against the [Rockefeller Archive Center BagIt Profile](../organizational-bag-profile.json).

These scripts make use of existing Python libraries for working with BagIt-compliant bags. Both require [bagit-python](https://github.com/LibraryOfCongress/bagit-python), and `validate_bag.py` requires [bagit-profiles-validator](https://github.com/ruebot/bagit-profiles-validator) as well.
