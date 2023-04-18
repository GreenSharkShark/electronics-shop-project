from src.item import Item


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
Item.pay_rate = 0.8
item2.apply_discount()


def test_item():
    assert item1.calculate_total_price() == 200000
    assert item2.price == 16000.0
