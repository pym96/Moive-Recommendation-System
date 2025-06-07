# -*- codeing = utf-8 -*-

# @File :model.py
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from sqlalchemy import and_

from base.core import db
ma = Marshmallow()

# 这里定义的用户的模型，和数据库的映射关系
# 字段是和数据库一致的
class User(db.Model):
    __tablename__ = 'tb_user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(255))  # 用户姓名
    age = db.Column(db.Integer)  # 用户年龄
    password = db.Column(db.String(255))
    realname = db.Column(db.String(255))  # 昵称
    idno = db.Column(db.String(50))
    avatar = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    intro = db.Column(db.String(100))
    addr = db.Column(db.String(100))
    bal = db.Column(db.DECIMAL)

    def __repr__(self):
        return '<User %r>' % self.username

# 这个是Marshmallow的类，用来灌装json用的
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True
        sqla_session = db.session

user_schema = UserSchema(many=False)

class ChartData(ma.Schema):
    class Meta:
        fields = ('name', 'value')
        
    # Add explicit field declarations
    name = fields.Str()
    value = fields.Int()

chart_data = ChartData(many=True)

############################################
# 辅助函数、装饰器
############################################

# 登录检验（用户名、密码验证）
def valid_login(username, password):
    user = User.query.filter(and_(User.username == username, User.password == password)).first()
    if user:
        return True
    else:
        return False

# 验证注册，用户名是否注册过
def valid_register(username):
    user = User.query.filter(User.username == username).first()
    if user:
        return False
    else:
        return True

