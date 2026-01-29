n, k = map(int, input().split())
array = []
count = 0

for _ in range(n):
    coin = int(input())
    array.append(coin)

array.sort(reverse = True)

for i in range(len(array)):
    if k < array[i] :
        continue
    else :
        k // array[i]  # 몫
        count += (k // array[i])
        k = k % array[i] # 나머지

print(count)