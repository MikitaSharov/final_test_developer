from abc import ABC, abstractmethod


class ControllerInterface(ABC):
    @abstractmethod
    def add_animal(self, animal):
        pass

    @abstractmethod
    def get_animal_by_id(self, animal_id):
        pass

    @abstractmethod
    def get_animal_by_name(self, name):
        pass

    @abstractmethod
    def show_all_commands(self, animal):
        pass

    @abstractmethod
    def teach_animal_command(self, animal, command_name, action):
        pass

    @abstractmethod
    def execute_animal_command(self, animal, command_id):
        pass
    