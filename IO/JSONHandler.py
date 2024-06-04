import json
from datetime import date
from modules.Dog import Dog
from modules.Cat import Cat
from modules.Hamster import Hamster
from modules.Horse import Horse
from modules.Camel import Camel
from modules.Donkey import Donkey


class JSONHandler:
    @staticmethod
    def save_to_json(animals, filename='animals.json'):
        data = []
        for animal in animals:
            animal_data = {
                'id': animal.get_id(),
                'name': animal.get_name(),
                'date_of_birthday': animal.get_date_of_birthday().isoformat(),
                'class': animal.get_class(),
                'commands_list': animal.get_commands_list()
            }
            data.append(animal_data)
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def load_from_json(filename='animals.json'):
        animals = []
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for animal_data in data:
                    animal_class = globals()[animal_data['class']]
                    animal = animal_class(animal_data['name'], date.fromisoformat(animal_data['date_of_birthday']))
                    for command_id, command_data in animal_data['commands_list'].items():
                        animal.set_commands_list(command_id, command_data)
                    animals.append(animal)
        except FileNotFoundError:
            print(f"Файл {filename} не найден")
        return animals
