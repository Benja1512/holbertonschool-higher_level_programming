#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[ret]), end="")
            ret += 1
        except IndexError:
            pass
        print("")
        return (ret)
