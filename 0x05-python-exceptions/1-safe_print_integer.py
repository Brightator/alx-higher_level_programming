#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except(ValueError, TypeError):
        return False
    else:
        return True

#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        int(value)
        return True
    except(ValueError):
        return False
