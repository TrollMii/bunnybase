from bunnybase import Hub, Data, clear_bunny, read_bunny, save_as_bunny, read_bunny_history
import time

hub = Hub()

hub << Data('number', number=100)

import time
import matplotlib.pyplot as plt

times = []
total_times = []
version_count = []

_start = time.time()
for i in range(1, 100):
    start = time.time()
    save_as_bunny('test.bunny', hub)
    end = time.time()
    
    times.append(end-start)
    total_times.append(end-_start)
    version_count.append(i)
    
    print(f'{i}, time: {end-start}, total: {end-_start}\r', end='')

_end = time.time()
print('finally:', _end-_start, 's')

plt.figure(figsize=(10, 6))
plt.plot(version_count, times, label='time per save (in seconds)', color='blue', alpha=0.7)
plt.plot(version_count, total_times, label='time (in seconds)', color='red', alpha=0.7)
plt.xlabel('Count of commits')
plt.ylabel('Time in seconds')
plt.title('Performance of bunny file format (saving)')
plt.legend()
plt.grid(True)
plt.savefig('benchmark.png')
plt.show()
