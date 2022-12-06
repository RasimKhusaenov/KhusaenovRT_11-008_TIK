from btw import BTW
from mtf import MoveToFront
from ac import ArithmeticCoding


# КОДЕР: Преобразование Б-У + стопка книг
def btw_plus_mtf_encode(message, alphabet=None, humanize_index=False):
    encoded_message, initial_message_index = BTW(message, humanize_index).encode()
    encoded_message = MoveToFront(encoded_message, alphabet, humanize_index).encode()
    return encoded_message, initial_message_index


# ДЕКОДЕР: Арифметическое код-е
def ac_decode(alphabet, p, encoded_number, length):
    decoded_message = ArithmeticCoding(alphabet, p, encoded_number, length).decode()
    return decoded_message


if __name__ == "__main__":
    try:
        algorithm = int(input("Если хотите выбрать \"Преобразование Б-У + стопка книг\", введите 0, "
                              "если хотите выбрать \"Арифметическое код-е\", введите 1: "))
        if algorithm == 0:
            input_filename = "mtf_input.txt"
            with open(input_filename, "r", encoding="UTF-8") as file:
                alphabet = file.readline().split()
            input_message = input("Введите сообщение для кодирования: ")
            result = btw_plus_mtf_encode(input_message, alphabet)
            print(result[0], result[1], sep="\n")
        elif algorithm == 1:
            input_filename = "ac_input.txt"
            with open(input_filename, "r", encoding="UTF-8") as file:
                alphabet = file.readline().split()
                p = list(float(number.replace(",", ".")) for number in file.readline().split())
            input_number, length = input("Введите точку из отрезка и длину исходного сообщения через пробел: ").split()
            input_number, length = float(input_number.replace(",", ".")), int(length)
            result = ac_decode(alphabet, p, input_number, length)
            print(result)
        else:
            raise ValueError
    except ValueError:
        exit("Вышло недопонимание...")
    except FileNotFoundError:
        exit("Не нашёл входной файл...")

