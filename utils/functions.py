import sys
from ruamel.yaml import YAML
from models import rest as _rest
from utils import colorize as _colorize

def setModuleError(**args):
    _colorize.consoleLog(msg="Technical error: %s" %(args.get('payload')), action="error")
    _colorize.consoleLog(msg="Response sent to the client: %s" %(args.get('error')), action="info")
    newError = _rest.ModuleStatus(payload=args.get('payload'), error=args.get('error'), status=args.get('status'))
    newError.setStatus()
    return newError

def resultError(result):
    if isinstance(result, _rest.ModuleStatus) and result.error:
        return True
    return False


def getConfig():
    try:
        readYamlConfig = readFile("./config/config.yaml", 'r')
        if resultError(readYamlConfig):
            exit(1)

        yamlconfig = readYamlConfig
        config = YAML().load(yamlconfig)
        return config
    except Exception as e:
        return setModuleError(payload=e, error='Error reading config file')

def readFile(path, perms):
    try:
        if not perms:
            perms = 'r'
        f = open(path, perms)
        return f.read()
    except Exception as e:
        return setModuleError(payload=e, error='RAW file can\'t be accessed at the moment')

def respStatus(status):
    if not status:
        status = 200
    return status


Config = getConfig()
