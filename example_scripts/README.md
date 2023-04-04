# Example Scripts

These example Python scripts create and validate bags with user-supplied payloads. These scripts make use of existing Python libraries for working with BagIt-compliant bags. Both require [bagit-python](https://github.com/LibraryOfCongress/bagit-python), and `validate_bag.py` requires [bagit-profiles-validator](https://github.com/bagit-profiles/bagit-profiles-validator). 

`validate-bag.py` validates against `organizational-bag-profile.json`, an example Rockefeller Archive Center BagIt Profile which encodes transfer requirements in a machine-readable format to ensure and facilitate compliance. Each organization has a BagIt Profile which is customized to meet their needs.