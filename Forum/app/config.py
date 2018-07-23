import os

base_dir = os.path.abspath(os.path.dirname(__file__))

# 通用配置
class Config:
    # 秘钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'
    # session是否永久有效
    SESSION_PERMANENT = True
    # 数据库
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 邮件发送
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.1000phone.com'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'lijie@1000phone.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '123456'
    # 使用本地bootstrap库
    BOOTSTRAP_SERVE_LOCAL = True
    # 文件上传
    MAX_CONTENT_LENGTH = 1024 * 1024 * 8
    UPLOADED_PHOTOS_DEST = os.path.join(base_dir, 'static/upload')

    # 初始化函数，即使没有内容也建议写上，
    # 可以在需要时使用统一接口完成特点环境的初始化
    @staticmethod
    def init_app(app):
        pass


# 开发环境配置
class DevelopConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'blog-dev.sqlite')


# 测试环境配置
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'blog-test.sqlite')


# 生产环境配置
class ProductConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'blog.sqlite')


# 配置字典
config = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'product': ProductConfig,
    'default': DevelopConfig
}