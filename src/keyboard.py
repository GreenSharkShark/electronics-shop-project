from src.item import Item
from src.mixin_language_changer import MixinLanguageChanger


class Keyboard(Item, MixinLanguageChanger):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
