def F(x): #7#
 if (x%4==0) and (x%100!=0) and (x%400==0):
 print("Да")
 else:
 print("Нет")
        
print(F(2022))