import datetime

day = int(input('Digite o dia em que você nasceu: '))
month = int(input('Digite o mês em que você nasceu: '))
year = int(input('Digite o ano em que você nasceu: '))

today = datetime.date.today()
age = today.year - int(year)

months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def monthName(number):
  return months[number - 1]


print(f'Você nasceu no dia {day} de {monthName(month)} de {year} e você tem {age} anos.')