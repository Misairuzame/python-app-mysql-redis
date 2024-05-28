import redis

from loadconfig import Config

config = Config()


class Cache:
    def __init__(self):
        cache = config.get_cache_config()
        self.con = redis.Redis(
            host=cache["host"], port=cache["port"], password=cache["password"]
        )

    # get Redis connection
    def get_conn(self):
        return self.con
