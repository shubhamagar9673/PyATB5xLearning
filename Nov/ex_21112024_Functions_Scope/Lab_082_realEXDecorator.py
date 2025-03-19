import time


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print("start_time")
        func()
        end_time = time.time()
        print("end_time")
        print("Total time take :-", end_time - start_time)


@time_decorator
def test_UI1():
    print("Add a function, time take by this function1")
    time.sleep(2)



@time_decorator
def test_UI2():
    print("Add a function, time take by this function2")
    time.sleep(5)

