from datetime import date

from controllers.Controller import Controller
from modules.Camel import Camel
from modules.Cat import Cat
from modules.Dog import Dog
from modules.Donkey import Donkey
from modules.Hamster import Hamster
from modules.Horse import Horse


class Menu:
    def __init__(self):
        self.__controller = Controller()

    def show_menu(self):
        while True:
            print('1. Добавить животное')
            print("2. Выбрать животное")
            print('3. Выход')
            choice = input('Выберите действие 1/2/3: ')
            if choice == '1':
                self.add_animal_menu()
            elif choice == '2':
                self.select_animal_menu()
            elif choice == '3':
                break

    def add_animal_menu(self):
        print('1. Собака')
        print('2. Кошка')
        print('3. Хомяк')
        print('4. Лошадь')
        print('5. Верблюд')
        print('6. Осёл')
        animal_type = input('Выберите тип животного 1/2/3/4/5/6: ')
        name = input('Введите имя животного: ')

        while True:
            date_of_birthday_input = input('Введите день рождения животного в формате YYYY-MM-DD: ')
            try:
                date_of_birthday = date.fromisoformat(date_of_birthday_input)
                break
            except ValueError:
                print(f'Неверный формат даты {date_of_birthday_input}. Попробуйте ещё раз в формате YYYY-MM-DD: ')

        if animal_type == '1':
            animal = Dog(name, date_of_birthday)
        elif animal_type == '2':
            animal = Cat(name, date_of_birthday)
        elif animal_type == '3':
            animal = Hamster(name, date_of_birthday)
        elif animal_type == '4':
            animal = Horse(name, date_of_birthday)
        elif animal_type == '5':
            animal = Camel(name, date_of_birthday)
        elif animal_type == '6':
            animal = Donkey(name, date_of_birthday)
        else:
            print('Неверный ввод')
            return

        self.__controller.add_animal(animal)
        print(f'Животное {name} добавлено с ID {animal.get_id()}')

    def select_animal_menu(self):
        for animal in self.__controller.get_animal():
            print(f'{animal.get_id()}. {animal.get_name()}')

        choice = input('Введите ID (номер) животного или его имя: ')
        if choice.isdigit():
            animal = self.__controller.get_animal_by_id(int(choice))
        else:
            animal = self.__controller.get_animal_by_name(choice)

        if animal:
            while True:
                print('1. Выполнить команду')
                print('2. Обучить команде')
                print('3. В предыдущее меню')
                sub_choice = input('Выберите действие 1/2/3: ')
                if sub_choice == '1':
                    self.execute_command_menu(animal)
                elif sub_choice == '2':
                    self.teach_command_menu(animal)
                elif sub_choice == '3':
                    break
        else:
            print('Животное не найдено')

    def execute_command_menu(self, animal):
        print(f'Доступные команды для {animal.get_name()}:')
        commands_list = animal.get_commands_list()
        for command_id, command_info in commands_list.items():
            print(f'{command_id}. {command_info["name"]}')

        choice = input('Введите ID (номер) или название команды: ')
        if choice.isdigit():
            command_id = choice
        else:
            command_id = next((cd_id for cd_id, command_info in commands_list.items() if command_info['name'] == choice), None)

        if command_id:
            result = self.__controller.execute_animal_command(animal, command_id)
            print(result)
        else:
            print('Команда не найдена')

    def teach_command_menu(self, animal):
        command_name = input('Введите название команды: ')
        action = input(f'Введите выполнение команды {command_name}: ')
        self.__controller.teach_animal_command(animal, command_name, action)
        print(f'Животное {animal.get_name()} обучено команде {command_name}')