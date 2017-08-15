#!/usr/bin/env python

import bagit
import bagit_profile
import os

def validate_bag(target):
    bag = bagit.Bag(target)
    profile = bagit_profile.Profile('https://raw.githubusercontent.com/RockefellerArchiveCenter/project_electron/master/transfer/organizational-bag-profile.json')

    # Validate bag against BagIt specification using bagit library
    try:
      bag.validate()
      print "Bag valid according to BagIt specification"
    except bagit.BagValidationError, e:
        print "Bag invalid according to BagIt specification"
        print e
        exit()

    # Validate profile serialization using bagit_profile library
    try:
        profile.validate_serialization(target)
        print "Bag serialization validates"
    except:
        print "Bag serialization does not validate"
        exit()

    # Validate bag against BagIt Profile using bagit_profile library
    if profile.validate(bag):
        print "Bag valid according to RAC profile"
    else:
        print "Bag invalid according to RAC profile"
        exit()

def main():
    target = raw_input("Please enter the path of a bag to validate: ")
    if os.path.isdir(target):
        validate_bag(target)
    else:
        print "Sorry, that does not seem to be a valid directory!"

main()
