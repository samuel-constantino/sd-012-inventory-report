from .importer import Importer


class JsonImporter(Importer):
    def import_data(self):
        result = []
        if self.split('.')[1] != 'json':
            raise ValueError("Arquivo inválido")
        else:
            result.extend(self.import_data(self))
        return result
