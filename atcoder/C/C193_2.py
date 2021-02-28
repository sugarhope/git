import math
N=int(input())

root=int(N**0.5)
temp=0
ab=set()

for i in range(2,root+1):
    temp=i*i
    while temp<=N:
        ab.add(temp)
        temp*=i

print(N-len(ab))
