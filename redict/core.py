from redis import Redis


class Redict(object):
    def __init__(self, host: str = 'localhost', port: int = 6379, db: int = 0, encoding: str = 'utf-8',
                 expire: int = None):
        self._redis = Redis(host=host, port=port, db=db, encoding=encoding)
        self._expire = expire
        self._encoding = encoding

    def __setitem__(self, key: any, value: any) -> bool:
        if self._expire:
            return self._redis.setex(key, self._expire, value)
        return self._redis.set(key, value)

    def __getitem__(self, key: any) -> str:
        value = self._redis.get(key)

        if value:
            self._redis.expire(key, self._expire)
            return value.decode(self._encoding)

        raise KeyError(key)

    def __contains__(self, key: any) -> bool:
        return self._redis.exists(key)
