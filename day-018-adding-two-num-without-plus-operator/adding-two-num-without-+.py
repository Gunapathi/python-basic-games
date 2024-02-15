x = 20
y = 30
while y != 0:
    temp = x & y
    x = x ^ y
    y = temp << 1

print(x)

