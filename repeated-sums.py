number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))
counter = 1
result = number1 * number2

while(counter <= number2):
  if(counter == number2):
    print(f'{number1} = {result}')
    break
  print(f'{number1} +', end=" ")
  counter += 1

