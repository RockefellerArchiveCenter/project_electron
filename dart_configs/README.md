# DART Configuration Files

This directory contains files which can be imported into DART to set up BagIt Profiles
and Storage Services to support the transfer of digital records through Aurora.

A link to a file should be sent to the individual at the donor organization
responsible for setting up DART, along with a message emphasizing the following:
- Instructions for importing settings can be found in the official DART documentations at <https://aptrust.github.io/dart-docs/users/settings/import/>
- The import will set up two separate areas of DART functionality:
  - BagIt Profile (see <https://aptrust.github.io/dart-docs/users/bagit/>): which
    controls which the fields which appear in the metadata entry step of creating
    transfers/bags, including required fields and fields with controlled values.
  - Storage Services (see <https://aptrust.github.io/dart-docs/users/settings/storage_services/>)
    which allows users to upload transfers/bags to Aurora development and production
    environments. For security reasons, usernames and passwords are not stored in
    these configuration files, so when you import the settings file DART will prompt
    you to enter credentials for an account in Aurora. Initially this will only
    be for Aurora development, but once initial testing has been completed we can
    either re-deliver a new config file or provide instructions on how to update
    the Storage Service settings to point at the production instance of Aurora.
