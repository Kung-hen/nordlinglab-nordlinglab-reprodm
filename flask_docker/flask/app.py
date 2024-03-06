#program begins 
#############################################################################################################################

#libraries are declared 
from pydoc import doc
from flask import Flask,  render_template, request,  jsonify, redirect, url_for,flash, Response,send_file



import json
import datetime
import os
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import reprod
import requests
import assess_txt
import grobid_tei_xml
import time
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nnevo0inerv32'
app.config['UPLOAD_FOLDER'] = 'static/files'
GROBID_URL = 'https://cloud.science-miner.com/grobid/api/processFulltextDocument'

#############################################################################################################################

   
   # getting the user to upload the file so we can extract the information
#############################################################################################################################




# checks for code availability
# some authors would provide access to their source code


query_code = [
    ['code', 'software', 'softwares', 'artifact'],
    ['availability', 'available'],
]


# checks for data availability
# some authors provide access to their data

query_data = [
    ['data', 'information', 'materials', 'measurements'],
    ['availability', 'available'],
]
# checks direction availability
query_method = [
    ['directions', 'process', 'procedure', 'technique', 'method'],
    ['availability', 'available'],
]

# in order to perform the checks 
# we need to ask the user to upload the file 
# the user will be prompted

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET', 'POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        # takes the file as input 
        file = form.file.data 

        #checks if file is in pdf format or not 
        global file_name
        file_name=secure_filename(file.filename)
        file_extension=file_name[-4:]
        if file_extension != ".pdf":
        
        # if file is not in pdf format an error message is shown 
        
            flash('Error！It is not pdf file. Please check it again')
            return redirect(url_for('home'))
        
        
        
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/files' ,secure_filename(file.filename))
        print(path)
        
        #next the file is saved 
        file.save(path)
        content = reprod.get_pdf_file_content(path)
        assess_code = assess_txt.txt_reprod(content,query_code,'code')
        assess_data = assess_txt.txt_reprod(content,query_data,'data')
        assess_method = assess_txt.txt_reprod(content,query_method,'method')
        print(assess_code)
        print(assess_data)
        print(assess_method)
        bool_assess_code = True if assess_code[13:]=='available' else False
        bool_assess_data = True if assess_data[13:]=='available' else False
        bool_assess_method = True if assess_method[15:]=='available' else False
        content = reprod.del_all_after_reference(content)
        urls = reprod.get_url(content)
        
        # indicates to the user to wait for a few seconds (2s in this case) while the pdf file is processed 
        
        print("wait 2.0s")
        time.sleep(2.0)
        global pdf
        pdf = requests.post(GROBID_URL, files={'input': open(path, 'rb')}).text  # replace test.pdf by path
        doc = grobid_tei_xml.parse_document_xml(pdf)


#############################################################################################################################

   
   # extracting info 
    
#############################################################################################################################

      # extracts all relevant information from the pdf file 
      
        title = doc.header.title #title of the article 
        print("title: " + doc.header.title)
        print(title)
        
        # prints the first 3 authors
        list_authors =doc.header.authors
        
        # checks if any author is found in file 
        # if no author then "No author" will be displayed as message
        
        
        if len(list_authors) < 1:
            author = "No author"
            
            # if the file contains one or more authors the first (or only author) will be displayed 
            # the message "et al." will follow if more than one author is found 
            # this indicates that there are more authors who wrote this paper 
            # but only the first one will be read 
            
          
        else:
            author = list_authors[0].full_name + " et al."
            
        # doi, number of citations and abstract are printed
        
        # doi
        doi = doc.header.doi
        
        # number of citations 
        citation_count = len(doc.citations)
        
        # abstract 
        abstract = doc.abstract
     
#############################################################################################################################

   
   # processing info into an output file
    
#############################################################################################################################


        # puts paper information in Database.csv 
        
        # the extracted fields will be placed in the .csv file 
        fields = ('doi','title','author','citation_count','code available','data available','method available')
        doc_inf = (doi,title,author,citation_count,bool_assess_code,bool_assess_data,bool_assess_method)
        database_path = os.path.join(os.path.split(os.path.abspath(__file__))[0],"./Database.csv")       
        
        # if database.csv is exist or not
        if os.path.isfile(database_path) == False:
            writer = csv.writer(open(database_path, 'w', newline='', encoding='utf-8'))
            writer.writerow(list(fields))

        # if paper information is exist in database.csv or not    
        exist_in_database = False
        csvfile=open(database_path,'r')
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['doi'] == doi:
                exist_in_database = True
                break 
        
        # write paper information in database            
        if exist_in_database == False:
            writer = csv.writer(open(database_path, 'a', newline='', encoding='utf-8'))
            writer.writerow(list(doc_inf))            

        os.remove(path)
        return render_template('references.html', assess_code=assess_code, assess_data=assess_data, assess_method=assess_method, form=form, urls = urls, title = title, author=author, citation_count = citation_count, doi = doi, abstract = abstract)
    return render_template('home.html', form=form)
    
    
    
    
    
    

#############################################################################################################################

  # getting the processed file with all the info extracted as an output


#############################################################################################################################




# after information has been written in the .csv file then we want to output that file 
@app.route("/get_csv")
def get_csv():
    return Response(pdf,headers={"Content-disposition":"attachment; filename="+file_name[:-4]+".xml"})

@app.route("/get_data")
def get_data():
    return send_file('Database.csv') #returns a .csv file as output 
    
    
    
    
    
    
    
    
#############################################################################################################################
# program ends 