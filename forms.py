from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField, EmailField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = EmailField("Email", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])
    name = StringField("Name", [validators.InputRequired()])
    submit = SubmitField("Sign Me Up!")


class LoginForm(FlaskForm):
    email = EmailField("Email", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])
    submit = SubmitField("Login!")


class CommentForm(FlaskForm):
    comment = CKEditorField("Leave Your comment here", [validators.input_required()])
    submit = SubmitField("Submit comment!")


class ContactForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired()])
    email = EmailField("Email", [validators.InputRequired()])
    phone = StringField("Phone Number", [validators.InputRequired()])
    message = CKEditorField("Message", [validators.InputRequired()])
    submit = SubmitField("Submit details")