from app import db

#Currently just an example db from tutorial
#NOT implementable
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nickname = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     posts = db.relationship('Post', backref='author', lazy='dynamic')#

#     def __repr__(self):
#         return '<User %r>' % (self.nickname)

class Button(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    buttonText = db.Column(db.String(64), index=True, unique=True)
    buttonType = db.Column(db.String(64))
    #button.children
    children = db.relationship('ChildrenIds', backref='parent', lazy='dynamic')

    def __repr__(self):
        return '<Button %r, isMusicButton=%r' % (self.buttonText, self.isMusicButton)

class ChildrenIds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #childrenIds.parent will return parent (as defined in
    #Button Model)
    parent_id = db.Column(db.Integer, db.ForeignKey('button.id'))



