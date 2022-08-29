from wtforms import Form, StringField, DecimalField, IntegerField, TextAreaField, PasswordField, validators

class RegisterForm(Form):
    name = StringField('fullname',[validators.Length(min=1,max=50)])
    username= StringField('username',[validators.Length(min=4,max=25)])
    email= StringField('email',[validators.Length(min=6,max=50)])
    password= PasswordField('password',[validators.DataRequired(), validators.EqualTo('confirm',message='passwords do not match')])
    confirm= PasswordField('confirmpassword')