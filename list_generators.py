numbers = [1, 2, 3, 4, 5, 6, 7, 8, 100]
result = []
for number in numbers:
    if number > 5 and number < 50:
        result.append(number)
print(result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 100]
result = filter(lambda number:number > 5 and number < 50, numbers)
print(list(result))


number = [7, 8, 100, 200, 300]
result1 = [number for number in number if number > 5 and number < 50]
print(result1)

names = ['leo', 'max', 'bob', 'bib']
names1 = []
for i in names:
    names1.append(i.upper())
print(names1)

names = ['leo', 'max', 'memЪ', 'bib']
names1 = []
for i in names:
    if 'm' in i[0]:
        names1.append(i)
print(names1)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 100]
result = []
for number in numbers:
    if number > 5:
        result.append(1)
    else:
        result.append(0)
print(result)

result012 = {i:i**2 for i in range(1,10)}
print(result012)
