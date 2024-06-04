from modules.Pet import Pet


class Dog(Pet):
    def __init__(self, name, date_of_birthday):
        super().__init__(name, date_of_birthday)

    def get_class(self):
        return "Dog"
