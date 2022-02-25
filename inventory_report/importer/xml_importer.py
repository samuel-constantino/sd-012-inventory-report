from .importer import Importer
from ..inventory.helpers.read_xml import read_xml


class XmlImporter(Importer):
    def import_data(path):
        extension = path.split('.')[1]

        if extension != 'xml':
            raise ValueError("Arquivo inválido")

        return read_xml(path)
