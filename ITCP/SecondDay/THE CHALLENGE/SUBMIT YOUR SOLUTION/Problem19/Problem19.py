
n = int(input())

def get_divisors(n):
    Divisors = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            Divisors.append(i)
    return(Divisors)

sum = 0
for i in range(0, len(get_divisors(n))):
    sum = sum + get_divisors(n)[i]


if (sum == n):
    print(n, " Is a perfect number")
else:
    print(n, " Is not a perfect number")

    

