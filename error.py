a = 0
b = 1

for i in range(1000):
    tmp = a + b
    a = b
    b = tmp

print(a)