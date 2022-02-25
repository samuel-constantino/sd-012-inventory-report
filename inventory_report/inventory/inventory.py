from .helpers.verify_data import verify_data


class Inventory():

    def import_data(path, type_report):
        return verify_data(path, type_report)
