try:
    from colorama import Fore, Style, init

    init()
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

    class Fore:  # type: ignore
        GREEN = ''
        YELLOW = ''
        RED = ''

    class Style:  # type: ignore
        RESET_ALL = ''


def format_output(message: str, color=None) -> str:
    """Возвращает строку с цветом, если colorama доступна."""
    if COLORAMA_AVAILABLE and color:
        return f'{color}{message}{Style.RESET_ALL}'
    return message
