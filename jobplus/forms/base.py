from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,ValidationError,TextAreaField,IntegerField,SelectField
from wtforms.validators import Length,Email,EqualTo,Required,URL,NumberRange
