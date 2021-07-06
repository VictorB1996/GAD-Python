def decorator_with_params(param):
    def inner_decorator(f):
        def wrapper(nr):
            print("Param: ", param)
            f_result = f(nr)
            return f_result
    return inner_decorator

def my_decorator(my_function):
    def wrapper(nr):
        my_function_result = my_function(nr)
        return my_function_result ** 2
    return wrapper


@my_decorator
def f1(nr):
    return nr

import time

def execution_time(f):
    def wrapper(sequence):
        start_time = time.time()
        f_result = f(sequence)
        end_time = time.time()
        print("Execution time: ", end_time - start_time)
        return f_result
    return wrapper

@execution_time
def f1(sequence):
    r = []
    for i in sequence:
        if i % 2 == 0:
            r.append(i)
    return r

@execution_time
def f2(seq):
    return [i for i in seq if i % 2 == 0]

if __name__ == "__main__":
    x = f1(list(range(50000)))
    y = f2(list(range(10000)))