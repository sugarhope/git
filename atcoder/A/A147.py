A1,A2,A3=map(int,input().split())
memo=A1+A2+A3
if memo>=22:
    print('bust')
else:
    print('win')