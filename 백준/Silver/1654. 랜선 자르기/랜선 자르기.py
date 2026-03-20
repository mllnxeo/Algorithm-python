k, n = map(int, input().split())
array = []

for i in range(k):
    a = int(input())
    array.append(a)

start = 1
end = max(array) 

while start <= end:
    mid = (start + end) // 2
    lines = 0

    for i in array:
        lines += i//mid

    if lines >= n:
        start = mid + 1
    else :
        end = mid-1
print(end)