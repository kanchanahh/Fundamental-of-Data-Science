number=int(input("ENter a number:"))

fact=1

a=1

while a<=number:
    fact=fact*a
    a=a+1

print("The factorial of", number, "is", fact)