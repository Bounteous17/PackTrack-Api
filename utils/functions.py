import sys
from ruamel.yaml import YAML

def getConfig():
    try:
        readYamlConfig = readFile("./config/config.yaml", 'r')
        if "error" in readYamlConfig:
            return readYamlConfig

        yamlconfig = readYamlConfig
        config = YAML().load(yamlconfig)
        return config
    except Exception as e:
        print (e)
        return {
                    "error": "An unexpected error ocurred reading config"
                }

def readFile(path, perms):
    try:
        if not perms:
            perms = 'r'
        f = open(path, perms)
        return f.read()
    except Exception as e:
        print (e)
        return {
                    "error": "An unexpected error occurred reading file"
                }

Config = getConfig()
