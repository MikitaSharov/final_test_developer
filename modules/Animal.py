from abc import ABC, abstractmethod

from controllers.Counters import Counters


class Animal(ABC):
    def __init__(self, name, date_of_birthday):
        self.__id = Counters.get_new_animal_id()
        self.__name = name
        self.__date_of_birthday = date_of_birthday
        self.__animal_type = self.get_class_type()
        self.__class_name = self.get_class()
        self.__commands_list = {}

    @abstractmethod
    def get_class(self):
        pass

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_date_of_birthday(self):
        return self.__date_of_birthday

    # def get_class_name(self):
    #     return self.__class_name

    def get_commands_list(self):
        return self.__commands_list

    def set_commands_list(self, command_id, command_data):
        self.__commands_list[command_id] = command_data

    def add_command(self, command_id, command_info):
        self.__commands_list[command_id] = command_info

    def get_animal_type(self):
        return self.__animal_type

    @abstractmethod
    def get_class_type(self):
        pass
