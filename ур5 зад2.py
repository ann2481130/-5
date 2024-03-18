s = input('Введите слово из маленьких латинских букв:')
vowels = 0
consonants = 0
print('Количество букв а:')
count = sum(1 for letter in s if letter == 'a')
if count != 0:
 print(count)
else:
  print('False')
print('Количество букв е:')
count = sum(1 for letter in s if letter == 'e')
if count != 0:
  print(count)
else:
  print('False')
print('Количество букв i:')
count = sum(1 for letter in s if letter == 'i')
if count !=0:
  print(count)
else:
 print('False')
print('Количество букв o:')
count = sum(1 for letter in s if letter == 'o')
if count != 0:
  print(count)
else:
 print('False')
print('Количество букв u:')
count = sum(1 for letter in s if letter == 'u')
if count != 0:
  print(count)
else:
  print('False')
for letter in s:
    if  letter in 'aeiou':
     vowels += 1
    else:
     consonants += 1
print('Количество гласных букв:', vowels)
print('Количество согласных букв:', consonants)

