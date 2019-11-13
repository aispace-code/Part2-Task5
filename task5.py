a = int(input('Number of students '))
b = int(input('Number of students2 '))
c = int(input('Number of students3 '))
print('This much desks we will need to purchase ', a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)