years = int(input('Digite o número de anos: '))
months = int(input('Digite o número de meses: '))
days = int(input('Digite o número de dias: '))

totalDays = (years * 365) + (months * 30) + days

print(f'{totalDays} dias')