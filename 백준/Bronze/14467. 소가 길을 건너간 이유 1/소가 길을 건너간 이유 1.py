k = int(input())
cnt = 0
array = {}

for i in range(k):
    cow, load = map(int, input().split())

    if cow in array :
        if array[cow] != load :
            cnt += 1
    array[cow] = load
print(cnt)