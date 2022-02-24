from datetime import datetime
from .helpers.company_inventory import get_company_inventory


class SimpleReport():
    def get_oldest_manufacturing_date(stock):
        oldest_date = None

        for product in stock:
            current_date = datetime.strptime(
                product['data_de_fabricacao'], '%Y-%m-%d'
            )

            if oldest_date is None or current_date < oldest_date:
                oldest_date = current_date

        return oldest_date.date()

    def get_closest_expiration_date(stock):
        closest_date = None

        for product in stock:
            current_date = datetime.strptime(
                product['data_de_validade'], '%Y-%m-%d'
            )

            if (
                closest_date is None
                or current_date > datetime.now()
                and current_date < closest_date
            ):
                closest_date = current_date

        return closest_date.date()

    def get_company_with_the_most_inventory(stock):
        return max(get_company_inventory(stock))

    @classmethod
    def generate(cls, stock):
        fabricacao = cls.get_oldest_manufacturing_date(stock)
        validade = cls.get_closest_expiration_date(stock)
        company = cls.get_company_with_the_most_inventory(stock)

        return (
            f'Data de fabricação mais antiga: {fabricacao}\n'
            f'Data de validade mais próxima: {validade}\n'
            f'Empresa com maior quantidade de produtos estocados: '
            f'{company}\n'
        )
