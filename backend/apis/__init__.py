from flask_restplus import Api

from backend.apis.one import ns as one
from backend.apis.two import ns as two

api = Api(
    title='backend',
    version='1.0',
    description='Python Backend of Flask HelloWorld.',
)

# 将 namespace分支集中注册到api里统一管理
api.add_namespace(one)
api.add_namespace(two)