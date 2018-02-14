from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))



class Admin(UserMixin,db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    def __repr__(self):
        return f'{self.username}'

class Blogpost(UserMixin,db.Model):
    __tablename__ = 'blogposts'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String())
    date = db.Column(db.String(255))
    category = db.Column(db.String(255))
    paragraph1 = db.Column(db.String())
    paragraph2 = db.Column(db.String())
    paragraph3 = db.Column(db.String())
    paragraph4 = db.Column(db.String()) 
    blogpic_id = db.Column(db.Integer,db.ForeignKey('blogpics.id'))
    comment = db.relationship("Comment",backref='blogposts',lazy="dynamic")
    def __repr__(self):
        return f'{self.title}'

    def save_blogposts(self):
        db.session.add(self)
        db.session.commit()
    def delete_blogposts(self):
        db.session.delete(self)
        db.session.commit()

class Blogpics(UserMixin,db.Model):
    __tablename__ = 'blogpics'
    id = db.Column(db.Integer,primary_key = True)
    img1 = db.Column(db.String(255))
    img2 = db.Column(db.String(255))
    img3 = db.Column(db.String(255))
    img4 = db.Column(db.String(255))
    img5 = db.Column(db.String(255))
    img6 = db.Column(db.String(255))
    img7 = db.Column(db.String(255))
    img8 = db.Column(db.String(255))
    img9 = db.Column(db.String(255))
    img10 = db.Column(db.String(255))
    blogposts = db.relationship('Blogpost',backref='Blogpics',lazy="dynamic")

    def __repr__(self):
        return f'{self.img1}'

class Subscriber(UserMixin,db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255),unique = True,index = True)

    def __repr__(self):
        return f'{self.email}'
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    commcontent = db.Column(db.String())
    blogpost_id = db.Column(db.Integer,db.ForeignKey('blogposts.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, blogpost_id):
        comments = Comment.query.filter_by(blogpost_id=blogpost_id).all()

        return comments
