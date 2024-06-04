from modules.Pet import Pet


class Hamster(Pet):
    def __init__(self, name, date_of_birthday):
        super().__init__(name, date_of_birthday)

    def get_class(self):
        return "Hamster"
    