from utils import deposit, info

while True:
    quit_ = ['q', 'в']
    info_ = ['i', 'и']
    user_input = input('Ввод:\n   ')
    if user_input.isdigit():
        deposit_ = int(user_input)
        confirmation = input(f'Подтвердить сумму: {deposit_}')
        if confirmation == '':
            input_note = input('Заметка:\n   ')
            deposit(deposit_, input_note)
            print(info())
        else:
            continue

    elif user_input in info_:
        print(info())
        pass

    elif user_input in quit_:
        break

    else:
        print('Неправильная команда')
        continue





