"""Генератор приветствий."""


def greeting(name: str) -> str:
    """Возвращает текст приветствияp.

    Args:
        name: Имя пользователя

    Returns:
        str: Текст приветствия
    """
    name_list = [name_part.capitalize() for name_part in name.split(' ')]
    name = ' '.join(name_list)
    return f'Привет, {name}'
