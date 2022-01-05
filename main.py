from cpu import get_Cpu
from gen import get_Gen
from hdd import get_Hdd
from mem import get_Mem
from net import get_Net

# GENERAL

general = get_Gen()

system = general[1]
node = general[2]
kernel = general[3]
machine = general[4]

def print_gen(system,node,kernel,machine):
    print('='*40)
    print(f"\n{'System: ' :<20}{system:>20} ")
    print(f"\n{'Node: ':<20}{node:>20} ")
    print(f"\n{'Kernel: ':<20}{kernel:>20} ")
    print(f"\n{'Machine: ':<20}{machine:>20} ")
    print('='*40)

   
# PROCESSOR

processor = get_Cpu()

cpu = processor[0]
cpu_freq = (processor[1][2] + processor[1][1]) / 2
physical_cores = processor[2]
total_cores = processor[3]
max_frequency = processor[4]
current_frequency = processor[5]
cpu_usage = processor[6] / 100
cpu_usage_per_core = processor[7]


def print_cpu(cpu,cpu_freq,physical_cores,total_cores,max_frequency,current_frequency,cpu_usage,cpu_usage_per_core):
    print('='*20)
    print(f"\n{'Cpu: ':<20}{cpu:>20}")
    print(f"\n{'Frequency: ':<20}{str(cpu_freq):>20}")
    print(f"\n{'Physical Cores: ':<20}{str(physical_cores):>20}")
    print(f"\n{'Total Cores: ':<20}{str(total_cores):>20}")
    print(f"\n{'Max Frequency: ':<20}{str(max_frequency):>20}")
    print(f"\n{'Current Frequency':<20}{str(current_frequency):>20}")
    print(f"\n{'Cpu Usage: ':<20}{str(round(cpu_usage)) + '%':>20}")
    print(f"\n{'Usage per Core':<20}{str(cpu_usage_per_core) + '%':>20}")
    print('='*40)


 
# HDD

sdb1,sdb2,sda = get_Hdd()

    # sdb1 HDD

sdb1_device = sdb1[0]
sdb1_mountpoint = sdb1[1]
sdb1_fstype = sdb1[2]
sdb1_usage = sdb1[3][3]
sdb1_total = sdb1[4]
sdb1_used = sdb1[5]
sdb1_free = sdb1[6]
sdb1_percentage = sdb1[7]
sdb1_read = sdb1[8]
sdb1_write = sdb1[9]


def print_sdb1(sdb1_device,sdb1_mountpoint,sdb1_fstype,sdb1_usage,sdb1_total,sdb1_used,sdb1_free,sdb1_percentage,sdb1_read,sdb1_write):

    print('='*40)
    print(f"{'Device: ':<20}{sdb1_device:>20}")
    print(f"{'Mountpoint: ':<20}{sdb1_mountpoint:>20}")
    print(f"{'File System Type: ':<20}{sdb1_fstype:>20}")
    print(f"{'Usage: ':<20}{str(sdb1_usage):>20}")
    print(f"{'Total: ':<20}{sdb1_total:>20}")
    print(f"{'Used: ':<20}{sdb1_used:>20}")
    print(f"{'Free: ':<20}{sdb1_free:>20}")
    print(f"{'Percentage: ':<20}{sdb1_percentage:>20}")
    print(f"{'Read: ':<20}{sdb1_read:>20}")
    print(f"{'Write: ':<20}{sdb1_write:>20}")
    print('='*40)

    # sdb2 HDD

sdb2_device = sdb2[0]
sdb2_mountpoint = sdb2[1]
sdb2_fstype = sdb2[2]
sdb2_usage = sdb2[3][3]
sdb2_total = sdb2[4]
sdb2_used = sdb2[5]
sdb2_free = sdb2[6]
sdb2_percentage = sdb2[7]
sdb2_read = sdb2[8]
sdb2_write = sdb2[9]

def print_sdb2(sdb2_device,sdb2_mountpoint,sdb2_fstype,sdb2_usage,sdb2_total,sdb2_used,sdb2_free,sdb2_percentage,sdb2_read,sdb2_write):

    print('='*40)
    print(f"{'Device: ':<20}{sdb2_device:>20}")
    print(f"{'Mountpoint: ':<20}{sdb2_mountpoint:>20}")
    print(f"{'File System Type: ':<20}{sdb2_fstype:>20}")
    print(f"{'Usage: ':<20}{str(sdb2_usage):>20}")
    print(f"{'Total: ':<20}{sdb2_total:>20}")
    print(f"{'Used: ':<20}{sdb2_used:>20}")
    print(f"{'Free: ':<20}{sdb2_free:>20}")
    print(f"{'Percentage: ':<20}{sdb2_percentage:>20}")
    print(f"{'Read: ':<20}{sdb2_read:>20}")
    print(f"{'Write: ':<20}{sdb2_write:>20}")
    print('='*40)



    # sda1 HDD

