from flask import request, jsonify
from functools import wraps
from pydantic import ValidationError

"""
  请求参数校验 decorator
  @param model_cls: pydantic 模型类
  @param strict: 是否严格校验，默认为 False
  @author petterguo
  @date 2025/05/14
  @return: decorator
"""

def validate_model(model_cls):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 自动提取请求数据（支持 JSON/表单/查询参数）
            data = {}
            if request.is_json:
                data = request.get_json(silent=True) or {}
            elif request.form:
                data = request.form.to_dict()
            else:
                data = request.args.to_dict()
            # 参数校验
            try:
                validated_data = model_cls(**data).dict()
                kwargs.update(validated_data)  # 注入校验后的参数
                return func(*args, **kwargs)
            except ValidationError as e:
                errors = [{"field": err["loc"][0], "msg": err["msg"]} for err in e.errors()]
                return jsonify({"code": 400, "errors": errors}), 400
        return wrapper
    return decorator
