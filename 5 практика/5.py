def F(n):
    a = []
    for i in range(10000000000):
        s = input()
        if s!=n:
            a = a.append(s)
        if s==0:
            print(len(a))
            break
print(F(0))