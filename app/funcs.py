def msg_welcome(name):
    result = "Hi {}!".format(name)
    return result


def printer(result):
    print(result)


def print_welcome(name, my_print=print):
    result = "Hi {}!".format(name)
    my_print(result)


if __name__ == '__main__':
    print_welcome('Alfred')
