import argparse
from insertion_sort import *
from Bubble_sort import *
from quick_sort import *
from shell_sort import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='main.py')
    parser.add_argument('--insertion', help='insertion sort algorithm',dest='insertion',action="store_true")
    parser.add_argument('--bubble', help='Bubble sort algorithm', dest='bubble',action="store_true")
    parser.add_argument('--quick', help='quick sort algorithm', dest='quick',action="store_true")
    parser.add_argument('--shell', help=' shell sort algorithm', dest='shell',action="store_true")

    args = parser.parse_args()
    if args.insertion:
        sort()
    if args.bubble:
        bubble()
    if args.quick:
        quick_sort()
    if args.shell:
        shell_sort()

