a = 1
b = 1
print(a)
print(b)

for i in range(100):
    temp = a
    a = b
    b = temp + b
    print(b)