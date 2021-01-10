N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
import numpy as np
A=np.array(A)
B=np.array(B)
C=np.dot(A,B)
if C==0:
    print('Yes')
else:
    print('No')