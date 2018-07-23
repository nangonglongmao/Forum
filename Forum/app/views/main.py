from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user
from app.forms import PostsForm
from app.models import Posts
from app.extensions import db


main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostsForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            u = current_user._get_current_object()
            p = Posts(content=form.content.data, user=u)
            db.session.add(p)
            flash('发表成功')
            return redirect(url_for('main.index'))
        else:
            flash('登录后才可发表')
            return redirect(url_for('user.login'))
    # 读取发表的博客
    # posts = Posts.query.filter(Posts.rid == 0).order_by(Posts.timestamp.desc()).all()
    # 分页查询
    page = request.args.get('page', 1, type=int)
    pagination = Posts.query.filter(Posts.rid == 0).order_by(Posts.timestamp.desc()).paginate(page=page, per_page=3, error_out=False)
    # 当页的数据
    posts = pagination.items
    return render_template('main/index.html', form=form, posts=posts, pagination=pagination)


@main.route('/ajax/')
def ajax():
    return render_template('main/ajax.html')


@main.route('/check_ajax/', methods=['GET', 'POST'])
def check_ajax():
    import json
    '''
    if request.method == 'GET':
        name = request.args.get('name')
    else:
        name = request.form.get('name')
    '''
    # values中包含get和post数据
    name = request.values.get('name')
    return json.dumps({'name': name})
