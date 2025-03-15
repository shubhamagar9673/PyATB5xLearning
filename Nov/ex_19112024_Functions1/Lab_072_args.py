#we can add n number of arguments here

def print_multiple_aguments(*args):
    #  *args ->> it will returns a list
    for i in args:
        print(i)
        print_multiple_aguments("Shubham")
        print_multiple_aguments("Shubham", "omkar", "hanmant")
