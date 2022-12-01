# -- coding: utf-8 --
#def f():
#   a = [1, 2, 3 ,123]
#   print(a)
#   print(sum(a))
#   result = 1
#   for i in a:
#      result *= i
#   print(result)
#f()


def f():
   num = [3, 3, 0, 0, 0, 3, 3]
   avg= sum(num) / len(num)
   num = [avg if i == 0 else i for i in num]
   print(num)
f()
