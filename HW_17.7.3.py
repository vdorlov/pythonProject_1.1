money = input('Сумма, которую Вы планируете положить под процент - ')
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

deposit = []

bank_1 = round(int(money)*(per_cent['ТКБ']/100))
deposit.append(bank_1)

bank_2 = round(int(money)*(per_cent['СКБ']/100))
deposit.append(bank_2)

bank_3 = round(int(money)*(per_cent['ВТБ']/100))
deposit.append(bank_3)

bank_4 = round(int(money)*(per_cent['СБЕР']/100))
deposit.append(bank_4)

print('ТКБ:', deposit[0], '\n'
      'СКБ:', deposit[1], '\n'
      'ВТБ:', deposit[2], '\n'
      'СБЕР:', deposit[3])

max_deposit = max(deposit)

print('Максимальная сумма, которую Вы можете заработать —', max_deposit)