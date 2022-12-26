

n = int(input())


Prime = False


if n > 1:
  
    for i in range(2, n):
        if (n % i) == 0:
            
            Prime = True
            
            break


if Prime:
    print(n, "is not a prime number")
else:
    print(n, "is a prime number")