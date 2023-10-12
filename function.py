#Switch case method
def this():
    print("I am doing this")

def that():
    print("I am doing that")


match input("Inter this/that:"):
    case 'this':
        this()
    case 'that':
        that()
    case _:
        print("Invalid syntex")


