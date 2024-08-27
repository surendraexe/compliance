
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'views_59d32d69d93549b1a43293f4bf4e2e24.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
