# 1. Реализовать вывод информации о промежутке времени в зависимости
# от его продолжительности duration в секундах: до минуты: <s> сек;
# до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
#

duration = int(input("Введите секунды >>> "))

minute = 60
hour = minute * 60
day = hour * 24

if duration < minute:
    print(duration, " сек.")
elif duration < hour:
    print(duration // minute, " мин. ", duration % minute, " сек.")
elif duration < day:
    print(duration // hour, " час.", duration % hour // minute, " мин. ", duration % minute, " сек.")
else:
    print(duration // day, "дн.", duration % day // hour, " час.", duration % hour // minute, " мин. ",
          duration % minute, " сек.")


