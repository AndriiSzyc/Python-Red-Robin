from datetime import datetime


def timer(func_name: str = 'Function'):
    def decorator(function):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = function(*args, **kwargs)
            end = datetime.now()
            print(
                'Function {func} execution time: {time.seconds}s, {time.microseconds}ms.'.format(func=func_name,
                time=end - start
                )
            )
            return result
        return wrapper
    return decorator