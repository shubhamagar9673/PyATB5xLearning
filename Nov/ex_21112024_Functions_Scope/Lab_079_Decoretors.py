def add_extra_security(func):

    def wrapper():
        print("1.Before the function is called.")
        print("2.Add helmet, Dashcam, gloves, guards, license")
        func()  #driving_scooty
        print("3.After the function is called")
        print("4.Secure driving, Leave all the items")
    return wrapper()

@add_extra_security
def drive_ola_scooty():
    print("ola")


@add_extra_security
def drive_scooty():
    print("Normal Function..!")
    print("I am driving a scooty")
