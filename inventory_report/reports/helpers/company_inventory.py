def get_company_inventory(stock):
    company_inventory = {}

    for product in stock:
        if product['nome_da_empresa'] not in company_inventory:
            company_inventory[product['nome_da_empresa']] = 1
        else:
            company_inventory[product['nome_da_empresa']] += 1

    return company_inventory
