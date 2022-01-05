import time
import psutil
import re

from functions import bytes2human
from functions import commify3


def get_Net():
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
