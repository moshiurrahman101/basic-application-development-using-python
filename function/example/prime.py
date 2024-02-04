n = int(input("Enter your number:"))

isPrime = True

for i in range(2, n):
    if n % i == 0:
        isPrime = False
        break
    
if isPrime == True:
    print("Prime number")
else:
    print("Not prime")
    
    