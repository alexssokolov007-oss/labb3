FACTORIAL_MAX_ITERATIVE = 1000
FACTORIAL_MAX_RECURSIVE = 500

FIBO_MAX_ITERATIVE = 10000
FIBO_MAX_RECURSIVE = 1000

RADIX_DEFAULT_BASE = 10

COUNTING_SORT_MAX_VALUE = 100000
COUNTING_SORT_MAX_RANGE_RATIO = 100

BUCKET_SORT_MIN_VALUE = 0.0
BUCKET_SORT_MAX_VALUE = 1.0

BENCHMARK_SMALL_TIME = 0.001
BENCHMARK_MEDIUM_TIME = 0.01
BENCHMARK_ARRAY_SIZES = [100, 1000]
BENCHMARK_NEARLY_SORTED_SWAPS = {100: 10, 1000: 50}
BENCHMARK_DUPLICATES_UNIQUE = 10

SEQUENCES_OPTIONS = [
    'Факториал (итеративно)',
    'Факториал (рекурсивно)',
    'Фибоначчи (итеративно)',
    'Фибоначчи (рекурсивно)',
    'Назад в главное меню',
]

SORTING_OPTIONS = [
    'Пузырьковая',
    'Быстрая',
    'Подсчётом',
    'По разрядам',
    'Кучей (heap)',
    'По корзинам (bucket)',
    'Назад в главное меню',
]

STACK_IMPLEMENTATIONS = [
    'Стек на связном списке',
    'Стек на списке',
    'Стек на двух очередях',
    'Назад в главное меню',
]

STACK_OPERATIONS = [
    'Push (добавить элемент)',
    'Pop (снять верхний)',
    'Peek (посмотреть верхний)',
    'Проверить пустоту',
    'Размер стека',
    'Минимум в стеке',
    'Назад',
]

BENCHMARK_ARRAY_NAMES = {
    'Случайные 100': 'rand_100',
    'Случайные 1000': 'rand_1000',
    'Почти отсортированные 100': 'near_100',
    'Почти отсортированные 1000': 'near_1000',
    'Много повторов 1000': 'dup_1000',
    'Обратный порядок 100': 'rev_100',
    'Обратный порядок 1000': 'rev_1000',
}
