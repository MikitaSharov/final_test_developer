from abc import ABC

from modules.Animal import Animal


class Pet(Animal, ABC):
    def get_class_type(self):
        return "Pet"
