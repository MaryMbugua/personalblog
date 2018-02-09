from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .. import db,photos
from ..models import Admin,Blogpost
from flask_login import login_required
from .forms import BlogpostForm




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
@login_required
def admin():
    '''
    View root page function that returns the index page and its data
    '''
   

    return render_template('admin.html')
@main.route('/post',methods = ['GET','POST'])
@login_required
def blogpost():
    '''
    View root page function that returns the index page and its data
    '''
    form = BlogpostForm()
    if form.validate_on_submit():
        user = Blogpost(title = form.title.data,date = form.date.data,paragraph1 = form.paragraph1.data,paragraph2 = form.paragraph2.data,paragraph3 = form.paragraph3.data,paragraph4 = form.paragraph4.data)
        db.session.add(user)
        db.session.commit()
        flash("blogpost successfully uploaded")
        return redirect(url_for('main.blogpost'))

    return render_template('post.html',post_form=form)




@main.route('/blogpicsupload',methods = ['GET','POST'])   
@login_required
def blogpics():
    '''
    View root page function that returns the index page and its data
    '''

    return render_template('picsupload.html')
    
@main.route('/blogpicsupload',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
    return render_template('blogpostfinal.html')



