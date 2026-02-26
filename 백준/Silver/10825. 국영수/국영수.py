n = int(input())
student = []
for i in range(n):
    a = input().split()
    student.append((a[0], int(a[1]), int(a[2]), int(a[3])))

student.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))

for s in student:
    print(s[0])