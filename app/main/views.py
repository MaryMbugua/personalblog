from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .. import db,photos
from ..models import Admin,Blogpost,Blogpics,Comment
from flask_login import login_required,current_user
from .forms import BlogpostForm,PicsuploadForm,CommentsForm




#Views
@main.route('/')
def index():
    '''
    view  root page function that returns 
    the index page and its data
    '''

    title = 'blog!'
     
    allposts = Blogpost.query.all()

    
    return render_template('index.html',title = title,allposts=allposts)

@main.route('/blogpost/<int:id>',methods=['GET','POST'])
def singleblogpost(id):
    

    title = 'Blogpost'
    post = Blogpost.query.filter_by(id=id).one()
    
    comments = Comment.get_comments(id)
    singlepost = Blogpost.query.get(id)
    form = CommentsForm()
    if form.validate_on_submit():
        comment = Comment(username = form.username.data,commcontent = form.commcontent.data,blogpost_id=id)
        db.session.add(comment)
        db.session.commit()
        flash("blogpost successfully uploaded")
        return redirect(url_for('main.index'))
        
    
    return render_template('blogpost.html',title = title,singlepost=singlepost,comments=comments,comment_form=form)
@main.route('/blogpost/delete',methods=['GET','POST'])
def delete_comment():
    commentsDelete = Comment.query.filter_by(id=Comment.id).first()
    if commentsDelete:
        commentsDelete.delete_comment()
        return redirect(url_for('main.index'))
    return render_template('blogpost.html',commentsDelete=commentsDelete)


@main.route('/fashion')
def fashion():
    

    title = 'blog!'
     
    allposts = Blogpost.query.all()

    
    return render_template('fashion.html',title = title,allposts=allposts)


@main.route('/lifestyle')
def lifestyle():
    '''
    view  lifestyle page function that returns 
    the lifestyle page and its data
    '''

    title = 'blog!'
     
    allposts = Blogpost.query.all()

    
    return render_template('lifestyle.html',title = title,allposts=allposts)

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
        post = Blogpost(title = form.title.data,date = form.date.data,paragraph1 = form.paragraph1.data,paragraph2 = form.paragraph2.data,paragraph3 = form.paragraph3.data,paragraph4 = form.paragraph4.data,category = form.category.data)
        db.session.add(post)
        db.session.commit()
        flash("blogpost successfully uploaded")
        return redirect(url_for('main.blogpost'))

    return render_template('post.html',post_form=form)




# @main.route('/blogpicsupload',methods = ['GET','POST'])   
# @login_required
# def blogpics():
#     '''
#     View root page function that returns the index page and its data
#     '''

#     return render_template('picsupload.html')

@main.route('/blogpicsupload',methods= ['GET','POST'])
@login_required
def upload_pics():
    form = PicsuploadForm()
    if form.validate_on_submit():
        # user = Blogpics(img1 = form.img1.data,img2 = form.img2.data,img3 = form.img3.data,img4 = form.img4.data,img5 = form.img5.data,img6 = form.img6.data,img7 = form.img7.data,img8 = form.img8.data,img9 = form.img9.data,img10 = form.img10.data)
        # filename = photos.save(request.files['photo'])
        # path = f'photos/{filename}'
        # blogpics.img1 = path1
        # blogpics.img2 = path2
        # blogpics.img3 = path3
        # blogpics.img4 = path4
        # blogpics.img5 = path5
        # blogpics.img6 = path6
        # blogpics.img7 = path7
        # blogpics.img8 = path8
        # blogpics.img9 = path9
        # blogpics.img10 = path10
        # db.session.add(user)

        filename = secure_filename(form.img1.file.filename)
        file_path = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename)

        form.img1.file.save(file_path)
        db.session.add(file_path)

        db.session.commit()
        # return redirect(url_for('main.blogpicsupload'))
    return render_template('picsupload.html',picsupload_form=form)


@main.route('/blogpostfinal',methods = ['GET','POST'])   
@login_required
def blogpostfinal():
    '''
    View root page function that returns the index page and its data
    '''

    return render_template('blogpostfinal.html')








