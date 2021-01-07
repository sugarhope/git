N,M=map(int,input().split())
even=0
odd=0

for i in range(0,N):
    even+=i
for j in range(0,M):
    odd+=j
print(odd+even)