from datetime import datetime

"""
  @description: 获取当前时间
  @param: None
  @return: 当前时间
  @author: Petter guo
"""
def getNowTime():
    return str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))