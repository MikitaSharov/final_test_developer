from abc import ABC, abstractmethod


class CommandsInterface(ABC):
    @abstractmethod
    def teach_command(self, animal, command_name, action):
        pass

    @abstractmethod
    def show_commands(self, animal):
        pass

    @abstractmethod
    def execute_command(self, animal, command_id):
        pass
    