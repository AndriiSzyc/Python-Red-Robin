# 1. double_result
# This decorator function should return the result of another function multiplied by two
def double_result(func):
    # return function result multiplied by two
    def wrapper(*args, **kwargs):
        amount = func(*args, **kwargs)
        return amount * 2
    return wrapper

def add(a, b):
    return a + b

add(5, 5)  # 10
print(add(5, 5))

@double_result
def add(a, b):
    return a + b

add(5, 5)  # 20
print(add(5, 5),'\n')

# 2. only_odd_parameters
# This decorator function should only allow a function to have odd numbers as parameters,
# otherwise, return the string "Please use only odd numbers!"

def only_odd_parameters(func):
    # if args passed to func are not odd - return "Please use only odd numbers!"
    def wrapper(*args):
        odd_parameters = []
        for i in args:
            if i % 2 != 0:
                odd_parameters.append(i)
        if len(args) == len(odd_parameters):
            amount = func(*args)
        else:
            raise Exception('Please use only odd numbers!')
        return amount
    return wrapper


@only_odd_parameters
def add(a, b):
    return a + b


print(add(5, 5)) # 10

#print(add(4, 4))  # "Please use only odd numbers!"


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e

#print(multiply(4, 5, 6, 7, 9))
print(multiply(1, 3, 5, 7, 9),'\n')
#
#
# 3.* logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):

def logged(func):
    # log function arguments and its return value
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if len(args) != 0:
            with open('logfile', 'a') as log_file:
                log_file.write(f'\nYou have *args {args} parameters. And result function {res if isinstance(res, int) else res[0]}')
        if len(kwargs) != 0:
            with open('logfile', 'a') as log_file:
                log_file.write(f'\nYou have **kwargs {kwargs} parameters. And result function {res if isinstance(res, int) else res[1]}')
        return func(*args, **kwargs)
    return wrapper

@logged
def func(*args, **kwargs):
    if len(args) != 0 and len(kwargs) != 0:
        return 3 + len(args), 3 + len(kwargs)
    elif len(args) == 0:
        return 3 + len(kwargs)
    else:
        return 3 + len(args)


#print(func(1, 2, 'stop', a='stop', b=['one', 33, 'cool']))


# you called func(4, 4, 4)
# it returned 6


# 4. type_check
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.

def type_check(correct_type):
    # put code here
    def decorator(func):
        def wrapper(args):
            if isinstance(args, correct_type):
                amount = func(args)
                return amount
            else:
                raise Exception(f"Wrong Type: {type(args)}")
        return wrapper
    return decorator

@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
#print(times2('Not A Number'))  # "Wrong Type: string" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))  # "Wrong Type: list" should be printed, since non-str passed to decorated function