import shutil
import os
from time import sleep

from ranging import processCsv
from parserIN import parserIn
from parserOUT import parserOut
from check_token import check_token

def center_text(text, width=None):
    if width is None:
        width = shutil.get_terminal_size().columns
    return text.center(width)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu(title="FAIRTURN", options=None):

    clear_console()
    width = shutil.get_terminal_size().columns

    # Верхняя рамка
    print("═" * width)

    # Заголовок
    print(center_text(title, width))
    print("─" * width)

    # Опции меню
    for option in options:
        print(center_text(option, width))

    # Нижняя рамка
    print("═" * width)
    print()


if __name__ == "__main__":
    while True:
        show_menu(
            title="FAIRTURN",
            options=[
                "1. Process table from Google Sheets",
                "2. Check token",
                "0. Exit"
            ]
        )

        choice = input(center_text("Your choice: ")).strip()

        match choice:
            case "1":
                try:
                    clear_console()
                    parserIn()
                    sleep(1)
                    clear_console()
                    try:
                        currentLab = int(input("Enter current lab number: "))
                    except Exception as ex:
                        print("Invalid number!")
                        sleep(2)
                        continue

                    processCsv(currentLab)
                    clear_console()
                    parserOut()
                    sleep(2)
                except Exception as ex:
                    print(f"\033[31mError: {ex}\033[0m")
                    sleep(5)

            case "2":
                try:
                    clear_console()
                    check_token()
                    sleep(2)
                except Exception as ex:
                    print(f"\033[31mError: {ex}\033[0m")
                    sleep(5)

            case "0":
                clear_console()
                exit(0)

            case _:
                clear_console()
                print("\033[31mInvalid choice!\033[0m")
                sleep(2)