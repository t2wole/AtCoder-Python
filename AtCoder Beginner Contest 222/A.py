n = int(input())

if n < 10:
    print('000', n, sep="")
elif n < 100:
    print('00', n, sep="")
elif n < 1000:
    print('0', n, sep="")
elif n < 10000:
    print(n)
