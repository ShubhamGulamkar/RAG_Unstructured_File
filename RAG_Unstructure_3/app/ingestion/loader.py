from lxml import etree
from io import BytesIO

def load_ccda(xml_content: str):
    parser = etree.XMLParser(recover=True)
    tree = etree.parse(BytesIO(xml_content.encode("utf-8")), parser)
    root = tree.getroot()

    text = []
    for elem in root.iter():
        if elem.text:
            text.append(elem.text.strip())

    return " ".join(text)