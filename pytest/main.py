#!/usr/bin/env python

__author__ = 'nwilson'

import sys
import ConfigParser

if __name__ == "__main__":

    config = ConfigParser.ConfigParser()
    config.read("util/pytest.config")

    print(config.sections())

    print(config.get("category", "option1"))
    print(config.get("category", "option2"))
    print(config.get("category", "option3"))
    print(config.get("category", "option4"))

    print(sys.version)
    print("this is only a test")
