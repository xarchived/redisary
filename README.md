# Redisary
Redis is a key-value database. Interestingly Python dictionaries are some how key-value data structure. So why not write
a wrapper that map Python dictionary to Redis server.

## Installation
```bash
pip install -U https://github.com/xurvan/redict/archive/master.zip
```

## Quickstart
A very simple usage could be like:

```python
from redisary import Redisary

redis = Redisary(host='127.0.0.1', db=0)

redis['k'] = 'data'
data = redis['k']
```
Well it works like a normal dictionary, the only advantage is data now stored on Redis and we could access it from
another process.

We also could set an expire for all keys of dictionary:


```python
from redisary import Redisary

redis = Redisary(expire=800)

redis['k'] = 'temporary'
```

## TODO

- [x] Map Redis 'string' to Python 'str'
- [ ] Map Redis 'list' to Python 'list'
- [ ] Map Redis 'hash' to Python 'dict'
- [ ] Map Redis 'set' to Python 'set'
- [ ] Map Redis 'sorted set' to something!
