pb_global_b = 12   #Global variable


def my_function():
    pb_a = 10    # local variable within the function
    print(pb_a)
    print(pb_global_b)
    my_function()
