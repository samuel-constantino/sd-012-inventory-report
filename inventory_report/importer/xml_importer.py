from .importer import Importer
from ..inventory.helpers.read_xml import read_xml


class XmlImporter(Importer):
    def import_data(path):
        if '.xml' not in path:
            raise ValueError("Arquivo inválido")

        return read_xml(path)
