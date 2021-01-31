N=int(input())
S=str(input())

import itertools

print(S)
passw=set(itertools.combinations(S,3))
#print(passw)
print(len(passw))