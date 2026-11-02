import time
import logging
from functools import wraps
from flask import request, jsonify

# Configure structured logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('stripe_webhook_monitor')

# Simple in-memory rate limiter
rate_limit_store = {}

def rate_limit(limit=5, window=60):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            client_ip = request.remote_addr
            current_time = time.time()
            
            if client_ip not in rate_limit_store:
                rate_limit_store[client_ip] = []
            
            # Filter timestamps within the window
            rate_limit_store[client_ip] = [t for t in rate_limit_store[client_ip] if current_time - t < window]
            
            if len(rate_limit_store[client_ip]) >= limit:
                logger.warning(f"Rate limit exceeded for IP: {client_ip}")
                return jsonify({"error": "Too many requests"}), 429
            
            rate_limit_store[client_ip].append(current_time)
            return f(*args, **kwargs)
        return wrapped
    return decorator

def log_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {str(e)}", exc_info=True)
            return jsonify({"error": "Internal server error"}), 500
    return wrapper