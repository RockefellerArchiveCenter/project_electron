#!/usr/bin/env python

import bagit
import os
from datetime import datetime

def make_bag(target):
    # get date
    date = datetime.now().isoformat()

    # define metadata
    metadata = {
        'Source-Organization':'The Kinks Community Foundation',
        'External-Identifier':'1968November22',
        'Internal-Sender-Description':'Grant awarded to the Village Green Preservation Society for the purpose of \"preserving the old ways from being abused, protecting the new ways for me and for you\"', # single and double quotes must be escaped
        'Title':'Grant to the Village Green Preservation Society',
        'Date-Start':'1966-11',
        'Date-End':'1968-11-22',
        'Record-Creators':['Custard Pie Appreciation Consortium', 'Desperate Dan Appreciation Society'], # multiple values for a single key are added as lists.
        'Record-Type':'grant records',
        'Language':'http://id.loc.gov/vocabulary/iso639-2/eng',
        'Restrictions':'Records open only to Mrs. Mopp and good old Mother Riley',
        'Bagging-Date':date,
        'Bag-Count':'1 of 2',
        'Bag-Group-Identifier':'Grants1968',
        'BagIt-Profile-Identifier': 'https://raw.github.com/ruebot/bagit-profiles/master/bagProfileBar.json'
        }

    # make bag
    bag = bagit.make_bag(target, metadata)

def main():
    # get target directory from user input
    target = raw_input("Please enter the path of a local directory to bag: ")

    if os.path.isdir(target):
        make_bag(target)
    else:
        print "Sorry, that does not seem to be a valid directory!"

main()
