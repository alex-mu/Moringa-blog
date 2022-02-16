#import os
#from flask_sqlalchemy import SQLAlchemy
###from flask import app

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/moringablog.db'
#db = SQLAlchemy(app)

#class Blogpost(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(50))
#     subtitle = db.Column(db.String(50))
#     author = db.Column(db.String(20))
#     date_posted = db.Column(db.DateTime)
#     content = db.Column(db.Text)


# if __name__ == '__main__':
#     app.run(debug=True)