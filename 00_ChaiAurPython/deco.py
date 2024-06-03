# import time
# #Problem: Write a decorator that measures the time a function takes to execute.
# def tenzin(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} ran in {end-start} time")
#         return result
#     return wrapper


# @tenzin #here we are saying that the function below should execute only after the tenzin is done
# def example_function(n):
#     time.sleep(n)

# example_function(2)

#Create a decorator to print the function name and the values of its arguments every time the function is called.
# def debug(func):
#     def wrapper(*args, **kwargs):
#         args_value = ', '.join(str(arg) for arg in args)
#         kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.
#         items())
#         print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
#         return func(*args, **kwargs)
#     return wrapper

# @debug
# def hello():
#     print("hello")

# @debug
# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}")

# hello()
# greet("chai", greeting="hanji ")


#Implement a decorator that caches the return values of a function, so that when it's called with 
#the same arguments, the cached value is returned instead of re-executing the function.

import time
def cache(func):
    cache_value={} #object as easier to access compare to an array
    print(cache_value)
    def wrapper(*arg):
        print(f'i am arguemnt that come {arg}')
        if arg in cache_value:
            return cache_value[arg] #use in second call of the function below
        result=func(*arg) #execute the function
        cache_value[arg]=result #adding in cache
        return result
    return wrapper

#this function will go through the decorator function 
@cache
def longrunfunc(a,b):
    time.sleep(2)
    return a+b

print(longrunfunc(2,3))
print(longrunfunc(2,3)) #this will come fast as it is in cache
print(longrunfunc(1,3)) #will take time to compute