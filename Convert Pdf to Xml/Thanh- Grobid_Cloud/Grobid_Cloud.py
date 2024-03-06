import requests
import os
import grobid_tei_xml
GROBID_URL = 'https://cloud.science-miner.com/grobid/api/processFulltextDocument'
xml = requests.post(GROBID_URL, files={'input': open('test.pdf', 'rb')}).text #replace test.pdf by path
doc = grobid_tei_xml.parse_document_xml(xml)

#extract every thing which we need
print("title: " + doc.header.title)
print("authors: " + ", ".join([a.full_name for a in doc.header.authors]))
print("doi: " + str(doc.header.doi))
print("citation count: " + str(len(doc.citations)))
print("abstract: " + doc.abstract)
