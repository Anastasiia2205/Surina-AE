def F(N):
    if N >=2:
        for i in range(1,100000000000):
            if (N%i==0) and (i!=1):
                print(i)
                break
print(F(8))