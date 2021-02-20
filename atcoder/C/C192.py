N,K=map(int,input().split())

g2_0 = int(''.join(sorted(str(N))))
g1_0 = int(''.join(sorted(str(N), reverse = True)))
n=g1_0-g2_0

def fx(n):
    g2 = int(''.join(sorted(str(n))))
    g1 = int(''.join(sorted(str(n), reverse=True)))
    n = g1 - g2

    return n

if K==0:
    n=N

elif K==1:
    pass

else:
    while K >1:
        K-=1
        n = fx(n)

print(n)