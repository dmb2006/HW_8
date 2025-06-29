from itertools import product

import pytest


class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """

        if quantity < 0:
            raise ValueError('Количество не может быть меньше 0')
        elif self.quantity >= quantity:
            return True
        else:
            return False

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if not self.check_quantity(quantity):
            raise ValueError(f'Недостаточно товара на складе')
        else:
            return self.check_quantity(quantity) * self.price

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if buy_count < 1:
            raise ValueError('Количество не может быть меньше 1')

        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if remove_count is None:
            del self.products[product]
        elif remove_count > self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= remove_count
        # raise NotImplementedError

    def clear(self):
        self.products = {}
        # raise NotImplementedError

    def get_total_price(self) -> float:
        total_price = 0.0

        for product, buy_count in self.products.items():
            total_price += product.price * buy_count
        return total_price
        # raise NotImplementedError

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        message = ("Недостаточно количество товаров")
        for product, buy_count in self.products.items():
            if not product.check_quantity(buy_count):
                raise ValueError(message)
            elif buy_count < 0:
                raise ValueError(message)
        for product, count in self.products.items():
            product.buy(count)


