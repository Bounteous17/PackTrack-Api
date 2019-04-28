import sys
from ruamel.yaml import YAML
from models import rest as _rest
from utils import colorize as _colorize

def setModuleError(**args):
    _colorize.consoleLog(msg="Technical error: %s" %(args.get('payload')), action="error")
    _colorize.consoleLog(msg="Human error: %s" %(args.get('error')), action="info")
    return _rest.ModuleStatus(payload=args.get('payload'), error=args.get('error'), key=args.get('key'), status=args.get('status'))


def setModuleSuccess(**args):
    _colorize.consoleLog(msg="Success return: %s" %(args.get('payload')), action="success")
    return _rest.ModuleStatus(payload=args.get('payload'), key=args.get('key'), status=args.get('status'))

def setFlaskResponse(result):
    result.setStatus()
    return result.flaskResp()

def resultError(result):
    if isinstance(result, _rest.ModuleStatus) and result.error:
        return True
    return False

def getConfig():
    try:
        readYamlConfig = readFile("./config/config.yaml", 'r')
        if resultError(readYamlConfig):
            return readYamlConfig

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

def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__

Config = getConfig()
