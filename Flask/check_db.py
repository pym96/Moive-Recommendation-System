from app import app, db

with app.app_context():
    try:
        db.engine.connect()
        print("数据库连接成功！")
        # 创建所有表
        db.create_all()
        print("所有数据表已创建/更新")
    except Exception as e:
        print(f"数据库连接错误: {str(e)}") 