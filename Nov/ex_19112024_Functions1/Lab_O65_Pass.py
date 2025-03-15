def first_part_last_name():
    pass # Here pass   means Do nothing but in future I will complete this function

def greet_to_all_of_you():
    print("Hello Everyone!!")

def greet():
    print("Yes")
    greet_to_all_of_you()  # this is function within function
    greet()

    greet_to_all_of_you()
    first_part_last_name()