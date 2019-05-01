from utils import functions as _functions

def checkMinData(_dict, _reqr):
    try:
        for item in _reqr:
            if not item in _dict:
                return _functions.setModuleError(payload=f'Missing  field {item} on the request', error=f'{item} whas not found on the request')
        return True
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error checkig endpoint data')

def validLength(**args):
    _min=args.get('_min')
    _max=args.get('_max')
    _str=args.get('_str')
    if _min < len(_str) < _max:
        return True
    return False

def checkPassword(password):
    _min=16
    _max=100
    valid = validLength(_min=_min, _max=_max, _str=password)
    if valid is True:
        return valid
    return _functions.setModuleError(payload=f'Password wrong length: {len(password)}', error=f'Min password length {_min}, maximum {_max}', status=400)
