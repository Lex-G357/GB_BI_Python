# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000
# (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится
# нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму,
# так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать
# только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел
# из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.
#

x = 1
ten = 10
hund = ten ** 2
thous = ten ** 3
ten_thous = ten ** 4
hund_thous = ten ** 5
all_sum = 0

while x % 2 and x < 1000:
    # print('Степень', x ** 3)
    degree = x ** 3
    sum_degree = (degree // hund_thous +
                  degree % hund_thous // ten_thous +
                  degree % hund_thous % ten_thous // thous +
                  degree % hund_thous % ten_thous % thous // hund +
                  degree % hund_thous % ten_thous % thous % hund // ten +
                  degree % ten)
    # print('Сумма', sum_degree)
    if not sum_degree % 7:
        all_sum = all_sum + sum_degree
    # else:
        # print(all_sum )
    x = x + 2
print(all_sum)
