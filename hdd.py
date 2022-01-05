import psutil

from functions import get_size


def get_sdb1(partitions):
    sdb1 = partitions[1]
    device = sdb1.device
    mountpoint = sdb1.mountpoint
    fstype = sdb1.fstype
    try:
        sdb1_usage = psutil.disk_usage(mountpoint)
    except PermissionError:
        print("Cpu usage can not be accessed")

    total_size = get_size(sdb1_usage.total)
    used_size = get_size(sdb1_usage.used)
    free_size = get_size(sdb1_usage.free)
    percentage = get_size(sdb1_usage.percent)

    disk_io = psutil.disk_io_counters()
    read = get_size(disk_io.read_bytes)
    write = get_size(disk_io.write_bytes)
    return (
        device,
        mountpoint,
        fstype,
        sdb1_usage,
        total_size,
        used_size,
        free_size,
        percentage,
        read,
        write,
    )


def get_sdb2(partitions):
    sdb2 = partitions[0]
    device = sdb2.device
    mountpoint = sdb2.mountpoint
    fstype = sdb2.fstype
    try:
        sdb2_usage = psutil.disk_usage(mountpoint)
    except PermissionError:
        print("Cpu usage can not be accessed")

    total_size = get_size(sdb2_usage.total)
    used_size = get_size(sdb2_usage.used)
    free_size = get_size(sdb2_usage.free)
    percentage = get_size(sdb2_usage.percent)

    disk_io = psutil.disk_io_counters()
    read = get_size(disk_io.read_bytes)
    write = get_size(disk_io.write_bytes)
    return (
        device,
        mountpoint,
        fstype,
        sdb2_usage,
        total_size,
        used_size,
        free_size,
        percentage,
        read,
        write,
    )


def get_sda(partitions):
    sda = partitions[2]
    device = sda.device
    mountpoint = sda.mountpoint
    fstype = sda.fstype
    try:
        sda_usage = psutil.disk_usage(mountpoint)
    except PermissionError:
        print("Cpu usage can not be accessed")

    total_size = get_size(sda_usage.total)
    used_size = get_size(sda_usage.used)
    free_size = get_size(sda_usage.free)
    percentage = get_size(sda_usage.percent)

    disk_io = psutil.disk_io_counters()
    read = get_size(disk_io.read_bytes)
    write = get_size(disk_io.write_bytes)
    return (
        device,
        mountpoint,
        fstype,
        sda_usage,
        total_size,
        used_size,
        free_size,
        percentage,
        read,
        write,
    )


def get_Hdd():
    partitions = psutil.disk_partitions()
    sdb1 = get_sdb1(partitions)
    sdb2 = get_sdb2(partitions)
    sda1 = get_sda(partitions)


    return sdb1, sdb2, sda1
