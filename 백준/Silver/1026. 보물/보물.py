n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

array = []
a.sort(reverse = True)
b.sort()
tmp = 0

for i in range(n):
    tmp += (a[i] * b[i])
print(tmp)