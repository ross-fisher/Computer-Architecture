#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *
import os

cpu = CPU()

if __name__ == '__main__':
    assert len(sys.argv) == 2
    cpu.load(os.path.join('examples', sys.argv[1]))
    cpu.run()

