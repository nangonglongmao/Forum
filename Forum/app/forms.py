from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from app.models import User
from app.extensions import photos


# 用户注册
class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[Length(6, 20, message='用户名必须在6~20个字符之间')])
    password = PasswordField('密码', validators=[Length(4, 12, message='密码长度必须在4~12个字符之间')])
    confirm = PasswordField('确认密码', validators=[EqualTo('password', message='两次密码不一致')])
    email = StringField('邮箱', validators=[Email(message='无效的邮箱格式')])
    submit = SubmitField('立即注册')

    # 自定义验证函数，验证username
    def validate_username(self, field):
        if User.query.filter(User.username == field.data).first():
            raise ValidationError('该用户已注册，请选用其他名称')
        return True

    # 自定义验证函数，验证email
    def validate_email(self, field):
        if User.query.filter(User.email == field.data).first():
            raise ValidationError('该邮箱已注册，请选用其他邮箱')
        return True


# 用户登录表单
class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(message='用户名不能为空')])
    password = PasswordField('密码', validators=[DataRequired(message='密码不能为空')])
    remember = BooleanField('记住我')
    submit = SubmitField('立即登录')


# 上传头像表单
class UploadForm(FlaskForm):
    icon = FileField('头像', validators=[FileRequired('请选择文件'), FileAllowed(photos, '只能上传图片')])
    submit = SubmitField('上传')


# 发表博客表单
class PostsForm(FlaskForm):
    content = TextAreaField('', validators=[Length(3, 140, message='说话注意分寸(3~140)')], render_kw={'placeholder': '这一刻的想法...'})
    submit = SubmitField('发表')
