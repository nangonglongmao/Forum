from flask import Flask, render_template
from app.config import config
from app.extensions import config_extensions
from app.views import config_blueprint

# 创建app，需要指定配置名字，以便灵活创建对象
def create_app(config_name):
    # 创建应用实例
    app = Flask(__name__)
    # 配置初始化
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # 配置扩展
    config_extensions(app)
    # 配置蓝本
    config_blueprint(app)
    # 配置错误显示页面
    config_errorhandler(app)
    # 返回对象
    return app


def config_errorhandler(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html')
