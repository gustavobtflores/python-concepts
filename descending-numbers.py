number1 = float(input('Digite o primeiro número: '))
number2 = float(input('Digite o segundo número: '))
number3 = float(input('Digite o terceiro número: '))

if(number1 > number2 and number1 > number3):
  print(number1)

  if(number2 > number3):
    print(f'{number2}\n{number3}')
  else:
    print(f'{number3}\n{number2}')
elif(number2 > number1 and number2 > number3):
  print(number2)

  if(number1 > number3):
    print(f'{number1}\n{number3}')
  else:
    print(f'{number3}\n{number1}')
else: 
  print(number3)

  if(number1 > number2):
    print(f'{number1}\n{number3}')
  else: 
    print(f'{number2}\n{number1}')
