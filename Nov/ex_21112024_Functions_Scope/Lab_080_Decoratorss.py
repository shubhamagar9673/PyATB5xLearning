def add_before_UI_after_UI(func):
    def wrapper():
        print("Before running UI TC")
        print("Start the browser")
        func()
        print("after running UI TC")
        print("Quite the browser")

    return wrapper()


@add_before_UI_after_UI
def test_API():
    print("I will test API")
