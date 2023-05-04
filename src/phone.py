from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __add__(self, other):
        # if not issubclass(Phone, Item):
        #     return 'Можно сложить только объекты класса Item и Phone.'
        return other.quantity + self.quantity

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f"{self.name}"

    @property
    def number_of_sim(self):
        """
        Геттер для атрибута number_of_sim
        :return:
        """
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        """
        Сеттер для атрибута name. Перед присвоением атрибута проверяет длину имени.
        :param :
        :return:
        """
        if not type(number_of_sim) == int or number_of_sim < 1:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
        self._number_of_sim = number_of_sim
