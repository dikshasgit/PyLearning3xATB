# Decorators

def my_decorator(func):
    def wrapper():
        print("Starting........")
        print("******************")
        func()
        print("******************")
        print("Starting........")

    return wrapper()


#my_decorator  # without this decorator won't work
def say_hello():
    print("Hello")

    # Decorator

    import time

    def my_decorator(func):
        def wrapper():
            start_time = time.time()
            func()
            end_time = time.time()
            print("Time taken = " + str(end_time - start_time))

        return wrapper()

    #my_decorator
    def time_logs():
        time.sleep(5)
        print("Log 1 time taken")

    #my_decorator
    def time_logs1():
        time.sleep(3)
        print("Log 2 time taken")