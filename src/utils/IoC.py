from typing import Callable, Optional, Dict, TypeVar, Generic

# Определяем тип IDependency
T = TypeVar('T')
IDependency = Callable[..., T]


class Scope:
    """
    Класс, представляющий область видимости для управления зависимостями.

    :param parent: Родительская область видимости, если есть.
    :type parent: Scope, optional
    """
    def __init__(self, parent: Optional['Scope'] = None):
        """
        Инициализирует новую область видимости.

        :param parent: Родительская область видимости, если есть.
        :type parent: Scope, optional
        """
        self.id: int = parent.id + 1 if parent else 0
        self.parent: Optional[Scope] = parent
        self.body: Dict[str, Optional[IDependency]] = {}

    def new_scope(self) -> 'Scope':
        """
        Создает новую дочернюю область видимости.

        :return: Новая дочерняя область видимости.
        :rtype: Scope
        """
        return Scope(self)


class IoC(Generic[T]):
    """
    Класс для управления зависимостями с помощью контейнера IoC.

    :param scope: Область видимости. По умолчанию создается новая область видимости.
    :type scope: Scope, optional
    """
    def __init__(self, scope: Optional[Scope] = None):
        """
        Инициализирует контейнер IoC.

        :param scope: Область видимости. По умолчанию создается новая область видимости.
        :type scope: Scope, optional
        """
        self.scope: Scope = scope or Scope()

    def register(self, key: str, dependency: IDependency[T]) -> None:
        """
        Регистрирует зависимость в контейнере.

        :param key: Ключ для идентификации зависимости.
        :type key: str
        :param dependency: Зависимость, которая будет зарегистрирована.
        :type dependency: IDependency
        """
        self.scope.body[key] = dependency

    def resolve(self, key: str, *args) -> T:
        """
        Разрешает и возвращает зависимость по указанному ключу.

        :param key: Ключ для поиска зависимости.
        :type key: str
        :param args: Позиционные аргументы для передачи к зависимости.
        :return: Разрешенная зависимость.
        :rtype: T
        :raises ValueError: Если зависимость не найдена.
        """
        dependency = self.scope.body.get(key)
        if not dependency:
            raise ValueError(f'dependency "{key}" not registered')
        return dependency(*args)

    def new(self, field: Callable[['IoC'], None]) -> None:
        """
        Создает новую дочернюю область видимости и вызывает функцию для ее настройки.

        :param field: Функция для настройки дочерней области видимости.
        :type field: Callable[['IoC'], None]
        """
        child_scope = self.scope.new_scope()
        child_ioc = IoC(child_scope)
        try:
            field(child_ioc)
        except Exception as ex:
            raise ex

    def delete(self, key: str) -> None:
        """
        Удаляет зависимость из контейнера.

        :param key: Ключ для идентификации зависимости.
        :type key: str
        """
        if key in self.scope.body:
            del self.scope.body[key]
