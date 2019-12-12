import config
import redis


class AppsRedis:
    """各应用redis"""

    def get_redis(self, port: str):
        """返回对应端口应用的redis"""
        pool = redis.ConnectionPool(host=config.REDIS_HOST, port=config.REDIS_PORT, db=config.AppsRedisConfig[port],
                                    decode_responses=True)
        return redis.StrictRedis(connection_pool=pool)
