import sys

n, m = map(int, input().split())
s1 = dict()
s2 = dict()

for i in range(n):
    name = input().strip()
    s1[name] = i+1
    s2[i+1] = name
    
for i in range(m):
    question = input().strip()
    try:
        print(s2[int(question)])
    except:
        print(s1[question])