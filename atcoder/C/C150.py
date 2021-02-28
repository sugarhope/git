import itertools
N=int(input())
P=tuple(map(str,input().split()))
Q=tuple(map(str,input().split()))

seq=[str(i) for i in range(1,N+1)]
perm=list(itertools.permutations((seq)))

a=perm.index(P)+1
b=perm.index(Q)+1

ans=abs(a-b)
print(ans)