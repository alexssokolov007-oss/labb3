from src.benchmarks import benchmark_sorts, print_benchmark_results, run_comprehensive_benchmark
from src.constants import (
    BENCHMARK_ARRAY_NAMES,
    RADIX_DEFAULT_BASE,
    SEQUENCES_OPTIONS,
    SORTING_OPTIONS,
    STACK_IMPLEMENTATIONS,
    STACK_OPERATIONS,
)
from src.generator_tests import (
    many_duplicates,
    nearly_sorted,
    rand_float_array,
    rand_int_array,
    reverse_sorted,
)
from src.output import Fore, format_output
from src.sequences import Sequences
from src.sorting import bucket_sort, bubble_sort, counting_sort, heap_sort, quick_sort, radix_sort
from src.stack import LinkedListStack, ListStack, QueueStack


def print_line(message: str, color=None) -> None:
    print(format_output(message, color))


def _ask_int(prompt: str) -> int:
    return int(input(prompt).strip())


def benchmark_menu() -> None:
    while True:
        print_line('\n— Бенчмарки —')
        print_line('1. Прогнать набор тестов')
        print_line('2. Сравнить алгоритмы на своём массиве')
        print_line('3. Назад')
        choice = input('Выберите пункт: ').strip()

        if choice == '1':
            run_comprehensive_benchmark()
        elif choice == '2':
            compare_algorithms_on_current_array()
        elif choice == '3':
            return
        else:
            print_line('Нет такого пункта.', Fore.RED)


def _read_manual_array(as_float: bool) -> list:
    raw = input('Введите числа через пробел: ').strip()
    if not raw:
        raise ValueError('Пустой ввод')
    parser = float if as_float else int
    return [parser(x) for x in raw.split()]


def _generate_array() -> list:
    print_line('\nСпособ генерации:')
    print_line('1. Случайные целые')
    print_line('2. Почти отсортированный')
    print_line('3. Много повторов')
    print_line('4. Обратный порядок')
    print_line('5. Случайные числа с плавающей точкой')
    gen_choice = input('Выберите пункт: ').strip()

    n = _ask_int('Размер массива: ')
    if gen_choice == '1':
        lo = _ask_int('Нижняя граница: ')
        hi = _ask_int('Верхняя граница: ')
        distinct = input('Только уникальные? (y/n): ').strip().lower() == 'y'
        return rand_int_array(n, lo, hi, distinct=distinct)
    if gen_choice == '2':
        swaps = _ask_int('Сколько случайных обменов: ')
        return nearly_sorted(n, swaps)
    if gen_choice == '3':
        k_unique = _ask_int('Сколько уникальных значений: ')
        return many_duplicates(n, k_unique)
    if gen_choice == '4':
        return reverse_sorted(n)
    if gen_choice == '5':
        lo = float(input('Нижняя граница: '))
        hi = float(input('Верхняя граница: '))
        return rand_float_array(n, lo, hi)
    raise ValueError('Неизвестный способ генерации')


def compare_algorithms_on_current_array() -> None:
    try:
        print_line('\n1. Ввести массив вручную\n2. Сгенерировать автоматически')
        way = input('Способ ввода: ').strip()
        as_float = False
        if way == '1':
            as_float = input('Массив float? (y/n): ').strip().lower() == 'y'
            arr = _read_manual_array(as_float)
        elif way == '2':
            arr = _generate_array()
            as_float = any(isinstance(x, float) for x in arr)
        else:
            print_line('Нет такого пункта.', Fore.RED)
            return

        print_line(f'Сгенерированный массив (первые 20): {arr[:20]}{"..." if len(arr) > 20 else ""}', Fore.GREEN)

        algos = {
            'Пузырьковая': bubble_sort,
            'Быстрая': quick_sort,
            'Подсчетом': counting_sort,
            'По разрядам': lambda a: radix_sort(a, RADIX_DEFAULT_BASE),
            'Кучей': heap_sort,
            'По корзинам': bucket_sort,
        }
        if as_float:
            algos.pop('Подсчетом', None)
            algos.pop('По разрядам', None)

        results = benchmark_sorts({'Ваш массив': arr}, algos)
        print_benchmark_results(results)
    except Exception as e:
        print_line(f'Ошибка: {e}', Fore.RED)


