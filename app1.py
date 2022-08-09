from dataclasses import dataclass
from decimal import Decimal

"""
    Napisz program, w którym z kolekcji obiektów, reprezentujących dane
    produktu (nazwa, kategoria, cena oraz zniżka), wyznaczysz cenę całkowitą 
    tych produktów, które należą do pewnej podanej przez Ciebie kategorii.
"""

@dataclass
class Product:
    name: str
    category: str
    price: Decimal
    discount: Decimal

    def has_category(self, category: str) -> bool:
        return self.category == category

    def get_total_price(self) -> Decimal:
        return self.price * (Decimal(1) - self.discount)

    @staticmethod
    def get_total_price_for_category(category: str, products: list['Product']) -> Decimal:
        return sum([p.get_total_price() for p in products if p.has_category(category)])


def main() -> None:
    products = [
        Product('P1', 'A', Decimal(100), Decimal('0.1')),
        Product('P2', 'B', Decimal(200), Decimal('0.2')),
        Product('P3', 'A', Decimal(300), Decimal('0.15')),
        Product('P4', 'C', Decimal(400), Decimal('0.11'))
    ]
    total_price = Product.get_total_price_for_category('A', products)
    print(total_price)

if __name__ == '__main__':
    main()

