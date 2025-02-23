import execjs
print(execjs.get().name)  # 应该返回 "Node.js"

import os
os.environ['EXECJS_RUNTIME'] = 'Node'
