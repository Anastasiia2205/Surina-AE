def F(a): #a=0#
    b = -1
    while True:
        n = int(input())
        a = a + n
        b = b + 1
        if n == 0:
            break
    print(a/b)
print(F(a))