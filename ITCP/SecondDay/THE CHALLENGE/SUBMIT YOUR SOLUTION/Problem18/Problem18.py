n = int(input())
import math
save = n


def primefactors(n):

    factors =[]
    while n % 2 == 0:
      factors.append(2)
      n = n / 2  

    for i in range(3,int(math.sqrt(n))+1,2):
     
        while (n % i == 0):
            factors.append(i)
            n = n / i
    
    if n > 2:
        factors.append(int(n))

    return factors 


Ugly = True
for j in range(0, len(primefactors(n))):
    if (primefactors(n)[j] != 2) and (primefactors(n)[j] != 3) and (primefactors(n)[j] != 5):
        Ugly = False

if Ugly:
    print(save, ' Ugly')
else:
    print(save, ' Not Ugly')




    