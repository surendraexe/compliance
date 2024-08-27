
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'views_a629759b6dfa4087863dca34f631b28e.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
