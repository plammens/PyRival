#!/usr/bin/env python3
"""
This file is part of https://github.com/cheran-senthil/PyRival
Copyright 2019 Cheran Senthilkumar <hello@cheran.io>

"""
import os
import sys
from atexit import register
from io import BytesIO

sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))

readline = BytesIO(os.read(0, os.fstat(0).st_size)).readline
write = sys.stdout.write

input = readline().rstrip(b'\r\n').decode


def print(*args, sep=' ', end='\n', f=sys.stdout):
    f.write(sep.join(map(str, args)).encode())
    f.write(end.encode())


def main():
    pass


if __name__ == '__main__':
    main()
