import numpy as np
import matplotlib.pyplot as plt
import csv
from threading import Timer
from apscheduler.scheduler import Scheduler
import psutil
import urllib.request
from scipy._lib.six import xrange


FILE = r'C:\Users\mayar\Desktop\Python\Monitor\monitor_data.txt'


class Monitor(object):
    def __init__(self, runtime, sample_rate, sample_parameters=[]):
        self.runtime = int(runtime)
        self.sample_rate = int(sample_rate)
        self.sample_parameters = sample_parameters
        self.CPU = []
        self.battery = []
        self.network = []
        self.RAM = []
        self.data_rows = []

        with open(FILE, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter='^')
            for row in csv_reader:
                self.data_rows.append(row)

        sched = Scheduler()
        sched.add_interval_job(self.start_sampling, seconds=self.sample_rate)
        sched.start()
        time = self.runtime + self.sample_rate
        Timer(time, self.stop).start()

    def save_data(self):
        cpu_usage = np.array(self.CPU)
        ram_usage = np.array(self.RAM)
        network = np.array(self.network)
        battery_percentages = np.array(self.battery)
        fieldnames = ['runtime', 'sample_rate', 'CPU_usage', 'RAM_usage', 'network', 'battery']
        with open(FILE, mode='w') as csv_file:
            writer = csv.DictWriter(csv_file, delimiter='^', fieldnames=fieldnames)
            writer.writeheader()
            for row in self.data_rows:
                writer.writerow(row)
            writer.writerow({'runtime': str(self.runtime),
                             'sample_rate': str(self.sample_rate),
                             'CPU_usage': str(cpu_usage),
                             'RAM_usage': str(ram_usage),
                             'network': str(network),
                             'battery': str(battery_percentages)})

    def CPU_graphs(self, time):
        cpu_usage = np.array(self.CPU)
        cpu_max = cpu_usage.max()
        fig, (ax1, ax2) = plt.subplots(2, 1)
        fig.suptitle('CPU usage')
        ax1.plot(time, cpu_usage, 'tab:orange')
        ax2.set_xlim(time[0] - 0.5, time[-1:] + 0.5)
        for i in xrange(cpu_usage.__len__()):
            if cpu_usage[i] == cpu_max:
                ax2.scatter(time[i], cpu_max, c='g')
        ax1.set_title('values')
        ax2.set_title('peaks')
        for ax in fig.get_axes():
            ax.label_outer()
        return fig

    def RAM_graphs(self, time):
        ram_usage = np.array(self.RAM)
        ram_max = ram_usage.max()
        fig, (ax1, ax2) = plt.subplots(2, 1)
        fig.suptitle('RAM usage')
        ax1.plot(time, ram_usage, 'tab:red')
        ax2.set_xlim(time[0] - 0.5, time[-1:] + 0.5)
        for i in xrange(ram_usage.__len__()):
            if ram_usage[i] == ram_max:
                ax2.scatter(time[i], ram_max, c='b')
        ax1.set_title('values')
        ax2.set_title('peaks')
        for ax in fig.get_axes():
            ax.label_outer()
        return fig

    def network_graphs(self, time):
        net = np.array(self.network)
        net_max = net.max()
        fig, (ax1, ax2) = plt.subplots(2, 1)
        fig.suptitle('network')
        ax1.plot(time, net, 'tab:orange')
        ax2.set_xlim(time[0] - 0.5, time[-1:] + 0.5)
        for i in xrange(net.__len__()):
            if net[i] == net_max:
                ax2.scatter(time[i], net_max, c='b')
        ax1.set_title('values')
        ax2.set_title('peaks')
        for ax in fig.get_axes():
            ax.label_outer()
        return fig

    def battery_graphs(self, time):
        battery_percentages = np.array(self.battery)
        battery_max = battery_percentages.max()
        fig, (ax1, ax2) = plt.subplots(2, 1)
        fig.suptitle('battery percentages')
        ax1.plot(time, battery_percentages, 'tab:red')
        ax2.set_xlim(time[0] - 0.5, time[-1:] + 0.5)
        for i in xrange(battery_percentages.__len__()):
            if battery_percentages[i] == battery_max:
                ax2.scatter(time[i], battery_max, c='b')
        ax1.set_title('values')
        ax2.set_title('peaks')
        for ax in fig.get_axes():
            ax.label_outer()
        return fig

    def status_graph(self, names, values):

        """this is my graph, it shows a monitor of all the sampled
           parameters at the end, to show the computer's activity"""

        plt.rcdefaults()
        fig, ax = plt.subplots(figsize=(18, 4))
        y_pos = np.arange(len(names))
        performance = np.array(values)
        error = np.random.rand(len(names))
        ax.barh(y_pos, performance, xerr=error, align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(names)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Performance')
        ax.set_title('your current computer monitor')
        for i, v in enumerate(values):
            ax.text(v + 1, i + .1, str(v), color='green', fontweight='bold')
        return fig

    def build_graphs(self):
        time = np.arange(0, self.runtime, self.sample_rate)
        values = []
        if self.CPU.__len__() > 0:
            self.CPU_graphs(time)
            values.append(self.CPU[self.CPU.__len__() - 1])
        if self.RAM.__len__() > 0:
            self.RAM_graphs(time)
            values.append(self.RAM[self.RAM.__len__() - 1] / 500000000)
        if self.battery.__len__() > 0:
            self.battery_graphs(time)
            values.append(self.battery[self.battery.__len__() - 1])
        if self.network.__len__() > 0:
            self.network_graphs(time)
            values.append(self.network[self.network.__len__() - 1])
        names = []
        for value in self.sample_parameters:
            if value == 'RAM':
                val = value + ' usage' + r' /500000000'
            elif value == 'CPU':
                val = value + ' usage'
            elif value == 'network':
                val = value + ' connection'
            else:
                val = value + ' percentage'
            names.append(val)
        self.my_graph(names, values)

        plt.show()

    def CPU_sampling(self):
        usage = psutil.cpu_percent(interval=1)
        self.CPU.append(int(usage))

    def RAM_sampling(self):
        memory = str(psutil.swap_memory())
        used_index = memory.find('used')
        memory = memory[used_index + 5:]
        comma_index = memory.find(',')
        memory = memory[:comma_index]
        self.RAM.append(int(memory))

    def battery_sampling(self):

        """on windows i couldn't sample the temperature
           so i sampled the battery instead"""

        battery = str(psutil.sensors_battery())
        percent_index = battery.find('percent')
        battery = battery[percent_index + 8:]
        comma_index = battery.find(',')
        battery = int(battery[:comma_index])
        self.battery.append(battery)

    def network_sampling(self):
        host = 'http://google.com'
        try:
            urllib.request.urlopen(host)  # Python 3.x
            is_connected = 1
        except:
            is_connected = 0
        self.network.append(is_connected)

    def start_sampling(self):
        for parameter in self.sample_parameters:
            if parameter == 'CPU':
                self.CPU_sampling()
            if parameter == 'RAM':
                self.RAM_sampling()
            if parameter == 'network':
                self.network_sampling()
            if parameter == 'battery':
                self.battery_sampling()

    def stop(self):
        self.save_data()
        self.build_graphs()
