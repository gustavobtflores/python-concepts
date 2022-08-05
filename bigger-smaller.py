number1 = float(input('Digite o primeiro número: '))
number2 = float(input('Digite o segundo número: '))
number3 = float(input('Digite o terceiro número: '))

if(number1 > number2 and number1 > number3):
  print(f'O maior número é: {number1}')
elif(number2 > number1 and number2 > number3):
  print(f'O maior número é: {number2}')
else:
  print(f'O maior número é: {number3}')

if(number1 < number2 and number1 < number3):
  print(f'O menor número é: {number1}')
elif(number2 < number1 and number2 < number3):
  print(f'O menor número é: {number2}')
else:
  print(f'O menor número é: {number3}')

