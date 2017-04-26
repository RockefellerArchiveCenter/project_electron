#!/usr/bin/env python

import bagit
import bagit_profile
import os

def validate_bag(target):
    bag = bagit.Bag(target)
    profile = bagit_profile.Profile('https://raw.github.com/ruebot/bagit-profiles/master/bagProfileBar.json')
    if profile.validate_serialization(target):
        print "Serialization validates"
        if profile.validate(bag):
            print "Bag is valid"
        else:
            print "Bag is invalid"
    else:
        print "Serialization does not validate"

def main():
    target = raw_input("Please enter the path of a bag to validate: ")
    if os.path.isdir(target):
        validate_bag(target)
    else:
        print "Sorry, that does not seem to be a valid directory!"

main()
