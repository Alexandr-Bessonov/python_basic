from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, title="type of clothing"):
        self.title = title

    @abstractmethod
    def my_metod_1(self):
        pass

    @abstractmethod
    def my_metod_2(self):
        pass


class Coat(Clothes):

    def my_metod_1(self):
        pass

    def my_metod_2(self):
        pass


class Costume(Clothes):

    def my_metod_1(self):
        pass

    def my_metod_2(self):
        pass
