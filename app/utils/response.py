from flask import jsonify
# 成功响应模板
# def success_response(data, status_code=200):
#     return jsonify({
#         "code": status_code,
#         'status': 'success',
#         'data': data
#     }), status_code

# # 错误响应模板
# def error_response(message, status_code=500):
#     return jsonify({
#         "code": status_code,
#         'status': 'error',
#         'message': message
#     }), status_code


# 成功响应模板
def success_response(data, status_code=200):
    return {
        "code": status_code,
        'status': 'success',
        'data': data
    }

# 错误响应模板
def error_response(message, status_code=500):
    return {
        "code": status_code,
        'status': 'error',
        'message': message
    }