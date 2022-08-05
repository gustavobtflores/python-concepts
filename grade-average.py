grade1 = float(input('Digite a sua primera nota: '))
grade2 = float(input('Digite a sua segunda nota: '))
average = (grade1 + grade2)/2

if(average == 10):
  print('Aluno aprovado com distinção')
elif(average >= 7):
  print('Aluno aprovado')
else:
  print('Aluno reprovado')

print(f'Média final: {average}')