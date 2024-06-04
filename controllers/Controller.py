from controllers.Commands import Commands
from controllers.ControllerInterface import ControllerInterface
from IO.JSONHandler import JSONHandler


class Controller(ControllerInterface):
    def __init__(self):
        self.__animals = JSONHandler.load_from_json()
        self.__commands = Commands()

    def add_animal(self, animal):
        self.__animals.append(animal)
        JSONHandler.save_to_json(self.__animals)

    def get_animal_by_id(self, animal_id):
        for animal in self.__animals:
            if animal.get_id() == animal_id:
                return animal
        return None

    def get_animal_by_name(self, name):
        for animal in self.__animals:
            if animal.get_name() == name:
                return animal
        return None

    def show_all_commands(self, animal):
        return self.__commands.show_commands(animal)

    def teach_animal_command(self, animal, command_name, action):
        self.__commands.teach_command(animal, command_name, action)
        JSONHandler.save_to_json(self.__animals)

    def execute_animal_command(self, animal, command_id):
        return self.__commands.execute_command(animal, command_id)

    def get_animal(self):
        return self.__animals
