#Prime Number

n = int(input("Enter a number: "))

if n <= 1:
    print("Not prime")
elif n == 2:
    print("Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")
