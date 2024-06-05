from abc import ABC

from modules.Animal import Animal


class Pack(Animal, ABC):
    def get_class_type(self):
        return "Pack"
