def show_data():
    """Выводит информацию из справочника"""
    print("№ | Имя | Фамилия | Телефон")
    with open('data.txt', 'r', encoding='utf-8') as data:
        print(data.read())

def new_data():
    """добавляет строку в справочник"""
    with open('data.txt', 'r', encoding='utf-8') as data:
        data = data.read()
    num = len(data.split("\n"))
    name = input('Введите Имя: ')
    fio = input('Введите Фамилию: ')
    phone_num = input('Введите номер телефлна: ')
    with open('data.txt', 'a', encoding='utf-8') as data:
        data.write(f'{num} | {name} | {fio} | {phone_num}\n')

def find_data():
    """Печатает результат поиска по справочнику."""
    with open('data.txt', 'r', encoding='utf-8') as data:
        data = data.read()
    contact_to_find = input('Введите, что хотите найти: ')
    result = search(data, contact_to_find )
    print(result)
    print("")
    
def search(data: str, info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    data = data.split('\n')
    return list(filter(lambda contact: info.lower() in contact.lower(), data))


def delete_data():
    """Удаляет данные в справочнике"""
    with open('data.txt', 'r', encoding='utf-8') as data:
        text = data.read()
    print("")
    delete_data = int(input("Введите номер строки для удаления: ")) - 1
    lines_data = text.split("\n")
    delete_data_lines = lines_data[delete_data]
    lines_data.pop(delete_data)
    print(f"Удалена запись: {delete_data_lines}\n")
    with open('data.txt', 'w', encoding='utf-8') as data:
        data.write("\n".join(lines_data))

def change():
    """Изменяет данные в справочнике"""
    with open('data.txt', 'r', encoding='utf-8') as data:
        text = data.read()
    numb = int(input("Введите номер строки для редактирования: ")) - 1
    lines_data = text.split("\n")
    edit_data = lines_data[numb]
    signs = edit_data.split(" | ")
    name = input('Введите Имя: ')
    fio = input('Введите Фамилию: ')
    phone_num = input('Введите номер телефлна: ')
    num = signs[0]
    if len(name) == 0:
        name = signs[1]
    if len(fio) == 0:
        fio = signs[2]
    if len(phone_num) == 0:
        phone_num = signs[3]
    edited_line = f'{num} | {name} | {fio} | {phone_num}'
    lines_data[numb] = edited_line
    print(f"Запись - {edit_data}, изменена на - {edited_line}\n")
    with open('data.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(lines_data))