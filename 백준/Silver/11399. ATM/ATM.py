n = int(input())
array = list(map(int, input().split()))
array.sort()

tmp = 0
a_list = []

for i in range(n):
    tmp += array[i] 
    a_list.append(tmp)

print(sum(a_list))