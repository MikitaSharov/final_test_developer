from controllers.CommandsInterface import CommandsInterface
from controllers.Counters import Counters


class Commands(CommandsInterface):
    @staticmethod
    def show_commands(animal):
        return animal.get_commands_list()

    @staticmethod
    def teach_command(animal, command_name, action):
        command_id = Counters.get_new_command_id(animal)
        command_info = {'name': command_name, 'action': action}
        animal.add_command(command_id, command_info)

    @staticmethod
    def execute_command(animal, command_id):
        commands_list = animal.get_commands_list()
        if command_id in commands_list:
            action = commands_list[command_id]
            return f"{animal.get_name()} выполняет команду {action['name']}: {action['action']}"
        return "Команда не найдена"
