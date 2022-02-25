from .importer import Importer


class CsvImporter(Importer):
    def import_data(self):
        result = []
        if self.split('.')[1] != 'csv':
            raise ValueError("Arquivo inválido")
        else:
            result.extend(self.import_data(self))
            print(result)
        return result
