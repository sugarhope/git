A,B,C=map(int,input().split())
if C==0:
    for i in range(max(A,B)+1):
        A=A-1
        if A==-1:
            print('Aoki')
            exit()
        B=B-1
        if B==-1:
            print('Takahashi')
            exit()

if C==1:
    for i in range(max(A,B)+1):
        B=B-1
        if B==-1:
            print('Takahashi')
            exit()
        A=A-1
        if A==-1:
            print('Aoki')
            exit()