
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'esi-return_869aa3d6d1574f2da524d70110bd19d6.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
