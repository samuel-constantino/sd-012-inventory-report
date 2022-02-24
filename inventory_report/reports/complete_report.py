from .simple_report import SimpleReport
from .helpers.company_inventory import get_company_inventory


class CompleteReport(SimpleReport):
    def format_company_inventory(stock):
        companies = get_company_inventory(stock)
        result = ''
        for item in companies:
            result += f'- {item}: {companies[item]}\n'

        return result

    @classmethod
    def generate(cls, stock):
        companies = cls.format_company_inventory(stock)
        print(companies)
        return(
            f'{SimpleReport.generate(stock)}\n'
            f'Produtos estocados por empresa: \n'
            f'{companies}'
        )
