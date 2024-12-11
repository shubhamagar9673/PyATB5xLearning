#Write a program to ask the user which browser he want to run automation
browser_name= input("Enter browser name:")
match browser_name:
    case "firefox":
        print("Starting Firefox!!!")
    case"chrome":
        print("Starting Chrome!!!")
    case"edge":
        print("Starting edge!!!")
    case"safari":
        print("Starting safari!!!")
    case _: #Default Case when nothing match
        print("Browser not found")
