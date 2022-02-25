from .importer import Importer
from ..inventory.helpers.read_json import read_json


class JsonImporter(Importer):
    def import_data(path):
        extension = path.split('.')[1]

        if extension != 'json':
            raise ValueError("Arquivo inválido")

        return read_json(path)
