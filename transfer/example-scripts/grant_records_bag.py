#!/usr/bin/env python

import bagit
import os

def make_bag(target):
    # define metadata
    metadata = {
        'Contact-Name': ['John Kunze', 'Andy Boyko'],
        'Internal-Sender-Description': 'This is some crap',
        'Restrictions': 'Grant records are closed to research until 10 years after inactive date'
        }

    # make bag
    bag = bagit.make_bag(target, metadata)

def main():
    # get target directory from user input
    target = raw_input("Please enter the relative or absolute path of a local directory to bag: ")

    if os.path.isdir(target):
        make_bag(target)
    else:
        print "Sorry, that does not seem to be a valid directory!"

main()
