import os
import time

from flask import Flask, request, send_from_directory
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from api.movieApi import movieBp
from api.userApi import userBp
from base.core import JSONEncoder, db
from base.response import ResMsg
from deeplearning.predict_lstm import sentimentalAnalysis_single

app = Flask(__name__)
# 注册用户相关的方法
app.register_blueprint(userBp, url_prefix='/user')
# 注册电影相关的方法
app.register_blueprint(movieBp, url_prefix='/movie')

# 数据库配置信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Pan114715@localhost/flask_douban_comment'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 前端返回的JSON用ASCII编码关闭，否则浏览器里面看到的文本会是乱码
app.config['JSON_AS_ASCII'] = False
# Flask必须的配置
app.config['SECRET_KEY'] = 'KJDFLSjfldskj'

UPLOAD_FOLDER = "upload"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'xls', 'JPG', 'PNG', 'gif', 'GIF'])

# 日志系统配置
# handler = logging.FileHandler('./error.log', encoding='UTF-8')
# logging_format = logging.Formatter(
#             '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
# handler.setFormatter(logging_format)
# app.logger.addHandler(handler)

# 返回json格式转换 使用这个的话就不需要每次都写json返回了，简化代码
app.json_provider_class = JSONEncoder

# 初始化数据库
db.init_app(app)
# Marshmallow 是用来封装返回SQLAlchemy 的返回结果的，通过这个包可以直接把数据转成JSON，从而返回给前端使用
ma = Marshmallow(app)


# 用来捕捉服务器运行过程中的500-内部错误，并给前端返回信息
@app.errorhandler(500)
def special_exception_handler(error):
    app.logger.error(error)
    return '请联系管理员', 500


# 判断文件后缀
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/file/upload', methods=['POST'], strict_slashes=False)
def api_upload():
    res = ResMsg()
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['myfile']
    if f and allowed_file(f.filename):
        fname = f.filename
        # fname = secure_filename(f.filename)
        print(fname)
        ext = fname.rsplit('.', 1)[1]
        unix_time = int(time.time())
        new_filename = str(unix_time) + '.' + ext
        f.save(os.path.join(file_dir, new_filename))
    res.update(data=new_filename, code=0)
    return res.data



@app.route('/file/download/<filename>/')
def api_download(filename):
    # print('下载..' + filename)
    return send_from_directory('upload', filename, as_attachment=False)





# 深度学习情感分析接口
@app.route('/deeplearning/senti_single', methods=['POST'])
def senti_single():
    res = ResMsg()
    data = request.json['data']
    datas = [data]
    print(datas)
    result = sentimentalAnalysis_single(datas)
    res.update(msg="成功", code=0, data=result)
    return res.data


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
