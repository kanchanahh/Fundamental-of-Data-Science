def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error: Division by zero"
    else:
        return x / y

def truncated_division(x, y):
    if y == 0:
        return "Error: Division by zero"
    else:
        return x // y

def modulus(x, y):
    if y == 0:
        return "Error: Division by zero"
    else:
        return x % y

def exponentiation(x, y):
    return x ** y

def main():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))

    print("A. Addition:", addition(x, y))
    print("B. Subtraction:", subtraction(x, y))
    print("C. Multiplication:", multiplication(x, y))
    
    if y != 0:
        print("D. Division:", division(x, y))
        print("E. Truncated division:", truncated_division(x, y))
        print("F. Modulus:", modulus(x, y))
    
    print("G. Exponentiation:", exponentiation(x, y))

if __name__ == "__main__":
    main()
