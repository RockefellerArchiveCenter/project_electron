# Creates a valid bag using metadata values hardcoded into the script. The directory to bag (which may contain subdirectories) 
# can either be passed as the first argument or entered when at the script prompt.
# Created by @RockefellerArchiveCenter for Project Electron

#!/usr/bin/env python

import bagit
import os
from datetime import datetime
import sys


def make_bag(target):
    # define metadata
    metadata = {
        'Source-Organization': 'Ford Foundation',
        'External-Identifier': '1968November22',
        'Internal-Sender-Description': 'Grant awarded to the Village Green Preservation Society for the purpose of \"preserving the old ways from being abused, protecting the new ways for me and for you\"', # single and double quotes must be escaped
        'Title': 'Grant to the Village Green Preservation Society',
        'Date-Start': '1966-11-01',
        'Date-End': '1968-11-22',
        'Record-Creators': ['Custard Pie Appreciation Consortium', 'Desperate Dan Appreciation Society'], # multiple values for a single key are added as lists.
        'Record-Type': 'grant records',
        'Language': 'eng',
        'Bagging-Date': datetime.now().isoformat(),
        'BagIt-Profile-Identifier': 'https://raw.githubusercontent.com/RockefellerArchiveCenter/project_electron/master/transfer/organizational-bag-profile.json'
        }

    # make bag
    bag = bagit.make_bag(target, metadata)


def main():
    if len(sys.argv) == 2:
        # use target directory passed as argument
        target = sys.argv[1]
    else:
        # get target directory from user input
        target = raw_input("Please enter the path of a local directory to bag: ")

    if os.path.isdir(target):
        make_bag(target)
    else:
        print "Sorry, that does not seem to be a valid directory!"

main()