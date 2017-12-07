#常用标准库（模块）
"""
bulidin
os
sys
functools
json
logging
multiprocessing  多任务进程
threading
copy
time
datatime
random
hashlib
socket
re 正则
。。。
"""
#hashlib 加密
import hashlib
m = hashlib.md5()
m.update(b"cmr")
print(m.hexdigest())