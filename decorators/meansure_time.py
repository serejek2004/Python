"""
    Import time
"""
import time


def measure_time(function):
    """
    :param function: *args **kwargs
    :return: wrapper
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        result_time = end_time - start_time
        print(f"Time done {function.__name__} is - {result_time*1000:.3f} mSecond")
        return result

    return wrapper
