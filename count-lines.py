""" This module counts the number of lines in standard input
Input: string from the system standard input
This has been added for test
This is confusing
 """

import sys

count = 0
for line in sys.stdin:
    count += 1

print(count, 'lines in standard input')
