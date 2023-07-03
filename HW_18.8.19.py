tickets = int(input('Введите количество приобретаемых билетов: '))
counter = 0
for i in range(tickets):
    age = int(input('Введите возраст посетителя: '))
    if age <= 17:
        counter += 0
    elif 18 <= age <= 24:
        counter += 990
    elif age >= 25:
        counter += 1390
if tickets >= 3:
    counter = counter * 0.90
print('Общая сумма к оплате:', int(counter))