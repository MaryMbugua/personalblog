from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,FileField,RadioField,BooleanField
from wtforms.validators import Required,AnyOf,Email
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from ..models import Blogpost,Blogpics

class BlogpostForm(FlaskForm):
    title = StringField('title',validators=[Required()])
    date = StringField('date',validators=[Required()])
    category = RadioField('Pick from the following categories',choices=[('lifestyle','Lifestyle'),('fashion','Fashion')],validators=[Required()])
    paragraph1 = TextAreaField('Paragraph onee...A must',validators=[Required()])
    paragraph2 = TextAreaField('Paragraph two')
    paragraph3 = TextAreaField('Paragraph three')
    paragraph4 = TextAreaField('Paragraph four')
    submit = SubmitField('Submit')

class PicsuploadForm(FlaskForm):
    img1 = FileField('img 1 a must',validators=[FileRequired()])
    img2 = FileField('img2')
    img3 = FileField('img3')
    img4 = FileField('img4')
    img5 = FileField('img5')
    img6 = FileField('img6')
    img7 = FileField('img7')
    img8 = FileField('img8')
    img9 = FileField('img9')
    img10 = FileField('img10')
    submit = SubmitField('Submit')

class SubscriptionForm(FlaskForm):
    email = StringField('Email Address',validators=[Required(),Email()])