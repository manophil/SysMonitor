import platform


def get_Gen():
    uname = platform.uname()
    system = uname.system
    node = uname.node
    kernel = uname.release
    machine = uname.machine
    return uname, system, node, kernel, machine
