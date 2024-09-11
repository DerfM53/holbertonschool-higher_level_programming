def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{}".format(value))
            return True
    except ValueError:
        return False
