import docx
from pathlib import Path

def write_document(pathname):
    for i, child in enumerate(Path(pathname).iterdir()):
        content = open(child, 'r').read()
        print(content)
        doc = docx.Document()
        doc.add_heading('TC de Programación', 0)
        p = doc.add_paragraph('Para cada uno de los siguientes códigos en Python, diga su salida:')
        p.bold = True
        doc.add_paragraph(content)
        doc.save('tests/demo.docx')


if __name__ == '__main__':
    write_document('tests')