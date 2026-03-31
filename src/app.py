"""
Nexpanse — основной модуль приложения.
"""


def hello():
    """Приветственная функция."""
    return "Hello from Nexpanse!"


def get_version():
    """Возвращает текущую версию приложения."""
    return "0.1.0"


def get_app_info():
    """Возвращает основную информацию о приложении."""
    return {
        "name": "Nexpanse",
        "version": get_version(),
        "greeting": hello(),
    }


def get_status():
    """Возвращает текущий статус приложения."""
    return {"status": "running", "version": get_version()}


if __name__ == "__main__":
    print(hello())
