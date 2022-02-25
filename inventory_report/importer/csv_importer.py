from .importer import Importer
from ..inventory.helpers.read_csv import read_csv


class CsvImporter(Importer):
    def import_data(path):
        if '.csv' not in path:
            raise ValueError("Arquivo inválido")

        return read_csv(path)
