count1=0
count2=0
temp=0
N=int(input())
for i in range(1,N+1,2):
    for j in range(1,N+1,2):
        if i%j==0:
           count1+=1
    if count1==8:
       count2+=1
    count1=0
print(count2)