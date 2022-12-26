a=[10,8,7,6,6,0,-1]

Croissante = True
Decroissante = True

for i in range(0, len(a) -1):
    if a[i] < a[i+1]:
        Decroissante = False    

for i in range(0, len(a) -1):
    
    if a[i] > a[i+1]:
        Croissante = False

if Croissante or Decroissante:
    print("Monotonne")
else:
    print("NON MONOTONE")
        