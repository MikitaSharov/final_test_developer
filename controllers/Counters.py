class Counters:
    __current_animal_id = 0

    @classmethod
    def get_new_animal_id(cls):
        cls.__current_animal_id += 1
        return cls.__current_animal_id

    @classmethod
    def get_new_command_id(cls, animal):
        commands_list = animal.get_commands_list()
        if commands_list:
            max_command_id = max(map(int, commands_list.keys()))
            return str(max_command_id + 1)
        else:
            return "1"
