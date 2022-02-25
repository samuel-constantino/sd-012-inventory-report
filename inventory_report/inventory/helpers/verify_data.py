from .read_csv import read_csv
from .read_json import read_json
from .read_xml import read_xml
from ...reports.simple_report import SimpleReport
from ...reports.complete_report import CompleteReport


def verify_path(path):
    extension = path.split('.')[1]
    if extension == 'csv':
        return read_csv(path)
    elif extension == 'json':
        return read_json(path)
    else:
        return read_xml(path)


def verify_data(path, type_report):
    content = verify_path(path)
    if type_report == 'simples':
        return SimpleReport.generate(content)
    else:
        return CompleteReport.generate(content)
