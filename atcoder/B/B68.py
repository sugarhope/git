def aaa(i,count):
    if i%2==0:
        count+=1
        i=int(i/2)
        return aaa(i,count)
    if i%2==1:
        return count

if __name__ == '__main__':
    import numpy as np
    N = int(input())
    AA=[]
    temp=0
    BB={}
    for i in range(1,N+1):
        temp=i
        count=aaa(i,0)
        AA.append([temp,count])
    for j in AA:
        BB[j[1]]=j[0]
    a=max(list(BB.keys()))
    print(BB[a])