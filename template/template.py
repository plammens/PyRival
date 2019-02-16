#!/usr/bin/env python3
"""
This file is part of https://github.com/cheran-senthil/PyRival
Copyright 2019 Cheran Senthilkumar <hello@cheran.io>

"""
import os
from atexit import register
from io import BytesIO

stdout = BytesIO()
register(lambda: os.write(1, stdout.getvalue()))

readline = BytesIO(os.read(0, os.fstat(0).st_size)).readline
write = stdout.write
input = lambda: readline().decode().rstrip('\r\n')


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)).encode())
    stdout.write(end.encode())


def main():
    pass


if __name__ == '__main__':
    main()
