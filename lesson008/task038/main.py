import function

while True:
    mode = input('Выберите режим работы справочника' + '\n'
                  + '1 - Чтение файла, 2 - Добавление в файл, 3 - Удаление, 4 - Замена, 5 - Поиск, 6 - ВЫХОД: ')
    if mode == '1':
        function.show_data()
    elif mode == '2':
        function.new_data()
    elif mode == '3':
        function.delete_data()
    elif mode == '4':
        function.change()
    elif mode == '5':
        function.find_data()
    elif mode == '6':
        break
    else:
        print('No mode')
