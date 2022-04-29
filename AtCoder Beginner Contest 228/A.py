s, t, x = map(int, input().split())

if s <= t:
    if s <= x < t:
        print("Yes")
    else:
        print("No")
else:
    if 0 <= x < t:
        print("Yes")
    elif s <= x:
        print("Yes")
    else:
        print("No")
        