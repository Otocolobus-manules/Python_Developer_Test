
from commands.ICommand import ICommand
from utils.IoC import IoC
from schemas.User import CreateUser, UpdateUser, DeleteUser


class StartConsoleApp(ICommand):
    def __init__(self, container: IoC):
        self.__container = container

    async def execute(self):
        while True:
            print("Выберите действие:")
            print("1. Создать пользователя")
            print("2. Обновить пользователя")
            print("3. Получить пользователя")
            print("4. Удалить пользователя")
            print("5. Выйти")

            choice = input("Номер действия: ")

            if choice == "1":
                username = input("Введите имя пользователя: ")
                user = CreateUser(name=username)
                result = await self.__container.resolve('Services.CreateUserService', user)
                print(f"Пользователь создан: id - {result.id}, username - {result.name}")

            elif choice == '2':
                user_id = int(input("Введите ID пользователя: "))
                username = input("Введите новое имя пользователя: ")
                user = UpdateUser(id=user_id, name=username)
                result = await self.__container.resolve('Services.UpdateUserService', user)
                print(f"Пользователь обновлен: id - {result.id}, username - {result.name}")

            elif choice == '3':
                user_id = int(input("Введите ID пользователя: "))
                result = await self.__container.resolve('Services.GetUserService', user_id)
                print(f"Данные пользователя: id - {result.id}, username - {result.name}")

            elif choice == '4':
                user_id = int(input("Введите ID пользователя: "))
                user = DeleteUser(id=user_id)
                result = await self.__container.resolve('Services.DeleteUserService', user)
                print(f"Пользователь удален: id - {result.id}, username - {result.name}")

            elif choice == '5':
                print("Выход из программы.")
                break

            else:
                print("Неверный выбор")