def sequences_menu(sequences: Sequences) -> None:
    while True:
        print_line('\n— Последовательности —')
        for i, option in enumerate(SEQUENCES_OPTIONS, 1):
            print_line(f'{i}. {option}')
        choice = input('Выберите пункт: ').strip()

        if choice == '5':
            return
        if choice in {'1', '2', '3', '4'}:
            try:
                n = _ask_int('Введите n: ')
                if choice == '1':
                    print_line(f'{n}! = {sequences.factorial(n)}', Fore.GREEN)
                elif choice == '2':
                    print_line(f'{n}! = {sequences.factorial_recursive(n)} (рекурсия)', Fore.GREEN)
                elif choice == '3':
                    print_line(f'F({n}) = {sequences.fibo(n)}', Fore.GREEN)
                elif choice == '4':
                    print_line(f'F({n}) = {sequences.fibo_recursive(n)} (рекурсия)', Fore.GREEN)
            except Exception as e:
                print_line(f'Ошибка: {e}', Fore.RED)
        else:
            print_line('Нет такого пункта.', Fore.RED)


def sorting_menu() -> None:
    while True:
        print_line('\n— Сортировки —')
        for i, option in enumerate(SORTING_OPTIONS, 1):
            print_line(f'{i}. {option}')
        choice = input('Выберите пункт: ').strip()

        if choice == '7':
            return
        if choice not in {'1', '2', '3', '4', '5', '6'}:
            print_line('Нет такого пункта.', Fore.RED)
            continue

        try:
            print_line('\n1. Ввести массив вручную\n2. Сгенерировать автоматически')
            way = input('Способ ввода: ').strip()
            as_float = choice in {'5', '6'}
            if way == '1':
                as_float = input('Массив float? (y/n): ').strip().lower() == 'y' if as_float else False
                arr = _read_manual_array(as_float)
            else:
                arr = _generate_array()
                as_float = any(isinstance(x, float) for x in arr)

            if choice in {'1', '2', '3', '4', '6'}:
                arr = [int(x) for x in arr]

            alg_results = None
            if choice == '1':
                alg_results = bubble_sort(arr)
            elif choice == '2':
                alg_results = quick_sort(arr)
            elif choice == '3':
                alg_results = counting_sort(arr)
            elif choice == '4':
                base_input = input(f'Основание (по умолчанию {RADIX_DEFAULT_BASE}): ').strip()
                base = int(base_input) if base_input else RADIX_DEFAULT_BASE
                alg_results = radix_sort(arr, base)
            elif choice == '5':
                buckets_input = input('Количество корзин (Enter — по длине массива): ').strip()
                buckets = int(buckets_input) if buckets_input else None
                alg_results = bucket_sort(arr, buckets)
            elif choice == '6':
                alg_results = heap_sort(arr)

            print_line(f'Отсортировано: {alg_results}', Fore.GREEN)
        except Exception as e:
            print_line(f'Ошибка: {e}', Fore.RED)


def stack_menu() -> None:
    while True:
        print_line('\n— Стек —')
        for i, option in enumerate(STACK_IMPLEMENTATIONS, 1):
            print_line(f'{i}. {option}')
        choice = input('Выберите реализацию: ').strip()

        if choice == '4':
            return
        if choice == '1':
            stack = LinkedListStack()
        elif choice == '2':
            stack = ListStack()
        elif choice == '3':
            stack = QueueStack()
        else:
            print_line('Нет такого пункта.', Fore.RED)
            continue
        stack_operations_menu(stack, STACK_IMPLEMENTATIONS[int(choice) - 1])


def stack_operations_menu(stack, stack_name: str) -> None:
    while True:
        print_line(f'\n— Операции ({stack_name}) —')
        for i, option in enumerate(STACK_OPERATIONS, 1):
            print_line(f'{i}. {option}')
        choice = input('Ваш выбор: ').strip()

        if choice == '7':
            return
        try:
            if choice == '1':
                x = _ask_int('Значение: ')
                stack.push(x)
                print_line(f'Добавлено: {x}', Fore.GREEN)
            elif choice == '2':
                print_line(f'Снято: {stack.pop()}', Fore.GREEN)
            elif choice == '3':
                print_line(f'Верхний элемент: {stack.peek()}', Fore.GREEN)
            elif choice == '4':
                print_line(f'Пустой? {stack.is_empty()}', Fore.GREEN)
            elif choice == '5':
                print_line(f'Размер: {len(stack)}', Fore.GREEN)
            elif choice == '6':
                print_line(f'Минимум: {stack.min()}', Fore.GREEN)
            else:
                print_line('Нет такого пункта.', Fore.RED)
        except Exception as e:
            print_line(f'Ошибка: {e}', Fore.RED)