sda_device = sda[0]
sda_mountpoint = sda[1]
sda_fstype = sda[2]
sda_usage = sda[3][3]
sda_total = sda[4]
sda_used = sda[5]
sda_free = sda[6]
sda_percentage = sda[7]
sda_read = sda[8]
sda_write = sda[9]


def print_sda(sda_device,sda_mountpoint,sda_fstype,sda_usage,sda_total,sda_used,sda_free,sda_percentage,sda_read,sda_write):

    print('='*40)
    print(f"{'Device: ':<20}{sda_device:>20}")
    print(f"{'Mountpoint: ':<20}{sda_mountpoint:>20}")
    print(f"{'File System Type: ':<20}{sda_fstype:>20}")
    print(f"{'Usage: ':<20}{str(sda_usage):>20}")
    print(f"{'Total: ':<20}{sda_total:>20}")
    print(f"{'Used: ':<20}{sda_used:>20}")
    print(f"{'Free: ':<20}{sda_free:>20}")
    print(f"{'Percentage: ':<20}{sda_percentage:>20}")
    print(f"{'Read: ':<20}{sda_read:>20}")
    print(f"{'Write: ':<20}{sda_write:>20}")
    print('='*40)


def print_hdd(print_sdb1,print_sdb2,print_sda):
    print_sdb1(sdb1_device,sdb1_mountpoint,sdb1_fstype,sdb1_usage,sdb1_total,sdb1_used,sdb1_free,sdb1_percentage,sdb1_read,sdb1_write)
    print_sdb2(sdb2_device,sdb2_mountpoint,sdb2_fstype,sdb2_usage,sdb2_total,sdb2_used,sdb2_free,sdb2_percentage,sdb2_read,sdb2_write)
    print_sda(sda_device,sda_mountpoint,sda_fstype,sda_usage,sda_total,sda_used,sda_free,sda_percentage,sda_read,sda_write)


# MEMORY
svmem, swap  = get_Mem()

    # svmem memory

svmem_total = svmem[1]
svmem_available = svmem[2]
svmem_used = svmem[3]
svmem_percentage = svmem[4]

def print_svmem(svmem_total,svmem_available,svmem_used,svmem_percentage):
    print('='*40)
    print(f"{'Total: ':<20}{svmem_total:>20}")
    print(f"{'Available: ':<20}{svmem_available:>20}")
    print(f"{'Used: ':<20}{svmem_used:>20}")
    print(f"{'Percentage: ':<20}{svmem_percentage:>20}")
    print('='*40)



    #  swap memory

swap_total = swap[1]
swap_used = swap[2]
swap_percentage = swap[3]


def print_swap(swap_total,swap_used,swap_percentage):
    print('='*40)
    print(f"{'Total: ':<20}{swap_total:>20}")
    print(f"{'Used: ':<20}{swap_used:>20}")
    print(f"{'Percentage: ':<20}{swap_percentage:>20}")
    print('='*40)


def print_mem(print_svmem,print_swap):
    print_svmem(svmem_total,svmem_available,svmem_used,svmem_percentage)
    print_swap(swap_total,swap_used,swap_percentage)

# NETWORK   

enp4s0,lo,wlan0 = get_Net()

    # enp4s0

enp4s0_bytes_sent_total = enp4s0[0]
enp4s0_bytes_sent_sec = enp4s0[1]
enp4s0_bytes_recv_total = enp4s0[2]
enp4s0_bytes_recv_sec = enp4s0[3]
enp4s0_packets_sent_total = enp4s0[4]
enp4s0_packets_sent_sec = enp4s0[5]
enp4s0_packets_recv_total = enp4s0[6]
enp4s0_packets_recv_sec = enp4s0[7]


def print_enp4s0(enp4s0_bytes_sent_total, enp4s0_bytes_sent_sec, enp4s0_bytes_recv_total, enp4s0_bytes_recv_sec, enp4s0_packets_sent_total, enp4s0_packets_sent_sec, enp4s0_packets_recv_total, enp4s0_packets_recv_sec):

    print('='*40)
    print(f"{'Bytes Sent: ':<20}{enp4s0_bytes_sent_total:>20}")
    print(f"{'Bytes Sent per Second: ':<20}{enp4s0_bytes_sent_sec:>20}")
    print(f"{'Bytes Received: ':<20}{enp4s0_bytes_recv_total:>20}")
    print(f"{'Bytes Received per Second: ':<20}{enp4s0_bytes_recv_sec:>20}")
    print(f"{'Packets Sent: ':<20}{enp4s0_packets_sent_total:>20}")
    print(f"{'Packets Sent per Second: ':<20}{enp4s0_packets_sent_sec:>20}")
    print(f"{'Packets Received: ':<20}{enp4s0_packets_recv_total:>20}")
    print(f"{'Packets Received per Second: ':<20}{enp4s0_packets_recv_sec:>20}")

    #lo

