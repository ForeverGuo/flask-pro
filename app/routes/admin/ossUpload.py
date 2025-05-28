import uuid
from flask import Blueprint, request
import os
import oss2
from app.utils.response import success_response, error_response

upload_bp = Blueprint('alioss', __name__, url_prefix='/alioss')

access_key_id = os.getenv("ALI_OSS_KEY")
access_key_secret = os.getenv("ALI_OSS_KEY_SECRET")
bucket_name = os.getenv("ALI_OSS_BUCKET")
oss_endpoint = os.getenv("ALI_OSS_ENDPOINT")
remote_file = ""

# 允许的文件扩展名
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp', 'pdf', 'doc', 'docx', 'xls', 'xlsx'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@upload_bp.route('/upload', methods=['POST'])
def upload_file():
  print(request.files)
  if 'file' not in request.files:
    return error_response("No file part")
  file = request.files['file']
  if file and allowed_file(file.filename):
    original_filename = file.filename
    file_extension = original_filename.rsplit('.', 1)[1].lower()
    unique_filename = f"{uuid.uuid4()}.{file_extension}"
    remote_file = f"mall/{unique_filename}"

  # 获取文件的 MIME 类型，大多数浏览器在上传时会提供正确的类型
  content_type = file.mimetype if file.mimetype else 'application/octet-stream'
  print(content_type)
  try:
    # 创建认证对象
    auth = oss2.Auth(access_key_id, access_key_secret)
    # 创建 bucket 对象
    bucket = oss2.Bucket(auth, oss_endpoint, bucket_name)

    result = bucket.put_object(
       remote_file, 
       file.stream, 
       headers={'Content-Type': content_type}
    )
    
    if result.status == 200:
       # 成功后的URL
       ossImageUrl = f"https://{bucket_name}.{oss_endpoint}/{remote_file}"
       return success_response({
          "imageUrl": ossImageUrl,
          "message": "上传成功"
       })
    else:
       return error_response("上传失败", result.status)

  except oss2.exceptions.OssError as e:
      # 捕获并处理 OSS 相关的错误
      #print(f"OSS 错误发生: {e.code} - {e.message}")
      return error_response(f"上传失败{e.message}") # 表示上传失败
  except FileNotFoundError:
      # 处理本地文件不存在的错误
      return error_response("上传失败, 文件未找到") # 表示上传失败
  except Exception as e:
      # 捕获其他可能的错误
      #print(f"发生未知错误: {e}")
      return error_response(f"上传失败{e.message}") # 表示上传失败
