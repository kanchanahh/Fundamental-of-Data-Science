def temperature(temp):
   fahrenheit= (temp *  9 / 5 ) + 32
   return fahrenheit

temp=float(input("Enter the Celsius temperature:"))
x=temperature(temp)

print("The fahrenheit temperature of the given Celsius temperature is:",x,"f")