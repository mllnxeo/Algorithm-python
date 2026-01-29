a, b = map(int, input().split())
count = 1

while b!=a:
    if b % 2 == 0:
        count += 1
        b //= 2
    elif b % 10 == 1 :
        count += 1
        b = b//10
    else :
        print(-1)
        break
    if b < a:
        print(-1)
        break
else : 
    print(count)