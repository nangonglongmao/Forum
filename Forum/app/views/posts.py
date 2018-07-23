from flask import Blueprint, jsonify
from flask_login import current_user


posts = Blueprint('posts', __name__)


@posts.route('/collect/<int:pid>/')
def collect(pid):
    # 判断是否收藏
    if current_user.is_favorite(pid):
        # 取消收藏
        current_user.del_favorite(pid)
    else:
        # 添加收藏
        current_user.add_favorite(pid)
    return jsonify({'result': 'ok'})
