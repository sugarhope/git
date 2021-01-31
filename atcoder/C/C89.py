N=int(input())
S=[tuple(map(str,input().split())) for _ in range(N)]
MARCH=tuple('MARCH')

import itertools
count=0

for name in itertools.combinations(S,3):
    temp=0
    n=[]
    for i in range(0,3):
        if name[i][0][0] in MARCH and name[i][0][0] not in n:
            n.append(name[i][0][0])
            temp+=1
        if temp==3:
            count+=1
print(count)