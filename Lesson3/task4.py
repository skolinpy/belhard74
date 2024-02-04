print("Введите три числа")
a = input("число а=")
b = input("число b=")
c = input("число c=")
positive = (int(a)>0)+(int(b)>0)+(int(c)>0)
negative = (int(a)<0)+(int(b)<0)+(int(c)<0)
zero = (int(a)==0)+(int(b)==0)+(int(c)==0)
print(positive,negative,zero)

