price_tickets_1 = 0
price_tickets_2 = 990
price_tickets_3 = 1390
all_price = 0
tickets = int(input('Введите количество билетов'))
if tickets <= 0:
    print('Введите число больше 0')
for i in range(tickets):
    age = int(input('Введите возраст посетителя в билете'))
    if age < 18 and age > 0:
        all_price += price_tickets_1
        print('Стоимость билетов', all_price, 'руб.')
    elif age >= 18 and age < 25:
        all_price += price_tickets_2
        print('Стоимость билетов', all_price, 'руб.')
    elif age >= 25:
        all_price += price_tickets_3
        print('Стоимость билетов', all_price, 'руб.')
    else:
        print('Введите корректный возраст')
if tickets > 3:
    all_price *= 0.9
    print('Ваша стоимость билетов со скидкой составила', all_price)