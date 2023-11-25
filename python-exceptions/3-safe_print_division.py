#!/usr/bin/python3
def safe_print_division(a, b):
    try: 
        result = (a / b)
        return result
    except:
        result = none
        return result
    finally:
        print("inside result: {}".format(result))
    return(result)

