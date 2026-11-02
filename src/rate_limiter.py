import time
from collections import deque
from functools import wraps

class RateLimiter:
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.calls = deque()

    def is_allowed(self):
        now = time.time()
        while self.calls and self.calls[0] <= now - self.period:
            self.calls.popleft()
        if len(self.calls) < self.max_calls:
            self.calls.append(now)
            return True
        return False

def rate_limit(max_calls, period):
    limiter = RateLimiter(max_calls, period)
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not limiter.is_allowed():
                raise Exception("Rate limit exceeded")
            return func(*args, **kwargs)
        return wrapper
    return decorator

class ErrorLogger:
    @staticmethod
    def log_error(endpoint, error):
        with open("error_log.txt", "a") as f:
            f.write(f"{time.ctime()} | Endpoint: {endpoint} | Error: {str(error)}\n")
