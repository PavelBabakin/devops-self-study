from timing_decorator import time_it
import time

@time_it
def some_function():
    # Some time-consuming operations
    time.sleep(2)
    print("Function executed!")

some_function()