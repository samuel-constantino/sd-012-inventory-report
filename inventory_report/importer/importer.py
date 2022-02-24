from abc import abstractclassmethod


class Importer():
    def __init__(self, import_file):
        self.import_file = import_file

    @abstractclassmethod
    def import_data(path):
        with open(path) as file:
            return file.read()
