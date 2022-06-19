from datetime import datetime

from redis import Redis

from app import redis
from app.config.settings import settings


class RateLimitService:
    def __init__(
        self,
        redis: Redis,
        bucket_size: int = settings.DDOS_NUMBER_OF_REQUEST,
        time_period: int = settings.DDOS_TIME_PERIOD,
    ) -> None:
        self.redis = redis
        self.bucket_size = bucket_size
        self.time_period = time_period

    def check(self, key) -> bool:
        pipe = self.redis.pipeline()
        now = datetime.now()
        key = f"{key}:{now.minute}"
        pipe.incr(key, 1)
        pipe.expire(key, self.time_period)
        result = pipe.execute()
        request_number = result[0]

        if request_number <= self.bucket_size:
            return True
        return False


def get_ratelimit_service() -> RateLimitService:
    return RateLimitService(redis)
