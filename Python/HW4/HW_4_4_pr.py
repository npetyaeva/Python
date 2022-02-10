# Задача №4
# Обменник. Скрипт запускается в консоли и работает постоянно. Остановится нажатием ctrl+c.
#     1. Скрипт сначала выводит "Выберите валюту из ['USD','EUR','CHF','GBP','CNY']"
#     2. Пользователь вводит один из 5 вариантов ['USD','EUR','CHF','GBP','CNY']
#     3. Потом Скрипт выводит "Введите сумму"
#     4. Пользователь вводит сумму int
#     5. Скрипт выводит:
#             "Вы ввели сумму int и валюту "Валюта" "
#             "конвертированная сумма в "Валюта" = int"
#     6. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#     7. После сообщеня об ошибке, скрипт должен автоматом вернуться к шагу 1.
#     8. Валюту пользователя определите сами.
import sys
import keyboard

status = True


def stop():
    global status
    status = False
    print("Работа завершена")


keyboard.add_hotkey('ctrl+c', stop)
currency_rates = {'usdrub': 0.013, 'eurrub': 0.011, 'uahrub': 0.37, 'chfrub': 0.012, 'bynrub': 0.03,
                  'rubusd': 74.8, 'eurusd': 0.87, 'uahusd': 27.98, 'chfusd': 0.92, 'bynusd': 2.56,
                  'usdeur': 1.14, 'rubeur': 85.38, 'uaheur': 31.94, 'chfeur': 1.06, 'byneur': 2.92,
                  'usduah': 0.035, 'rubuah': 2.67, 'euruah': 0.031, 'chfuah': 0.033, 'bynuah': 0.09,
                  'usdchf': 1.08, 'rubchf': 80.98, 'eurchf': 0.94, 'uahchf': 30.29, 'bynchf': 2.77,
                  'usdbyn': 0.39, 'rubbyn': 29.15, 'eurbyn': 0.34, 'uahbyn': 10.93, 'chfbyn': 0.36,
                  }
while True:
    if status:
        print('Выберите валюту из USD, EUR, CHF, RUB, UAH, BYN')
        currency = input().lower().strip()
        print('Введите сумму: ')
        amount = input().strip()
        if amount == "":
            print('Вы ввели пустое поле. Введите число.')
        else:
            try:
                if float(amount) <= 0:
                    print('Введите положительное число.')
                elif float(amount) * 100 % 100 != 0:
                    print('Вы ввели не целое число.')
                else:
                    print('Ты ввёл', amount, currency.upper())
                    for i, j in currency_rates.items():
                        if i[3:] == currency:
                            print('конвертированная сумма в', i[:3].upper(), '=', round(int(amount) * j, 2), i[:3].upper())
            except ValueError:
                print('Вы ввели не число. Введите число.')
        print()
    else:
        sys.exit(0)
