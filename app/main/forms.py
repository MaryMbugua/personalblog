from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogpostForm(FlaskForm):
    title = StringField('title',validators=[Required()])
    date = StringField('date',validators=[Required()])
    paragraph1 = TextAreaField('Paragraph onee...A must',validators=[Required()])
    paragraph2 = TextAreaField('Paragraph two')
    paragraph3 = TextAreaField('Paragraph three')
    paragraph4 = TextAreaField('Paragraph four')
    submit = SubmitField('Submit')

# class PicsuploadForm():
