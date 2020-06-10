import datetime


def log_with_path(path):
    def logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='cp1251') as f:
                time_now = datetime.datetime.now()
                f.write(f'{time_now.strftime("%Y-%m-%d.%H:%M:%S")} \n')
                f.write(f'func name - {old_function.__name__} \n')
                f.write(f'args - {args}, kwargs - {kwargs} \n')
                f.write(f'result - {result} \n \n')

            return result
        return new_function
    return logger

