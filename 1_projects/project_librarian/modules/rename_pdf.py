import PyPDF2
from PIL import Image
import pytesseract

def rename_pdf_files(path):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    for filename in os.listdir(path):
        if filename.endswith('.pdf'):
            pdf_file = open(os.path.join(path, filename), 'rb')
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            page = pdf_reader.getPage(0)
            xobj = page['/Resources']['/XObject'].getObject()

            for obj in xobj:
                if xobj[obj]['/Subtype'] == '/Image':
                    size = (xobj[obj]['/Width'], xobj[obj]['/Height'])
                    data = xobj[obj].getData()
                    if xobj[obj]['/ColorSpace'] == '/DeviceRGB':
                        mode = "RGB"
                    else:
                        mode = "P"

                    if xobj[obj]['/Filter'] == '/FlateDecode':
                        img = Image.frombytes(mode, size, data)
                        text = pytesseract.image_to_string(img)
                        author = None
                        title = None
                        lines = text.split('\n')
                        for line in lines:
                            line = line.strip()
                            if 'by' in line:
                                author = line.split('by')[-1].strip()
                            if 'By' in line:
                                author = line.split('By')[-1].strip()
                            if 'BY' in line:
                                author = line.split('BY')[-1].strip()
                            if 'Title:' in line:
                                title = line.split(':')[-1].strip()
                            if 'TITLE:' in line:
                                title = line.split(':')[-1].strip()
                            if 'title:' in line:
                                title = line.split(':')[-1].strip()
                        if author and title:
                            if validate_author_and_title(author, title):
                                new_filename = author + ' - ' + title + '.pdf'
                                os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
                                break
            pdf_file.close()