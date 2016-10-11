import psutil


disks = psutil.disk_partitions() #disk partitions


computercpu = psutil.cpu_percent(interval=5, percpu=True) #

print(disks)#prints the number of disk partitions

print(computercpu)#prints the cpu percentage