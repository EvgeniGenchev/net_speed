import psutil
import speedtest
from tabulate import tabulate

class network_speed():
    def __init__(self):
        self.tester = psutil.net_if_addrs()
        self.speed = speedtest.Speedtest()
        self.interface = self.interfaces()[0]
        self.download_speed, self.upload_speed = self.speeds()         
        
    def interfaces(self):
        return [str(f) for f, _ in self.tester.items()]

    def speeds(self):
        download_speed  = str(round(self.speed.download() / 1_000_000, 2))
        upload_speed    = str(round(self.speed.upload() / 1_000_000, 2)) 
        return download_speed, upload_speed       

        
    def __str__(self):
        data = {"Interfaces": [self.interface], 
                "Download": [self.download_speed + 'Mbps'],  
                "Upload": [self.upload_speed + 'Mbps' ]}

        return str(tabulate(data, headers="keys", tablefmt="pretty" ))



print(network_speed())
