# 4. Дан список, содержащий искажённые данные с должностями
# и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
# 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
#
# Известно, что имя сотрудника всегда в конце строки. Сформировать
# и вывести на экран фразы вида: 'Привет, Игорь!'
# Подумать, как получить имена сотрудников из элементов списка, как
# привести их к корректному виду. Можно ли при
# этом не создавать новый список?
#

a = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

a = ' '.join(a).capitalize()
a = a.split()
print(a)
a[1] = a[1].capitalize()
a[4] = a[4].capitalize()
a[8] = a[8].capitalize()
a[10] = a[10].capitalize()
print('Привет,', a[1], '!')
print('Привет,', a[4], '!')
print('Привет,', a[8], '!')
print('Привет,', a[10], '!')
