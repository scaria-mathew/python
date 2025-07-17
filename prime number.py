# Prime Number

n = int(input("Enter a number: "))

for i in range(1,n):
    if n == 2:
        print("prime")

    if n % i == 0:
        print("Not prime")
 
    else: 
        print("prime")
    break

