#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install pdfminer
# use the code to install pdfminer from your installerish thing


# In[2]:


from typing import Container
from io import BytesIO, StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, XMLConverter, HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import re
from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')


# In[3]:


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


# In[4]:


path = r"C:\Users\iyusa\Desktop\2nd sem\Scientific information\jupyter notebook\THE JAZZ TRANSFORMER ON THE FRONT LINE EXPLORING THE SHORTCOMINGS OF AI-COMPOSED MUSIC THROUGH QUANTITATIVE MEASURES, Wu.pdf"
text = get_pdf_file_content(path)
text1 = text


# In[5]:


lines = sent_tokenize(text)
ss =''
for l in lines:
    s = l.replace('\n', '')
    #This part we can replace \n with either space or no space, we get different results
    ss += s
    print(s)


# In[6]:


text = ss
ss


# In[7]:


def del_all_after_reference(text):
    text = text.lower()
    idx = text.rfind("references")
    if idx >= 0:
        text = text[:idx]
    return text


# In[8]:


text = del_all_after_reference(text)
text1 = del_all_after_reference(text1)


# In[9]:


def get_url(string):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    url = [_url for _url in url if 'doi.org' not in _url]
    return url


# In[10]:


result_url = get_url(text)
result_url += get_url(text1)
result_url


# In[11]:


# Below starts retrieving from result_url above.
# We will use beutifulsoup4 package, please install if you don't have this package
# pip install beautifulsoup4
# pip install requests


# In[12]:


import requests
from bs4 import BeautifulSoup


# In[13]:


def retrieve_url(url):
    response = requests.get(url)
    url = BeautifulSoup(response.text, "html.parser")
    return url.prettify()  #Outputs result in formatted HTML     


# In[18]:


for i in range(len(result_url)):
    result = retrieve_url(result_url[i])
    print (result_url[i])
    result = result.lower()
    if 'error 404' in result:
        message = "Can't access because of error 404"
    elif 'page not found' in result:
        message = "Can't access because page not found" 
    else:
        message = "Can be accessed!"
    
    print (message)

