from flask import render_template,request,redirect,url_for,abort
from . import main
from .. import db
from ..models import Admin
from flask_login import login_required



#Views
@main.route('/')
def index():
    '''
    view  root page function that returns 
    the index page and its data
    '''

    title = 'blog!'

    
    return render_template('index.html',title = title)


@main.route('/admin',methods = ['GET','POST'])
def admin():
    '''
    View root page function that returns the index page and its data
    '''
   

    return render_template('admin.html')
