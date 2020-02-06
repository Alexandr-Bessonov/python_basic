from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, title="type of clothing"):
        self.title = title

    # @abstractmethod
    # def my_metod_1(self):
    #     pass
    #
    # @abstractmethod
    # def my_metod_2(self):
    #     pass
    # @property
    # def sq_all(self):
    #     return str(f'Общая площадь материала \n {self.sq_coat+ self.sq_costume}')


class Coat(Clothes):
    def __init__(self, title):
        super().__init__(title)
        self.sq_coat = round(self.title / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь требуемого материала на пальто {self.sq_coat}'


class Costume(Clothes):

    def __init__(self, title):
        super().__init__(title)
        self.sq_costume = round(self.title * 2 + 0.3)

    def __str__(self):
        return f'Площадь требуемого материала на костюм {self.sq_costume}'

coat = Coat(48)
costume = Costume(1.72)
print(coat)
print(costume)
print(coat.__str__())
print(costume.__str__())

# print(f'Общая площадь материала: {coat.__str__()+ costume.__str__()}')