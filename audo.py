import sys
import base64

def main():
    args = sys.argv[1:]  # Получаем список всех аргументов командной строки, исключая имя скрипта

    # Проверяем наличие "dshack" в аргументах
    if "dshack" in args:
        index = args.index("dshack")  # Находим индекс первого вхождения "dshack"
        if index + 1 < len(args):  # Убеждаемся, что есть следующий аргумент после "dshack"
            value_after_dshack = args[index + 1]
            data_to_encode = value_after_dshack.encode('utf-8')
            encoded_data = base64.b64encode(data_to_encode)
            print("Первая часть токена: " + str(encoded_data))
        else:
            print("Нет значения после 'dshack'")
    else:
        print("Строка 'dshack' не найдена в аргументах командной строки")

if __name__ == "__main__":
    main()
