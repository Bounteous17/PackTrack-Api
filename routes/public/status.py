from utils import functions as _functions

def alive():
    try:
        return _functions.setModuleSuccess(payload='Hi, how are you', status=200)
    except Exception as e:
        return _functions.setModuleError(payload=e, error="Error checking alive", status=500)

