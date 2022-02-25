from csv import DictReader


def read_csv(path):
    with open(path, 'r') as file:
        return [dict for dict in DictReader(file)]
