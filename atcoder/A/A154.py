S,T=map(str,input().split())
A,B=map(int,input().split())
U=str(input())

if U==S:
    A-=1
if U==T:
    B-=1
print(A,B)