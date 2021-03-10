#!/usr/bin/python3

import simpy
import logging
import logging.handlers
import sys
import json
from simmbse import Branch

# Load System Model
with open('./function.json', 'r') as inf:
    systemModel = json.load(inf)
    inf.close()

# Setup Logger
logger = logging.getLogger("SimMA")
logger.setLevel(logging.DEBUG)
ls = logging.StreamHandler(sys.stdout)
ls.setLevel(logging.INFO)
logFormat = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
ls.setFormatter(logFormat)
logger.addHandler(ls)

# Initialize SimPy
env = simpy.Environment()

def main():
    for call in systemModel['data']['cpsSystemModel']['callStructure']:
        if call['function']['name'] == "Main":
            print("Parsing Main Branch....")
            mainStructure = Branch(env, logger, "0", systemModel, call['structure'])
            print(mainStructure)
if __name__ == "__main__":
    main()
