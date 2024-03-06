from typing import Container
from io import BytesIO, StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, XMLConverter, HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import re
import requests
from bs4 import BeautifulSoup

def get_pdf_file_content(path_to_pdf):
    '''
    path_to_pdf: is the parameter that will give access to the PDF File 
    we want to extract the content.
    '''
    
    '''
    PDFResourceManager is used to store shared resources such as fonts or images that 
    we might encounter in the files. 
    '''
    
    resource_manager = PDFResourceManager(caching=True)
    
    '''
    create a string object that will contain the final text the representation of the pdf. 
    '''
    out_text = StringIO()
    '''
    UTF-8 is one of the most commonly used encodings, and Python often defaults to using it.
    In our case, we are going to specify in order to avoid some encoding errors.
    '''
    codec = 'utf-8'
    
    """
    LAParams is the object containing the Layout parameters with a certain default value. 
    """
    laParams = LAParams()
    
    '''
    Create a TextConverter Object, taking :
    - ressource_manager,
    - out_text 
    - layout parameters.
    '''
    text_converter = TextConverter(resource_manager, out_text, laparams=laParams)
    fp = open(path_to_pdf, 'rb')
    
    '''
    Create a PDF interpreter object taking: 
    - ressource_manager 
    - text_converter
    '''
    interpreter = PDFPageInterpreter(resource_manager, text_converter)

    '''
    We are going to process the content of each page of the original PDF File
    '''
    for page in PDFPage.get_pages(fp, pagenos=set(), maxpages=0, password="", caching=True, check_extractable=True):
        interpreter.process_page(page)

    '''
    Retrieve the entire contents of the “file” at any time 
    before the StringIO object’s close() method is called.
    '''
    text = out_text.getvalue()

    '''
    Closing all the ressources we previously opened
    '''
    fp.close()
    text_converter.close()
    out_text.close()
    
    '''
    Return the final variable containing all the text of the PDF
    '''
    return text

def del_all_after_reference(text):
    text = text.lower()
    idx = text.rfind("references")
    print(idx)
    if idx >= 0:
        text = text[:idx]
    return text

def get_url(x):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\s\S*', str(x))
    return url

if __name__ == '__main__':
    print('ok')
    main()