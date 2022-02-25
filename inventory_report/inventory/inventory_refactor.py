from collections.abc import Iterable
from .helpers.verify_data import verify_data
from .inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, type_report):
        dicts = self.importer.import_data(path)
        self.data += dicts
        return verify_data(path, type_report)

    def __iter__(self):
        return InventoryIterator(self.data)

# Solução baseada no repositório: https://github.dev/tryber/sd-012-inventory-report/pull/47/files