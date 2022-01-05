import psutil

from functions import get_size


def get_Mem():
    def get_Svmen():
        svmem = psutil.virtual_memory()
        total = get_size(svmem.total)
        available = get_size(svmem.available)
        used = get_size(svmem.used)
        percentage = get_size(svmem.percent)
        return svmem, total, available, used, percentage

    def get_Swap():
        swap = psutil.swap_memory()
        total = get_size(swap.total)
        used = get_size(swap.used)
        percentage = get_size(swap.percent)
        return swap, total, used, percentage

    svmem = get_Svmen()
    swap = get_Swap()

    return svmem, swap

