import logging


def logged(input_exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except input_exception as exception:
                if mode == "console":
                    logging.error(exception)
                elif mode == "file":
                    with open("error.txt", "a") as file:
                        if input_exception is not None:
                            file.write(str(exception) + '\n')
                else:
                    print("Use CONSOLE or FILE")

        return wrapper

    return decorator
