utf_value = int(input("Enter a UTF-8 value between 32 and 126: "))

if 32 <= utf_value <= 126:
    character = chr(utf_value)
    print("Corresponding character:", character)
else:
    print("Invalid input. Please enter a value between 32 and 126.")
