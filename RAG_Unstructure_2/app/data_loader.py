from lxml import etree


def load_ccda(file_path: str):
    tree = etree.parse(file_path)
    root = tree.getroot()
    return etree.tostring(root, encoding='unicode')



def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks