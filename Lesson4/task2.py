text=input("введите текст:")
dict1={n:text.count(n) for n in text}
print(dict1)
# print(dict1) #{'как посчитать количество вхождений каждой буквы в текст введенный с клавиатуры'}
