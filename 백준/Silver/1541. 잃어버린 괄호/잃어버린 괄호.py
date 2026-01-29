data = input()
data_m = data.split('-')
result = sum(map(int, data_m[0].split('+')))
a = 0
# print(result)

for i in range(1, len(data_m)):
    a = sum(map(int, data_m[i].split('+'))) 
    result -= a

print(result)