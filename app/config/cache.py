"""This module is settings for cache"""

CacheConfig = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 60,
    'CACHE_KEY_PREFIX': 'movies_collector',
    'CACHE_REDIS_HOST': 'localhost',
    'CACHE_REDIS_PORT': '6379',
    'CACHE_REDIS_DB': '0',
    'CACHE_REDIS_PASSWORD': None
}
