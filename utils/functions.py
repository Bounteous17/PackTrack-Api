import sys
from ruamel.yaml import YAML

def getConfig():
    with open("./config/config.yaml", 'r') as yamlconfig:
        config = YAML().load(yamlconfig)
    return config

Config = getConfig()
