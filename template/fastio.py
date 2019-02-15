import os
import sys
from atexit import register
from io import BytesIO

sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))

readline = BytesIO(os.read(0, os.fstat(0).st_size)).readline
write = sys.stdout.write
input = lambda: readline().decode().rstrip('\r\n')


def print(*args, sep=' ', end='\n', f=sys.stdout):
    f.write(sep.join(map(str, args)).encode())
    f.write(end.encode())

