n = int(input())
a = list(map(int, input().split()))
count = [0] * 200
result = 0

for i in range(n):
    count[a[i] % 200] += 1

for j in count:
    result += (j * (j - 1)) // 2

print(result)
