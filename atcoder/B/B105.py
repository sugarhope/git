N=int(input())
anses=[]
for n in range(26):
    for m in range(15):
        ans=4*n+7*m
        if ans<=100:
            anses.append(ans)
anses=set(anses)
if N in anses:
    print('Yes')
else:
    print('No')