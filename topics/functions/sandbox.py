import time


# DECORATOR EXAMPLE

def print_hello_when_called(func):

    def wrapper(*args, **kwargs):
        time_start = time.time()
        result_f = func(*args, **kwargs)
        print('Exc time:', time.time() - time_start)
        return result_f
    return wrapper

@print_hello_when_called
def sum(a, b):
    return a + b


print(sum(10, 10))