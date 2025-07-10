print("Enter 1 -> C to F")
print("Enter 2 -> C to K")

opt = int(input("Option: "))

if opt == 1:
    cel = int(input("Value: "))
    fah = 9/5 * cel + 32
    print("Fahrenheit: ", fah)
if opt == 2: 
    cel = int(input("Value: "))
    kel = cel + 273.15
    print("Celsius: ", kel)
if opt > 2 or opt < 1: 
    print("Invalid Option")

