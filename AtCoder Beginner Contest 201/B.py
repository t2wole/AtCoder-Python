lst = []

for i in range(int(input())):
    name, height = input().split()
    lst.append([int(height), name])
lst.sort()
print(lst[-2][1])