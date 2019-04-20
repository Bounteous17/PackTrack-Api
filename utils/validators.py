from utils import functions as _functions

def checkMinData(_dict, _reqr):
    try:
        for item in _reqr:
            if not item in _dict:
                return _functions.setModuleError(payload=f'Missing  field {item} on the request', error=f'{item} whas not found on the request')
        return True
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error checkig endpoint data')
