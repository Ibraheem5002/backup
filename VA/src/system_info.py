import psutil

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def get_ram_usage():
    ram = psutil.virtual_memory()
    return ram.percent

def get_battery_percentage():
    battery = psutil.sensors_battery()
    if battery:
        return battery.percentage
    else:
        return None

def systemInfo():
    ram = psutil.virtual_memory()
    battery = psutil.sensors_battery()
    cpu_stats = psutil.cpu_stats()

    dic = {
        "ram" : ram.total,
        "cpu" : cpu_stats,
        "battery" : battery
    }
    
    return dic