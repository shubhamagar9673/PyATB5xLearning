public_toilet = "PB"


def home():
    private_toilet = "PT"
    print(public_toilet)  # this is within the scope as this is a global variable
    print(private_toilet)
    home()


def stranger():
    print(public_toilet)  # this is in scope as this is a global variable
    # print(private_toilet)   this will give error as this is not in scope of this function


stranger()

# print(public_toilet)
