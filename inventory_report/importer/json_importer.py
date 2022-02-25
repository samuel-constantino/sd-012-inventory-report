from ..inventory.helpers.read_json import read_json
from .importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        if '.json' not in path:
            raise ValueError("Arquivo inválido")

        return read_json(path)
