age = int(input("Digite sua idade: "))

if(age < 5):
  print('Idade sem classificação')
if(age >= 5 and age <= 7):
  print('Infantil A')
if(age >= 8 and age <= 10):
  print('Infantil B')
if(age >= 11 and age <= 13):
  print('Juvenil A')
if(age >= 14 and age <= 17):
  print('Juvenil B')
if(age >= 18):
  print('Adulto')