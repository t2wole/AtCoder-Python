s = input()

a = s[0]
b = s[1]
c = s[2]

if a == b == c:
    print('1')
elif a != b and b != c and c != a:
    print('6')
else:
    print('3')


