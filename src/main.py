import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.output import Fore, format_output
from src.sequences import Sequences
from src.ui import benchmark_menu, sequences_menu, sorting_menu, stack_menu


def print_line(message: str, color=None) -> None:
    print(format_output(message, color))


def main() -> None:
    sequences = Sequences()
    while True:
        try:
            print_line('\n' + '=' * 40)
            print_line('Учебные алгоритмы: последовательности, сортировки, стеки')
            print_line('=' * 40)
            print_line('1. Последовательности')
            print_line('2. Сортировки')
            print_line('3. Стек')
            print_line('4. Бенчмарки')
            print_line('5. Выход')
            choice = input('Выберите пункт: ').strip()

            if choice == '1':
                sequences_menu(sequences)
            elif choice == '2':
                sorting_menu()
            elif choice == '3':
                stack_menu()
            elif choice == '4':
                benchmark_menu()
            elif choice == '5':
                print_line('Пока!', Fore.YELLOW)
                break
            else:
                print_line('Нет такого пункта.', Fore.RED)
        except KeyboardInterrupt:
            print_line('\nВыход по Ctrl+C', Fore.YELLOW)
            break
        except EOFError:
            print_line('\nВвод прерван', Fore.YELLOW)
            break


if __name__ == '__main__':
    main()
