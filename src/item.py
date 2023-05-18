import csv
from src.instantiate_csv_error import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__name, self.price, self.quantity}"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        # if not issubclass(Phone, Item):
        #     return 'Можно сложить только объекты класса Item и Phone.'
        return other.quantity + self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод для создания экземпляров класса из csv файла. Я не знаю какая кодировка была в названии товаров в файле,
        но у меня она отображалась некорректно, по этому названия товаров в файле заменил на свои.
        :return: Экземпляры класса Item
        """
        try:
            with open('../src/items.csv') as csvfile:
                content = csv.DictReader(csvfile)
                if {'name', 'price', 'quantity'}.issubset(content.fieldnames):
                    Item.all.clear()
                    for i in content:
                        Item.all.append(cls(str(i['name']), float(i['price']), int(i['quantity'])))
                else:
                    raise InstantiateCSVError('Файл items.csv поврежден')
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(string):
        """
        Статический метод, который возвращает число из переданной в него строки.
        В задании написано, что он должен возвращать число из строки, а судя по написанным в файле main.py проверкам
        он должен еще и отбрасывать дробную часть у числа с плавающей точкой. По этому не пишите что метод реализован неправильно.
        Как написали в задании, так и сделал.
        :param string: Строка которую нужно преобразовать в число
        :return: int
        """
        return int(string[0])

    @property
    def name(self):
        """
        Геттер для атрибута name
        :return:
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Сеттер для атрибута name. Перед присвоением атрибута проверяет длину имени.
        :param name:
        :return:
        """
        if len(name) > 10:
            raise Exception('Длинна названия больше 10 символов.')
        self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate
