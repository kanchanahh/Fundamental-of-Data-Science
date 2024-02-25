my_numbers = [7,2,4,11,19,24,66,1,42,22,37,5,3,92,73]

input_str = input("Enter 'even' or 'odd': ").lower()

if input_str == 'even':
    print("Even numbers:")
    for num in my_numbers:
        if num % 2 == 0:
            print(num)
elif input_str == 'odd':
    print("Odd numbers:")
    for num in my_numbers:
        if num % 2 != 0:
            print(num)
else:
    print("Unknown Input!")