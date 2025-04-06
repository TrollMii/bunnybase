from bunnybase import Hub, Data, clear_bunny, read_bunny, save_as_bunny, read_bunny_history
import time
import random
hub = Hub()


import time
import matplotlib.pyplot as plt

times = []
total_times = []
count = []

_start = time.time()
for i in range(1, 10_000_000):
    num = random.randint(1,1000)
    start = time.time()
    hub << Data('number', num=num)
    end = time.time()
    
    times.append(end-start)
    total_times.append(end-_start)
    count.append(i)
    
    print(f'{i}, time: {end-start}, total: {end-_start}\r', end='')

_end = time.time()
print('finally:', _end-_start, 's')

plt.figure(figsize=(10, 6))
plt.plot(count, times, label='time per append (in seconds)', color='blue', alpha=0.7)
plt.plot(count, total_times, label='time (in seconds)', color='red', alpha=0.7)
plt.xlabel('Count of appends')
plt.ylabel('Time in seconds')
plt.title('Performance of bunnybase (appending to hub)')
plt.legend()
plt.grid(True)
plt.savefig('benchmark.png')
plt.show()
