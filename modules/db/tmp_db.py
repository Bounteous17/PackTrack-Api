import redis
from models import redis as _redis
from utils import functions as _functions

def newInstance(newRedis):
    return redis.StrictRedis(
                host=newRedis.host,
                port=newRedis.port,
                db=newRedis.db,
                decode_responses=True
            )

RevokeInstance = newInstance(
            _redis.Redis(
                    host=_functions.Config['redis']['host'],
                    port=_functions.Config['redis']['port'],
                    db=_functions.Config['redis']['instances']['revoke']['db']
                )
        )
TokensExpires = _redis.Expires(
            access_expires=_functions.Config['jwt']['access_expires'],
            refresh_expires=_functions.Config['jwt']['refresh_expires']
        )
