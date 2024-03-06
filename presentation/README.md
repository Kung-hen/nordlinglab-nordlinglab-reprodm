# Introduction

Welcome to the NordlingLab-Reprodm Repository. 

This repository contains material for the "Scientific Information Gathering and Processing for Engineering Research" course created by Dr. Torbjšrn Nordling at National Cheng Kung University, Taiwan. 
This repository in specific, contains all the work done in our attempt of creating a web service for predicting reproducibility of scientific articles during the aforementioned course by Prof. Nordling in the Spring Semester 
of 2022. The resulting web service represents the work of all the students and professor working together to make this project a reality. 

But why bother with reproducibilty? In recent years, the awareness and interest of reproducibility of scientific articles have significantly increased, thus, leading to a major reconsideration of how scientific articles should 
be assessed and considered "reproducible". Many scientists have started finding better ways, such as the use of Machine Learning, that are more time efficient, less costly and can be implemented by many more people around the world.
With this web service, we hope to add our contribution in trying to resolve this "reproducbility crisis" (Baker 2016).

# Description

In this repository, one of the first things you can find is the source code used to convert from pdf to xml in the Folder called **Convert Pdf to Xml**. Students have committed and commented their code for better readability.
In the **Report** folder you can find a latex document continuing our Final Report of the Literature Review conducted during this is semester in the course. You can also find initial commits made my each group, however, **technical_report_Final.tex** is 
the class's final report. In addition to that, you can find the figures used in the **Figures** folder. This subfolder would contain figures related to the metrics we used, PRISMA flow charts, tree diagrams etc. 
You can also find the **Flask_docker** and **Flask_webpage** folders in this repository along with some notes on the Technical Report. 

Our web service at it most basic allows a user to upload a PDF file and outputs extracted information from that file. In more detail, when you go to our web service the user is prompted to upload a PDF file. The service works such that when you upload a file,
a check will be performed to confirm that the file being attempted to upload is indeed in PDF (Portable Document Format), i.e. a file with a .pdf extension. Any file that is not a PDF file will cause an error to be shown on the screen. After a successful upload, the file is converted to text 
so that important information is extracted. You can find further information on how our web service uses tools such as GROBID and pdftotext in the **Technial Report** . 

Furthermore, the information we can extract include: article's name, author's name, URLs in the article, and number of references. In addition, the web service is being hosted on an NGINX server and we use Flask framework this web service. Finally, a Docker container is used to ensure that our web service can run on different operating systems. 




# Important Libraries

The following are some important libraries used in building this webservice:

The main dependencies are:

a. Web Framework: 

* [Flask]( https://flask.palletsprojects.com/en/2.1.x/): Web-development Micro Framework

* [WTForms](https://wtforms.readthedocs.io/en/3.0.x/):  to make forms in flask

* [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/): for hosting the web service

b. Natural Language Processing:

* [Nltk](https://www.nltk.org/) 

* [Genism](https://radimrehurek.com/gensim/)

c. Pdf to text conversion:

* [Pdfminer](https://pypi.org/project/pdfminer/)

d. Convert PDF to XML: 

* [PDF to TEI](https://gitlab.com/internetarchive/grobid_tei_xml)
   
   
## Note

This code is Open Source under the Apache 2.0 license and belongs to Nordling Lab/Nordron AB. The students and professor have committed their code to this repository and can be made available as Open Source, that is free to use 
for anyone in the world. Otherwise all individual students would own their code but neither could use the software package because all the code is needed to run the service. Please visit https://www.nordlinglab.org/ for more information. 



