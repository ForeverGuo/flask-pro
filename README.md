### 电商管理项目

- 功能说明
  1. 登录、注册、注销、修改密码、修改个人信息
  2. 用户管理（增删改查）
  3. 商品管理（增删改查）
  4. 订单管理（增删改查）
  5. 持续更新
  
- 环境要求
  - Python 3.x
  - Flask 3.x
  - Flask-SQLAlchemy 3.x
  - Flask-Restx 1.x

- 虚拟环境激活
  - source venv/bin/activate

- 项目依赖包

```python
pip install -r requirements.txt
```
- 项目结构

```python
my_flask_app/
│
├── app/                      # 应用程序主目录
│   ├── __init__.py           # 初始化应用程序
│   ├── routes/               # 路由模块
│   │   ├── __init__.py
│   │   ├── auth.py           # 认证相关路由
│   │   └── main.py           # 主路由
│   ├── models/               # 数据模型
│   │   ├── __init__.py
│   │   └── user.py           # 用户模型
│   ├── templates/            # 模板文件
│   │   └── index.html        # 首页模板
│   ├── static/               # 静态文件
│   │   └── style.css         # 样式表
│   └── config.py             # 配置文件
│
├── tests/                    # 测试代码
│   └── test_routes.py        # 路由测试
│
├── requirements.txt          # 依赖文件
├── run.py                    # 启动文件
└── config.py                 # 配置文件（可选）
```

- 启动项目

```
python run.py
```

