"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture(autouse=True)
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(500), f'Запрашиваемое количество книг не может быть отрицательным или превышает количеству книг на складе {product.quantity}'

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(999) != product.quantity, f'Запрашиваемое количество книг превышает количеству на складе'

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        # assert product.buy(165) != product.quantity, f'Запрашиваемое количество книг превышает количеству на складе'

        with pytest.raises(ValueError) as info:
            product.buy(1005)
            assert str(info.value) == 'Недостаточно товара на складе'

        with pytest.raises(ValueError) as info:
            product.buy(-1)
            assert str(info.value) == 'Количество не может быть меньше 0'

class TestCart:

    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, product):
        cart = Cart()

        cart.add_product(product, 5)
        cart.add_product(product, 5)
        assert cart.products[product] == 10, f'Количество товаров не соответсвует добаленым товаров'

    def test_add_product_buy_count_zero(self, product):
        cart = Cart()
        with pytest.raises(ValueError) as info:
            cart.add_product(product, 0)
            assert str(info.value) == 'Количество не может быть меньше 1'

    def test_remove_product(self, product):
        cart = Cart()

        cart.add_product(product, 5)
        cart.remove_product(product)
        assert product not in cart.products, f'Товар присутсвует в корзине'

        cart.add_product(product, 5)
        cart.remove_product(product, 45)
        assert product not in cart.products, f'Товар присутсвует в корзине'

    def test_clear(self, product):
        cart = Cart()

        cart.add_product(product, 5)
        cart.clear()
        assert len(cart.products) == 0, f'Товар присутсвует в корзине'

    def test_total_price(self, product):
        cart = Cart()
        apple = Product('iphone', 1500, 'mobile', 50)
        samsung = Product('samsung', 1500, 'mobile', 45)
        cart.add_product(apple, 12)
        cart.add_product(samsung, 13)

        assert cart.get_total_price() == 37500, f'Не верно расчитана цена за товары'
        # cart.get_total_price()

    def test_buy_more_than_acceptable(self, product):
        cart = Cart()
        cart.add_product(product, 1111)
        with pytest.raises(ValueError) as info:
            cart.buy()
            assert str(info.value) == "Недостаточно количество товаров"
