#!/usr/bin/env python3

# import sys
import fileinput


# minimum length of a line.
MINLINE = 6


def splitat(line, st, nd):
    print(line[st:nd+1])


# for line in sys.stdin.read().split('\n'):
for line in fileinput.input(inplace=True):

    last = 0
    for i in range(len(line)):
        if (
            i > last+MINLINE
            and i < len(line) - MINLINE
            and (line[i] in "!?…"
                 or line[i] == '.'
                 and line[i-1] != 'M'  # do not break at M. Potter
                 )
            # do not break "smth… rest or smth~? said"
            and not line[i+2].islower()
            and line[i+1] == ' '
        ):
            # candidate for split
            if line[i+2] == '»':
                splitat(line, last, i+2)
                last = i+4
            else:
                splitat(line, last, i)
                last = i+2

    print(line[last:], end='')
    # splitat(line, last, len(line))
