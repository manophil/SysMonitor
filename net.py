try:
    import time
except ImportError:
    print("Cannot import time module - this is needed for this application.")
    print("Exiting...")
    sys.exit()

try:
    import psutil
except ImportError:
    print("Cannot import psutil module - this is needed for this application.")
    print("Exiting...")
    sys.exit()

try:
    import re  # Needed for regex
except ImportError:
    print("Cannot import re module - this is needed for this application.")
    print("Exiting...")
    sys.exit()


def get_Net():
    def bytes2human(n):
        """
        >>> bytes2human(10000)
        '9.8 K'
        >>> bytes2human(100001221)
        '95.4 M'
        """
        symbols = ("K", "M", "G", "T", "P", "E", "Z", "Y")
        prefix = {}
        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10
        for s in reversed(symbols):
            if n >= prefix[s]:
                value = float(n) / prefix[s]
                return "%.2f %s" % (value, s)
        return "%.2f B" % (n)

    # end def

    #
    # Routine to add commas to a float string
    #
    def commify3(amount):
        amount = str(amount)
        amount = amount[::-1]
        amount = re.sub(r"(\d\d\d)(?=\d)(?!\d*\.)", r"\1,", amount)
        return amount[::-1]

    # end def commify3(amount):

    # ===================
    # Main Python section
    # ===================

    # Before
    tot_before = psutil.net_io_counters()
    pnic_before = psutil.net_io_counters(pernic=True)

    # sleep some interval so we can compute rates
    interval = 0.2
    time.sleep(interval)

    tot_after = psutil.net_io_counters()
    pnic_after = psutil.net_io_counters(pernic=True)

    # start output:
    total_sent = bytes2human(tot_after.bytes_sent)
    total_recv = bytes2human(tot_after.bytes_recv)

    nic_names = list(pnic_after.keys())
    nic_names.sort(key=lambda x: sum(pnic_after[x]), reverse=True)
    print("Interface:")

    def get_enp4s0(nic_names):
        enp4s0 = nic_names[0]
        stats_before = pnic_before[enp4s0]
        stats_after = pnic_after[enp4s0]
        bytes_sent_total = bytes2human(stats_after.bytes_sent)
        bytes_sent_sec = (
            bytes2human(stats_after.bytes_sent - stats_before.bytes_sent) + "/s"
        )
        bytes_recv_total = bytes2human(stats_after.bytes_recv)
        bytes_recv_sec = (
            bytes2human(stats_after.bytes_recv - stats_before.bytes_recv) + "/s"
        )
        packets_sent_total = commify3(stats_after.packets_sent)
        packets_sent_sec = (
            commify3(stats_after.packets_sent - stats_before.packets_sent) + "/s"
        )
        packets_recv_total = commify3(stats_after.packets_recv)
        packets_recv_sec = (
            commify3(stats_after.packets_recv - stats_before.packets_recv) + "/s"
        )

        return (
            bytes_sent_total,
            bytes_sent_sec,
            bytes_recv_total,
            bytes_recv_sec,
            packets_sent_total,
            packets_sent_sec,
            packets_recv_total,
            packets_recv_sec,
        )

    def get_lo(nic_names):
        lo = nic_names[1]
        stats_before = pnic_before[lo]
        stats_after = pnic_after[lo]
        bytes_sent_total = bytes2human(stats_after.bytes_sent)
        bytes_sent_sec = (
            bytes2human(stats_after.bytes_sent - stats_before.bytes_sent) + "/s"
        )
        bytes_recv_total = bytes2human(stats_after.bytes_recv)
        bytes_recv_sec = (
            bytes2human(stats_after.bytes_recv - stats_before.bytes_recv) + "/s"
        )
        packets_sent_total = commify3(stats_after.packets_sent)
        packets_sent_sec = (
            commify3(stats_after.packets_sent - stats_before.packets_sent) + "/s"
        )
        packets_recv_total = commify3(stats_after.packets_recv)
        packets_recv_sec = (
            commify3(stats_after.packets_recv - stats_before.packets_recv) + "/s"
        )

        return (
            bytes_sent_total,
            bytes_sent_sec,
            bytes_recv_total,
            bytes_recv_sec,
            packets_sent_total,
            packets_sent_sec,
            packets_recv_total,
            packets_recv_sec,
        )

    def get_wlan0(nic_names):
        wlan0 = nic_names[2]
        stats_before = pnic_before[wlan0]
        stats_after = pnic_after[wlan0]
        bytes_sent_total = bytes2human(stats_after.bytes_sent)
        bytes_sent_sec = (
            bytes2human(stats_after.bytes_sent - stats_before.bytes_sent) + "/s"
        )
        bytes_recv_total = bytes2human(stats_after.bytes_recv)
        bytes_recv_sec = (
            bytes2human(stats_after.bytes_recv - stats_before.bytes_recv) + "/s"
        )
        packets_sent_total = commify3(stats_after.packets_sent)
        packets_sent_sec = (
            commify3(stats_after.packets_sent - stats_before.packets_sent) + "/s"
        )
        packets_recv_total = commify3(stats_after.packets_recv)
        packets_recv_sec = (
            commify3(stats_after.packets_recv - stats_before.packets_recv) + "/s"
        )

        return (
            bytes_sent_total,
            bytes_sent_sec,
            bytes_recv_total,
            bytes_recv_sec,
            packets_sent_total,
            packets_sent_sec,
            packets_recv_total,
            packets_recv_sec,
        )

    enp4s0 = get_enp4s0(nic_names)
    lo = get_lo(nic_names)
    wlan0 = get_wlan0(nic_names)

    return enp4s0, lo, wlan0
