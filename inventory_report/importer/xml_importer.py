from .importer import Importer


class XmlImporter(Importer):
    def import_data(self):
        result = []
        if self.split('.')[1] != 'xml':
            raise ValueError("Arquivo inválido")
        else:
            result.extend(self.import_data(self.import_file))
        return result
