def F(a, b, c): 
 if (a > b) and (c > b):
 print(b)
 if (b > a) and (c > a):
 print(a)
 if (b > c) and (a > c):
 print(c)
print(F(1,6,-5))