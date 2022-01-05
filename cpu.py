import cpuinfo
import psutil


def get_Cpu():
    cpu = cpuinfo.get_cpu_info()["brand_raw"]
    cpufreq = psutil.cpu_freq()
    physical_Cores = psutil.cpu_count(logical=False)
    total_Cores = psutil.cpu_count(logical=True)
    max_Frequency = cpufreq.max
    min_Frequency = cpufreq.min
    current_Frequency = cpufreq.current
    cpu_Usage = psutil.cpu_percent(percpu=False)
    cpu_Usage_per_Core = psutil.cpu_percent(percpu=True)
    return (
        cpu,
        cpufreq,
        physical_Cores,
        total_Cores,
        max_Frequency,
        min_Frequency,
        current_Frequency,
        cpu_Usage,
        cpu_Usage_per_Core,
    )
