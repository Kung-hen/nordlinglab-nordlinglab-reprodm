from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
import json
import datetime
import os
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from . import reprod

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        # path = os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/files' ,secure_filename(file.filename))
        file.save(path) # Then save the file
        content = reprod.get_pdf_file_content(path)
        content = reprod.del_all_after_reference(content)
        urls = reprod.get_url(content)
        os.remove(path)
        return render_template('references.html', form=form, urls = urls)
    return render_template('home.html', form=form)