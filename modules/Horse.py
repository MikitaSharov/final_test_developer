from modules.Pack import Pack


class Horse(Pack):
    def __init__(self, name, date_of_birthday):
        super().__init__(name, date_of_birthday)

    def get_class(self):
        return "Horse"
