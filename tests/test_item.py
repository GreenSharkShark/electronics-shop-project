from src.item import Item


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
Item.pay_rate = 0.8
item2.apply_discount()
print(item1.name)


def calculate_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.price == 16000.0


def string_to_number():
    assert Item.string_to_number('5') == 5


def instantinate_from_csv():
    Item.instantiate_from_csv()
    assert Item.all[0].name == "Phone"


def test_repr():
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    assert str(item1) == 'Смартфон'


test_str()
calculate_total_price()
string_to_number()
