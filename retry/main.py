# ЮНУСОВ ПАВЕЛ ИИАД 1

import functools
import sys

def retry(count=5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(count):
                try:
                    return func(*args, **kwargs)
                except ValueError as e:
                    last_exception = e
                    continue
                except OSError as e:
                    sys.stdout.write(f"{func.__name__} raise OsError exception.\n")
                    last_exception = e
                    continue
                except Exception as e:
                    raise e
                  
            if last_exception:
                raise last_exception
        
        return wrapper
    
    return decorator
