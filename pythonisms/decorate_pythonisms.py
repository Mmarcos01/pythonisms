from functools import wraps

def star_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'***"{orig_val}"'
    return wrapper

@star_decorator
def decorate(text):
    return text
