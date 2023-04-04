 Prompts users to specify an existing bag to validate. Validates against the BagIt Specification, this and the Rockefeller 
# Archive Center BagIt Profile.
# Created by the @RockefellerArchiveCenter for Project Electron

#!/usr/bin/env python

import bagit
import bagit_profile
import iso8601
import json
from os.path import isfile, isdir, join
import re
from pycountry import languages

# Reads keys from bag-info.txt into dictionary
def get_fields_from_file(fpath):
    fields = {}
    try:
        patterns = [
            '(?P<key>[\w\-]+)',
            '(?P<val>.+)'
        ]
        with open(fpath,'rb') as f:
            for line in f.readlines():
                line = line.strip('\n')

                row_search = re.search(":?(\s)?".join(patterns), line)
                if row_search:
                    fields[row_search.group('key').replace('-','_').strip()] = row_search.group('val').strip()
    except Exception as e:
        print e

    return fields

# Validates date and language datatypes
def validate_datatypes(bag):
    """Assumes a valid bag/bag info; returns true if all datatypes in bag pass"""
    dates = []
    langz = []

    bag_dates_to_validate = ['Date_Start', 'Date_End', 'Bagging_Date']
    bag_info_data = get_fields_from_file(join(str(bag), 'bag-info.txt'))

    for k,v in bag_info_data.iteritems():
        if k in bag_dates_to_validate:
            dates.append(v)
        if k == 'Language':
            langz.append(v)

    if dates:
        for date in dates:
            try:
                iso8601.parse_date(date)
            except:
                print "invalid date: '{}'".format(date)
                return False

    if langz:
        for language in langz:
            try:
                languages.lookup(language)
            except:
                print "invalid language code: '{}'".format(language)
                return False
    return True

# Makes sure optional metadata.json file is valid JSON
def validate_metadata_file(bag):
    """checks if the metadata file path and is json is correct if exist"""

    try:
        data = ''
        with open(metadata_file,'r') as open_file:
            data = open_file.read()
            return data
            return json.loads(data)
    except ValueError as e:
        print "invalid json: {}".format(e)

    return False

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

    #Validate date and language datatypes
    if validate_datatypes(bag):
        print "All datatypes in bag are valid"
    else:
        print "Invalid datatypes"
        exit()

    #Make sure metadata.json is valid
    metadata_file = join(str(bag), 'data', 'metadata.json')
    if not isfile(metadata_file):
        print 'no metadata file'
    else:
        if validate_metadata_file(bag):
            print "Optional metadata.json file is valid"
        else:
            print "Optional metadata.json file is not valid JSON"
            exit()

def main():
    target = raw_input("Please enter the path of a bag to validate: ")
    if isdir(target):
        validate_bag(target)
    else:
        print "Sorry, that does not seem to be a valid directory!"

main()