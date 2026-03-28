"""
Nexpanse — основной модуль приложения.
"""


def hello():
    """Приветственная функция."""
    return "Hello from Nexpanse!"


def get_version():
    """Возвращает текущую версию приложения."""
    return "0.1.0"


if __name__ == "__main__":
    print(hello())
