

"This program takes an any type of input and then prints its type  "


user_input = input("Enter something: ")

# Try int first
try:
    value_int = int(user_input)
    print("Type: int")
    print("Value:", value_int)

except ValueError:
    # Not an int, try float
    try:
        value_float = float(user_input)
        print("Type: float")
        print("Value:", value_float)

    except ValueError:
        # Not int, not float → treat as string
        print("Type: str")
        print("Value:", user_input)









