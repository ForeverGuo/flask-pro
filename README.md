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

# 激活虚拟环境
source venv/bin/activate 

# 生成 requirements.txt（包含所有已安装包）
pip freeze > requirements.txt
