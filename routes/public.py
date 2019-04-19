from utils import functions as _functions

def alive():
    try:
        return 'Hi, how are you';
    except Exception as e:
        error = "Error checking alive"
        newError = _functions.setModuleError(payload=e, error=error)
        return newError.flaskResp()