lo_bytes_sent_total = lo[0]
lo_bytes_sent_sec = lo[1]
lo_bytes_recv_total = lo[2]
lo_bytes_recv_sec = lo[3]
lo_packets_sent_total = lo[4]
lo_packets_sent_sec = lo[5]
lo_packets_recv_total = lo[6]
lo_packets_recv_sec = lo[7]

def print_lo(lo_bytes_sent_total,lo_bytes_sent_sec,lo_bytes_recv_total,lo_bytes_recv_sec,lo_packets_sent_total,lo_packets_sent_sec,lo_packets_recv_total,lo_packets_recv_sec):
    print('='*40)
    print(f"{'Bytes Sent: ':<20}{lo_bytes_sent_total:>20}")
    print(f"{'Bytes Sent per Second: ':<20}{lo_bytes_sent_sec:>20}")
    print(f"{'Bytes Received: ':<20}{lo_bytes_recv_total:>20}")
    print(f"{'Bytes Received per Second: ':<20}{lo_bytes_recv_sec:>20}")
    print(f"{'Packets Sent: ':<20}{lo_packets_sent_total:>20}")
    print(f"{'Packets Sent per Second: ':<20}{lo_packets_sent_sec:>20}")
    print(f"{'Packets Received: ':<20}{lo_packets_recv_total:>20}")
    print(f"{'Packets Received per Second: ':<20}{lo_packets_recv_sec:>20}")
    print('='*40)



    #wlan0

wlan0_bytes_sent_total = wlan0[0]
wlan0_bytes_sent_sec = wlan0[1]
wlan0_bytes_recv_total = wlan0[2]
wlan0_bytes_recv_sec = wlan0[3]
wlan0_packets_sent_total = wlan0[4]
wlan0_packets_sent_sec = wlan0[5]
wlan0_packets_recv_total = wlan0[6]
wlan0_packets_recv_sec = wlan0[7]

def print_wlan0(wlan0_bytes_sent_total,wlan0_bytes_sent_sec,wlan0_bytes_recv_total,wlan0_bytes_recv_sec,wlan0_packets_sent_total,wlan0_packets_sent_sec,wlan0_packets_recv_total,wlan0_packets_recv_sec):
    print('='*40)
    print(f"{'Bytes Sent: ':<20}{wlan0_bytes_sent_total:>20}")
    print(f"{'Bytes Sent per Second: ':<20}{wlan0_bytes_sent_sec:>20}")
    print(f"{'Bytes Received: ':<20}{wlan0_bytes_recv_total:>20}")
    print(f"{'Bytes Received per Second: ':<20}{wlan0_bytes_recv_sec:>20}")
    print(f"{'Packets Sent: ':<20}{wlan0_packets_sent_total:>20}")
    print(f"{'Packets Sent per Second: ':<20}{wlan0_packets_sent_sec:>20}")
    print(f"{'Packets Received: ':<20}{wlan0_packets_recv_total:>20}")
    print(f"{'Packets Received per Second: ':<20}{wlan0_packets_recv_sec:>20}")
    print('='*40)

def print_network(print_enp4s0,print_wlan0,print_lo):
    print_enp4s0(enp4s0_bytes_sent_total, enp4s0_bytes_sent_sec, enp4s0_bytes_recv_total, enp4s0_bytes_recv_sec, enp4s0_packets_sent_total, enp4s0_packets_sent_sec, enp4s0_packets_recv_total, enp4s0_packets_recv_sec)
    print_lo(lo_bytes_sent_total,lo_bytes_sent_sec,lo_bytes_recv_total,lo_bytes_recv_sec,lo_packets_sent_total,lo_packets_sent_sec,lo_packets_recv_total,lo_packets_recv_sec)
    print_wlan0(wlan0_bytes_sent_total,wlan0_bytes_sent_sec,wlan0_bytes_recv_total,wlan0_bytes_recv_sec,wlan0_packets_sent_total,wlan0_packets_sent_sec,wlan0_packets_recv_total,wlan0_packets_recv_sec)




def print_all(print_gen,print_cpu,print_mem,print_hdd,print_network):
    print_gen(system,node,kernel,machine)
    print_cpu(cpu, cpu_freq, physical_cores, total_cores, max_frequency, current_frequency, cpu_usage, cpu_usage_per_core)  
    print_mem(print_svmem,print_swap)
    print_hdd(print_sdb1,print_sdb2,print_sda)
    print_network(print_enp4s0,print_lo,print_wlan0)

print_all(print_gen, print_cpu, print_mem, print_hdd, print_network)