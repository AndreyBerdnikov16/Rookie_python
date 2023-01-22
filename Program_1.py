per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму для расчета доходности по вкладам:'))/10
if money >= 10:
    deposit = [per_cent['ТКБ'] * money,
               per_cent['СКБ'] * money,
               per_cent['ВТБ'] * money,
               per_cent['СБЕР'] * money]
    deposit_max = list(map(int, deposit))
    print('Максимальная сумма, которую вы можете заработать —', (sorted(deposit_max)[-1]))
else:
    print('Недостаточно средств для открытия вклада')