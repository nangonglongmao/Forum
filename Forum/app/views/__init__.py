from .main import main
from .user import user
from .posts import posts

# 配置蓝本
DEFAULT_BLUEPRINT = (
    # (蓝本，前缀)
    (main, ''),
    (user, '/user'),
    (posts, '/posts'),
)


def config_blueprint(app):
    for blueprint, url_prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=url_prefix)
