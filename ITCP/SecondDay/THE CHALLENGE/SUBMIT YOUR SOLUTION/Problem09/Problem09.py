a1=[-9,1,2,3,4,0,-2]
a2=[2,8,-1,4]

a3 = []

for i in range(0, len(a1)):
    for j in range(0, len(a2)):
        if a1[i] == a2[j]:
            a3.append(a1[i])

print(a3)
        