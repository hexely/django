from datetime import date
import csv
# дата окончания
time_out = date(2024, 2, 24)


def deposit(deposit_, note):

    # сегодняшняя дата
    today = date.today()
    # кол-во дней между датами
    days_left = (time_out - today).days
    # Сумма после вычета депозита нужна для расчета суммы внесения в день
    total_amount = 200000 - deposit_
    # сумма в день
    amount_per_day = total_amount / days_left

    try:
        with open('data.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # Проходимся по строкам и читаем данные в формате словаря
            for row in reader:
                last_row = row
            if last_row:
                print(last_row['Осталось'])

        total_amount = int(last_row['Осталось']) - deposit_
        amount_per_day = total_amount / days_left

    except:
        print('Start program')

    finally:
        # Создаем список данных для записи в CSV файл
        data = [
            [deposit_, today, int(amount_per_day), days_left, total_amount, note],
        ]

        # Открываем файл для записи
        with open('data.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Записываем заголовки столбцов
            if csvfile.tell() == 0:
                writer.writerow(['Внесение', 'Дата', 'В день', 'Осталось дней', 'Осталось', 'Примечание'])

            # Записываем данные
            for row in data:
                writer.writerow(row)


def info():
    # Открываем файл для чтения
    with open('data.csv', 'r', newline='') as readfile:
        # Представление данных в виде словаря
        read = csv.DictReader(readfile)

        # Проходимся по строкам и возвращаем последнюю строку в формате словаря
        for row_read in read:
            last_row_read = row_read
            printing = f'\nОсталось собрать:   {last_row_read["Осталось"]}\n' \
                       f'Осталось дней:      {last_row_read["Осталось дней"]}\n' \
                       f'В день надо:        {last_row_read["В день"]}\n' \
                       f'\nПоследнее внесение:   {last_row_read["Внесение"]}\n' \
                       f'Заметка:  {last_row_read["Примечание"]}\n'

        return printing
