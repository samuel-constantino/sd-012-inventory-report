import xml.etree.ElementTree as ET


def read_xml(path):
    tree = ET.parse(path)
    root = tree.getroot()
    result = []
    for child in root:
        dict_of_itens = {}
        for item in child.getchildren():
            dict_of_itens[item.tag] = item.text
        result.extend([dict_of_itens])

    return result
