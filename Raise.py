def divide_numbers(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    
    return a / b

try:
    result = divide_numbers(10, 0)
except ZeroDivisionError as error:
    print("An error occurred:", error)
