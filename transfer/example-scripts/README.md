# Example Scripts

Scripts to create and validate bags.

`create_bag.py` prompts users to specify a directory (which may contain subdirectories) as the bag payload. Metadata values written to `bag-info.txt` can be edited by changing variables in each script.

`validate_bag.py` prompts users to specify an existing bag to validate. In addition to validating against the BagIt Specification, this validates against the [Rockefeller Archive Center BagIt Profile](../organizational-bag-profile.json).

These scripts make use of existing Python libraries for working with BagIt-compliant bags. Both require [bagit-python](https://github.com/LibraryOfCongress/bagit-python), and `validate_bag.py` requires [bagit-profiles-validator](https://github.com/ruebot/bagit-profiles-validator) as well.
