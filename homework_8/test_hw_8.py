"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
import random

from homework_8.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(666) == True
        assert product.check_quantity(1000) == True
        assert product.check_quantity(99999) == False


    def test_product_buy(self, product):
        origin_quantity = product.quantity #Изначальное кол-во товара
        quantity_to_buy = random.randint(1, 1000) # Случайнное кол-во купленнногоо товара
        product.buy(quantity_to_buy)
        assert product.quantity == origin_quantity - quantity_to_buy

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError, match="Продукт закончился"):
          product.buy(product.quantity + 1)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, cart, product):  # Добавляем продукт в корзину
        cart.add_product(product, buy_count=3)
        assert cart.products[product] == 3

    def test_add_existing_product(self, cart, product): # Добавляем еще один продукт в корзину
        cart.add_product(product, buy_count=2)
        cart.add_product(product, buy_count=1)
        assert cart.products[product] == 3

    def test_remove_product_partial(self, cart, product):   # Добавляем и удаляем продукт (частично)
        cart.add_product(product, buy_count=5)
        cart.remove_product(product, remove_count=2)
        assert cart.products[product] == 3

    def test_remove_product_completely(self, cart, product):    # Добавляем и полностью удаляем продукт
        cart.add_product(product, buy_count=5)
        cart.remove_product(product)
        assert product not in cart.products

    def test_remove_more_than_available(self, cart, product):   # Добавляем продукт и удаляем из корзины больше, чем в ней есть
        cart.add_product(product, buy_count=5)
        cart.remove_product(product, remove_count=10)
        assert product not in cart.products

    def test_clear_cart(self, cart, product):   # Очищаем корзину в один клик
        cart.add_product(product, buy_count=3)
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price(self, cart, product):  # Проверка общей стоимости корзины
        cart.add_product(product, buy_count=3)
        assert cart.get_total_price() == 300.0

    def test_buy_successful(self, cart, product):   # Проверка успешной покупки
        cart.add_product(product, buy_count=100)
        cart.buy()
        assert len(cart.products) == 0
        assert product.quantity == 900

    def test_buy_insufficient_stock(self, cart, product):   # Проверка, что покупка выбрасывает исключение при недостатке товара на складе
        cart.add_product(product, buy_count=1001)
        with pytest.raises(ValueError, match="Товар временно закончился"):
            cart.buy()