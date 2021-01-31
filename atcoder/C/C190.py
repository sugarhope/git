N,M=map(int,input().split())
AB=[tuple(map(int,input().split())) for _ in range(M)]
K=int(input())
CD=[tuple(map(int,input().split())) for __ in range(K)]

import itertools
count=0
counts=[]

for ball in itertools.product(*CD,repeat=1):
    for i,j in AB:
        if i in ball and j in ball:
            count+=1
    counts.append(count)
    count=0
print(max(counts))
